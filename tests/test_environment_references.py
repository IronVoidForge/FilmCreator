import json
from pathlib import Path
from types import SimpleNamespace

import orchestrator.common as common_module
import orchestrator.core.paths as core_paths
import orchestrator.scaffold as scaffold_module
from orchestrator.environment_references import run_environment_reference_generation
from orchestrator.prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from orchestrator.reference_assets import load_reference_queue


def _set_projects_root(monkeypatch, tmp_path: Path) -> Path:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(core_paths, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    return projects_root


def _write_prompt(path: Path, *, subject_id: str, variant_name: str) -> None:
    package = PromptPackage(
        path=path,
        title=f"{subject_id} prompt",
        prompt_id=f"{subject_id}_{variant_name}_prompt",
        purpose="Reference generation validation",
        workflow_type="still.t2i.klein.distilled",
        positive_prompt="wide cinematic detailed establishing environment reference",
        negative_prompt="blurry",
        inputs_markdown="\n".join(
            [
                "- subject_kind: environment",
                f"- subject_id: {subject_id}",
                "- source_artifact_ids: prompt_prep_index",
                "- reference_mode: canonical_reference_generation",
                f"- variant_name: {variant_name}",
                "- reuse_policy: reuse canonical spatial canon",
            ]
        ),
        continuity_notes_markdown="- keep continuity",
        sources_markdown="- 03_prompt_packages/prepared/PROMPT_PREPARATION_INDEX.json",
    )
    write_prompt_package(path, package)


def _write_environment_bible(project_dir: Path, environment_id: str, *, chapters: list[str], display_name: str) -> None:
    path = project_dir / "02_story_analysis" / "bibles" / "environments" / f"ENV_{environment_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "environment_id": environment_id,
                "display_name": display_name,
                "status": "canonical",
                "entity_kind": "environment",
                "role": "main",
                "landmark_descriptor": "red moss terraces and looming stone arches",
                "chapter_mentions": chapters,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def test_environment_reference_generation_filters_test_slice_by_chapters(monkeypatch, tmp_path: Path) -> None:
    _set_projects_root(monkeypatch, tmp_path)
    project_slug = "demo"
    project_dir = common_module.PROJECTS_ROOT / project_slug

    arena_prompt = project_dir / "03_prompt_packages" / "prepared" / "environments" / "arena" / "establishing_wide_prompt.md"
    city_prompt = project_dir / "03_prompt_packages" / "prepared" / "environments" / "city" / "establishing_wide_prompt.md"
    _write_prompt(arena_prompt, subject_id="arena", variant_name="establishing_wide")
    _write_prompt(city_prompt, subject_id="city", variant_name="establishing_wide")

    index_path = project_dir / "03_prompt_packages" / "prepared" / "PROMPT_PREPARATION_INDEX.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(
            [
                {
                    "subject_kind": "environment",
                    "subject_id": "arena",
                    "variant_name": "establishing_wide",
                    "status": "canonical",
                    "path": str(arena_prompt),
                    "chapter_mentions": ["CH002", "CH003"],
                },
                {
                    "subject_kind": "environment",
                    "subject_id": "city",
                    "variant_name": "establishing_wide",
                    "status": "canonical",
                    "path": str(city_prompt),
                    "chapter_mentions": ["CH006"],
                },
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    _write_environment_bible(project_dir, "arena", chapters=["CH002", "CH003"], display_name="Warhoon Arena")
    _write_environment_bible(project_dir, "city", chapters=["CH006"], display_name="Helium City")

    called_ids: list[str] = []

    def fake_run_still(**kwargs):
        called_ids.append(kwargs["asset_id"])
        return SimpleNamespace(
            manifest_path=project_dir / "logs" / f"{kwargs['asset_id']}_manifest.json",
            patched_workflow_path=project_dir / "logs" / f"{kwargs['asset_id']}_workflow.json",
            execution_ready=True,
            execute_requested=kwargs["execute"],
            blockers=[],
            warnings=[],
        )

    monkeypatch.setattr("orchestrator.environment_references.run_still", fake_run_still)

    summary = run_environment_reference_generation(
        project_slug,
        variants=["establishing_wide"],
        chapters="2-3",
        test_slice=True,
        execute=False,
    )

    queue = load_reference_queue(project_dir, "environment")
    assert called_ids == ["arena"]
    assert [entry["asset_id"] for entry in queue] == ["arena"]
    assert summary.planned_count == 1


def test_environment_generation_prompt_package_includes_reference_and_booster_metadata(monkeypatch, tmp_path: Path) -> None:
    _set_projects_root(monkeypatch, tmp_path)
    project_slug = "demo"
    project_dir = common_module.PROJECTS_ROOT / project_slug

    prompt_path = project_dir / "03_prompt_packages" / "prepared" / "environments" / "arena" / "establishing_wide_prompt.md"
    _write_prompt(prompt_path, subject_id="arena", variant_name="establishing_wide")
    index_path = project_dir / "03_prompt_packages" / "prepared" / "PROMPT_PREPARATION_INDEX.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(
            [
                {
                    "subject_kind": "environment",
                    "subject_id": "arena",
                    "variant_name": "establishing_wide",
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
    _write_environment_bible(project_dir, "arena", chapters=["CH002"], display_name="Warhoon Arena")

    generated_prompt_files: list[Path] = []

    def fake_run_still(**kwargs):
        generated_prompt_files.append(Path(kwargs["prompt_file"]))
        return SimpleNamespace(
            manifest_path=project_dir / "logs" / "arena_manifest.json",
            patched_workflow_path=project_dir / "logs" / "arena_workflow.json",
            execution_ready=True,
            execute_requested=kwargs["execute"],
            blockers=[],
            warnings=[],
        )

    monkeypatch.setattr("orchestrator.environment_references.run_still", fake_run_still)

    run_environment_reference_generation(
        project_slug,
        variants=["establishing_wide"],
        chapters="2-3",
        test_slice=True,
        execute=False,
        prompt_variant_id="environment_readability",
    )

    generated = parse_prompt_package(generated_prompt_files[0])
    assert generated.inputs["subject_kind"] == "environment"
    assert generated.inputs["subject_id"] == "arena"
    assert generated.inputs["reference_mode"] == "canonical_reference_generation"
    assert generated.inputs["variant_name"] == "establishing_wide"
    assert generated.inputs["reuse_policy"] == "reuse canonical spatial canon"
    assert generated.inputs["prompt_variant_id"] == "environment_readability"
    assert generated.inputs["booster_bundle_ids"]
    assert "positive_boosters" in generated.inputs
    assert "negative_boosters" in generated.inputs
    assert "Prompt boosters:" in generated.repair_notes_markdown
