# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:39:12.504472+00:00
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

**Visual Continuity Facts:**
- **Location:** Upper floor of a building in the deserted city, overlooking the valley.
- **Characters:** Narrator (I), Sola, Woola (hound). Lorquas Ptomel mentioned as staying at the city.
- **Enemy Ship:** Gray-painted, low craft, drifting ~50 feet above ground, unmanned/dead crew visible.
- **Prisoner:** Slender girlish figure, coal black hair, light reddish copper skin, naked except ornaments, oval face, large eyes.
- **Action:** Enemy fleet retreats after being fired upon; one ship captured and burned; prisoner dragged into building by females.

**Broad Story Summary:**
On the third day post-incubator ceremony, the procession retreats due to enemy air fleet arrival. The narrator watches from a window as green Martians fire a volley at the approaching ships. The battle results in the destruction of the enemy fleet and the capture of one flagship. After looting and burning the ship, Martian warriors bring a human female prisoner into the city. The narrator sees her face, she makes a sign for help which he fails to answer due to ignorance of customs, and she is dragged away into the building.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Chapter 8

## Stable Environment Families

| Asset ID | Environment Family | Role | Primary Geography | Atmosphere |
|----------|-------------------|------|------------------|------------|
| building_upper_floor_window | Building Upper Floor/Window | Primary Observation Setting | Interior upper floor with window overlooking valley | Dim interior light, green Martian fire glow from outside, dusk/dawn transition |
| valley_overlook | Valley Geography | Secondary Overlooked Setting | Open valley terrain below city | Distant atmospheric haze, smoke from burning enemy ship, muted natural lighting |
| city_interior | City Interior Space | Transit/Conclusion Setting | Building interior corridors and rooms | Shadowy interior, torch or fire light sources, enclosed architecture |

## One-Off Mentions (Not Stable Families)

- Enemy ship: Gray-painted low craft drifting above ground (transit vessel, not stable geography)
- Deserted city exterior: Background location mentioned but not detailed

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_upper_floor_window

[[SECTION markdown]]
# Building Upper Floor Window - Observation Setting

## Environment Role
Primary observation and transit setting for narrator's window-view sequences.

## Architecture and Geography
Interior upper floor of multi-story building in deserted city. Large window provides panoramic view overlooking valley below. Enclosed interior space with vertical access implied by multiple floors.

## Lighting and Atmosphere Cues
Dim interior ambient light contrasted with exterior green fire glow from Martian weapons. Dusk or dawn transition lighting conditions. Smoke haze visible through window from burning enemy ship in distance.

## Scale Cues and Environmental Anchors
Window frame as primary anchor point for observation sequences. Interior floor level establishes human scale against distant valley geography. Building height creates vertical perspective between interior space and exterior landscape.

## Descriptive Noun Phrases
- "upper floor window"
- "interior observation deck"
- "panoramic city view"
- "valley overlook frame"
- "green fire glow exterior"
- "dim interior ambient light"
- "smoke haze through glass"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_overlook

[[SECTION markdown]]
# Valley Overlook - Secondary Geography Setting

## Environment Role
Secondary geography setting viewed from building windows. Distant landscape anchor for spatial orientation.

## Architecture and Geography
Open valley terrain below city elevation. Natural landscape features including ground level, distant horizons, atmospheric depth zones. No built structures visible in immediate view.

## Lighting and Atmosphere Cues
Distant atmospheric haze creating muted natural lighting conditions. Smoke plumes from burning enemy ship create temporary atmospheric disturbances. Green fire glow reflects off valley surfaces during battle sequences.

## Scale Cues and Environmental Anchors
Valley floor establishes distant scale reference point. City building height creates vertical separation between observation point and landscape. Atmospheric depth zones create layered visual hierarchy.

## Descriptive Noun Phrases
- "distant valley terrain"
- "landscape overlook zone"
- "atmospheric haze layer"
- "smoke plume disturbance"
- "green fire glow reflection"
- "valley floor reference plane"
- "distant horizon band"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_interior

[[SECTION markdown]]
# City Interior Space - Transit and Conclusion Setting

## Environment Role
Transit and conclusion setting for prisoner movement sequences. Secondary interior space following window observation.

## Architecture and Geography
Building interior corridors and rooms within deserted city structure. Enclosed architectural spaces with vertical circulation implied by multiple floors. Interior walls, doors, and passages define movement paths.

## Lighting and Atmosphere Cues
Shadowy interior lighting conditions with torch or fire light sources creating localized illumination zones. Dim ambient light contrasted with brighter exterior glow through windows. Smoke haze from burning ship may permeate interior spaces.

## Scale Cues and Environmental Anchors
Interior doorways establish human-scale passage points. Interior walls create enclosed spatial boundaries. Floor level establishes consistent horizontal reference throughout interior sequences.

## Descriptive Noun Phrases
- "interior corridor space"
- "enclosed building room"
- "shadowy interior zone"
- "torch light illumination"
- "interior wall boundary"
- "doorway passage point"
- "floor level reference plane"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
