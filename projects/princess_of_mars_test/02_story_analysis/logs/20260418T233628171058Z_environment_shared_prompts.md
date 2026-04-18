# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:36:28.171058+00:00
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

Asset id: disabled_airship

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/disabled_airship.md

**Environment Role:** Secondary / Action Hub (Transit Setting)

**Architecture or Geography:** Long, low, gray-painted vessel drifting unguided into the distance. Vessel structure includes upper works and stem-to-stern configuration.

**Lighting and Atmosphere Cues:** Sunlight gleaming on devices. Fire spurs from banners/upper works upon impact. Burning ship drifts southeast. Smoke and heat implied by burning state.

**Scale Cues and Recurring Environmental Anchors:** Large vessel compared to warriors. Banners swinging from stem to stern. Loot includes casks of water, silks, furs, stone vessels. Burning drift serves as a dynamic anchor.

**Descriptive Noun Phrases for Render-Facing Prompts:** Gray-painted airship hull, burning vessel drifting southeast, swinging banners on disabled ship, loot casks and stone vessels on deck, fire spurring from upper works.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: disabled_airship

[[SECTION purpose]]
Secondary action hub transit setting prompt for stable local generation. Defines gray-painted vessel drifting unguided into distance with upper works and stem-to-stern configuration. Supports fire spurring from banners/upper works upon impact. Burning ship drift serves as dynamic environmental anchor for warriors and loot elements.
[[/SECTION]]

[[SECTION positive_prompt]]
gray-painted airship hull, burning vessel drifting southeast, swinging banners on disabled ship, loot casks and stone vessels on deck, fire spurring from upper works, sunlight gleaming on devices, smoke and heat implied by burning state, large vessel compared to warriors, stem-to-stern configuration, upper works structure
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, unrelated terrain elements, static grounded architecture, calm weather conditions, intact hull without damage, absence of fire or smoke, small scale relative to environment, missing banners or loot items, daytime without sunlight cues, peaceful transit without impact effects
[[/SECTION]]

[[SECTION inputs_markdown]]
asset_id: disabled_airship
project_slug: princess_of_mars_test
environment_role: secondary_action_hub_transit_setting
architecture_geography: long_low_gray_painted_vessel_drifting_unguided_into_distance
lighting_atmosphere: sunlight_gleaming_on_devices_fire_spurs_from_banners_upper_works_upon_impact
scale_environmental_anchors: large_vessel_compared_to_warriors_banners_swinging_from_stem_to_stern_loot_casks_of_water_silks_furs_stone_vessels
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Burning drift serves as dynamic anchor for scene composition. Banners swinging from stem to stern maintain visual rhythm across vessel length. Loot elements (casks, silks, furs, stone vessels) provide texture anchors on deck. Fire spurring from upper works indicates impact state and maintains action hub role. Sunlight gleaming on devices establishes lighting consistency. Southeast drift direction maintained for continuity across shots.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Maintain burning vessel state without transitioning to intact hull. Keep fire spurring from upper works visible in all frames. Ensure banners remain swinging from stem to stern configuration. Preserve large vessel scale relative to warriors and loot items. Avoid proper nouns in prompt bodies for stable generation. Keep sunlight cues consistent with device gleaming effects.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
