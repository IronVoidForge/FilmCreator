# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:33:09.687284+00:00
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

Chapter id: CH022

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

**Setting:** A rocky hill inhabited by Hammer-Heads and the lush, red-themed Country of the Quadlings.

**Characters:** Dorothy, Scarecrow, Tin Woodman, Cowardly Lion, Toto, Hammer-Heads (armless creatures with projectile heads), Winged Monkeys, a Farmer's Wife, Castle Guards, and Glinda (mentioned).

**Events:**
- The travelers attempt to climb a rocky hill but are intercepted by the Hammer-Heads, who guard the territory.
- The Scarecrow and the Lion are both knocked down the hill by the Hammer-Heads' ability to shoot their heads forward like projectiles.
- Realizing they cannot fight the creatures physically, Dorothy uses the Golden Cap to summon the Winged Monkeys.
- The Winged Monkeys fly the travelers over the hill, bypassing the frustrated Hammer-Heads, and deposit them in the Country of the Quadlings.
- Upon arrival, the group observes the red-colored aesthetic of the Quadling land and receives a meal from a kind farmer's wife.
- The travelers follow directions to Glinda's castle, where they are met by guards in red uniforms and granted immediate entry to see the Good Witch.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [rocky_hill_territory](rocky_hill_territory)
- [quadling_countryside](quadling_countryside)
- [glindas_castle_approach](glindas_castle_approach)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: rocky_hill_territory

[[SECTION markdown]]

# Rocky Hill Territory

**Role:** Secondary / Obstacle Setting

**Architecture or Geography:** A steep, rugged, and uneven rocky hill. The terrain is characterized by hard surfaces and difficult climbing paths that serve as a natural fortification for inhabitants.

**Lighting and Atmosphere Cues:** Harsh, direct sunlight; exposed and unshielded landscape; sense of physical struggle and confrontation.

**Scale Cues and Recurring Environmental Anchors:** Steep inclines; jagged rock outcroppings; narrow pathways suitable for ambush.

**Descriptive Noun Phrases:** Rugged rocky slope, steep stone incline, jagged hill terrain, defensive rocky outcrop.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: quadling_countryside

[[SECTION markdown]]

# Quadling Countryside

**Role:** Primary Setting

**Architecture or Geography:** Lush, fertile landscape characterized by a pervasive red-themed aesthetic. Rolling hills and greenery that appear saturated with crimson tones.

**Lighting and Atmosphere Cues:** Warm, vibrant lighting; soft, lush atmosphere; heavy saturation of red hues in the flora and soil.

**Scale Cues and Recurring Environmental Anchors:** Expansive vistas; rolling red hills; pastoral farmsteads.

**Descriptive Noun Phrases:** Crimson-hued landscape, lush red countryside, saturated scarlet meadows, vibrant quadling terrain.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: glindas_castle_approach

[[SECTION markdown]]

# Glinda's Castle Approach

**Role:** Secondary / Destination Setting

**Architecture or Geography:** Formal entrance to a grand castle; structured and orderly compared to the wild hills. Features guarded entry points.

**Lighting and Atmosphere Cues:** Stately and imposing; bright, clear visibility; sense of authority and magical presence.

**Scale Cues and Recurring Environmental Anchors:** Large-scale castle gates; uniformed guards; formal architectural boundaries.

**Descriptive Noun Phrases:** Grand castle entrance, red-uniformed guard posts, majestic fortress approach, formal palace threshold.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
