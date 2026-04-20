# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:42:08.009749+00:00
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

Chapter id: CH003

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
A vast, circular basin on Mars covered in a thick, yellowish, moss-like vegetation. The landscape features low hills, quartz-bearing rock outcroppings, and a specific glass-roofed enclosure acting as an incubator for Martian life.

**Characters:**
* **The Protagonist:** An Earthman, currently naked and unarmed, possessing superhuman agility and leaping ability due to the low Martian gravity.
* **Martian Warriors:** A group of twenty massive beings (approx. 15 feet tall) with multiple arms and red eyes, riding large, four-legged, multi-limbed mounts. They are heavily armed with long spears and advanced long-range rifles.
* **The Martian Leader:** The head of the hunting party; he demonstrates a capacity for peaceful diplomacy by approaching the protagonist unarmed to offer a gesture of friendship.
* **Hatchlings:** Newly emerged, grotesque creatures from large white eggs, characterized by yellowish-green skin, six limbs, and protruding eyes.

**Key Events:**
1. **Awakening on Mars:** The protagonist wakes in a Martian basin and discovers the effects of low gravity, finding that even simple walking results in uncontrolled hopping.
2. **Discovery of the Incubator:** While exploring for water, the protagonist finds a glass-roofed structure containing large white eggs and observes the hatching of strange, multi-limbed creatures.
3. **The Ambush:** A party of twenty Martian warriors approaches silently. The protagonist is nearly killed by the tip of a massive spear held by the lead warrior.
4. **The Great Leap:** To escape the immediate threat, the protagonist utilizes the low gravity to perform a massive 30-foot leap, landing safely on the far side of the incubator. This display of agility transforms the Martians' view of him from prey to a "wonderful discovery."
5. **Diplomatic Contact:** The Martian leader dismounts and approaches the protagonist unarmed. He offers a metal armlet as a sign of peace; the protagonist accepts it, signaling his intent for friendship.
6. **Departure:** The leader escorts the protagonist away, placing him on the back of one of the Martian mounts to join the retreating cavalcade heading toward the distant hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

- [martian_basin_landscape](#martian_basin_landscape)
- [martian_incubator_enclosure](#martian_incubator_enclosure)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_basin_landscape

[[SECTION markdown]]

# Martian Basin Landscape

**Role:** Primary setting.

**Geography:** A vast, circular basin featuring low hills and prominent quartz-bearing rock outcroppings. The ground is covered in a thick, yellowish, moss-like vegetation.

**Lighting and Atmosphere:** Alien and expansive; the atmosphere supports low-gravity physics allowing for extreme leaping.

**Scale Cues:** Vast, wide-angle landscape with distant, rolling hills.

**Descriptive Phrases:** yellowish mossy terrain, quartz-veined rock outcroppings, low Martian hills, circular basin floor, alien vegetation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_incubator_enclosure

[[SECTION markdown]]

# Martian Incubator Enclosure

**Role:** Secondary setting / Point of interest.

**Architecture:** A specific, glass-roofed enclosure/structure designed to act as an incubator for Martian life.

**Lighting and Atmosphere:** Biological focus; a site of emergence and hatching.

**Scale Cues:** A localized, identifiable structure situated within the larger basin landscape.

**Descriptive Phrases:** glass-roofed incubator, white egg clusters, biological nursery, transparent dome structure, hatching site.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
