# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:35:00.533764+00:00
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

**Location: The White Rabbit’s House (Interior)**
*   **Event:** The White Rabbit enters, frantic and muttering about the Duchess and his lost items (fan and white kid gloves). 
*   **Character Entrance/Interaction:** Alice observes the Rabbit; he mistakes her for his housemaid, "Mary Ann," and commands her to fetch the items. Alice complies out of fear/confusion.
*   **Setting Shift:** Alice enters a neat house with a brass plate reading "W. RABBIT." She moves upstairs to a tidy room containing a table by a window.
*   **Object Interaction:** On the table, Alice finds a fan and several pairs of tiny white kid gloves. Near a looking-glass, she finds an unlabeled bottle.
*   **Transformation 1 (Growth):** Alice drinks from the bottle. She rapidly grows until her head presses against the ceiling. She is forced into uncomfortable positions: kneeling, lying down with an elbow against the door, and eventually sticking one arm out the window and one foot up the chimney to fit.
*   **Character Interaction/Conflict:** The Rabbit arrives at the door. Because Alice's elbow blocks it, he decides to enter through the window. 
*   **Action/Sound Event:** Alice reaches out a hand toward the window; she hears a shriek and the sound of breaking glass (implied cucumber-frames).
*   **Character Reveal/Dialogue:** A new character, Pat (a laborer), is introduced via dialogue. The Rabbit and Pat discuss the "arm" filling the window.
*   **Action/Sound Event:** Alice reaches out again; two shrieks and more breaking glass are heard.
*   **Event (The Chimney):** A group of animals arrives with ladders and ropes to attack the house. They decide to send a character named Bill down the chimney. 
*   **Action/Interaction:** Alice, positioned in the chimney, delivers a sharp kick to the scrambling animal above her.
*   **Outcome:** "Bill" (a small lizard) is kicked out of the chimney and into the crowd. The Rabbit threatens to burn the house down.
*   **Transformation 2 (Shrinking):** The Rabbit throws a barrowful of pebbles through the window. As they hit the floor, they transform into little cakes. Alice eats one cake and shrinks to a manageable size.
*   **Exit:** Alice runs out of the house, passing a crowd of animals holding the injured Bill.

**Location: The Wood (Exterior)**
*   **Setting Shift:** Alice escapes into a thick wood to avoid the crowd.
*   **Character Interaction/Conflict:** An enormous puppy discovers Alice. Alice attempts to play with it using a stick to distract it, dodging behind a large thistle to avoid being trampled. 
*   **Action/Exit:** Once the puppy settles down, Alice runs away until she is out of breath.
*   **Location Subzone:** Alice rests against a buttercup in a clearing.
*   **Object Interaction/Reveal:** Alice finds a large mushroom. She climbs onto tiptoe to peer over the edge of the cap.
*   **Character Reveal:** On top of the mushroom, Alice discovers a large blue Caterpillar sitting and smoking a long hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [white_rabbits_house](white_rabbits_house)
- [the_wood](the_wood)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: white_rabbits_house
[[SECTION markdown]]
# White Rabbit's House

**Role:** Primary Setting

**Architecture & Geography:**
A neat, domestic interior featuring a tidy room with a table positioned by a window. The space includes a doorway, a chimney, and a looking-glass. The architecture feels constrained once the occupant grows, creating a sense of claustrophobia between the floor and the ceiling.

**Lighting & Atmosphere:**
Domestic and bright, likely filtered through a window. The atmosphere shifts from orderly and quiet to chaotic, frantic, and cramped as Alice's physical scale changes relative to the room.

**Scale Cues & Anchors:**
- A table by a window.
- A looking-glass (mirror).
- A chimney flue.
- Small domestic items: fan, tiny white kid gloves, unlabeled bottle, pebbles/cakes.
- The ceiling (acting as a physical limit for the character).

**Descriptive Noun Phrases:**
Neat domestic interior, brass nameplate, window-side table, looking-glass, cramped attic room, chimney flue, tiny white gloves, oversized occupant in small room.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: the_wood
[[SECTION markdown]]
# The Wood

**Role:** Secondary / Transit Setting

**Architecture & Geography:**
A thick, dense woodland featuring clearings and varied flora. The terrain includes large thistles, buttercup patches, and significant fungal growths like large mushrooms.

**Lighting & Atmosphere:**
Dappled sunlight through thick foliage; wild, unpredictable, and overwhelming. The atmosphere is one of escape and sudden encounters with oversized fauna.

**Scale Cues & Anchors:**
- Large thistles (used for hiding).
- Buttercup patches (resting spots).
- Enormous mushrooms (acting as platforms/vantage points).
- Dense thickets.

**Descriptive Noun Phrases:**
Thick woodland, dappled forest light, giant thistle, buttercup clearing, massive mushroom cap, dense foliage, overgrown forest floor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
