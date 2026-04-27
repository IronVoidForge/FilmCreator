from pathlib import Path

import orchestrator.common as common_module
import orchestrator.core.paths as core_paths
import orchestrator.scaffold as scaffold_module
from orchestrator.reference_assets import (
    approve_reference_candidate,
    load_approved_manifest,
    load_candidates,
    load_reference_queue,
    lock_reference_candidate,
    make_reference_request,
    queue_path,
    register_reference_candidate,
    write_reference_queue,
)


def _set_projects_root(monkeypatch, tmp_path: Path) -> Path:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(core_paths, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    return projects_root


def test_register_approve_lock_updates_approved_reference_manifest(monkeypatch, tmp_path: Path) -> None:
    _set_projects_root(monkeypatch, tmp_path)
    project_slug = "demo"
    project_dir = common_module.PROJECTS_ROOT / project_slug
    prompt_path = project_dir / "03_prompt_packages" / "prepared" / "characters" / "hero" / "bust_portrait_prompt.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(
        "\n".join(
            [
                "# Title",
                "Hero Reference Prompt",
                "",
                "# ID",
                "hero_bust_portrait_prompt",
                "",
                "# Purpose",
                "Reference generation validation",
                "",
                "# Workflow Type",
                "still.t2i.klein.distilled",
                "",
                "# Positive Prompt",
                "cinematic portrait reference",
                "",
                "# Negative Prompt",
                "blurry",
                "",
                "# Inputs",
                "- subject_kind: character",
                "- subject_id: hero",
                "- source_artifact_ids: prompt_prep_index",
                "- reference_mode: canonical_reference_generation",
                "- variant_name: bust_portrait",
                "- reuse_policy: reuse canonical visual canon",
                "",
                "# Continuity Notes",
                "- keep continuity",
                "",
                "# Sources",
                "- 03_prompt_packages/prepared/PROMPT_PREPARATION_INDEX.json",
                "",
            ]
        ),
        encoding="utf-8",
    )
    request = make_reference_request(
        asset_kind="character",
        asset_id="hero",
        variant_key="bust_portrait",
        prompt_path=prompt_path,
        priority="high",
        warnings=[],
    )
    request["status"] = "prepared"
    write_reference_queue(project_dir, "character", [request])

    register_reference_candidate(
        project_slug,
        asset_kind="character",
        asset_id="hero",
        variant_key="bust_portrait",
        image_path="C:/tmp/hero.png",
    )
    candidates = load_candidates(project_dir, "character", "hero")
    candidate_id = candidates[0]["candidate_id"]

    approve_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)
    approved = load_approved_manifest(project_dir, "character")
    assert approved[0]["canonical_reference_candidate_id"] == candidate_id
    assert approved[0]["canonical_reference_image"] == "C:/tmp/hero.png"
    assert approved[0]["usable_for_downstream"] is True
    assert approved[0]["locked"] is False

    lock_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)
    approved = load_approved_manifest(project_dir, "character")
    queue = load_reference_queue(project_dir, "character")
    assert approved[0]["locked"] is True
    assert queue[0]["selected_candidate_id"] == candidate_id
    assert queue[0]["status"] == "locked"
