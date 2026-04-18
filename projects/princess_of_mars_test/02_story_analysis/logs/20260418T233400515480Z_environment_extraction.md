# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:34:00.515480+00:00
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

**Story Summary**
The procession retreats to the city after an incubator ceremony. A fleet of twenty gray airships arrives from the hills, bearing strange banners. Green Martians fire a volley from building windows; ships return fire but suffer heavy damage due to suddenness and targeting tactics (wireless, officers). One ship is disabled and drifting southeast. Warriors rush to capture it, loot arms, food, water, and jewels, then burn the vessel before towing it away. The crew is dead or incapacitated. Carter observes from a window/balcony. Upon returning to the plaza, Carter sees the prisoner being dragged into a building by green Martian females.

**Visual Continuity**
*   **Ships:** Long, low, gray-painted vessels. Twenty in total initially. One disabled drifting southeast.
*   **Warriors:** Green Martians. Wear spears. Some climb windows to fire. Others swarm the disabled ship from sides/windows using grappling hooks.
*   **Prisoner:** Slender, girlish figure. Naked except for highly wrought ornaments. Skin is light reddish copper color. Cheeks have crimson glow. Lips are ruby. Hair is coal black, waving, caught loosely into a strange coiffure. Eyes large and lustrous. Oval face.
*   **Environment:** Deserted city buildings with upper floors and rooftops. Valley floor. Hills beyond. Open ground/plaza.
*   **Action Details:** Banners swing from stem to stern. Devices gleam in sunlight. Fire spurs from banners/upper works upon impact. Loot includes casks of water, silks, furs, stone vessels. Burning ship drifts unguided into the distance.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH008

- **disabled_airship**: Secondary action hub, drifting vessel with burning aftermath and loot anchors.
- **city_buildings**: Primary observation setting, multi-story structures with upper floors and rooftops used for firing.
- **open_plaza**: Secondary transit space, open ground level where prisoner is moved into building entrance.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: disabled_airship

[[SECTION markdown]]
**Environment Role:** Secondary / Action Hub (Transit Setting)

**Architecture or Geography:** Long, low, gray-painted vessel drifting unguided into the distance. Vessel structure includes upper works and stem-to-stern configuration.

**Lighting and Atmosphere Cues:** Sunlight gleaming on devices. Fire spurs from banners/upper works upon impact. Burning ship drifts southeast. Smoke and heat implied by burning state.

**Scale Cues and Recurring Environmental Anchors:** Large vessel compared to warriors. Banners swinging from stem to stern. Loot includes casks of water, silks, furs, stone vessels. Burning drift serves as a dynamic anchor.

**Descriptive Noun Phrases for Render-Facing Prompts:** Gray-painted airship hull, burning vessel drifting southeast, swinging banners on disabled ship, loot casks and stone vessels on deck, fire spurring from upper works.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_buildings

[[SECTION markdown]]
**Environment Role:** Primary / Observation Point (Transit Setting)

**Architecture or Geography:** Deserted city buildings with upper floors and rooftops. Valley floor context visible beyond structures. Hills beyond the city horizon.

**Lighting and Atmosphere Cues:** Sunlight illuminating building facades. Green Martians firing from windows. Devices gleam in sunlight. Open daylight conditions.

**Scale Cues and Recurring Environmental Anchors:** Multi-story structures providing elevation for warriors. Windows used as firing positions. Rooftops accessible for climbing. Building entrance where prisoner is dragged.

**Descriptive Noun Phrases for Render-Facing Prompts:** Deserted city buildings with upper floors, windows used for firing, rooftops with grappling hooks, valley floor beyond structures, hills in background horizon.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: open_plaza

[[SECTION markdown]]
**Environment Role:** Secondary / Retreat Destination (Transit Setting)

**Architecture or Geography:** Open ground/plaza at valley floor level. Ground space in front of city buildings. Entrance to building where prisoner is dragged.

**Lighting and Atmosphere Cues:** Open daylight conditions. Clear visibility for Carter's observation from window/balcony. No specific weather effects noted, standard ambient lighting.

**Scale Cues and Recurring Environmental Anchors:** Ground level space allowing dragging action. Building entrance serves as transition point to interior. Open space allows fleet arrival context.

**Descriptive Noun Phrases for Render-Facing Prompts:** Open ground plaza at valley floor, building entrance with prisoner being dragged, open daylight on plaza surface, transition space between fleet and city interior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
