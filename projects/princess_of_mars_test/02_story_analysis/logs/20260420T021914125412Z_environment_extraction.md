# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:19:14.125412+00:00
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

# Chapter Summary: A Fair Captive From The Sky

## Story Arc

### 1. The Retreat Order & Enemy Arrival
On the third day after the incubator ceremony, the procession is ordered to return home but immediately recalled due to the arrival of enemy airships. Twenty gray-painted vessels swing over the hills toward the city. The green Martians, trained for this evolution, melt into nearby buildings within three minutes.

### 2. The Naval Battle
The narrator climbs to an upper floor window to observe. A volley is fired from building windows by the Martians, causing the enemy fleet to return fire. Both sides display deadly accuracy; bullets drop at explosions and banners dissolve in flames. The enemy ships circle and turn back, intending to complete a great circle opposite the firing line.

### 3. The Disabled Ship & Recovery
Twenty minutes after the first volley, the fleet retreats, damaged and limping. One ship is entirely unmanned and helpless. Warriors rush to the roofs to cover the possibility of reinforcements or return fire. They chase the disabled craft, which drifts fifty feet above ground toward a building south of their position. Warriors board the vessel with spears and grappling hooks, hauling it to ground.

### 4. Looting and Burning
The warriors systematically rifle the vessel for several hours, requisitioning chariots to transport loot: arms, ammunition, silks, furs, jewels, stone vessels, and food/water (including casks of water). After removing the last load, they tow the craft out into the valley. They empty carboys over the dead sailors and decks. A final missile is thrown onto the vessel, igniting it. The ship soars majestically into the air as a floating funeral pyre, drifting southeast until lost in the distance.

### 5. The Prisoner's Appearance
Depressed by the defeat of a kindred people, the narrator descends to the street. Sola rushes up as the cavalcade returns to the plaza. Lorquas Ptomel remains at the deserted city due to fear of airship attack for over a week. As they enter the plaza, the narrator sees a prisoner being dragged into a nearby building by green Martian females. The creature is described as a slender, girlish figure similar to Earth women: oval face, coal black hair, light reddish copper skin, naked except for ornaments. She makes a sign (appeal for succor) with her free hand. Her eyes meet the narrator's; hope fades into dejection and contempt before she is dragged away.

## Visual Continuity Facts

### Character States & Locations
- **Narrator:** Positioned on upper floor window during battle, then descends to street/plaza. Accompanied by Woola (hound).
- **Sola:** Rushes up to narrator upon return to plaza; actively involved in procession defense.
- **Lorquas Ptomel:** Remains at deserted city with caravan/children due to safety concerns.
- **Green Martians:** Melt into building doorways during enemy arrival; swarm from windows during battle; board disabled ship from windows; rush onto plain to meet retreating fleet.
- **Enemy Fleet:** Gray-painted, long and low vessels. Initially twenty ships; one disabled at end of chapter.

### Environmental & Object Details
- **City:** Described as "open ground" with spacious doorways. Buildings have upper floors with windows facing the valley/hills.
- **Airships:** Long, low, gray-painted. Carried strange banners and odd devices on prow. Swung from stem to stern above upper works.
- **Battlefield:** Valley across which ships advance. Ground is open plain where warriors rush out to meet disabled ship.
- **Loot Items:** Arms, ammunition, silks, furs, jewels, strangely carved stone vessels, solid foods/liquids, casks of water.
- **Disabled Ship:** Drifting fifty feet above ground; bodies of crew strewn about; eventually set on fire and towed away.

### Temporal Markers
- **Incubator Ceremony:** Third day after this event marks the start of the chapter's action.
- **Battle Duration:** Lasts approximately twenty minutes from first volley to fleet retreat.
- **Looting Duration:** Requires several hours.
- **Post-Battle Stay:** Caravan remains at city for more than a week due to fear of return attack.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH008

## Primary Settings

### City (Primary)
- Role: Main setting for narrator's observation and descent
- Geography: Open ground with spacious doorways, upper floors with windows facing valley/hills
- Lighting: Natural daylight during battle observation
- Atmosphere: Tense military engagement, then post-battle recovery
- Scale: Multi-story buildings overlooking open plain
- Anchors: Upper floor windows, plaza entrance, building doorways

### Valley/Battlefield (Secondary)
- Role: Transit setting for enemy fleet advance and disabled ship drift
- Geography: Open plain across which ships advance, fifty feet above ground
- Lighting: Natural daylight with smoke from burning vessel
- Atmosphere: Military combat, then funeral pyre procession
- Scale: Large open space accommodating airship movement
- Anchors: Firing line, disabled ship position, valley edge

## Secondary Settings

### Building South of Position (Secondary)
- Role: Landing point for disabled vessel
- Geography: Multi-story structure with accessible entry points
- Lighting: Natural daylight with fire glow from burning ship
- Atmosphere: Post-combat recovery, looting operations
- Scale: Ground floor accessible to boarding warriors
- Anchors: Entry doorways, upper windows, ground level

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city

[[SECTION markdown]]
# City - Primary Setting

## Environment Role
Primary setting for narrator's observation and descent during battle sequence.

## Architecture & Geography
Open ground with spacious doorways throughout the urban area. Multi-story buildings feature upper floors with windows facing the valley and hills. Buildings positioned along open plain edges provide observation points. Doorways accommodate movement between interior spaces and exterior battlefield zones.

## Lighting & Atmosphere
Natural daylight conditions during military engagement. Smoke from burning vessel creates atmospheric haze in post-combat sequences. Military tension permeates the environment during enemy fleet arrival. Post-battle atmosphere shifts to recovery operations with looting activities.

## Scale & Anchors
Large-scale urban environment accommodating airship movement overhead. Upper floor windows serve as primary observation anchors. Plaza entrance marks transition from battlefield to civilian zones. Building doorways provide access points for warriors and civilians. Ground level accommodates disabled vessel landing.

## Descriptive Noun Phrases
- Spacious doorway entrances
- Multi-story building facades
- Upper floor observation windows
- Open ground plaza areas
- Valley-facing window positions
- Hill-viewing elevated floors
- Urban recovery zones
- Battle observation platforms

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_battlefield

[[SECTION markdown]]
# Valley/Battlefield - Secondary Setting

## Environment Role
Secondary transit setting for enemy fleet advance and disabled ship drift operations.

## Architecture & Geography
Open plain across which enemy airships advance toward city position. Ground surface fifty feet above building level during vessel drift. Large-scale open space accommodating long, low gray-painted vessels with strange banners on prow. Firing line established along valley edge. Disabled ship drifts southeast through open terrain.

## Lighting & Atmosphere
Natural daylight conditions during combat engagement. Smoke from burning funeral pyre creates atmospheric haze in post-combat sequences. Military combat atmosphere during volley exchanges. Funeral procession atmosphere when vessel burns as floating pyre drifting into distance.

## Scale & Anchors
Large-scale open space accommodating airship movement and boarding operations. Firing line serves as primary combat anchor. Disabled ship position marks recovery operation center. Valley edge provides observation boundary. Ground level accommodates warrior rush-out operations.

## Descriptive Noun Phrases
- Open plain battlefield surface
- Fifty-foot vessel drift altitude
- Gray-painted airship vessels
- Strange banner displays
- Firing line combat zones
- Disabled ship landing areas
- Southeast drifting trajectory
- Funeral pyre burning zones

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_south_position

[[SECTION markdown]]
# Building South of Position - Secondary Setting

## Environment Role
Secondary setting serving as landing point for disabled vessel and looting operations.

## Architecture & Geography
Multi-story structure with accessible entry points at ground level. Building positioned south of main combat position. Ground floor accommodates warrior boarding operations with spears and grappling hooks. Upper windows provide observation and potential reinforcement access. Structure receives disabled craft drifting fifty feet above ground before landing.

## Lighting & Atmosphere
Natural daylight conditions during recovery operations. Fire glow from burning ship illuminates building exterior in post-combat sequences. Military combat atmosphere during initial boarding. Post-combat looting atmosphere during several hours of systematic rifle operations.

## Scale & Anchors
Ground floor serves as primary boarding anchor. Entry doorways accommodate warrior movement and loot transport. Upper windows provide observation points for reinforcements. Building scale accommodates chariot requisition for loot transport. Ground level facilitates vessel towing operations into valley.

## Descriptive Noun Phrases
- Multi-story structure facades
- Ground floor entry doorways
- Upper window observation points
- South position building placement
- Vessel landing zones
- Chariot transport areas
- Loot requisition spaces
- Warrior boarding platforms

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
