# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:04:22.049688+00:00
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

Asset id: prisoner_captive

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/prisoner_captive.md

# The Prisoner - Chapter VIII Captive

**Display Name:** The Prisoner  
**Chapter Role:** Captive/Secondary Character  
**Physical Presence:** Referenced (encounter point in plaza)  

## Physical Description
- **Face:** Oval, finely chiseled features, large lustrous eyes
- **Hair:** Coal black, waving, loose coiffure
- **Skin Tone:** Light reddish copper
- **Cheeks:** Crimson
- **Lips:** Ruby
- **Build:** Slender, girlish figure
- **Height:** Considerably less than half as tall as green Martian warriors

## Costume & Silhouette
- **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments
- **Silhouette:** Erect walking upon two legs
- **Accessories:** Highly wrought ornaments (specific type not documented)

## Continuity-Critical Traits
- Being dragged by females into building
- Seen from upper floor window observation point
- Looks at narrator with hope then dejection
- Slender girlish figure with oval face and finely chiseled features
- Large lustrous eyes, coal black waving hair (loose coiffure)
- Light reddish copper skin, crimson cheeks, ruby lips

## Render-Facing Prompt Notes
*Physical description sufficient for image generation.*

**Uncertainty Notes:**
- Specific ornament types not documented
- Canonical name unknown
- Background and origin unclear

**Useful Descriptive Noun Phrases (for later prompts):**
- slender girlish figure with oval face and finely chiseled features
- large lustrous eyes, coal black waving hair in loose coiffure
- light reddish copper skin, crimson cheeks, ruby lips
- destitute of clothes save for highly wrought ornaments

# Aliases

[a prisoner, her]



# Canonical Character ID

prisoner_captive



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/prisoner_captive_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: prisoner_captive

[[SECTION purpose]]
Shared character reference prompt for stable local generation of the prisoner captive. Ensures consistent physical traits (face, hair, skin, ornaments) across scenes without relying on scene-specific blocking or proper nouns.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure with oval face and finely chiseled features, large lustrous eyes, coal black waving hair in loose coiffure, light reddish copper skin, crimson cheeks, ruby lips, destitute of clothes save for highly wrought ornaments, erect walking upon two legs.
[[/SECTION]]

[[SECTION negative_prompt]]
blurry, low quality, extra fingers, missing eyes, wearing standard clothes, green skin, dark hair, heavy makeup, text, watermark, signature, bad anatomy, deformed limbs, wrong skin tone, clothed body.
[[/SECTION]]

[[SECTION inputs_markdown]]
Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/prisoner_captive.md
Asset ID: prisoner_captive
Canonical Character ID: prisoner_captive
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Must maintain light reddish copper skin tone and coal black hair color. Ornaments are present but specific type is undocumented; ensure they appear as highly wrought jewelry or accessories without defining exact material if unknown. Height reference is considerably less than green Martian warriors (if context requires comparison).
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Uncertainty regarding specific ornament types documented in source. If generation fails to include ornaments, prioritize adding generic highly wrought ornaments rather than removing them. Skin tone description "light reddish copper" may need adjustment based on model interpretation of copper vs red.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
