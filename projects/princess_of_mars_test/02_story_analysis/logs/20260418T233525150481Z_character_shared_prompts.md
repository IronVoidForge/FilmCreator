# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:35:25.150481+00:00
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

# carter

## Display Name
Carter

## Chapter Role
Observer / Commander (Implied)

## Physical Presence
Referenced (Observes from window/balcony)

## Physical Description
*   **Supported by Source:** None. The text provides no physical description for Carter in this chapter.
*   **Visual Identity:** Unknown. Cannot be generated based on current text.

## Costume & Silhouette
*   **Supported by Source:** None.
*   **Continuity Traits:** None recorded in this chapter.

## Uncertainty Notes
*   **Critical Missing Info:** Visual appearance is entirely undefined in the provided material. Manual description required for future image generation.
*   **Context:** Carter is identified by name but lacks physical attributes in Chapter CH008.

# Aliases

None



# Canonical Character ID

carter



# Fully Identified

false

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
Carter is an Observer/Commander figure referenced in Chapter CH008 with no physical description provided in source material. Visual identity, costume, and silhouette are entirely undefined per uncertainty notes. Manual character description required before stable image generation can proceed. Current prompts use general descriptive terms to accommodate future manual input addition.

[[/SECTION]]

[[SECTION positive_prompt]]
Observer standing at window or balcony, composed posture, formal attire, neutral expression, clean lines, structured silhouette, muted color palette, professional appearance, calm demeanor, architectural background, minimalistic design, steady stance, dignified presence, understated elegance, composed figure, restrained movement, balanced composition

[[/SECTION]]

[[SECTION negative_prompt]]
exaggerated features, distorted proportions, overly detailed textures, chaotic blocking, bright saturated colors, emotional expressions, dynamic action poses, cluttered background, messy silhouette, informal clothing, casual stance, animated gestures, complex patterns, ornate details, busy composition, unrealistic anatomy, inconsistent lighting, over-processed appearance

[[/SECTION]]

[[SECTION inputs_markdown]]
Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md (missing)
Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/carter.md
Current status: Visual appearance undefined in Chapter CH008 source material. Manual description required per uncertainty notes before stable generation can proceed.

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Carter identified by name only with no physical attributes recorded in Chapter CH008. Physical presence supported by source is limited to window/balcony observation location. Costume and silhouette traits not recorded in chapter material. Visual identity unknown per uncertainty notes. Manual description input required for future image generation. Face, hair, body type, costume logic, silhouette, and recurring materials cannot be specified without manual character description addition.

[[/SECTION]]

[[SECTION repair_notes_markdown]]
Add manual character description to projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md before stable generation can proceed. Current prompts use general descriptive terms to accommodate future manual input. Once manual description is added, update positive/negative prompts with specific face, hair, body type, costume logic, silhouette, and recurring materials from that manual description.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
