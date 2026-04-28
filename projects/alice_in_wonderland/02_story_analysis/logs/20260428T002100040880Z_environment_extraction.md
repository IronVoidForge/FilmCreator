# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:21:00.040880+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH012

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



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

**Setting:** A courtroom where a jury sits in a box; later, a riverbank under trees as the sun sets.

**Characters:**
- **Alice:** Currently at her full size (nearly two miles high), then shrinking back to normal size.
- **The King:** An authoritative but somewhat bumbling figure who reads from a notebook and issues rules.
- **The Queen:** A temperamental ruler prone to sudden outbursts of anger.
- **The White Rabbit:** The court official/messenger, respectful yet hurried.
- **The Knave:** The prisoner, made of cardboard.
- **The Jury/Lizard (Bill):** A group of creatures; the Lizard is a specific jury member who gets knocked over and then has ink spilled on him by the Queen.
- **Alice's Sister:** Appears at the end in the real world.

**Key Events:**
1. **The Accident:** Alice, growing large, accidentally tips over the jury-box while jumping up. The jurymen fall out like goldfish; one is a Lizard (Bill) who is placed head-downward and then later has an inkstand thrown at him by the Queen.
2. **Rule 42:** The King reads "Rule Forty-two," stating those over a mile high must leave. Alice argues she is nearly two miles high, leading to a debate on the validity of the rule.
3. **The Evidence:** The White Rabbit presents a piece of paper—a set of verses found in the prisoner's possession. 
4. **Reading the Verses:** The White Rabbit reads a cryptic poem regarding "she," "him," and "the tarts." The King attempts to interpret the verses as evidence of the Knave's guilt regarding the stolen tarts.
5. **The Conflict:** Alice challenges the meaninglessness of the verses. The Queen, furious at the interruption, orders "Off with her head!" 
6. **The Escape/Awakening:** Alice tells the cards they are nothing but a pack of cards; the cards fly at her, causing her to wake up on the riverbank in the real world.
7. **The Epilogue:** Alice tells her sister about the dream. The sister watches the sunset, reflecting on how the sounds of the natural world (rustling grass, sheep-bells) mirror the sounds of Wonderland.

**Visual/Continuity Elements:**
- **Scale Shift:** Alice starts huge, causing the jury to fall; she ends as a normal girl in the real world.
- **The Jury Box:** A structure that is tipped over and then restored.
- **The Verses:** A physical piece of paper read by the White Rabbit.
- **The Knave's Physicality:** He is made of cardboard, making his "lack of ability to swim" a literal visual gag.
- **The Transition:** The transition from the "pack of cards" flying at Alice to her waking up on the grass serves as the bridge between the dream and reality.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [courtroom_jury_box_setting](#courtroom_jury_box_setting)
- [riverbank_sunset_setting](#riverbank_sunset_setting)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: courtroom_jury_box_setting

[[SECTION markdown]]

# Courtroom Jury Box Setting

**Role:** Primary setting (Dream/Fantasy)

**Architecture or Geography:** A surreal, oversized courtroom space centered around a jury-box structure. The scale is distorted by Alice's massive size; the box is a wooden structure containing various small creatures acting as jurors.

**Lighting and Atmosphere Cues:** High-contrast, theatrical lighting with sharp shadows. The atmosphere is one of chaotic authority—tense, bureaucratic, yet absurdly fragile.

**Scale Cues and Recurring Environmental Anchors:** Alice's massive scale (two miles high) dwarfs the jury box; the jury members are small, falling out like goldfish when tipped. The Knave is a flat, cardboard figure.

**Useful Descriptive Noun Phrases:**
- Oversized wooden jury box
- Chaotic courtroom assembly
- Cardboard prisoner
- Tiny, fluttering jurymen
- Surreal legal hall

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: riverbank_sunset_setting

[[SECTION markdown]]

# Riverbank Sunset Setting

**Role:** Secondary setting (Real World)

**Architecture or Geography:** A natural riverbank with lush grass and overhanging trees. The terrain is soft and organic.

**Lighting and Atmosphere Cues:** Warm, golden hour lighting from a setting sun. The atmosphere is peaceful, nostalgic, and grounded in the real world, contrasting with the dream sequence.

**Scale Cues and Recurring Environmental Anchors:** Human-scale environment; Alice's normal size. Sounds of rustling grass and distant sheep-bells provide an auditory anchor to the natural landscape.

**Useful Descriptive Noun Phrases:**
- Golden hour riverbank
- Rustling tall grass
- Sun-drenched meadow
- Soft evening shadows
- Naturalistic pastoral landscape

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
