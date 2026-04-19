# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:52:10.540168+00:00
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

Asset id: hills_beyond

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/hills_beyond.md

# Hills Beyond - CH008 Environment

## Environment Role
Secondary distant geography providing directional context and scale reference.

## Architecture and Geography
- Hill crests visible from plaza and building levels
- Slopes extending southeast/southwesterly directions
- Distant terrain beyond valley floor
- Elevated positions for air craft approach paths
- Background geography defining regional boundaries

## Lighting and Atmosphere Cues
- Daylight conditions across hill surfaces
- Light reflecting off slope faces
- Atmospheric haze at distant crest lines
- Smoke patterns drifting toward hill elevations
- Hill visibility from plaza level

## Scale Cues and Environmental Anchors
- Hill elevation provides vertical scale reference
- Crest lines visible from plaza define horizon
- Fleet approach paths dip below hill crests
- Southeast/southwesterly directional orientation established
- Distant terrain beyond valley establishes regional context

## Descriptive Noun Phrases for Render-Facing Prompts
- "hill crests visible from plaza and building levels"
- "slopes extending southeast/southwesterly directions"
- "distant terrain beyond valley floor"
- "elevated positions for air craft approach paths"
- "background geography defining regional boundaries"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: hills_beyond
[[SECTION purpose]]
This environment serves as a secondary distant geography providing directional context and scale reference for the main plaza and building levels. It defines regional boundaries and establishes horizon lines visible from elevated positions, ensuring consistent vertical scale against architectural elements.
[[/SECTION]]
[[SECTION positive_prompt]]
hill crests visible from plaza and building levels, slopes extending southeast/southwesterly directions, distant terrain beyond valley floor, elevated positions for air craft approach paths, background geography defining regional boundaries, daylight conditions across hill surfaces, light reflecting off slope faces, atmospheric haze at distant crest lines, smoke patterns drifting toward hill elevations, hill elevation provides vertical scale reference
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific brand names, indoor scenes, close-up details, urban density, water bodies, vegetation forests, night sky, storm clouds, fog obscuring visibility, low resolution, distorted geometry, floating elements, text overlays, human figures, vehicles on ground level, excessive detail, cluttered composition
[[/SECTION]]
[[SECTION inputs_markdown]]
- Asset ID: hills_beyond
- Project Slug: princess_of_mars_test
- Environment Role: Secondary distant geography providing directional context and scale reference.
- Architecture and Geography: Hill crests visible from plaza and building levels; Slopes extending southeast/southwesterly directions; Distant terrain beyond valley floor; Elevated positions for air craft approach paths; Background geography defining regional boundaries.
- Lighting and Atmosphere Cues: Daylight conditions across hill surfaces; Light reflecting off slope faces; Atmospheric haze at distant crest lines; Smoke patterns drifting toward hill elevations; Hill visibility from plaza level.
- Scale Cues and Environmental Anchors: Hill elevation provides vertical scale reference; Crest lines visible from plaza define horizon; Fleet approach paths dip below hill crests; Southeast/southwesterly directional orientation established; Distant terrain beyond valley establishes regional context.
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
- Ensure hill crests remain consistent in height relative to plaza level across shots.
- Maintain southeast/southwesterly directional orientation for slopes.
- Atmospheric haze should be present at distant crest lines but not obscure visibility of main anchors.
- Smoke patterns should drift toward hill elevations without blocking key environmental features.
- Hill elevation must provide clear vertical scale reference against building levels.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
- If hills appear too close, adjust distance to maintain secondary geography role.
- Ensure slope directions match southeast/southwesterly constraints.
- Check that atmospheric haze does not reduce visibility of crest lines below threshold.
- Verify smoke patterns do not obscure key environmental anchors like approach paths.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
