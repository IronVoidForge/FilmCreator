import json
from pathlib import Path

import orchestrator.authoring as authoring_module
import orchestrator.common as common_module
from orchestrator.lmstudio_client import LMStudioChatResult
import orchestrator.scaffold as scaffold_module
import orchestrator.state as state_module
import orchestrator.story_authoring as story_authoring_module
from orchestrator.common import TEMPLATES_ROOT as REAL_TEMPLATES_ROOT
from orchestrator.prompt_package import parse_prompt_package


def _packet(
    *,
    task: str,
    sections: dict[str, str] | None = None,
    records: list[str] | None = None,
    fenced: bool = False,
) -> str:
    lines = [
        "[[FILMCREATOR_PACKET]]",
        f"task: {task}",
        "version: 1",
    ]
    for name, content in (sections or {}).items():
        lines.extend(
            [
                "",
                f"[[SECTION {name}]]",
                content.rstrip(),
                "[[/SECTION]]",
            ]
        )
    for record in records or []:
        lines.extend(["", record.rstrip()])
    lines.append("[[/FILMCREATOR_PACKET]]")
    body = "\n".join(lines)
    if fenced:
        return f"```md\n{body}\n```"
    return body


def _record(*, record_type: str, fields: dict[str, str], sections: dict[str, str]) -> str:
    lines = [
        "[[FILMCREATOR_RECORD]]",
        f"type: {record_type}",
    ]
    for key, value in fields.items():
        lines.append(f"{key}: {value}")
    for name, content in sections.items():
        lines.extend(
            [
                "",
                f"[[SECTION {name}]]",
                content.rstrip(),
                "[[/SECTION]]",
            ]
        )
    lines.append("[[/FILMCREATOR_RECORD]]")
    return "\n".join(lines)


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

        if "task: chapter_summary" in user_prompt:
            return _packet(
                task="chapter_summary",
                sections={
                    "project_summary_markdown": "# Project Summary\nA Mars adventure project.\n",
                    "chapter_summary_markdown": "# Chapter Summary\nAirship battle, drifting vessel, captive introduction.\n",
                },
            )

        if "task: character_extraction" in user_prompt:
            return _packet(
                task="character_extraction",
                sections={
                    "character_index_markdown": "# Character Index\n- john_carter\n- dejah_thoris\n",
                },
                records=[
                    _record(
                        record_type="character",
                        fields={
                            "asset_id": "john_carter",
                            "manual_description_required": "false",
                            "manual_description_reason": "",
                        },
                        sections={
                            "markdown": "# John Carter\nReliable protagonist breakdown.\n",
                        },
                    ),
                    _record(
                        record_type="character",
                        fields={
                            "asset_id": "dejah_thoris",
                            "manual_description_required": "true",
                            "manual_description_reason": "The chapter introduces her vividly but does not provide enough stable facial, costume, and silhouette detail for dependable reference generation by itself.",
                        },
                        sections={
                            "markdown": "# Dejah Thoris\nImportant captive figure with incomplete stable visual description in this chapter alone.\n",
                        },
                    ),
                ],
            )

        if "task: environment_extraction" in user_prompt:
            return _packet(
                task="environment_extraction",
                sections={
                    "environment_index_markdown": "# Environment Index\n- abandoned_martian_city\n- martian_airship_battlefield\n",
                },
                records=[
                    _record(
                        record_type="environment",
                        fields={"asset_id": "abandoned_martian_city"},
                        sections={
                            "markdown": "# Abandoned Martian City\nAncient empty city with broad plazas and building fronts.\n",
                        },
                    ),
                    _record(
                        record_type="environment",
                        fields={"asset_id": "martian_airship_battlefield"},
                        sections={
                            "markdown": "# Martian Airship Battlefield\nOpen valley and sky battle zone around the city.\n",
                        },
                    ),
                ],
                fenced=True,
            )

        if "task: scene_decomposition" in user_prompt:
            return _packet(
                task="scene_decomposition",
                sections={
                    "scene_index_markdown": "# Scene Index\n- SC001: Airship attack and discovery of the captive\n",
                },
                records=[
                    _record(
                        record_type="scene",
                        fields={"scene_id": "SC001"},
                        sections={
                            "markdown": "# SC001\n## Purpose\nAirship attack, damaged drift, looting, and the first sight of the captive.\n",
                        },
                    )
                ],
            )

        if "task: scene_beats" in user_prompt:
            return _packet(
                task="scene_beats",
                sections={
                    "updated_scene_markdown": "# SC001\n## Purpose\nAirship attack and captive reveal.\n## Beats\n- BT001 attack from cover\n- BT002 damaged ship drift and seizure\n- BT003 captive reveal\n",
                    "beat_index_markdown": "# Beat Index\n- BT001 attack from cover\n- BT002 damaged ship drift and seizure\n- BT003 captive reveal\n",
                },
                records=[
                    _record(
                        record_type="beat",
                        fields={"beat_id": "BT001"},
                        sections={"markdown": "# BT001\nAttack from cover.\n"},
                    ),
                    _record(
                        record_type="beat",
                        fields={"beat_id": "BT002"},
                        sections={"markdown": "# BT002\nDamaged ship drifts and is boarded.\n"},
                    ),
                    _record(
                        record_type="beat",
                        fields={"beat_id": "BT003"},
                        sections={"markdown": "# BT003\nThe captive is revealed and seen by the protagonist.\n"},
                    ),
                ],
            )

        if "task: clip_planning" in user_prompt:
            return _packet(
                task="clip_planning",
                sections={
                    "clip_roster_markdown": "# SC001 Clip Roster\n- CL001 battle reveal wide\n- CL002 captive reaction reveal\n",
                },
                records=[
                    _record(
                        record_type="clip",
                        fields={"clip_id": "CL001"},
                        sections={
                            "markdown": "# Title\nSC001 CL001 Clip Plan\n\n# ID\nSC001_CL001\n\n# Purpose\nEstablish the sudden attack and the first exchange of fire.\n\n# Inputs\n- beat_id: BT001\n- duration_seconds: 5\n- composition_type: master_wide\n- continuity_mode: reframe_same_moment\n- starting_keyframe_strategy: scene_refs_to_keyframe\n- dependency_policy: independent\n- visible_character_assets: john_carter\n- required_refs: image_1,image_2\n- optional_refs: image_3,image_4\n\n# Output Targets\n- SC001_CL001_KF01_v001.png\n- SC001_CL001_MV01_v001.mp4\n",
                        },
                    ),
                    _record(
                        record_type="clip",
                        fields={"clip_id": "CL002"},
                        sections={
                            "markdown": "# Title\nSC001 CL002 Clip Plan\n\n# ID\nSC001_CL002\n\n# Purpose\nReveal the captive and the exchanged look.\n\n# Inputs\n- beat_id: BT003\n- duration_seconds: 5\n- composition_type: reaction\n- continuity_mode: cutaway\n- starting_keyframe_strategy: scene_refs_to_keyframe\n- dependency_policy: independent\n- visible_character_assets: john_carter,dejah_thoris\n- required_refs: image_1,image_2\n- optional_refs: image_3,image_4\n\n# Output Targets\n- SC001_CL002_KF01_v001.png\n- SC001_CL002_MV01_v001.mp4\n",
                        },
                    ),
                ],
            )

        if "task: character_shared_prompts" in user_prompt:
            asset_id = "character_asset"
            for marker in ("Asset id: ", "asset_id: "):
                if marker in user_prompt:
                    asset_id = user_prompt.split(marker, 1)[1].splitlines()[0].strip()
                    break
            return _packet(
                task="character_shared_prompts",
                records=[
                    _record(
                        record_type="character_prompt",
                        fields={"asset_id": asset_id},
                        sections={
                            "purpose": f"Stable reference still for {asset_id}.",
                            "positive_prompt": f"descriptive visible traits for {asset_id}, grounded local reference, stable silhouette",
                            "negative_prompt": "extra limbs, duplicate face, blurred features",
                            "inputs_markdown": f"- project_id: demo\n- asset_id: {asset_id}",
                            "continuity_notes_markdown": f"- Preserve the stable look for {asset_id} across later coverage.",
                            "repair_notes_markdown": "- Refresh if later scenes drift.",
                        },
                    ),
                ],
            )

        if "task: environment_shared_prompts" in user_prompt:
            asset_id = "environment_asset"
            for marker in ("Asset id: ", "asset_id: "):
                if marker in user_prompt:
                    asset_id = user_prompt.split(marker, 1)[1].splitlines()[0].strip()
                    break
            return _packet(
                task="environment_shared_prompts",
                records=[
                    _record(
                        record_type="environment_prompt",
                        fields={"asset_id": asset_id},
                        sections={
                            "purpose": f"Stable environment reference still for {asset_id}.",
                            "positive_prompt": f"descriptive visible features for {asset_id}, grounded environment reference, stable architecture and atmosphere",
                            "negative_prompt": "modern signage, crowding, contemporary vehicles",
                            "inputs_markdown": f"- project_id: demo\n- asset_id: {asset_id}",
                            "continuity_notes_markdown": f"- Keep the stable environment identity for {asset_id}.",
                            "repair_notes_markdown": "- Use as the base environmental reference for scene planning.",
                        },
                    )
                ],
            )

        if "Target stage: " in system_prompt:
            stage_line = next(line for line in system_prompt.splitlines() if line.startswith("Target stage: "))
            stage = stage_line.split(": ", 1)[1]
            return _packet(
                task="clip_prompt",
                sections={
                    "purpose": f"{stage} purpose",
                    "positive_prompt": f"{stage} positive prompt",
                    "negative_prompt": f"{stage} negative prompt",
                    "inputs_markdown": "\n".join(
                        [
                            "- duration_seconds: 5",
                            "- batch_role: ",
                        ]
                    ),
                    "continuity_notes_markdown": f"- {stage} continuity note",
                    "repair_notes_markdown": f"- {stage} repair note",
                },
            )

        raise AssertionError(f"Unexpected LM Studio prompt:\nSYSTEM:\n{system_prompt}\n\nUSER:\n{user_prompt}")

    def chat_completion_result(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        model: str | None = None,
    ) -> LMStudioChatResult:
        return LMStudioChatResult(
            status="success",
            model=model or "test-local-model",
            payload={},
            text=self.chat_completion(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                temperature=temperature,
                model=model,
            ),
        )


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
    (projects_root / "demo" / "02_story_analysis" / "scene_breakdowns" / "CH001_SC001_airship_attack_and_captive_reveal.md").write_text(
        "# stale scene file\n",
        encoding="utf-8",
    )
    (projects_root / "demo" / "02_story_analysis" / "character_breakdowns" / "the_narrator.md").write_text(
        "# stale character alias\n",
        encoding="utf-8",
    )
    (projects_root / "demo" / "02_story_analysis" / "environment_breakdowns" / "ancient_city_reference.md").write_text(
        "# stale environment alias\n",
        encoding="utf-8",
    )
    (projects_root / "demo" / "01_source" / "character_descriptions" / "legacy_extra_manual_description.md").write_text(
        "\n".join(
            [
                "<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->",
                "",
                "# Asset ID",
                "legacy_extra",
                "",
                "# Purpose",
                "Paste a stable manual visual description for this character so later shared reference generation can use it.",
                "",
                "# Manual Description",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (projects_root / "demo" / "01_source" / "character_descriptions" / "archivist_manual_description.md").write_text(
        "\n".join(
            [
                "# Asset ID",
                "archivist",
                "",
                "# Manual Description",
                "A real manually pasted description that should survive cleanup.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    summary = story_authoring_module.authoring_checkpoint(
        project_slug="demo",
        chapter="CH001_demo.md",
        scene_id="CH001_SC001",
    )

    assert summary.analysis.chapter_id == "CH001"
    assert summary.analysis.scene_ids == ["CH001_SC001"]
    assert len(summary.analysis.manual_character_description_requests) == 1
    manual_request = summary.analysis.manual_character_description_requests[0]
    assert manual_request.asset_id == "dejah_thoris"
    assert manual_request.source_path == "projects/demo/01_source/character_descriptions/dejah_thoris_manual_description.md"

    manual_description_path = projects_root / "demo" / "01_source" / "character_descriptions" / "dejah_thoris_manual_description.md"
    assert manual_description_path.exists()
    assert "Paste a stable manual visual description" in manual_description_path.read_text(encoding="utf-8")
    assert (projects_root / "demo" / "01_source" / "character_descriptions" / "legacy_extra_manual_description.md").exists() is False
    assert (projects_root / "demo" / "01_source" / "character_descriptions" / "archivist_manual_description.md").exists()

    assert summary.planning.scene_id == "CH001_SC001"
    assert summary.planning.beat_ids == ["BT001", "BT002", "BT003"]
    assert summary.planning.clip_ids == ["CL001", "CL002"]
    assert (projects_root / "demo" / "02_story_analysis" / "scene_breakdowns" / "CH001_SC001.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "beat_bundles" / "CH001_SC001" / "BT001.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "clip_plans" / "CH001_SC001" / "CL001.md").exists()
    assert (projects_root / "demo" / "02_story_analysis" / "clip_plans" / "CH001_SC001" / "CL002.md").exists()
    assert (
        projects_root
        / "demo"
        / "02_story_analysis"
        / "scene_breakdowns"
        / "CH001_SC001_airship_attack_and_captive_reveal.md"
    ).exists() is False
    assert (projects_root / "demo" / "02_story_analysis" / "character_breakdowns" / "the_narrator.md").exists() is False
    assert (projects_root / "demo" / "02_story_analysis" / "environment_breakdowns" / "ancient_city_reference.md").exists() is False

    shared_character_prompt = parse_prompt_package(
        projects_root / "demo" / "03_prompt_packages" / "characters" / "john_carter" / "john_carter_ref_prompt.md"
    )
    assert shared_character_prompt.workflow_type == "still.t2i.klein.distilled"
    assert shared_character_prompt.purpose.startswith("Stable reference still")
    assert "john_carter" in shared_character_prompt.positive_prompt
    assert "projects/demo/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md" in shared_character_prompt.sources
    assert "projects/demo/02_story_analysis/character_breakdowns/john_carter.md" in shared_character_prompt.sources

    clip_keyframe_prompt = parse_prompt_package(
        projects_root
        / "demo"
        / "03_prompt_packages"
        / "keyframes"
        / "CH001_SC001"
        / "CL001"
        / "CH001_SC001_CL001_keyframe_prompt.md"
    )
    assert clip_keyframe_prompt.purpose == "keyframe purpose"
    assert "projects/demo/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md" in clip_keyframe_prompt.sources
    assert "projects/demo/02_story_analysis/story_summary/project_summary.md" in clip_keyframe_prompt.sources

    log_files = sorted((projects_root / "demo" / "02_story_analysis" / "logs").glob("*.md"))
    assert len(log_files) >= 8


def test_packet_parser_accepts_missing_record_closers() -> None:
    response = "\n".join(
        [
            "[[FILMCREATOR_PACKET]]",
            "task: scene_decomposition",
            "version: 1",
            "",
            "[[SECTION scene_index_markdown]]",
            "# Scene Index",
            "- SC001: Example scene",
            "[[/SECTION]]",
            "",
            "[[FILMCREATOR_RECORD]]",
            "type: scene",
            "scene_id: SC001",
            "",
            "[[SECTION markdown]]",
            "# SC001",
            "Scene body one.",
            "[[/SECTION]]",
            "",
            "[[FILMCREATOR_RECORD]]",
            "type: scene",
            "scene_id: SC002",
            "",
            "[[SECTION markdown]]",
            "# SC002",
            "Scene body two.",
            "[[/SECTION]]",
            "",
            "[[/FILMCREATOR_PACKET]]",
        ]
    )

    packet = story_authoring_module._parse_packet_document(response, expected_task="scene_decomposition")

    assert packet.metadata["task"] == "scene_decomposition"
    assert packet.sections["scene_index_markdown"].startswith("# Scene Index")
    assert len(packet.records) == 2
    assert packet.records[0].fields["scene_id"] == "SC001"
    assert packet.records[0].sections["markdown"].startswith("# SC001")
    assert packet.records[1].fields["scene_id"] == "SC002"


def test_scene_decomposition_validator_warns_on_two_scenes_and_rejects_empty() -> None:
    scene_records = [
        story_authoring_module._PacketRecord(
            fields={"scene_id": "SC001"},
            sections={
                "markdown": "# SC001\nScene one setup.\n[[SECTION Scene Summary]]\nSetup only.\n[[/SECTION]]",
            },
        ),
        story_authoring_module._PacketRecord(
            fields={"scene_id": "SC002"},
            sections={
                "markdown": "# SC002\nScene two aftermath.\n[[SECTION Scene Summary]]\nAftermath.\n[[/SECTION]]",
            },
        ),
    ]

    warnings = story_authoring_module._validate_scene_decomposition(
        chapter_id="CH013",
        scene_records=scene_records,
    )

    assert any("preferred minimum is 3" in warning for warning in warnings)

    try:
        story_authoring_module._validate_scene_decomposition(chapter_id="CH013", scene_records=[])
    except story_authoring_module.LMStudioError as exc:
        assert "no usable scenes" in str(exc)
    else:
        raise AssertionError("Expected empty scene decomposition to fail validation.")
