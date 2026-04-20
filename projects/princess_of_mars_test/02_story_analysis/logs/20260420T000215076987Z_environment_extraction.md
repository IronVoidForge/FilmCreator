# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:02:15.076987+00:00
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

Chapter id: CH008

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

**Broad Story Summary:**
On the third day after the incubator ceremony, the narrator and Sola return home but are ordered back immediately upon seeing enemy airships approaching. The green Martians retreat into buildings. From a window, the narrator observes the arrival of twenty gray-painted enemy vessels. A volley is exchanged; the enemy fleet returns fire but is eventually driven off by accurate Martian aim. One ship crashes near the city and is looted. Warriors find a small prisoner inside, drag her to ground, and loot the vessel before setting it ablaze with a missile. The narrator descends to the street and enters the plaza. There, he sees the captured woman being dragged into a building. She turns and makes eye contact with the narrator, signaling for help, but is taken away.

**Visual Continuity Facts:**
- **Characters:** Narrator (human-like), Sola (Martian companion), Woola (hound), Green Martians (green warriors), Prisoner (slender, girlish, Earth-like features, coal black hair, light reddish copper skin).
- **Locations:** Incubator building (upper floor window), City plaza, Open valley, Building roofs.
- **Objects:** Gray-painted airships (long, low, banners, odd devices), Chariots, Mastodons, Grappling hooks, Spears, Casks of water, Solid foods/liquids, Missile (faint spurt of flame).
- **Actions:** Melting into mist (Martians), Swinging over crest (ships), Firing volley, Dragging prisoner, Setting fire, Releasing guy ropes.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test

## Extracted Environments

| Asset ID | Environment Name | Role | Description |
|----------|------------------|------|-------------|
| incubator_building | Incubator Building | Primary | Upper floor window setting where narrator and Sola reside |
| city_plaza | City Plaza | Secondary | Open public space where enemy ships crash and prisoners are dragged |
| enemy_airships | Enemy Airships | Secondary | Gray-painted vessels with banners and odd devices |
| crashed_ship_site | Crashed Ship Site | Secondary | Location near city where enemy vessel crashes and is looted |
| open_valley | Open Valley | Background | Broader geography visible from elevated positions |

## Environment Families

- **Incubator Building**: Primary residence setting with upper floor windows overlooking the city
- **City Plaza**: Transit and action setting in urban public space
- **Enemy Airships**: Secondary vessel settings with distinct gray paint and banner decorations
- **Crashed Ship Site**: Secondary crash location near city boundaries
- **Open Valley**: Background geography for atmospheric context

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: incubator_building

[[SECTION markdown]]
# Incubator Building

## Environment Role
Primary setting - residence and observation point for narrator and Sola

## Architecture & Geography
Multi-story structure with elevated upper floor windows providing city views. Interior spaces designed for habitation with access to exterior viewing platforms.

## Lighting & Atmosphere
Natural daylight filtering through large windows, creating soft illumination on interior surfaces. Atmospheric tension from approaching enemy airships visible through glass panes. Green Martian warriors present in adjacent areas.

## Scale & Anchors
Human-scale interior rooms contrasting with massive cityscape views beyond windows. Window frames serve as primary viewing anchors. Upper floor positioning provides elevated vantage point over lower city levels.

## Descriptive Noun Phrases
- Elevated upper floor window
- City-view observation room
- Glass-pane viewing platform
- Multi-story habitation structure
- Interior living quarters with exterior access

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_plaza

[[SECTION markdown]]
# City Plaza

## Environment Role
Secondary setting - public transit and action space where enemy ships crash and prisoners are moved

## Architecture & Geography
Open urban public square with paved ground surfaces. Building facades surrounding the plaza perimeter. Access points to adjacent structures for prisoner movement.

## Lighting & Atmosphere
Daylight illumination on open plaza surfaces. Smoke and debris from crashed airships creating atmospheric disturbance. Enemy fire and missile spurs adding dynamic lighting elements.

## Scale & Anchors
Human-scale ground level with towering building facades as vertical anchors. Crashed enemy vessels serve as massive temporary objects dominating the space. Building entrances provide transit points between plaza and interior spaces.

## Descriptive Noun Phrases
- Open urban public square
- Paved plaza ground surface
- Building-facade perimeter
- Crashed vessel debris field
- Transit access entrance points

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: enemy_airships

[[SECTION markdown]]
# Enemy Airships

## Environment Role
Secondary setting - hostile vessels with distinct gray paint and banner decorations

## Architecture & Geography
Long, low-profile airship hulls with odd devices mounted on exterior surfaces. Banner decorations attached to vessel sides. Grappling hooks and cables visible for docking or movement operations.

## Lighting & Atmosphere
Metallic gray surfaces reflecting ambient daylight. Faint spurt of flame from missile systems creating localized light sources. Smoke trails from firing volleys adding atmospheric elements.

## Scale & Anchors
Massive vessel scale dwarfing human figures. Banner decorations serve as visual identification anchors. Odd devices and mounted equipment provide functional anchors on hull surfaces.

## Descriptive Noun Phrases
- Gray-painted airship hull
- Long low-profile vessel structure
- Banner-decoration side panels
- Mounted odd device fixtures
- Grappling hook attachment points

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: crashed_ship_site

[[SECTION markdown]]
# Crashed Ship Site

## Environment Role
Secondary setting - crash location near city boundaries where enemy vessel is looted and set ablaze

## Architecture & Geography
Ground-level crash site adjacent to city perimeter. Debris field from exploded airship hull components. Building structures nearby providing access points for warriors and prisoners.

## Lighting & Atmosphere
Daylight on debris-strewn ground with smoke rising from burning wreckage. Missile flame spurs creating dynamic lighting effects. Fire from setting ablaze operations adding intense light sources.

## Scale & Anchors
Crushed vessel fragments serving as massive temporary anchors. Debris field boundaries defining crash perimeter. Nearby building structures providing vertical scale references and access points.

## Descriptive Noun Phrases
- Ground-level crash debris field
- Exploded hull fragment scatter
- Burning wreckage fire zone
- Missile flame light sources
- Adjacent city perimeter structures

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: open_valley

[[SECTION markdown]]
# Open Valley

## Environment Role
Background setting - broader geography visible from elevated positions providing atmospheric context

## Architecture & Geography
Wide open valley terrain with natural landscape features. Distant horizon lines visible from elevated viewing points. Building rooftops and structures scattered across valley floor.

## Lighting & Atmosphere
Natural daylight illuminating expansive valley surfaces. Atmospheric haze or mist creating depth perception. Smoke from city activities drifting across valley adding atmospheric movement.

## Scale & Anchors
Vast landscape scale contrasting with human-scale buildings. Distant horizon lines serving as primary anchors. Rooftop structures providing vertical reference points within valley expanse.

## Descriptive Noun Phrases
- Wide open valley terrain
- Natural landscape features
- Distant horizon line views
- Scattered rooftop structures
- Atmospheric haze depth zones

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
