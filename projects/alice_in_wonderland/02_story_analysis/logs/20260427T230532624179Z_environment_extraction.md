# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:05:32.624179+00:00
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

**Setting:** 
- A riverbank (sunny, hot day).
- A large rabbit-hole under a hedge.
- A deep vertical well/tunnel lined with cupboards, bookshelves, maps, and pictures.
- A long, low hall lit by a row of hanging lamps, featuring many locked doors.
- A small passage (rat-hole sized) leading to a lush garden with bright flowers and fountains.

**Characters:**
- Alice: A young girl, curious and prone to internal monologue/self-instruction.
- The White Rabbit: An anthropomorphic rabbit wearing a waistcoat and carrying a watch.
- Alice's Sister: Present on the bank at the start.
- Dinah: Alice's cat (mentioned in thought).

**Key Events & Transitions:**
- **The Bank:** Alice sits by her sister, feeling bored/sleepy. The White Rabbit runs past, checking a watch from its waistcoat pocket.
- **The Chase:** Alice chases the Rabbit to the hedge and follows it down the rabbit-hole.
- **The Fall:** Alice falls down a deep well/tunnel. 
    - *Visual Detail:* The walls are lined with cupboards and bookshelves. 
    - *Object Interaction:* Alice grabs an empty "ORANGE MARMALADE" jar from a shelf and places it in a cupboard to avoid dropping it.
    - *Internal State:* Alice talks to herself about the center of the earth, latitude/longitude, and her cat Dinah.
- **The Landing:** Alice hits a heap of sticks and dry leaves at the bottom.
- **The Hallway:** Alice follows the White Rabbit into a long, lamp-lit hall. She discovers all the doors are locked.
- **The Discovery (Key):** Alice finds a three-legged glass table with a tiny golden key. The key is too small for the large doors.
- **The Discovery (Door):** Alice finds a low curtain hiding a small door (15 inches high). She uses the golden key; it fits.
- **The Garden Reveal:** Through the small door, Alice sees a beautiful garden but realizes she is too large to fit through.
- **The Transformation (Shrinking):** Alice finds a bottle labeled "DRINK ME" on the glass table. She tastes it (flavor: cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast) and shrinks to ten inches tall.
- **The Conflict:** Now small enough for the door, she realizes she left the golden key on top of the high glass table. She tries to climb the slippery table leg but fails and cries.
- **The Transformation (Cake):** Alice finds a glass box under the table containing a cake labeled "EAT ME." 
- **The Decision:** Alice eats the cake, hoping it will either make her large enough to reach the key or small enough to fit under the door. After eating it, she remains the same size.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [riverbank_setting](#riverbank_setting)
- [rabbit_hole_tunnel](#rabbit_hole_tunnel)
- [lamp_lit_hallway](#lamp_lit_hallway)
- [lush_garden_view](#lush_garden_view)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: riverbank_setting

[[SECTION markdown]]

# Riverbank Setting

**Role:** Primary (Starting)

**Geography:** A grassy bank beside a slow-moving river.

**Lighting and Atmosphere:** Bright, sunny, hot day; sleepy and tranquil atmosphere.

**Scale Cues:** Human-scale landscape; wide open sky and river horizon.

**Prompt Phrases:** sun-drenched riverbank, lush green grass, shimmering water, drowsy summer afternoon.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: rabbit_hole_tunnel

[[SECTION markdown]]

# Rabbit Hole Tunnel

**Role:** Transit Setting

**Geography:** A deep, vertical shaft or well descending into the earth.

**Lighting and Atmosphere:** Dimly lit; transition from natural sunlight to subterranean shadows.

**Scale Cues:** Massive vertical scale; walls lined with domestic objects.

**Architecture/Features:** Vertical tunnel walls lined with cupboards, bookshelves, maps, and framed pictures; shelves holding jars (e.g., orange marmalade).

**Prompt Phrases:** deep vertical shaft, subterranean library, wall-mounted cupboards, floating household objects, dusty bookshelves.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: lamp_lit_hallway

[[SECTION markdown]]

# Lamp Lit Hallway

**Role:** Primary (Transition)

**Geography:** A long, low interior hall.

**Lighting and Atmosphere:** Warm, artificial light from a row of hanging lamps; mysterious and enclosed.

**Scale Cues:** Low ceilings; repetitive architectural elements.

**Architecture/Features:** Long corridor, many locked doors, three-legged glass table, small curtained alcove.

**Prompt Phrases:** long low hallway, hanging oil lamps, warm amber glow, rows of locked doors, glass pedestal table.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: lush_garden_view

[[SECTION markdown]]

# Lush Garden View

**Role:** Secondary (Revealed)

**Geography:** A vibrant garden seen through a small aperture.

**Lighting and Atmosphere:** Bright, saturated colors; high-key natural lighting; idyllic and magical.

**Scale Cues:** Seen from a miniature perspective; distant flowers and fountains.

**Architecture/Features:** Brightly colored flowers, flowing water fountains, manicured greenery.

**Prompt Phrases:** vibrant floral garden, sunlit flowerbeds, sparkling fountains, lush botanical vista.

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
