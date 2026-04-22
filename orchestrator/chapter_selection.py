from __future__ import annotations

import re


def normalize_chapter_id(value: str | int | None) -> str | None:
    if value is None:
        return None
    text = str(value).strip().upper()
    if not text:
        return None
    match = re.fullmatch(r"CH?0*(\d{1,3})", text)
    if match:
        return f"CH{int(match.group(1)):03d}"
    match = re.fullmatch(r"CH(\d{3})", text)
    if match:
        return f"CH{int(match.group(1)):03d}"
    return None


def parse_chapter_selector(selector: str | None) -> list[str]:
    if not selector or not str(selector).strip():
        return []

    raw = str(selector).strip().upper()
    parts = [part.strip() for part in re.split(r"[,\s]+", raw) if part.strip()]
    selected: list[str] = []
    seen: set[str] = set()

    for part in parts:
        range_match = re.fullmatch(r"(CH?\d{1,3})-(CH?\d{1,3})", part)
        if range_match:
            start = normalize_chapter_id(range_match.group(1))
            end = normalize_chapter_id(range_match.group(2))
            if not start or not end:
                continue
            start_num = int(start[2:])
            end_num = int(end[2:])
            lo, hi = sorted((start_num, end_num))
            for number in range(lo, hi + 1):
                chapter_id = f"CH{number:03d}"
                if chapter_id not in seen:
                    seen.add(chapter_id)
                    selected.append(chapter_id)
            continue

        normalized = normalize_chapter_id(part)
        if normalized and normalized not in seen:
            seen.add(normalized)
            selected.append(normalized)

    return selected


def chapter_matches(chapter_id: str, selected_chapters: set[str]) -> bool:
    if not selected_chapters:
        return True
    normalized = normalize_chapter_id(chapter_id)
    return bool(normalized and normalized in selected_chapters)


def any_chapter_matches(values: list[str], selected_chapters: set[str]) -> bool:
    if not selected_chapters:
        return True
    for value in values:
        normalized = normalize_chapter_id(value)
        if normalized and normalized in selected_chapters:
            return True
    return False
