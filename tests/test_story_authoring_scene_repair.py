from orchestrator.story_authoring import (
    _PacketDocument,
    _PacketRecord,
    _extract_scene_decomposition_outputs,
)


def test_extract_scene_decomposition_outputs_repairs_missing_scene_ids_from_index() -> None:
    packet = _PacketDocument(
        metadata={"task": "scene_decomposition", "version": "1"},
        sections={
            "scene_index_markdown": "- SC001: Opening\n- SC002: Chase",
        },
        records=[
            _PacketRecord(
                fields={"type": "scene"},
                sections={"markdown": "scene purpose: opening"},
            ),
            _PacketRecord(
                fields={"type": "scene"},
                sections={"markdown": "scene purpose: chase"},
            ),
        ],
    )

    _, records, warnings = _extract_scene_decomposition_outputs(packet=packet, chapter_id="CH001")

    assert records[0].fields["scene_id"] == "SC001"
    assert records[1].fields["scene_id"] == "SC002"
    assert any("Inferred missing scene_id 'SC001'" in warning for warning in warnings)
