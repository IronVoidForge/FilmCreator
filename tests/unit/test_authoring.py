import json
from pathlib import Path

import orchestrator.authoring as authoring_module
import orchestrator.scaffold as scaffold_module
import orchestrator.state as state_module
from orchestrator.common import TEMPLATES_ROOT as REAL_TEMPLATES_ROOT
from orchestrator.prompt_package import parse_prompt_package


class _FakeLMStudioClient:
    def __init__(self, _settings: object) -> None:
        self.calls: list[str] = []

    def resolve_model(self, available_models=None) -> str:  # noqa: ANN001
        return "test-local-model"

    def chat_completion(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        model: str | None = None,
    ) -> str:
        assert temperature == 0.2
        assert model is None
        stage_line = next(line for line in system_prompt.splitlines() if line.startswith("Target stage: "))
        stage = stage_line.split(": ", 1)[1]
        assert "First line must be [[FILMCREATOR_PACKET]]" in user_prompt
        lines = [
            "[[FILMCREATOR_PACKET]]",
            "task: clip_prompt",
            f"stage: {stage}",
            "version: 1",
            "",
            "[[SECTION purpose]]",
            f"{stage} purpose",
            "[[/SECTION]]",
            "",
            "[[SECTION positive_prompt]]",
            f"{stage} positive prompt",
            "[[/SECTION]]",
            "",
            "[[SECTION negative_prompt]]",
            f"{stage} negative prompt",
            "[[/SECTION]]",
            "",
            "[[SECTION inputs_markdown]]",
            "- duration_seconds: 5",
            "- batch_role: ",
            "[[/SECTION]]",
            "",
            "[[SECTION continuity_notes_markdown]]",
            f"- {stage} continuity note",
            "[[/SECTION]]",
            "",
            "[[SECTION repair_notes_markdown]]",
            f"- {stage} repair note",
            "[[/SECTION]]",
            "",
            "[[/FILMCREATOR_PACKET]]",
        ]
        return "\n".join(lines)


def test_write_prompts_writes_canonical_files_and_updates_clip_state(tmp_path: Path, monkeypatch) -> None:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "ROOT", tmp_path)
    monkeypatch.setattr(scaffold_module, "TEMPLATES_ROOT", REAL_TEMPLATES_ROOT)
    monkeypatch.setattr(scaffold_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(state_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(state_module, "ROOT", tmp_path)
    monkeypatch.setattr(state_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(authoring_module, "ROOT", tmp_path)
    monkeypatch.setattr(authoring_module, "LMStudioClient", _FakeLMStudioClient)
    monkeypatch.setattr(authoring_module, "load_runtime_settings", lambda: object())
    monkeypatch.setattr(authoring_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())

    scaffold_module.create_clip("demo", "SC001", "CL001")

    summary = authoring_module.write_prompts(
        project_slug="demo",
        scene_id="SC001",
        clip_id="CL001",
    )

    assert summary.project_slug == "demo"
    assert summary.scene_id == "SC001"
    assert summary.clip_ids == ["CL001"]
    assert summary.model == "test-local-model"
    assert len(summary.written_files) == 4

    keyframe_prompt = parse_prompt_package(
        projects_root
        / "demo"
        / "03_prompt_packages"
        / "keyframes"
        / "SC001"
        / "CL001"
        / "SC001_CL001_keyframe_prompt.md"
    )
    assert keyframe_prompt.purpose == "keyframe purpose"
    assert keyframe_prompt.positive_prompt == "keyframe positive prompt"
    assert keyframe_prompt.inputs["duration_seconds"] == "5"
    assert keyframe_prompt.sources == [
        "projects/demo/02_story_analysis/clip_plans/SC001/CL001.md",
        "projects/demo/02_story_analysis/scene_breakdowns/SC001.md",
        "projects/demo/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md",
        "projects/demo/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md",
        "projects/demo/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md",
        "projects/demo/02_story_analysis/story_summary/project_summary.md",
    ]

    clip_state = state_module.load_clip_state("demo", "SC001", "CL001")
    assert clip_state["inputs"]["scene_stage_prompt_package"] == (
        "projects/demo/03_prompt_packages/scenes/SC001/CL001/SC001_CL001_scene_stage_prompt.md"
    )
    assert clip_state["inputs"]["keyframe_prompt_package"] == (
        "projects/demo/03_prompt_packages/keyframes/SC001/CL001/SC001_CL001_keyframe_prompt.md"
    )
    assert clip_state["inputs"]["fix_prompt_packages"] == [
        "projects/demo/03_prompt_packages/fixes/SC001/CL001/SC001_CL001_fix_01_prompt.md"
    ]
    assert clip_state["inputs"]["cut_motion_prompt_package"] == (
        "projects/demo/03_prompt_packages/cut_motion/SC001/CL001/SC001_CL001_cut_motion_prompt.md"
    )
