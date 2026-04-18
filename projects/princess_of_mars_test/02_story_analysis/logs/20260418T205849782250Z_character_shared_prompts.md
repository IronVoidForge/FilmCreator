# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:58:49.782250+00:00
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

Asset id: green_martian_females

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_females.md

# Green Martian Females

**Chapter Role:** Warriors / Captors  
**Physical Presence:** Referenced (not individually present)  

## Physical Description
*Only described as "green" in source material. No detailed physical features documented.*

## Costume & Silhouette
*Unknown - no visual documentation available beyond color descriptor.*

## Continuity-Critical Traits
- Fire volley from building windows facing valley
- Drag prisoner into building with green Martian females
- Board disabled ship with spears and grappling hooks
- Systematically rifle vessel for loot
- Set disabled ship on fire as floating funeral pyre

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance extremely limited. "Green" is only documented feature.  
**Key Phrases for Later Use:** "green Martian females," "warriors from building windows," "captors of prisoner"

## Important Notes
- Character identification too weak for stable reruns without clarification
- May already exist under different cultural name or designation
- Manual description required before any image generation can proceed reliably

# Aliases

None



# Canonical Character ID

green_martian_females



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martian_females_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1
[[/FILMCREATOR_PACKET]]
[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martian_females
[[/FILMCREATOR_RECORD]]
[[SECTION purpose]]
Base prompt for green_martian_females asset. Focuses on known descriptors (green skin, warrior role) while flagging lack of detailed physical data in source material. Intended for stable local generation where specific face/hair details are undefined.
[[/SECTION]]
[[SECTION positive_prompt]]
green-skinned female warrior, alien silhouette, armored tactical gear, holding spears, dynamic combat stance, cinematic lighting, volumetric fog, neutral expression, functional costume
[[/SECTION]]
[[SECTION negative_prompt]]
ugly, deformed, extra fingers, bad anatomy, human facial features, pale skin, western clothing, low resolution, blurry, text, watermark
[[/SECTION]]
[[SECTION inputs_markdown]]
Project: princess_of_mars_test. Source: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_females.md. Asset ID: green_martian_females.
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Source material only documents 'green' color. No specific face, hair, or body type details available. Role defined as Warriors/Captors. Render-Facing Prompt Notes indicate physical appearance extremely limited. Manual description required for stable reruns to resolve ambiguity on facial features and attire specifics.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Add manual physical description before generating detailed shots to resolve ambiguity on facial features and attire specifics. Ensure costume logic aligns with 'warrior' archetype rather than generic human clothing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
