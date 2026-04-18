# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:19:18.072093+00:00
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

# Chapter Summary: A Fair Captive from the Sky

## Story Arc
1.  **Retreat:** The procession returns to a deserted city immediately after an incubator ceremony due to sudden orders.
2.  **Airship Arrival:** Twenty gray-painted airships swing over the hills toward the city. They are met with a volley of fire from building windows.
3.  **Naval Engagement:** Green Martian warriors return fire with high accuracy, targeting crew points and upper works. Several ships limp away; one is disabled and drifting.
4.  **Recovery Operation:** Warriors board the disabled ship to loot arms, ammunition, jewels, and water. They burn the vessel from within before towing it away.
5.  **Discovery:** While returning to the plaza, the narrator spots a slender, girlish figure being dragged into a building by green Martian females.

## Visual Continuity Facts
- **Locations:**
    - Upper floor window (view of valley/hills).
    - Building roofs (observation point).
    - Plaza (crowded with Martians).
    - Building interior (portal/depths).
- **Characters & Appearance:**
    - **Narrator:** Observes from distance, descends to street.
    - **Sola:** Rushes up to narrator upon arrival at plaza.
    - **Woola:** Hound follows close at heel.
    - **Captive:** Slender, girlish figure. Skin: light reddish copper. Hair: coal black, loosely caught. Features: Oval face, large lustrous eyes, finely chiseled. Attire: Destitute of clothes except ornaments.
- **Actions:**
    - Warriors melt like mist into doorways.
    - Ships swing broadside and circle.
    - Bodies strewn about decks (crews dead/unmanned).
    - Grappling hooks used to haul ship to ground.
    - Missile thrown back onto vessel causing flame spurt.
- **Atmosphere:**
    - Initial: Peaceful advance of ships.
    - Middle: Deadly accuracy, fire, smoke.
    - End: Hope mixed with dejection; captive looks at narrator with hope then loathing.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test

## Extracted Environments

| Asset ID | Environment Name | Role |
|----------|------------------|------|
| upper_floor_window | Upper Floor Window View | Primary Observation Point |
| building_roofs | Building Roofs | Secondary Transit Setting |
| plaza | Martian Plaza | Primary Action Arena |
| building_interior | Building Interior Depths | Secondary Portal Setting |
| disabled_airship | Disabled Airship Hull | Recovery Operation Zone |

## Environment Categories

- **Observation Points:** upper_floor_window, building_roofs
- **Action Arenas:** plaza, disabled_airship
- **Portal Settings:** building_interior

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: upper_floor_window

[[SECTION markdown]]
# Upper Floor Window View

## Environment Role
Primary observation point for narrator's initial perspective.

## Architecture and Geography
Elevated window frame overlooking valley terrain and distant hills. Glass panes provide framed view of landscape beyond immediate city walls.

## Lighting and Atmosphere Cues
Natural daylight filtering through window glass. Soft shadows cast by interior architecture. Distant haze over valley floor suggesting Martian atmospheric conditions.

## Scale Cues and Environmental Anchors
Window frame establishes human scale against vast landscape. Interior room boundaries define intimate space contrasting with exterior openness.

## Descriptive Noun Phrases
- "framed valley view"
- "distant hill silhouette"
- "interior window frame"
- "Martian atmospheric haze"
- "elevated observation vantage"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_roofs

[[SECTION markdown]]
# Building Roofs

## Environment Role
Secondary transit setting for elevated movement and observation.

## Architecture and Geography
Flat rooftop surfaces atop city buildings. Multiple roof levels create tiered urban landscape. Open-air exposure to Martian sky.

## Lighting and Atmosphere Cues
Direct sunlight on exposed surfaces. Sharp shadows between adjacent structures. Dust particles visible in light beams suggesting atmospheric density.

## Scale Cues and Environmental Anchors
Roof edges establish building height references. Adjacent rooftops provide depth markers across cityscape.

## Descriptive Noun Phrases
- "flat rooftop surface"
- "tiered urban landscape"
- "exposed Martian sky"
- "adjacent roof levels"
- "cityscape depth markers"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza

[[SECTION markdown]]
# Martian Plaza

## Environment Role
Primary action arena for crowd gatherings and combat sequences.

## Architecture and Geography
Open paved public square surrounded by building facades. Crowded with green Martian figures. Central gathering space for procession activities.

## Lighting and Atmosphere Cues
Ambient daylight illuminating open plaza space. Smoke and fire effects from naval engagement create dynamic lighting conditions. Dust clouds from combat activity.

## Scale Cues and Environmental Anchors
Building perimeters define plaza boundaries. Crowd density provides human scale reference. Central plaza area serves as focal point for action sequences.

## Descriptive Noun Phrases
- "open paved square"
- "surrounding building facades"
- "green Martian crowd"
- "combat smoke effects"
- "central gathering space"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_interior

[[SECTION markdown]]
# Building Interior Depths

## Environment Role
Secondary portal setting for depth transitions and movement.

## Architecture and Geography
Interior corridors and rooms within city buildings. Doorways serve as transition points between interior and exterior spaces. Portal-like entrances leading to deeper levels.

## Lighting and Atmosphere Cues
Dimmer interior lighting compared to exterior. Shadows created by architectural elements. Smoke from burning airship may penetrate through doorways.

## Scale Cues and Environmental Anchors
Doorway frames establish passage scale. Interior walls define enclosed space boundaries. Depth markers visible through portal entrances.

## Descriptive Noun Phrases
- "interior corridor space"
- "doorway transition points"
- "enclosed architectural walls"
- "portal entrance depths"
- "dimmer interior lighting"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: disabled_airship

[[SECTION markdown]]
# Disabled Airship Hull

## Environment Role
Recovery operation zone for looting and destruction sequences.

## Architecture and Geography
Large metallic airship hull structure with open deck areas. Damaged vessel with bodies strewn across decks. Grappling hooks attached to hull exterior.

## Lighting and Atmosphere Cues
Fire and flame effects from burning interior. Smoke billowing from damaged sections. Daylight illuminating exterior hull surfaces.

## Scale Cues and Environmental Anchors
Hull dimensions establish massive scale compared to human figures. Deck areas provide flat ground reference. Grappling hooks mark attachment points.

## Descriptive Noun Phrases
- "metallic airship hull"
- "open deck areas"
- "damaged vessel structure"
- "grappled hull exterior"
- "burning interior effects"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
