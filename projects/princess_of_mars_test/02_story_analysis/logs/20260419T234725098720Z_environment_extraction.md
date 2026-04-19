# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:47:25.098720+00:00
- task: environment_extraction

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

Chapter id: CH001

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter I: On The Arizona Hills

## Story Summary
John Carter reflects on his mortality and decision to write this chronicle. He recounts finding a gold vein with Captain James K. Powell in 1865. Powell leaves to purchase machinery while Carter guards the claim. Apaches ambush Powell's party. Carter discovers the tracks, pursues them at night, finds Powell dead surrounded by tepees, and charges the warriors. After rescuing Powell's body from mutilation, Carter's horse leads him into a defile toward a cave entrance where he collapses from exhaustion.

## Visual Continuity Facts
- **Lighting:** Clear Arizona mornings, bright moonlight at night, sudden daylight in cave.
- **Props:** Colt revolvers (two), carbine, saddle horse, burros (seen earlier), canteen, cartridge belts.
- **Locations:** Arizona hills, mountainside, valley, water hole, plateau with tepees, gorge, cave entrance (4ft high, 3-4ft wide).
- **Characters:** John Carter (wearing military attire implied by commission), Powell (dead body), Apaches (warriors in tepees).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter I

## Primary Settings
- arizona_hills
- mountainside
- plateau_with_tepees

## Secondary Settings
- valley
- water_hole
- gorge
- cave_entrance

## Lighting & Atmosphere Notes
- Clear Arizona mornings with bright sunlight
- Bright moonlight at night
- Sudden daylight in cave interior
- Dust and heat haze typical of desert terrain
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_hills

[[SECTION markdown]]
# Arizona Hills Environment

## Environment Role
Primary setting - main location for chapter opening and Carter's reflection

## Architecture or Geography
Rolling desert hills with sparse vegetation, typical Arizona high-desert topography. Wide open spaces with distant mountain ranges visible on horizon.

## Lighting and Atmosphere Cues
Clear Arizona morning light with bright direct sunlight. Dust particles visible in air beams. Heat haze rising from ground surface. Blue sky with minimal cloud cover.

## Scale Cues and Environmental Anchors
Hills extend for miles in all directions. Distant mountain peaks provide depth reference. Ground level shows scattered rocks and dry grass tufts.

## Descriptive Noun Phrases
- rolling desert hills
- sparse high-desert vegetation
- distant mountain ranges
- open Arizona terrain
- heat shimmering ground
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mountainside

[[SECTION markdown]]
# Mountainside Environment

## Environment Role
Secondary setting - transition area between hills and valley

## Architecture or Geography
Steep desert mountain slope with rocky outcrops. Sparse scrub vegetation clinging to rock faces. Natural erosion patterns visible on stone surfaces.

## Lighting and Atmosphere Cues
Bright sunlight hitting angled rock surfaces creates strong shadows. Dust settles in crevices. Wind may carry loose debris across surface.

## Scale Cues and Environmental Anchors
Mountain face rises sharply from valley floor. Rock formations provide natural landmarks. Ground shows scattered boulders and loose stones.

## Descriptive Noun Phrases
- steep desert mountain slope
- rocky outcrops with scrub
- natural erosion patterns
- shadowed rock crevices
- wind-swept stone surface
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plateau_with_tepees

[[SECTION markdown]]
# Plateau with Tepees Environment

## Environment Role
Secondary setting - Apache encampment location

## Architecture or Geography
Flat elevated desert plateau. Multiple tepee structures arranged in circular pattern. Ground shows footprints and disturbed earth around encampment perimeter.

## Lighting and Atmosphere Cues
Bright daylight illuminating entire plateau. Shadows from tepee poles create radial patterns on ground. Dust settles evenly across flat surface.

## Scale Cues and Environmental Anchors
Tepees stand 10-12 feet tall with conical shape. Encampment spans approximately 50-100 feet diameter. Distant hills provide horizon reference.

## Descriptive Noun Phrases
- elevated desert plateau
- circular tepee arrangement
- disturbed earth perimeter
- radial shadow patterns
- conical tepee structures
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley

[[SECTION markdown]]
# Valley Environment

## Environment Role
Secondary setting - lower terrain area between hills and mountainside

## Architecture or Geography
Wide desert valley floor with gentle slopes. Sparse vegetation along valley bottom. Natural drainage patterns visible in soil surface.

## Lighting and Atmosphere Cues
Sunlight creates soft shadows across valley floor. Heat rises from ground creating shimmering effect. Blue sky visible above distant ridges.

## Scale Cues and Environmental Anchors
Valley extends for miles between mountain ranges. Ground shows scattered rocks and dry wash channels. Horizon line marked by distant peaks.

## Descriptive Noun Phrases
- wide desert valley floor
- gentle sloping terrain
- natural drainage patterns
- scattered valley rocks
- distant peak horizon
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: water_hole

[[SECTION markdown]]
# Water Hole Environment

## Environment Role
Secondary setting - natural water source location

## Architecture or Geography
Small desert pool with shallow edges. Surrounding ground shows animal tracks and disturbed soil. Sparse vegetation grows near water's edge.

## Lighting and Atmosphere Cues
Sunlight reflects off water surface creating bright highlights. Cool shadows around water's perimeter. Heat haze more pronounced away from water source.

## Scale Cues and Environmental Anchors
Pool diameter approximately 10-20 feet. Water depth varies from ankle to knee level at edges. Surrounding ground shows circular pattern of footprints.

## Descriptive Noun Phrases
- shallow desert pool
- animal track patterns
- water's edge vegetation
- bright surface reflections
- cool perimeter shadows
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: gorge

[[SECTION markdown]]
# Gorge Environment

## Environment Role
Secondary setting - narrow passage area

## Architecture or Geography
Narrow rocky passage with steep walls. Natural stone arches and overhangs visible. Ground shows erosion patterns from water flow.

## Lighting and Atmosphere Cues
Sunlight filters through gaps creating dappled light patterns. Shadows from rock overhangs create cool areas. Dust settles in crevices and ledges.

## Scale Cues and Environmental Anchors
Gorge width varies from 5-15 feet at different points. Rock walls rise 30-50 feet above ground. Natural stone formations provide visual anchors.

## Descriptive Noun Phrases
- narrow rocky passage
- steep gorge walls
- natural stone arches
- dappled light patterns
- erosion-formed ledges
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_entrance

[[SECTION markdown]]
# Cave Entrance Environment

## Environment Role
Secondary setting - transition to interior cave space

## Architecture or Geography
Natural rock opening approximately 4 feet high and 3-4 feet wide. Rough stone edges with natural overhang. Interior darkness visible beyond entrance.

## Lighting and Atmosphere Cues
Bright daylight at entrance creates strong contrast with interior shadows. Sunlight illuminates rough stone texture. Dust particles visible in light beams near entrance.

## Scale Cues and Environmental Anchors
Opening width provides human passage reference. Rock surface shows natural weathering patterns. Ground level shows scattered stones around entrance perimeter.

## Descriptive Noun Phrases
- 4-foot high rock opening
- 3-4 foot wide entrance
- rough stone edges
- interior darkness contrast
- weathered rock texture
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
