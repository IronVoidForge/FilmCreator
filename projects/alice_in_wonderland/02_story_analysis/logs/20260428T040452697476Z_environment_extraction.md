# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:04:52.697476+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
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



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each environment item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION environment_index_markdown]] and [[SECTION markdown]] exactly as written

- do not echo this instruction block back as an example packet; return the actual packet only



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

**Setting: The White Rabbit's House**
*   **Location:** A neat little house with a brass plate reading "W. RABBIT."
*   **Interior Subzones:** 
    *   A tidy upstairs room containing a table by a window, a looking-glass, and a small bottle (no label).
    *   A chimney/fireplace.
    *   The doorway (blocked by Alice's size).

**Characters & Entrances/Exits**
*   **Alice:** Enters the house via the front door; exits via the door after shrinking; later enters a thick wood.
*   **White Rabbit:** Enters the house area, attempts to enter the room through the door (fails), then attempts the window.
*   **Pat:** A worker/animal outside the house; interacts with the Rabbit and Bill.
*   **Bill (a Lizard):** Appears via the chimney (after being kicked); later seen outside being held by guinea-pigs.
*   **The Crowd:** A group of small animals/birds waiting outside the house.
*   **Enormous Puppy:** Encountered by Alice in the woods; interacts with her via a stick.
*   **Blue Caterpillar:** Revealed at the end, sitting atop a large mushroom in the woods.

**Key Events & Physical Transitions**
*   **The Search:** The White Rabbit searches for lost gloves and a fan; mistakes Alice for his housemaid "Mary Ann."
*   **The Growth Spurt:** Alice finds an unlabeled bottle in the Rabbit's room, drinks it, and grows so large her head presses against the ceiling. She eventually occupies the entire room, with one arm out the window and one foot up the chimney.
*   **The Window Confrontation:** The Rabbit attempts to enter through the window; Alice reaches out a hand to snatch at him, causing a crash in what is assumed to be a cucumber-frame.
*   **The Chimney Incident:** A group of animals attempts to use ladders and ropes to reach the house/chimney. They decide Bill must go down the chimney. Alice, positioned in the chimney, delivers a sharp kick to the scrambling animal (Bill).
*   **The Siege:** The Rabbit orders a "barrowful" of pebbles to be thrown at the house. The pebbles hit Alice through the window and transform into small cakes on the floor.
*   **The Shrinking:** Alice eats one of the cake-pebbles, shrinks to a manageable size, and escapes the house.
*   **The Woods Encounter:** Alice wanders into a thick wood. She is nearly trampled by an enormous puppy but manages to distract it with a stick.
*   **The Discovery:** While resting against a buttercup, Alice discovers a large mushroom. Peering over the edge, she reveals the Blue Caterpillar smoking a hookah.

**Objects & Visual Continuity**
*   **White Kid Gloves & Fan:** The objects the Rabbit is searching for.
*   **Unlabeled Bottle:** Causes rapid growth.
*   **Pebbles/Cakes:** Small stones that transform into edible cakes upon landing.
*   **Stick:** Used by Alice to play with the puppy.
*   **Hookah:** Being used by the Caterpillar.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [white_rabbit_house](white_rabbit_house)
- [thick_woods](thick_woods)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: white_rabbit_house
[[SECTION markdown]]
# White Rabbit's House

**Role:** Primary Setting

**Architecture & Geography:**
A neat, small-scale domestic residence. Features a tidy upstairs room with a window and a fireplace/chimney. The interior is characterized by tight spatial constraints that become extreme when Alice grows. Includes a doorway and a window frame (noted as cucumber-frame).

**Lighting & Atmosphere:**
Domestic, bright, and orderly. Transitions to a sense of claustrophobia and chaotic congestion as Alice's physical scale expands to fill the entire volume of the room.

**Scale Cues & Anchors:**
- Brass plate reading "W. RABBIT."
- A table positioned by a window.
- A looking-glass (mirror).
- The chimney/fireplace.
- Small, manageable furniture that becomes dwarfed by Alice's massive scale.

**Descriptive Noun Phrases:**
neat little house, brass nameplate, tidy upstairs room, cucumber-frame window, cramped domestic interior, oversized occupant in small room, soot-stained chimney.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thick_woods
[[SECTION markdown]]
# Thick Woods

**Role:** Secondary / Transit Setting

**Architecture & Geography:**
A dense, overgrown woodland area. Features heavy vegetation including large buttercups and massive mushrooms. The terrain is uneven and feels enclosed by foliage.

**Lighting & Atmosphere:**
Dappled light through thick canopy; organic, wild, and slightly overwhelming. A sense of discovery amidst the density.

**Scale Cues & Anchors:**
- Enormous puppy (relative to Alice).
- Large mushroom (serving as a platform/seat).
- Oversized buttercups for resting.
- Dense undergrowth.

**Descriptive Noun Phrases:**
thick woodland, dense foliage, oversized flora, giant mushroom cap, dappled forest light, overgrown thicket, botanical wonderland.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
