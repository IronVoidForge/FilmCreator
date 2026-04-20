# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:58:30.665680+00:00
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

# Chapter Summary: CH008 - A Fair Captive From The Sky

## Scene 1: Return & Enemy Fleet Arrival
- **Action:** Narrator and Sola return to the deserted city after the incubation ceremony. Martians retreat immediately upon sighting enemy airships.
- **Visual Continuity:**
    - **Martian Warriors:** Green, melting into doorways like mist.
    - **Enemy Vessels:** Huge craft, long, low, gray-painted, swinging over hill crests.
    - **Quantity:** Twenty vessels advancing majestically toward the city.
- **Outcome:** Immediate hasty return ordered; Martians fire volley from windows as ships approach.

## Scene 2: Battle Observation & Naval Engagement
- **Action:** Narrator climbs to an upper floor window to observe the cause of retreat. A naval battle ensues between city defenders and enemy fleet.
- **Visual Continuity:**
    - **Enemy Ships:** Each carries a strange banner; odd devices gleam on prows. Figures crowd forward decks.
    - **Fire Exchange:** Martians fire from building windows; enemy ships return fire with guns.
    - **Accuracy:** Narrator notes deadly accuracy of Martians (little figure drops at each explosion); enemy fire ineffectual due to suddenness.
    - **Damage:** Foremost vessel swings broadside, others follow in wake. Several craft limping perceptibly.
- **Outcome:** Enemy fleet retreats trailing off; one ship disabled and drifting.

## Scene 3: Capture of Disabled Vessel & Looting
- **Action:** Warriors capture the unmanned drifting ship. Systematic rifling of vessel occurs over several hours.
- **Visual Continuity:**
    - **Ship Status:** Drifting fifty feet above ground, bodies of crew strewn about, no sign of life.
    - **Capture Method:** Warriors swarm from windows with great spears; grappling hooks used to haul boat to ground.
    - **Loot Contents:** Arms, ammunition, silks, furs, jewels, strangely carved stone vessels, solid foods/liquids, casks of water.
    - **Disposal:** Warriors empty carboys over dead sailors/decks; ship set on fire with missile.
- **Outcome:** Ship burns as floating funeral pyre, drifting southeast until lost in distance.

## Scene 4: Narrator's Depression & Prisoner Discovery
- **Action:** Narrator descends to street feeling depressed about the defeat of a kindred people. Lorquas Ptomel keeps caravan safe in city due to fear of attack.
- **Visual Continuity:**
    - **Atmosphere:** Awe-inspiring sight of floating funeral pyre; narrator feels strange yearning toward unknown foemen.
    - **Prisoner Entry:** Human woman dragged into nearby building by Green Martian females.
    - **Physical Description:** Slender, girlish figure; oval face, beautiful features; coal black waving hair; light reddish copper skin; naked save for highly wrought ornaments.
    - **Interaction:** Woman makes sign (appeal for succor); narrator fails to respond due to ignorance of customs.
- **Outcome:** Woman dragged away into depths of deserted edifice in dejection and contempt.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH008

| Asset ID | Environment Family | Role |
|----------|-------------------|------|
| martian_city_edifice | Martian City/Deserted Edifice | Primary |
| enemy_airship_vessel | Enemy Vessels/Airships | Secondary |
| street_level_ground | Street Level | Transit |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_city_edifice

[[SECTION markdown]]
**Environment Role:** Primary setting - windows, doorways, deserted edifice where Martians operate and narrator descends.

**Architecture & Geography:** Multi-story buildings with numerous windows for firing volleys; doorways that melt into like mist; streets at ground level; nearby buildings for prisoner entry.

**Lighting & Atmosphere:** Green Martian warriors melting into structures like mist; awe-inspiring sight of floating funeral pyre; deserted city atmosphere with sudden enemy arrival.

**Scale Cues:** Enemy vessels float fifty feet above ground swinging over hill crests; building heights accommodate window fire positions; street level accessible for narrator descent.

**Environmental Anchors:** Windows (firing positions), doorways (entry/exit points), streets (ground movement), edifice depths (prisoner destination).

**Descriptive Noun Phrases:** Deserted Martian city buildings, green warrior mist doorways, window firing galleries, street level ground, floating funeral pyre sight.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: enemy_airship_vessel

[[SECTION markdown]]
**Environment Role:** Secondary/transit setting - huge gray-painted craft that arrive and are captured.

**Architecture & Geography:** Huge long low vessels; strange banner on each ship; odd devices gleaming on prows; grappling hooks for hauling to ground; fifty feet above ground initially.

**Lighting & Atmosphere:** Gray-painted hulls with gleaming odd devices; drifting funeral pyre appearance when burning; missile fire lighting the vessel.

**Scale Cues:** Fifty feet above ground before capture; swinging broadside over city; several craft limping perceptibly; foremost vessel swings first then others follow in wake.

**Environmental Anchors:** Hulls (main body), prows (device locations), banners (identification), grappling hooks (capture mechanism).

**Descriptive Noun Phrases:** Gray-painted enemy airships, strange banner vessels, odd device prows, grappling hook capture points, floating funeral pyre craft.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: street_level_ground

[[SECTION markdown]]
**Environment Role:** Transit setting - ground level where narrator descends and prisoner is dragged through streets.

**Architecture & Geography:** Street level of deserted city; nearby building for prisoner entry; depths of deserted edifice for final destination; ground accessible for narrator movement.

**Lighting & Atmosphere:** Awe-inspiring sight of floating funeral pyre from street level; depressed atmosphere after kindred people defeat; strange yearning toward unknown foemen.

**Scale Cues:** Ground level contrasting with fifty-foot vessel height; street width for narrator descent; building heights visible from ground perspective.

**Environmental Anchors:** Streets (movement paths), ground level (narrator position), nearby buildings (prisoner entry points), edifice depths (final destination).

**Descriptive Noun Phrases:** Street level city ground, deserted edifice streets, nearby building entrances, ground movement paths, funeral pyre sight from street.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
