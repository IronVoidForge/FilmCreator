from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core.json_io import read_json, write_json
from .prompt_package import parse_prompt_package
from .scaffold import create_project

REFERENCE_ASSET_SCHEMA_VERSION = "2026-04-23-reference-assets-v1"
REFERENCE_ASSET_ROOT = Path("03_reference_assets")

CHARACTER_DEFAULT_VARIANTS = ["full_body_neutral", "bust_portrait", "profile_view"]
ENVIRONMENT_DEFAULT_VARIANTS = ["establishing_wide", "medium_spatial", "detail_focus"]

CHARACTER_CANONICAL_VARIANT = "full_body_neutral"
ENVIRONMENT_CANONICAL_VARIANT = "establishing_wide"

VALID_APPROVAL_STATES = {"unreviewed", "approved", "rejected", "locked", "stale"}


@dataclass(frozen=True)
class ReferencePhaseSummary:
    project_slug: str
    asset_kind: str
    planned_count: int
    candidate_count: int
    approved_count: int
    locked_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "asset_kind": self.asset_kind,
            "planned_count": self.planned_count,
            "candidate_count": self.candidate_count,
            "approved_count": self.approved_count,
            "locked_count": self.locked_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_asset_kind(asset_kind: str) -> str:
    cleaned = asset_kind.strip().lower()
    if cleaned not in {"character", "environment"}:
        raise ValueError(f"Unsupported reference asset kind: {asset_kind}")
    return cleaned


def normalize_id(value: str) -> str:
    return value.strip().lower()


def plural_kind(asset_kind: str) -> str:
    kind = normalize_asset_kind(asset_kind)
    return "characters" if kind == "character" else "environments"


def id_field(asset_kind: str) -> str:
    kind = normalize_asset_kind(asset_kind)
    return "character_id" if kind == "character" else "environment_id"


def canonical_variant(asset_kind: str) -> str:
    kind = normalize_asset_kind(asset_kind)
    return CHARACTER_CANONICAL_VARIANT if kind == "character" else ENVIRONMENT_CANONICAL_VARIANT


def default_variants(asset_kind: str) -> list[str]:
    kind = normalize_asset_kind(asset_kind)
    return list(CHARACTER_DEFAULT_VARIANTS if kind == "character" else ENVIRONMENT_DEFAULT_VARIANTS)


def reference_root(project_dir: Path, asset_kind: str) -> Path:
    return project_dir / REFERENCE_ASSET_ROOT / plural_kind(asset_kind)


def queue_path(project_dir: Path, asset_kind: str) -> Path:
    prefix = normalize_asset_kind(asset_kind).upper()
    return reference_root(project_dir, asset_kind) / f"{prefix}_REFERENCE_QUEUE.json"


def queue_markdown_path(project_dir: Path, asset_kind: str) -> Path:
    prefix = normalize_asset_kind(asset_kind).upper()
    return reference_root(project_dir, asset_kind) / f"{prefix}_REFERENCE_QUEUE.md"


def review_queue_path(project_dir: Path, asset_kind: str) -> Path:
    prefix = normalize_asset_kind(asset_kind).upper()
    return reference_root(project_dir, asset_kind) / "review" / f"{prefix}_REFERENCE_REVIEW_QUEUE.md"


def approved_path(project_dir: Path, asset_kind: str) -> Path:
    prefix = normalize_asset_kind(asset_kind).upper()
    return reference_root(project_dir, asset_kind) / f"APPROVED_{prefix}_REFERENCES.json"


def approved_markdown_path(project_dir: Path, asset_kind: str) -> Path:
    prefix = normalize_asset_kind(asset_kind).upper()
    return reference_root(project_dir, asset_kind) / f"APPROVED_{prefix}_REFERENCES.md"


def candidates_path(project_dir: Path, asset_kind: str, asset_id: str) -> Path:
    return reference_root(project_dir, asset_kind) / normalize_id(asset_id) / "REFERENCE_CANDIDATES.json"


def candidates_markdown_path(project_dir: Path, asset_kind: str, asset_id: str) -> Path:
    return reference_root(project_dir, asset_kind) / normalize_id(asset_id) / "REFERENCE_CANDIDATES.md"


def load_reference_queue(project_dir: Path, asset_kind: str) -> list[dict[str, Any]]:
    path = queue_path(project_dir, asset_kind)
    if not path.exists():
        return []
    payload = read_json(path)
    return payload if isinstance(payload, list) else []


def write_reference_queue(project_dir: Path, asset_kind: str, entries: list[dict[str, Any]]) -> list[str]:
    entries = sorted(entries, key=lambda item: (str(item.get("asset_id", "")), str(item.get("variant_key", ""))))
    json_path = queue_path(project_dir, asset_kind)
    md_path = queue_markdown_path(project_dir, asset_kind)
    review_path = review_queue_path(project_dir, asset_kind)
    write_json(json_path, entries)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_queue_markdown(asset_kind, entries), encoding="utf-8")
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(render_queue_review_markdown(asset_kind, entries), encoding="utf-8")
    return [str(json_path), str(md_path), str(review_path)]


def load_candidates(project_dir: Path, asset_kind: str, asset_id: str) -> list[dict[str, Any]]:
    path = candidates_path(project_dir, asset_kind, asset_id)
    if not path.exists():
        return []
    payload = read_json(path)
    return payload if isinstance(payload, list) else []


def write_candidates(project_dir: Path, asset_kind: str, asset_id: str, candidates: list[dict[str, Any]]) -> list[str]:
    candidates = sorted(candidates, key=lambda item: str(item.get("candidate_id", "")))
    json_path = candidates_path(project_dir, asset_kind, asset_id)
    md_path = candidates_markdown_path(project_dir, asset_kind, asset_id)
    write_json(json_path, candidates)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_candidates_markdown(asset_kind, asset_id, candidates), encoding="utf-8")
    return [str(json_path), str(md_path)]


def load_approved_manifest(project_dir: Path, asset_kind: str) -> list[dict[str, Any]]:
    path = approved_path(project_dir, asset_kind)
    if not path.exists():
        return []
    payload = read_json(path)
    return payload if isinstance(payload, list) else []


def write_approved_manifest(project_dir: Path, asset_kind: str, approved: list[dict[str, Any]]) -> list[str]:
    approved = sorted(approved, key=lambda item: str(item.get("asset_id", "")))
    json_path = approved_path(project_dir, asset_kind)
    md_path = approved_markdown_path(project_dir, asset_kind)
    write_json(json_path, approved)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_approved_markdown(asset_kind, approved), encoding="utf-8")
    return [str(json_path), str(md_path)]


def find_queue_entry(entries: list[dict[str, Any]], asset_id: str, variant_key: str) -> dict[str, Any] | None:
    normalized_asset_id = normalize_id(asset_id)
    normalized_variant = variant_key.strip().lower()
    for entry in entries:
        if normalize_id(str(entry.get("asset_id", ""))) == normalized_asset_id and str(entry.get("variant_key", "")).strip().lower() == normalized_variant:
            return entry
    return None


def find_candidate(project_dir: Path, asset_kind: str, candidate_id: str) -> tuple[str, dict[str, Any], list[dict[str, Any]]] | None:
    root = reference_root(project_dir, asset_kind)
    if not root.exists():
        return None
    target = candidate_id.strip()
    for path in sorted(root.glob("*/REFERENCE_CANDIDATES.json")):
        asset_id = path.parent.name
        candidates = load_candidates(project_dir, asset_kind, asset_id)
        for candidate in candidates:
            if str(candidate.get("candidate_id", "")).strip() == target:
                return asset_id, candidate, candidates
    return None


def next_candidate_id(existing: list[dict[str, Any]], asset_id: str, variant_key: str) -> str:
    prefix = f"{normalize_id(asset_id)}_{variant_key.strip().lower()}_cand_"
    highest = 0
    for candidate in existing:
        candidate_id = str(candidate.get("candidate_id", ""))
        if not candidate_id.startswith(prefix):
            continue
        suffix = candidate_id[len(prefix):]
        if suffix.isdigit():
            highest = max(highest, int(suffix))
    return f"{prefix}{highest + 1:03d}"


def prompt_package_path(project_dir: Path, asset_kind: str, asset_id: str, variant_key: str) -> Path:
    return project_dir / "03_prompt_packages" / "prepared" / plural_kind(asset_kind) / normalize_id(asset_id) / f"{variant_key.strip().lower()}_prompt.md"


def validate_prompt_package(path: Path, required_inputs: set[str]) -> list[str]:
    warnings: list[str] = []
    if not path.exists():
        return ["missing prompt package"]
    try:
        package = parse_prompt_package(path)
    except Exception as exc:  # pragma: no cover - defensive parser boundary
        return [f"prompt package parse failed: {exc}"]
    missing = sorted(key for key in required_inputs if not str(package.inputs.get(key, "")).strip())
    warnings.extend(f"missing input `{key}`" for key in missing)
    if not package.positive_prompt.strip():
        warnings.append("missing positive prompt")
    if len(package.positive_prompt.split()) < 12:
        warnings.append("positive prompt appears thin")
    return warnings


def make_reference_request(
    *,
    asset_kind: str,
    asset_id: str,
    variant_key: str,
    prompt_path: Path,
    priority: str,
    warnings: list[str],
) -> dict[str, Any]:
    status = "blocked" if warnings else "planned"
    return {
        "schema_version": REFERENCE_ASSET_SCHEMA_VERSION,
        "reference_request_id": f"{normalize_id(asset_id)}_{variant_key.strip().lower()}",
        "asset_kind": normalize_asset_kind(asset_kind),
        "asset_id": normalize_id(asset_id),
        "variant_key": variant_key.strip().lower(),
        "prompt_package_path": str(prompt_path),
        "status": status,
        "approval_state": "unreviewed",
        "locked": False,
        "priority": priority,
        "candidate_ids": [],
        "selected_candidate_id": "",
        "review_notes": [],
        "warnings": warnings,
        "updated_at": utc_now(),
    }


def register_reference_candidate(
    project_slug: str,
    *,
    asset_kind: str,
    asset_id: str,
    variant_key: str,
    image_path: str,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    kind = normalize_asset_kind(asset_kind)
    normalized_asset_id = normalize_id(asset_id)
    normalized_variant = variant_key.strip().lower()
    queue = load_reference_queue(project_dir, kind)
    request = find_queue_entry(queue, normalized_asset_id, normalized_variant)
    warnings: list[str] = []
    prompt_path = prompt_package_path(project_dir, kind, normalized_asset_id, normalized_variant)
    if request is None:
        warnings.append("candidate registered without an existing reference queue entry")
    else:
        prompt_path = Path(str(request.get("prompt_package_path", prompt_path)))
    candidates = load_candidates(project_dir, kind, normalized_asset_id)
    candidate_id = next_candidate_id(candidates, normalized_asset_id, normalized_variant)
    candidate = {
        "schema_version": REFERENCE_ASSET_SCHEMA_VERSION,
        "candidate_id": candidate_id,
        "asset_kind": kind,
        "asset_id": normalized_asset_id,
        "variant_key": normalized_variant,
        "source_prompt_package": str(prompt_path),
        "image_path": image_path,
        "approval_state": "unreviewed",
        "locked": False,
        "is_selected": False,
        "review_notes": [],
        "created_at": utc_now(),
        "updated_at": utc_now(),
    }
    candidates.append(candidate)
    written = write_candidates(project_dir, kind, normalized_asset_id, candidates)
    if request is not None:
        candidate_ids = [str(item) for item in request.get("candidate_ids", []) if str(item).strip()]
        if candidate_id not in candidate_ids:
            candidate_ids.append(candidate_id)
        request["candidate_ids"] = candidate_ids
        request["status"] = "generated"
        request["updated_at"] = utc_now()
        written.extend(write_reference_queue(project_dir, kind, queue))
    written.extend(write_approved_manifest(project_dir, kind, load_approved_manifest(project_dir, kind)))
    return summarize_reference_phase(project_slug, kind, project_dir, warnings=warnings, written_files=written)


def approve_reference_candidate(project_slug: str, *, asset_kind: str, candidate_id: str) -> ReferencePhaseSummary:
    return set_candidate_state(project_slug, asset_kind=asset_kind, candidate_id=candidate_id, state="approved")


def reject_reference_candidate(project_slug: str, *, asset_kind: str, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return set_candidate_state(project_slug, asset_kind=asset_kind, candidate_id=candidate_id, state="rejected", reason=reason)


def lock_reference_candidate(project_slug: str, *, asset_kind: str, candidate_id: str) -> ReferencePhaseSummary:
    return set_candidate_state(project_slug, asset_kind=asset_kind, candidate_id=candidate_id, state="locked")


def set_candidate_state(
    project_slug: str,
    *,
    asset_kind: str,
    candidate_id: str,
    state: str,
    reason: str | None = None,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    kind = normalize_asset_kind(asset_kind)
    if state not in VALID_APPROVAL_STATES:
        raise ValueError(f"Unsupported approval state: {state}")
    found = find_candidate(project_dir, kind, candidate_id)
    if found is None:
        raise ValueError(f"Reference candidate not found: {candidate_id}")
    asset_id, candidate, candidates = found
    candidate["approval_state"] = state
    candidate["locked"] = state == "locked" or bool(candidate.get("locked"))
    candidate["updated_at"] = utc_now()
    notes = [str(item) for item in candidate.get("review_notes", []) if str(item).strip()]
    if reason:
        notes.append(reason)
    candidate["review_notes"] = notes
    written = write_candidates(project_dir, kind, asset_id, candidates)
    queue = load_reference_queue(project_dir, kind)
    request = find_queue_entry(queue, asset_id, str(candidate.get("variant_key", "")))
    if request is not None:
        request["approval_state"] = state
        request["locked"] = state == "locked" or bool(request.get("locked"))
        if state in {"approved", "locked"}:
            request["selected_candidate_id"] = candidate_id
            request["status"] = "approved" if state == "approved" else "locked"
        elif state == "rejected":
            request["status"] = "rejected"
        request["updated_at"] = utc_now()
        written.extend(write_reference_queue(project_dir, kind, queue))
    approved = upsert_approved_reference(project_dir, kind, candidate)
    written.extend(write_approved_manifest(project_dir, kind, approved))
    return summarize_reference_phase(project_slug, kind, project_dir, warnings=[], written_files=written)


def upsert_approved_reference(project_dir: Path, asset_kind: str, candidate: dict[str, Any]) -> list[dict[str, Any]]:
    kind = normalize_asset_kind(asset_kind)
    approved = load_approved_manifest(project_dir, kind)
    asset_id = normalize_id(str(candidate.get("asset_id", "")))
    variant = str(candidate.get("variant_key", "")).strip().lower()
    state = str(candidate.get("approval_state", "")).strip().lower()
    existing = next((item for item in approved if normalize_id(str(item.get("asset_id", ""))) == asset_id), None)
    if existing is None:
        existing = {
            "schema_version": REFERENCE_ASSET_SCHEMA_VERSION,
            "asset_kind": kind,
            "asset_id": asset_id,
            "canonical_reference_candidate_id": "",
            "canonical_reference_image": "",
            "supporting_references": {},
            "locked": False,
            "usable_for_downstream": False,
            "review_notes": [],
            "updated_at": utc_now(),
        }
        approved.append(existing)
    if state in {"approved", "locked"}:
        image_path = str(candidate.get("image_path", ""))
        if variant == canonical_variant(kind) or not existing.get("canonical_reference_candidate_id"):
            existing["canonical_reference_candidate_id"] = str(candidate.get("candidate_id", ""))
            existing["canonical_reference_image"] = image_path
        else:
            supporting = existing.get("supporting_references", {})
            if not isinstance(supporting, dict):
                supporting = {}
            supporting[variant] = image_path
            existing["supporting_references"] = supporting
        existing["locked"] = bool(existing.get("locked")) or state == "locked"
        existing["usable_for_downstream"] = bool(existing.get("canonical_reference_image")) and (bool(existing.get("locked")) or state == "approved")
        existing["updated_at"] = utc_now()
    return approved


def summarize_reference_phase(
    project_slug: str,
    asset_kind: str,
    project_dir: Path,
    *,
    warnings: list[str],
    written_files: list[str],
) -> ReferencePhaseSummary:
    kind = normalize_asset_kind(asset_kind)
    queue = load_reference_queue(project_dir, kind)
    approved = load_approved_manifest(project_dir, kind)
    candidate_count = 0
    root = reference_root(project_dir, kind)
    if root.exists():
        for path in root.glob("*/REFERENCE_CANDIDATES.json"):
            payload = read_json(path)
            if isinstance(payload, list):
                candidate_count += len(payload)
    review_count = sum(1 for item in queue if item.get("warnings") or str(item.get("status", "")) in {"blocked", "rejected"})
    locked_count = sum(1 for item in approved if item.get("locked"))
    return ReferencePhaseSummary(
        project_slug=project_slug,
        asset_kind=kind,
        planned_count=len(queue),
        candidate_count=candidate_count,
        approved_count=len([item for item in approved if item.get("canonical_reference_image")]),
        locked_count=locked_count,
        review_queue_count=review_count,
        written_files=sorted(set(written_files)),
        warnings=warnings,
    )


def render_queue_markdown(asset_kind: str, entries: list[dict[str, Any]]) -> str:
    title = "Character" if normalize_asset_kind(asset_kind) == "character" else "Environment"
    lines = [f"# {title} Reference Queue", "", "| Asset | Variant | Status | Approval | Locked | Prompt Package | Notes |", "|---|---|---|---|---|---|---|"]
    for entry in entries:
        notes = "; ".join([*entry.get("warnings", []), *entry.get("review_notes", [])])
        lines.append(
            "| {asset} | {variant} | {status} | {approval} | {locked} | `{prompt}` | {notes} |".format(
                asset=entry.get("asset_id", ""),
                variant=entry.get("variant_key", ""),
                status=entry.get("status", ""),
                approval=entry.get("approval_state", ""),
                locked="yes" if entry.get("locked") else "no",
                prompt=entry.get("prompt_package_path", ""),
                notes=notes or "ready",
            )
        )
    lines.append("")
    return "\n".join(lines)


def render_queue_review_markdown(asset_kind: str, entries: list[dict[str, Any]]) -> str:
    title = "Character" if normalize_asset_kind(asset_kind) == "character" else "Environment"
    lines = [f"# {title} Reference Review Queue", ""]
    review_entries = [item for item in entries if item.get("warnings") or str(item.get("status", "")) in {"blocked", "rejected"}]
    if not review_entries:
        lines.append("No reference queue issues.")
        lines.append("")
        return "\n".join(lines)
    for entry in review_entries:
        lines.append(f"## {entry.get('asset_id')} / {entry.get('variant_key')}")
        lines.append("")
        lines.append(f"- Status: {entry.get('status', '')}")
        lines.append(f"- Prompt: `{entry.get('prompt_package_path', '')}`")
        for warning in entry.get("warnings", []):
            lines.append(f"- Warning: {warning}")
        for note in entry.get("review_notes", []):
            lines.append(f"- Note: {note}")
        lines.append("")
    return "\n".join(lines)


def render_candidates_markdown(asset_kind: str, asset_id: str, candidates: list[dict[str, Any]]) -> str:
    title = "Character" if normalize_asset_kind(asset_kind) == "character" else "Environment"
    lines = [f"# {title} Reference Candidates: {normalize_id(asset_id)}", "", "| Candidate | Variant | Approval | Locked | Image | Notes |", "|---|---|---|---|---|---|"]
    for candidate in candidates:
        lines.append(
            "| {candidate} | {variant} | {approval} | {locked} | `{image}` | {notes} |".format(
                candidate=candidate.get("candidate_id", ""),
                variant=candidate.get("variant_key", ""),
                approval=candidate.get("approval_state", ""),
                locked="yes" if candidate.get("locked") else "no",
                image=candidate.get("image_path", ""),
                notes="; ".join(candidate.get("review_notes", [])) or "",
            )
        )
    lines.append("")
    return "\n".join(lines)


def render_approved_markdown(asset_kind: str, approved: list[dict[str, Any]]) -> str:
    title = "Character" if normalize_asset_kind(asset_kind) == "character" else "Environment"
    lines = [f"# Approved {title} References", ""]
    if not approved:
        lines.append("No approved references yet.")
        lines.append("")
        return "\n".join(lines)
    for entry in approved:
        lines.append(f"## {entry.get('asset_id', '')}")
        lines.append("")
        lines.append(f"- Canonical candidate: `{entry.get('canonical_reference_candidate_id', '')}`")
        lines.append(f"- Canonical image: `{entry.get('canonical_reference_image', '')}`")
        lines.append(f"- Locked: {'yes' if entry.get('locked') else 'no'}")
        lines.append(f"- Usable downstream: {'yes' if entry.get('usable_for_downstream') else 'no'}")
        supporting = entry.get("supporting_references", {})
        if isinstance(supporting, dict) and supporting:
            lines.append("- Supporting references:")
            for variant, image in sorted(supporting.items()):
                lines.append(f"  - {variant}: `{image}`")
        lines.append("")
    return "\n".join(lines)
