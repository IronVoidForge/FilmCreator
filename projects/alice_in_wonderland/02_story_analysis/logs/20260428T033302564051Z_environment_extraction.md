# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:33:02.564051+00:00
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

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Location:** A riverbank; a circular race-course marked out on the ground.
**Characters:** 
- Alice (Human girl)
- Mouse (Authority figure, storyteller)
- Dodo (Leader of the Caucus-race)
- Lory (Sulky bird)
- Duck (Literal-minded bird)
- Eaglet (Mocking bird)
- Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab, and others.

**Events:**
1. **The Wet Assembly:** A group of animals and birds (draggled feathers, wet fur) assemble on a bank, visibly uncomfortable and cross due to being wet. 
2. **Argument with Lory:** Alice engages in a verbal dispute with the Lory regarding its age; the Lory becomes sulky and refuses to answer.
3. **The Mouse's "Dry" Story:** The Mouse calls for order and attempts to dry everyone by reciting a historical text about William the Conqueror. 
4. **Interruption/Confusion:** The Duck interrupts the Mouse, misunderstanding the word "it." Alice reports she is still wet.
5. **The Caucus-race Proposal:** The Dodo moves to adjourn the meeting for more "energetic remedies," proposing a Caucus-race. The Eaglet mocks the Dodo's vocabulary.
6. **The Race:** The Dodo marks a circular course. The animals run in no specific order, starting and stopping at will for approximately thirty minutes until they are dry.
7. **Prize Distribution:** The Dodo declares everyone a winner. Alice is designated as the prize-giver. 
8. **Object Interaction (Comfits):** Alice retrieves a box of comfits from her pocket and distributes them to the group. Large birds struggle to taste theirs; small ones choke.
9. **Object Interaction (Thimble):** The Mouse insists Alice receives a prize. Alice produces a thimble from her pocket. The Dodo presents it back to her as an "elegant thimble" in a formal ceremony. Alice bows and accepts it.
10. **The Mouse's Tale:** The group settles into a ring. The Mouse begins a "long and sad tale." 
11. **Linguistic Misunderstanding:** Alice confuses the Mouse's "tale" (story) with its physical "tail." She attempts to help by offering to undo a "knot" she thinks she sees in the story/tail.
12. **The Mouse Exits:** Offended by Alice's perceived nonsense, the Mouse growls and walks away from the group.
13. **Crab Argument:** An Old Crab lectures a Young Crab on temper; they bicker briefly.
14. **The Dinah Reveal:** Alice mentions her cat, Dinah, and how she catches mice/birds. 
15. **Mass Exit:** The mention of the cat causes panic. Birds (Magpie, Canary) use various excuses to flee the area immediately.
16. **Alice's Solitude:** Alice is left alone on the bank, feeling lonely and crying. She hears distant footsteps and looks up expectantly.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [riverbank_assembly](#riverbank_assembly)
- [caucus_race_course](#caucus_race_course)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: riverbank_assembly
[[SECTION markdown]]
# Riverbank Assembly

**Role:** Primary setting

**Architecture or Geography:** 
A natural, sloping bank adjacent to a body of water. The terrain is uneven and composed of damp earth and vegetation suitable for a gathering of various animals and birds.

**Lighting and Atmosphere Cues:** 
Damp, humid, and heavy atmosphere. Post-rain or post-immersion mood. Lighting should feel diffused and slightly somber, reflecting the "draggled" and uncomfortable state of the inhabitants.

**Scale Cues and Recurring Environmental Anchors:** 
The scale is grounded in the perspective of small animals (mice, birds, crabs) and a single human girl. Key anchors include the proximity to the water's edge and the presence of various wet textures (feathers, fur).

**Descriptive Noun Phrases:** 
Damp riverbank, sloping muddy shore, sodden vegetation, draggled feathers, wet animal fur, humid riverside atmosphere, natural assembly point.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: caucus_race_course
[[SECTION markdown]]
# Caucus-Race Course

**Role:** Secondary / Transit setting

**Architecture or Geography:** 
A makeshift, circular track marked out directly on the ground of the riverbank. It is a non-standard, informal racing circuit defined by simple markings in the dirt/sand.

**Lighting and Atmosphere Cues:** 
Energetic but chaotic. The atmosphere shifts from the somber dampness of the assembly to a frantic, disorganized movement as animals run in no specific order.

**Scale Cues and Recurring Environmental Anchors:** 
A small-scale circular perimeter. The anchor is the "circular course" marked on the ground which dictates the movement of the crowd.

**Descriptive Noun Phrases:** 
Circular dirt track, makeshift racecourse, hand-marked ground circle, chaotic racing path, trampled riverbank earth.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
