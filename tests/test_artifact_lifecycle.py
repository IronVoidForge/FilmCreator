from pathlib import Path

from orchestrator.artifact_lifecycle import (
    ArtifactMetadata,
    is_locked,
    mark_stale,
    merge_preserving_locked_fields,
    write_artifact_with_metadata,
)
from orchestrator.core.json_io import read_json


def test_mark_stale_updates_status_and_history() -> None:
    metadata = ArtifactMetadata(
        status="approved",
        created_at_utc="2026-04-26T00:00:00+00:00",
        updated_at_utc="2026-04-26T00:00:00+00:00",
        source_fingerprint="abc",
    )

    stale = mark_stale(metadata, "upstream changed")

    assert stale.status == "stale"
    assert stale.revision_history[-1]["reason"] == "upstream changed"


def test_merge_preserving_locked_fields_keeps_locked_values() -> None:
    old = {
        "artifact_id": "hero_ref",
        "canonical_reference_image": "locked.png",
        "variant_name": "bust_portrait",
        "metadata": {
            "status": "locked",
            "created_at_utc": "2026-04-26T00:00:00+00:00",
            "updated_at_utc": "2026-04-26T00:00:00+00:00",
            "source_fingerprint": "old",
            "locked_fields": {"__artifact__": True, "canonical_reference_image": True},
            "manual_overrides": {},
            "revision_history": [],
        },
    }
    new = {
        "artifact_id": "hero_ref",
        "canonical_reference_image": "new.png",
        "variant_name": "full_body_neutral",
        "metadata": {
            "status": "approved",
            "created_at_utc": "2026-04-26T00:00:00+00:00",
            "updated_at_utc": "2026-04-26T01:00:00+00:00",
            "source_fingerprint": "new",
            "locked_fields": {},
            "manual_overrides": {},
            "revision_history": [],
        },
    }

    merged = merge_preserving_locked_fields(old, new)

    assert merged["canonical_reference_image"] == "locked.png"
    assert merged["variant_name"] == "bust_portrait"
    assert is_locked(merged["metadata"]) is True


def test_write_artifact_with_metadata_persists_metadata(tmp_path: Path) -> None:
    path = tmp_path / "artifact.json"
    write_artifact_with_metadata(
        path,
        {"artifact_id": "hero_ref", "value": "approved.png"},
        artifact_type="reference_asset",
        status="approved",
        source_fingerprint="fp1",
    )

    payload = read_json(path)
    assert payload["artifact_type"] == "reference_asset"
    assert payload["metadata"]["status"] == "approved"
