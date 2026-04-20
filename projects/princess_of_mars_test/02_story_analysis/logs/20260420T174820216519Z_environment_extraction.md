# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:48:20.217021+00:00
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
The protagonist accompanies Sola and a massive military cavalcade—consisting of two hundred decorated chariots drawn by enormous beasts—to a remote incubator located on a dead sea bottom. Upon arrival, the chieftain Lorquas Ptomel and Tars Tarkas oversee the hatching process. The protagonist demonstrates his physical prowess by leaping over parked chariots to impress the leaders. As the young Martians emerge from the incubator, they are captured in a ritualistic gauntlet formed by women and youths. The protagonist observes the cold, utilitarian nature of Martian child-rearing: offspring are communal, raised by foster mothers to be warriors, and any defective specimens are promptly killed. Following the ceremony, the community returns to their territory, and the protagonist spends time under Sola's tutelage, learning the language and honing his telepathic skills.

**Characters:**
* **Protagonist:** An Earthman who has mastered Martian walking and is rapidly learning the language and telepathy; he discovers his mind is unreadable by Martians.
* **Sola:** A female Martian who acts as a guide and foster mother to a newly hatched male Martian, while also caring for the protagonist.
* **Tars Tarkas:** A Martian warrior/leader who interacts with the protagonist.
* **Lorquas Ptomel (Jed):** An enormous chieftain who oversees the incubator ceremony.
* **The Young Martian:** A physically perfect, four-foot-tall male captured by Sola; he becomes a rival to the protagonist in their shared education.

**Settings:**
* **The Plaza:** The central hub of the Martian community where chariots are harnessed.
* **The Dead Sea Bottom:** A level expanse where the incubator is located and where the hatching ceremony takes place.
* **The Incubator:** A remote, specialized structure used to hatch eggs via solar rays after a five-year incubation period.
* **The Dead City:** The location where the protagonist resides during his periods of idleness and education.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH007

| Asset ID | Description |
| :--- | :--- |
| dead_sea_bottom_basin | The vast, level expanse containing the incubator and ceremonial grounds. |
| incubator_structure | The specialized solar-ray facility for hatching Martian eggs. |
| martian_plaza | The central hub of the community used for chariot harnessing and assembly. |
| dead_city_quarters | The residential and educational area within the ruins. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_sea_bottom_basin

[[SECTION markdown]]

# Dead Sea Bottom Basin

**Role:** Primary ceremonial setting.

**Geography:** A vast, level expanse of a dried-up seabed; flat, desolate, and expansive.

**Lighting and Atmosphere:** Harsh, direct solar exposure; open sky; sense of immense emptiness and ritualistic gravity.

**Scale Cues:** Massive military cavalcade of two hundred chariots; enormous beasts; wide horizons.

**Prompt Phrases:** level desiccated seabed, vast salt flat expanse, desolate basin floor, ceremonial wasteland, sun-drenched void.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: incubator_structure

[[SECTION markdown]]

# Incubator Structure

**Role:** Primary functional setting.

**Architecture:** A remote, specialized structure designed to capture and focus solar rays; utilitarian and ancient in appearance.

**Lighting and Atmosphere:** Concentrated beams of light; intense solar heat; clinical and ritualistic atmosphere.

**Scale Cues:** Large enough to house multiple eggs/specimens; central focal point of the basin.

**Prompt Phrases:** solar-ray incubator, specialized hatching monolith, concentrated sunlight chamber, ancient biological facility, sun-focused stone structure.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza

[[SECTION markdown]]

# Martian Plaza

**Role:** Secondary transit and assembly setting.

**Architecture:** A central hub within the community; organized for heavy transport and animal harnessing.

**Lighting and Atmosphere:** Busy, communal, high-activity lighting; dusty and functional.

**Scale Cues:** Rows of decorated chariots; large beasts of burden; crowds of warriors and youths.

**Prompt Phrases:** chariot assembly plaza, martial hub, bustling Martian courtyard, harness station, ceremonial gathering ground.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_city_quarters

[[SECTION markdown]]

# Dead City Quarters

**Role:** Secondary residential and educational setting.

**Architecture:** Ruins of a former civilization; repurposed for habitation and study.

**Lighting and Atmosphere:** Shaded, quiet, contemplative; sense of ancient decay mixed with current utility.

**Scale Cues:** Domestic scale; intimate spaces for tutelage and telepathic training.

**Prompt Phrases:** ruined Martian city, ancient stone dwellings, shadowed urban ruins, repurposed archaeological site, quiet scholar's quarters.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
