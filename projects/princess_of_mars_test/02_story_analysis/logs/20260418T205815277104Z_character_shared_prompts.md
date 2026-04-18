# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:58:15.277104+00:00
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

Asset id: earthly_woman_prisoner

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/earthly_woman_prisoner.md

# Earthly Woman / Prisoner

**Chapter Role:** Captive / Subject  
**Physical Presence:** Physically Present (dragged into building by warriors)  

## Physical Description
- Slender girlish figure
- Earthly woman appearance
- Oval face
- Coal black hair
- Light reddish copper skin
- Naked except ornaments

## Costume & Silhouette
- Wears only ornaments (no clothing documented)
- Girlish silhouette
- Ornamented body

## Continuity-Critical Traits
- Looks at narrator from building window
- Makes sign of appeal for help
- Dragged away by green Martian females
- Narrator feels hope and dejection upon seeing her
- Represents mixed emotions: hope, fear, exultation, depression in narrator

## Render-Facing Prompt Notes
**Key Phrases for Later Use:** "slender girlish figure," "oval face with coal black hair," "light reddish copper skin," "naked except ornaments," "Earthly woman appearance"  
**Uncertainty:** Cultural context of ornaments and their significance may require clarification

## Important Notes
- Fully identified character with sufficient physical description for image generation
- May require cultural clarification regarding ornament types and meanings
- Emotional significance to narrator is well-documented

# Aliases

prisoner, captive, Earthly woman



# Canonical Character ID

earthly_woman_prisoner



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/earthly_woman_prisoner_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: earthly_woman_prisoner

[[SECTION purpose]]
Generate stable physical reference for slender girlish figure with oval face, coal black hair, and light reddish copper skin. Focus on ornamented body silhouette without clothing. Use consistent facial features and body type across all generations. Avoid scene-specific actions or emotional states in base prompt.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure, oval face with coal black hair, light reddish copper skin, naked except ornaments, Earthly woman appearance, ornamental jewelry pieces, delicate body silhouette, girlish proportions, natural skin texture, minimal clothing coverage, decorative accessories on body
[[/SECTION]]

[[SECTION negative_prompt]]
clothing, garments, fabric, full dress, elaborate costume, scene-specific actions, emotional expressions, dramatic lighting, shadows from building, green Martian females, warriors, green skin, proper nouns, cultural context markers, complex background elements, detailed environmental blocking
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/earthly_woman_prisoner.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character represents captive subject with stable physical description. Ornament types and cultural significance may require clarification. Emotional significance to narrator is well-documented but should not appear in base prompt. Continuity-critical traits include window appearance, appeal gestures, and being dragged away by green Martian females.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Uncertainty regarding ornament cultural context needs resolution. May need additional clarification on specific jewelry types and their meanings. Emotional states should be separated from physical description for prompt stability.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
