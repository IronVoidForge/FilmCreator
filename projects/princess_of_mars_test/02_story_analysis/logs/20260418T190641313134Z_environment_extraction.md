# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:06:41.313134+00:00
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

# Chapter Label
Chapter VIII - A Fair Captive from the Sky

# Visual Continuity Facts
- **Airships:** Long, low, gray-painted vessels with banners and glowing devices on prows.
- **Warriors:** Green Martians (erect posture), wearing green attire, using spears and grappling hooks.
- **Prisoner:** Slender, girlish figure; light reddish copper skin; coal black hair; naked except for ornaments.
- **Environment:** Deserted city buildings with windows/roofs; valley floor; hills beyond.
- **Fire Effects:** Spurts of flame on ship banners; roaring flames on vessel decks; drifting funeral pyre.

# Broad Story Summary
The narrator and procession return to the deserted city after an incubation ceremony but are ordered back immediately upon seeing a fleet of twenty gray airships approaching. The green Martians fire from buildings, engaging the ships in a deadly exchange where the Martians demonstrate high accuracy against the ships' crews and equipment. The fleet retreats with damage; one unmanned ship drifts helplessly toward the city. Warriors capture this vessel, loot it for arms, jewels, and water, then burn it before towing it away. As the narrator watches from a window, he sees a prisoner being dragged into a building by green Martian females. The prisoner turns to look at the narrator, signaling hope which fades into dejection as she is taken into the depths of the edifice.

# Key Scene Decomposition Points
- **Arrival:** Procession returns; order given for retreat upon sighting ships.
- **Engagement:** Martians fire volley; ships return fire; specific targeting of crew/apparatus.
- **Retreat:** Fleet limps away; one ship unmanned and drifting.
- **Recovery:** Warriors swarm the drifting ship; loot operation (hours); burning of vessel.
- **Discovery:** Narrator sees prisoner dragged in; visual contact between narrator and prisoner.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test

## Extracted Environment Families

| Asset ID | Role | Description |
|----------|------|-------------|
| city_buildings | primary | Deserted urban structures with windows and roofs where Martians fire from |
| valley_floor | transit | Open ground between city buildings and distant hills |
| hills_background | secondary | Elevated geography beyond the valley floor |
| airship_fleet | secondary | Gray vessels with banners approaching and retreating from city |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_buildings

[[SECTION markdown]]
# City Buildings Environment

## Role
Primary setting for chapter action and Martians' defensive positions

## Architecture & Geography
Deserted urban structures with intact windows and roof surfaces. Multi-story buildings forming a canyon-like streetscape. Flat rooftops visible from valley floor perspective.

## Lighting & Atmosphere
Dim natural light filtering through building gaps. Smoke haze from burning vessels drifting across structure facades. Gray-painted vessel banners create dark vertical accents against lighter building walls.

## Scale & Anchors
Large enough to accommodate airship fleet above and Martians firing from upper windows. Building heights exceed valley floor visibility range. Windows serve as recurring firing positions. Rooftops function as observation points for narrator in window.

## Descriptive Noun Phrases
- deserted city buildings with windows and roofs
- gray-painted vessel banners on building facades
- multi-story urban structures forming canyon streetscape
- intact window openings for defensive fire
- flat rooftops visible from valley perspective
- smoke haze drifting across structure surfaces
- narrator's observation window in building wall

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_floor

[[SECTION markdown]]
# Valley Floor Environment

## Role
Transit setting between city and distant hills; primary viewing area for narrator

## Architecture & Geography
Open flat ground surface at base of city buildings. Unobstructed line of sight to hills beyond. Ground level serves as approach path for airship fleet.

## Lighting & Atmosphere
Brighter natural illumination compared to building interiors. Smoke from burning vessels creates temporary atmospheric haze. Gray vessel debris drifts across open surface before being towed away.

## Scale & Anchors
Large enough to accommodate full airship fleet landing and maneuvering. Sufficient space for Martians to swarm drifting vessel. Ground level provides narrator's window view perspective. Valley floor serves as central stage for fleet engagement.

## Descriptive Noun Phrases
- open flat ground at base of city buildings
- unobstructed line of sight to distant hills
- approach path for airship fleet movement
- ground level viewing area from building windows
- space for Martians to swarm drifting vessel
- central stage for fleet engagement and retreat
- smoke haze drifting across open surface

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills_background

[[SECTION markdown]]
# Hills Background Environment

## Role
Secondary geography providing depth and scale reference for valley scene

## Architecture & Geography
Elevated landforms beyond valley floor. Distant ridgelines visible through atmospheric haze. Serves as horizon boundary for city buildings and valley space.

## Lighting & Atmosphere
Dimmer natural light due to distance and atmospheric perspective. Appears as dark silhouette against sky. Smoke from burning vessels may partially obscure distant hill contours.

## Scale & Anchors
Provides depth reference for valley floor scale. Distant enough to remain atmospheric rather than detailed. Serves as visual boundary for city buildings and valley space. Hills beyond establish geographic context for deserted city location.

## Descriptive Noun Phrases
- elevated landforms beyond valley floor
- distant ridgelines visible through haze
- horizon boundary for city buildings
- dark silhouette against sky
- atmospheric depth reference for valley scene
- geographic context for deserted city location
- distant hills establishing valley boundaries

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: airship_fleet

[[SECTION markdown]]
# Airship Fleet Environment

## Role
Secondary mobile environment; primary antagonist presence in chapter

## Architecture & Geography
Long, low gray-painted vessels with banners and glowing devices on prows. Twenty ships forming fleet formation. Vessels approach from distance then retreat damaged. One unmanned ship drifts helplessly toward city.

## Lighting & Atmosphere
Gray hulls create dark vertical elements against sky. Banners show spurs of flame creating bright accents. Roaring flames on vessel decks produce intense light sources. Drifting funeral pyre adds atmospheric smoke.

## Scale & Anchors
Large enough to dominate valley floor and building skyline. Fleet formation spans entire visible horizon. Individual vessels exceed building height when viewed from ground level. Glowing devices on prows serve as recurring visual anchors.

## Descriptive Noun Phrases
- long low gray-painted vessels with banners
- glowing devices on vessel prows
- fleet of twenty ships approaching and retreating
- spurs of flame on ship banners
- roaring flames on vessel decks
- drifting unmanned funeral pyre
- dark vertical elements against sky

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
