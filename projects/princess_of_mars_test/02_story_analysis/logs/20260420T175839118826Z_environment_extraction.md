# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:58:39.118826+00:00
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

Chapter id: CH014

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

John Carter struggles with his unspoken feelings for Dejah Thoris, fearing that a confession might burden her further; however, a misunderstanding leads to a moment of tension where Dejah withdraws from him in silent dignity. As the group prepares to depart for Thark, Carter protests the heavy chains Sarkoja has placed on Dejah's chariot, but Tars Tarkas defends it as a security measure, though he later shows a hint of compassion by unfastening her fetters during a campout. Amidst this, Carter notes the intense hatred directed toward him by Sarkoja and the warrior Zad.

The tension escalates when Dejah Thoris expresses her contempt for Carter through Sola, leaving Carter feeling profoundly homesick for Earth. During the march toward Thark, the party destroys an incubator belonging to the green men of Warhoon. The journey takes a violent turn during a rest halt when Zad provokes Carter into a formal duel. As they fight, Sarkoja uses a mirror to catch the sun and blind Carter, attempting to aid Zad in a killing blow. In the ensuing chaos, Sola heroically leaps to shield Dejah Thoris from Sarkoja's dagger, but the distraction allows Zad to land a fatal thrust in Carter's chest, leaving him fading into unconsciousness.
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
| martian_march_route | The rugged, desolate landscape traversed by the Thark party during their journey toward Thark. |
| warhoon_outpost_site | A temporary encampment or waypoint featuring green men technology and incubators. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_march_route

[[SECTION markdown]]

# Martian March Route

**Role:** Transit Setting

**Geography:** Rugged, desolate terrain characteristic of the Barsoomian wilderness; uneven ground suitable for heavy chariot movement and marching parties.

**Lighting and Atmosphere:** Harsh, direct sunlight; high-contrast shadows; dusty and arid atmosphere prone to sudden visual disruptions (e.g., reflected glare).

**Scale and Anchors:** Vast, open vistas interrupted by rocky outcrops or temporary camp sites; recurring presence of Thark war chariots and heavy chains.

**Prompt Phrases:** Desolate Martian wasteland, rugged red terrain, harsh sunlight, dusty horizon, wide-angle wilderness, arid Barsoomian landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_outpost_site

[[SECTION markdown]]

# Warhoon Outpost Site

**Role:** Secondary Setting

**Geography:** A localized site within the march route, containing remnants of Green Man technology.

**Lighting and Atmosphere:** Exposed to the elements; harsh sunlight; sense of sudden violence and disruption.

**Scale and Anchors:** Small-scale technological installations; presence of green men incubators; temporary rest halt location.

**Prompt Phrases:** Green man encampment, destroyed incubator, primitive alien technology, makeshift desert outpost, site of skirmish.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
