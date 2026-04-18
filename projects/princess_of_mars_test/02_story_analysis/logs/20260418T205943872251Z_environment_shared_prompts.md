# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:59:43.872251+00:00
- task: environment_shared_prompts

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

Asset id: disabled_martian_ship

Task: write one reusable shared environment-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment_prompt
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

- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/disabled_martian_ship.md

**Role:** Secondary setting / Looting target

**Architecture/Geography:** Martian air vessel hauled to ground with systematic rifling. Stone vessels, arms, ammunition, silks, furs, jewels visible during looting sequences.

**Lighting/Atmosphere:** Daylight conditions with fire from last warrior creating funeral pyre atmosphere. Ship appears unmanned and helpless after receiving brunt of fire.

**Scale:** Medium-scale vessel interior with systematic emptying process. Stone vessels and equipment provide reference points for rifling operations.

**Anchors:** Vessel hull, stone vessels, arms storage, ammunition compartments, silk/fur storage areas, jewel containers, food/water supplies.

**Descriptive Phrases:** Disabled Martian ship, ground-hauled vessel, systematic rifling zone, stone vessel storage, arms and ammunition compartments, funeral pyre atmosphere, unmanned helpless craft.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: disabled_martian_ship
[[SECTION purpose]]
Stable local generation prompt for disabled martian ship environment reference. Defines vessel interior, looting zone architecture, funeral pyre atmosphere, and systematic emptying process anchors for consistent environmental rendering across story sequences.
[[/SECTION]]
[[SECTION positive_prompt]]
Ground-hauled vessel interior with systematic rifling zone. Stone vessel storage compartments visible. Arms and ammunition storage areas present. Silk and fur storage containers in view. Jewel containers scattered throughout. Food and water supply areas intact. Daylight conditions with funeral pyre atmosphere from last warrior fire. Unmanned helpless craft appearance. Medium-scale vessel interior architecture. Vessel hull structural elements prominent.
[[/SECTION]]
[[SECTION negative_prompt]]
Proper nouns or brand names. Fully operational ship systems. Crew members or living beings present. Nighttime or darkness conditions. Overgrown vegetation or jungle elements. Modern technology or electronics visible. Bright neon lighting effects. Clean pristine condition without damage. Flying or airborne vessel state.
[[/SECTION]]
[[SECTION inputs_markdown]]
princess_of_mars_test_02_story_analysis_environment_breakdowns_disabled_martian_ship.md
disabled_martian_ship_asset_reference
ground_hauled_vessel_interior_anchor
stone_vessel_storage_compartment
arms_ammo_storage_area
funeral_pyre_atmosphere_reference
unmanned_helpless_craft_state
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Maintain vessel interior scale consistency across all shots. Keep funeral pyre atmosphere intensity stable for looting sequences. Ensure stone vessel storage compartments remain visible reference points. Preserve arms and ammunition compartment locations throughout environment variations. Match unmanned helpless craft appearance in all environmental states. Coordinate silk/fur/jewel container placements with story progression.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Review vessel hull structural element visibility if interior shots appear too empty. Adjust funeral pyre atmosphere intensity if daylight conditions conflict with fire elements. Verify stone vessel storage compartments maintain consistent scale across environment variations. Check arms and ammunition compartment locations remain stable for systematic rifling operations. Ensure unmanned helpless craft appearance doesn't contradict any operational system indicators.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
