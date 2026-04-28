# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:04:53.083958+00:00
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
- Alice (human girl)
- Mouse (authoritative, prone to offense)
- Dodo (solemn, leader of the Caucus-race)
- Lory (sulky, older than Alice)
- Duck (literal-minded)
- Eaglet (skeptical, mocking)
- Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab, and others.

**Events:**
1. **The Wet Gathering:** A group of animals (birds with draggled feathers, wet fur) assembles on the bank. They are uncomfortable and cross due to being wet. 
2. **Argument with Lory:** Alice engages in a long argument with the Lory regarding its age; the Lory refuses to answer and becomes sulky.
3. **The Mouse's "Dry" Story:** The Mouse calls for order and attempts to dry everyone by reciting a historical text about William the Conqueror. 
4. **Interruption/Confusion:** The Duck interrupts the Mouse, misunderstanding the word "it." The Eaglet mocks the Dodo’s vocabulary. Alice reports she is still wet.
5. **The Caucus-Race:** The Dodo adjourns the meeting to propose a "Caucus-race." He marks out a circular course. The animals run in no specific order, starting and stopping whenever they please for thirty minutes until they are dry.
6. **Prize Distribution:** The Dodo declares everyone a winner. Alice is designated as the prize-giver. 
7. **Object Interaction (Comfits):** Alice retrieves a box of comfits from her pocket and distributes them to the group. There is chaos/choking among the small animals and complaints from large birds.
8. **Object Interaction (Thimble):** The Mouse insists Alice receives a prize. Alice produces a thimble. The Dodo leads the group in a formal presentation, returning the thimble to Alice as an "elegant" gift. Alice bows and accepts it solemnly.
9. **The Mouse's Tale:** The animals sit in a ring. The Mouse begins telling a "long and sad tale." 
10. **Misunderstanding/Conflict:** Alice confuses the Mouse's "tale" (story) with its physical "tail." She attempts to help by trying to "undo a knot," which the Mouse perceives as an insult. The Mouse exits, walking away angrily.
11. **The Crab Argument:** As the Mouse leaves, an Old Crab scolds a Young Crab for losing her temper.
12. **The Dinah Reveal:** Alice mentions her cat, Dinah, and how she catches mice/birds. 
13. **Mass Exit:** The mention of a cat causes panic. Birds (Magpie, Canary) use various excuses to flee the area immediately.
14. **Alice's Solitude:** Alice is left alone on the bank, crying due to loneliness and the absence of Dinah. She hears footsteps in the distance.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [riverbank_setting](riverbank_setting)
- [caucus_race_course](caucus_race_course)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: riverbank_setting
[[SECTION markdown]]
# Riverbank Setting

**Role:** Primary setting.

**Architecture or Geography:** A natural, sloping bank adjacent to a body of water; soft earth and potentially muddy edges where the animals have gathered.

**Lighting and Atmosphere Cues:** Damp, heavy atmosphere; post-rain/post-swim humidity; sense of discomfort from wetness; transition from chaotic social gathering to lonely, somber solitude.

**Scale Cues and Recurring Environmental Anchors:** Low-angle perspective relative to the small animal inhabitants; patches of damp earth; proximity to water's edge.

**Descriptive Noun Phrases:** Damp riverbank, sodden earth, muddy shoreline, weeping girl on a bank, draggled feathers and fur, post-swim gathering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: caucus_race_course
[[SECTION markdown]]
# Caucus-Race Course

**Role:** Secondary / Activity setting.

**Architecture or Geography:** A circular track marked out directly on the ground/dirt; non-linear and informal geometry.

**Lighting and Atmosphere Cues:** High energy, chaotic movement; dusty or muddy tracks from running feet; sense of arbitrary rules and nonsensical motion.

**Scale Cues and Recurring Environmental Anchors:** Small-scale circular boundary; a ring of animals running in no specific direction; central area for prize distribution.

**Descriptive Noun Phrases:** Circular dirt track, makeshift racecourse, trampled ground, chaotic animal loop, prize-giving circle.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
