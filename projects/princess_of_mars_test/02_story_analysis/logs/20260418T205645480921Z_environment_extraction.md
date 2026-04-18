# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:56:45.480921+00:00
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

# Chapter Title
Chapter VIII - A Fair Captive from the Sky

# Scene 1: Retreat & Investigation
- **Event:** Martians retreat immediately after incubation ceremony procession debouches into open ground.
- **Action:** Narrator investigates cause of sudden retreat from upper floor window.
- **Visual:** Twenty gray air ships swing slowly over hill crests, each carrying strange banners and odd devices on prows.

# Scene 2: Battle
- **Event:** Green warriors fire a terrific volley from building windows facing the valley.
- **Action:** Air fleet returns fire with guns; ships move parallel to firing line then turn back.
- **Visual:** Banners dissolve in spurts of flame; green figures drop at bullet explosions; fire from vessels is ineffectual due to suddenness of first volley.
- **Outcome:** Fleet limps away; one ship receives brunt of fire, appears unmanned and helpless.

# Scene 3: Disabled Ship & Loot
- **Event:** Warriors chase disabled ship; board with spears and grappling hooks.
- **Action:** Ship hauled to ground; systematic rifling of vessel.
- **Visual:** Loot includes arms, ammunition, silks, furs, jewels, stone vessels, food/water.
- **Outcome:** Ship towed out, emptied, set on fire by missile from last warrior. Drifts away as floating funeral pyre.

# Scene 4: Return & Prisoner
- **Event:** Warriors return to plaza; danger of air craft passed for a week.
- **Action:** Narrator sees prisoner dragged into building by green Martian females.
- **Visual:** Slender girlish figure, Earthly woman appearance, oval face, coal black hair, light reddish copper skin, naked except ornaments.
- **Interaction:** She looks at narrator, makes sign (appeal for help), then is dragged away. Narrator feels hope and dejection.

# Emotional Beats
- **Depression:** Narrator feels defeat of kindred people rather than routing of horde.
- **Hope:** Mixed surge of hope, fear, exultation, and depression upon seeing prisoner.
- **Regret:** Realizes he did not answer her signal for succor due to ignorance of Martian customs.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter VIII

## Primary Environments
- **open_ground_hill** - Main retreat location with air ships visible over hill crests
- **valley_battlefield** - Central battle zone where green warriors fire from building windows

## Secondary Environments  
- **building_windows_upper_floor** - Narrator's observation point for investigation
- **plaza_return** - Gathering space after danger passes, prisoner brought here
- **disabled_martian_ship** - Looting target, towed to ground and set ablaze

## Transit/Functional Environments
- All environments serve as staging grounds for Martian fleet movements and warrior operations

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: open_ground_hill

[[SECTION markdown]]
**Role:** Primary setting / Retreat location

**Architecture/Geography:** Open ground with hill crests forming natural elevation markers. Gray air ships swing slowly over hill ridges, banners and odd devices visible on prows.

**Lighting/Atmosphere:** Daylight conditions with slow-moving aerial vessels creating atmospheric tension. Smoke from burning banners adds visual texture during battle sequences.

**Scale:** Large-scale environment accommodating twenty air ships in formation. Hill crests provide reference points for fleet positioning and movement patterns.

**Anchors:** Hill crests, air ship prows, banner displays, ground-level observation points.

**Descriptive Phrases:** Gray air ships over hill crests, strange banners on prows, open ground retreat zone, aerial vessel formation, hill ridge elevation markers.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_windows_upper_floor

[[SECTION markdown]]
**Role:** Secondary setting / Observation point

**Architecture/Geography:** Multi-story building with upper floor windows facing valley and open ground. Green warriors fire from building windows facing the valley during battle sequences.

**Lighting/Atmosphere:** Interior daylight with exterior battle smoke visible through windows. Bullet explosions create intermittent light flashes from outside.

**Scale:** Medium-scale interior space with window frames providing viewing corridors to exterior environment. Building height creates vertical separation between narrator and action below.

**Anchors:** Window frames, upper floor observation deck, building facade facing valley, interior walls separating from exterior view.

**Descriptive Phrases:** Upper floor windows facing valley, green warriors firing positions, interior observation point, window frame viewing corridors, building facade battle line.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_battlefield

[[SECTION markdown]]
**Role:** Primary setting / Battle zone

**Architecture/Geography:** Wide valley with building windows facing the valley serving as firing positions. Air fleet moves parallel to firing line then turns back during engagement sequences.

**Lighting/Atmosphere:** Daylight battle conditions with banners dissolving in spurts of flame. Fire from vessels appears ineffectual against sudden first volley explosions.

**Scale:** Large-scale open terrain accommodating air fleet movements and building-to-valley sightlines. Parallel ship formations create horizontal movement patterns across valley floor.

**Anchors:** Building windows facing valley, air fleet formation lines, firing line positions, valley floor movement paths, banner display locations.

**Descriptive Phrases:** Valley battle zone, building windows firing positions, air fleet parallel movements, banner flame dissolution, green warrior firing line, valley floor engagement area.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_return

[[SECTION markdown]]
**Role:** Secondary setting / Gathering space

**Architecture/Geography:** Plaza where warriors return after danger of air craft passed for a week. Building interior spaces visible as prisoner dragged into building by green Martian females.

**Lighting/Atmosphere:** Interior daylight with relief atmosphere after battle danger passes. Mixed emotions create atmospheric tension despite physical safety.

**Scale:** Medium-scale plaza space accommodating warrior gatherings and prisoner transport. Building interiors provide vertical depth for observation from upper floors.

**Anchors:** Plaza gathering areas, building entrance points, interior observation spaces, prisoner transport paths, warrior assembly zones.

**Descriptive Phrases:** Plaza return zone, danger passed atmosphere, green Martian female figures, building interior spaces, prisoner drag path, warrior assembly area.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: disabled_martian_ship

[[SECTION markdown]]
**Role:** Secondary setting / Looting target

**Architecture/Geography:** Martian air vessel hauled to ground with systematic rifling. Stone vessels, arms, ammunition, silks, furs, jewels visible during looting sequences.

**Lighting/Atmosphere:** Daylight conditions with fire from last warrior creating funeral pyre atmosphere. Ship appears unmanned and helpless after receiving brunt of fire.

**Scale:** Medium-scale vessel interior with systematic emptying process. Stone vessels and equipment provide reference points for rifling operations.

**Anchors:** Vessel hull, stone vessels, arms storage, ammunition compartments, silk/fur storage areas, jewel containers, food/water supplies.

**Descriptive Phrases:** Disabled Martian ship, ground-hauled vessel, systematic rifling zone, stone vessel storage, arms and ammunition compartments, funeral pyre atmosphere, unmanned helpless craft.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
