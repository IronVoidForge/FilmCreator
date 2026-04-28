# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:07:20.962297+00:00
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

**Location: The White Rabbit's House (Interior)**
*   **Event:** The White Rabbit enters the scene, frantic and muttering about "The Duchess" and lost items (fan and white kid gloves). 
*   **Character Entrance/Interaction:** The Rabbit mistakes Alice for his housemaid, "Mary Ann," and commands her to fetch the items. Alice, frightened, complies and runs toward the Rabbit's residence.
*   **Location Shift:** Alice enters a neat little house with a brass plate reading "W. RABBIT." She moves upstairs to a tidy room containing a table by a window.
*   **Object Interaction:** On the table, Alice finds a fan and several pairs of tiny white kid gloves. Nearby, she discovers an unlabeled bottle.
*   **Transformation 1 (Growth):** Alice drinks from the bottle. She rapidly grows until her head presses against the ceiling. She continues to grow until she is forced into an uncomfortable position: kneeling, then lying down with one elbow against the door and one arm curled around her head, eventually placing one arm out the window and one foot up the chimney.
*   **External Conflict (The Siege):** The White Rabbit arrives at the door. Because Alice's elbow blocks it, he attempts to enter through the window. 
*   **Action/Interaction:** Alice reaches out a hand and makes a "snatch" in the air near the window. This results in a shriek and the sound of breaking glass (a cucumber-frame).
*   **Character Reveal/Dialogue:** A new character, Pat (an animal), is introduced via dialogue. The Rabbit and Pat discuss the "arm" filling the window. 
*   **Action/Interaction:** Alice makes a second "snatch" in the air, causing more shrieks and broken glass.
*   **The Siege Escalates:** A crowd of small animals arrives with ladders and ropes. They attempt to reach the window/roof. There is a loud crash involving a loose slate.
*   **Action/Interaction (The Kick):** The Rabbit orders "Bill" to go down the chimney. Alice, positioned in the chimney, delivers a sharp kick to the scrambling creature above her.
*   **Result:** Bill is ejected from the chimney. A chorus of voices reacts to his "sky-rocket" exit.
*   **Conflict Escalation:** The Rabbit threatens to burn the house down. Alice shouts back a threat involving her cat, Dinah.
*   **Object Interaction/Transformation 2 (Shrinking):** The Rabbit begins throwing pebbles through the window. As they hit the floor, the pebbles transform into little cakes. Alice eats one cake and rapidly shrinks.
*   **Exit:** Once small enough, Alice exits through the door.

**Location: Outside / Thick Wood**
*   **Character Interaction/Visual State:** Alice emerges to find a crowd of animals. She sees Bill (a lizard) being held up by two guinea-pigs. Fearing the crowd, Alice flees into a thick wood.
*   **Character Entrance/Interaction:** An enormous puppy appears, looking down at Alice. 
*   **Action/Interaction:** Alice uses a stick to play with the puppy to distract it. The puppy performs "charges" and tumbles over itself. Alice uses this distraction to escape into the woods.
*   **Location Shift:** Alice rests against a large buttercup. She observes her surroundings looking for something to eat or drink to restore her size.
*   **Character Reveal/Visual Discovery:** Alice finds a large mushroom. She climbs onto tiptoe and peeks over the edge of the cap.
*   **Reveal:** On top of the mushroom, she discovers a large blue caterpillar sitting with arms folded, smoking a long hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
- [white_rabbit_house](white_rabbit_house)
- [thick_wood](thick_wood)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: white_rabbit_house
[[SECTION markdown]]
# White Rabbit's House

**Role:** Primary setting (interior/exterior conflict)

**Architecture & Geography:**
A neat, small-scale domestic residence. Features include a tidy upstairs room with a window and a table, a door, a chimney, and a roof with slates. The interior becomes physically constrained as the protagonist grows, forcing her into awkward positions against walls, windows, and chimneys.

**Lighting & Atmosphere:**
Domestic and cozy initially, transitioning to chaotic and claustrophobic during the "siege." Lighting shifts from soft window light to the frantic energy of pebbles being thrown through glass.

**Scale Cues & Anchors:**
- Brass plate reading "W. RABBIT" at the entrance.
- A table positioned by a window.
- Tiny white kid gloves and a fan on the table.
- The chimney serves as a vertical transit point for characters.
- Extreme scale shifts: from a standard room to a space where a single limb blocks a window or an elbow blocks a door.

**Descriptive Noun Phrases:**
neat little house, brass nameplate, tidy upstairs room, cucumber-frame window, stone chimney, loose roof slates, transforming pebbles, tiny white kid gloves.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thick_wood
[[SECTION markdown]]
# Thick Wood

**Role:** Secondary setting (transit and refuge)

**Architecture & Geography:**
A dense, overgrown woodland area. Features large-scale flora such as massive buttercups and towering mushrooms that dwarf the protagonist.

**Lighting & Atmosphere:**
Dappled sunlight through heavy foliage; sense of overwhelming scale and natural unpredictability. The atmosphere shifts from a place of refuge to one of discovery.

**Scale Cues & Anchors:**
- Enormous puppy appearing from the undergrowth.
- A large buttercup used as a resting point.
- A massive mushroom cap serving as a platform for characters.

**Descriptive Noun Phrases:**
thick woodland, oversized flora, giant buttercup, towering mushroom cap, dappled forest floor, dense undergrowth.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
