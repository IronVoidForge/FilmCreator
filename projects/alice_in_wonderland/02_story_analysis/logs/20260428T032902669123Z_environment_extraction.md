# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:29:02.669623+00:00
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
*   **Characters:** Alice, Alice's Sister.
*   **Events:** Alice sits by the bank, bored, looking at her sister's book (no pictures/conversations). 
*   **Visual State:** Hot, sleepy day.

**Location: Field / Hedge**
*   **Characters:** Alice, White Rabbit.
*   **Events:** A White Rabbit with pink eyes runs past Alice. The Rabbit speaks ("Oh dear! Oh dear! I shall be late!") and checks a watch from its waistcoat-pocket. 
*   **Action:** Alice chases the Rabbit and watches it disappear down a large rabbit-hole under a hedge.

**Location: The Rabbit-Hole / Deep Well**
*   **Characters:** Alice (falling).
*   **Events:** Alice plunges down the hole. The descent is slow, like falling through a deep well. 
*   **Environment/Objects:** The walls are lined with cupboards, bookshelves, maps, and pictures on pegs. 
*   **Interaction:** Alice grabs an empty jar labeled "ORANGE MARMALADE" from a shelf; she places it into a cupboard to avoid dropping it on anyone below.
*   **Internal State:** Alice muses about the depth (4,000 miles), latitude/longitude, and the "Antipathies." She attempts a curtsey while falling.

**Location: Bottom of the Hole (Heap of sticks/leaves)**
*   **Characters:** Alice, White Rabbit (distant).
*   **Events:** Alice lands with a "thump!" on a heap of sticks and dry leaves. She is unhurt. 
*   **Action:** The White Rabbit is seen hurrying down a long passage; Alice chases it.
*   **Transition:** The Rabbit turns a corner, shouting about the time, and disappears.

**Location: Long, Low Hall**
*   **Characters:** Alice.
*   **Environment/Objects:** A hall lit by a row of hanging lamps. Numerous doors line the walls, but all are locked. 
*   **Object Interaction:** Alice finds a three-legged solid glass table in the middle of the hall. On it sits a tiny golden key.
*   **Discovery:** Alice finds a low curtain; behind it is a small door (15 inches high). The golden key fits this lock.
*   **Reveal:** Through the small door, Alice sees a beautiful garden with bright flowers and fountains, but she is too large to enter.

**Location: Long, Low Hall (Second Pass)**
*   **Characters:** Alice.
*   **Object Interaction:** Alice returns to the glass table. A small bottle labeled "DRINK ME" has appeared on it. 
*   **Action:** Alice checks for a "poison" label. Finding none, she drinks the liquid (tastes of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast).
*   **Transformation 1:** Alice shrinks to ten inches high.
*   **Conflict:** Alice realizes she left the golden key on top of the glass table. She tries to climb a table leg, but it is too slippery.
*   **Emotional State:** Alice cries, then scolds herself.
*   **Object Interaction:** Alice finds a small glass box under the table containing a tiny cake marked "EAT ME" in currants.
*   **Action:** Alice eats the cake to attempt to change her size again.
*   **Transformation 2 (Incomplete):** After eating, she initially remains the same size, then continues eating the rest of the cake.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
[[SECTION ...]]
- [riverbank_setting](riverbank_setting)
- [field_and_hedge_setting](field_and_hedge_setting)
- [rabbit_hole_descent](rabbit_hole_descent)
- [hallway_of_doors](hallway_of_doors)
- [miniature_garden_view](miniature_garden_view)
[[/SECTION]]
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: riverbank_setting
[[SECTION markdown]]
[[SECTION ...]]
# Riverbank Setting
**Role:** Primary (Opening)
**Architecture/Geography:** Grassy riverbank, natural outdoor terrain.
**Lighting/Atmosphere:** Hot, sleepy, sun-drenched afternoon; drowsy and tranquil.
**Scale/Anchors:** Large riverbank area, presence of a seated figure near water.
**Prompt Phrases:** sunny riverbank, drowsy summer day, grassy bank, heat haze, peaceful meadow.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: field_and_hedge_setting
[[SECTION markdown]]
[[SECTION ...]]
# Field and Hedge Setting
**Role:** Secondary / Transit
**Architecture/Geography:** Open field transitioning into dense shrubbery or a hedge line.
**Lighting/Atmosphere:** Bright daylight, active and kinetic energy.
**Scale/Anchors:** Large hedge with a distinct rabbit-hole opening at the base.
**Prompt Phrases:** grassy field, thick garden hedge, rabbit hole entrance, bright outdoor light, manicured shrubbery.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: rabbit_hole_descent
[[SECTION markdown]]
[[SECTION ...]]
# Rabbit-Hole Descent
**Role:** Transit (Vertical)
**Architecture/Geography:** A deep, well-like shaft; interior walls lined with domestic shelving.
**Lighting/Atmosphere:** Dimly lit, surreal, slow-motion descent; dreamlike and cavernous.
**Scale/Anchors:** Walls lined with cupboards, bookshelves, maps, and hanging pictures; floating household objects.
**Prompt Phrases:** deep vertical well, interior shaft walls, shelves of books and maps, floating domesticity, surreal descent, cupboard-lined walls.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hallway_of_doors
[[SECTION markdown]]
[[SECTION ...]]
# Hallway of Doors
**Role:** Primary (Interior)
**Architecture/Geography:** A long, low hall with numerous locked doors; contains a central glass table.
**Lighting/Atmosphere:** Lit by a row of hanging lamps; mysterious, enclosed, and slightly claustrophobic.
**Scale/Anchors:** Three-legged solid glass table, row of hanging lamps, small curtained doorway (15 inches high).
**Prompt Phrases:** long low hall, rows of locked doors, hanging lamps, glass pedestal table, miniature door behind curtain, mysterious corridor.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: miniature_garden_view
[[SECTION markdown]]
[[SECTION ...]]
# Miniature Garden View
**Role:** Secondary (Visual Destination)
**Architecture/Geography:** A lush, manicured garden seen through a small aperture.
**Lighting/Atmosphere:** Bright, vibrant, and highly saturated; enticing and beautiful.
**Scale/Anchors:** Tiny view through a 15-inch door; bright flowers and fountains.
**Prompt Phrases:** miniature garden vista, bright blooming flowers, tiny fountains, sunlit garden through a keyhole, vibrant botanical view.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
