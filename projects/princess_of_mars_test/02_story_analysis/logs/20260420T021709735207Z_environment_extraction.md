# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:17:09.735207+00:00
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

Chapter id: CH007

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

# Chapter Summary: Child-Raising on Mars (CH007)

## Scene 1: The Procession to the Incubator
**Visual Continuity:**
- Sola escorts the narrator to the plaza where ~250 three-wheeled chariots are being harnessed to mastodonian animals.
- Warriors ride at the head (five abreast) and rear of the caravan; outriders flank sides.
- Animals are guided telepathically, wearing no bit or bridle.
- The cavalcade moves in single file toward the incubator location.

**Narrative:**
- The narrator is dragged into an empty chariot by Sola and proceeds with the procession.
- They travel across the valley before the city, through hills, down to the dead sea bottom (incubator terminal point).
- Upon arrival, chariots are parked with military precision on four sides of the enclosure.

## Scene 2: The Hatching Ceremony
**Visual Continuity:**
- Half a score of warriors dismount and advance toward the incubator.
- Tars Tarkas explains to Lorquas Ptomel Jed regarding the subject of conversation.
- The incubator is alive with hideous little devils (young Martians) ranging 3-4 feet in height.
- Warriors command relative to the incubator; narrator leaps over parked chariots for edification.

**Narrative:**
- Tars Tarkas signs for Sola to send the narrator to him.
- The narrator repeats his performance of leaping over chariots for Lorquas Ptomel's edification.
- Warriors break an opening in the incubator wall large enough for exit of young Martians.

## Scene 3: Child Capture and Rearing Ritual
**Visual Continuity:**
- Women and younger Martians form two solid walls leading out through chariots into the plain.
- Little Martians scamper between walls; captured one at a time by women/older children.
- Last in line captures first to reach end; opposite captures second, etc.
- Women fall out of line and return to respective chariots; young men turn over captured ones to women.

**Narrative:**
- The ceremony involves capturing young Martians as they leave the incubator.
- Work of rearing consists solely in teaching them to talk and use weapons from first year.
- Young Martians are common children of the community, unknown to their mothers or fathers.
- Education devolves upon females who chance to capture them (e.g., Sola).

## Scene 4: Explanation of Martian Child-Rearing System
**Visual Continuity:**
- Incubators built in remote fastnesses to avoid discovery by other tribes.
- Discovery of alien incubator results in no children for another five years.
- Community composed of ~30,000 souls roaming arid land between 40-80 degrees south latitude.

**Narrative:**
- System involves careful selection of hardiest specimens; birth rate regulated to offset death loss.
- Each female brings forth ~13 eggs/year; only ~100 most perfect chosen from yearly supply.
- Eggs hidden in subterranean vaults (too low for incubation) until examined by council of twenty chieftains.
- After five years, ~500 almost perfect eggs placed in air-tight incubators to hatch by sun's rays.
- System causes loss of finer feelings and higher humanitarian instincts among Martians.

## Scene 5: Narrator's Development and Return
**Visual Continuity:**
- Sola's duties doubled caring for young Martian as well as narrator.
- Both require little attention; equally advanced in Martian education.
- Narrator develops telepathic powers shortly after tutelage.

**Narrative:**
- After return to dead city, narrator passes several days in comparative idleness.
- Warriors ride forth early morning and return just before darkness (transporting eggs to incubator).
- Sola takes upon herself to train narrator and young Martian together.
- Narrator masters language within a week; understands nearly everything said.
- Narrator develops telepathic powers so that he can sense practically everything around him.
- **Key Fact:** While narrator catches telepathic messages easily from others, no one could read a jot from his mind under any circumstances (undoubted advantage over Martians).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Child-Raising on Mars (CH007)

## Primary Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|-------|--------------|
| plaza_valley_procession | Plaza/Valley Procession Route | Primary | Chariot harnessed area, valley before city, hills, dead sea bottom |
| incubator_terminal | Incubator Terminal Enclosure | Primary | Air-tight incubators, sun-ray hatching zone, young Martian emergence point |

## Secondary Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|-------|--------------|
| remote_fastnesses | Remote Fastness Incubator Sites | Secondary | Subterranean vaults, council examination chambers, hidden from other tribes |
| arid_land_territory | Arid Land Community Territory | Secondary | 40-80 degrees south latitude, roaming territory between dead cities |

## Transit Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|-------|--------------|
| egg_transport_routes | Egg Transport Routes | Transit | Warriors ride early morning to darkness, subterranean vault connections |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_valley_procession

[[SECTION markdown]]
# Plaza Valley Procession Route

## Environment Role
Primary transit setting for the chariot procession and assembly point.

## Architecture and Geography
- Open plaza where ~250 three-wheeled chariots are harnessed to mastodonian animals
- Valley terrain before city boundaries
- Rolling hills leading downward toward dead sea bottom
- Single-file procession route through valley floor
- Four-sided parking area around incubator enclosure

## Lighting and Atmosphere Cues
- Telepathic guidance of animals (no bit or bridle)
- Military precision parking on four sides
- Daylight conditions for sun-ray hatching preparation
- Atmospheric telepathic communication between warriors and animals

## Scale Cues and Environmental Anchors
- ~250 three-wheeled chariots in procession
- Five warriors abreast at head and rear of caravan
- Outriders flanking sides of cavalcade
- Mastodonian animal guides (no bridle)
- Incubator enclosure as destination anchor

## Descriptive Noun Phrases for Render-Facing Prompts
- "chariot harnessed plaza"
- "valley procession route"
- "mastodonian animal guide station"
- "military precision parking area"
- "dead sea bottom terminal point"
- "hill descent corridor"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: incubator_terminal

[[SECTION markdown]]
# Incubator Terminal Enclosure

## Environment Role
Primary setting for hatching ceremony and young Martian emergence.

## Architecture and Geography
- Air-tight incubator containers in dead sea bottom enclosure
- Subterranean vault connections to remote fastnesses
- Wall structure with breakable opening for exit
- Sun-ray exposure zone for hatching process
- Enclosed terminal point at valley floor end

## Lighting and Atmosphere Cues
- Sun's rays penetrating air-tight incubators
- Alive atmosphere with young Martians (3-4 feet height)
- Hideous little devils emerging from incubator
- Daylight conditions for hatching completion
- Telepathic command atmosphere around enclosure

## Scale Cues and Environmental Anchors
- ~500 almost perfect eggs from yearly supply
- Half score of warriors dismounting at entrance
- Young Martians ranging 3-4 feet in height
- Incubator wall as primary anchor structure
- Chariot parking area surrounding enclosure

## Descriptive Noun Phrases for Render-Facing Prompts
- "air-tight incubator container"
- "sun-ray hatching zone"
- "young Martian emergence point"
- "enclosure terminal wall"
- "dead sea bottom hatchery"
- "subterranean vault connection"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: remote_fastnesses

[[SECTION markdown]]
# Remote Fastness Incubator Sites

## Environment Role
Secondary setting for incubator construction and egg examination.

## Architecture and Geography
- Subterranean vaults for egg storage (too low for incubation)
- Remote locations to avoid discovery by other tribes
- Council chamber for twenty chieftains examination
- Air-tight container fabrication sites
- Hidden from alien tribe surveillance

## Lighting and Atmosphere Cues
- Hidden atmosphere avoiding tribal discovery
- Subterranean vault lighting conditions
- Council chamber formal examination lighting
- Remote isolation from other territories
- Protective concealment from external threats

## Scale Cues and Environmental Anchors
- Council of twenty chieftains examining eggs
- ~13 eggs per female yearly supply
- ~100 most perfect chosen from yearly supply
- Subterranean vault storage capacity
- Remote fastness location markers

## Descriptive Noun Phrases for Render-Facing Prompts
- "subterranean egg vault"
- "council examination chamber"
- "remote incubator site"
- "tribal concealment zone"
- "air-tight container fabrication area"
- "hidden from alien surveillance"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arid_land_territory

[[SECTION markdown]]
# Arid Land Community Territory

## Environment Role
Secondary setting for community movement and roaming territory.

## Architecture and Geography
- Arid land between 40-80 degrees south latitude
- Roaming territory of ~30,000 souls
- Dead city locations as reference points
- Egg transport route corridors
- Community movement pathways

## Lighting and Atmosphere Cues
- Sun's rays for incubation exposure
- Arid land atmospheric conditions
- Daylight to darkness warrior patrol cycles
- Roaming territory visibility conditions
- Remote fastness concealment atmosphere

## Scale Cues and Environmental Anchors
- ~30,000 souls in community
- Warriors ride early morning to just before darkness
- Dead city as territorial anchor
- Egg transport route markers
- Latitude range 40-80 degrees south

## Descriptive Noun Phrases for Render-Facing Prompts
- "arid land territory"
- "community roaming zone"
- "dead city territorial anchor"
- "egg transport corridor"
- "south latitude 40-80 degrees"
- "warrior patrol route"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: egg_transport_routes

[[SECTION markdown]]
# Egg Transport Routes

## Environment Role
Transit setting for egg movement between vaults and incubators.

## Architecture and Geography
- Warriors riding routes from early morning to darkness
- Subterranean vault connection pathways
- Dead city to remote fastness corridors
- Egg transport vehicle paths
- Route markers between territories

## Lighting and Atmosphere Cues
- Early morning daylight conditions
- Just before darkness return timing
- Sun-ray exposure during transport
- Protective concealment atmosphere
- Warrior patrol lighting cycles

## Scale Cues and Environmental Anchors
- Warriors riding forth early morning
- Return just before darkness
- Egg transport vehicle capacity
- Route distance between vaults and incubators
- Dead city as starting/ending point

## Descriptive Noun Phrases for Render-Facing Prompts
- "egg transport route"
- "warrior patrol corridor"
- "subterranean vault pathway"
- "early morning daylight zone"
- "just before darkness return path"
- "dead city to incubator route"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
