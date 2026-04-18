# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:58:41.853372+00:00
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

Asset id: sola

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/sola.md

# Sola

## Display Name & Role
**Name:** Sola  
**Role:** Companion / Messenger

## Presence Status
**Status:** Referenced  
**Note:** Character rushes up to the narrator.

## Physical Description
**Supported Details:** None provided in this chapter.  
**Uncertainty Notes:** No physical traits (height, build, hair color, skin tone) are described in the text. Only action ("rushes up") is recorded.

## Costume & Silhouette
**Details:** Unknown.  
**Continuity Traits:** None specified in this chapter.

## Render-Facing Prompt Phrases
- "Figure rushing to narrator"
- "Uncertain physical build"
- "Martian attire (implied)"

# Aliases

None



# Canonical Character ID

sola



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/sola_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: sola
[[SECTION purpose]]
Establish a reusable character reference for Sola, focusing on the action of approaching the narrator and implied planetary aesthetic, while noting physical details are currently undefined and require stable placeholder logic.
[[/SECTION]]
[[SECTION positive_prompt]]
Figure rushing to narrator, uncertain physical build, companion messenger silhouette, planetary attire implied, approaching stance, dynamic movement, soft lighting on figure, neutral expression.
[[/SECTION]]
[[SECTION negative_prompt]]
static pose, detailed facial features, specific hair color, modern clothing, urban setting, text overlay, watermark, blurry background, distorted limbs, extra fingers, low resolution.
[[/SECTION]]
[[SECTION inputs_markdown]]
Asset ID: sola
Project Path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/sola.md
Manual Description Path: Missing
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Physical description undefined in source chapter. Costume details unknown, only implied planetary attire noted. Action "rushes up" is primary visual anchor. No manual override available.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Await manual character description input if specific traits become available. Maintain generic silhouette until confirmed. Do not invent physical build without source confirmation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
