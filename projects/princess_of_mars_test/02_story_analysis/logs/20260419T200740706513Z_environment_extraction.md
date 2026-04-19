# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:07:40.706513+00:00
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

# Chapter VII Summary: Child-Raising on Mars

## Opening Scene Sequence
- Location: City plaza after breakfast (exact replica of preceding day's meal)
- Visual: Sola escorts narrator to plaza where entire community watches harnessing of 250 three-wheeled chariots
- Each chariot drawn by single mastodonian animal, gorgeously decorated with metal ornaments, jewels, silks, furs
- Female Martians seated in chariots loaded with ornaments; young Martian drivers perched on beasts
- Warriors at head (five abreast) and rear of caravan; outriders flank sides

## Procession to Incubator
- Formation: Single file line of march
- Warrior count: ~200 at head, 200 at rear, 25-30 outriders on each side
- All but narrator heavily armed
- Draft animals guided entirely by telepathic means (no bit or bridle)
- Narrator dragged into empty chariot with Sola

## Incubator Ceremony - Key Visual Sequences
1. Arrival at incubator: Chariots parked with military precision on four sides of enclosure
2. Dismounting warriors: Half a score led by enormous chieftain Lorquas Ptomel, Jed; includes Tars Tarkas and lesser chiefs
3. Narrator's performance: Leaps entirely over parked chariots for edification of Lorquas Ptomel
4. Incubator contents: All but very few eggs hatched; hideous little devils 3-4 feet tall moving restlessly
5. Opening creation: Warriors break opening in wall large enough for exit

## Release Ceremony Visual Flow
- Formation: Women and younger Martians form two solid walls leading through chariots into plain
- Action: Little Martians scamper wild as deer, captured one at a time by women/older children
- Last in line captures first to reach end; opposite captures second, continuing until all leave enclosure
- Women who catch young fall out of line and return to respective chariots
- Young men's captives later turned over to some women

## Post-Ceremony Scene
- Sola found in narrator's chariot with hideous little creature held tightly in arms
- Narrator advances to incubator side under Tars Tarkas command (mastered walking under Martian conditions)
- Tars Tarkas points over incubator, says "Sak" - wants narrator to repeat performance

## Educational System Revealed
- Work of rearing: Teaching to talk and use weapons from first year of life
- Incubation period: Five years in subterranean vaults where temperature too low for incubation
- Birth rate: Each adult female brings forth about thirteen eggs each year
- Selection process: Council of twenty chieftains examines yearly supply; all but ~100 most perfect destroyed
- Final selection: About five hundred almost perfect eggs chosen from thousands after five years
- Hatching event: All but about one per cent hatching in two days

## Community Details
- Population: Approximately thirty thousand souls
- Territory: Arid and semi-arid land between forty and eighty degrees south latitude
- Headquarters: Southwest corner near crossing of two Martian canals
- Incubator location: Remote fastnesses, little likelihood of discovery by other tribes
- Journey ahead: Tremendous journey from dead city to incubator (narrator knew nothing)

## Character Development Notes
- Sola's duties doubled: Care for young Martian and narrator
- Both equally advanced in Martian education
- Narrator develops telepathic powers so he can sense practically everything around him
- Martian language extremely simple; week to make all wants known and understand nearly everything said
- Unique ability: Can catch telepathic messages from others but no one can read from his mind

## Setting Transitions
- Route: Out across little valley before city, through hills, down into dead sea bottom
- Incubator as terminal point of journey this day
- After return to dead city: Several days in comparative idleness
- Next day: All warriors ride forth early morning, don't return until just before darkness fell
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter VII

## Primary Environments
- city_plaza - Main gathering location for chariot procession
- incubator_enclosure - Subterranean vaults where egg hatching occurs

## Secondary/Transit Environments
- chariot_caravan - Three-wheeled vehicles with mastodonian draft animals
- dead_city - Terminal point of journey from incubator

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_plaza

[[SECTION markdown]]
# City Plaza Environment

## Environment Role
Primary setting for chariot gathering and community observation

## Architecture/Geography
- Open plaza space within dead city territory
- Arid land between forty and eighty degrees south latitude
- Southwest corner near crossing of two Martian canals
- Remote fastnesses with little discovery likelihood by other tribes

## Lighting and Atmosphere Cues
- Bright daylight conditions for morning gathering
- Clear visibility for community watching harnessing ceremony
- Dry, dusty atmosphere typical of arid Martian landscape

## Scale Cues and Recurring Environmental Anchors
- Accommodates 250 three-wheeled chariots in formation
- Space for ~30,000 souls population capacity
- Large enough for military precision parking on four sides of enclosure
- Open area allowing outriders to flank caravan sides

## Descriptive Noun Phrases
- plaza gathering space
- community observation area
- arid city territory
- chariot parking formation
- military precision enclosure
- southwest canal crossing
- remote fastness location
- dead city plaza

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: incubator_enclosure

[[SECTION markdown]]
# Incubator Enclosure Environment

## Environment Role
Primary terminal setting for egg hatching and creature release ceremony

## Architecture/Geography
- Subterranean vaults with low temperature conditions
- Enclosed space requiring wall opening for exit
- Remote location in little valley before city
- Four-sided enclosure for chariot parking formation

## Lighting and Atmosphere Cues
- Dim interior lighting from subterranean position
- Cold atmosphere too low for normal incubation
- Hatching event creates active movement within enclosed space
- All but one per cent hatching in two days creates dynamic environment

## Scale Cues and Recurring Environmental Anchors
- Accommodates ~500 almost perfect eggs after five years
- Space for 250 chariots parked on four sides
- Wall opening large enough for exit passage
- Interior space for 3-4 foot tall hideous little devils moving restlessly

## Descriptive Noun Phrases
- subterranean vault enclosure
- egg hatching chamber
- wall opening passage
- low temperature interior
- remote fastness location
- four-sided chariot parking
- creature release enclosure
- incubation period space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chariot_caravan

[[SECTION markdown]]
# Chariot Caravan Environment

## Environment Role
Secondary transit setting for procession from city to incubator

## Architecture/Geography
- Three-wheeled chariots drawn by single mastodonian animal each
- Gorgeously decorated with metal ornaments, jewels, silks, furs
- Female Martians seated in chariots loaded with ornaments
- Young Martian drivers perched on beasts
- Warriors positioned at head (five abreast) and rear of caravan

## Lighting and Atmosphere Cues
- Bright daylight for morning procession
- Metallic ornament reflections visible
- Colorful decorations create visual richness
- Telepathic guidance creates silent, coordinated movement

## Scale Cues and Recurring Environmental Anchors
- ~200 warriors at head, 200 at rear, 25-30 outriders on each side
- Single file line of march formation
- All but narrator heavily armed
- Draft animals guided entirely by telepathic means (no bit or bridle)

## Descriptive Noun Phrases
- three-wheeled chariot
- mastodonian draft animal
- gorgeously decorated vehicle
- metal ornament carriage
- jewel-adorned chariot
- silk-furred decoration
- warrior-headed caravan
- telepathic-guided procession
- single file march formation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dead_city

[[SECTION markdown]]
# Dead City Environment

## Environment Role
Secondary transit setting as terminal point of journey and departure location

## Architecture/Geography
- Arid territory between forty and eighty degrees south latitude
- Southwest corner near crossing of two Martian canals
- Route out across little valley before city
- Hills leading down into dead sea bottom
- Several days in comparative idleness after return

## Lighting and Atmosphere Cues
- Bright daylight for morning departure
- Clear visibility for journey observation
- Dry, dusty atmosphere typical of arid landscape
- Comparative idleness suggests quiet, still conditions

## Scale Cues and Recurring Environmental Anchors
- Accommodates ~30,000 souls population
- Large enough for 250 chariots gathering in plaza
- Route through hills and valley before city
- Terminal point of journey from incubator location

## Descriptive Noun Phrases
- arid dead city territory
- southwest canal crossing
- little valley route
- hills leading down
- dead sea bottom
- comparative idleness space
- morning departure point
- terminal journey location

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
