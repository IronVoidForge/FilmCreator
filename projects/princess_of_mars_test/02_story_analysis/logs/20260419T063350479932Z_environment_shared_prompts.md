# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T06:33:50.479932+00:00
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

Asset id: drifting_warship

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/drifting_warship.md

# Drifting Warship - Salvage and Funeral Pyre Zone

## Environment Role
Secondary setting for salvage operation and memorial pyre; transit zone between combat area and towing sequence

## Architecture and Geography
Large gray-painted airship vessel, long and low profile. Hull structure with upper works mowed through by projectiles. Banners dissolved in flame on exterior surfaces. Interior spaces accessible through damaged hull openings. Vessel positioned in valley sky above city plaza. Drifting craft converted to funeral pyre with burning banners and upper works.

## Lighting and Atmosphere Cues
Daylight conditions during initial observation from building windows. Fire illumination from burning warship creates dramatic atmospheric effects. Flames consume banners and mowed upper works. Crimson glow from captive's skin visible against fire backdrop. Smoke and ash create atmospheric haze around vessel. Dramatic contrast between gray hull and orange flames.

## Scale Cues and Environmental Anchors
Vessel size established through observation from building windows. Hull length accommodates multiple Martian warriors for boarding and looting operations. Upper works height allows projectile damage to be clearly visible. Vessel width provides space for arms, ammunition, silks, furs, jewels, stone vessels, and water casks. Valley sky establishes altitude context relative to city below.

## Descriptive Noun Phrases
- Large gray-painted airship vessel
- Long low profile hull structure
- Upper works mowed through by projectiles
- Banners dissolved in flame on exterior
- Interior spaces accessible through damaged openings
- Drifting craft converted to funeral pyre
- Salvage zone with arms ammunition silks furs jewels
- Stone vessels and water casks as loot items
- Burning warship soaring majestically into air
- Floating funeral pyre in valley sky

## Render-Facing Prompt Elements
```
large gray-painted airship vessel, long low profile hull, upper works mowed through by projectiles, banners dissolved in flame on exterior, interior spaces accessible through damaged openings, drifting craft converted to funeral pyre, salvage zone with arms ammunition silks furs jewels stone vessels water casks, burning warship soaring majestically into air, floating funeral pyre in valley sky, fire illumination creating dramatic atmospheric effects
```

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: drifting_warship
[[SECTION purpose]]
Secondary setting for salvage operation and memorial pyre; transit zone between combat area and towing sequence
[[/SECTION]]
[[SECTION positive_prompt]]
large gray-painted airship vessel, long low profile hull, upper works mowed through by projectiles, banners dissolved in flame on exterior, interior spaces accessible through damaged openings, drifting craft converted to funeral pyre, salvage zone with arms ammunition silks furs jewels stone vessels water casks, burning warship soaring majestically into air, floating funeral pyre in valley sky, fire illumination creating dramatic atmospheric effects
[[/SECTION]]
[[SECTION negative_prompt]]
blurry, distorted, low resolution, watermark, text, signature, oversaturated, underexposed, noisy
[[/SECTION]]
[[SECTION inputs_markdown]]
# Drifting Warship - Salvage and Funeral Pyre Zone

## Environment Role
Secondary setting for salvage operation and memorial pyre; transit zone between combat area and towing sequence

## Architecture and Geography
Large gray-painted airship vessel, long and low profile. Hull structure with upper works mowed through by projectiles. Banners dissolved in flame on exterior surfaces. Interior spaces accessible through damaged hull openings. Vessel positioned in valley sky above city plaza. Drifting craft converted to funeral pyre with burning banners and upper works.

## Lighting and Atmosphere Cues
Daylight conditions during initial observation from building windows. Fire illumination from burning warship creates dramatic atmospheric effects. Flames consume banners and mowed upper works. Crimson glow from captive's skin visible against fire backdrop. Smoke and ash create atmospheric haze around vessel. Dramatic contrast between gray hull and orange flames.

## Scale Cues and Environmental Anchors
Vessel size established through observation from building windows. Hull length accommodates multiple Martian warriors for boarding and looting operations. Upper works height allows projectile damage to be clearly visible. Vessel width provides space for arms, ammunition, silks, furs, jewels, stone vessels, and water casks. Valley sky establishes altitude context relative to city below.

## Descriptive Noun Phrases
- Large gray-painted airship vessel
- Long low profile hull structure
- Upper works mowed through by projectiles
- Banners dissolved in flame on exterior
- Interior spaces accessible through damaged openings
- Drifting craft converted to funeral pyre
- Salvage zone with arms ammunition silks furs jewels
- Stone vessels and water casks as loot items
- Burning warship soaring majestically into air
- Floating funeral pyre in valley sky

## Render-Facing Prompt Elements
large gray-painted airship vessel, long low profile hull, upper works mowed through by projectiles, banners dissolved in flame on exterior, interior spaces accessible through damaged openings, drifting craft converted to funeral pyre, salvage zone with arms ammunition silks furs jewels stone vessels water casks, burning warship soaring majestically into air, floating funeral pyre in valley sky, fire illumination creating dramatic atmospheric effects
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
- Environment serves as a secondary setting for the salvage operation and memorial pyre.
- Acts as a transit zone between the combat area and the towing sequence.
- Vessel is positioned in the valley sky above the city plaza.
- Drifting craft converted to funeral pyre with burning banners and upper works.
- Scale established through observation from building windows relative to city below.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
- Ensure prompts avoid proper nouns (e.g., "Martian" replaced with descriptive terms if needed).
- Maintain stable architecture and geography descriptions.
- Focus on visible environmental anchors like the valley sky and city plaza.
- Keep atmosphere consistent with fire illumination and daylight conditions.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
