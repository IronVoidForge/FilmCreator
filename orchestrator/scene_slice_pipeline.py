from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .character_bible import run_character_bible_synthesis
from .character_taxonomy import run_character_taxonomy
from .character_visual_evidence_refinement import run_character_visual_evidence_refinement
from .core.json_io import read_json
from .environment_bible import run_environment_bible_synthesis
from .identity_refinement import run_identity_refinement
from .production_pipeline import run_story_analysis_pipeline
from .scaffold import create_project
from .scene_bindings import run_scene_binding_synthesis
from .scene_contracts import run_scene_contract_synthesis
from .shot_planner import run_shot_planning
from .visual_fallbacks import run_visual_fallback_synthesis


@dataclass(frozen=True)
class SceneSliceRunSummary:
    profile: str
    project_slug: str
    chapters: str | None
    mode: str
    completed_phases: list[str]
    phase_summaries: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "profile": self.profile,
            "project_slug": self.project_slug,
            "chapters": self.chapters,
            "mode": self.mode,
            "completed_phases": self.completed_phases,
            "phase_summaries": self.phase_summaries,
            "warnings": self.warnings,
        }


def run_scene_slice_pipeline(
    project_slug: str,
    *,
    chapter: str,
    scene: str,
    mode: str = "force",
    coverage_density: str | None = None,
) -> SceneSliceRunSummary:
    """Run a book-agnostic one-scene slice through shot packages.

    The slice keeps project-level character and environment context complete, then
    limits expensive downstream scene work to one selected scene.
    """
    _validate_mode(mode)
    chapter_id = _normalize_chapter_id(chapter)
    scene_id = _normalize_scene_slice_id(chapter_id=chapter_id, scene=scene)
    project_dir = create_project(project_slug)

    phase_summaries: dict[str, Any] = {}
    completed_phases: list[str] = []
    warnings: list[str] = [
        "Scene-slice mode ensures full story-analysis context in resume mode, builds project-wide character/environment bibles, then writes downstream outputs for the selected scene only."
    ]

    story_resume = run_story_analysis_pipeline(project_slug, chapters=None, mode="resume")
    phase_summaries["story_analysis_resume_all"] = _to_dict(story_resume)
    completed_phases.append("story_analysis_resume_all")

    if mode == "force":
        story_selected = run_story_analysis_pipeline(project_slug, chapters=chapter_id, mode="force")
        phase_summaries["story_analysis_selected_chapter"] = _to_dict(story_selected)
        completed_phases.append("story_analysis_selected_chapter")

    scene_markdown_path = _scene_markdown_path(project_dir=project_dir, scene_id=scene_id)
    if not scene_markdown_path.exists():
        raise ValueError(
            f"Selected scene {scene_id} was not found at {scene_markdown_path}. "
            "Run chapter analysis for the chapter first or choose a scene listed in the chapter scene index."
        )

    for phase_name, summary in [
        ("character_taxonomy", run_character_taxonomy(project_slug, force=mode == "force")),
        ("identity_refinement", run_identity_refinement(project_slug, use_llm=True, apply_merge=True)),
        ("character_bibles", run_character_bible_synthesis(project_slug, use_llm=True, force=mode == "force")),
        ("character_visual_evidence", run_character_visual_evidence_refinement(project_slug, force=mode == "force")),
        ("environment_bibles", run_environment_bible_synthesis(project_slug, use_llm=True, force=mode == "force")),
        ("visual_fallbacks", run_visual_fallback_synthesis(project_slug, force=mode == "force")),
    ]:
        phase_summaries[phase_name] = _to_dict(summary)
        completed_phases.append(phase_name)

    contract_summary = run_scene_contract_synthesis(
        project_slug,
        use_llm=True,
        force=mode == "force",
        chapters=chapter_id,
        scene_id=scene_id,
    )
    phase_summaries["scene_contracts"] = _to_dict(contract_summary)
    completed_phases.append("scene_contracts")
    contract_path = _scene_contract_path(project_dir=project_dir, scene_id=scene_id)
    if not contract_path.exists():
        raise ValueError(f"Scene-slice contract phase did not write the selected scene contract: {contract_path}")

    binding_summary = run_scene_binding_synthesis(
        project_slug,
        force=mode == "force",
        chapters=chapter_id,
        scene_id=scene_id,
    )
    phase_summaries["scene_bindings"] = _to_dict(binding_summary)
    completed_phases.append("scene_bindings")
    binding_path = _scene_binding_path(project_dir=project_dir, scene_id=scene_id)
    if not binding_path.exists():
        raise ValueError(f"Scene-slice binding phase did not write the selected scene binding: {binding_path}")

    scene_scope = _load_scene_prompt_scope(project_dir=project_dir, scene_id=scene_id)

    shot_summary = run_shot_planning(
        project_slug,
        use_llm=True,
        force=mode == "force",
        chapters=chapter_id,
        scene_id=scene_id,
        coverage_density=coverage_density,
    )
    phase_summaries["shot_packages"] = _to_dict(shot_summary)
    completed_phases.append("shot_packages")
    shot_files = _scene_shot_package_files(project_dir=project_dir, scene_id=scene_id)
    if not shot_files:
        raise ValueError(f"Scene-slice shot phase did not write any shot packages for {scene_id}.")

    phase_summaries["scene_slice"] = {
        "chapter_id": chapter_id,
        "scene_id": scene_id,
        "through_phase": "shot_packages",
        "prompt_scope": scene_scope,
        "shot_package_count": len(shot_files),
        "shot_package_paths": [str(path) for path in shot_files],
        "later_phases": [
            "dialogue_timeline",
            "descriptor_enrichment",
            "prompt_preparation",
            "character_references",
            "environment_references",
        ],
    }

    return SceneSliceRunSummary(
        profile="scene_slice",
        project_slug=project_slug,
        chapters=chapter_id,
        mode=mode,
        completed_phases=completed_phases,
        phase_summaries=phase_summaries,
        warnings=warnings,
    )


def _load_scene_prompt_scope(*, project_dir: Path, scene_id: str) -> dict[str, Any]:
    chapter_id = scene_id[:5]
    binding_path = _scene_binding_path(project_dir=project_dir, scene_id=scene_id)
    contract_path = _scene_contract_path(project_dir=project_dir, scene_id=scene_id)
    binding = read_json(binding_path) if binding_path.exists() else {}
    contract = read_json(contract_path) if contract_path.exists() else {}

    character_ids = _scene_character_ids(binding)
    environment_ids = _scene_environment_ids(binding)
    return {
        "scene_id": scene_id,
        "chapter_id": chapter_id,
        "character_ids": character_ids,
        "environment_ids": environment_ids,
        "scene_contract_path": str(contract_path) if contract_path.exists() else "",
        "scene_binding_path": str(binding_path) if binding_path.exists() else "",
        "scene_title": contract.get("scene_title") or contract.get("summary") or scene_id,
}


def _scene_markdown_path(*, project_dir: Path, scene_id: str) -> Path:
    chapter_id = scene_id[:5]
    return project_dir / "02_story_analysis" / "scene_breakdowns" / "chapters" / chapter_id / f"{scene_id}.md"


def _scene_contract_path(*, project_dir: Path, scene_id: str) -> Path:
    chapter_id = scene_id[:5]
    return project_dir / "02_story_analysis" / "contracts" / "scenes" / chapter_id / f"{scene_id}.json"


def _scene_binding_path(*, project_dir: Path, scene_id: str) -> Path:
    chapter_id = scene_id[:5]
    return project_dir / "02_story_analysis" / "contracts" / "scene_bindings" / chapter_id / f"{scene_id}_BINDINGS.json"


def _scene_shot_package_files(*, project_dir: Path, scene_id: str) -> list[Path]:
    chapter_id = scene_id[:5]
    shot_dir = project_dir / "02_story_analysis" / "shot_packages" / chapter_id / scene_id
    if not shot_dir.exists():
        return []
    return sorted(path for path in shot_dir.glob(f"{scene_id}_SH*.json") if path.is_file())


def _scene_character_ids(binding: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    for item in binding.get("resolved_characters", []):
        if not isinstance(item, dict):
            continue
        canonical_id = str(item.get("canonical_id") or "").strip()
        status = str(item.get("status") or "").strip().lower()
        if canonical_id and canonical_id.lower() not in {"none", "null", "n/a"} and status != "unresolved":
            ids.append(canonical_id)
    return _ordered_unique(ids)


def _scene_environment_ids(binding: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    resolved = binding.get("resolved_environment")
    if isinstance(resolved, dict):
        canonical_id = str(resolved.get("canonical_id") or "").strip()
        if canonical_id and canonical_id.lower() not in {"none", "null", "n/a"}:
            ids.append(canonical_id)
    for item in binding.get("beat_environment_overrides", []):
        if not isinstance(item, dict):
            continue
        env = item.get("environment")
        if isinstance(env, dict):
            canonical_id = str(env.get("canonical_id") or "").strip()
            if canonical_id and canonical_id.lower() not in {"none", "null", "n/a"}:
                ids.append(canonical_id)
    return _ordered_unique(ids)


def _ordered_unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(value)
    return ordered


def _normalize_chapter_id(chapter: str) -> str:
    text = str(chapter or "").strip().upper()
    if text.startswith("CH") and text[2:].isdigit():
        return f"CH{int(text[2:]):03d}"
    if text.isdigit():
        return f"CH{int(text):03d}"
    raise ValueError(f"Invalid chapter selector for scene slice: {chapter!r}")


def _normalize_scene_slice_id(*, chapter_id: str, scene: str) -> str:
    text = str(scene or "").strip().upper()
    prefix = f"{chapter_id}_SC"
    if text.startswith(prefix) and text.removeprefix(prefix).isdigit():
        return f"{chapter_id}_SC{int(text.removeprefix(prefix)):03d}"
    if text.startswith("SC") and text[2:].isdigit():
        return f"{chapter_id}_SC{int(text[2:]):03d}"
    if text.isdigit():
        return f"{chapter_id}_SC{int(text):03d}"
    raise ValueError(f"Invalid scene selector for scene slice: {scene!r}")


def _validate_mode(mode: str) -> None:
    if mode not in {"resume", "force"}:
        raise ValueError(f"Unsupported run mode: {mode}")


def _to_dict(summary: Any) -> dict[str, Any]:
    if hasattr(summary, "to_dict"):
        return summary.to_dict()
    if isinstance(summary, dict):
        return summary
    return {"result": str(summary)}
