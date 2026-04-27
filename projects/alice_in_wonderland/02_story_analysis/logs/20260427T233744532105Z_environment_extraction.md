# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:37:44.532105+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH004

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
- The White Rabbit’s House: A tidy house with a brass nameplate ("W. RABBIT"), featuring a window with a table, a looking-glass, and a chimney.
- The Wood: A thick forest area where Alice flees after leaving the house.

**Characters:**
- **Alice:** Currently giant-sized; she is curious, resourceful, and somewhat anxious about her shifting size.
- **The White Rabbit:** Anxious, authoritative, and prone to temperamental outbursts.
s- **Pat (Bill):** A small creature/animal who falls down the chimney.
- **The Puppy:** An enormous dog that interacts with Alice in the wood.
- **The Blue Caterpillar:** A large blue caterpillar smoking a hookah on top of a mushroom.

**Key Events & Visual Continuity:**
- **The Search:** The White Rabbit searches for his lost fan and gloves; Alice finds him and is mistaken for a housemaid named "Mary Ann."
- **The House Entry:** Alice enters the Rabbit's house to find the items. She finds a fan and tiny white kid gloves on a table in the window.
- **Size Change (Growth):** Alice drinks from a small bottle near the looking-glass. She grows so large her head presses against the ceiling, then she fills the room entirely, eventually having to put an arm out the window and a foot up the chimney to fit.
- **The Interaction with Pat/Bill:** The Rabbit and Pat (the one who falls) attempt to enter the house. Alice's elbow blocks the door; the Rabbit tries the window. A "snatch" by Alice causes a crash in the garden/window area. 
- **The Chimney Kick:** As the Rabbit sends "Bill" down the chimney, Alice kicks him. Bill (the lizard) is sent flying out of the house like a "Jack-in-the-box."
- **Size Change (Shrinking):** The Rabbit throws pebbles through the window; they turn into small cakes on the floor. Alice eats one and shrinks to a manageable size.
- **The Escape:** Alice runs from the crowd of animals (including the recovering Bill) into the thick wood.
- **The Puppy Encounter:** In the wood, Alice encounters an enormous puppy. She plays with it using a stick before fleeing its size/energy.
- **The Discovery:** While resting by a large mushroom, Alice peers over the top to discover a large Blue Caterpillar smoking a hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [white_rabbit_house](#white_rabbit_house)
- [the_thick_wood](#the_thick_wood)

[[/SECTION]]

[[/FILMCREATOR_PACKET]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: white_rabbit_house

[[SECTION markdown]]
# White Rabbit House

**Role:** Primary setting (Interior/Exterior transition)

**Architecture or Geography:** A tidy, domestic house featuring a window with a table, a looking-glass, and a chimney. The space is compact but subject to extreme scale shifts as Alice grows to fill the room entirely.

**Lighting and Atmosphere Cues:** Domestic indoor lighting; bright sunlight through the window; shifting tension between cozy domesticity and claustrophobic crowding as Alice expands.

**Scale Cues and Recurring Environmental Anchters:** A brass nameplate ("W. RABBIT"); a table holding tiny white kid gloves and a fan; the looking-glass; the chimney opening. The room acts as a vessel that becomes increasingly cramped.

**Useful Descriptive Noun Phrases:** Tidy domestic interior, brass nameplate, window sill with trinkets, expanding ceiling constraints, narrow doorway, soot-filled chimney.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: the_thick_wood

[[SECTION markdown]]
# The Thick Wood

**Role:** Secondary setting (Transit and Encounter)

**Architecture or Geography:** A dense, thick forest area with heavy foliage. Features large mushrooms as significant terrain features.

**Lighting and Atmosphere Cues:** Dappled sunlight through thick canopy; sense of wildness and overwhelming scale due to the presence of giant creatures (the puppy).

**Scale Cues and Recurring Environmental Anchters:** Massive tree trunks; enormous puppies; oversized mushrooms serving as platforms or vantage points.

**Useful Descriptive Noun Phrases:** Dense forest foliage, dappled light, massive mushroom cap, overgrown woodland, thicket.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
