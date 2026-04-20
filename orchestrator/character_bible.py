import json
from pathlib import Path
from typing import Dict, Any

from .character_bible_models import CharacterBible


def build_character_bible(character_id: str, registry_entry: Dict[str, Any]) -> CharacterBible:
    return CharacterBible(
        character_id=character_id,
        display_name=registry_entry.get("name", character_id),
        aliases=registry_entry.get("aliases", []),
        stable_visual_summary="",
        physical_traits=registry_entry.get("traits", []),
        costume_signature="",
        personality="",
        role="",
        voice_notes="",
        continuity_constraints=[],
        unresolved_ambiguities=[],
        evidence_refs=registry_entry.get("evidence", []),
    )


def save_character_bible(project_path: Path, bible: CharacterBible):
    output_dir = project_path / "02_story_analysis" / "bibles" / "characters"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{bible.character_id}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(bible.__dict__, f, indent=2)


def run_character_bible_synthesis(project_path: Path):
    registry_path = project_path / "02_story_analysis" / "world" / "CHARACTER_REGISTRY.json"

    if not registry_path.exists():
        raise FileNotFoundError("Character registry not found")

    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    for char_id, entry in registry.items():
        bible = build_character_bible(char_id, entry)
        save_character_bible(project_path, bible)
