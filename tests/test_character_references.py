import json
from pathlib import Path
from types import SimpleNamespace

import orchestrator.common as common_module
import orchestrator.core.paths as core_paths
import orchestrator.scaffold as scaffold_module
from orchestrator.character_references import run_character_reference_generation
from orchestrator.prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from orchestrator.reference_assets import load_reference_queue


def _set_projects_root(monkeypatch, tmp_path: Path) -> Path:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(core_paths, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    return projects_root


def _write_prompt(path: Path, *, subject_kind: str, subject_id: str, variant_name: str, reuse_policy: str) -> None:
    package = PromptPackage(
        path=path,
        title=f"{subject_id} prompt",
        prompt_id=f"{subject_id}_{variant_name}_prompt",
        purpose="Reference generation validation",
        workflow_type="still.t2i.klein.distilled",
        positive_prompt="cinematic detailed stable composition portrait reference",
        negative_prompt="blurry",
        inputs_markdown="\n".join(
            [
                f"- subject_kind: {subject_kind}",
                f"- subject_id: {subject_id}",
                "- source_artifact_ids: prompt_prep_index",
                "- reference_mode: canonical_reference_generation",
                f"- variant_name: {variant_name}",
                f"- reuse_policy: {reuse_policy}",
            ]
        ),
        continuity_notes_markdown="- keep continuity",
        sources_markdown="- 03_prompt_packages/prepared/PROMPT_PREPARATION_INDEX.json",
    )
    write_prompt_package(path, package)


def _write_character_bible(project_dir: Path, character_id: str, *, chapters: list[str], display_name: str) -> None:
    path = project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{character_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "character_id": character_id,
                "display_name": display_name,
                "status": "canonical",
                "entity_kind": "individual",
                "story_role": "main",
                "chapter_mentions": chapters,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def test_character_reference_generation_filters_test_slice_by_chapters(monkeypatch, tmp_path: Path) -> None:
    _set_projects_root(monkeypatch, tmp_path)
    project_slug = "demo"
    project_dir = common_module.PROJECTS_ROOT / project_slug

    hero_prompt = project_dir / "03_prompt_packages" / "prepared" / "characters" / "hero" / "bust_portrait_prompt.md"
    side_prompt = project_dir / "03_prompt_packages" / "prepared" / "characters" / "sidekick" / "bust_portrait_prompt.md"
    _write_prompt(hero_prompt, subject_kind="character", subject_id="hero", variant_name="bust_portrait", reuse_policy="reuse canonical visual canon")
    _write_prompt(side_prompt, subject_kind="character", subject_id="sidekick", variant_name="bust_portrait", reuse_policy="reuse canonical visual canon")

    index_path = project_dir / "03_prompt_packages" / "prepared" / "PROMPT_PREPARATION_INDEX.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(
            [
                {
                    "subject_kind": "character",
                    "subject_id": "hero",
                    "variant_name": "bust_portrait",
                    "status": "canonical",
                    "path": str(hero_prompt),
                    "chapter_mentions": ["CH002", "CH003"],
                },
                {
                    "subject_kind": "character",
                    "subject_id": "sidekick",
                    "variant_name": "bust_portrait",
                    "status": "canonical",
                    "path": str(side_prompt),
                    "chapter_mentions": ["CH005"],
                },
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    _write_character_bible(project_dir, "hero", chapters=["CH002", "CH003"], display_name="John Carter")
    _write_character_bible(project_dir, "sidekick", chapters=["CH005"], display_name="Tars Tarkas")

    called_ids: list[str] = []

    def fake_run_still(**kwargs):
        called_ids.append(kwargs["asset_id"])
        prompt_file = Path(kwargs["prompt_file"])
        return SimpleNamespace(
            manifest_path=project_dir / "logs" / f"{kwargs['asset_id']}_manifest.json",
            patched_workflow_path=project_dir / "logs" / f"{kwargs['asset_id']}_workflow.json",
            execution_ready=True,
            execute_requested=kwargs["execute"],
            blockers=[],
            warnings=[],
        )

    monkeypatch.setattr("orchestrator.character_references.run_still", fake_run_still)

    summary = run_character_reference_generation(
        project_slug,
        variants=["bust_portrait"],
        chapters="2-3",
        test_slice=True,
        execute=False,
    )

    queue = load_reference_queue(project_dir, "character")
    assert called_ids == ["hero"]
    assert [entry["asset_id"] for entry in queue] == ["hero"]
    assert summary.planned_count == 1


def test_character_generation_prompt_package_includes_reference_and_booster_metadata(monkeypatch, tmp_path: Path) -> None:
    _set_projects_root(monkeypatch, tmp_path)
    project_slug = "demo"
    project_dir = common_module.PROJECTS_ROOT / project_slug

    prompt_path = project_dir / "03_prompt_packages" / "prepared" / "characters" / "hero" / "bust_portrait_prompt.md"
    _write_prompt(prompt_path, subject_kind="character", subject_id="hero", variant_name="bust_portrait", reuse_policy="reuse canonical visual canon")
    index_path = project_dir / "03_prompt_packages" / "prepared" / "PROMPT_PREPARATION_INDEX.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(
            [
                {
                    "subject_kind": "character",
                    "subject_id": "hero",
                    "variant_name": "bust_portrait",
                    "status": "canonical",
                    "path": str(prompt_path),
                    "chapter_mentions": ["CH002"],
                }
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    _write_character_bible(project_dir, "hero", chapters=["CH002"], display_name="John Carter")

    generated_prompt_files: list[Path] = []

    def fake_run_still(**kwargs):
        prompt_file = Path(kwargs["prompt_file"])
        generated_prompt_files.append(prompt_file)
        return SimpleNamespace(
            manifest_path=project_dir / "logs" / "hero_manifest.json",
            patched_workflow_path=project_dir / "logs" / "hero_workflow.json",
            execution_ready=True,
            execute_requested=kwargs["execute"],
            blockers=[],
            warnings=[],
        )

    monkeypatch.setattr("orchestrator.character_references.run_still", fake_run_still)

    run_character_reference_generation(
        project_slug,
        variants=["bust_portrait"],
        chapters="2-3",
        test_slice=True,
        execute=False,
        prompt_variant_id="character_readability",
    )

    generated = parse_prompt_package(generated_prompt_files[0])
    assert generated.inputs["subject_kind"] == "character"
    assert generated.inputs["subject_id"] == "hero"
    assert generated.inputs["reference_mode"] == "canonical_reference_generation"
    assert generated.inputs["variant_name"] == "bust_portrait"
    assert generated.inputs["reuse_policy"] == "reuse canonical visual canon"
    assert generated.inputs["prompt_variant_id"] == "character_readability"
    assert generated.inputs["booster_bundle_ids"]
    assert "positive_boosters" in generated.inputs
    assert "negative_boosters" in generated.inputs
    assert "Prompt boosters:" in generated.repair_notes_markdown
