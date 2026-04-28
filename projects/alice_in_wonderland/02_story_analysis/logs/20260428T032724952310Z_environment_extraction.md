# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:27:24.952810+00:00
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

Chapter id: CH006

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

**Location: The House Exterior / Woods Edge**
*   **Event:** A Fish-Footman (fish-like face, powdered curly hair) runs from the woods to a house and raps on the door.
*   **Event:** A Frog-Footman (round face, large eyes, powdered curly hair) opens the door.
*   **Interaction/Object:** The Fish-Footman presents a massive letter (size of a man) to the Frog-Footman; it is an invitation from the Queen for the Duchess to play croquet.
*   **Visual Detail:** Both footmen bow low, and their powdered curls become entangled.
*   **Event:** Alice hides in the woods, laughing at the entanglement, then peeks out to see the Fish-Footman gone; the Frog-Footman is now sitting on the ground staring at the sky.
*   **Interaction:** Alice knocks on the door. The Frog-Footman refuses to help, noting he is on her side of the door and that loud noises are coming from inside.
*   **Audio/Visual Continuity:** Inside the house, there is constant howling, sneezing, and the sound of breaking dishes/kettles.
*   **Event:** A large plate skims out of the house, narrowly missing the Frog-Footman's nose, and breaks against a tree. The Footman remains indifferent.
*   **Decision:** Alice decides to ignore the Footman's idiocy and opens the door to enter.

**Location: The Kitchen (Interior)**
*   **Environment/Atmosphere:** A large, smoke-filled kitchen. High concentration of pepper in the air causing sneezing.
*   **Characters Present:** 
    *   The Duchess (sitting on a three-legged stool).
    *   The Cook (leaning over a fire, stirring a large cauldron of soup).
    *   The Baby (sneezing and howling).
    *   The Cheshire Cat (sitting on the hearth, grinning widely).
*   **Interaction:** Alice asks why the cat is grinning. The Duchess identifies it as a Cheshire Cat and shouts "Pig!" at the baby.
*   **Event/Action:** The Cook begins throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and the baby. 
*   **Visual Detail:** The Duchess remains indifferent to being hit; Alice jumps in terror as a large saucepan nearly hits the baby's nose.
*   **Dialogue/Conflict:** Alice attempts to discuss the rotation of the earth (24 hours). The Duchess responds by telling the Cook to "chop off her head!"
*   **Event/Performance:** The Duchess sings a violent lullaby, shaking the baby violently at the end of every line. The Cook and Baby join in a chorus ("Wow! wow! wow!").
*   **Exit/Transition:** The Duchess flings the baby at Alice and exits to play croquet; the Cook throws a frying pan after her (misses).

**Location: Outside / The Woods**
*   **Character State:** Alice holds the "star-fish" shaped, snorting baby. She learns the "proper" way to nurse it: twisting it into a knot and holding its right ear and left foot.
*   **Transformation Event:** As Alice walks, the baby's nose becomes snout-like and eyes shrink. The baby grunts/sobs and transforms completely into a pig.
*   **Event:** Alice sets the pig down; it trots into the woods.
*   **Character Entrance:** The Cheshire Cat appears on a tree bough. 
*   **Visual Detail:** The Cat has very long claws and many teeth, but maintains a good-natured grin.
*   **Interaction/Dialogue:** The Cat provides directions. It informs Alice that the Hatter and March Hare live in different directions and that both are mad.
*   **Logic/Reveal:** The Cat argues they are all mad, using its own behavior (growling when pleased) as proof of madness.
*   **Visual Effect:** The Cat vanishes, then reappears, then vanishes again—this time vanishing slowly, starting with the tail and ending with a lingering grin.
*   **Event/Transition:** Alice walks toward the March Hare's house. 
*   **Location Detail:** The March Hare's house has chimneys shaped like ears and a thatched roof made of fur.
*   **Scale Shift:** Alice nibbles more mushroom to raise her height to approximately two feet before approaching the house.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
- [woods_edge_and_exterior](woods_edge_and_exterior)
- [duchess_kitchen_interior](duchess_kitchen_interior)
- [enchanted_woods_pathway](enchanted_woods_pathway)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: woods_edge_and_exterior
[[SECTION markdown]]
# Woods Edge and House Exterior

**Role:** Secondary / Transit Setting

**Architecture or Geography:** 
A transition zone between dense woodland and a residential structure. Features a threshold door where footmen interact. The area is bordered by trees capable of catching flying debris (plates, dishes).

**Lighting and Atmosphere Cues:** 
Unpredictable and chaotic. High kinetic energy due to objects being thrown from the house. Auditory atmosphere includes constant howling, sneezing, and the sound of breaking ceramics from within the structure.

**Scale Cues and Recurring Environmental Anchors:** 
The scale is disrupted by oversized props (a man-sized letter). The door serves as a primary threshold between the chaotic interior and the indifferent exterior.

**Descriptive Noun Phrases:** 
*   Threshold of the Duchess's house
*   Entangled footmen at the doorstep
*   Flying ceramic shards against tree bark
*   Woodland edge bordering domestic chaos
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: duchess_kitchen_interior
[[SECTION markdown]]
# Duchess's Kitchen Interior

**Role:** Primary Setting

**Architecture or Geography:** 
A large, cavernous kitchen dominated by a hearth and a cooking fire. Features a three-legged stool for seating and a central area for cauldron-based cooking.

**Lighting and Atmosphere Cues:** 
Heavy, smoke-filled atmosphere. High concentration of airborne pepper causing constant sneezing. The lighting is likely warm and flickering from the hearth but obscured by thick culinary smoke.

**Scale Cues and Recurring Environmental Anchors:** 
Large cauldrons, heavy fire-irons, saucepans, and various kitchen dishes. The scale feels cluttered and volatile due to the frequent projectile motion of kitchenware.

**Descriptive Noun Phrases:** 
*   Smoke-filled culinary chamber
*   Pepper-heavy atmosphere
*   Hearth with a grinning Cheshire Cat
*   Cauldron over a roaring fire
*   Flying saucepans and heavy ironware
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: enchanted_woods_pathway
[[SECTION markdown]]
# Enchanted Woods Pathway

**Role:** Secondary / Transit Setting

**Architecture or Geography:** 
A woodland area featuring tree boughs suitable for feline perching. The landscape leads toward specialized dwellings, such as the March Hare's house which features ear-shaped chimneys and a fur-thatched roof.

**Lighting and Atmosphere Cues:** 
Dreamlike and surreal. Features visual phenomena such as vanishing/reappearing entities (the Cheshire Cat). The atmosphere is one of whimsical madness.

**Scale Cues and Recurring Environmental Anchors:** 
Mushroom patches used for height manipulation. Trees with thick boughs. Distant, eccentric architecture (ear-chimneys) acting as navigational landmarks.

**Descriptive Noun Phrases:** 
*   Surreal woodland canopy
*   Fur-thatched roof dwellings
*   Ear-shaped chimneys
*   Mushroom-dotted forest floor
*   Vanishing feline silhouettes in the trees
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
