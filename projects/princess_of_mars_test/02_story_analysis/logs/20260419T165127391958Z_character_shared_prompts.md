# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:51:27.391958+00:00
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

Asset id: human_female_prisoner

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/human_female_prisoner.md

# Human Female Prisoner - Chapter CH008

## Display Name & Role
**Human Female Prisoner** - Captive, Appeal Signal

## Physical Presence
**Referenced** - Dragged from burning air craft into city building; turns to Carter before being taken away.

## Physical Description (Supported by Source)
- Build: Slender, girlish figure
- Skin: Light reddish copper tone
- Features: Finely chiseled facial features
- Eyes: Large, lustrous
- Hair: Coal black, waving, caught loosely into strange coiffure
- Attire: Naked except for highly wrought ornaments
- Cheeks: Crimson-colored
- Lips: Ruby-colored

## Costume & Silhouette
- No clothing; adorned with highly wrought ornaments only
- Ornamentation style described as "strange" (continuity detail)
- Silhouette emphasizes slender, girlish proportions

## Continuity-Critical Traits
- Signals appeal to John Carter from burning ship
- Dragged into building by Green Martian females
- Captive status established through visual description and action
- Key emotional focal point of chapter scene

## Render-Facing Noun Phrases
- "Human female prisoner with light reddish copper skin"
- "Slender girlish figure in highly wrought ornaments"
- "Coal black waving hair in strange coiffure"
- "Large lustrous eyes, finely chiseled features"
- "Crimson cheeks, ruby lips"
- "Appealing to John Carter from burning air craft"

## Uncertainty Notes
- Ornamentation style described as "strange" but specific design not detailed
- Coiffure described as "strange" without specific styling details
- No prior costume history provided in this chapter

# Aliases

None



# Canonical Character ID

human_female_prisoner



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/human_female_prisoner_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: human_female_prisoner

[[SECTION purpose]]
Reusable shared character-reference prompt draft for stable local generation focusing on physical consistency, attire (ornaments), and facial features.
[[/SECTION]]

[[SECTION positive_prompt]]
Human female prisoner with light reddish copper skin, slender girlish figure in highly wrought ornaments, coal black waving hair in strange coiffure, large lustrous eyes, finely chiseled features, crimson cheeks, ruby lips, distressed expression, standing amidst burning air craft debris.
[[/SECTION]]

[[SECTION negative_prompt]]
clothing, fabric, textile, text, watermark, blurry, low quality, green skin, dark skin, bald, short hair, bright eyes, wide mouth, smiling, laughing, modern technology, metal armor, alien females, proper nouns.
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/human_female_prisoner.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Captive status established through visual description and action. Signals appeal from burning ship. Dragged into building by females. Key emotional focal point. Ornamentation style described as "strange" without specific design details. Coiffure described as "strange" without specific styling details. No prior costume history provided in this chapter.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Manual character description path missing. Prompts avoid proper nouns to ensure generalizability across scenes. Uncertainty preserved regarding ornamentation and coiffure specifics.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
