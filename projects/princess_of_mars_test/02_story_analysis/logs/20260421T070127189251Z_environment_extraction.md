# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:01:27.189251+00:00
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
The protagonist joins Sola in a massive procession of decorated three-wheeled chariots drawn by enormous animals. The cavalcade travels across a valley and dead sea bottom to reach a remote incubator. Upon arrival, the chieftain Lorquas Ptomel and Tars Tarkas oversee the hatching process. The protagonist performs a feat of leaping over parked chariots to impress the leaders. As the young Martians emerge from the incubator, they are captured in a ritualistic gauntlet formed by women and youths. Following the ceremony, the community returns to their territory, having completed the cycle of transporting eggs from subterranean vaults to the incubator. The protagonist spends several days in idleness before beginning intensive training with Sola.

**Characters:**
- **The Protagonist:** An Earthman who has mastered Martian walking and is learning the language and telepathy; he discovers his mind is uniquely shielded from Martian telepathic reading.
- **Sola:** A female Martian who acts as a guide and foster mother to a newly hatched Martian child.
- **Tars Tarkas:** A Martian warrior/leader involved in the coordination of the hatching.
- **Lorquas Ptomel, Jed:** The enormous chieftain overseeing the incubator operations.
- **The Young Martian:** A physically perfect, four-foot-tall male captured by Sola, who becomes a rival to the protagonist during training.

**Settings:**
- **The Plaza/City:** The starting point of the journey, filled with chariots and community activity.
- **The Dead Sea Bottom:** A level expanse traversed during the procession.
- **The Incubator:** A remote, walled enclosure where Martian eggs are hatched by solar rays after five years of incubation.
- **The Martian Territory:** An arid/semi-arid region located between forty and eighty degrees south latitude, near the crossing of Martian canals.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description |
| :--- | :--- |
| martian_plaza_city | A bustling urban hub filled with decorated chariots and community activity. |
| dead_sea_bottom | A vast, level expanse of dried seabed used for long-distance processions. |
| remote_incubator_complex | A walled enclosure designed to harness solar rays for egg hatching. |
| martian_arid_territory | An arid/semi-arid landscape located near major canal crossings. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza_city

[[SECTION markdown]]

# Martian Plaza City

**Role:** Primary / Transit Setting

**Architecture & Geography:** A dense urban hub characterized by wide thoroughfares capable of accommodating massive processions. Features heavy presence of three-wheeled chariots and large animal enclosures.

**Lighting & Atmosphere:** High activity, bustling communal atmosphere; bright, open sunlight typical of a central settlement.

**Scale & Anchors:** Large-scale chariot parking areas; decorated ceremonial vehicles; high density of Martian community members.

**Prompt Phrases:** bustling martian plaza, decorated three-wheeled chariots, large animal herds, urban procession hub, ancient martian architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_sea_bottom

[[SECTION markdown]]

# Dead Sea Bottom

**Role:** Transit Setting

**Architecture & Geography:** A vast, level, and featureless expanse of dried seabed. Extremely flat terrain providing unobstructed sightlines.

**Lighting & Atmosphere:** Harsh, direct sunlight; expansive, desolate, and silent atmosphere broken only by the movement of processions.

**Scale & Anchors:** Massive scale; horizon-to-horizon flatness; long, linear procession paths.

**Prompt Phrases:** vast dried seabed, level martian desert, dead sea floor, endless flat expanse, sun-bleached basin.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: remote_incubator_complex

[[SECTION markdown]]

# Remote Incubator Complex

**Role:** Primary Setting

**Architecture & Geography:** A remote, walled enclosure specifically engineered for biological processes. Features specialized structures designed to capture and focus solar rays onto Martian eggs.

**Lighting & Atmosphere:** Intense solar illumination; ritualistic and ceremonial atmosphere; heat-focused environment.

**Scale & Anchors:** Walled perimeter; central hatching zones; large groups of observers (chieftains, youths, women) forming ritual gauntlets.

**Prompt Phrases:** walled martian incubator, solar ray hatching chamber, ritualistic enclosure, egg incubation site, sun-drenched ceremonial complex.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_arid_territory

[[SECTION markdown]]

# Martian Arid Territory

**Role:** Secondary Setting

**Architecture & Geography:** An arid to semi-arid landscape located in the southern latitudes. Defined by its proximity to the intersection of major Martian canals.

**Lighting & Atmosphere:** Dry, dusty atmosphere; bright, harsh lighting characteristic of low-latitude Martian plains.

**Scale & Anchors:** Intersection of massive canal systems; vast stretches of dry land; sparse vegetation or landmarks.

**Prompt Phrases:** arid martian landscape, southern latitude plains, canal intersection, semi-arid martian desert, sun-baked terrain.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
