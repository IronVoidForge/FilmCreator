from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .core.json_io import read_json, write_json
from .core.paths import ensure_dir, repo_relative
from .scaffold import create_project


DOWNSTREAM_PHASE_ORDER = [
    "scene_contracts",
    "scene_bindings",
    "shot_packages",
    "dialogue_timeline",
    "descriptor_enrichment",
    "prompt_preparation",
]


def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _runs_dir(project_slug: str) -> Path:
    path = create_project(project_slug) / "02_story_analysis" / "runs" / "downstream"
    ensure_dir(path)
    return path


def _sanitize_run_id(run_id: str) -> str:
    return "".join(ch for ch in run_id if ch.isalnum() or ch in {"-", "_"})


@dataclass(frozen=True)
class DownstreamRunSummary:
    project_slug: str
    run_id: str
    pipeline_key: str
    status: str
    current_phase: str | None
    state_path: str
    written_files: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "run_id": self.run_id,
            "pipeline_key": self.pipeline_key,
            "status": self.status,
            "current_phase": self.current_phase,
            "state_path": self.state_path,
            "written_files": self.written_files,
        }


class DownstreamRunTracker:
    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload

    @property
    def project_slug(self) -> str:
        return str(self.payload.get("project_slug", "")).strip()

    @property
    def run_id(self) -> str:
        return str(self.payload.get("run_id", "")).strip()

    @property
    def pipeline_key(self) -> str:
        return str(self.payload.get("pipeline_key", "downstream_pipeline")).strip() or "downstream_pipeline"

    @property
    def config_signature(self) -> str:
        return str(self.payload.get("config_signature", "")).strip()

    @property
    def current_phase(self) -> str | None:
        value = self.payload.get("current_phase")
        return str(value).strip() if isinstance(value, str) and value.strip() else None

    @property
    def latest_path(self) -> Path:
        return _runs_dir(self.project_slug) / f"{self.pipeline_key}_latest.json"

    @property
    def run_path(self) -> Path:
        return _runs_dir(self.project_slug) / f"{self.pipeline_key}_{_sanitize_run_id(self.run_id)}.json"

    @classmethod
    def start_or_resume(
        cls,
        *,
        project_slug: str,
        pipeline_key: str,
        config: dict[str, Any],
        resume: bool = True,
    ) -> "DownstreamRunTracker":
        runs_dir = _runs_dir(project_slug)
        latest_path = runs_dir / f"{pipeline_key}_latest.json"
        config_signature = _fingerprint(config)

        if resume and latest_path.exists():
            existing = read_json(latest_path)
            if (
                isinstance(existing, dict)
                and str(existing.get("project_slug", "")).strip() == project_slug
                and str(existing.get("pipeline_key", "")).strip() == pipeline_key
                and str(existing.get("config_signature", "")).strip() == config_signature
                and str(existing.get("status", "")).strip() in {"running", "failed"}
            ):
                tracker = cls(existing)
                tracker.payload["status"] = "running"
                tracker.payload["updated_at_utc"] = _utc_now()
                tracker._save()
                return tracker

        started_at_utc = _utc_now()
        run_id = f"{started_at_utc.replace(':', '').replace('-', '')}_{uuid.uuid4().hex[:8]}"
        payload: dict[str, Any] = {
            "project_slug": project_slug,
            "pipeline_key": pipeline_key,
            "run_id": run_id,
            "status": "running",
            "started_at_utc": started_at_utc,
            "updated_at_utc": started_at_utc,
            "completed_at_utc": None,
            "current_phase": None,
            "config": config,
            "config_signature": config_signature,
            "phases": {
                phase: {
                    "status": "pending",
                    "total_items": None,
                    "completed_items": 0,
                    "items": {},
                    "summary": None,
                    "started_at_utc": None,
                    "completed_at_utc": None,
                }
                for phase in DOWNSTREAM_PHASE_ORDER
            },
            "written_files": [
                repo_relative(latest_path),
                repo_relative(runs_dir / f"{pipeline_key}_{_sanitize_run_id(run_id)}.json"),
            ],
        }
        tracker = cls(payload)
        tracker._save()
        return tracker

    @classmethod
    def load_latest(
        cls,
        *,
        project_slug: str,
        pipeline_key: str,
    ) -> "DownstreamRunTracker | None":
        latest_path = _runs_dir(project_slug) / f"{pipeline_key}_latest.json"
        if not latest_path.exists():
            return None
        payload = read_json(latest_path)
        if not isinstance(payload, dict):
            return None
        return cls(payload)

    def _phase_payload(self, phase_name: str) -> dict[str, Any]:
        phases = self.payload.setdefault("phases", {})
        phase = phases.setdefault(
            phase_name,
            {
                "status": "pending",
                "total_items": None,
                "completed_items": 0,
                "items": {},
                "summary": None,
                "started_at_utc": None,
                "completed_at_utc": None,
            },
        )
        if not isinstance(phase.get("items"), dict):
            phase["items"] = {}
        return phase

    def _save(self) -> None:
        self.payload["updated_at_utc"] = _utc_now()
        write_json(self.latest_path, self.payload)
        write_json(self.run_path, self.payload)

    def set_phase_running(self, phase_name: str, *, total_items: int | None = None) -> None:
        phase = self._phase_payload(phase_name)
        if phase.get("started_at_utc") is None:
            phase["started_at_utc"] = _utc_now()
        if total_items is not None:
            phase["total_items"] = int(total_items)
        phase["status"] = "running"
        self.payload["current_phase"] = phase_name
        self.payload["status"] = "running"
        self._save()

    def set_phase_total(self, phase_name: str, total_items: int) -> None:
        phase = self._phase_payload(phase_name)
        phase["total_items"] = int(total_items)
        self._save()

    def phase_completed(self, phase_name: str) -> bool:
        return str(self._phase_payload(phase_name).get("status", "")).strip() == "completed"

    def is_item_completed(self, phase_name: str, item_id: str, fingerprint: str) -> bool:
        phase = self._phase_payload(phase_name)
        items = phase.get("items", {})
        record = items.get(item_id, {}) if isinstance(items, dict) else {}
        return (
            isinstance(record, dict)
            and str(record.get("status", "")).strip() == "completed"
            and str(record.get("fingerprint", "")).strip() == fingerprint
        )

    def mark_item_completed(
        self,
        phase_name: str,
        item_id: str,
        fingerprint: str,
        *,
        outputs: list[str] | None = None,
    ) -> None:
        phase = self._phase_payload(phase_name)
        items = phase.setdefault("items", {})
        if not isinstance(items, dict):
            items = {}
            phase["items"] = items
        items[item_id] = {
            "status": "completed",
            "fingerprint": fingerprint,
            "completed_at_utc": _utc_now(),
            "outputs": outputs or [],
        }
        phase["completed_items"] = sum(
            1
            for value in items.values()
            if isinstance(value, dict) and str(value.get("status", "")).strip() == "completed"
        )
        self._save()

    def mark_phase_completed(self, phase_name: str, *, summary: dict[str, Any] | None = None) -> None:
        phase = self._phase_payload(phase_name)
        phase["status"] = "completed"
        phase["completed_at_utc"] = _utc_now()
        phase["summary"] = summary
        self.payload["current_phase"] = phase_name
        self._save()

    def mark_failed(self, phase_name: str, exc: Exception) -> None:
        phase = self._phase_payload(phase_name)
        phase["status"] = "failed"
        phase["failed_at_utc"] = _utc_now()
        phase["error"] = {
            "type": type(exc).__name__,
            "message": str(exc),
        }
        self.payload["status"] = "failed"
        self.payload["current_phase"] = phase_name
        self.payload["completed_at_utc"] = None
        self._save()

    def mark_run_completed(self) -> DownstreamRunSummary:
        self.payload["status"] = "completed"
        self.payload["completed_at_utc"] = _utc_now()
        self._save()
        return DownstreamRunSummary(
            project_slug=self.project_slug,
            run_id=self.run_id,
            pipeline_key=self.pipeline_key,
            status=str(self.payload.get("status", "completed")),
            current_phase=self.current_phase,
            state_path=repo_relative(self.latest_path),
            written_files=list(self.payload.get("written_files", [])),
        )
