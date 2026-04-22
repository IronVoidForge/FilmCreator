from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .chapter_selection import chapter_matches, parse_chapter_selector
from .core.json_io import read_json, write_json
from .scaffold import create_project


@dataclass
class SceneBindingReference:
    label: str
    canonical_id: str | None = None
    display_name: str = ""
    status: str = "unresolved"
    entity_kind: str = ""
    resolution_score: int | None = None
    source_path: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "canonical_id": self.canonical_id,
            "display_name": self.display_name,
            "status": self.status,
            "entity_kind": self.entity_kind,
            "resolution_score": self.resolution_score,
            "source_path": self.source_path,
            "notes": self.notes,
        }


@dataclass
class BeatEnvironmentOverride:
    beat_id: str
    environment: SceneBindingReference
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "beat_id": self.beat_id,
            "environment": self.environment.to_dict(),
            "reason": self.reason,
        }


@dataclass
class FutureEnvironmentRequest:
    scene_id: str
    chapter_id: str
    requested_label: str
    request_type: str
    reason: str = ""
    parent_environment_id: str | None = None
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "scene_id": self.scene_id,
            "chapter_id": self.chapter_id,
            "requested_label": self.requested_label,
            "request_type": self.request_type,
            "reason": self.reason,
            "parent_environment_id": self.parent_environment_id,
            "evidence_refs": self.evidence_refs,
        }


@dataclass
class SceneBindingMetadata:
    artifact_id: str
    artifact_type: str = "scene_binding"
    status: str = "generated"
    source_fingerprint: str | None = None
    created_at_utc: str = ""
    updated_at_utc: str = ""
    upstream_dependencies: list[dict[str, Any]] = field(default_factory=list)
    locked_fields: dict[str, bool] = field(default_factory=dict)
    manual_overrides: dict[str, Any] = field(default_factory=dict)
    revision_history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "status": self.status,
            "source_fingerprint": self.source_fingerprint,
            "created_at_utc": self.created_at_utc,
            "updated_at_utc": self.updated_at_utc,
            "upstream_dependencies": self.upstream_dependencies,
            "locked_fields": self.locked_fields,
            "manual_overrides": self.manual_overrides,
            "revision_history": self.revision_history,
        }


@dataclass
class SceneBinding:
    scene_id: str
    chapter_id: str
    binding_mode: str
    resolved_characters: list[SceneBindingReference] = field(default_factory=list)
    resolved_environment: SceneBindingReference | None = None
    beat_environment_overrides: list[BeatEnvironmentOverride] = field(default_factory=list)
    candidate_environment_ids: list[str] = field(default_factory=list)
    future_environment_requests: list[FutureEnvironmentRequest] = field(default_factory=list)
    review_flags: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    evidence_summary: list[str] = field(default_factory=list)
    metadata: SceneBindingMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "scene_id": self.scene_id,
            "chapter_id": self.chapter_id,
            "binding_mode": self.binding_mode,
            "resolved_characters": [item.to_dict() for item in self.resolved_characters],
            "resolved_environment": self.resolved_environment.to_dict() if self.resolved_environment else None,
            "beat_environment_overrides": [item.to_dict() for item in self.beat_environment_overrides],
            "candidate_environment_ids": self.candidate_environment_ids,
            "future_environment_requests": [item.to_dict() for item in self.future_environment_requests],
            "review_flags": self.review_flags,
            "notes": self.notes,
            "evidence_refs": self.evidence_refs,
            "evidence_summary": self.evidence_summary,
            "metadata": self.metadata.to_dict() if self.metadata else None,
        }


@dataclass(frozen=True)
class SceneBindingSummary:
    project_slug: str
    total_scene_entries: int
    synthesized_count: int
    reused_count: int
    stale_locked_count: int
    review_queue_count: int
    future_environment_request_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_scene_entries": self.total_scene_entries,
            "synthesized_count": self.synthesized_count,
            "reused_count": self.reused_count,
            "stale_locked_count": self.stale_locked_count,
            "review_queue_count": self.review_queue_count,
            "future_environment_request_count": self.future_environment_request_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _first_nonempty(*values: object, fallback: str = "") -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


def _compact_snippet(text: str, *, limit: int = 220) -> str:
    collapsed = " ".join(text.split()).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _normalize_optional_canonical_id(value: Any) -> str | None:
    text = str(value or "").strip()
    if not text or text.lower() in {"none", "null", "(none)", "n/a"}:
        return None
    return text


def _coerce_int(value: Any) -> int | None:
    if isinstance(value, int):
        return value
    text = str(value or "").strip()
    return int(text) if text.isdigit() else None


def _binding_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "scene_bindings"


def _scene_contract_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "scenes"


def _scene_contract_files(project_dir: Path) -> list[Path]:
    root = _scene_contract_root(project_dir)
    if not root.exists():
        return []
    return sorted(path for path in root.glob("CH*/CH*_SC*.json") if path.is_file())


def _binding_path(project_dir: Path, scene_id: str) -> Path:
    chapter_id = scene_id[:5]
    return _binding_root(project_dir) / chapter_id / f"{scene_id}_BINDINGS.json"


def _load_json_file(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    return payload if isinstance(payload, dict) else {}


def _load_existing_metadata(existing: dict[str, Any] | None, artifact_id: str, fp: str) -> SceneBindingMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return SceneBindingMetadata(
        artifact_id=artifact_id,
        status=str(old_meta.get("status", "generated")),
        source_fingerprint=fp,
        created_at_utc=str(old_meta.get("created_at_utc") or _utc_now()),
        updated_at_utc=_utc_now(),
        upstream_dependencies=old_meta.get("upstream_dependencies", []),
        locked_fields=old_meta.get("locked_fields", {}),
        manual_overrides=old_meta.get("manual_overrides", {}),
        revision_history=old_meta.get("revision_history", []),
    )


def _reference_from_raw(raw_ref: dict[str, Any]) -> SceneBindingReference:
    return SceneBindingReference(
        label=str(raw_ref.get("label", "")),
        canonical_id=_normalize_optional_canonical_id(raw_ref.get("canonical_id")),
        display_name=_first_nonempty(str(raw_ref.get("display_name", "")), str(raw_ref.get("label", "")), fallback=""),
        status=str(raw_ref.get("status", "review") or "review"),
        entity_kind=str(raw_ref.get("entity_kind", "") or ""),
        resolution_score=_coerce_int(raw_ref.get("resolution_score")),
        source_path=str(raw_ref.get("source_path", "") or ""),
        notes=str(raw_ref.get("notes", "") or ""),
    )


def _candidate_sort_key(ref: SceneBindingReference) -> tuple[int, int, str]:
    is_canonical = 1 if ref.canonical_id and ref.status == "canonical" else 0
    score = ref.resolution_score or 0
    return (is_canonical, score, ref.label.lower())


def _dedupe_refs(refs: list[SceneBindingReference]) -> list[SceneBindingReference]:
    deduped: list[SceneBindingReference] = []
    seen: set[tuple[str | None, str]] = set()
    for ref in refs:
        key = (ref.canonical_id, ref.label.lower())
        if key in seen:
            continue
        seen.add(key)
        deduped.append(ref)
    return deduped


def _append_future_environment_request(
    requests: list[FutureEnvironmentRequest],
    *,
    scene_id: str,
    chapter_id: str,
    label: str,
    reason: str,
    evidence_refs: list[dict[str, Any]],
    parent_environment_id: str | None = None,
) -> None:
    requested_label = label.strip()
    if not requested_label:
        return
    for existing in requests:
        if existing.requested_label.lower() == requested_label.lower():
            return
    requests.append(
        FutureEnvironmentRequest(
            scene_id=scene_id,
            chapter_id=chapter_id,
            requested_label=requested_label,
            request_type="missing_environment",
            reason=_compact_snippet(reason, limit=220),
            parent_environment_id=parent_environment_id,
            evidence_refs=evidence_refs[:6],
        )
    )


def _resolve_environment_binding(
    *,
    scene_contract: dict[str, Any],
    chapter_fallback: SceneBindingReference | None,
) -> tuple[str, SceneBindingReference | None, list[str], list[str], list[str], list[FutureEnvironmentRequest]]:
    scene_id = str(scene_contract.get("scene_id", "")).strip().upper()
    chapter_id = str(scene_contract.get("chapter_id", "")).strip().upper() or scene_id[:5]
    evidence_refs = scene_contract.get("evidence_refs", []) if isinstance(scene_contract.get("evidence_refs"), list) else []
    raw_refs = scene_contract.get("environments_required", [])
    refs = [_reference_from_raw(item) for item in raw_refs if isinstance(item, dict)]
    refs = _dedupe_refs(refs)
    candidate_environment_ids = [ref.canonical_id for ref in refs if ref.canonical_id]
    candidate_environment_ids = [item for item in candidate_environment_ids if item]

    review_flags: list[str] = []
    notes: list[str] = []
    future_requests: list[FutureEnvironmentRequest] = []

    canonical_refs = [ref for ref in refs if ref.canonical_id and ref.status == "canonical"]
    canonical_ids = {ref.canonical_id for ref in canonical_refs if ref.canonical_id}

    if len(canonical_ids) == 1 and canonical_refs:
        chosen = sorted(canonical_refs, key=_candidate_sort_key, reverse=True)[0]
        return "scene_level", chosen, candidate_environment_ids, review_flags, notes, future_requests

    if len(canonical_ids) > 1:
        chosen = sorted(canonical_refs, key=_candidate_sort_key, reverse=True)[0]
        review_flags.append("multiple_scene_environment_candidates")
        notes.append("Multiple canonical environments were listed; chose the highest-confidence scene-level environment.")
        return "scene_level", chosen, candidate_environment_ids, review_flags, notes, future_requests

    for ref in refs:
        if not ref.canonical_id:
            _append_future_environment_request(
                future_requests,
                scene_id=scene_id,
                chapter_id=chapter_id,
                label=ref.label or ref.display_name,
                reason=ref.notes or "Scene referenced an environment that was not canonically resolved.",
                evidence_refs=evidence_refs,
                parent_environment_id=chapter_fallback.canonical_id if chapter_fallback and chapter_fallback.canonical_id else None,
            )

    if chapter_fallback and chapter_fallback.canonical_id:
        notes.append("Inherited chapter-level environment because the scene did not resolve a canonical environment.")
        review_flags.append("scene_environment_used_chapter_fallback")
        return "chapter_fallback", chapter_fallback, candidate_environment_ids, review_flags, notes, future_requests

    unresolved = refs[0] if refs else None
    if unresolved:
        notes.append("Scene referenced a non-canonical environment and no chapter fallback was available.")
    else:
        notes.append("Scene contract did not provide an environment reference.")
    review_flags.append("scene_environment_unresolved")
    return "unresolved", unresolved, candidate_environment_ids, review_flags, notes, future_requests


def _render_scene_binding_markdown(binding: SceneBinding) -> str:
    env = binding.resolved_environment
    env_display = "(none)"
    if env:
        env_display = _first_nonempty(env.display_name, env.label, fallback=env.canonical_id or "(none)")
        if env.canonical_id:
            env_display = f"{env_display} ({env.canonical_id})"

    lines = [
        f"# Scene Binding: {binding.scene_id}",
        "",
        f"- scene_id: `{binding.scene_id}`",
        f"- chapter_id: `{binding.chapter_id}`",
        f"- binding_mode: `{binding.binding_mode}`",
        f"- resolved_environment: {env_display}",
        "",
        "## Resolved Cast",
        "",
    ]
    if binding.resolved_characters:
        for ref in binding.resolved_characters:
            display = _first_nonempty(ref.display_name, ref.label, fallback=ref.canonical_id or ref.label)
            suffix: list[str] = []
            if ref.canonical_id:
                suffix.append(ref.canonical_id)
            if ref.status:
                suffix.append(ref.status)
            lines.append(f"- {display}{f' ({', '.join(suffix)})' if suffix else ''}")
    else:
        lines.append("- (none)")

    lines.extend(["", "## Notes", ""])
    if binding.notes:
        lines.extend([f"- {item}" for item in binding.notes])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Review Flags", ""])
    if binding.review_flags:
        lines.extend([f"- {item}" for item in binding.review_flags])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Future Environment Requests", ""])
    if binding.future_environment_requests:
        for request in binding.future_environment_requests:
            lines.append(f"- {request.requested_label} ({request.request_type})")
    else:
        lines.append("- (none)")

    return "\n".join(lines) + "\n"


def _render_binding_index(records: list[SceneBinding]) -> str:
    lines = ["# Scene Binding Index", ""]
    if not records:
        lines.append("- No scene bindings.")
        return "\n".join(lines) + "\n"
    for record in records:
        env = record.resolved_environment
        env_display = _first_nonempty(env.display_name, env.label, fallback=env.canonical_id or "(none)") if env else "(none)"
        lines.append(
            f"- `{record.scene_id}` - mode={record.binding_mode}, env={env_display}, cast={len(record.resolved_characters)}, flags={len(record.review_flags)}"
        )
    return "\n".join(lines) + "\n"


def _render_review_queue(queue: list[dict[str, Any]]) -> str:
    lines = ["# Scene Binding Review Queue", ""]
    if not queue:
        lines.append("- No binding review items.")
        return "\n".join(lines) + "\n"
    for item in queue:
        lines.append(f"- `{item['scene_id']}`")
        for issue in item.get("issues", []):
            lines.append(f"  - {issue}")
    return "\n".join(lines) + "\n"


def _render_future_environment_requests(requests: list[FutureEnvironmentRequest]) -> str:
    lines = ["# Future Environment Requests", ""]
    if not requests:
        lines.append("- No future environment requests.")
        return "\n".join(lines) + "\n"
    for request in requests:
        lines.append(
            f"- `{request.scene_id}` - {request.requested_label} ({request.request_type})"
        )
    return "\n".join(lines) + "\n"


def _binding_from_existing(existing: dict[str, Any], metadata: SceneBindingMetadata) -> SceneBinding:
    resolved_environment_payload = existing.get("resolved_environment")
    resolved_environment = (
        _reference_from_raw(resolved_environment_payload)
        if isinstance(resolved_environment_payload, dict)
        else None
    )
    return SceneBinding(
        scene_id=str(existing.get("scene_id", "")),
        chapter_id=str(existing.get("chapter_id", "")),
        binding_mode=str(existing.get("binding_mode", "unresolved")),
        resolved_characters=[
            _reference_from_raw(item)
            for item in existing.get("resolved_characters", [])
            if isinstance(item, dict)
        ],
        resolved_environment=resolved_environment,
        beat_environment_overrides=[
            BeatEnvironmentOverride(
                beat_id=str(item.get("beat_id", "")),
                environment=_reference_from_raw(item.get("environment", {})),
                reason=str(item.get("reason", "")),
            )
            for item in existing.get("beat_environment_overrides", [])
            if isinstance(item, dict) and isinstance(item.get("environment"), dict)
        ],
        candidate_environment_ids=[str(item) for item in existing.get("candidate_environment_ids", []) if str(item).strip()],
        future_environment_requests=[
            FutureEnvironmentRequest(
                scene_id=str(item.get("scene_id", "")),
                chapter_id=str(item.get("chapter_id", "")),
                requested_label=str(item.get("requested_label", "")),
                request_type=str(item.get("request_type", "")),
                reason=str(item.get("reason", "")),
                parent_environment_id=_normalize_optional_canonical_id(item.get("parent_environment_id")),
                evidence_refs=item.get("evidence_refs", []) if isinstance(item.get("evidence_refs"), list) else [],
            )
            for item in existing.get("future_environment_requests", [])
            if isinstance(item, dict)
        ],
        review_flags=[str(item) for item in existing.get("review_flags", []) if str(item).strip()],
        notes=[str(item) for item in existing.get("notes", []) if str(item).strip()],
        evidence_refs=existing.get("evidence_refs", []) if isinstance(existing.get("evidence_refs"), list) else [],
        evidence_summary=existing.get("evidence_summary", []) if isinstance(existing.get("evidence_summary"), list) else [],
        metadata=metadata,
    )


def run_scene_binding_synthesis(
    project_slug: str,
    *,
    force: bool = False,
    chapters: str | None = None,
) -> SceneBindingSummary:
    project_dir = create_project(project_slug)
    selected_chapters = set(parse_chapter_selector(chapters))
    scene_contract_files = [
        path for path in _scene_contract_files(project_dir) if chapter_matches(path.parent.name or path.stem[:5], selected_chapters)
    ]
    output_root = _binding_root(project_dir)
    review_dir = output_root / "review"
    output_root.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    warnings: list[str] = []
    written_files: list[str] = []
    review_queue: list[dict[str, Any]] = []
    records: list[SceneBinding] = []
    review_records: list[SceneBinding] = []
    future_requests: list[FutureEnvironmentRequest] = []
    chapter_environment_cache: dict[str, SceneBindingReference] = {}

    total_scenes = len(scene_contract_files)
    for index, scene_contract_path in enumerate(scene_contract_files, start=1):
        scene_contract = _load_json_file(scene_contract_path)
        scene_id = str(scene_contract.get("scene_id", "")).strip().upper() or scene_contract_path.stem.upper()
        chapter_id = str(scene_contract.get("chapter_id", "")).strip().upper() or scene_id[:5]
        print(f"[scene-binding] {index}/{total_scenes} starting {scene_id}...")
        fingerprint_payload = {
            "scene_contract": scene_contract,
            "chapter_fallback_environment": chapter_environment_cache.get(chapter_id).to_dict() if chapter_environment_cache.get(chapter_id) else None,
        }
        fp = _fingerprint(fingerprint_payload)
        base_path = _binding_path(project_dir, scene_id)
        base_path.parent.mkdir(parents=True, exist_ok=True)
        existing = read_json(base_path) if base_path.exists() else None
        metadata = _load_existing_metadata(existing if isinstance(existing, dict) else None, f"{scene_id}_SCENE_BINDINGS", fp)

        if isinstance(existing, dict) and not force:
            old_meta = existing.get("metadata") or {}
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                binding = _binding_from_existing(existing, metadata)
                records.append(binding)
                if binding.resolved_environment and binding.resolved_environment.canonical_id and binding.binding_mode != "unresolved":
                    chapter_environment_cache[chapter_id] = binding.resolved_environment
                future_requests.extend(binding.future_environment_requests)
                if binding.review_flags:
                    review_records.append(binding)
                    review_queue.append({"scene_id": scene_id, "issues": list(binding.review_flags)})
                print(f"[scene-binding] {index}/{total_scenes} finished {scene_id} (reused)")
                continue

            if old_meta.get("status") == "locked":
                stale_locked += 1
                if isinstance(existing.get("metadata"), dict):
                    existing["metadata"]["status"] = "stale"
                    write_json(base_path, existing)
                warnings.append(f"Locked scene binding became stale and was not regenerated: {scene_id}")
                print(f"[scene-binding] {index}/{total_scenes} finished {scene_id} (stale locked)")
                continue

        resolved_characters = _dedupe_refs(
            [
                _reference_from_raw(item)
                for item in scene_contract.get("characters_required", [])
                if isinstance(item, dict)
            ]
        )
        binding_mode, resolved_environment, candidate_environment_ids, review_flags, notes, scene_requests = _resolve_environment_binding(
            scene_contract=scene_contract,
            chapter_fallback=chapter_environment_cache.get(chapter_id),
        )
        future_requests.extend(scene_requests)

        unresolved_characters = [
            ref for ref in resolved_characters if ref.status != "canonical" or not ref.canonical_id
        ]
        if unresolved_characters:
            review_flags.append("scene_cast_contains_unresolved_references")
            notes.append(f"{len(unresolved_characters)} scene cast reference(s) still require review.")

        metadata.upstream_dependencies = [
            {
                "dependency_type": "scene_contract",
                "dependency_id": scene_id,
                "version": _fingerprint(scene_contract),
            }
        ]
        metadata.revision_history.append(
            {
                "timestamp_utc": _utc_now(),
                "action": "synthesized",
                "source_fingerprint": fp,
            }
        )

        binding = SceneBinding(
            scene_id=scene_id,
            chapter_id=chapter_id,
            binding_mode=binding_mode,
            resolved_characters=resolved_characters,
            resolved_environment=resolved_environment,
            beat_environment_overrides=[],
            candidate_environment_ids=candidate_environment_ids,
            future_environment_requests=scene_requests,
            review_flags=review_flags,
            notes=notes,
            evidence_refs=scene_contract.get("evidence_refs", []) if isinstance(scene_contract.get("evidence_refs"), list) else [],
            evidence_summary=scene_contract.get("evidence_summary", []) if isinstance(scene_contract.get("evidence_summary"), list) else [],
            metadata=metadata,
        )

        write_json(base_path, binding.to_dict())
        base_path.with_suffix(".md").write_text(_render_scene_binding_markdown(binding), encoding="utf-8")
        written_files.extend([str(base_path), str(base_path.with_suffix(".md"))])
        records.append(binding)
        synthesized += 1

        if resolved_environment and resolved_environment.canonical_id and binding_mode != "unresolved":
            chapter_environment_cache[chapter_id] = resolved_environment

        if review_flags:
            review_records.append(binding)
            review_queue.append({"scene_id": scene_id, "issues": review_flags})

        print(f"[scene-binding] {index}/{total_scenes} finished {scene_id} (synthesized)")

    write_json(output_root / "SCENE_BINDING_INDEX.json", [record.to_dict() for record in records])
    (output_root / "SCENE_BINDING_INDEX.md").write_text(_render_binding_index(records), encoding="utf-8")
    write_json(output_root / "SCENE_BINDING_REVIEW_INDEX.json", [record.to_dict() for record in review_records])
    (output_root / "SCENE_BINDING_REVIEW_INDEX.md").write_text(_render_binding_index(review_records), encoding="utf-8")
    write_json(review_dir / "SCENE_BINDING_REVIEW_QUEUE.json", review_queue)
    (review_dir / "SCENE_BINDING_REVIEW_QUEUE.md").write_text(_render_review_queue(review_queue), encoding="utf-8")
    write_json(output_root / "FUTURE_ENVIRONMENT_REQUESTS.json", [item.to_dict() for item in future_requests])
    (output_root / "FUTURE_ENVIRONMENT_REQUESTS.md").write_text(_render_future_environment_requests(future_requests), encoding="utf-8")

    written_files.extend(
        [
            str(output_root / "SCENE_BINDING_INDEX.json"),
            str(output_root / "SCENE_BINDING_INDEX.md"),
            str(output_root / "SCENE_BINDING_REVIEW_INDEX.json"),
            str(output_root / "SCENE_BINDING_REVIEW_INDEX.md"),
            str(review_dir / "SCENE_BINDING_REVIEW_QUEUE.json"),
            str(review_dir / "SCENE_BINDING_REVIEW_QUEUE.md"),
            str(output_root / "FUTURE_ENVIRONMENT_REQUESTS.json"),
            str(output_root / "FUTURE_ENVIRONMENT_REQUESTS.md"),
        ]
    )

    return SceneBindingSummary(
        project_slug=project_slug,
        total_scene_entries=len(scene_contract_files),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        future_environment_request_count=len(future_requests),
        written_files=written_files,
        warnings=warnings,
    )
