# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:03:01.536454+00:00
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

Chapter id: CH003

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

**Location:** A riverbank; a circular race-course area nearby.
**Characters:** 
- Alice (human girl)
- The Mouse (authoritative, prone to offense)
- The Lory (sulky, older bird)
- The Duck (literal-minded)
- The Dodo (solemn, leader of the Caucus-race)
- The Eaglet (skeptical/mocking bird)
- Various Birds (Magpie, Canary, etc.)
- Crabs (Old Crab and Young Crab)

**Events:**
1. **The Wet Assembly:** A group of animals and birds (draggled feathers, wet fur) assemble on a bank, visibly uncomfortable and wet. 
2. **Argument with Lory:** Alice engages in a verbal dispute with the Lory regarding its age; the Lory refuses to answer and becomes sulky.
3. **The Mouse's "Dry" History:** The Mouse calls for order. The group sits in a large ring with the Mouse in the center. The Mouse attempts to dry them by reciting a historical text about William the Conqueror. 
4. **Interruption/Confusion:** The Lory shivers at the text; the Duck interrupts, confused by the word "it"; Alice reports she is still wet.
5. **The Caucus-race Proposal:** The Dodo adjourns the meeting to propose a "Caucus-race" as a remedy for being wet. The Eaglet mocks the Dodo's vocabulary.
6. **The Race:** The Dodo marks out a circular course. The animals run in no specific order, starting and stopping at will for approximately thirty minutes until they are dry.
7. **Prize Distribution:** The Dodo declares everyone a winner. Alice is designated as the prize-giver. 
8. **Object Interaction (Comfits):** Alice retrieves a box of comfits from her pocket and distributes one to each participant. Large birds struggle to taste them; small birds choke/need patting on the back.
9. **Object Interaction (Thimble):** The Mouse insists Alice receives a prize. Alice produces a thimble. The Dodo leads the group in a formal presentation of the thimble back to Alice, which she accepts with a bow.
10. **The Mouse's Tale:** The group sits in a ring again. The Mouse begins telling a "long and sad tale." 
11. **Linguistic Misunderstanding:** Alice confuses the Mouse's "tale" (story) with its physical "tail." She interrupts the story to comment on the tail.
12. **The Conflict/Exit:** Alice attempts to help by offering to "undo a knot" in the story. The Mouse takes this as an insult and walks away from the group.
13. **Crab Argument:** As the Mouse leaves, an Old Crab scolds a Young Crab for losing its temper.
14. **The Dinah Reveal:** Alice mentions her cat, Dinah, expressing how good she is at catching birds.
15. **Mass Exit:** The mention of a cat causes panic. Birds (Magpie, Canary) use various excuses to flee the scene immediately. 
16. **Alice's Solitude:** Alice is left alone on the bank, feeling lonely and crying. She hears distant footsteps approaching.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [riverbank_assembly](#riverbank_assembly)
- [caucus_race_course](#caucus_race_course)
[[/SECTION]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: riverbank_assembly
[[SECTION markdown]]
# Riverbank Assembly

**Role:** Primary setting

**Architecture or Geography:** A natural, sloping riverbank; muddy and damp terrain. The area serves as a gathering point for the wet assembly of animals.

**Lighting and Atmosphere Cues:** Damp, heavy atmosphere; post-rain humidity; somber and uncomfortable mood due to the characters being "draggled" and wet.

**Scale Cues and Recurring Environmental Anchors:** Low-angle perspective relative to the small animals; patches of wet mud; river reeds or bank vegetation.

**Descriptive Noun Phrases:**
- Damp riverbank slope
- Muddy shoreline
- Draggled vegetation
- Saturated earth
- Riverine embankment
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: caucus_race_course
[[SECTION markdown]]
# Caucus-Race Course

**Role:** Secondary setting / Transit setting

**Architecture or Geography:** A circular, makeshift race-track marked out on the ground near the riverbank. 

**Lighting and Atmosphere Cues:** Transitioning from damp/heavy to drying/bright as the sun or air dries the participants; chaotic energy during the race.

**Scale Cues and Recurring Environmental Anchors:** A defined circular boundary; a central area for prize distribution (comfits and thimbles).

**Descriptive Noun Phrases:**
- Circular dirt track
- Arbitrary race course
- Looped path in the grass
- Ceremonial prize circle
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
