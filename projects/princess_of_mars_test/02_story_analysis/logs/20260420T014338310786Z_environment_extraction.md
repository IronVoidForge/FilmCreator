# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:43:38.310786+00:00
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

Chapter id: CH027

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

# Chapter Summary: Chapter XXVII - From Joy to Death

## Visual Continuity Facts
*   **Golden Incubator:** Located on the roof of the Helium Palace, containing a snow-white egg representing the unborn son.
*   **Airship Arrival:** A bright-white light approaches Helium, landing at the palace docks with dispatch signals for the Jeddak.
*   **Council Chamber:** Tardos Mors paces on the raised platform while members fill the chamber; silence follows his announcement of doom.
*   **Palace Garden:** Royal family (including Woola) gathers in a sunken garden within an inner courtyard as breathing becomes difficult.
*   **Flight Path:** Carter flies low across an old sea bottom to maintain sufficient air for breathing, discarding ornaments and lying on the deck.
*   **Atmosphere Plant Exterior:** Great walls loom before him; small door with crew laboring to pierce the wall.
*   **Plant Interior:** Three great doors open sequentially; Carter opens the second and third while collapsing unconscious.

## Broad Story Summary
Barsoom faces extinction as the atmosphere plant engine stops, causing air pressure to decrease rapidly. The Jeddak declares three days remaining before death by asphyxiation becomes inevitable for the entire population. John Carter discovers "nine long forgotten sounds" (thought waves) which serve as the key to unlock the three great doors of the atmosphere plant. He flies to the plant at high speed, discarding all weight except the engine and compass. Upon arrival, he opens the doors sequentially while his companion starts the pumps, saving Barsoom but collapsing from exhaustion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test

## Stable Environment Families

| Asset ID | Environment Name | Role | Location |
|----------|------------------|------|----------|
| golden_incubator | Golden Incubator | Primary | Helium Palace Roof |
| palace_docks | Palace Docks | Transit | Helium Palace Arrival Point |
| council_chamber | Council Chamber | Secondary | Raised Platform Area |
| palace_garden | Palace Garden | Secondary | Sunken Inner Courtyard |
| flight_path | Flight Path | Transit | Old Sea Bottom |
| atmosphere_plant_exterior | Atmosphere Plant Exterior | Primary | Great Walls with Small Door |
| atmosphere_plant_interior | Atmosphere Plant Interior | Primary | Three Great Doors Area |

## Environment Notes

- All environments relate to Barsoom's atmospheric crisis and extinction threat
- Architecture ranges from palace structures to industrial plant facilities
- Lighting cues include bright-white approach lights, sunken garden shadows, and interior door sequences
- Scale varies from intimate council spaces to massive wall structures
- Recurring anchors: Helium Palace, atmosphere plant doors, flight path landmarks

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: golden_incubator

[[SECTION markdown]]
# Golden Incubator

## Environment Role
Primary setting - contains the unborn son's snow-white egg representation

## Architecture and Geography
Roof structure of Helium Palace with elevated positioning above palace grounds. Contains a large incubation chamber housing the egg display.

## Lighting and Atmosphere Cues
Bright-white approach light from airship arrival creates dramatic contrast against palace roof. Egg displays in pristine white condition representing unborn life. Snow-white color palette dominates interior space.

## Scale and Environmental Anchors
Large open roof space with elevated vantage point. Palace architecture provides surrounding context. Egg chamber serves as central focal point within incubator structure.

## Descriptive Noun Phrases
snow-white egg display, Helium Palace roof structure, elevated incubation chamber, unborn son representation, bright-white approach lighting, pristine white interior space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: palace_docks

[[SECTION markdown]]
# Palace Docks

## Environment Role
Transit setting - arrival point for airship dispatch signals to Jeddak

## Architecture and Geography
Docking area at Helium Palace with landing platform infrastructure. Features dispatch signal mechanisms and approach landing zone.

## Lighting and Atmosphere Cues
Bright-white light approaches from distance creating high-contrast arrival effect. Dispatch signals illuminate dock area during airship landing sequence.

## Scale and Environmental Anchors
Large docking platform with palace architecture in background. Airship landing creates temporary scale expansion. Dock infrastructure serves as primary anchor point.

## Descriptive Noun Phrases
airship landing platform, Helium Palace docks, dispatch signal mechanisms, bright-white approach light, arrival zone infrastructure, Jeddak communication area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: council_chamber

[[SECTION markdown]]
# Council Chamber

## Environment Role
Secondary setting - raised platform where Tardos Mors announces doom

## Architecture and Geography
Large chamber with raised platform for speaker. Members fill surrounding chamber space creating enclosed council area. Raised platform provides elevated speaking position.

## Lighting and Atmosphere Cues
Silence creates heavy atmospheric weight after announcement. Chamber lighting emphasizes speaker on raised platform. Enclosed space creates intimate yet formal atmosphere.

## Scale and Environmental Anchors
Raised platform serves as central anchor point. Chamber members create surrounding scale context. Platform elevation provides visual hierarchy within chamber space.

## Descriptive Noun Phrases
raised platform speaking area, council chamber interior, Tardos Mors announcement zone, enclosed member gathering space, silence-weighted atmosphere, formal chamber architecture

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: palace_garden

[[SECTION markdown]]
# Palace Garden

## Environment Role
Secondary setting - sunken garden where royal family gathers during breathing crisis

## Architecture and Geography
Sunken garden structure within inner courtyard. Features elevated surrounding walls creating enclosed garden space. Royal gathering area with central open space.

## Lighting and Atmosphere Cues
Sunken position creates shadowed interior lighting. Breathing difficulty creates heavy atmospheric weight. Sunken garden provides intimate royal gathering atmosphere.

## Scale and Environmental Anchors
Sunken structure serves as primary anchor point. Inner courtyard walls provide surrounding scale context. Royal family gathering area creates central focal point within garden space.

## Descriptive Noun Phrases
sunken garden structure, inner courtyard location, royal family gathering zone, breathing difficulty atmosphere, enclosed garden space, sunken interior lighting

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: flight_path

[[SECTION markdown]]
# Flight Path

## Environment Role
Transit setting - low flight across old sea bottom for breathing maintenance

## Architecture and Geography
Old sea bottom terrain with historical underwater geography. Features low-altitude flight corridor through ancient seabed landscape. Historical sea floor provides distinctive terrain characteristics.

## Lighting and Atmosphere Cues
Low altitude creates intimate atmospheric perspective. Flight path lighting emphasizes movement through old sea bottom. Discarded ornaments create visual debris along flight corridor.

## Scale and Environmental Anchors
Old sea bottom serves as primary anchor point. Low flight altitude creates intimate scale relationship. Historical seabed provides distinctive environmental context for transit journey.

## Descriptive Noun Phrases
old sea bottom terrain, low-altitude flight corridor, historical underwater geography, discarded ornament debris, ancient seabed landscape, breathing maintenance zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: atmosphere_plant_exterior

[[SECTION markdown]]
# Atmosphere Plant Exterior

## Environment Role
Primary setting - great walls with small door and crew laboring to pierce wall

## Architecture and Geography
Massive wall structure with small door entrance. Features industrial plant exterior with towering wall architecture. Crew labor area at small door provides access point through great walls.

## Lighting and Atmosphere Cues
Great walls loom creating imposing atmospheric scale. Small door creates intimate contrast against massive wall structure. Crew labor activity creates dynamic lighting effects at pierce point.

## Scale and Environmental Anchors
Great walls serve as primary anchor point creating overwhelming scale. Small door provides intimate access anchor. Wall piercing location serves as critical environmental landmark.

## Descriptive Noun Phrases
great wall structure, small door entrance, industrial plant exterior, towering wall architecture, crew labor pierce zone, imposing atmospheric scale, wall piercing activity area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: atmosphere_plant_interior

[[SECTION markdown]]
# Atmosphere Plant Interior

## Environment Role
Primary setting - three great doors with sequential opening and pump activation

## Architecture and Geography
Interior space containing three great door structures. Features sequential door arrangement with central pump activation zone. Industrial interior with massive door architecture.

## Lighting and Atmosphere Cues
Three doors open sequentially creating dramatic lighting progression. Interior space provides enclosed industrial atmosphere. Pump activation creates mechanical lighting effects within interior zone.

## Scale and Environmental Anchors
Three great doors serve as primary anchor points creating sequential scale hierarchy. Interior pump zone serves as central operational anchor. Door arrangement provides distinctive environmental landmark sequence.

## Descriptive Noun Phrases
three great door structures, sequential opening mechanism, industrial plant interior, massive door architecture, pump activation zone, enclosed interior space, mechanical lighting progression

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
