# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:07:00.675373+00:00
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
- The protagonist receives a set of Martian warrior's arms and ornaments from a respectful yet menacing warrior.
- Sola and other women remodel the armor to fit the protagonist's smaller frame.
- The protagonist undergoes intensive combat training in the plaza with Martian youths, guided by Sola.
- Through persistent study, the protagonist masters the Martian language, allowing him to eavesdrop on the adults in his sleeping quarters.
- During a nighttime conversation, the protagonist learns through Sarkoja that the beautiful Red female prisoner is being taken to Thark to be executed in the great games rather than held for ransom.
- Sola expresses her sympathy for the prisoner and her disdain for the constant, senseless bloodshed of Martian life, causing a rift with the other women.
- The protagonist resolves to eventually ask Sola for help in escaping the Green Martians.

**Characters:**
- **The Protagonist:** An Earthman learning Martian combat skills and language; observant and calculating.
- **Sola:** A female Green Martian who shows maternal kindness to the protagonist and expresses empathy for the Red prisoner, despite social pressure to be ruthless.
- **Sarkoja:** An older, more hardened female Martian who reprimands Sola for her "weak" sentiments.
- **The Red Prisoner:** A beautiful captive of the Red Martians whose fate is to die in public games.
- **Other Women/Youths:** Members of the communal living quarters who serve as artisans and combat instructors.

**Settings:**
- **The Plaza:** The training ground where the protagonist practices with weapons.
- **The Sleeping Quarters:** A communal domicile shared by several females, young Martians, the protagonist, Sola, and Woola the hound.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [martian_plaza](#martian_plaza)
- [communal_sleeping_quarters](#communal_sleeping_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza

[[SECTION markdown]]

# Martian Plaza

**Role:** Primary (Training/Social)

**Architecture or Geography:** An open, expansive outdoor training ground used for martial instruction and communal gathering. Likely characterized by hard-packed Martian soil or stone surfaces suitable for combat drills.

**Lighting and Atmosphere Cues:** Bright, harsh Martian sunlight; high visibility; dusty atmosphere stirred by movement and combat training.

**Scale Cues and Recurring Environmental Anchors:** Large open scale; populated by groups of Martian youths and instructors; central area for weapon practice.

**Descriptive Noun Phrases:** Sun-drenched martial plaza, dust-mote filled training ground, wide Martian expanse, stone-hard combat floor, communal assembly space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: communal_sleeping_quarters

[[SECTION markdown]]

# Communal Sleeping Quarters

**Role:** Secondary (Domestic/Intimate)

**Architecture or Geography:** A shared, multi-occupant domicile. Contains areas for sleeping, garment/armor modification, and social interaction among the female Martians and youths.

**Lighting and Atmosphere Cues:** Dimly lit at night; intimate and enclosed; shadows cast by communal living activities; quiet but prone to eavesdropping opportunities.

**Scale Cues and Recurring Environmental Anchors:** Human-scale interior; crowded with inhabitants (females, youths, protagonist, and Woola); domestic tools for armor remodeling.

**Descriptive Noun Phrases:** Shared Martian domicile, dim communal quarters, cramped sleeping chamber, shadow-filled living space, multi-occupant Martian dwelling.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
