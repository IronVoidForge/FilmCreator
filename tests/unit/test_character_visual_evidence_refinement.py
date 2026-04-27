from pathlib import Path

from orchestrator.character_visual_evidence_refinement import (
    classify_visual_terms,
    find_character_visual_evidence,
    split_source_into_paragraphs,
)


def _write_chapter(project_root: Path, chapter_id: str, text: str) -> None:
    chapter_dir = project_root / "01_source" / "chapters"
    chapter_dir.mkdir(parents=True, exist_ok=True)
    (chapter_dir / f"{chapter_id}_chapter.md").write_text(text, encoding="utf-8")


def test_dorothy_exact_clothing_attaches_to_dorothy(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    _write_chapter(
        project_root,
        "CH003",
        """
Dorothy had only one other dress, but that happened to be clean and was hanging on a peg beside her bed. It was gingham, with checks of white and blue. The girl washed herself carefully and tied her pink sunbonnet on her head.

A girl in the palace was dressed in a pretty green silk gown.
""",
    )
    bible = {
        "character_id": "dorothy",
        "display_name": "Dorothy",
        "chapter_mentions": ["CH003"],
        "identity_baseline": "A young girl.",
    }

    evidence = find_character_visual_evidence(project_root, bible, ["CH003"])
    snippets = " ".join(item.snippet for item in evidence)

    assert "gingham" in snippets
    assert "white and blue" in snippets
    assert "pink sunbonnet" in snippets
    assert "green silk gown" not in snippets


def test_scarecrow_source_details_attach_by_direct_name(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    _write_chapter(
        project_root,
        "CH003",
        """
The Scarecrow's head was a small sack stuffed with straw, with eyes, nose, and mouth painted on it to represent a face. An old, pointed blue hat was perched on his head. The rest of the figure was a blue suit of clothes, worn and faded.
""",
    )
    bible = {
        "character_id": "the_scarecrow",
        "display_name": "The Scarecrow",
        "chapter_mentions": ["CH003"],
        "identity_baseline": "A living scarecrow.",
    }

    evidence = find_character_visual_evidence(project_root, bible, ["CH003"])
    snippets = " ".join(item.snippet for item in evidence)

    assert "stuffed with straw" in snippets
    assert "pointed blue hat" in snippets
    assert "blue suit of clothes" in snippets


def test_generic_visual_terms_without_character_anchor_are_ignored(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    _write_chapter(
        project_root,
        "CH011",
        """
The room was full of green silk gowns, green ribbons, and polished shoes. A fountain stood in the middle of the chamber.
""",
    )
    bible = {
        "character_id": "dorothy",
        "display_name": "Dorothy",
        "chapter_mentions": ["CH011"],
        "identity_baseline": "A young girl.",
    }

    evidence = find_character_visual_evidence(project_root, bible, ["CH011"])

    assert evidence == []


def test_visual_description_of_object_seen_by_character_is_not_attached(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    _write_chapter(
        project_root,
        "CH020",
        """
A little farther on Dorothy met a most beautifully dressed young Princess, who stopped short as she saw the strangers and started to run away.

Dorothy took a needle and thread while Oz cut strips of green silk for the balloon.
""",
    )
    bible = {
        "character_id": "dorothy",
        "display_name": "Dorothy",
        "chapter_mentions": ["CH020"],
        "identity_baseline": "A young girl.",
    }

    evidence = find_character_visual_evidence(project_root, bible, ["CH020"])
    auto_patchable = [item for item in evidence if item.confidence >= 0.85 and not item.risk_flags]

    assert auto_patchable == []


def test_possessive_room_and_other_characters_clothes_are_not_owned_visuals(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    _write_chapter(
        project_root,
        "CH013",
        """
When he walked into Dorothy's room, Dorothy wiped every tear from his face with her apron so his joints would not be rusted.

The Winged Monkeys had tossed the Scarecrow's clothes into the tall tree.
""",
    )
    dorothy_bible = {
        "character_id": "dorothy",
        "display_name": "Dorothy",
        "chapter_mentions": ["CH013"],
        "identity_baseline": "A young girl.",
    }
    monkeys_bible = {
        "character_id": "winged_monkeys",
        "display_name": "Winged Monkeys",
        "chapter_mentions": ["CH013"],
        "identity_baseline": "Monkey-like creatures with wings.",
    }

    dorothy_evidence = find_character_visual_evidence(project_root, dorothy_bible, ["CH013"])
    monkey_evidence = find_character_visual_evidence(project_root, monkeys_bible, ["CH013"])
    auto_patchable = [
        item
        for item in [*dorothy_evidence, *monkey_evidence]
        if item.confidence >= 0.85 and not item.risk_flags
    ]

    assert auto_patchable == []


def test_visual_terms_are_categorized() -> None:
    terms = classify_visual_terms("Dorothy wore silver shoes and tied a pink sunbonnet on her head.")

    assert "costume" in terms
    assert "material_state" in terms
    assert "appearance" in terms


def test_split_source_ignores_markdown_headings() -> None:
    paragraphs = split_source_into_paragraphs("# Chapter\n\nDorothy wore silver shoes.\n\nThe road was bright.")

    assert paragraphs == ["Dorothy wore silver shoes.", "The road was bright."]
