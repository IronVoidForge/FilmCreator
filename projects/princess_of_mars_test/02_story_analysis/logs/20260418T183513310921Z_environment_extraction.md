# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:35:13.310921+00:00
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

**Story Summary:**
John Carter observes from a window as a fleet of twenty gray airships approaches the deserted city. Green Martians fire a volley from buildings, initiating a battle where the airships return fire with ineffectual results due to suddenness and damage. The fleet retreats after sustaining heavy casualties; one ship drifts helplessly and is boarded by warriors who loot arms, jewels, and water. The crew empties carboys over dead sailors and burns the vessel before it drifts away. Carter feels a strange yearning for the "kindred people" defeated. He sees a human woman prisoner being dragged into a building; she looks at him with hope then dejection as he fails to signal help due to cultural ignorance.

**Visual Continuity:**
- **Locations:** Window of upper floor (Carter's vantage point), Rooftops, Plaza/Street level, Building interiors.
- **Characters Visible:** John Carter, Sola, Woola, Green Martian Warriors, Airship Crews (distant figures), Human Woman Prisoner.
- **Props/Vehicles:** Gray airships (20+), Chariots, Mastodons, Grappling hooks, Carboys, Stone vessels, Banners/Devices on ships.
- **Lighting/Atmosphere:** Daylight, sunlight reflecting off ship devices, smoke and flame from burning vessel.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test

| Asset ID | Environment Name | Role | Primary Features |
|----------|------------------|------|------------------|
| window_upper_floor | Carter's Vantage Window | Primary | Upper floor observation point, daylight view |
| rooftops | City Rooftop Network | Secondary/Transit | Elevated positions, smoke and flame visible |
| plaza_street_level | Plaza and Street Level | Primary/Transit | Ground level action zone, building facades |
| building_interiors | Building Interior Spaces | Secondary | Enclosed spaces, prisoner movement areas |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: window_upper_floor

[[SECTION markdown]]
# Window Upper Floor - Carter's Vantage Point

## Environment Role
Primary observation setting for John Carter's perspective during the fleet approach and battle sequence.

## Architecture and Geography
Upper floor residential or military structure with large window opening facing city plaza. Elevated position provides clear sightlines to approaching airships and rooftop activity.

## Lighting and Atmosphere Cues
Natural daylight streaming through window, sunlight reflecting off distant ship devices visible from interior. Smoke haze from burning vessel may drift into view. Interior shadows contrast with bright exterior light.

## Scale and Environmental Anchors
Human-scale interior space with large window as primary anchor point. Window frame defines composition boundaries. Distant cityscape provides depth reference. Airships appear at varying distances through glass.

## Descriptive Noun Phrases for Render Prompts
- Large observation window
- Upper floor interior
- Daylight streaming through glass
- City plaza view from above
- Distant airship silhouette
- Smoke haze in distance
- Window frame composition
- Interior shadows and exterior light contrast

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: rooftops

[[SECTION markdown]]
# Rooftops - City Rooftop Network

## Environment Role
Secondary setting for elevated positions, transit zone between plaza and building interiors, vantage points for Green Martian Warriors.

## Architecture and Geography
Network of connected rooftop surfaces across city buildings. Elevated platforms with parapets and access points. Open-air spaces with multiple levels visible from different angles.

## Lighting and Atmosphere Cues
Daylight with sunlight reflecting off ship devices mounted on rooftops. Smoke and flame from burning vessel drift upward through air. Green Martian fire volleys create bright flashes against daylight sky.

## Scale and Environmental Anchors
City-scale elevated network with multiple building heights visible. Rooftop edges define horizontal boundaries. Parapets and access points serve as compositional anchors. Distant plaza appears below at reduced scale.

## Descriptive Noun Phrases for Render Prompts
- Connected rooftop surfaces
- Elevated city platforms
- Ship device reflections
- Smoke drift upward
- Green Martian fire volleys
- Rooftop parapets
- Multiple building heights
- Open-air elevated spaces

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_street_level

[[SECTION markdown]]
# Plaza Street Level - Ground Action Zone

## Environment Role
Primary transit and action setting for fleet approach, battle sequence, and prisoner movement. Central ground-level zone connecting all other environments.

## Architecture and Geography
Open plaza space surrounded by building facades at street level. Wide paved surfaces with multiple entry points to buildings. Ground-level view of approaching airships from distance.

## Lighting and Atmosphere Cues
Full daylight with sunlight reflecting off ship devices visible from ground. Smoke and flame from burning vessel create dramatic atmospheric effects. Green Martian fire volleys illuminate plaza space.

## Scale and Environmental Anchors
City-scale open plaza with building facades as vertical anchors. Airships appear at varying distances across sky. Building entrances serve as compositional entry points. Ground level provides human-scale reference for action sequences.

## Descriptive Noun Phrases for Render Prompts
- Open plaza space
- Building facade surrounds
- Paved ground surfaces
- Multiple building entrances
- Approaching airship silhouettes
- Smoke and flame effects
- Daylight atmospheric haze
- Ground-level action zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_interiors

[[SECTION markdown]]
# Building Interiors - Enclosed Spaces

## Environment Role
Secondary setting for prisoner movement and interior observation points. Enclosed spaces contrasting with exterior daylight environments.

## Architecture and Geography
Enclosed interior spaces within city buildings. Multiple rooms or corridors connecting different areas. Interior walls, doors, and structural elements define space boundaries.

## Lighting and Atmosphere Cues
Interior lighting may be dimmer than exterior daylight. Natural light enters through windows or doorways creating contrast zones. Smoke from burning vessel may drift into interior spaces.

## Scale and Environmental Anchors
Human-scale enclosed spaces with architectural features as anchors. Doorways and windows serve as compositional entry points to exterior views. Interior walls define spatial boundaries.

## Descriptive Noun Phrases for Render Prompts
- Enclosed interior spaces
- Interior wall surfaces
- Doorway openings
- Window light contrast
- Dimmer interior lighting
- Smoke drift into interiors
- Human-scale enclosed rooms
- Structural boundary elements

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
