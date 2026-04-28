# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:10:25.503774+00:00
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

Chapter id: CH007

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

**Setting:**
*   A large table set out under a tree in front of a house. 
*   The table is crowded with tea-things (tea, bread-and-butter, milk-jug).
*   Later: A wooded area containing a tree with a door built into it.
*   Final Location: The long hall with the little glass table, leading to the garden via a small door.

**Characters:**
*   **Alice:** Observant, easily frustrated by nonsense, attempts to maintain politeness and logic.
*   **The Hatter:** Eccentric, irritable, obsessed with time/clocks, prone to riddles without answers.
*   **The March Hare:** Erratic, defensive, participates in the nonsensical social cues of the party.
*   **The Dormouse:** Constantly sleeping or semi-conscious; provides interrupted, surreal storytelling.

**Key Events & Scene Beats:**
*   **Arrival at the Tea Party:** Alice approaches a large table under a tree where the March Hare, Hatter, and a sleeping Dormouse are crowded into one corner. They shout "No room!" despite there being plenty of space. Alice sits in a large armchair at the end of the table.
*   **The Failed Social Exchange:** The March Hare offers wine that isn't there; Alice calls him uncivil; the Hare retorts about her sitting without an invitation.
*   **The Riddle:** The Hatter makes a personal remark about Alice's hair and poses the riddle: "Why is a raven like a writing-desk?" He admits he doesn't know the answer.
*   **The Broken Watch:** The Hatter checks his watch, which shows the day of the month but not the time. He shakes it and holds it to his ear. He blames "butter" for the watch being two days wrong. The March Hare dips the watch into a cup of tea.
*   **The Personification of Time:** The Hatter explains that Time is a person ("him") with whom he quarreled last March at the Queen of Hearts' concert. Because of this quarrel, Time refuses to do anything for him, and it is perpetually six o'clock (tea-time).
*   **The Dormouse's Story:** After being pinched awake by the Hatter and Hare, the Dormouse tells a story about three sisters (Elsie, Lacie, and Tillie) who lived at the bottom of a treacle-well. Alice interrupts with logical questions about eating treacle and drawing from a well.
*   **The Seat Rotation:** To get a "clean cup," the Hatter initiates a move: The Hatter moves, the Dormouse follows him, the March Hare moves to the Dormouse's spot, and Alice reluctantly moves to the March Hare's spot (where she encounters spilled milk).
*   **Alice's Departure:** After being told "Then you shouldn't talk" by the Hatter, Alice leaves in disgust. She looks back once to see them trying to stuff the Dormouse into a teapot.
*   **The Tree Door:** Walking through the woods, Alice finds a door built into a tree. 
*   **Return to the Garden:** Alice enters the door, finds herself in the long hall, uses the golden key on the garden door, and nibbles the mushroom piece from her pocket to shrink to one foot tall. She successfully enters the beautiful garden.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [tea_party_glade](tea_party_glade)
- [wooded_pathway](wooded_pathway)
- [hall_of_doors](hall_of_doors)
- [the_garden](the_garden)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: tea_party_glade
[[SECTION markdown]]
# Tea Party Glade

**Role:** Primary Setting

**Architecture or Geography:**
An outdoor clearing featuring a large, sprawling table set beneath the shade of a massive tree. The setting is characterized by an organized chaos of mismatched tea-things, including milk jugs, bread-and-butter plates, and various teacups.

**Lighting and Atmosphere Cues:**
Dappled sunlight filtering through heavy foliage; a sense of stagnant, perpetual late-afternoon light (perpetual 6:00 PM); surreal and nonsensical social atmosphere.

**Scale Cues and Recurring Environmental Anchors:**
A large armchair at the end of the table; a crowded corner of the table where the hosts reside; spilled milk patches on the tablecloth.

**Descriptive Noun Phrases:**
Dappled woodland shade, cluttered tea table, mismatched porcelain, oversized armchair, sprawling tree canopy, stagnant tea-time glade.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: wooded_pathway
[[SECTION markdown]]
# Wooded Pathway

**Role:** Transit Setting

**Architecture or Geography:**
A dense, natural woodland area. The terrain is organic and uneven, featuring thick vegetation and large trees.

**Lighting and Atmosphere Cues:**
Natural forest lighting; sense of transition and movement away from the social chaos of the tea party.

**Scale Cues and Recurring Environmental Anchors:**
A specific tree containing a built-in door serving as a threshold between the woods and the interior structures.

**Descriptive Noun Phrases:**
Dense woodland, organic forest floor, tree-integrated door, leafy canopy, transitional forest path.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hall_of_doors
[[SECTION markdown]]
# Hall of Doors

**Role:** Secondary Setting / Transit

**Architecture or Geography:**
A long, narrow interior hallway. The architecture is characterized by its length and the presence of various doors, including a small door leading to an external area. Includes a small glass table.

**Lighting and Atmosphere Cues:**
Interior lighting; sense of enclosure and scale shifts as characters change size.

**Scale Cues and Recurring Environmental Anchors:**
A long hallway perspective; a small glass table; the garden door at the end of the corridor.

**Descriptive Noun Phrases:**
Elongated hallway, miniature glass table, threshold corridor, architectural transition.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: the_garden
[[SECTION markdown]]
# The Garden

**Role:** Primary Setting (Destination)

**Architecture or Geography:**
An expansive, beautiful garden visible through a small door. It represents the goal of Alice's journey in this chapter.

**Lighting and Atmosphere Cues:**
Bright, vibrant, and inviting lighting; high-saturation colors to contrast with the previous surreal/cluttered settings.

**Scale Cues and Recurring Environmental Anchors:**
The garden appears massive and lush from the perspective of a shrunken Alice.

**Descriptive Noun Phrases:**
Lush botanical garden, vibrant floral landscape, sun-drenched garden, miniature-scale paradise.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
