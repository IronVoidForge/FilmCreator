# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:22:12.984115+00:00
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

**Locations:**
* **The White Rabbit’s House:** A neat little house with a brass plate reading "W. RABBIT." Interior includes a tidy room with a window table, a looking-glass, and a chimney. Exterior features a window overlooking a cucumber-frame area and a garden/hedge area.
* **Thick Wood:** A dense forest setting where Alice seeks refuge. Contains large thistles and buttercups.
* **Mushroom Clearing:** A specific spot in the wood featuring a large mushroom tall enough for Alice to peer over.

**Characters:**
* **Alice:** Currently tiny; undergoes rapid growth to giant proportions, then shrinks via magic cake.
* **The White Rabbit:** Anxious, authoritative, and prone to anger. Mistakes Alice for his housemaid, "Mary Ann."
* **Pat:** A subordinate/worker (likely an animal) seen through the window.
* **Bill:** A small creature (a lizard) who is forced down the chimney by the Rabbit's orders.
* **The Crowd:** A group of small animals and birds outside the house, including two guinea-pigs.
* **Enormous Puppy:** A large, playful, but intimidating animal in the woods that chases Alice.
* **Blue Caterpillar:** A large, calm creature sitting atop a mushroom, smoking a hookah.

**Key Events & Visual Continuity:**
* **Entrance/Discovery:** The White Rabbit enters the scene looking for lost gloves and a fan; he encounters Alice and commands her to fetch them.
* **The House Interior:** Alice enters the Rabbit's house. She finds a fan and white kid gloves on a window table. 
* **Size Change (Growth):** Alice drinks from an unlabeled bottle near a looking-glass. She grows rapidly, eventually becoming so large she is wedged in the room (head against ceiling, one arm out the window, one foot up the chimney).
* **The Confrontation at the Window:** The Rabbit attempts to enter through the window. Alice reaches out and "snatches" at the air, causing a crash in what is assumed to be a cucumber-frame. 
* **The Chimney Incident:** A group of animals attempt to use ladders/ropes to reach the house. Bill is ordered down the chimney. Alice, inside the chimney, delivers a sharp kick to Bill, sending him flying out like a "Jack-in-the-box."
* **Size Change (Shrinking):** The Rabbit's crowd throws pebbles through the window; these pebbles turn into small cakes on the floor. Alice eats one and shrinks to a manageable size.
* **Escape:** Alice exits the house, passes the recovering Bill (being tended to by guinea-pigs), and flees into the woods.
* **The Puppy Encounter:** In the woods, Alice is hunted/played with by an enormous puppy using a stick as a lure. She uses a large thistle for cover.
* **The Reveal:** Alice rests against a buttercup and discovers a large mushroom. Peering over the edge, she reveals the Blue Caterpillar smoking a hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [white_rabbit_house](white_rabbit_house)
- [dense_woodland](dense_woodland)
- [mushroom_clearing](mushroom_clearing)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: white_rabbit_house
[[SECTION markdown]]
# White Rabbit's House

**Role:** Primary setting

**Architecture or Geography:**
A neat, small-scale domestic dwelling. Interior features a tidy room with a window table, a looking-glass (mirror), and a functional chimney. Exterior includes a window overlooking a cucumber-frame garden area and surrounding hedges.

**Lighting and Atmosphere Cues:**
Domestic, enclosed, and increasingly claustrophobic as the occupant grows. Bright daylight filtering through windows, transitioning to chaotic and cramped during the growth sequence.

**Scale Cues and Recurring Environmental Anchors:**
*   Window table with accessories (fan, white kid gloves).
*   Looking-glass/Mirror.
*   Chimney flue.
*   Cucumber-frame garden visible through the window.
*   Extreme scale shifts: The room transforms from a cozy space to a tight, restrictive container as Alice grows to fill it from floor to ceiling.

**Descriptive Noun Phrases:**
Neat little house, brass nameplate "W. RABBIT", tidy domestic interior, looking-glass reflection, cucumber-frame garden, chimney flue, cramped miniature room.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dense_woodland
[[SECTION markdown]]
# Dense Woodland

**Role:** Secondary / Transit setting

**Architecture or Geography:**
A thick, overgrown forest characterized by massive flora relative to the protagonist. Features large thistles and buttercups that serve as tactical cover.

**Lighting and Atmosphere Cues:**
Dappled sunlight through heavy foliage; sense of exposure and vulnerability despite the density. High-stakes, kinetic atmosphere during chase sequences.

**Scale Cues and Recurring Environmental Anchors:**
*   Enormous thistles (used for hiding).
*   Large buttercups.
*   Overgrown forest floor.

**Descriptive Noun Phrases:**
Thick wood, dense foliage, giant thistles, oversized buttercups, dappled forest light, overgrown woodland floor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mushroom_clearing
[[SECTION markdown]]
# Mushroom Clearing

**Role:** Secondary setting

**Architecture or Geography:**
A specific clearing within the dense wood, dominated by a singular, massive fungal structure.

**Lighting and Atmosphere Cues:**
Calm, surreal, and hazy. Atmospheric smoke from a hookah.

**Scale Cues and Recurring Environmental Anchors:**
*   Large mushroom (tall enough to peer over).
*   Hookah smoke plumes.

**Descriptive Noun Phrases:**
Giant mushroom cap, fungal clearing, hookah smoke, towering mushroom, surreal woodland plateau.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
