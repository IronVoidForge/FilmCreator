# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:57:29.737217+00:00
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

Chapter id: CH017

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

# Chapter Summary: A Costly Recapture (Chapter XVII)

## Scene 1: Rescue from Tal Hajus' Chamber
**Plot:** Carter overhears Tal Hajus planning to torture Dejah Thoris for ten days. He interrupts the scene, killing Tal Hajus with a punch after raising his sword. He rescues Dejah Thoris and Sola from the chamber where they were held captive before the floor was cleared of warriors.
**Visuals:** The inner chamber is immense and circular, thronged with chieftains and women. Tal Hajus squats on a raised platform with six limbs resembling a devil fish. Dejah Thoris stands erect in her beautiful figure, showing scorn and disgust.

## Scene 2: Escape from Thark City and Initial Journey
**Plot:** Carter lowers Dejah Thoris and Sola to the ground using straps and leather from his trappings. They mount their thoats and ride out of the city of Thark towards Helium. They initially turn northeast across the mossy waste instead of circling back northwest.
**Visuals:** The courtyard where they left their thoats is visible. The group rides through the hills to the south, then turns northeast. Dejah Thoris clings to Carter's shoulder, sobbing quietly.

## Scene 3: Getting Lost and Woola's Arrival
**Plot:** The party gets lost as no waterways are in sight. They travel all night and day, eventually collapsing from fatigue. Woola (Carter's faithful dog) follows them across the trackless waste to share their fate.
**Visuals:** The landscape is a yellow, moonlit moss with no distant trees. The group lies down on the moss to sleep. Woola snuggles close to Carter, showing his love and loyalty.

## Scene 4: First Thoat Collapse
**Plot:** The first thoat begins to stumble and eventually pitches violently to the ground. Carter decides not to kill it immediately but leaves it behind after relieving it of its trappings. They continue with one beast, walking while Dejah Thoris rides.
**Visuals:** The poor beast is in a pitiable condition, unable to rise. Trappings are flung down beside it. Sola and Carter walk while Dejah Thoris rides the remaining thoat.

## Scene 5: Encounter with Thark Warriors (Tars Tarkas' Men)
**Plot:** A party of mounted men is sighted in the hills. They appear to be Thark warriors sent to capture them. Carter sacrifices himself, using his rifle and jumping abilities to hold off the warriors while Dejah Thoris and Sola escape into the hills. He is eventually captured by the remaining warriors after fighting until he is overwhelmed.
**Visuals:** Several hundred mounted warriors are discernible from a pass. A chieftain uses a fieldglass to spot them. Carter fires his rifle (even hundred rounds in magazine, another hundred in belt) while lying flat on the moss. He is eventually struck down by blows falling upon him in perfect torrents.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XVII

## tal_hajus_chamber
**Role:** Primary setting for Scene 1  
**Description:** Immense circular inner chamber where Tal Hajus is held captive with chieftains and women. Raised platform with six limbs resembling devil fish.

## thark_city_courtyard  
**Role:** Secondary/Transit setting for Scenes 1-2  
**Description:** Courtyard area near Thark City where Carter lowers Dejah Thoris and Sola to ground using straps and leather from trappings.

## mossy_waste_desert
**Role:** Primary/Transit setting for Scenes 2-5  
**Description:** Yellow moonlit moss landscape with no waterways, distant trees, or visible geography beyond hills. Trackless waste where party travels all night and day.

## southern_hills
**Role:** Secondary/transit setting for Scenes 2 & 5  
**Description:** Hills to the south and pass areas where mounted warriors are sighted from distance. Fieldglass spotting point with several hundred discernible warriors.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: tal_hajus_chamber

[[SECTION markdown]]
# Tal Hajus Chamber

## Environment Role
Primary setting for Scene 1 - Rescue from Tal Hajus' Chamber

## Architecture and Geography
- Immense circular inner chamber
- Raised platform with six limbs resembling devil fish
- Interior space thronged with chieftains and women
- Inner chamber floor cleared of warriors after rescue

## Lighting and Atmosphere Cues
- Dramatic interior lighting highlighting central figures
- Tal Hajus squatting on elevated platform
- Dejah Thoris standing erect showing scorn and disgust
- Intense emotional atmosphere during torture planning scene

## Scale Cues and Environmental Anchors
- Chamber size accommodates multiple chieftains and women simultaneously
- Raised platform creates vertical hierarchy within space
- Circular geometry defines chamber boundaries
- Platform serves as central anchor point for Tal Hajus presence

## Descriptive Noun Phrases
- immense circular inner chamber
- raised devil-fish platform
- thronged chieftain assembly
- torture planning interior
- captive holding chamber
- warrior-cleared floor space
- six-limbed elevated structure

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_city_courtyard

[[SECTION markdown]]
# Thark City Courtyard

## Environment Role
Secondary/Transit setting for Scenes 1-2 - Escape from Thark City and Initial Journey

## Architecture and Geography
- Courtyard area near Thark City entrance
- Ground level access point for escape
- Visible courtyard where thoats were left before departure
- Connection between city interior and exterior landscape

## Lighting and Atmosphere Cues
- Daylight conditions during escape sequence
- Transition lighting from city to open waste
- Leather trappings visible in daylight
- Straps and equipment catching ambient light

## Scale Cues and Environmental Anchors
- Courtyard space accommodates multiple escapees with equipment
- Ground level provides access point for thoat mounting
- Visible courtyard boundaries define escape zone
- Thark City proximity serves as geographic anchor

## Descriptive Noun Phrases
- city entrance courtyard
- escape ground level
- visible departure area
- leather trappings storage
- thoat mounting platform
- city-to-waste transition zone
- escape equipment drop-off point

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mossy_waste_desert

[[SECTION markdown]]
# Mossy Waste Desert

## Environment Role
Primary/Transit setting for Scenes 2-5 - Getting Lost and Woola's Arrival, First Thoat Collapse, Encounter with Thark Warriors

## Architecture and Geography
- Yellow moonlit moss landscape
- No waterways in sight during travel
- Trackless waste with no distant trees
- Open desert terrain across hills to south
- Pass areas where mounted warriors are sighted from distance

## Lighting and Atmosphere Cues
- Moonlit yellow moss conditions
- Night and day travel lighting variations
- Wide open landscape with minimal shadows
- Atmospheric visibility limited by distance
- Fieldglass spotting point in pass areas

## Scale Cues and Environmental Anchors
- Vast landscape accommodates party traveling all night and day
- No visible landmarks beyond hills to south
- Trackless waste defines geographic boundaries
- Pass serves as distant observation point for several hundred warriors
- Moss surface provides ground-level anchor throughout journey

## Descriptive Noun Phrases
- yellow moonlit moss landscape
- trackless desert waste
- no waterways terrain
- open hills to south
- pass observation point
- wide open desert expanse
- fatigue-collapse resting area
- several hundred discernible warriors from distance

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: southern_hills

[[SECTION markdown]]
# Southern Hills

## Environment Role
Secondary/transit setting for Scenes 2 & 5 - Escape from Thark City and Initial Journey, Encounter with Thark Warriors

## Architecture and Geography
- Hills to the south of Thark City
- Pass areas where mounted warriors are sighted
- Distant hills visible from courtyard
- Geographic boundary between city and waste
- Fieldglass spotting point in pass areas

## Lighting and Atmosphere Cues
- Daylight conditions during escape sequence
- Distant hill silhouettes against sky
- Pass area lighting for warrior observation
- Atmospheric visibility limited by distance
- Hill contours create natural elevation changes

## Scale Cues and Environmental Anchors
- Hills serve as distant geographic markers
- Pass areas provide elevated observation points
- Several hundred warriors discernible from pass vantage
- Hill-to-waste transition defines escape route
- Southern hills anchor journey direction

## Descriptive Noun Phrases
- southern hill range
- pass observation point
- distant warrior sighting area
- fieldglass spotting location
- several hundred mounted warriors
- hills to south geography
- elevated pass vantage point
- escape route boundary marker

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
