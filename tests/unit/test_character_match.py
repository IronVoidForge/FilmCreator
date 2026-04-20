from __future__ import annotations

import json
from pathlib import Path

import orchestrator.book_ingest as book_ingest_module
import orchestrator.character_match as character_match_module


def test_character_match_candidates_use_registry_and_chapter_context(tmp_path: Path, monkeypatch) -> None:
    project_dir = tmp_path / "projects" / "demo"
    monkeypatch.setattr(book_ingest_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_ingest_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(character_match_module, "create_project", lambda slug: project_dir)

    book_ingest_module.ingest_book_text(
        project_slug="demo",
        raw_text="\n".join(
            [
                "CHAPTER I",
                "Carter meets the princess in the city.",
                "",
                "CHAPTER II",
                "A second encounter mentions Carter again.",
                "",
            ]
        ),
    )

    registry_path = project_dir / "02_story_analysis" / "world" / "CHARACTER_REGISTRY.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(
        json.dumps(
            {
                "john_carter": {
                    "canonical_id": "john_carter",
                    "display_name": "John Carter",
                    "aliases": ["carter"],
                    "sources": ["projects/demo/02_story_analysis/character_breakdowns/chapters/CH001/john_carter.md"],
                    "status": "canonical",
                    "entity_kind": "individual",
                    "resolution_reason": "canonical test entry",
                },
                "dejah_thoris": {
                    "canonical_id": "dejah_thoris",
                    "display_name": "Dejah Thoris",
                    "aliases": ["princess"],
                    "sources": ["projects/demo/02_story_analysis/character_breakdowns/chapters/CH001/dejah_thoris.md"],
                    "status": "canonical",
                    "entity_kind": "individual",
                    "resolution_reason": "canonical test entry",
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    candidates = character_match_module.find_character_match_candidates(
        project_slug="demo",
        asset_id="carter",
        aliases="Narrator",
        markdown="# Carter\nA brave figure.",
        top_n=2,
    )

    assert candidates
    assert candidates[0].canonical_id == "john_carter"
    assert candidates[0].score > 0
    assert candidates[0].source_chapters == ["CH001"]
