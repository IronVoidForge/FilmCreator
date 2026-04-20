# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:39:54.596323+00:00
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

Chapter id: CH001

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

**Setting:** The Arizona hills and mountains; specifically a remote gold-bearing quartz vein, a high plateau filled with Apache tepees, and a large, mysterious cave near a cliffside trail.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer and soldier of fortune. He is characterized by an instinctive sense of duty and a physical resilience that borders on the supernatural.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.

**Events:**
* **The Discovery:** Carter and Powell locate a massive gold vein in the Arizona mountains in 1865.
* **The Departure:** Powell departs to fetch machinery, leaving Carter to guard the claim.
* **The Pursuit:** Noticing suspicious movement in the valley, Carter tracks what he believes to be an Apache raiding party. He discovers signs of a struggle and follows the trail through the night.
* **The Skirmish:** Carter stumbles upon a large Apache camp on a plateau. He launches a sudden, aggressive charge with his revolvers, causing the warriors to scatter in confusion.
* **The Aftermath:** Amidst the chaos, Carter finds Powell dead, riddled with arrows. He retrieves the body and flees the pursuing warriors.
* **The Cave:** While attempting to evade capture, Carter's horse leads him to a large cave at the end of a cliffside trail. After confirming Powell is deceased, Carter enters the cave to scout it. 
* **The Collapse:** Inside the cave, Carter experiences an overwhelming, unnatural drowsiness and loses consciousness on the floor.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH001

| Asset ID | Description | Role |
| :--- | :--- | :--- |
| arizona_mountain_quartz_vein | Remote gold-bearing quartz vein in the Arizona hills. | Primary (Discovery) |
| apache_plateau_camp | High plateau featuring Apache tepees and valley views. | Secondary (Skirmish) |
| cliffside_cave_system | Large, mysterious cave at the end of a cliffside trail. | Primary (Climax/Transition) |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountain_quartz_vein

[[SECTION markdown]]

# Arizona Mountain Quartz Vein

**Role:** Primary discovery setting.

**Geography:** Rugged, remote Arizona hills and mountains; characterized by rocky outcrops and exposed mineral deposits.

**Lighting & Atmosphere:** Harsh, high-desert sunlight; dry, dusty air; sense of isolation and rugged frontier prospecting.

**Scale & Anchors:** Massive gold-bearing quartz veins embedded in mountain rock; scattered mining tools/prospecting gear.

**Prompt Phrases:** remote Arizona mountains, gold-bearing quartz vein, rocky desert hills, 1865 prospecting site, sun-bleached granite, mineralized rock faces.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_plateau_camp

[[SECTION markdown]]

# Apache Plateau Camp

**Role:** Secondary skirmish setting.

**Geography:** A high, expansive plateau overlooking a valley; open terrain suitable for large encampments.

**Lighting & Atmosphere:** Nighttime/Twilight; shadows cast by campfires; chaotic atmosphere of sudden movement and scattered warriors.

**Scale & Anchors:** Clusters of Apache tepees; wide horizon lines; valley floor visible below the plateau edge.

**Prompt Phrases:** high desert plateau, Apache tepee encampment, twilight mountain vista, scattered campfires, rugged highland terrain.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cliffside_cave_system

[[SECTION markdown]]

# Cliffside Cave System

**Role:** Primary transition setting.

**Geography:** A large, cavernous opening located at the terminus of a narrow cliffside trail; deep interior chambers.

**Lighting & Atmosphere:** Transition from bright daylight to oppressive, heavy darkness; unnatural, heavy atmosphere inducing drowsiness; cool, damp cave air.

**Scale & Anchors:** Massive limestone or sandstone cave mouth; steep cliff edges; cavernous floor space; echoing silence.

**Prompt Phrases:** large mysterious cave, cliffside trail entrance, dark cavern interior, heavy atmospheric haze, subterranean chamber, rocky cave floor.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
