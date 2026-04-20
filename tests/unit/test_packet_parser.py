from __future__ import annotations

from orchestrator.features.authoring import packet_parser


def test_parse_packet_document_accepts_missing_record_closers() -> None:
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

    packet = packet_parser.parse_packet_document(response, expected_task="scene_decomposition")

    assert packet.metadata["task"] == "scene_decomposition"
    assert packet.sections["scene_index_markdown"].startswith("# Scene Index")
    assert len(packet.records) == 2
    assert packet.records[0].fields["scene_id"] == "SC001"
    assert packet.records[0].sections["markdown"].startswith("# SC001")
    assert packet.records[1].fields["scene_id"] == "SC002"


def test_parse_packet_document_accepts_implicit_markdown_sections() -> None:
    response = "\n".join(
        [
            "[[FILMCREATOR_PACKET]]",
            "task: chapter_summary",
            "version: 1",
            "project_summary_markdown:",
            "# Project Summary",
            "Reusable overview text.",
            "",
            "chapter_summary_markdown:",
            "# Chapter Summary",
            "Chapter-specific text.",
            "[[/FILMCREATOR_PACKET]]",
        ]
    )

    packet = packet_parser.parse_packet_document(response, expected_task="chapter_summary")

    assert packet.metadata["project_summary_markdown"].startswith("# Project Summary")
    assert packet.metadata["chapter_summary_markdown"].startswith("# Chapter Summary")


def test_parse_packet_document_infers_missing_task_and_version_when_sections_are_present() -> None:
    response = "\n".join(
        [
            "[[FILMCREATOR_PACKET]]",
            "project_summary_markdown:",
            "[[SECTION project_summary_markdown]]",
            "# Project Summary",
            "[[/SECTION]]",
            "chapter_summary_markdown:",
            "[[SECTION chapter_summary_markdown]]",
            "# Chapter Summary",
            "[[/SECTION]]",
            "[[/FILMCREATOR_PACKET]]",
        ]
    )

    packet = packet_parser.parse_packet_document(response, expected_task="chapter_summary")

    assert packet.metadata["task"] == "chapter_summary"
    assert packet.metadata["version"] == "1"
    assert packet.sections["project_summary_markdown"] == "# Project Summary"
    assert packet.sections["chapter_summary_markdown"] == "# Chapter Summary"


def test_extract_character_records_from_index_markdown_salvages_heading_blocks() -> None:
    markdown = "\n".join(
        [
            "# Character Index - Chapter II",
            "",
            "## protagonist",
            "- **Asset ID:** protagonist",
            "- **Canonical Character ID:** CH002 Protagonist",
            "- **Aliases:** Narrator, Conscious Entity",
            "- **Is Fully Identified:** false",
            "- **Manual Description Required:** true",
            "- **Manual Description Reason:** Sparse visual detail.",
            "- **Clarification Required:** true",
            "- **Clarification Reason:** Needs identity clarification.",
            "- **Clarification Question:** What is the protagonist?",
            "",
            "## apache_warriors",
            "- **Asset ID:** apache_warriors",
            "- **Canonical Character ID:** CH002 Apache Warriors",
            "- **Aliases:** Apache Tribe Members",
            "- **Is Fully Identified:** false",
            "- **Manual Description Required:** true",
            "- **Manual Description Reason:** Sparse visual detail.",
            "- **Clarification Required:** true",
            "- **Clarification Reason:** Needs identity clarification.",
            "- **Clarification Question:** What do they look like?",
        ]
    )

    records = packet_parser.extract_character_records_from_index_markdown(markdown)

    assert len(records) == 2
    assert records[0].fields["type"] == "character"
    assert records[0].fields["asset_id"] == "protagonist"
    assert records[0].fields["canonical_character_id"] == "CH002 Protagonist"
    assert records[0].sections["markdown"].startswith("## protagonist")
    assert records[1].fields["asset_id"] == "apache_warriors"


def test_validate_scene_decomposition_warns_on_two_scenes_and_rejects_empty() -> None:
    scene_records = [
        packet_parser.PacketRecord(
            fields={"scene_id": "SC001"},
            sections={"markdown": "# SC001\nScene one setup.\n[[SECTION Scene Summary]]\nSetup only.\n[[/SECTION]]"},
        ),
        packet_parser.PacketRecord(
            fields={"scene_id": "SC002"},
            sections={"markdown": "# SC002\nScene two aftermath.\n[[SECTION Scene Summary]]\nAftermath.\n[[/SECTION]]"},
        ),
    ]

    warnings = packet_parser.validate_scene_decomposition(chapter_id="CH013", scene_records=scene_records)

    assert any("preferred minimum is 3" in warning for warning in warnings)

    try:
        packet_parser.validate_scene_decomposition(chapter_id="CH013", scene_records=[])
    except Exception as exc:
        assert "no usable scenes" in str(exc)
    else:  # pragma: no cover - defensive
        raise AssertionError("Expected empty scene decomposition to fail")
