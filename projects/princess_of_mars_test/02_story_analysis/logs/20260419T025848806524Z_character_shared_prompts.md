# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:58:48.806524+00:00
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

Asset id: captive

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/captive.md

# The Captive - Chapter CH008

## Display Name
The Captive

## Chapter Role
Signal-sender / Prisoner

## Physical Presence
Present - seen by Carter before being taken inside building

## Physical Description
**Status:** Detailed visual description provided in chapter text

**Supported Details:** 
- Slender, girlish figure
- Oval face
- Light reddish copper skin
- Coal black waving hair (loose coiffure)
- Naked except highly wrought ornaments
- Crimson cheeks/ruby lips

**Uncertainty Notes:** 
- Canonical name not explicitly stated in chapter text
- Physical description is complete but identity confirmation needed

## Costume, Silhouette, Continuity Traits
**Status:** Partially described in chapter text

**Supported Details:** 
- Silhouette: slender, girlish figure
- Hair: coal black, waving, loose coiffure
- Skin tone: light reddish copper
- Adornments: highly wrought ornaments (no specific costume details)
- Facial features: oval face, crimson cheeks, ruby lips

**Continuity-Critical Traits:** 
- Signal-sender gesture made to Carter before capture
- Taken inside building as prisoner
- No specific costume or armor described beyond ornaments

## Render-Facing Prompt Noun Phrases
- "slender girlish figure" (silhouette)
- "copper skin tone" (color)
- "coal black waving hair" (hair description)
- "highly wrought ornaments" (adornments)
- "oval face with crimson cheeks and ruby lips" (facial features)

## Uncertainty Summary
This character has complete physical description but lacks explicit canonical naming in chapter text. While visual details are renderable, identity confirmation is required before proceeding. Clarification needed regarding whether this figure represents Princess of Mars from the story context.

# Aliases

None



# Canonical Character ID

captive



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/captive_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: captive

[[SECTION purpose]]
Shared reference prompt for generating consistent visual representation of The Captive character across scenes. Focuses on physical attributes, silhouette, and adornments while avoiding scene-specific blocking or proper nouns. Used for stable local generation to maintain character continuity in render pipelines.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure with copper skin tone, coal black waving hair in loose coiffure, highly wrought ornaments adorning body, oval face with crimson cheeks and ruby lips, signal-sender gesture pose, prisoner silhouette, detailed facial features, ornamental adornments, slender build, girlish proportions, light reddish copper complexion, dark flowing hair, intricate ornamentation
[[/SECTION]]

[[SECTION negative_prompt]]
blurry, low resolution, extra limbs, missing fingers, distorted face, unnatural skin texture, scene-specific blocking, background elements, proper nouns, canonical names, armor plates, costume details beyond ornaments, facial expressions not matching character status, inconsistent hair style, wrong skin tone, heavy makeup, jewelry beyond wrought ornaments, bulky build, mature proportions
[[/SECTION]]

[[SECTION inputs_markdown]]
Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/captive.md
Display Name: The Captive
Chapter Role: Signal-sender / Prisoner
Physical Description: Slender girlish figure, oval face, light reddish copper skin, coal black waving hair (loose coiffure), naked except highly wrought ornaments, crimson cheeks/ruby lips
Continuity Traits: Taken inside building as prisoner, signal-sender gesture made to Carter before capture
Canonical Character ID: captive
Fully Identified: false
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character maintains consistent physical attributes across all renders. Silhouette should remain slender girlish figure with copper skin tone. Hair must be coal black waving in loose coiffure. Adornments limited to highly wrought ornaments only - no additional costume details beyond this. Facial features oval face with crimson cheeks and ruby lips must stay consistent. Signal-sender gesture pose indicates character status as signal-sender before capture. Avoid scene-specific blocking that conflicts with prisoner silhouette.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Character lacks explicit canonical naming in chapter text - visual details renderable but identity confirmation required before proceeding. Physical description is complete but identity confirmation needed regarding whether this figure represents Princess of Mars from story context. Clarification needed on character representation within story universe. No manual description input available at current path.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
