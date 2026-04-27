# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:14:19.362976+00:00
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

Chapter id: CH013

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

**Setting:** The Yellow Castle in the Land of the West; a rocky plain; a tall tree with a smooth trunk.

**Characters:** Dorothy, the Cowardly Lion, the Tin Woodman, the Scarecrow, the Winkies (Yellow People), and the Winged Monkeys (mentioned).

**Events:**
- **Liberation:** Following the death of the Wicked Witch, Dorothy frees the Cowardly Lion from his prison and declares the Winkies free from slavery. The Winkies celebrate their freedom with a feast.
- **Rescuing the Tin Woodman:** Dorothy and the Lion lead a group of Winkies to a rocky plain where they find the battered and rusted Tin Woodman. They carry him back to the Yellow Castle, where Winkie tinsmiths spend three days and nights repairing his body, leaving him with several patches but fully functional.
- **Rescuing the Scarecrow:** The group searches for the Scarecrow and finds his clothes discarded in a tall tree by the Winged Monkeys. Using a newly repaired axe (featuring a gold handle and polished blade), the Tin Woodman chops down the tree. The group retrieves the clothes, stuffs them with fresh straw, and restores the Scarecrow.
- **Departure Preparations:** Reunited and rested, the group decides to return to the Emerald City to claim their rewards from the Wizard. 
- **Farewell Gifts:** As they prepare to leave, the Winkies present the travelers with precious gifts: golden collars for Toto and the Lion, a diamond bracelet for Dorothy, a gold-headed walking stick for the Scarecrow, and a jewel-encrusted silver oil-can for the Tin Woodman.
- **The Golden Cap:** While gathering food, Dorothy discovers the Golden Cap in the Witch's cupboard. Finding it pretty, she decides to wear it as she travels. The group sets off toward the Emerald City.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [yellow_castle](#yellow_castle)
- [rocky_plain](#rocky_plain)
- [tall_tree_location](#tall_tree_location)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: yellow_castle

[[SECTION markdown]]

# Yellow Castle

**Role:** Primary setting; seat of power in the Land of the West.

**Architecture/Geography:** A massive, imposing structure characterized by its monochromatic yellow color palette. It serves as a hub for Winkie activity and repair workshops.

**Lighting and Atmosphere:** Celebratory yet formal; bright, golden hues reflecting off surfaces; atmosphere of liberation and industriousness (tinsmithing).

**Scale Cues:** Large-scale fortress capable of housing large feasts and specialized artisan workshops.

**Descriptive Noun Phrases:** Monochromatic yellow citadel, Winkie stronghold, golden halls, industrial repair workshop, celebratory feast hall.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: rocky_plain

[[SECTION markdown]]

# Rocky Plain

**Role:** Secondary setting; transit and discovery location.

**Architecture/Geography:** An expansive, rugged terrain defined by scattered rock formations and uneven ground.

**Lighting and Atmosphere:** Harsh, exposed sunlight; desolate and weathered; a place of abandonment where the Tin Woodman was found.

**Scale Cues:** Wide-open vistas; vast stretches of stone and earth.

**Descriptive Noun Phrases:** Desolate rocky expanse, sun-bleached stone plain, rugged wasteland, scattered boulders.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: tall_tree_location

[[SECTION markdown]]

# Tall Tree Location

**Role:** Secondary setting; specific landmark.

**Architecture/Geography:** A singular, prominent tree featuring a notably smooth trunk, standing as a landmark within the landscape.

**Lighting and Atmosphere:** Dappled light through foliage; sense of previous disturbance (discarded clothes).

**Scale Cues:** Verticality contrasting with the surrounding plains; a distinct environmental anchor.

**Descriptive Noun Phrases:** Smooth-barked tall tree, solitary landmark tree, vertical forest element.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
