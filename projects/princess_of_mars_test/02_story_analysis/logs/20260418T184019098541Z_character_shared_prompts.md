# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:40:19.098541+00:00
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

Asset id: john_carter

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/john_carter.md

# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist observing from window, feels yearning for defeated "kindred people"

**Physical Presence:** Present (observes from upper floor window)

**Physical Description:** 
- Male human character
- Observes battle from elevated vantage point
- Shows emotional response to defeated warriors and prisoner
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Wears clothing appropriate for Martian environment
- Positioned at window of upper floor building
- Cultural ignorance noted (fails to signal help due to cultural differences)

**Useful Descriptive Noun Phrases:**
- "Heroic male figure"
- "Observer from elevated position"
- "Emotionally invested protagonist"
- "Human warrior in alien setting"

**Uncertainty Notes:**
- Specific physical features (hair, eyes, build) not detailed in source
- Exact costume details limited to general warrior attire

# Aliases

None



# Canonical Character ID

john_carter



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/john_carter_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: john_carter

[[SECTION purpose]]
Shared character reference for stable local generation of John Carter, focusing on silhouette and emotional state rather than specific facial features which are undefined in source.
[[/SECTION]]

[[SECTION positive_prompt]]
Heroic male figure, observer from elevated position, emotionally invested protagonist, human warrior in alien setting, wearing clothing appropriate for Martian environment, positioned at window of upper floor building, showing yearning expression, cultural ignorance noted.
[[/SECTION]]

[[SECTION negative_prompt]]
blurry, low resolution, wrong face, inconsistent costume, scene-specific blocking, crowded background, distorted limbs, specific facial features not detailed, proper nouns in prompt body.
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/john_carter.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Stable traits: Martian clothing, elevated position, emotional state (yearning). Avoid scene-specific blocking that breaks stability.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Address uncertainty regarding physical features by suggesting generic descriptors. Ensure costume logic remains consistent with alien setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
