# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:43:53.282201+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH009

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

**Events:**
The protagonist receives a set of warrior's arms and ornaments from a respectful yet menacing Martian, which Sola and other women remodel to fit his smaller size. He begins intensive combat training with the Martian youth in the plaza, aided by his familiarity with Earthly weaponry. Through persistent effort, he masters the Martian language, allowing him to eavesdrop on the adults in his communal sleeping quarters. During a nighttime conversation, he learns from Sarkoja that the beautiful Red female prisoner is being transported to Thark to be executed at the great games before Tal Hajus. A heated argument breaks out between Sola and the other women; Sola defends her sympathy for the captive, expressing a philosophical disdain for the endless cycle of Martian bloodshed. This interaction confirms Sola's character and the protagonist's resolve to eventually seek her help in escaping the Green Martians.

**Characters:**
- **The Protagonist:** An Earthman undergoing combat training; successfully learns the Martian language.
- **Sola:** A female Green Martian who acts as a mentor/protector; shows unexpected empathy for the Red prisoner and expresses philosophical views on the brutality of Martian life.
- **Sarkoja:** An older, more hardened female Green Martian; critical of Sola's perceived weakness.
- **The Prisoner (Red Woman):** A beautiful captive being moved toward execution in Thark.
- **Other Females/Young Martians:** Members of the communal living group who participate in training and social discourse.

**Settings:**
- **The Plaza:** The location where the protagonist practices combat with the Martian youth.
- **Communal Sleeping Quarters:** The shared domicile where the protagonist lives with Sola, several females, young Martians, and Woola the hound; the site of the pivotal overheard conversation.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [plaza_training_grounds](plaza_training_grounds)
- [communal_sleeping_quarters](communal_sleeping_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: plaza_training_grounds

[[SECTION markdown]]

# Plaza Training Grounds

**Role:** Primary / Secondary (Activity Hub)

**Architecture or Geography:** An open, outdoor communal space; likely paved or hard-packed Martian soil suitable for combat and movement.

**Lighting and Atmosphere Cues:** Exposed to the Martian sky; bright, harsh lighting during training sessions; dusty atmosphere from physical exertion.

**Scale Cues and Recurring Environmental Anchors:** Wide expanse capable of accommodating multiple combatants and youths; central area for martial practice.

**Descriptive Noun Phrases:** Open Martian plaza, dust-swept training ground, sun-drenched combat arena, wide communal courtyard.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: communal_sleeping_quarters

[[SECTION markdown]]

# Communal Sleeping Quarters

**Role:** Primary (Social/Domestic)

**Architecture or Geography:** A shared, multi-occupant domicile; interior space designed for group living.

**Lighting and Atmosphere Cues:** Dimly lit at night; intimate but crowded atmosphere; shadows cast by communal groups.

**Scale Cues and Recurring Environmental Anchors:** Shared sleeping areas; presence of various inhabitants (females, youths, hounds); domestic clutter of a communal life.

**Descriptive Noun Phrases:** Shared Martian dormitory, dim communal quarters, group living space, interior Martian dwelling.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
