# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:38:19.052810+00:00
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

Chapter id: CH005

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

**Setting:** A captive's chamber decorated with beautiful murals of Martian landscapes; a deserted city street; and the interior of a building overlooking a valley.

**Characters:**
* **The Protagonist:** An adventurous human captive attempting to test his limits and escape.
* **Sola:** A kind and sympathetic female Martian who provides food, drink, and warmth to the protagonist.
* **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for protection and hunting; it acts as a constant guardian/pursuer.
* **The Colossal Creature:** A large, white, hairless, ape-like being with a shock of bristly hair that captures the protagonist.

**Events:**
* Sola leaves the protagonist under the guard of a ferocious Martian beast that blocks the room's exit.
* The protagonist observes the room's murals and learns about Martian biology (the milk-producing plant) and the planet's moons/night cycles through narration.
* Sola returns to provide food (cheese-like substance) and drink (plant-derived milk), and later covers the sleeping protagonist with furs during the cold Martian night.
* Seeking to test the watch dog's capabilities, the protagonist attempts to leave the room. The beast follows him at a distance until they reach the edge of the city.
* The beast suddenly charges the protagonist with extreme speed. The protagonist uses his jumping ability to evade the creature and leaps into a window thirty feet above the ground.
* After successfully pulling himself onto the windowsill, the protagonist is grabbed from behind by a massive, ape-like creature and dragged into a room.
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
| captive_chamber_murals | A decorated room featuring Martian landscape murals and biological depictions. |
| deserted_martian_cityscape | An empty urban street setting with high windows and sudden verticality. |
| colossal_creature_lair | An interior room within a building overlooking a valley, used for containment. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: captive_chamber_murals

[[SECTION markdown]]

# Captive Chamber Murals

**Role:** Primary setting (Interior)

**Architecture/Geography:** A confined indoor chamber featuring walls adorned with detailed, illustrative murals. The room serves as a living textbook of Martian biology and astronomy.

**Lighting/Atmosphere:** Warmth provided by furs and food; atmosphere shifts from the intimacy of Sola's care to the tension of being guarded by a beast. Lighting is influenced by the depicted night cycles on the walls.

**Scale/Anchors:** Murals depicting milk-producing plants, Martian moons, and planetary night cycles. The presence of the Watch Dog at the threshold.

**Prompt Phrases:** decorated captive cell, martian landscape murals, biological illustrations, plant-derived milk vessels, fur-covered sleeping area, watchful predator silhouette.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deserted_martian_cityscape

[[SECTION markdown]]

# Deserted Martian Cityscape

**Role:** Transit setting (Exterior)

**Architecture/Geography:** An empty, abandoned urban street characterized by sudden elevation changes and high windows.

**Lighting/Atmosphere:** Open, exposed, and high-tension. The environment facilitates rapid movement and sudden chases.

**Scale/Anchors:** Wide streets leading to the city edge; thirty-foot vertical window ledges; high-altitude sills.

**Prompt Phrases:** deserted martian street, abandoned urban architecture, high windows, steep verticality, dusty cityscape, wide empty thoroughfare.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: colossal_creature_lair

[[SECTION markdown]]

# Colossal Creature Lair

**Role:** Secondary setting (Interior)

**Architecture/Geography:** An interior room within a building that overlooks a vast valley.

**Lighting/Atmosphere:** Dimly lit, high-stakes containment area; sense of being observed from above or through large openings.

**Scale/Anchors:** Large windows overlooking a sweeping valley; scale defined by the massive size of the ape-like creature.

**Prompt Phrases:** building interior overlooking valley, vast martian valley view, large windowed room, high-altitude containment, dim interior lighting.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
