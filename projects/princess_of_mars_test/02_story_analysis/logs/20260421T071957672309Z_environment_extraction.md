# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:19:57.672309+00:00
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

Chapter id: CH011

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

**Summary:**
Following his rise in status among the Tharks, John Carter secures better living conditions for Dejah Thoris by assigning Sola to guard her. Carter moves them into a more prestigious building featuring ancient, elaborate architecture and frescoes depicting a long-extinct, fair-skinned race of Martians. During their time in the new quarters, Carter and Dejah Thoris share an intimate conversation where he reveals his true origin: he is from Earth, not the mysterious valley of Dor. Dejah Thoris expresses skepticism but ultimately chooses to believe him based on her intuition. She explains that while Barsoomians can observe Earth through advanced telescopic technology, they did not recognize Carter because he lacks the typical "unsightly" clothing and ornaments worn by most Earthmen. The chapter concludes with Dejah Thoris providing historical context regarding the evolution of the Red Martian race and the ancient civilization of Korad, just before Carter is summoned to appear before Lorquas Ptomel.

**Characters:**
- **John Carter:** An Earthman who has established himself as a high-ranking warrior among the Tharks; he reveals his extraterrestrial origins to Dejah Thoris.
- **Dejah Thoris:** A noblewoman of the Red Martians; she displays deep curiosity and empathy toward Carter and shares much of Barsoom's history.
- **Sola:** A Thark woman who acts as a protector and attendant for Dejah Thoris.
- **Sarkoja:** A hostile Thark female who remains a potential threat to the group.
- **Lorquas Ptomel:** A high-ranking leader/chieftain who summons Carter.
- **Tars Tarkas:** A prominent Thark warrior present during the summons.

**Settings:**
- **The New Quarters:** A pretentious, ancient building near the audience chamber, featuring marble ceilings, gold chains, and elaborate frescoes of a lost Martian race.
- **The Plaza/Audience Chamber:** The central hub of the Thark community where political power is wielded.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [prestigious_ancient_quarters](prestigious_ancient_quarters)
- [thark_plaza_audience_chamber](thark_plaza_audience_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: prestigious_ancient_quarters

[[SECTION markdown]]

# Prestigious Ancient Quarters

**Role:** Primary setting (intimate/domestic)

**Architecture & Geography:** An ancient, pretentious building characterized by elaborate, classical Martian architecture. Features include high marble ceilings and heavy gold chains used for structural or decorative purposes. The walls are adorned with detailed frescoes depicting a long-extinct race of fair-skinned Martians.

**Lighting & Atmosphere:** Sophisticated and historical; the atmosphere is one of faded grandeur and quiet intimacy amidst ancient stone.

**Scale & Anchors:** Large, high-ceilinged rooms that feel cavernous yet decorated; recurring anchors include the marble surfaces and the narrative frescoes on the walls.

**Prompt Phrases:** Ancient Martian architecture, marble ceilings, gold chains, historical frescoes, fair-skinned Martian murals, faded grandeur, classical stone interiors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_plaza_audience_chamber

[[SECTION markdown]]

# Thark Plaza / Audience Chamber

**Role:** Secondary setting (political/public)

**Architecture & Geography:** A central hub of the Thark community designed for political gatherings and formal summons. It serves as a communal space where power is wielded and leaders congregate.

**Lighting & Atmosphere:** Open, public, and imposing; carries the weight of social hierarchy and martial authority.

**Scale & Anchors:** Large-scale communal plaza; acts as the central nexus for Thark movement and political assembly.

**Prompt Phrases:** Thark community hub, central Martian plaza, formal audience chamber, large-scale communal space, martial political center.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
