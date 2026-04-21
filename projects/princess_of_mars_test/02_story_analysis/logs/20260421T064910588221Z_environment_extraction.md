# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:49:10.588221+00:00
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

**Setting:**
The Arizona hills and mountains; specifically a remote gold-bearing quartz vein, a high plateau with an Apache camp, and a large, ancient cave located on a narrow trail near a cliffside.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer and soldier of fortune. He is characterized by a compulsive sense of duty and a tendency to act before fully processing danger.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.
* **Apache Warriors:** A large group of hostile warriors who ambush Powell.

**Events:**
* **Introduction:** An elderly John Carter introduces himself, explaining his unique immortality/aging process and his intent to record his life story before his final death.
* **The Discovery:** Carter and Powell discover a massive gold vein in Arizona in 1865. They decide Powell will return to civilization to fetch machinery while Carter guards the claim.
* **The Ambush:** After Powell departs, Carter notices suspicious movement in the valley. Suspecting an Apache ambush, he pursues the trail. He discovers a large Apache camp on a plateau and engages them in a chaotic skirmish.
* **The Aftermath:** During the fight, Carter finds Powell dead, riddled with arrows. Carter retrieves the body and flees the pursuing warriors.
* **The Cave:** While attempting to escape, Carter's horse takes him to a narrow cave entrance on a high trail. After confirming Powell is deceased, Carter enters the cave to scout it.
* **The Collapse:** Inside the large, ancient chamber, Carter experiences an overwhelming, unnatural drowsiness. Despite his efforts to stay awake and remain alert to pursuit, he loses consciousness and collapses on the cave floor.
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
| arizona_gold_vein_claim | Remote quartz vein in the Arizona hills/mountains. | Primary (Discovery) |
| apache_plateau_camp | High plateau hosting a large Apache settlement. | Secondary (Conflict) |
| ancient_cliffside_cave | Large, ancient chamber located on a narrow high trail. | Primary (Transition/Inciting Incident) |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_gold_vein_claim

[[SECTION markdown]]

# Arizona Gold Vein Claim

**Role:** Primary setting for discovery and initial character establishment.

**Geography:** Rugged, remote Arizona hills and mountains; characterized by rocky terrain and exposed geological formations. Features a massive, prominent gold-bearing quartz vein embedded in the hillside.

**Lighting & Atmosphere:** Harsh, high-desert sunlight; dry, dusty atmosphere with intense heat shimmer over the rocks.

**Scale & Anchors:** Vast, desolate mountain vistas; the singular, glittering quartz vein serves as the central visual anchor.

**Prompt Phrases:** rugged desert mountains, exposed quartz vein, gold-bearing rock, arid Arizona hills, sun-bleached granite, remote prospecting site.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_plateau_camp

[[SECTION markdown]]

# Apache Plateau Camp

**Role:** Secondary setting for combat and ambush sequence.

**Geography:** A high, elevated plateau overlooking the valley trails; surrounded by steep drops and rocky outcrops.

**Lighting & Atmosphere:** High-contrast shadows from midday sun; dusty, chaotic atmosphere filled with movement and tension.

**Scale & Anchors:** Large-scale settlement footprint on a flat highland; anchored by the surrounding cliff edges and the descent into the valley below.

**Prompt Phrases:** high desert plateau, elevated encampment, rocky highland, overlooking valley, ambush terrain, sun-drenched mesa.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_cliffside_cave

[[SECTION markdown]]

# Ancient Cliffside Cave

**Role:** Primary setting for the inciting incident and transition.

**Geography:** A large, ancient subterranean chamber accessed via a narrow entrance on a high, precarious cliffside trail.

**Lighting & Atmosphere:** Transition from bright exterior sunlight to deep, oppressive interior shadows; heavy, unnatural stillness; dim, diffused light filtering through the entrance; sense of overwhelming drowsiness/stagnant air.

**Scale & Anchors:** Massive internal chamber scale; narrow, claustrophobic cave mouth; ancient stone walls and floor.

**Prompt Phrases:** massive ancient cavern, narrow cliffside entrance, subterranean chamber, deep shadows, limestone cave interior, oppressive stillness, high-altitude cave.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
