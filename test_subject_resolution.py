"""Test script to validate subject resolution logic"""
from pathlib import Path
from orchestrator.shot_planner import (
    _resolve_renderable_subject_id,
    _load_character_bible,
    _looks_like_object_subject,
    _looks_like_environment_anchor,
    _looks_like_celestial_anchor,
    _looks_like_environment_phenomenon,
)

project_dir = Path("C:/FilmCreator_MC/projects/princess_of_mars_test")

# Test cases
test_cases = [
    ("protagonist", "Should resolve protagonist"),
    ("john_carter", "Should resolve john_carter"),
    ("vapor", "Should return empty for vapor (environment phenomenon)"),
    ("mist", "Should return empty for mist (environment phenomenon)"),
    ("spear", "Should return empty for spear (key item)"),
    ("tars_tarkas", "Should resolve tars_tarkas"),
]

print("Testing subject resolution logic:\n")
print("=" * 80)

for subject_id, description in test_cases:
    result = _resolve_renderable_subject_id(subject_id, project_dir)
    print(f"\nTest: {description}")
    print(f"  Input: '{subject_id}'")
    print(f"  Output: '{result}'")
    
    # Additional diagnostics
    if _looks_like_object_subject(subject_id):
        print(f"  -> Detected as object subject")
    if _looks_like_environment_phenomenon(subject_id):
        print(f"  -> Detected as environment phenomenon")
    if _looks_like_environment_anchor(subject_id):
        print(f"  -> Detected as environment anchor")
    if _looks_like_celestial_anchor(subject_id):
        print(f"  -> Detected as celestial anchor")
    
    bible = _load_character_bible(project_dir, subject_id)
    if bible:
        print(f"  -> Found character bible")
        entity_kind = bible.get("entity_kind", "")
        print(f"  -> entity_kind: '{entity_kind}'")
        alias_res = bible.get("alias_resolution", {})
        if isinstance(alias_res, dict):
            target = alias_res.get("canonical_target_id")
            print(f"  -> canonical_target_id: {target}")

print("\n" + "=" * 80)
print("\nExpected results:")
print("  - protagonist: should return 'protagonist' (or redirect if alias)")
print("  - john_carter: should return 'john_carter'")
print("  - vapor: should return '' (empty)")
print("  - mist: should return '' (empty)")
print("  - spear: should return '' (empty)")
print("  - tars_tarkas: should return 'tars_tarkas'")
