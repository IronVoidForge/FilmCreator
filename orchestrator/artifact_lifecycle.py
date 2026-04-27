from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core.json_io import write_json


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass(frozen=True)
class ArtifactMetadata:
    status: str
    created_at_utc: str
    updated_at_utc: str
    source_fingerprint: str
    locked_fields: dict[str, bool] = field(default_factory=dict)
    manual_overrides: dict[str, Any] = field(default_factory=dict)
    revision_history: list[dict[str, Any]] = field(default_factory=list)

    @classmethod
    def from_dict(cls, payload: dict[str, Any] | None, *, default_status: str = "generated") -> "ArtifactMetadata":
        data = payload if isinstance(payload, dict) else {}
        created_at = str(data.get("created_at_utc", "")).strip() or utc_now()
        updated_at = str(data.get("updated_at_utc", "")).strip() or created_at
        locked_fields = data.get("locked_fields", {})
        manual_overrides = data.get("manual_overrides", {})
        revision_history = data.get("revision_history", [])
        return cls(
            status=str(data.get("status", default_status)).strip() or default_status,
            created_at_utc=created_at,
            updated_at_utc=updated_at,
            source_fingerprint=str(data.get("source_fingerprint", "")).strip(),
            locked_fields={str(key): bool(value) for key, value in locked_fields.items()} if isinstance(locked_fields, dict) else {},
            manual_overrides=dict(manual_overrides) if isinstance(manual_overrides, dict) else {},
            revision_history=[dict(item) for item in revision_history if isinstance(item, dict)] if isinstance(revision_history, list) else [],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "created_at_utc": self.created_at_utc,
            "updated_at_utc": self.updated_at_utc,
            "source_fingerprint": self.source_fingerprint,
            "locked_fields": dict(self.locked_fields),
            "manual_overrides": dict(self.manual_overrides),
            "revision_history": list(self.revision_history),
        }


def compute_source_fingerprint(payload: Any) -> str:
    normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()


def metadata_sidecar_path(path: Path) -> Path:
    return Path(f"{path}.meta.json")


def read_artifact_sidecar(path: Path) -> dict[str, Any] | None:
    sidecar = metadata_sidecar_path(path)
    if not sidecar.exists():
        return None
    try:
        payload = json.loads(sidecar.read_text(encoding="utf-8"))
    except Exception:
        return None
    return payload if isinstance(payload, dict) else None


def is_locked(metadata: ArtifactMetadata | dict[str, Any] | None) -> bool:
    meta = metadata if isinstance(metadata, ArtifactMetadata) else ArtifactMetadata.from_dict(metadata)
    return meta.status == "locked" or bool(meta.locked_fields.get("__artifact__"))


def mark_stale(metadata: ArtifactMetadata | dict[str, Any] | None, reason: str) -> ArtifactMetadata:
    meta = metadata if isinstance(metadata, ArtifactMetadata) else ArtifactMetadata.from_dict(metadata)
    history = list(meta.revision_history)
    history.append({"at_utc": utc_now(), "action": "mark_stale", "reason": str(reason).strip()})
    return ArtifactMetadata(
        status="stale",
        created_at_utc=meta.created_at_utc,
        updated_at_utc=utc_now(),
        source_fingerprint=meta.source_fingerprint,
        locked_fields=dict(meta.locked_fields),
        manual_overrides=dict(meta.manual_overrides),
        revision_history=history,
    )


def merge_preserving_locked_fields(old: dict[str, Any] | None, new: dict[str, Any]) -> dict[str, Any]:
    old_payload = dict(old) if isinstance(old, dict) else {}
    merged = dict(new)

    old_meta = ArtifactMetadata.from_dict(old_payload.get("metadata"), default_status=str(old_payload.get("status", "generated")))
    new_meta = ArtifactMetadata.from_dict(merged.get("metadata"), default_status=str(merged.get("status", old_meta.status or "generated")))

    if is_locked(old_meta):
        for key, value in old_payload.items():
            if key == "metadata":
                continue
            merged[key] = value
    else:
        for field_name, locked in old_meta.locked_fields.items():
            if field_name == "__artifact__" or not locked:
                continue
            if field_name in old_payload:
                merged[field_name] = old_payload[field_name]

    for field_name, value in old_meta.manual_overrides.items():
        if field_name in old_payload:
            merged[field_name] = value

    history = list(old_meta.revision_history) + [item for item in new_meta.revision_history if item not in old_meta.revision_history]
    merged_meta = ArtifactMetadata(
        status=old_meta.status if is_locked(old_meta) else new_meta.status,
        created_at_utc=old_meta.created_at_utc,
        updated_at_utc=utc_now(),
        source_fingerprint=new_meta.source_fingerprint or old_meta.source_fingerprint,
        locked_fields={**old_meta.locked_fields, **new_meta.locked_fields},
        manual_overrides={**old_meta.manual_overrides, **new_meta.manual_overrides},
        revision_history=history,
    )
    merged["metadata"] = merged_meta.to_dict()
    return merged


def write_artifact_with_metadata(
    path: Path,
    payload: dict[str, Any],
    *,
    artifact_type: str,
    status: str,
    source_fingerprint: str,
    previous_payload: dict[str, Any] | None = None,
    locked_fields: dict[str, bool] | None = None,
    manual_overrides: dict[str, Any] | None = None,
    revision_note: dict[str, Any] | None = None,
) -> dict[str, Any]:
    previous_meta = ArtifactMetadata.from_dict(previous_payload.get("metadata") if isinstance(previous_payload, dict) else None, default_status=status)
    history = list(previous_meta.revision_history)
    if revision_note:
        history.append(dict(revision_note))
    metadata = ArtifactMetadata(
        status=status,
        created_at_utc=previous_meta.created_at_utc,
        updated_at_utc=utc_now(),
        source_fingerprint=source_fingerprint,
        locked_fields=dict(locked_fields or previous_meta.locked_fields),
        manual_overrides=dict(manual_overrides or previous_meta.manual_overrides),
        revision_history=history,
    )
    to_write = dict(payload)
    to_write["artifact_type"] = artifact_type
    to_write["metadata"] = metadata.to_dict()
    if previous_payload:
        to_write = merge_preserving_locked_fields(previous_payload, to_write)
    write_json(path, to_write)
    return to_write
