from __future__ import annotations

from pathlib import Path

import orchestrator.book_ingest as book_ingest_module
import orchestrator.book_librarian as book_librarian_module


def test_book_librarian_reads_index_and_returns_paragraph_windows(tmp_path: Path, monkeypatch) -> None:
    project_dir = tmp_path / "projects" / "demo"
    monkeypatch.setattr(book_ingest_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_ingest_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(book_librarian_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_librarian_module, "resolve_user_path", lambda value: tmp_path / value)

    book_ingest_module.ingest_book_text(
        project_slug="demo",
        raw_text="\n".join(
            [
                "CHAPTER I",
                "First paragraph about Carter.",
                "",
                "Second paragraph about Dejah.",
                "",
                "CHAPTER II",
                "Third paragraph about Mars.",
                "",
            ]
        ),
    )

    chapter_text = book_librarian_module.chapter_text("demo", "CH001")
    assert "First paragraph about Carter." in chapter_text

    window = book_librarian_module.get_paragraph_window("demo", "CH001", 1, 2)
    assert window.chapter_id == "CH001"
    assert window.paragraph_start == 1
    assert window.paragraph_end == 2
    assert "First paragraph about Carter." in window.text
    assert "Second paragraph about Dejah." in window.text

    contexts = book_librarian_module.search_chapter_context("demo", "CH001", ["Carter"], window=0, top_n=2)
    assert contexts
    assert contexts[0].chapter_id == "CH001"
    assert "Carter" in contexts[0].text or "Carter" in contexts[0].preview
