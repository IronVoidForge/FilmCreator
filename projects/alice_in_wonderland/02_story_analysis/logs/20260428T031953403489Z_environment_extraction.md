# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:19:53.403489+00:00
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

**Location:** A riverbank; wet, muddy terrain.
**Characters:** 
- Alice (human girl)
- Mouse (authority figure)
- Lory (sulky bird)
- Duck (literal-minded bird)
- Dodo (solemn leader)
- Eaglet (mocking bird)
- Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab, and others.

**Events:**
1. **The Wet Assembly:** A group of animals (birds with draggled feathers, mammals with clinging fur) are gathered on the bank, all dripping wet and uncomfortable. 
2. **Argument with Lory:** Alice engages in a verbal dispute with the Lory regarding its age; the Lory becomes sulky and refuses to answer.
3. **The Mouse's "Dry" Tale:** The Mouse calls for order and attempts to dry everyone by reciting a historical text about William the Conqueror. 
4. **Linguistic Conflict:** The Duck interrupts, misunderstanding the word "it" in the history lesson; the Eaglet mocks the Dodo's vocabulary. Alice reports she is still wet.
5. **The Caucus-Race:** To solve the dryness issue, the Dodo initiates a "Caucus-race." 
    - *Action:* The Dodo marks a circular course. Animals run in no specific order, starting and stopping at will for approximately thirty minutes.
    - *Result:* Once everyone is dry, the Dodo declares the race over.
6. **Prize Distribution:** 
    - The Dodo deliberates on winners, eventually declaring "Everybody has won."
    - Alice is designated as the prize-giver.
    - Alice retrieves a box of comfits from her pocket and distributes one to each participant.
    - As a prize for herself, Alice is forced to surrender her thimble to the group; the animals present it back to her with a formal speech and cheers.
7. **The Comfit Chaos:** The animals eat the comfits, resulting in large birds complaining of lack of taste and small birds choking/requiring patting on the back.
8. **The Mouse's Tale & Misunderstanding:** 
    - The group settles into a ring for the Mouse to tell his history.
    - Alice becomes distracted by the physical appearance of the Mouse's tail, confusing "tale" (story) with "tail" (appendage).
    - Alice attempts to be helpful by offering to "undo a knot" in the story, which the Mouse perceives as an insult.
9. **The Mouse's Exit:** The Mouse growls and walks away from the group in anger.
10. **The Dinah Reveal:** 
    - While discussing the Mouse's departure, Alice mentions her pet cat, Dinah, and how she catches mice/birds.
    - *Reaction:* A "remarkable sensation" occurs; birds (Magpie, Canary) use various excuses to flee the area immediately.
11. **Alice's Solitude:** Alice is left alone on the bank, feeling lonely and crying for Dinah. 
12. **Ending Beat:** Alice hears distant pattering footsteps, looking up hopefully for a returning Mouse.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [riverbank_muddy_shore](riverbank_muddy_shore)
[[/SECTION]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: riverbank_muddy_shore
[[SECTION markdown]]
# Riverbank Muddy Shore

**Role:** Primary setting.

**Architecture or Geography:** 
A low-lying, wet riverbank characterized by muddy terrain and uneven ground. The area serves as a gathering point for various animals and is defined by its dampness and proximity to water.

**Lighting and Atmosphere Cues:** 
Damp, heavy, and uncomfortable atmosphere. Lighting should suggest an overcast or humid environment where moisture clings to surfaces. High humidity/mist potential.

**Scale Cues and Recurring Environmental Anchors:** 
The scale is grounded in the perspective of a small child and various animals; the mud and puddles act as significant physical obstacles. The circular course marked by the Dodo serves as a temporary structural anchor for movement.

**Descriptive Noun Phrases:** 
- Saturated riverbank
- Clinging mud and silt
- Draggled feathers and wet fur textures
- Damp, uneven shoreline
- Muddy assembly ground
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
