from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

from orchestrator import common as common_module
from orchestrator import scaffold as scaffold_module
from orchestrator import world_global as world_global_module
from orchestrator import world_refinement as world_refinement_module


def _seed_character_entry(*, canonical_id: str, display_name: str, chapter_id: str) -> dict:
    return {
        "canonical_id": canonical_id,
        "display_name": display_name,
        "status": "canonical",
        "entity_kind": "individual",
        "aliases": [canonical_id],
        "alias_history": [],
        "first_seen_chapter": chapter_id,
        "last_seen_chapter": chapter_id,
        "chapter_mentions": [chapter_id],
        "sources": [f"projects/demo/02_story_analysis/character_breakdowns/chapters/{chapter_id}/{canonical_id}.md"],
        "source_history": [],
        "open_questions": [],
        "resolution_reason": "",
        "resolved_to": None,
        "resolution_history": [],
        "description_layers": {
            "initial_extracted": [],
            "stable_canonical": [],
            "chapter_specific": {},
        },
    }


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def test_refine_world_dry_run_writes_artifacts_without_mutating_registries(tmp_path, monkeypatch) -> None:
    repo_root = tmp_path
    project_dir = repo_root / "projects" / "demo"
    global_dir = project_dir / "02_story_analysis" / "world" / "global"
    global_dir.mkdir(parents=True, exist_ok=True)

    character_registry = {
        "woola": _seed_character_entry(canonical_id="woola", display_name="woola", chapter_id="CH004"),
        "woola_ch008": _seed_character_entry(canonical_id="woola_ch008", display_name="woola", chapter_id="CH008"),
    }
    _write_json(global_dir / "CHARACTER_REGISTRY_GLOBAL.json", character_registry)
    _write_json(global_dir / "ENVIRONMENT_REGISTRY_GLOBAL.json", {})
    _write_json(global_dir / "CHARACTER_DIRECTORY.json", {})
    _write_json(global_dir / "ENVIRONMENT_DIRECTORY.json", {})

    monkeypatch.setattr(common_module, "ROOT", repo_root)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", repo_root / "projects")
    monkeypatch.setattr(scaffold_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_global_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_refinement_module, "create_project", lambda project_slug: project_dir)

    summary = world_refinement_module.refine_world_identities(
        project_slug="demo",
        use_llm=False,
        apply_changes=False,
    )

    assert summary.project_slug == "demo"
    assert summary.candidate_count == 1
    assert summary.comparison_count == 1
    assert summary.applied_count == 0
    assert summary.human_review_count == 1

    result_path = project_dir / "02_story_analysis" / "world" / "refinement" / "REFINEMENT_RESULT.json"
    decisions_path = project_dir / "02_story_analysis" / "world" / "refinement" / "REFINEMENT_DECISIONS.json"
    assert result_path.exists()
    assert decisions_path.exists()

    after_registry = json.loads((global_dir / "CHARACTER_REGISTRY_GLOBAL.json").read_text(encoding="utf-8"))
    assert after_registry == character_registry


def test_refine_world_applies_safe_merge_and_preserves_provenance(tmp_path, monkeypatch) -> None:
    repo_root = tmp_path
    project_dir = repo_root / "projects" / "demo"
    global_dir = project_dir / "02_story_analysis" / "world" / "global"
    global_dir.mkdir(parents=True, exist_ok=True)

    target = _seed_character_entry(canonical_id="woola", display_name="woola", chapter_id="CH004")
    subject = _seed_character_entry(canonical_id="woola_ch008", display_name="woola", chapter_id="CH008")
    target["aliases"] = ["woola"]
    subject["aliases"] = ["woola_ch008"]
    character_registry = {
        "woola": target,
        "woola_ch008": subject,
    }
    _write_json(global_dir / "CHARACTER_REGISTRY_GLOBAL.json", character_registry)
    _write_json(global_dir / "ENVIRONMENT_REGISTRY_GLOBAL.json", {})
    _write_json(global_dir / "CHARACTER_DIRECTORY.json", {})
    _write_json(global_dir / "ENVIRONMENT_DIRECTORY.json", {})

    class _FakeLMStudioClient:
        def __init__(self, settings) -> None:
            self.settings = settings

        def chat_completion_result(self, *, system_prompt, user_prompt, temperature, model=None):
            return SimpleNamespace(
                is_success=True,
                text=json.dumps(
                    {
                        "entity_type": "character",
                        "subject_ids": ["woola", "woola_ch008"],
                        "action": "merge_into_existing",
                        "target_id": "woola",
                        "new_canonical_id": None,
                        "new_entity_kind": None,
                        "reason": "chapter-suffixed duplicate",
                        "confidence": "high",
                        "requires_human_review": False,
                    }
                ),
                error_message=None,
            )

    monkeypatch.setattr(common_module, "ROOT", repo_root)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", repo_root / "projects")
    monkeypatch.setattr(scaffold_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_global_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_refinement_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_refinement_module, "LMStudioClient", _FakeLMStudioClient)
    monkeypatch.setattr(
        world_refinement_module,
        "load_runtime_settings",
        lambda: SimpleNamespace(
            lmstudio_base_url="http://127.0.0.1:1234/v1",
            lmstudio_model=None,
            lmstudio_timeout_seconds=1.0,
        ),
    )

    summary = world_refinement_module.refine_world_identities(
        project_slug="demo",
        use_llm=True,
        apply_changes=True,
    )

    assert summary.candidate_count == 1
    assert summary.applied_count == 1

    updated_registry = json.loads((global_dir / "CHARACTER_REGISTRY_GLOBAL.json").read_text(encoding="utf-8"))
    updated_directory = json.loads((global_dir / "CHARACTER_DIRECTORY.json").read_text(encoding="utf-8"))

    assert updated_registry["woola"]["aliases"]
    assert "woola_ch008" in updated_registry["woola"]["aliases"]
    assert updated_registry["woola_ch008"]["status"] == "resolved_into"
    assert updated_registry["woola_ch008"]["resolved_to"] == "woola"
    assert updated_directory["woola"]["canonical_id"] == "woola"
    assert updated_directory["woola_ch008"]["resolved_to"] == "woola"


def test_refine_world_retries_empty_completion_once(tmp_path, monkeypatch) -> None:
    repo_root = tmp_path
    project_dir = repo_root / "projects" / "demo"
    global_dir = project_dir / "02_story_analysis" / "world" / "global"
    global_dir.mkdir(parents=True, exist_ok=True)

    character_registry = {
        "woola": _seed_character_entry(canonical_id="woola", display_name="woola", chapter_id="CH004"),
        "woola_ch008": _seed_character_entry(canonical_id="woola_ch008", display_name="woola", chapter_id="CH008"),
    }
    _write_json(global_dir / "CHARACTER_REGISTRY_GLOBAL.json", character_registry)
    _write_json(global_dir / "ENVIRONMENT_REGISTRY_GLOBAL.json", {})
    _write_json(global_dir / "CHARACTER_DIRECTORY.json", {})
    _write_json(global_dir / "ENVIRONMENT_DIRECTORY.json", {})

    calls: list[str] = []

    class _RetryingLMStudioClient:
        def __init__(self, settings) -> None:
            self.settings = settings

        def chat_completion_result(self, *, system_prompt, user_prompt, temperature, model=None):
            calls.append(user_prompt)
            if len(calls) == 1:
                return SimpleNamespace(is_success=True, text="", error_message="empty")
            return SimpleNamespace(
                is_success=True,
                text=json.dumps(
                    {
                        "entity_type": "character",
                        "subject_ids": ["woola", "woola_ch008"],
                        "action": "merge_into_existing",
                        "target_id": "woola",
                        "new_canonical_id": None,
                        "new_entity_kind": None,
                        "reason": "chapter-suffixed duplicate",
                        "confidence": "high",
                        "requires_human_review": False,
                    }
                ),
                error_message=None,
            )

    monkeypatch.setattr(common_module, "ROOT", repo_root)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", repo_root / "projects")
    monkeypatch.setattr(scaffold_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_global_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_refinement_module, "create_project", lambda project_slug: project_dir)
    monkeypatch.setattr(world_refinement_module, "LMStudioClient", _RetryingLMStudioClient)
    monkeypatch.setattr(
        world_refinement_module,
        "load_runtime_settings",
        lambda: SimpleNamespace(
            lmstudio_base_url="http://127.0.0.1:1234/v1",
            lmstudio_model=None,
            lmstudio_timeout_seconds=1.0,
        ),
    )

    summary = world_refinement_module.refine_world_identities(
        project_slug="demo",
        use_llm=True,
        apply_changes=False,
    )

    assert summary.candidate_count == 1
    assert summary.comparison_count == 1
    assert len(calls) == 2
    assert any("compact_retry" in prompt for prompt in calls)
