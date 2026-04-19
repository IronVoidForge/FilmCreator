# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:09:41.047605+00:00
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

# Chapter Summary: The Fair Captive from the Sky

**Narrative Arc:**
The third day after the incubator ceremony, the procession sets out toward home but is ordered to return immediately upon entering the open ground. The green Martians melt into nearby buildings like mist. The narrator enters a building on the city front (where he previously encountered apes) and climbs to an upper floor to observe the valley.

**Visual Continuity & Battle Sequence:**
*   **Arrival of Fleet:** Twenty gray-painted, long, low airships swing over the crest of the nearest hill. Each carries a strange banner and a painted device on the prow that gleams in sunlight. Figures crowd forward decks.
*   **First Volley:** Green Martian warriors fire a terrific volley from building windows facing the valley. The scene changes by magic; the foremost vessel swings broadside, bringing guns into play.
*   **Fire Exchange:** Our own fire never diminishes (approx 75% accuracy). A little figure drops on one craft at each explosion; banners and upper works dissolve in spurts of flame. Enemy fire is ineffectual due to suddenness of first volley catching crews unprepared.
*   **Tactics:** Green warriors have objective points for fire: wireless finding/sighting apparatus, smaller guns, gunners, officers, crew members, upper works, steering gear/propellers.
*   **Retreat & Damage:** Twenty minutes after the first volley, the fleet swings trailing off. Several craft limp perceptibly. Fire ceases; energies focus on escape. Warriors rush to roofs and follow retreating armada with continuous fusillade.
*   **The Disabled Ship:** One barely moving craft is in sight, entirely unmanned, drifting slowly. Warriors cease firing as it appears helpless. As she neared the city (50 feet above ground), warriors swarmed upon her from windows using great spears to ease collision shock. Grappling hooks were thrown; big boat hauled to ground.
*   **Search & Loot:** Warriors search vessel stem to stern. Dead sailors examined for signs of life. A party drags a little figure (less than half as tall, walks erect). Loot requisitioned: arms, ammunition, silks, furs, jewels, carved stone vessels, solid foods/liquids (casks of water).
*   **Destruction:** Last load removed; craft towed far out into valley. Warriors empty contents of carboys over dead sailors/decks. Last warrior throws missile back upon vessel; faint spurt of flame rises. Guy ropes released; warship soars majestically into air, decks/upper works mass of roaring flames.
*   **Aftermath:** Ship drifts to southeast, rising higher as flames eat wooden parts. Narrator watches for hours from roof until lost in distance. Warriors follow with possibility of reinforcement return.

**Character Interaction & Resolution:**
*   **Narrator's Emotion:** Depressed by defeat of kindred people (humans) rather than routing unfriendly creatures. Feels hallucination; yearning toward unknown foemen; hope fleet returns for reckoning.
*   **Street Scene:** Woola follows at heel. Sola rushes up as though searching. Cavalcade returning to plaza; homeward march given up for week due to fear of air craft return attack. Lorquas Ptomel remains at deserted city until danger passed.
*   **The Prisoner:** As Sola and narrator enter plaza, glimpse of prisoner from battle craft being roughly dragged into nearby building by green Martian females.
*   **Visual Description of Captive:** Slender, girlish figure similar to earthly women. Oval face, beautiful features, finely chiseled. Large lustrous eyes. Mass of coal black, waving hair caught loosely into strange coiffure. Skin light reddish copper color; crimson glow of cheeks and ruby lips. Destitute of clothes save for highly wrought ornaments; entirely naked.
*   **Interaction:** Captive does not see narrator at first. Just as she disappears through portal, eyes meet mine. She makes little sign with free hand (ununderstood). Look of hope fades into dejection, loathing, contempt. Narrator realizes he did not answer signal; feels appeal for succor prevented by ignorance. Dragged out of sight into depths of deserted edifice.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH008

## Valley
- **Role:** Primary observation setting
- **Description:** Wide valley observed from city buildings, visible geography with distant features
- **Atmosphere:** Open ground, daylight conditions during battle sequence
- **Anchors:** Distant hills, valley floor, horizon line

## City Buildings
- **Role:** Transit and observation setting
- **Architecture:** Multi-story urban structures on city front
- **Lighting:** Sunlight with interior shadows from upper floors
- **Scale:** Large buildings allowing vertical movement to upper levels
- **Anchors:** Windows facing valley, building facades, stairwells

## Plaza
- **Role:** Secondary character interaction setting
- **Description:** Open paved area near city center
- **Atmosphere:** Public gathering space with returning procession
- **Scale:** Ground level open area for crowd movement
- **Anchors:** Building entrances, plaza boundaries, street access points

## Roof
- **Role:** Observation and transit setting
- **Description:** Elevated flat surface atop city buildings
- **Lighting:** Daylight conditions with panoramic valley views
- **Scale:** Large enough for prolonged observation hours
- **Anchors:** Building edge, parapet walls, distant horizon

## Deserted Edifice
- **Role:** Secondary transit setting
- **Description:** Abandoned building interior and depths
- **Atmosphere:** Empty urban structure with portal access
- **Scale:** Multi-level interior allowing vertical movement
- **Anchors:** Building entrance, internal corridors, upper floors

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_ch008

[[SECTION markdown]]
# Valley - Chapter CH008 Environment

## Environment Role
Primary observation setting for battle sequence and aftermath viewing.

## Architecture and Geography
Wide open valley with visible distant hills forming natural horizon line. Ground level terrain suitable for airship movement and fleet operations. Valley floor extends toward city boundaries creating depth perspective from elevated viewpoints.

## Lighting and Atmosphere Cues
Daylight conditions during first volley and battle sequence. Sunlight illuminates painted devices on prow that gleam in sunlight. Distant features visible through atmospheric haze. Aftermath viewing occurs under sustained daylight for hours until ship lost in distance.

## Scale Cues and Environmental Anchors
Large scale valley allowing fleet movement across crest of nearest hill. Distant hills serve as primary horizon anchor. Valley floor provides depth reference for airship positioning. Horizon line marks boundary between open ground and city structures.

## Descriptive Noun Phrases
- Wide valley floor
- Distant hills forming natural horizon
- Open ground conditions
- Airship movement terrain
- Battle sequence viewing area
- Fleet operation zone
- Daylight observation space
- Valley depth perspective
- Horizon line boundary
- City structure edge reference

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_buildings_ch008

[[SECTION markdown]]
# City Buildings - Chapter CH008 Environment

## Environment Role
Transit and observation setting for narrator movement and battle viewing.

## Architecture and Geography
Multi-story urban structures on city front with windows facing valley. Interior spaces allowing vertical movement to upper floors. Building facades create exterior observation points. Stairwells and portals enable access between levels.

## Lighting and Atmosphere Cues
Sunlight conditions with interior shadows from upper floor positions. Windows provide natural light sources for interior observation. Green Martians melt into nearby buildings like mist suggesting atmospheric integration with structure surfaces.

## Scale Cues and Environmental Anchors
Large buildings allowing narrator to climb to upper floor for valley observation. Windows facing valley serve as primary viewing anchors. Building facades create exterior reference points. Portal access points enable entry and exit movement.

## Descriptive Noun Phrases
- Multi-story urban structures
- City front buildings
- Upper floor observation levels
- Windows facing valley
- Building facade surfaces
- Interior stairwell spaces
- Portal access points
- Urban structure interiors
- Elevated viewing positions
- Ground level building bases

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_ch008

[[SECTION markdown]]
# Plaza - Chapter CH008 Environment

## Environment Role
Secondary character interaction setting for procession and prisoner arrival.

## Architecture and Geography
Open paved area near city center with building entrances providing access points. Street level gathering space for crowd movement and cavalcade return. Public space boundaries define plaza perimeter.

## Lighting and Atmosphere Cues
Daylight conditions during returning procession scene. Open area allows natural light distribution across ground surface. Public gathering atmosphere with crowd presence affecting ambient conditions.

## Scale Cues and Environmental Anchors
Ground level open area suitable for crowd movement and procession return. Building entrances serve as primary access anchors. Street access points define plaza boundaries. Plaza floor provides reference for character positioning.

## Descriptive Noun Phrases
- Open paved gathering area
- City center plaza space
- Building entrance access points
- Street level public area
- Crowd movement ground surface
- Procession return zone
- Public gathering perimeter
- Plaza boundary markers
- Ground level open space
- Urban public square

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: roof_ch008

[[SECTION markdown]]
# Roof - Chapter CH008 Environment

## Environment Role
Observation and transit setting for prolonged viewing of battle aftermath.

## Architecture and Geography
Elevated flat surface atop city buildings with panoramic valley views. Building edge provides safety boundary. Parapet walls create perimeter reference points. Large enough surface area for sustained observation hours.

## Lighting and Atmosphere Cues
Daylight conditions with unobstructed panoramic valley visibility. Elevated position provides enhanced light distribution across viewing area. Sustained daylight viewing until ship lost in distance.

## Scale Cues and Environmental Anchors
Large roof surface allowing narrator to watch for hours from elevated position. Building edge serves as primary safety anchor. Distant horizon visible from elevated viewpoint. Parapet walls create perimeter reference points.

## Descriptive Noun Phrases
- Elevated flat observation surface
- Building rooftop area
- Panoramic valley viewing zone
- Building edge boundary
- Parapet wall perimeter
- Elevated daylight position
- Horizon viewing platform
- Rooftop observation space
- Elevated safety boundary
- Panoramic viewing area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: deserted_edifice_ch008

[[SECTION markdown]]
# Deserted Edifice - Chapter CH008 Environment

## Environment Role
Secondary transit setting for prisoner movement and building interior exploration.

## Architecture and Geography
Abandoned building interior with multi-level structure allowing vertical movement. Portal access points enable entry and exit between levels. Internal corridors provide horizontal movement paths. Building depths create interior reference spaces.

## Lighting and Atmosphere Cues
Interior lighting conditions from remaining windows or artificial sources. Empty urban structure atmosphere with portal access creating light sources. Interior shadows from upper floor positions affecting ambient conditions.

## Scale Cues and Environmental Anchors
Multi-level interior allowing vertical movement between floors. Building entrance serves as primary access anchor. Internal corridors provide horizontal movement reference points. Upper floors create elevated interior viewing positions.

## Descriptive Noun Phrases
- Abandoned building interior
- Multi-level structure space
- Portal access entry points
- Internal corridor pathways
- Building depth interior zones
- Upper floor interior levels
- Vertical movement spaces
- Empty urban structure
- Interior reference areas
- Building entrance access point

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
