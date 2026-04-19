# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:58:57.639003+00:00
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

Asset id: carter

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/carter.md

# Carter - Chapter CH008

## Display Name
Carter

## Chapter Role
Observer/Narrator

## Physical Presence
Present - physically located in city plaza/building throughout chapter

## Physical Description
**Status:** No physical or visual description provided in chapter text

**Supported Details:** None from source material

**Uncertainty Notes:** 
- Character serves as primary observer but lacks any physical description in this chapter
- Cannot generate dependable images without manual description intervention
- Role is clear (observer/narrator) but visual identity is undefined in source

## Costume, Silhouette, Continuity Traits
**Status:** Not described in chapter text

**Supported Details:** None from source material

**Continuity-Critical Traits:** 
- Observer position: city plaza/building upper floors/windows
- No costume or silhouette details available for render-facing prompts

## Render-Facing Prompt Noun Phrases
- "observer character" (placeholder)
- "city plaza location" (contextual)
- "no physical description - requires manual intervention" (uncertainty flag)

## Uncertainty Summary
This character lacks any physical or visual description in the provided chapter text. While their role as observer is clear, no renderable details exist for dependable image generation. Manual description required before proceeding with visual production.

# Aliases

None



# Canonical Character ID

carter



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: carter

[[SECTION purpose]]
Character serves as primary observer/narrator positioned in city plaza or building upper floors throughout chapter. No physical description exists in source material - requires manual intervention for visual production. Role is clear but renderable details undefined. Prompts must reflect uncertainty while maintaining continuity of observer positioning and avoiding proper nouns.

[[/SECTION]]

[[SECTION positive_prompt]]
observer character, neutral expression, standing or seated position, city plaza background, building windows visible, upper floor location, no specific costume details, undefined physical features, narrator presence, urban environment, consistent silhouette, minimal blocking, static composition, observer role emphasis

[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, brand names, specific character identities, detailed facial features, named clothing items, scene-specific actions, dynamic camera movement, complex lighting setups, multiple characters, dialogue bubbles, text overlays, weather effects, time of day indicators, location markers, numbered elements, copyrighted imagery, animated sequences

[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/carter.md
projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md (missing)
projects/princess_of_mars_test/01_source/character_descriptions/carter.md

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character role as observer/narrator is consistent across chapter. Physical description undefined - requires manual intervention before visual production. Positioning in city plaza or building upper floors should remain constant. No costume or silhouette details available for render-facing prompts. All prompts must avoid proper nouns and use descriptive noun phrases only.

[[/SECTION]]

[[SECTION repair_notes_markdown]]
Manual character description required before proceeding with visual generation. Source material lacks physical details for dependable image production. Consider adding generic observer characteristics (neutral expression, undefined features) while noting uncertainty in continuity notes. Recommend creating separate manual description document at projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
