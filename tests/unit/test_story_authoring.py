import json
from pathlib import Path

import orchestrator.authoring as authoring_module
import orchestrator.common as common_module
import orchestrator.scaffold as scaffold_module
import orchestrator.state as state_module
import orchestrator.story_authoring as story_authoring_module
from orchestrator.common import TEMPLATES_ROOT as REAL_TEMPLATES_ROOT
from orchestrator.prompt_package import parse_prompt_package


class _FakeAuthoringLMStudioClient:
    def __init__(self, _settings: object) -> None:
        pass

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

        if "project_summary_markdown" in user_prompt:
            return json.dumps(
                {
                    "project_summary_markdown": "# Project Summary\nA Mars adventure project.\n",
                    "chapter_summary_markdown": "# Chapter Summary\nAirship battle, drifting vessel, captive introduction.\n",
                }
            )

        if "character_index_markdown" in user_prompt:
            return json.dumps(
                {
                    "character_index_markdown": "# Character Index\n- john_carter\n- dejah_thoris\n",
                    "characters": [
                        {
                            "asset_id": "john_carter",
                            "filename": "hero_protagonist_profile.md",
                            "markdown": "# John Carter\nReliable protagonist breakdown.\n",
                            "manual_description_required": False,
                            "manual_description_reason": "",
                        },
                        {
                            "asset_id": "dejah_thoris",
                            "filename": "captured_princess_profile.md",
                            "markdown": "# Dejah Thoris\nImportant captive figure with incomplete stable visual description in this chapter alone.\n",
                            "manual_description_required": True,
                            "manual_description_reason": "The chapter introduces her vividly but does not provide enough stable facial, costume, and silhouette detail for dependable reference generation by itself.",
                        },
                    ],
                }
            )

        if "environment_index_markdown" in user_prompt:
            return json.dumps(
                {
                    "environment_index_markdown": "# Environment Index\n- abandoned_martian_city\n- martian_airship_battlefield\n",
                    "environments": [
                        {
                            "asset_id": "abandoned_martian_city",
                            "filename": "ancient_city_reference.md",
                            "markdown": "# Abandoned Martian City\nAncient empty city with broad plazas and building fronts.\n",
                        },
                        {
                            "asset_id": "martian_airship_battlefield",
                            "filename": "airship_battlefield_zone.md",
                            "markdown": "# Martian Airship Battlefield\nOpen valley and sky battle zone around the city.\n",
                        },
                    ],
                }
            )

        if "scene_index_markdown" in user_prompt:
            return json.dumps(
                {
                    "scene_index_markdown": "# Scene Index\n- SC001: Airship attack and discovery of the captive\n",
                    "scenes": [
                        {
                            "scene_id": "SC001",
                            "filename": "SC001_airship_attack_and_captive_reveal.md",
                            "markdown": "# SC001\n## Purpose\nAirship attack, damaged drift, looting, and the first sight of the captive.\n",
                        }
                    ],
                }
            )

        if "updated_scene_markdown" in user_prompt:
            return json.dumps(
                {
                    "scene_id": "SC001",
                    "updated_scene_markdown": "# SC001\n## Purpose\nAirship attack and captive reveal.\n## Beats\n- BT001 attack from cover\n- BT002 damaged ship drift and seizure\n- BT003 captive reveal\n",
                    "beat_index_markdown": "# Beat Index\n- BT001 attack from cover\n- BT002 damaged ship drift and seizure\n- BT003 captive reveal\n",
                    "beats": [
                        {
                            "beat_id": "BT001",
                            "filename": "BT001_attack_from_cover.md",
                            "markdown": "# BT001\nAttack from cover.\n",
                        },
                        {
                            "beat_id": "BT002",
                            "filename": "BT002_derelict_drift.md",
                            "markdown": "# BT002\nDamaged ship drifts and is boarded.\n",
                        },
                        {
                            "beat_id": "BT003",
                            "filename": "BT003_captive_reveal.md",
                            "markdown": "# BT003\nThe captive is revealed and seen by the protagonist.\n",
                        },
                    ],
                }
            )

        if "clip_roster_markdown" in user_prompt:
            return json.dumps(
                {
                    "scene_id": "SC001",
                    "clip_roster_markdown": "# SC001 Clip Roster\n- CL001 battle reveal wide\n- CL002 captive reaction reveal\n",
                    "clips": [
                        {
                            "clip_id": "CL001",
                            "filename": "CL001_battle_reveal_wide.md",
                            "markdown": "# Title\nSC001 CL001 Clip Plan\n\n# ID\nSC001_CL001\n\n# Purpose\nEstablish the sudden attack and the first exchange of fire.\n\n# Inputs\n- beat_id: BT001\n- duration_seconds: 5\n- composition_type: master_wide\n- continuity_mode: reframe_same_moment\n- starting_keyframe_strategy: scene_refs_to_keyframe\n- dependency_policy: independent\n- visible_character_assets: john_carter\n- required_refs: image_1,image_2\n- optional_refs: image_3,image_4\n\n# Output Targets\n- SC001_CL001_KF01_v001.png\n- SC001_CL001_MV01_v001.mp4\n",
                        },
                        {
                            "clip_id": "CL002",
                            "filename": "CL002_captive_reaction_reveal.md",
                            "markdown": "# Title\nSC001 CL002 Clip Plan\n\n# ID\nSC001_CL002\n\n# Purpose\nReveal the captive and the exchanged look.\n\n# Inputs\n- beat_id: BT003\n- duration_seconds: 5\n- composition_type: reaction\n- continuity_mode: cutaway\n- starting_keyframe_strategy: scene_refs_to_keyframe\n- dependency_policy: independent\n- visible_character_assets: john_carter,dejah_thoris\n- required_refs: image_1,image_2\n- optional_refs: image_3,image_4\n\n# Output Targets\n- SC001_CL002_KF01_v001.png\n- SC001_CL002_MV01_v001.mp4\n",
                        },
                    ],
                }
            )

        if "character_prompts" in user_prompt and "environment_prompts" in user_prompt:
            return json.dumps(
                {
                    "character_prompts": [
                        {
                            "asset_id": "john_carter",
                            "purpose": "Stable heroic reference still.",
                            "positive_prompt": "athletic human man, weathered traveler, upright posture, practical adventurer styling",
                            "negative_prompt": "extra limbs, duplicate face, blurred features",
                            "inputs": {
                                "project_id": "demo",
                                "asset_id": "john_carter",
                            },
                            "continuity_notes": ["Preserve the stable protagonist look for later scene coverage."],
                            "repair_notes": ["If later scenes drift, use this as the identity reference baseline."],
                        },
                        {
                            "asset_id": "dejah_thoris",
                            "purpose": "Initial captive reference still with caution around missing details.",
                            "positive_prompt": "slender regal young woman, dark flowing hair, luminous large eyes, poised captive bearing",
                            "negative_prompt": "extra limbs, distorted anatomy, blurred face",
                            "inputs": {
                                "project_id": "demo",
                                "asset_id": "dejah_thoris",
                                "manual_description_required": "true",
                            },
                            "continuity_notes": ["Manual description may be needed before finalizing the long-term shared reference."],
                            "repair_notes": ["Refresh after a manual character description is pasted."],
                        },
                    ],
                    "environment_prompts": [
                        {
                            "asset_id": "abandoned_martian_city",
                            "purpose": "Stable city reference still.",
                            "positive_prompt": "ancient empty martian city, broad stone plaza, weathered building fronts, dry red-world atmosphere",
                            "negative_prompt": "modern signage, crowding, contemporary vehicles",
                            "inputs": {
                                "project_id": "demo",
                                "asset_id": "abandoned_martian_city",
                            },
                            "continuity_notes": ["Keep the broad plaza and abandoned monumental architecture stable."],
                            "repair_notes": ["Use as the base environmental reference for scene planning."],
                        }
                    ],
                }
            )

        if "Target stage: " in system_prompt:
            stage_line = next(line for line in system_prompt.splitlines() if line.startswith("Target stage: "))
            stage = stage_line.split(": ", 1)[1]
            return json.dumps(
                {
                    "purpose": f"{stage} purpose",
                    "positive_prompt": f"{stage} positive prompt",
                    "negative_prompt": f"{stage} negative prompt",
                    "inputs": {
                        "duration_seconds": "5",
                        "batch_role": "",
                    },
                    "continuity_notes": [f"{stage} continuity note"],
                    "repair_notes": [f"{stage} repair note"],
                }
            )

        raise AssertionError(f"Unexpected LM Studio prompt:\nSYSTEM:\n{system_prompt}\n\nUSER:\n{user_prompt}")


def test_authoring_checkpoint_writes_analysis_planning_and_manual_character_placeholders(
    tmp_path: Path, monkeypatch
) -> None:
    projects_root = tmp_path / "projects"

    monkeypatch.setattr(common_module, "ROOT", tmp_path)
    monkeypatch.setattr(common_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "ROOT", tmp_path)
    monkeypatch.setattr(scaffold_module, "TEMPLATES_ROOT", REAL_TEMPLATES_ROOT)
    monkeypatch.setattr(scaffold_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(state_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(state_module, "ROOT", tmp_path)
    monkeypatch.setattr(state_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(authoring_module, "ROOT", tmp_path)
    monkeypatch.setattr(authoring_module, "LMStudioClient", _FakeAuthoringLMStudioClient)
    monkeypatch.setattr(authoring_module, "load_runtime_settings", lambda: object())
    monkeypatch.setattr(authoring_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(story_authoring_module, "LMStudioClient", _FakeAuthoringLMStudioClient)
    monkeypatch.setattr(story_authoring_module, "load_runtime_settings", lambda: object())

    scaffold_module.create_project("demo")

    chapter_path = projects_root / "demo" / "01_source" / "chapters" / "CH001_demo.md"
    chapter_path.write_text(
        "\n".join(
            [
                "# Title",
                "Demo Chapter",
                "",
                "# Chapter",
                "CH001",
                "",
                "# Text",
                "A damaged vessel drifts above an abandoned city while a captive is discovered.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    summary = story_authoring_module.authoring_checkpoint(
        project_slug="demo",
        chapter="CH001_demo.md",
        scene_id="SC001",
    )

    assert summary.analysis.chapter_id == "CH001"
    assert summary.analysis.scene_ids == ["SC001"]
    assert len(summary.analysis.manual_character_description_requests) == 1
    manual_request = summary.analysis.manual_character_description_requests[0]
    assert manual_request.asset_id == "dejah_thoris"
    assert manual_request.source_path == "projects/demo/01_source/character_descriptions/dejah_thoris_manual_description.md"

    manual_description_path = projects_root / "demo" / "01_source" / "character_descriptions" / "dejah_thoris_manual_description.md"
    assert manual_description_path.exists()
    assert "Paste a stable manual visual description" in manual_description_path.read_text(encoding="utf-8")

    assert summary.planning.scene_id == "SC001"
    assert summary.planning.beat_ids == ["BT001", "BT002", "BT003"]
    assert summary.planning.clip_ids == ["CL001", "CL002"]
    assert (projects_root / "demo" / "02_story_analysis" / "scene_breakdowns" / "SC001.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "beat_bundles" / "SC001" / "BT001.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "clip_plans" / "SC001" / "CL001.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "clip_plans" / "SC001" / "CL002.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "scene_breakdowns" / "SC001_airship_attack_and_captive_reveal.md").exists() is False

    shared_character_prompt = parse_prompt_package(
        projects_root / "demo" / "03_prompt_packages" / "characters" / "john_carter" / "john_carter_ref_prompt.md"
    )
    assert shared_character_prompt.workflow_type == "still.t2i.klein.distilled"
    assert shared_character_prompt.purpose == "Stable heroic reference still."
    assert "projects/demo/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md" in shared_character_prompt.sources

    clip_keyframe_prompt = parse_prompt_package(
        projects_root
        / "demo"
        / "03_prompt_packages"
        / "keyframes"
        / "SC001"
        / "CL001"
        / "SC001_CL001_keyframe_prompt.md"
    )
    assert clip_keyframe_prompt.purpose == "keyframe purpose"
    assert "projects/demo/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md" in clip_keyframe_prompt.sources
    assert "projects/demo/02_story_analysis/story_summary/project_summary.md" in clip_keyframe_prompt.sources
