# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T15:52:56.189848+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
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



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

## Story Summary

Carter and Sola return from an incubator ceremony but are ordered to retreat immediately upon spotting a fleet of enemy airships approaching the city. A battle erupts where Green Martians fire first, catching the ships off guard. The Martians then target ship crews and equipment with high accuracy. One ship is disabled, drifting down toward the city. Martians board the vessel, loot arms, jewels, and water, then burn it from within before towing it away. Carter returns to the city plaza where he witnesses a captured humanoid female being dragged into a building. She makes eye contact with Carter and signals for help, but is taken away before he can respond due to his ignorance of local customs.

## Visual Continuity Facts

- **Characters:** John Carter (human), Sola (Martian companion), Woola (hound).
- **Enemies:** Green Martians (green attire, mounted warriors), Gray Airships (long, low, gray-painted, banners on stem/stern).
- **Prisoner:** Slender girlish figure, light reddish copper skin, coal black hair, no clothes except ornaments.
- **Locations:** City buildings (upper floors, windows), Valley, Hills, Plaza.
- **Objects:** Chariots, mastodons, spears, grappling hooks, casks of water, stone vessels.
- **Events:** Incubator ceremony aftermath, airship fleet arrival, volley fire, ship burning, prisoner capture.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test

## Extracted Environments

| Asset ID | Environment Name | Role | Architecture/Geography |
|----------|------------------|------|------------------------|
| city_buildings | City Buildings | Primary Setting | Upper floors, windows, stone structures |
| valley | The Valley | Transit Setting | Open terrain, natural landscape |
| hills | Hills | Secondary Setting | Elevated terrain, distant views |
| plaza | City Plaza | Primary Setting | Open gathering space, central location |

## Environment Descriptions

Each environment file contains detailed render-facing information including role, architecture, lighting cues, scale anchors, and descriptive noun phrases for prompt writing.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_buildings

[[SECTION markdown]]
# City Buildings - Environment File

## Environment Role
Primary setting - main urban location where characters interact with the city infrastructure

## Architecture and Geography
- Multi-story stone structures with upper floors
- Windowed facades facing outward
- Dense urban clustering
- Vertical building arrangements typical of Martian city design

## Lighting and Atmosphere Cues
- Natural daylight filtering through windows
- Interior shadows on upper levels
- Exterior ambient light from valley surroundings
- Atmospheric haze between buildings

## Scale Cues and Environmental Anchors
- Building height relative to human/Martian figures
- Window size indicating interior spaces
- Street level perspective for plaza connection
- Stone material texture as recurring anchor

## Descriptive Noun Phrases
- "stone upper floors"
- "windowed facades"
- "urban stone structures"
- "city building exteriors"
- "upper level windows"
- "stone architectural elements"
- "Martian city buildings"
- "building window frames"

## Render-Facing Notes
- Focus on verticality and density
- Emphasize stone texture consistency
- Include atmospheric haze between structures
- Maintain scale relative to character figures

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley

[[SECTION markdown]]
# The Valley - Environment File

## Environment Role
Transit setting - open terrain connecting city locations and battle zones

## Architecture and Geography
- Open natural landscape
- Wide valley floor with gentle slopes
- Natural terrain features without artificial structures
- Connection points between hills and city buildings

## Lighting and Atmosphere Cues
- Broad daylight illumination across valley floor
- Soft shadows from distant hills
- Atmospheric depth through valley perspective
- Natural ambient light from surrounding terrain

## Scale Cues and Environmental Anchors
- Valley width relative to character movement paths
- Distant hill silhouettes as horizon anchors
- Ground texture consistency across open space
- Battle zone scale indicators

## Descriptive Noun Phrases
- "open valley floor"
- "natural landscape terrain"
- "valley ground surfaces"
- "wide valley spaces"
- "valley perspective views"
- "terrain connection points"
- "Martian valley landscapes"
- "valley battle zones"

## Render-Facing Notes
- Emphasize open space and depth
- Include distant hill silhouettes for scale
- Maintain natural terrain texture consistency
- Focus on atmospheric perspective cues

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills

[[SECTION markdown]]
# Hills - Environment File

## Environment Role
Secondary setting - elevated terrain providing vantage points and distant views

## Architecture and Geography
- Elevated natural terrain formations
- Rolling hill surfaces with gentle slopes
- Distant horizon line features
- Connection to valley floor below

## Lighting and Atmosphere Cues
- Sunlight hitting hill tops at varying angles
- Shadowed lower slopes creating depth
- Atmospheric haze from distance perspective
- Natural ambient light from valley surroundings

## Scale Cues and Environmental Anchors
- Hill height relative to character figures
- Distant city building silhouettes as anchors
- Terrain slope consistency across surfaces
- Horizon line markers for scale reference

## Descriptive Noun Phrases
- "elevated hill terrain"
- "rolling hill surfaces"
- "hill top formations"
- "distant hill silhouettes"
- "hill slope textures"
- "elevated landscape views"
- "Martian hill terrains"
- "hill horizon markers"

## Render-Facing Notes
- Emphasize elevation and height variation
- Include distant city building references for scale
- Maintain natural terrain texture consistency
- Focus on atmospheric depth cues from valley perspective

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza

[[SECTION markdown]]
# City Plaza - Environment File

## Environment Role
Primary setting - central gathering space where key character interactions occur

## Architecture and Geography
- Open urban gathering space
- Central city location with building connections
- Stone-paved or constructed surface
- Connection points to surrounding city buildings

## Lighting and Atmosphere Cues
- Natural daylight illuminating open plaza space
- Building shadows falling across plaza surface
- Atmospheric haze from surrounding structures
- Ambient light from valley surroundings visible in distance

## Scale Cues and Environmental Anchors
- Plaza width relative to character group sizes
- Surrounding building heights as vertical anchors
- Ground texture consistency with city buildings
- Distant valley/hill silhouettes for horizon reference

## Descriptive Noun Phrases
- "open plaza gathering space"
- "central city location"
- "plaza stone surfaces"
- "urban plaza grounds"
- "plaza connection points"
- "city plaza exteriors"
- "Martian plaza spaces"
- "plaza horizon views"

## Render-Facing Notes
- Emphasize open space with building connections
- Include surrounding building heights for scale
- Maintain stone texture consistency with city buildings
- Focus on atmospheric depth from valley perspective

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
