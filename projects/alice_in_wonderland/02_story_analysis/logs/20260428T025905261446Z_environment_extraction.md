# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T02:59:05.261446+00:00
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

Chapter id: CH001

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

- keep the environment set small and useful

- use concise visible descriptions



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Location: Riverbank**
- **Characters:** Alice, Alice's Sister.
- **Events:** Alice sits by the bank, bored, looking at a book with no pictures/conversations. 
- **Visual State:** Hot, sleepy day.

**Location: Field / Hedge**
- **Characters:** Alice, White Rabbit (Pink eyes, wearing a waistcoat with a pocket).
- **Events:** 
    - The White Rabbit runs past Alice, muttering "Oh dear! Oh dear! I shall be late!"
    - The White Rabbit pulls a watch out of its waistcoat pocket and checks it.
    - Alice, driven by curiosity, chases the Rabbit.
    - The White Rabbit enters a large rabbit-hole under a hedge.
    - Alice follows the Rabbit into the hole.

**Location: The Rabbit-Hole / Deep Well (Transition)**
- **Characters:** Alice.
- **Events:** 
    - The tunnel dips suddenly into a deep well/shaft.
    - Alice falls slowly through the darkness.
    - **Object Interaction:** Alice passes cupboards and bookshelves filled with maps and pictures. She grabs an empty jar labeled "ORANGE MARMALADE" from a shelf and places it into a cupboard to avoid dropping it on anyone below.
    - **Dialogue/Internal Monologue:** Alice muses about the depth of the fall, her school lessons (latitude/longitude), and her cat Dinah.
    - **Visual State:** Dark, descending through a vertical shaft lined with domestic objects.

**Location: Heap of Sticks and Dry Leaves**
- **Characters:** Alice, White Rabbit (distant).
- **Events:** 
    - Alice lands with a "thump" on a heap of sticks/leaves; she is unhurt.
    - The White Rabbit is seen in the distance hurrying down a long passage, muttering about his ears and whiskers.
    - Alice chases after him.

**Location: Long, Low Hall**
- **Characters:** Alice.
- **Setting Details:** Lit by a row of lamps hanging from the roof; many doors line the walls, all locked.
- **Events:** 
    - Alice explores the hall, trying every door, but finds them all locked.
    - **Object Interaction (The Table):** Alice finds a three-legged glass table. On it sits a tiny golden key.
    - **Discovery:** Alice finds a low curtain; behind it is a small door (approx. 15 inches high).
    - **Action:** Alice uses the golden key on the small door; it fits.
    - **Reveal:** Through the small door, Alice sees a beautiful garden with bright flowers and fountains.
    - **Constraint:** Alice realizes she is too large to fit through the door.

**Location: Long, Low Hall (Continued)**
- **Characters:** Alice.
- **Events:** 
    - **Object Interaction (The Bottle):** Alice returns to the glass table. A small bottle labeled "DRINK ME" has appeared (not previously there).
    - **Action:** Alice inspects the label for "poison," finds none, and drinks the liquid.
    - **Sensory Detail:** The drink tastes of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast.
    - **Transformation 1:** Alice shrinks to ten inches high.
    - **Conflict:** Alice realizes she left the golden key on top of the glass table. She tries to climb the slippery glass leg but fails.
    - **Emotional State:** Alice sits down and cries.
    - **Object Interaction (The Cake):** Alice finds a small glass box under the table containing a tiny cake marked "EAT ME" in currants.
    - **Action:** Alice eats the cake to attempt to change her size again.
    - **Transformation 2 (Unresolved):** After eating, she initially remains the same size, then continues eating the rest of the cake.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [riverbank_setting](riverbank_setting)
- [field_and_hedge](field_and_hedge)
- [rabbit_hole_shaft](rabbit_hole_shaft)
- [landing_heap](landing_heap)
- [long_low_hall](long_low_hall)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: riverbank_setting
[[SECTION markdown]]
# Riverbank Setting
**Role:** Primary setting (opening)
**Architecture/Geography:** Grassy riverbank, natural terrain.
**Lighting/Atmosphere:** Hot, sleepy, sun-drenched afternoon; drowsy atmosphere.
**Scale/Anchors:** Large river, grassy banks, Alice's sister reading nearby.
**Descriptive Noun Phrases:** Sun-baked riverbank, drowsy summer day, lush grass, slow-moving water.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: field_and_hedge
[[SECTION markdown]]
# Field and Hedge
**Role:** Secondary setting / Transition
**Architecture/Geography:** Open field leading to a dense, large hedge.
**Lighting/Atmosphere:** Bright daylight; sense of sudden movement and curiosity.
**Scale/Anchors:** Large rabbit-hole entrance under the hedge.
**Descriptive Noun Phrases:** Verdant meadow, thick garden hedge, dark burrow entrance, sunlit field.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: rabbit_hole_shaft
[[SECTION markdown]]
# Rabbit-Hole Shaft
**Role:** Transit setting
**Architecture/Geography:** A deep, vertical well or shaft; a descending tunnel.
**Lighting/Atmosphere:** Dark, cavernous, surreal; slow descent through shadows.
**Scale/Anchors:** Verticality of the fall; walls lined with domestic objects (cupboards, bookshelves, maps).
**Descriptive Noun Phrases:** Deep subterranean shaft, vertical tunnel, floating domestic clutter, dark abyss, shelves of curiosities.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: landing_heap
[[SECTION markdown]]
# Landing Heap
**Role:** Secondary setting
**Architecture/Geography:** The base of the rabbit hole; a cluttered floor.
**Lighting/Atmosphere:** Dim, dusty, subterranean.
**Scale/Anchors:** A heap of sticks and dry leaves.
**Descriptive Noun Phrases:** Pile of dry leaves, tangled sticks, dusty tunnel floor, subterranean landing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: long_low_hall
[[SECTION markdown]]
# Long Low Hall
**Role:** Primary setting
**Architecture/Geography:** A long, low corridor with many locked doors; a small door (15 inches high) behind a curtain.
**Lighting/Atmosphere:** Lit by a row of hanging lamps; mysterious and claustrophobic yet grand.
**Scale/Anchors:** Three-legged glass table, tiny golden key, small door leading to a garden view.
**Descriptive Noun Phrases:** Dimly lit corridor, row of hanging lamps, endless locked doors, three-legged glass table, miniature doorway, glimpse of a bright garden.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
