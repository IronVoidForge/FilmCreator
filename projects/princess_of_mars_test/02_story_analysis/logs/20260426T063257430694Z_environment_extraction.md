# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:32:57.431195+00:00
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
The Arizona hills and mountains; specifically a remote gold-bearing quartz vein, a high plateau filled with Apache tepees, and a large, ancient cave located on a narrow trail between a cliff and a ravine.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer and seasoned fighter. He is characterized by an instinctive sense of duty that often overrides his survival instinct.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.
* **Apache Warriors:** A large group (approximately five hundred) encountered during a pursuit.

**Events:**
* **The Discovery:** Carter and Powell discover a massive gold vein in Arizona in 1865. They decide that Powell will return to civilization to secure machinery while Carter holds the claim.
* **The Pursuit:** After Powell departs, Carter observes suspicious movement in the valley. Suspecting an Apache ambush, he pursues the trail, discovering tracks of galloping ponies.
* **The Skirmish:** Carter discovers a large Apache camp on a plateau. He launches a sudden, violent charge with his revolvers, causing the warriors to scatter in confusion.
* **Finding Powell:** Amidst the chaos, Carter finds Powell dead, riddled with arrows. Carter retrieves the body to prevent mutilation and flees the plateau under heavy fire.
* **The Escape and the Cave:** While fleeing, Carter's horse takes a wrong turn, leading him away from the pursuit and toward a high cliff. He discovers a large, ancient cave at the end of a trail.
* **The End of the Journey:** After confirming Powell is dead, Carter enters the cave to explore. Overcome by extreme fatigue and a mysterious drowsiness, he collapses on the cave floor, marking the beginning of his ten-year disappearance.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH001

| Asset ID | Description |
| :--- | :--- |
| arizona_quartz_vein_location | Remote gold-bearing quartz vein in the Arizona hills. |
| apache_plateau_camp | High plateau featuring Apache tepees and open valley views. |
| ancient_cliffside_cave | Large, ancient cave located on a narrow trail between cliff and ravine. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location

[[SECTION markdown]]

# Arizona Quartz Vein Location

**Role:** Primary (Discovery)

**Geography:** Remote, rugged Arizona hills and mountains; characterized by rocky terrain and exposed geological formations containing massive gold-bearing quartz veins.

**Lighting & Atmosphere:** Harsh, high-desert sunlight; dry, dusty atmosphere; sense of isolation and frontier wilderness.

**Scale & Anchors:** Vast mountain ranges; localized mineral deposits; scattered desert scrub.

**Prompt Phrases:** rugged Arizona mountains, gold-bearing quartz vein, rocky desert hills, sun-bleached terrain, remote prospecting site.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_plateau_camp

[[SECTION markdown]]

# Apache Plateau Camp

**Role:** Secondary (Conflict)

**Geography:** A high, expansive plateau overlooking a valley; open terrain suitable for large encampments.

**Lighting & Atmosphere:** Wide-open sky; dusty and chaotic during skirmish; sense of exposure to the elements and attackers.

**Scale & Anchors:** Large scale; hundreds of Apache tepees; wide valley vistas; galloping pony tracks.

**Prompt Phrases:** high desert plateau, Apache tepee camp, expansive valley view, dusty highland plains, large-scale encampment.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_cliffside_cave

[[SECTION markdown]]

# Ancient Cliffside Cave

**Role:** Primary (Transition/End)

**Geography:** A large, ancient cave situated at the terminus of a narrow trail; positioned between a steep cliff face and a deep ravine.

**Lighting & Atmosphere:** Dim, subterranean lighting; cool, heavy atmosphere; sense of enclosure and mysterious drowsiness; shadows cast by high cliff walls.

**Scale & Anchors:** Massive cave interior; narrow mountain trail; sheer cliff walls; deep ravine edge.

**Prompt Phrases:** large ancient cave, narrow cliffside trail, rocky ravine, dark cavernous interior, limestone cliff shelter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
