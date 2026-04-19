# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T06:32:31.978703+00:00
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

Asset id: earthling_woman

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/earthling_woman.md

# Earthling Woman (Captive)

## Display Name
Earthling Woman / Captive

## Chapter Role
Primary captive figure brought to the plaza after airship battle; central reference point for narrator's observations of Martian customs and treatment of prisoners.

## Physical Presence
**Present:** Yes - Physically present in Story Beat 3, dragged into building by Martian females while being observed from window.

## Physical Description (Supported by Source)
- **Figure:** Slender, girlish figure similar to earthly women
- **Face:** Oval face with finely chiseled features
- **Eyes:** Large lustrous eyes
- **Hair:** Coal black waving hair caught loosely
- **Skin:** Light reddish copper color with crimson glow of cheeks and ruby lips
- **Attire:** Destitute of clothes; highly wrought ornaments only

## Costume & Silhouette
- **Silhouette:** Slender, feminine form with loose hair arrangement
- **Ornaments:** Highly wrought decorative pieces (specific types not detailed)
- **State:** Naked/clothless except for ornamental pieces

## Continuity-Critical Traits
- Captive status established through being dragged by Martian females
- Physical description provides stable reference for character identification
- Copper skin color distinguishes from typical human appearance
- Ornamentation suggests cultural significance despite destitution

## Render-Facing Prompt Elements
"Slender girlish figure with oval face, copper skin, coal black waving hair caught loosely, large lustrous eyes, light reddish copper complexion with crimson glow of cheeks and ruby lips, destitute of clothes except highly wrought ornaments"

## Uncertainty Notes
- Specific ornament types not detailed in source material
- Exact cultural context of ornaments unclear
- Emotional state beyond physical description not specified

# Aliases

None



# Canonical Character ID

earthling_woman



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/earthling_woman_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: earthling_woman

[[SECTION purpose]]
Reusable shared character reference prompt for stable local generation of the Earthling Woman captive figure. This prompt establishes consistent physical appearance including facial structure, skin tone, hair style, and ornamentation across different scenes while avoiding scene-specific blocking or proper nouns. Designed for maintaining visual continuity when rendering this character in various contexts within the story.
[[/SECTION]]

[[SECTION positive_prompt]]
Slender girlish figure with oval face and finely chiseled features, large lustrous eyes, coal black waving hair caught loosely, light reddish copper skin tone with crimson glow on cheeks and ruby lips, destitute of clothes except highly wrought decorative ornaments, feminine silhouette with loose hair arrangement
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific cultural references, scene blocking, background elements, clothing details beyond ornaments, emotional expressions not specified, facial features inconsistent with oval face description, skin color variations from copper tone, hair styles other than coal black waving, ornament types not detailed in source material
[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: earthling_woman
Character Role: Primary captive figure brought to plaza after airship battle
Physical Presence: Present in Story Beat 3, dragged into building by Martian females while observed from window
Continuity Status: Fully identified with stable physical description
Render Priority: High - central reference point for narrator observations of Martian customs and treatment of prisoners
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Copper skin color distinguishes from typical human appearance and provides stable identification marker. Ornamentation suggests cultural significance despite destitute state, though specific types remain undefined in source material. Captive status established through being dragged by Martian females creates important narrative context for character positioning. Physical description provides consistent reference for character identification across different renderings.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Uncertainty regarding exact cultural context of ornaments requires careful handling to avoid inventing specific types not detailed in source material. Emotional state beyond physical description not specified should be avoided in prompt generation. Face features must maintain oval shape with finely chiseled characteristics for consistency. Skin tone variations from light reddish copper should be minimized to preserve character identification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
