# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:35:58.971899+00:00
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

Asset id: green_martians

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martians.md

# green_martians

## Display Name
Green Martians

## Chapter Role
Warriors / Attackers

## Physical Presence
Present (Firing volleys, capturing ships)

## Physical Description
*   **Supported by Source:** Species traits defined in Visual Continuity notes.
    *   **Species:** Green Martians (implied green skin tone).
    *   **Equipment:** Wear spears.
    *   **Actions:** Climb windows to fire; swarm disabled ship from sides/windows using grappling hooks.
*   **Visual Identity:** Defined by species name and equipment usage.

## Costume & Silhouette
*   **Supported by Source:** Spears as primary weapon/tool.
*   **Continuity Traits:** Capable of vertical movement (climbing windows) and aerial/ground assault tactics.

## Uncertainty Notes
*   **Status:** Visual identity is defined by species classification and equipment. No manual description required for general representation.

# Aliases

warriors



# Canonical Character ID

green_martians



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martians_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martians

[[SECTION purpose]]
This prompt defines consistent visual representation for Green Martians across stable local generation runs. Focus on species traits, equipment, and recurring materials rather than scene-specific blocking to maintain continuity across generations.
[[/SECTION]]

[[SECTION positive_prompt]]
Green skin tone humanoid figure with spear equipment in hand. Vertical climbing posture near window frame. Grappling hook attached to limb for aerial assault. Warrior silhouette with tactical gear. Repeated green material texture on body surface. Compact weapon grip held firmly. Dynamic attack stance mid-movement.
[[/SECTION]]

[[SECTION negative_prompt]]
Human facial features, standard clothing, static pose, scene-specific blocking, background environment details, proper nouns, specific character names, human anatomy references, non-green skin tones, civilian attire, relaxed posture, grounded standing position, decorative elements unrelated to combat gear.
[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: green_martians
Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martians.md
Visual continuity notes reference for species traits and equipment specifications.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Species classification defines visual identity through green skin tone and spear equipment. Vertical movement capability (window climbing) and aerial assault tactics (grappling hooks) are recurring continuity traits. No manual description required for general representation as per source documentation.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Maintain consistent green material texture across all generations. Avoid introducing human facial features or civilian attire that conflicts with warrior silhouette. Keep equipment references to spears and grappling hooks only. Monitor for scene-specific blocking elements that may break continuity between runs.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
