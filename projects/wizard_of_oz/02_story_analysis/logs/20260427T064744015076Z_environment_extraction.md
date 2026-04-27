# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:47:44.015076+00:00
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
Project slug: wizard_of_oz

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

**Setting:** A small, one-room farmhouse situated in the middle of the vast, gray, and sun-bleached Kansas prairies. The landscape is flat and devoid of color or trees.

**Characters:**
- **Dorothy:** An orphan girl who maintains a sense of joy and laughter despite her surroundings.
- **Aunt Em:** Dorothy's aunt; once pretty, she has become thin, gaunt, and gray due to the harsh life on the farm.
- **Uncle Henry:** Dorothy's uncle; a hardworking, stern, and solemn farmer.
- **Toto:** Dorothy's small, energetic black dog.

**Events:**
- The family lives in a state of constant vigilance against the weather, specifically cyclones.
- A massive storm approaches from both the north and south, signaling an imminent cyclone.
- As Uncle Henry goes to tend to the livestock, Aunt Em directs Dorothy to seek shelter in the underground cyclone cellar.
- Before Dorothy can reach the trap door, a powerful cyclone hits the house, lifting it off the ground and carrying it into the air.
- Inside the flying house, Dorothy experiences the terrifying but eventually rhythmic motion of being carried by the wind.
- After a brief moment of panic where Toto nearly falls through the open trap door, Dorothy secures him and settles down.
- As the hours pass, Dorothy overcomes her initial fright and eventually falls asleep while the house is carried miles away by the storm.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [kansas_prairie_landscape](kansas_prairie_landscape)
- [farmhouse_interior_and_cellar](farmhouse_interior_and_cellar)
- [flying_house_interior](flying_house_interior)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: kansas_prairie_landscape

[[SECTION markdown]]

# Kansas Prairie Landscape

**Role:** Primary / Background Setting

**Geography:** Vast, flat, and featureless plains. A sun-bleached expanse of gray tones with no trees or significant topographical variation.

**Lighting and Atmosphere:** Harsh, bright, sun-bleached light; oppressive atmosphere; shifting into dark, turbulent storm skies as the cyclone approaches.

**Scale Cues:** Infinite horizon lines; sense of isolation and exposure to the elements.

**Descriptive Noun Phrases:** Gray prairie expanse, flat sun-bleached plains, desolate horizon, approaching cyclonic storm clouds, wind-swept dust.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: farmhouse_interior_and_cellar

[[SECTION markdown]]

# Farmhouse Interior and Cellar

**Role:** Primary Setting

**Architecture:** A small, one-room farmhouse; rustic, utilitarian construction. Includes an underground cyclone cellar accessed via a trap door in the floor.

**Lighting and Atmosphere:** Dim, enclosed, dusty interior; sense of constant vigilance and vulnerability to weather.

**Scale Cues:** Cramped, single-room living space; subterranean shelter.

**Descriptive Noun Phrases:** One-room farmhouse, rustic wooden interior, underground cyclone cellar, heavy trap door, weathered farm dwelling.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: flying_house_interior

[[SECTION markdown]]

# Flying House Interior

**Role:** Transit Setting

**Architecture:** The interior of the farmhouse, now detached from its foundation and airborne.

**Lighting and Atmosphere:** Chaotic, rhythmic motion; turbulent wind sounds; shifting light as the house rotates through storm clouds; sense of terrifying kinetic energy transitioning into a rhythmic lull.

**Scale Cues:** Enclosed space subject to violent external forces; open trap door creating a dangerous threshold.

**Descriptive Noun Phrases:** Airborne farmhouse interior, tilting wooden floors, wind-rattled walls, swirling storm light, oscillating cabin motion.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
