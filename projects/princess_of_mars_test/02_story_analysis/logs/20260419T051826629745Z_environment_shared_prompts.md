# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:18:26.629745+00:00
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

Asset id: martian_buildings_valley

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/martian_buildings_valley.md

# Martian Buildings/Valley Environment

## Environment Role
Secondary battle setting with window fire positions and interior melting sequences.

## Architecture or Geography
Building interiors where Martians melt into structures within three minutes. Window positions serve as firing points for green warriors. Valley serves as approach route for airship fleet.

## Lighting and Atmosphere Cues
Terrific volley from windows with bullets dropping at explosion points. Banners dissolve in flame during battle sequence. Warriors melt into mist after engagement. Green warrior fire creates dramatic lighting effects.

## Scale Cues and Recurring Environmental Anchors
Green warriors fire volley from building windows. Lead vessel returns fire swinging broadside. Martians target specific points including sighting apparatus, gunners, officers. Fleet retreats with several craft limping. Building interiors serve as melting positions for Martians.

## Useful Descriptive Noun Phrases
Martian building interiors, window firing positions, green warrior volley, mist-melting warriors, explosion point bullets, sighting apparatus target, gunner position target, officer position target, valley approach route, building interior melting sequence.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: martian_buildings_valley
[[SECTION purpose]]
Generate stable architectural and atmospheric reference for extraterrestrial building interiors serving as secondary battle zones. Focus on window firing positions, interior melting sequences, valley approach routes, and green combatant volley points. Maintain consistent scale anchors including lead vessel broadside return fire positions and retreating craft limping formations. Use asset id martian_buildings_valley for stable generation continuity.
[[/SECTION]]
[[SECTION positive_prompt]]
extraterrestrial building interiors with window firing positions, interior melting sequences, valley approach route, green combatant volley points, lead vessel broadside return fire position, retreating craft limping formations, explosion point bullets, sighting apparatus target, gunner position target, officer position target, mist-melting warriors, dramatic lighting effects from combatant fire, banners dissolving in flame, airship fleet approach, building interior melting sequence
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific names, brand references, unrealistic physics, distorted architecture, inconsistent scale, floating elements, wrong color palette, blurred details, overexposed lighting, underexposed shadows, missing environmental anchors, unstable geometry, incorrect atmospheric density, broken continuity markers
[[/SECTION]]
[[SECTION inputs_markdown]]
asset_id: martian_buildings_valley
project_reference: princess_of_mars_test
environment_role: secondary battle setting with window fire positions and interior melting sequences
architecture_geography: building interiors where targets melt into structures within three minutes. Window positions serve as firing points for green warriors. Valley serves as approach route for airship fleet.
lighting_atmosphere_cues: terrific volley from windows with bullets dropping at explosion points. Banners dissolve in flame during battle sequence. Warriors melt into mist after engagement. Green warrior fire creates dramatic lighting effects.
scale_anchors: green warriors fire volley from building windows. Lead vessel returns fire swinging broadside. Targets specific points including sighting apparatus, gunners, officers. Fleet retreats with several craft limping. Building interiors serve as melting positions for targets.
useful_descriptive_phrases: extraterrestrial building interiors, window firing positions, green combatant volley, mist-melting warriors, explosion point bullets, sighting apparatus target, gunner position target, officer position target, valley approach route, building interior melting sequence
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Maintain consistent window firing position geometry across all generated frames. Keep valley approach route perspective stable for airship fleet sequences. Ensure lead vessel broadside return fire position remains anchored relative to building interiors. Preserve mist-melting warrior transition timing consistency. Match explosion point bullet drop patterns with atmospheric density. Align banner dissolving in flame sequence with battle engagement markers. Sustain green combatant volley intensity across multiple firing windows. Keep retreating craft limping formations consistent with fleet retreat narrative.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
If window firing positions appear inconsistent, re-anchor to original architectural blueprint. If valley approach route perspective shifts, realign with established horizon line. If lead vessel broadside return fire position drifts, reset relative to building interior reference points. If mist-melting warrior transitions vary in timing, standardize to three-minute melting sequence marker. If explosion point bullet drop patterns break continuity, recalibrate atmospheric density parameters. If banner dissolving in flame sequence desynchronizes, resync with battle engagement markers. If green combatant volley intensity fluctuates, normalize across all firing windows. If retreating craft limping formations become inconsistent, restore fleet retreat narrative alignment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
