from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import time

from .character_bible_models import (
    CharacterBible,
    CharacterBibleMetadata,
    CharacterBibleSynthesisSummary,
)
from .character_bible_fallback import (
    needs_visual_production_fallback,
    deterministic_visual_fallback,
    visual_field_audit,
    fallback_result_audit,
)
from .character_bible_writer import (
    write_character_bible_index,
    write_character_bible_review_index,
    write_character_bible_markdown,
    write_character_review_queue_markdown,
)
from .core.json_io import read_json, write_json
from .core.paths import ROOT
from .book_librarian import search_book_index, search_chapter_context
from .lmstudio_client import LMStudioClient
from .settings import load_runtime_settings
from .scaffold import create_project
from .features.authoring.packet_parser import parse_packet_document
from .world_global import global_character_registry_path


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _write_fallback_diagnostics_markdown(path: Path, diagnostics: list[dict[str, Any]], project_slug: str) -> None:
    lines = [
        f"# Character Bible Fallback Diagnostics",
        f"",
        f"**Project:** {project_slug}",
        f"**Total Records:** {len(diagnostics)}",
        f"**Attempted:** {sum(1 for item in diagnostics if item['fallback_attempted'])}",
        f"**Non-Empty:** {sum(1 for item in diagnostics if item['fallback_result_audit']['non_empty'])}",
        f"",
        f"| Character | Missing | Attempted | Bucket | Filled | Status | Preview |",
        f"|-----------|---------|-----------|--------|--------|--------|---------|",
    ]
    
    for item in diagnostics:
        char_id = item["character_id"]
        missing = item["pre_fallback_audit"]["missing_count"]
        total = item["pre_fallback_audit"]["total_prompt_critical_fields"]
        attempted = "yes" if item["fallback_attempted"] else "no"
        bucket = item["fallback_result_audit"].get("fallback_bucket") or "none"
        filled = item["fallback_result_audit"]["filled_count"]
        filled_total = filled + item["fallback_result_audit"]["empty_count"]
        status = item["fallback_result_audit"].get("status") or "none"
        preview = item["fallback_preview"].get("production_body_descriptor") or item["fallback_preview"].get("production_identity_descriptor") or ""
        preview = preview[:60] + "..." if len(preview) > 60 else preview
        
        lines.append(f"| {char_id} | {missing}/{total} | {attempted} | {bucket} | {filled}/{filled_total} | {status} | {preview} |")
    
    path.write_text("\n".join(lines), encoding="utf-8")
