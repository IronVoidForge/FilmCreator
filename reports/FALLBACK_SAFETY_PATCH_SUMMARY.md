# Fallback Safety Patch Implementation Summary

## Goal
Made the visual production fallback conservative and book-agnostic while the new taxonomy system is being built.

## Files Changed

### 1. orchestrator\character_bible_fallback.py
**Hardcoded Rules Removed:**
- ❌ Removed: `if char_id == "protagonist" → alias_redirect to "john_carter"`
- ❌ Removed: Book-specific markers: `"martian"`, `"thark"`, `"green martian"`, `"red martian"`, `"barsoom"`, `"helium"`, `"woola"`, `"calot"`, `"thoat"`
- ❌ Removed: Hardcoded role-to-species mappings: `"chieftain" → non_human_humanoid`
- ❌ Removed: Geographic markers: `"virginia"`, `"confederate"`, `"american"`

**Conservative Fallback Rules Implemented:**
1. **Alias redirects** - Only from explicit `alias_redirect_target` metadata, not hardcoded IDs
2. **Associated evidence filtering** - Entity using/wearing/riding X is not X itself
   - "riding a mount" → entity is not a mount
   - "wearing alien harness" → entity is not alien
   - "followed by hounds" → entity is not a hound
3. **Identity-first classification** - Prioritizes `identity_baseline` and `physical_build` over costume/evidence
4. **Conservative unknown fallback** - Weak/mixed evidence → `unknown_reference` instead of confident wrong bucket
5. **Direct evidence only** - Only classifies as non-human/quadruped/creature if direct evidence says entity IS that type

**New Helper Functions:**
- `has_direct_identity_evidence(text, markers)` - Checks for direct identity markers
- `has_associated_entity_evidence(text, markers)` - Detects when entity is associated with but not the thing itself
- `conservative_emergency_bucket(entry, bible_data, text)` - Returns conservative bucket for weak evidence

**Classification Order (Priority):**
1. Alias redirect (from metadata only)
2. Group/horde (entity_kind or direct collective evidence)
3. Context-only (entity_kind or explicit non-renderable metadata)
4. Quadruped (entity IS mount/beast, not using one)
5. Non-human humanoid (alien + humanoid markers in identity)
6. Human (human markers in identity)
7. Creature (entity IS creature/beast, not associated with one)
8. Unknown reference (weak/mixed evidence)

### 2. tests\test_character_bible_production_fallbacks.py
**Book-Specific Tests Removed/Replaced:**
- ❌ `test_fallback_bucket_protagonist_redirect` → ✅ `test_fallback_bucket_alias_redirect_from_metadata`
- ❌ `test_fallback_bucket_john_carter_human` → ✅ `test_fallback_bucket_human_soldier`
- ❌ `test_fallback_bucket_martian_mounts_quadruped` → ✅ `test_fallback_bucket_unnamed_mount_quadruped`
- ❌ `test_fallback_bucket_green_martian_non_human_humanoid` → ✅ `test_fallback_bucket_alien_humanoid_leader`
- ❌ `test_fallback_bucket_dead_friend_context_only` → ✅ `test_fallback_bucket_deceased_reference_context_only`
- ❌ `test_fallback_bucket_apache_warriors_group` → ✅ `test_fallback_bucket_warriors_group`
- ❌ `test_fallback_bucket_woola_large_quadruped` → ✅ `test_fallback_bucket_watchdog_large_quadruped`
- ❌ References to "John Carter", "Barsoom", "Tars Tarkas", "Martian", "Apache", "Woola" removed

**New Conservative Fallback Tests Added:**
1. ✅ `test_human_riding_animal_remains_human` - Human riding mount ≠ quadruped
2. ✅ `test_human_wearing_alien_clothing_remains_human` - Human wearing alien gear ≠ alien
3. ✅ `test_humanoid_with_mount_not_quadruped` - Humanoid with mount ≠ quadruped
4. ✅ `test_direct_animal_becomes_quadruped` - Direct animal evidence → quadruped
5. ✅ `test_weak_evidence_becomes_unknown_reference` - Weak evidence → unknown_reference
6. ✅ `test_explicit_alias_metadata_produces_redirect` - Alias from metadata only
7. ✅ `test_explicit_context_only_metadata` - Context-only from metadata
8. ✅ `test_mummified_corpse_context_only` - Mummified corpse without active visual → context_only
9. ✅ `test_leader_with_hounds_not_hound` - Leader followed by hounds ≠ hound
10. ✅ `test_warrior_carrying_weapon_not_weapon` - Warrior carrying weapon ≠ weapon

**Synthetic Test Names Used:**
- `human_soldier`, `alien_cloaked_human`, `humanoid_leader_with_mount`
- `unnamed_mount`, `role_label_entity`, `deceased_reference`
- `colossal_ape`, `warriors`, `watchdog`, `alien_officer`

## Validation Results

### Compilation
```
✅ python -m compileall orchestrator
Compiling 'orchestrator\\character_bible_fallback.py'...
SUCCESS
```

### Tests
```
✅ pytest tests\test_character_bible_production_fallbacks.py -q
37 passed in 0.03s
SUCCESS
```

## Remaining Risks

### Low Risk
1. **Generic anatomical markers remain** - "green skin", "four arms", "tusks" are kept as generic non-human markers (not book-specific)
2. **Other modules may have hardcoded logic** - This patch only addresses `character_bible_fallback.py`. Other modules found with book-specific logic:
   - `orchestrator\character_descriptor_repair.py` - Has "barsoom_humanoid" bucket
   - `orchestrator\descriptor_enrichment.py` - Has "green_martian_individual", "red_martian_individual" profile classes
   - `orchestrator\visual_fallbacks.py` - Has "barsoom_humanoid" costume fallback
   - `orchestrator\world_registry.py` - Has hardcoded "john_carter" alias resolution
   - `orchestrator\dialogue_timeline.py` - Has hardcoded "john_carter" lookup
   - `orchestrator\features\world\global_helpers.py` - Has "protagonist", "chieftain", "martian_leader" in role lists
   - `orchestrator\scene_contracts.py` - Has "chieftain" → "The Chieftain" display name mapping

### Mitigation
- This patch makes the fallback layer conservative and safe
- Fallback will return `unknown_reference` for weak evidence instead of confident wrong classifications
- Associated evidence (mounts, clothing, weapons) no longer redefines entity type
- Alias redirects require explicit metadata, not hardcoded ID patterns

## Next Steps
1. ✅ **COMPLETE**: Conservative fallback safety patch
2. **TODO**: Build upstream taxonomy system to replace fallback heuristics
3. **TODO**: Refactor other modules to remove book-specific logic (see "Remaining Risks" above)
4. **TODO**: Add taxonomy metadata to character bibles for explicit classification
