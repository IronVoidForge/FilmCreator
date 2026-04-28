# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:59:09.116124+00:00
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

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Location: Riverbank**
- **Characters:** Alice, Sister (off-screen/passive).
- **Events:** Alice sits by a riverbank on a hot day; she expresses boredom with her sister's book (no pictures or conversations).
- **Visual State:** Sunny, sleepy atmosphere.

**Location: The Hedge / Rabbit-Hole Entrance**
- **Characters:** Alice, White Rabbit.
- **Events:** A White Rabbit with pink eyes runs past Alice. The Rabbit checks a watch from its waistcoat-pocket and exclaims, "Oh dear! Oh dear! I shall be late!" Alice, driven by curiosity, chases the Rabbit. The Rabbit enters a large rabbit-hole under a hedge; Alice follows immediately.

**Location: The Vertical Well/Tunnel**
- **Characters:** Alice (falling).
- **Events:** The hole turns into a deep well. Alice falls slowly. 
- **Environment/Objects:** The walls are lined with cupboards, bookshelves, maps, and pictures on pegs. 
- **Interaction:** Alice grabs an empty jar labeled "ORANGE MARMALADE" from a shelf; she chooses to place it in a cupboard rather than drop it.
- **Internal Monologue/Action:** Alice calculates her depth (approx. 4000 miles) and contemplates the Antipathies. She attempts a curtsey while falling. She drifts into a sleepy state, dreaming of her cat Dinah.
- **Transition:** A loud "thump!" marks the end of the fall as she lands on a heap of sticks and dry leaves.

**Location: The Long Passage / Hall of Doors**
- **Characters:** Alice, White Rabbit (briefly).
- **Events:** Alice jumps up; it is dark overhead. She sees the White Rabbit hurrying down a long passage. She chases him around a corner. 
- **Environment/Objects:** A long, low hall lit by a row of lamps hanging from the roof. Numerous doors line the walls, but all are locked.
- **Discovery 1:** Alice finds a three-legged glass table in the middle of the hall. On it sits a tiny golden key. She tries the key on the large doors; it is too small/the locks are too large.
- **Discovery 2:** Alice finds a low curtain. Behind it is a small door (approx. 15 inches high). The golden key fits this lock perfectly.

**Location: The Small Passage / Garden View**
- **Characters:** Alice.
- **Events:** Alice opens the tiny door and looks through a passage (size of a rat-hole) into a beautiful garden with bright flowers and fountains. 
- **Conflict:** Alice realizes she is too large to fit through the door. She wishes she could "shut up like a telescope."

**Location: The Glass Table (Scale Shift 1)**
- **Characters:** Alice.
- **Events:** Alice returns to the glass table. A small bottle, previously unseen, is now on the table. It has a label: "DRINK ME."
- **Interaction:** Alice inspects the bottle for poison. Finding none, she drinks it. The liquid tastes of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast.
- **Transformation:** Alice shrinks to ten inches high. 
- **Conflict/Failure:** Having shrunk, she realizes she left the golden key on top of the glass table. She tries to climb a table leg, but it is too slippery. She sits down and cries.

**Location: The Glass Table (Scale Shift 2)**
- **Characters:** Alice.
- **Events:** Alice discovers a small glass box under the table. Inside is a tiny cake marked "EAT ME" in currants.
- **Decision/Interaction:** Alice decides to eat the cake to either grow large enough to reach the key or small enough to fit under the door. She eats the cake. 
- **Visual State:** After eating, she initially remains the same size, then proceeds to finish the entire cake.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[SECTION environment_index_markdown]
[[SECTION ...]]
# Environment Index

- [riverbank_setting](riverbank_setting)
- [rabbit_hole_tunnel](rabbit_hole_tunnel)
- [hall_of_doors](hall_of_doors)
- [miniature_garden_view](miniature_garden_view)
[[/SECTION]]
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: riverbank_setting
[SECTION markdown]
[[SECTION ...]]
# Riverbank Setting

**Role:** Primary (Introductory)
**Architecture/Geography:** A grassy, sloping riverbank under a summer sun.
**Lighting/Atmosphere:** Bright, sunny, warm, and sleepy; high-key natural lighting.
**Scale/Anchors:** Large scale relative to Alice; presence of a nearby river and shade from trees.
**Descriptive Noun Phrases:** Sunny riverbank, lush grass, drowsy summer afternoon, shaded bank.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: rabbit_hole_tunnel
[SECTION markdown]
[[SECTION ...]]
# Rabbit Hole Tunnel

**Role:** Transit Setting
**Architecture/Geography:** A deep, vertical well-like shaft. The walls are not natural earth but are lined with domestic architecture including cupboards, bookshelves, and pegs for maps and pictures.
**Lighting/Atmosphere:** Dim, surreal, drifting light; a sense of slow, weightless descent.
**Scale/Anchors:** Massive verticality (approx. 4000 miles); walls cluttered with household objects like jars of orange marmalade and hanging frames.
**Descriptive Noun Phrases:** Vertical domestic shaft, floating bookshelves, cupboard-lined walls, surreal descent, gravity-defying interior.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hall_of_doors
[SECTION markdown]
[[SECTION ...]]
# Hall of Doors

**Role:** Primary Setting
**Architecture/Geography:** A long, low passage or hallway. The walls are lined with numerous large, locked doors. Features a three-legged glass table in the center and a small curtained area leading to a tiny door.
**Lighting/Atmosphere:** Dimly lit by a row of hanging lamps from the ceiling; mysterious and claustrophobic.
**Scale/Anchors:** Long horizontal axis; recurring anchor is the three-legged glass table with its golden key.
**Descriptive Noun Phrases:** Low-ceilinged hall, row of hanging lamps, corridor of locked doors, glass pedestal table, miniature doorway.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: miniature_garden_view
[SECTION markdown]
[[SECTION ...]]
# Miniature Garden View

**Role:** Secondary (Vista) Setting
**Architecture/Geography:** A lush, beautiful garden visible through a tiny, rat-hole sized opening. Contains bright flowers and fountains.
**Lighting/Atmosphere:** Vibrant, saturated colors; bright, idyllic sunlight contrasting with the dark hall.
**Scale/Anchors:** Extremely small perspective (viewed from 10-inch height); anchor is the fountain and floral clusters.
**Descriptive Noun Phrases:** Sun-drenched garden, miniature fountains, vibrant flowerbeds, tiny vista through a keyhole.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
