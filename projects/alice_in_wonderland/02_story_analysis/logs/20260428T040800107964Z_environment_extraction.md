# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:08:00.107964+00:00
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
*   **Entrance/Exit:** A Frog-Footman (round face, large frog eyes, powdered curly hair) opens the door. The Fish-Footman hands over a massive letter (Queen's croquet invitation). Both bow; their curls entangle.
*   **Event:** Alice hides in the woods to laugh at the footmen. When she peeks out, the Fish-Footman has exited; the Frog-Footman sits on the ground staring at the sky.
*   **Interaction:** Alice knocks. The Frog-Footman refuses to help, claiming he is on her side of the door and that it's too noisy inside.
*   **Visual/Audio Detail:** Extraordinary noise from inside: howling, sneezing, and crashing dishes.
*   **Object Interaction:** A large plate skims out of the house, grazes the Frog-Footman’s nose, and breaks against a tree. The Footman remains indifferent.
*   **Decision:** Alice decides to ignore the Footman's idiotic commentary and enters the house through the door.

**Location: The Kitchen (Interior)**
*   **Environment/Atmosphere:** Thick smoke; heavy presence of pepper causing sneezing.
*   **Characters Present:** The Duchess (on a three-legged stool), a Cook (leaning over a cauldron of soup), a Baby (sneezing and howling), and the Cheshire Cat (sitting on the hearth, grinning).
*   **Interaction:** Alice asks why the cat is grinning. The Duchess identifies it as a Cheshire Cat and shouts "Pig!" at the baby.
*   **Conflict/Action:** The Cook begins throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and the Baby. The Duchess remains unreactive to being hit.
*   **Dialogue/Reveal:** Alice attempts to discuss the Earth's rotation; the Duchess responds by telling the Cook to "chop off her head!"
*   **Performance/Action:** The Duchess sings a violent lullaby, shaking the baby violently at the end of every line. The Baby and Cook join in a "Wow! wow! wow!" chorus.
*   **Exit/Transition:** The Duchess flings the baby at Alice and exits to play croquet; the Cook throws a frying pan at her (misses).

**Location: Outside / Woods**
*   **Character State:** Alice holds the "star-fish" shaped, snorting baby. She learns the "correct" way to nurse it is to twist it into a knot by its ear and foot.
*   **Transformation/Reveal:** As Alice walks, the baby's nose becomes a snout and eyes shrink. The baby grunts and transforms into a pig.
*   **Event:** Alice sets the pig down; it trots into the woods.
*   **Encounter: The Cheshire Cat:**
    *   The Cat appears on a tree bough (long claws, many teeth, wide grin).
    *   **Dialogue/Logic:** The Cat explains that everyone is mad. It proves its own madness by claiming it growls when pleased and wags its tail when angry (contrary to dogs).
    *   **Visual Effect:** The Cat vanishes, then reappears. It eventually vanishes slowly, starting with the tail and ending with the grin, which lingers in the air.
*   **Decision/Pathing:** Alice heads toward the March Hare's house.

**Location: Approaching the March Hare's House**
*   **Visual Detail:** The house has chimneys shaped like ears and a roof thatched with fur.
*   **Scale Shift:** Alice nibbles more mushroom to raise her height to approximately two feet.
*   **State of Mind:** Alice is hesitant/anxious about the potential madness of the inhabitants.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
environment_index_markdown
[[SECTION environment_index_markdown]]
- [woods_edge_and_house_exterior](woods_edge_and_house_exterior)
- [chaotic_kitchen_interior](chaotic_kitchen_interior)
- [enchanted_woods](enchanted_woods)
- [march_hare_house_approach](march_hare_house_approach)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
asset_id: woods_edge_and_house_exterior
[[SECTION markdown]]
# Woods Edge and House Exterior

**Environment Role:** Primary / Transit Setting

**Architecture or Geography:** A transition zone between dense woodland and a residential structure. Features a prominent doorway where footmen reside. Includes large trees capable of catching flying debris (plates).

**Lighting and Atmosphere Cues:** Bright, perhaps slightly surreal daylight; auditory atmosphere is defined by extreme internal noise (howling, sneezing, crashing) leaking from the house.

**Scale Cues and Recurring Environmental Anchors:** A single house door acting as a threshold; large trees near the entrance; massive oversized letters/envelopes.

**Useful Descriptive Noun Phrases:**
- Threshold of the footmen's house
- Wooded perimeter
- Clattering domestic noise leakage
- Tree-grazed debris
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: chaotic_kitchen_interior
[[SECTION markdown]]
# Chaotic Kitchen Interior

**Environment Role:** Primary Setting

**Architecture or Geography:** A cramped, domestic kitchen interior featuring a hearth and cooking stations. Includes a three-legged stool for seating and large cauldrons.

**Lighting and Atmosphere Cues:** Thick, heavy smoke; airborne pepper particles causing constant sneezing; chaotic and violent energy; warm, flickering light from the hearth/cauldron.

**Scale Cues and Recurring Environmental Anchors:** A central cauldron of soup; a stone hearth where the Cheshire Cat sits; scattered kitchenware (saucepans, fire-irons, plates).

**Useful Descriptive Noun Phrases:**
- Smoke-filled culinary chamber
- Pepper-heavy atmosphere
- Hearthside grinning cat
- Flying cookware chaos
- Cauldron-centered kitchen
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: enchanted_woods
[[SECTION markdown]]
# Enchanted Woods

**Environment Role:** Secondary / Transit Setting

**Architecture or Geography:** Dense woodland with thick tree boughs and undergrowth.

**Lighting and Atmosphere Cues:** Dappled light through leaves; a sense of madness and unpredictability; shifting visual reality (transforming creatures).

**Scale Cues and Recurring Environmental Anchors:** Tree boughs suitable for feline perching; forest floor where transformed animals (pigs) trot away.

**Useful Descriptive Noun Phrases:**
- Dappled woodland canopy
- Shifting forest shadows
- Perch of the Cheshire Cat
- Transforming wilderness
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: march_hare_house_approach
[[SECTION markdown]]
# March Hare House Approach

**Environment Role:** Secondary Setting

**Architecture or Geography:** A surreal, anthropomorphic dwelling. The house features chimneys shaped like ears and a roof thatched with fur.

**Lighting and Atmosphere Cues:** Whimsical yet unsettling; high-concept surrealism.

**Scale Cues and Recurring Environmental Anchors:** Scale is relative to Alice's height (which fluctuates via mushroom consumption); the ear-shaped chimneys serve as primary landmarks.

**Useful Descriptive Noun Phrases:**
- Fur-thatched roofline
- Ear-shaped chimney stacks
- Surreal domestic architecture
- Whimsical madness threshold
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
