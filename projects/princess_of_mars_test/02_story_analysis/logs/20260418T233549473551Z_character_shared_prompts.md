# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:35:49.473551+00:00
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

# green_martian_females

## Display Name
Green Martian Females

## Chapter Role
Captors / Draggers

## Physical Presence
Present (Dragging prisoner into a building)

## Physical Description
*   **Supported by Source:** Subset of Green Martians. Inherits species traits (green skin, etc.).
    *   **Specific Action:** Identified as the group dragging the prisoner into the building upon return to the plaza.
*   **Visual Identity:** Defined by species classification and specific action role.

## Costume & Silhouette
*   **Supported by Source:** Spears (inherited from general Green Martians).
*   **Continuity Traits:** Distinguished from male warriors by gender and specific capture action in this chapter.

## Uncertainty Notes
*   **Status:** Visual identity is defined by species classification and specific role within the group. No manual description required for image generation based on current text.

# Aliases

None



# Canonical Character ID

green_martian_females



# Fully Identified

true

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
[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martian_females
[[SECTION purpose]]
Generate consistent female Green Martian captors based on species traits and action role. Focus on stable visual identity (green skin, spears) rather than scene-specific blocking. Use asset id green_martian_females for tracking.
[[/SECTION]]
[[SECTION positive_prompt]]
green-skinned humanoid female, slender build, holding spears, dragging prisoner, intense gaze, metallic spear tips, functional attire, outdoor lighting, dynamic movement, species texture details
[[/SECTION]]
[[SECTION negative_prompt]]
human skin tone, male features, civilian clothing, static pose, low resolution, blurry details, text, watermark, soft focus, human anatomy proportions
[[/SECTION]]
[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_females.md
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Maintain consistent green skin tone across generations. Ensure spear placement reflects capture action (dragging). Distinguish from male warriors via gender markers in facial structure and body type. Note: Manual description path missing, rely on breakdown notes for species traits.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
If gender appears ambiguous, adjust facial structure keywords. If lighting is too flat, add outdoor plaza context. If skin tone shifts, reinforce green-skinned descriptor. Check spear metallic texture if dull.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
