from __future__ import annotations

import json
from pathlib import Path

import orchestrator.book_ingest as book_ingest_module


def test_ingest_book_text_writes_manifest_and_book_index(tmp_path: Path, monkeypatch) -> None:
    project_dir = tmp_path / "projects" / "demo"
    monkeypatch.setattr(book_ingest_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_ingest_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())

    summary = book_ingest_module.ingest_book_text(
        project_slug="demo",
        raw_text="\n".join(
            [
                "CHAPTER I",
                "First paragraph.",
                "",
                "Second paragraph.",
                "",
                "CHAPTER II",
                "Another chapter paragraph.",
                "",
            ]
        ),
    )

    assert summary.project_slug == "demo"
    assert summary.manifest_path == "projects/demo/01_source/book/book_manifest.md"
    assert summary.book_index_path == "projects/demo/01_source/book/book_index.json"

    index_path = project_dir / "01_source" / "book" / "book_index.json"
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    assert payload["project_slug"] == "demo"
    assert payload["chapter_count"] == 2
    assert payload["chapters"][0]["chapter_id"] == "CH001"
    assert payload["chapters"][0]["paragraph_count"] == 2
    assert payload["chapters"][0]["paragraphs"][0]["preview"] == "First paragraph."


def test_ensure_book_ingested_skips_existing_manifest(tmp_path: Path, monkeypatch) -> None:
    project_dir = tmp_path / "projects" / "demo"
    book_dir = project_dir / "01_source" / "book"
    book_dir.mkdir(parents=True)
    (book_dir / "book_manifest.md").write_text("# Book Manifest\n", encoding="utf-8")
    monkeypatch.setattr(book_ingest_module, "create_project", lambda slug: project_dir)

    assert book_ingest_module.ensure_book_ingested(project_slug="demo") is None


def test_ensure_book_ingested_uses_raw_book_when_manifest_missing(tmp_path: Path, monkeypatch) -> None:
    project_dir = tmp_path / "projects" / "demo"
    book_dir = project_dir / "01_source" / "book"
    book_dir.mkdir(parents=True)
    (book_dir / "raw_book.txt").write_text("CHAPTER I\nA road begins.\n", encoding="utf-8")
    monkeypatch.setattr(book_ingest_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_ingest_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())

    summary = book_ingest_module.ensure_book_ingested(project_slug="demo")

    assert summary is not None
    assert summary.chapter_ids == ["CH001"]
    assert (book_dir / "book_manifest.md").exists()
