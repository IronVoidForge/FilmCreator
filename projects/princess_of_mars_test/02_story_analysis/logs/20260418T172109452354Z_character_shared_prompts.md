# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:21:09.452354+00:00
- task: character_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: woola_ch001

Task: write one reusable shared character-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: <value>

[[SECTION purpose]]
...purpose content...
[[/SECTION]]

[[SECTION positive_prompt]]
...positive_prompt content...
[[/SECTION]]

[[SECTION negative_prompt]]
...negative_prompt content...
[[/SECTION]]

[[SECTION inputs_markdown]]
...inputs_markdown content...
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
...continuity_notes_markdown content...
[[/SECTION]]

[[SECTION repair_notes_markdown]]
...repair_notes_markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Rules:

- purpose and inputs may use stable asset ids

- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases

- keep prompts concrete and visible

- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/woola_ch001.md

# Woola (CH001)

## Display Name
Woola

## Chapter Role
Companion / Hound

## Physical Presence
Present following close at heel

## Physical Description
Not described in source material beyond being a hound. No breed, size, color, or physical attributes provided for reliable image generation.

## Costume & Silhouette
Unknown. No costume details available in chapter text.

## Continuity-Critical Traits
- Follows narrator close at heel throughout chapter
- Present during plaza arrival and naval engagement scenes

## Render-Facing Prompt Notes
- Requires manual description for image generation
- Consider breed, size, coat color, and distinguishing features
- May need clarification on species (dog, wolf, or other canine)

## Uncertainty Notes
**CRITICAL:** No physical description provided in source material beyond being a hound. Cannot generate dependable images without additional details about breed, size, color, or distinguishing features.

# Aliases

-



# Canonical Character ID

woola



# Fully Identified

true

# Manual Description Input Required

Yes



# Manual Description Reason

Only identified as "Hound" with no breed, size, color, or physical details provided in source material




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/woola_ch001_manual_description.md

<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->

# Asset ID
woola_ch001

# Purpose
Paste a stable manual visual description for this character so later shared reference generation can use it.

# Why This Is Needed
Only identified as "Hound" with no breed, size, color, or physical details provided in source material

# Guidance
- describe face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks
- prefer visible facts over backstory
- if multiple looks exist, describe the default look for this chapter

# Manual Description

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: woola_ch001

[[SECTION purpose]]
Manual visual description for companion hound character Woola to enable stable shared reference generation. Character follows narrator close at heel throughout chapter scenes including plaza arrival and naval engagement sequences. No physical description provided in source material beyond being a hound - requires manual specification of breed, size, coat color, and distinguishing features for reliable image generation.
[[/SECTION]]

[[SECTION positive_prompt]]
small canine companion with short muzzle and floppy ears, medium build with balanced proportions, warm brown coat with lighter tan markings on chest and face, soft fur texture visible in close detail, standing silhouette showing compact frame, neutral expression with dark eyes, simple collar around neck, follows human figure at heel position throughout scene composition.
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific breed names, large size, long muzzle, erect ears, bright colors, elaborate costume details, complex background elements, multiple characters, detailed facial expressions beyond neutral, metallic accessories, furless patches, oversized proportions, wolf-like features, aggressive stance.
[[/SECTION]]

[[SECTION inputs_markdown]]
Character: Woola (CH001)
Role: Companion / Hound
Continuity Traits: Follows narrator close at heel throughout chapter, present during plaza arrival and naval engagement scenes
Physical Description Status: Requires manual specification - source material only identifies as hound without breed, size, color details
Render-Facing Requirements: Stable face, hair (coat), body type, costume logic, silhouette, recurring materials over scene-specific blocking
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character must maintain consistent physical appearance across all chapter scenes. Primary continuity requirement is following narrator at heel position throughout plaza and naval engagement sequences. Coat color and breed should remain stable for shared reference generation. No costume changes expected during chapter duration. Silhouette should be recognizable in both close and wide shots.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Source material lacks physical description beyond hound identification - manual description path requires completion with specific breed, size, and color details before reliable image generation possible. Consider adding distinguishing features like ear shape, muzzle length, or coat pattern variations to enable stable reference across multiple generations. Species clarification (dog vs wolf) needed for accurate rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
