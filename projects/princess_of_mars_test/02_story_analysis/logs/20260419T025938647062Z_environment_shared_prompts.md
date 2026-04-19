# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:59:38.647062+00:00
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

Asset id: outlying_hills_hill_crest

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/outlying_hills_hill_crest.md

# Outlying Hills / Hill Crest

## Environment Role
Secondary setting for fleet sighting and approach.

## Architecture or Geography
Outlying hills, hill crest elevation.

## Lighting and Atmosphere Cues
Distant view, gray sky implied by airships, approach from elevation.

## Scale Cues and Recurring Environmental Anchors
Hill crest, distant city skyline, fleet count approximates twenty vessels.

## Useful Descriptive Noun Phrases
"Hill crest", "Outlying ridge", "Fleet approach path".

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: outlying_hills_hill_crest

[[SECTION purpose]]
Generate stable environmental reference prompts for secondary fleet sighting setting featuring elevated hill terrain with distant atmospheric depth and airship-scale approach paths. Use consistent asset identifiers for architecture, geography, lighting, atmosphere, scale, and recurring anchors across all generation tasks.
[[/SECTION]]

[[SECTION positive_prompt]]
hill crest elevation, outlying ridge landscape, gray sky atmosphere, distant city skyline view, fleet approach path from height, twenty vessel formation, elevated terrain anchor, atmospheric depth, airship-scale geometry, horizon line visibility, approach trajectory, distant urban silhouette, hilltop vantage point, atmospheric haze, elevated perspective, fleet alignment pattern
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific brand names, indoor scenes, close-up details, ground-level view, bright sunny conditions, foggy obscuration, single vessel, crowded composition, low angle perspective, urban foreground elements, detailed mechanical parts, text overlays, logos, signatures, water reflections, cloud cover, night lighting, artificial illumination sources
[[/SECTION]]

[[SECTION inputs_markdown]]
# Environment Reference Inputs

## Asset Identifier: outlying_hills_hill_crest

### Architecture or Geography
- Primary terrain: hill crest elevation
- Secondary features: outlying ridge landscape
- View type: distant atmospheric depth

### Lighting and Atmosphere Cues
- Sky condition: gray sky implied by airships
- Approach direction: from elevated height
- Atmospheric quality: haze with horizon visibility

### Scale Cues and Recurring Environmental Anchors
- Fleet count: approximates twenty vessels
- Primary anchor: hill crest elevation
- Secondary anchor: distant city skyline silhouette

### Useful Descriptive Noun Phrases
- Hill crest
- Outlying ridge
- Fleet approach path
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
## Continuity Notes for Environment Generation

1. Maintain consistent asset identifier outlying_hills_hill_crest across all generation tasks
2. Preserve elevated perspective as primary viewpoint anchor
3. Keep fleet count at approximately twenty vessels for scale consistency
4. Ensure gray sky atmosphere remains visible without obscuration
5. Distant city skyline should appear as silhouette, not detailed foreground element
6. Approach trajectory must originate from height, not ground level
7. Hill crest elevation serves as primary environmental anchor point
8. Atmospheric haze provides depth without reducing visibility of key elements

## Recurring Environmental Anchors
- Hill crest elevation (primary)
- Outlying ridge landscape (secondary)
- Distant city skyline silhouette (tertiary)
- Fleet approach path from height (action anchor)
[[/SECTION]]

[[SECTION repair_notes_markdown]]
## Repair Notes for Environment Generation

### Common Issues to Address
1. If proper nouns appear in prompts, replace with descriptive noun phrases
2. Ensure elevated perspective is maintained across all generations
3. Verify fleet count remains approximately twenty vessels
4. Check that gray sky atmosphere is visible without foggy obscuration
5. Confirm distant city skyline appears as silhouette, not detailed foreground
6. Validate approach trajectory originates from height, not ground level

### Quality Checks
- Asset identifier consistency: outlying_hills_hill_crest
- Perspective elevation: maintained at hill crest level
- Fleet scale: approximately twenty vessels visible
- Atmospheric quality: gray sky with haze depth
- View distance: distant city skyline as silhouette
- Approach direction: from elevated height

### Stability Markers
- Architecture geography: outlying hills, hill crest elevation
- Lighting atmosphere: gray sky, atmospheric haze
- Scale anchors: hill crest, fleet count, distant skyline
- Recurring elements: approach path, elevation perspective
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
