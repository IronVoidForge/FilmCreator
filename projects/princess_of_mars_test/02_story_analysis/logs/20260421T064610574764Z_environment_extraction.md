# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:46:10.574764+00:00
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

**Setting:** The Arizona hills and mountains; specifically a remote mining site, a high plateau with Apache tepees, and a large, ancient cave.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer, driven by a sense of duty and a search for gold. He is an experienced fighter who possesses a unique, near-immortal quality.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.

**Events:**
* **Introduction:** An elderly John Carter introduces himself, explaining his unusual longevity and his intent to record the strange events of his life, specifically the ten years he spent in an Arizona cave.
* **The Gold Discovery:** Following the Civil War, Carter and Powell discover a massive gold-bearing quartz vein in the Arizona mountains. 
* **The Separation:** To secure machinery for the mine, Powell departs for civilization while Carter stays to guard the claim.
* **The Pursuit:** Noticing suspicious movement in the valley, Carter suspects Powell is being pursued by Apaches. He arms himself and tracks the trail into the night.
* **The Skirmish:** Carter discovers a large Apache camp on a plateau. He launches a sudden, loud charge with his revolvers, causing the warriors to scatter in confusion.
* **Finding Powell:** Amidst the chaos, Carter finds Powell dead, riddled with arrows. Carter retrieves the body to prevent mutilation.
* **The Escape and the Cave:** Pursued by the Apaches, Carter flees through a mountain pass. He eventually reaches a large cave at the end of a cliffside trail. After confirming Powell is deceased, Carter enters the cave to explore.
* **The Drowsiness:** Inside the cave, Carter experiences an overwhelming, unnatural drowsiness that overcomes his physical will, leading him to collapse on the floor.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description | Role |
| :--- | :--- | :--- |
| arizona_mountain_mining_site | Rugged mountains containing gold-bearing quartz veins. | Primary |
| apache_plateau_camp | High plateau featuring tepees and open valley views. | Secondary |
| ancient_cliffside_cave | Large, mysterious cave at the end of a cliffside trail. | Primary |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountain_mining_site

[[SECTION markdown]]

# Arizona Mountain Mining Site

**Role:** Primary Setting

**Architecture & Geography:** Rugged, arid mountain terrain; steep slopes characterized by massive gold-bearing quartz veins embedded in the rock face. Remote and desolate mining claim.

**Lighting & Atmosphere:** Harsh, high-desert sunlight; dusty atmosphere with sharp shadows cast by rocky outcrops.

**Scale & Anchors:** Large-scale geological formations; prominent quartz veins serving as visual anchors for the mining site.

**Prompt Phrases:** rugged desert mountains, gold-bearing quartz veins, arid canyon walls, remote prospecting claim, sun-bleached rock.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_plateau_camp

[[SECTION markdown]]

# Apache Plateau Camp

**Role:** Secondary Setting

**Architecture & Geography:** A high, elevated plateau overlooking a wide valley; dotted with traditional Apache tepees.

**Lighting & Atmosphere:** Nighttime setting; moonlight illuminating the plateau; sense of sudden chaos and scattered movement.

**Scale & Anchors:** Expansive valley views from the plateau edge; clusters of tepees as recurring structural elements.

**Prompt Phrases:** high desert plateau, apache tepees, moonlit canyon, elevated campsite, vast valley vista.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_cliffside_cave

[[SECTION markdown]]

# Ancient Cliffside Cave

**Role:** Primary Setting

**Architecture & Geography:** A massive, cavernous interior located at the terminus of a narrow cliffside trail; deep limestone or sandstone formations.

**Lighting & Atmosphere:** Dim, subterranean lighting; heavy, unnatural atmosphere characterized by overwhelming drowsiness and stillness.

**Scale & Anchors:** Large-scale cave mouth; high ceilings; floor space large enough for movement/collapse.

**Prompt Phrases:** massive ancient cave, cliffside cavern entrance, dark subterranean chamber, limestone cave interior, oppressive atmospheric stillness.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
