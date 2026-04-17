from pathlib import Path

from orchestrator.prompt_package import parse_prompt_package


def test_parse_prompt_package_sections(tmp_path: Path) -> None:
    prompt_file = tmp_path / "prompt.md"
    prompt_file.write_text(
        "\n".join(
            [
                "# Title",
                "Scene Build Prompt",
                "",
                "# ID",
                "SC001_CL001_scene_build_prompt",
                "",
                "# Purpose",
                "Generate the opener.",
                "",
                "# Workflow Type",
                "still.scene_build.four_ref.klein.distilled",
                "",
                "# Positive Prompt",
                "cinematic frame",
                "",
                "# Negative Prompt",
                "blurry",
                "",
                "# Inputs",
                "- project_id: demo",
                "- scene_id: SC001",
                "",
                "# Continuity Notes",
                "- preserve wardrobe",
                "",
                "# Sources",
                "- 02_story_analysis/clip_plans/SC001/CL001.md",
                "",
            ]
        ),
        encoding="utf-8",
    )

    prompt = parse_prompt_package(prompt_file)

    assert prompt.title == "Scene Build Prompt"
    assert prompt.prompt_id == "SC001_CL001_scene_build_prompt"
    assert prompt.workflow_type == "still.scene_build.four_ref.klein.distilled"
    assert prompt.positive_prompt == "cinematic frame"
    assert prompt.inputs["project_id"] == "demo"
    assert prompt.sources == ["02_story_analysis/clip_plans/SC001/CL001.md"]
