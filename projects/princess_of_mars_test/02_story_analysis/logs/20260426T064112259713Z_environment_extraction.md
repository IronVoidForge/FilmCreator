# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:41:12.259713+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH007

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Events:**
The protagonist joins Sola and a massive cavalcade of two hundred and fifty decorated chariots drawn by enormous animals to witness the hatching at a remote incubator. Upon arrival, the protagonist performs a feat of physical prowess (leaping over parked chariots) for the chieftain Lorquas Ptomel. The community executes a ritualized "capture" where women and youths form a gauntlet to collect the newly hatched, three-to-four-foot-tall Martians as they emerge from the incubator. Following the ceremony, the warriors transport eggs from subterranean vaults to the incubator for their next five-year incubation cycle. Back at the dead city, the protagonist undergoes intensive training in Martian language and telepathy under Sola's tutelage.

**Characters:**
* **The Protagonist:** An Earthman learning Martian customs; discovers he possesses a unique mental defense that prevents Martians from reading his thoughts.
* **Sola:** A female Martian who acts as the protagonist's guide and foster mother to a newly hatched male.
* **Tars Tarkas:** A warrior/chief involved in the coordination of the incubator ceremony.
* **Lorquas Ptomel (Jed):** The enormous principal chieftain overseeing the proceedings.
* **The Young Martian:** A physically perfect, four-foot-tall male captured during the hatching; becomes a rival to the protagonist during training.

**Settings:**
* **The Plaza:** The central gathering point of the Martian community.
* **The Dead Sea Bottom/Valley:** The terrain traversed by the massive chariot procession.
* **The Incubator:** A remote, walled enclosure where Martian eggs hatch after five years of exposure to sun rays.
* **The Dead City:** The protagonist's base of operations and site of his ongoing education.

**Key Concepts:**
* **Telepathy:** The universal Martian language used for communication between species and for guiding animals without bridles.
* **Martian Child-Rearing:** A pitiless system where children are communal property, raised by foster mothers to be warriors, with no concept of parental love.
* **Biological Selection:** A strict process involving the destruction of "imperfect" eggs and regulated birth rates to manage dwindling resources on a dying planet.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [dead_sea_bottom_valley](dead_sea_bottom_valley)
- [the_incubator_enclosure](the_incubator_enclosure)
- [the_dead_city](the_dead_city)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_sea_bottom_valley

[[SECTION markdown]]

# Dead Sea Bottom Valley

**Role:** Transit setting / Processional route.

**Geography:** A vast, desolate valley floor characterized by the dried remains of an ancient sea; wide enough to accommodate a cavalcade of two hundred and fifty decorated chariots.

**Lighting and Atmosphere:** Harsh, exposed Martian sunlight; dusty and windswept; sense of immense, empty scale.

**Scale Cues:** Massive animal-drawn chariots; long processions stretching across the horizon.

**Prompt Phrases:** Desiccated seabed, vast salt flats, ancient valley floor, sweeping desert vistas, chariot procession path.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: the_incubator_enclosure

[[SECTION markdown]]

# The Incubator Enclosure

**Role:** Primary ritual setting.

**Geography:** A remote, walled enclosure designed to capture and focus sun rays; contains a central area for egg hatching and communal gathering.

**Lighting and Atmosphere:** Intense solar exposure; bright, direct light focused on the hatching site; ceremonial and high-energy atmosphere.

**Scale Cues:** Walled perimeter; large groups of Martians forming human gauntlets; three-to-four-foot tall hatchlings emerging from central points.

**Prompt Phrases:** Sun-drenched walled enclosure, ritualistic hatching site, solar exposure zone, communal gathering plaza, Martian egg nursery.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: the_dead_city

[[SECTION markdown]]

# The Dead City

**Role:** Primary base of operations / Secondary training setting.

**Geography:** A ruined, ancient urban center; serves as a site for intensive study and telepathic training.

**Lighting and Atmosphere:** Somber, quiet, and scholarly; shadows cast by decaying architecture; sense of isolation and antiquity.

**Scale Cues:** Large-scale ruins; interior spaces used for language and mental tutelage.

**Prompt Phrases:** Ruined Martian metropolis, ancient stone structures, desolate urban landscape, silent city streets, crumbling architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
