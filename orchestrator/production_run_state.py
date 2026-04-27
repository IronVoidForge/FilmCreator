from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def persist_run_summary(
    *,
    project_slug: str,
    run_type: str,
    payload: dict[str, Any],
    repo_root: Path | None = None,
) -> str:
    root = (repo_root or Path.cwd()).resolve()
    project_root = root / "projects" / project_slug
    run_dir = project_root / "02_story_analysis" / "runs" / "production"
    run_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_run_type = run_type.replace(" ", "_").replace("/", "_")
    run_path = run_dir / f"{stamp}_{safe_run_type}.json"
    latest_path = run_dir / "production_menu_latest.json"

    wrapped = {
        "run_type": run_type,
        "project_slug": project_slug,
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "payload": payload,
    }
    text = json.dumps(wrapped, indent=2)
    run_path.write_text(text, encoding="utf-8")
    latest_path.write_text(text, encoding="utf-8")
    return str(run_path)
