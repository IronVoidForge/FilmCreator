from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..common import ROOT, ensure_dir, read_json, write_json
from ..scaffold import create_clip, create_project, create_scene
from ..state import load_clip_state, path_to_manifest_value, record_clip_run, resolve_continuity_source, resolve_user_path
from ..workflow_patcher import WorkflowPatchError, detect_workflow_format, load_workflow_payload, patch_workflow_payload, prune_api_prompt_to_output_nodes
from ..prompt_package import PromptPackage, parse_prompt_package
from ..comfy_client import ComfyClient
from ..settings import RuntimeSettings, load_runtime_settings
from ..registry_loader import get_workflow, load_registry
from ..delete_safety import remove_path_within_project


STAGE_DIR_BY_STAGE = {
    "scene_build": "scene_build",
    "scene_refinement": "scene_build",
    "scene_build_two_ref": "scene_build",
    "scene_refinement_two_ref": "scene_build",
    "keyframe": "keyframes",
    "still_fix": "fixes",
    "anchor_frame": "anchor_frames",
    "interval_frame": "interval_frames",
}

ASSET_CODE_BY_STAGE = {
    "scene_build": "SB",
    "scene_refinement": "SB",
    "scene_build_two_ref": "SB",
    "scene_refinement_two_ref": "SB",
    "keyframe": "KF",
    "still_fix": "FX",
    "cut_motion": "MV",
    "anchor_frame": "AF",
    "interval_frame": "IF",
}

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}


@dataclass(frozen=True)
class RunSummary:
    stage: str
    workflow_id: str
    workflow_format: str
    execution_ready: bool
    execute_requested: bool
    manifest_path: Path
    patched_workflow_path: Path
    output_root: Path
    prompt_file: Path
    continuity_source: str | None
    resolved_refs: dict[str, str]
    comfy_input_refs: dict[str, str]
    blockers: list[str]
    warnings: list[str]
    comfy_base_url: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage": self.stage,
            "workflow_id": self.workflow_id,
            "workflow_format": self.workflow_format,
            "execution_ready": self.execution_ready,
            "execute_requested": self.execute_requested,
            "manifest_path": path_to_manifest_value(self.manifest_path),
            "patched_workflow_path": path_to_manifest_value(self.patched_workflow_path),
            "output_root": path_to_manifest_value(self.output_root),
            "prompt_file": path_to_manifest_value(self.prompt_file),
            "continuity_source": self.continuity_source,
            "resolved_refs": self.resolved_refs,
            "comfy_input_refs": self.comfy_input_refs,
            "blockers": self.blockers,
            "warnings": self.warnings,
            "comfy_base_url": self.comfy_base_url,
        }


@dataclass(frozen=True)
class PreparedRun:
    workflow: dict[str, Any]
    workflow_payload: dict[str, Any]
    workflow_format: str
    manifest_path: Path
    patched_workflow_path: Path
    output_root: Path
    output_scope: str
    output_name_pattern: str
    prompt_package: PromptPackage
    prompt_file: Path
    project_slug: str
    scene_id: str | None
    clip_id: str | None
    stage: str
    asset_id: str | None
    asset_family: str | None
    resolved_refs: dict[str, str]
    comfy_input_refs: dict[str, str]
    continuity_source: str | None
    blockers: list[str]
    warnings: list[str]
    save_prefix: str
    settings: RuntimeSettings


def run_still(
    *,
    project_slug: str,
    stage: str,
    prompt_file: str,
    workflow_id: str | None = None,
    scene_id: str | None = None,
    clip_id: str | None = None,
    asset_id: str | None = None,
    ref_args: list[str] | None = None,
    seed: int | None = None,
    execute: bool = False,
) -> RunSummary:
    settings = load_runtime_settings()
    prepared = prepare_still_run(
        project_slug=project_slug,
        stage=stage,
        prompt_file=prompt_file,
        workflow_id=workflow_id,
        scene_id=scene_id,
        clip_id=clip_id,
        asset_id=asset_id,
        ref_args=ref_args or [],
        seed=seed,
        settings=settings,
    )

    if execute:
        if prepared.blockers:
            blocker_text = "; ".join(prepared.blockers)
            raise RuntimeError(f"Run is not execution-ready: {blocker_text}")
        _execute_prepared_run(prepared)

    return _summary_from_prepared(prepared, execute_requested=execute)


def prepare_still_run(
    *,
    project_slug: str,
    stage: str,
    prompt_file: str,
    workflow_id: str | None,
    scene_id: str | None,
    clip_id: str | None,
    asset_id: str | None,
    ref_args: list[str],
    seed: int | None,
    settings: RuntimeSettings,
    record_clip_run_entry: bool = True,
) -> PreparedRun:
    workflow = _resolve_workflow(stage, workflow_id)
    _validate_stage(workflow, stage)

    prompt_path = _resolve_existing_path(prompt_file)
    prompt_package = parse_prompt_package(prompt_path)
    if prompt_package.workflow_type != workflow["id"]:
        raise ValueError(
            f"Prompt package workflow type '{prompt_package.workflow_type}' does not match workflow '{workflow['id']}'"
        )

    output_root, asset_family = _resolve_scope(
        project_slug=project_slug,
        workflow=workflow,
        stage=stage,
        scene_id=scene_id,
        clip_id=clip_id,
        asset_id=asset_id,
    )

    raw_ref_map = _parse_ref_args(ref_args)
    resolved_refs, continuity_source, ref_warnings = _resolve_stage_refs(
        workflow=workflow,
        stage=stage,
        prompt_package=prompt_package,
        raw_ref_map=raw_ref_map,
        project_slug=project_slug,
        scene_id=scene_id,
        clip_id=clip_id,
    )

    from ..scaffold import create_run_manifest

    manifest_path = create_run_manifest(
        project_slug=project_slug,
        workflow_id=workflow["id"],
        stage=stage,
        prompt_file=path_to_manifest_value(prompt_path),
        scene_id=scene_id,
        clip_id=clip_id,
        input_refs=list(resolved_refs.values()),
        seed=seed,
    )
    run_id = manifest_path.stem
    save_prefix = f"filmcreator/{project_slug}/{run_id}_{stage}"
    comfy_input_refs = _plan_comfy_input_refs(run_id, resolved_refs)

    workflow_path = ROOT / workflow["filename"]
    workflow_payload = load_workflow_payload(workflow_path)
    workflow_format = detect_workflow_format(workflow_payload)

    blockers: list[str] = []
    warnings: list[str] = list(ref_warnings)
    patch_error: str | None = None
    if prompt_package.negative_prompt and "negative_prompt" not in workflow.get("patch_points", {}):
        warnings.append(
            "Negative Prompt is present, but the registry does not yet declare a negative_prompt patch point."
        )

    try:
        patched_workflow = patch_workflow_payload(
            workflow_payload,
            workflow,
            prompt_text=prompt_package.positive_prompt or None,
            negative_prompt=prompt_package.negative_prompt if "negative_prompt" in workflow.get("patch_points", {}) else None,
            save_prefix=save_prefix,
            seed=seed,
            source_images=comfy_input_refs or None,
        )
        preferred_output_nodes = workflow.get("preferred_output_nodes", [])
        if workflow_format == "api_prompt" and preferred_output_nodes:
            patched_workflow = prune_api_prompt_to_output_nodes(patched_workflow, preferred_output_nodes)
    except WorkflowPatchError as exc:
        patch_error = str(exc)
        patched_workflow = workflow_payload
        blockers.append(f"workflow patching failed: {exc}")

    if workflow_format != "api_prompt":
        blockers.append(
            "workflow is not in ComfyUI API prompt format. Re-export it with File -> Export (API) or add a conversion step."
        )

    patched_workflow_path = manifest_path.parent / f"{run_id}_patched_workflow.json"
    ensure_dir(patched_workflow_path.parent)
    patched_workflow_path.write_text(json.dumps(patched_workflow, indent=2) + "\n", encoding="utf-8")

    manifest = read_json(manifest_path)
    manifest["status"] = "prepared"
    manifest["prompt_package"] = prompt_package.to_manifest_dict()
    manifest["input_ref_map"] = resolved_refs
    manifest["comfy_input_ref_map"] = comfy_input_refs
    manifest["continuity_source"] = continuity_source
    manifest["output_root"] = path_to_manifest_value(output_root)
    manifest["patched_workflow_file"] = path_to_manifest_value(patched_workflow_path)
    manifest["workflow_file"] = workflow["filename"]
    manifest["workflow_format"] = workflow_format
    manifest["key_settings"] = {
        "seed": seed,
        "save_prefix": save_prefix,
        "comfy_base_url": settings.comfy_base_url,
    }
    manifest["warnings"] = warnings
    manifest["blockers"] = blockers
    if patch_error:
        manifest["patch_error"] = patch_error
    write_json(manifest_path, manifest)

    if record_clip_run_entry and workflow["output_scope"] == "clip" and scene_id and clip_id:
        record_clip_run(
            project_slug,
            scene_id,
            clip_id,
            stage=stage,
            manifest_path=manifest_path,
            prompt_file=prompt_path,
        )

    return PreparedRun(
        workflow=workflow,
        workflow_payload=patched_workflow,
        workflow_format=workflow_format,
        manifest_path=manifest_path,
        patched_workflow_path=patched_workflow_path,
        output_root=output_root,
        output_scope=workflow["output_scope"],
        output_name_pattern=workflow["output_name_pattern"],
        prompt_package=prompt_package,
        prompt_file=prompt_path,
        project_slug=project_slug,
        scene_id=scene_id,
        clip_id=clip_id,
        stage=stage,
        asset_id=asset_id,
        asset_family=asset_family,
        resolved_refs=resolved_refs,
        comfy_input_refs=comfy_input_refs,
        continuity_source=continuity_source,
        blockers=blockers,
        warnings=warnings,
        save_prefix=save_prefix,
        settings=settings,
    )


def execute_prepared_run(prepared: PreparedRun) -> None:
    _execute_prepared_run(prepared)


def _summary_from_prepared(prepared: PreparedRun, *, execute_requested: bool) -> RunSummary:
    return RunSummary(
        stage=prepared.stage,
        workflow_id=prepared.workflow["id"],
        workflow_format=prepared.workflow_format,
        execution_ready=not prepared.blockers,
        execute_requested=execute_requested,
        manifest_path=prepared.manifest_path,
        patched_workflow_path=prepared.patched_workflow_path,
        output_root=prepared.output_root,
        prompt_file=prepared.prompt_file,
        continuity_source=prepared.continuity_source,
        resolved_refs=prepared.resolved_refs,
        comfy_input_refs=prepared.comfy_input_refs,
        blockers=prepared.blockers,
        warnings=prepared.warnings,
        comfy_base_url=prepared.settings.comfy_base_url,
    )


def _execute_prepared_run(prepared: PreparedRun) -> None:
    if prepared.workflow_format != "api_prompt":
        raise RuntimeError(
            "The prepared workflow is not in API prompt format, so it cannot be sent to /prompt yet."
        )

    prompt_id: str | None = None
    comfy_outputs: list[dict[str, str]] = []

    try:
        _stage_input_refs(prepared)

        client = ComfyClient(
            prepared.settings.comfy_base_url,
            timeout_seconds=prepared.settings.comfy_timeout_seconds,
        )
        submission = client.submit_prompt(prepared.workflow_payload)

        manifest = read_json(prepared.manifest_path)
        prompt_id = submission["prompt_id"]
        manifest["status"] = "submitted"
        manifest["comfy_prompt_id"] = prompt_id
        write_json(prepared.manifest_path, manifest)

        history_entry = client.wait_for_completion(
            prompt_id,
            poll_interval_seconds=prepared.settings.comfy_poll_interval_seconds,
            timeout_seconds=prepared.settings.comfy_timeout_seconds,
        )
        comfy_outputs = client.collect_history_outputs(history_entry)
        if not comfy_outputs:
            raise RuntimeError(f"ComfyUI prompt {prompt_id} completed without any saved routed outputs.")

        from ..runner import _route_outputs as route_outputs

        routed_outputs = route_outputs(prepared, comfy_outputs)
    except Exception as exc:
        manifest = read_json(prepared.manifest_path)
        manifest["status"] = "failed"
        manifest["error"] = str(exc)
        if prompt_id:
            manifest["comfy_prompt_id"] = prompt_id
        error_details = getattr(exc, "details", None)
        if error_details:
            manifest["error_details"] = error_details
        write_json(prepared.manifest_path, manifest)

        if not prepared.settings.keep_staged_files:
            _cleanup_staged_files(prepared, comfy_outputs)
        raise

    if not prepared.settings.keep_staged_files:
        _cleanup_staged_files(prepared, comfy_outputs)

    manifest = read_json(prepared.manifest_path)
    manifest["status"] = "completed"
    manifest["output_files"] = [path_to_manifest_value(path) for path in routed_outputs]
    manifest["comfy_outputs"] = comfy_outputs
    write_json(prepared.manifest_path, manifest)


def _resolve_workflow(stage: str, workflow_id: str | None) -> dict[str, Any]:
    if workflow_id:
        return get_workflow(workflow_id)

    if stage == "cut_motion":
        return get_workflow("video.cut_motion.wan.i2v")

    matches = [workflow for workflow in load_registry()["workflows"] if stage in workflow["supported_stages"]]
    if not matches:
        raise KeyError(f"No workflow is registered for stage '{stage}'")
    if len(matches) > 1:
        workflow_ids = ", ".join(sorted(workflow["id"] for workflow in matches))
        raise ValueError(
            f"Stage '{stage}' matches multiple workflows ({workflow_ids}); pass --workflow-id explicitly"
        )
    return matches[0]


def _validate_stage(workflow: dict[str, Any], stage: str) -> None:
    if stage not in workflow["supported_stages"]:
        raise ValueError(f"Workflow '{workflow['id']}' does not support stage '{stage}'")


def _resolve_scope(
    *,
    project_slug: str,
    workflow: dict[str, Any],
    stage: str,
    scene_id: str | None,
    clip_id: str | None,
    asset_id: str | None,
) -> tuple[Path, str | None]:
    project_root = create_project(project_slug)

    if workflow["output_scope"] == "project":
        if not asset_id:
            raise ValueError("Project-scoped still runs require --asset-id")
        asset_family = _asset_family_for_stage(stage)
        output_root = project_root / "04_references" / asset_family / asset_id
        ensure_dir(output_root)
        return output_root, asset_family

    if workflow["output_scope"] == "scene":
        if not scene_id:
            raise ValueError("Scene-scoped still runs require --scene")
        return create_scene(project_slug, scene_id), None

    if not scene_id or not clip_id:
        raise ValueError("Clip-scoped still runs require both --scene and --clip")
    clip_root = create_clip(project_slug, scene_id, clip_id)
    if stage == "cut_motion":
        output_root = clip_root / "video"
    else:
        output_root = clip_root / "stills" / STAGE_DIR_BY_STAGE[stage]
    ensure_dir(output_root)
    return output_root, None


def _asset_family_for_stage(stage: str) -> str:
    if stage in {"character_reference", "character_reference_variant"}:
        return "characters"
    if stage in {"environment_reference", "environment_reference_variant"}:
        return "environments"
    raise ValueError(f"Could not infer project asset family for stage '{stage}'")


def _parse_ref_args(ref_args: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for item in ref_args:
        if "=" not in item:
            raise ValueError(f"Reference '{item}' must use slot=path syntax")
        slot, value = item.split("=", 1)
        slot = _canonicalize_ref_slot(slot.strip())
        value = value.strip()
        if not slot or not value:
            raise ValueError(f"Reference '{item}' must use slot=path syntax")
        parsed[slot] = path_to_manifest_value(_resolve_existing_path(value))
    return parsed


def _resolve_stage_refs(
    *,
    workflow: dict[str, Any],
    stage: str,
    prompt_package: PromptPackage,
    raw_ref_map: dict[str, str],
    project_slug: str,
    scene_id: str | None,
    clip_id: str | None,
) -> tuple[dict[str, str], str | None, list[str]]:
    required_slots = {slot["slot"] for slot in workflow.get("required_image_slots", [])}
    optional_slots = {slot["slot"] for slot in workflow.get("optional_image_slots", [])}
    allowed_slots = required_slots | optional_slots

    unknown_slots = sorted(set(raw_ref_map) - allowed_slots)
    if unknown_slots:
        unknown_text = ", ".join(unknown_slots)
        raise ValueError(f"Unknown image slots for workflow '{workflow['id']}': {unknown_text}")

    resolved = dict(raw_ref_map)
    continuity_source: str | None = None
    warnings: list[str] = []

    if stage == "still_fix" and "image1" in required_slots and "image1" not in resolved:
        fix_of = prompt_package.inputs.get("fix_of")
        if _is_image_reference(fix_of):
            resolved["image1"] = fix_of
            warnings.append("No image1 ref was provided, so the runner will use Inputs -> fix_of as the still-fix base image.")
        elif scene_id and clip_id:
            clip_state = load_clip_state(project_slug, scene_id, clip_id)
            approved_assets = clip_state.get("approved_assets", {})
            latest_review = clip_state.get("latest_review_decision") or {}
            fallback_candidates = [
                approved_assets.get("still_fixes", [])[-1] if approved_assets.get("still_fixes") else "",
                approved_assets.get("approved_keyframe"),
                approved_assets.get("golden_frame"),
                clip_state.get("current_continuity_source"),
                clip_state.get("approved_video_last_frame"),
                latest_review.get("chosen_primary"),
            ]
            fallback_fix_of = next((candidate for candidate in fallback_candidates if _is_image_reference(candidate)), "")
            if fallback_fix_of:
                resolved["image1"] = fallback_fix_of
                warnings.append(
                    "No image1 ref was provided, so the runner will use the latest approved still-compatible image "
                    "as the still-fix base image."
                )

    if "image1" in required_slots and "image1" not in resolved:
        if not scene_id or not clip_id:
            raise ValueError("Continuation stages require --scene and --clip to resolve image1 from state")
        continuity = resolve_continuity_source(project_slug, scene_id, clip_id)
        continuity_source = continuity.path
        resolved["image1"] = continuity.path
    elif "image1" in resolved:
        continuity_source = resolved["image1"]

    if "image2" in optional_slots and "image2" not in resolved and continuity_source:
        resolved["image2"] = continuity_source
        warnings.append(
            "No image2 ref was provided, so the runner will reuse the resolved continuity source for that slot."
        )

    if stage == "keyframe":
        if "image3" in optional_slots and "image3" not in resolved and "image2" in resolved:
            resolved["image3"] = resolved["image2"]
            warnings.append(
                "No image3 ref was provided, so the runner will duplicate image2 for that optional slot."
            )

        if "image4" in optional_slots and "image4" not in resolved:
            continuity = None
            if scene_id and clip_id:
                try:
                    continuity = resolve_continuity_source(project_slug, scene_id, clip_id)
                except ValueError:
                    continuity = None
            if continuity is not None:
                continuity_source = continuity_source or continuity.path
                resolved["image4"] = continuity.path
                warnings.append(
                    "No image4 continuity ref was provided, so the runner will reuse the resolved continuity source for that slot."
                )
            elif "image1" in resolved:
                resolved["image4"] = resolved["image1"]
                warnings.append(
                    "No image4 ref was provided, so the runner will duplicate image1 for that optional slot."
                )

    remaining_optional = sorted(optional_slots - set(resolved))
    if remaining_optional:
        warnings.append(
            "Optional image slots were not provided: "
            + ", ".join(remaining_optional)
            + ". If the workflow export still contains baked-in example filenames for those nodes, live execution may need explicit refs."
        )

    missing = sorted(required_slots - set(resolved))
    if missing:
        missing_text = ", ".join(missing)
        raise ValueError(f"Missing required image refs for workflow '{workflow['id']}': {missing_text}")

    for slot, value in resolved.items():
        path = resolve_user_path(value)
        if not path.exists():
            raise FileNotFoundError(f"Resolved image ref for slot '{slot}' does not exist: {path}")

    return resolved, continuity_source, warnings


def _resolve_existing_path(value: str) -> Path:
    path = resolve_user_path(value)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    return path


def _next_version(directory: Path) -> int:
    highest = 0
    for path in directory.glob("*"):
        match = re.search(r"_v(\d+)\.", path.name)
        if match:
            highest = max(highest, int(match.group(1)))
    return highest + 1


def _next_index(directory: Path, asset_code: str | None) -> int:
    if not asset_code:
        return 1

    highest = 0
    pattern = re.compile(rf"_{re.escape(asset_code)}(\d+)")
    for path in directory.glob("*"):
        match = pattern.search(path.stem)
        if match:
            highest = max(highest, int(match.group(1)))
    return highest + 1


def _plan_comfy_input_refs(run_id: str, resolved_refs: dict[str, str]) -> dict[str, str]:
    staged: dict[str, str] = {}
    for slot, source in resolved_refs.items():
        source_path = resolve_user_path(source)
        safe_name = source_path.name.replace(" ", "_")
        staged[slot] = f"filmcreator/{run_id}/{slot}_{safe_name}"
    return staged


def _stage_input_refs(prepared) -> None:
    for slot, staged_name in prepared.comfy_input_refs.items():
        source = resolve_user_path(prepared.resolved_refs[slot])
        destination = prepared.settings.comfy_input_dir / Path(staged_name)
        ensure_dir(destination.parent)
        shutil.copy2(source, destination)


def _cleanup_staged_files(prepared, comfy_outputs: list[dict[str, str]]) -> None:
    project_root = create_project(prepared.project_slug).resolve()
    for staged_name in prepared.comfy_input_refs.values():
        path = prepared.settings.comfy_input_dir / Path(staged_name)
        try:
            if path.exists():
                remove_path_within_project(path, project_root=project_root)
            if path.parent.resolve() == project_root or project_root in path.parent.resolve().parents:
                _remove_empty_parents(path.parent, prepared.settings.comfy_input_dir)
        except ValueError:
            continue

    for output in comfy_outputs:
        path = _resolve_comfy_output_source(prepared, output)
        try:
            if path.exists():
                remove_path_within_project(path, project_root=project_root)
            if path.parent.resolve() == project_root or project_root in path.parent.resolve().parents:
                _remove_empty_parents(path.parent, prepared.settings.comfy_output_dir)
        except ValueError:
            continue


def _resolve_comfy_output_source(prepared, output: dict[str, str]) -> Path:
    fullpath = output.get("fullpath", "")
    if fullpath:
        candidate = Path(fullpath)
        if candidate.exists():
            return candidate
    return prepared.settings.comfy_output_dir / output.get("subfolder", "") / output["filename"]


def _remove_empty_parents(path: Path, stop_at: Path) -> None:
    stop = stop_at.resolve()
    try:
        path.resolve().relative_to(stop)
    except ValueError:
        return

    current = path
    while current.exists() and current.is_dir():
        if current.resolve() == stop:
            return
        try:
            current.rmdir()
        except OSError:
            return
        current = current.parent


def _is_image_reference(value: str | None) -> bool:
    if not value:
        return False
    return Path(value).suffix.lower() in IMAGE_SUFFIXES


def _canonicalize_ref_slot(slot: str) -> str:
    normalized = slot.strip()
    aliases = {
        "source_frame": "image1",
        "continuity_ref": "image2",
        "image_1": "image1",
        "image_2": "image2",
        "image_3": "image3",
        "image_4": "image4",
    }
    return aliases.get(normalized, normalized)
