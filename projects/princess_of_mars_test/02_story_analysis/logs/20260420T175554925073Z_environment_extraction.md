# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:55:54.925073+00:00
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

**Events:**
John Carter is summoned to an audience with Lorquas Ptomel, a Tharkian leader. Ptomel confronts Carter regarding his status as a prisoner who nonetheless commands respect, and accuses him of plotting an escape with Dejah Thoris (the "red girl"). Ptomel warns that while they do not wish to fight among themselves, Carter will be killed if he attempts to escape or attacks a Thark in self-defense. Carter realizes that Sarkoja, a powerful female figure, has been spying on him and reporting his intentions to undermine him.

Following the audience, Tars Tarkas approaches Carter and offers him quarters within the Tharkian buildings. Carter selects a room on the third floor of an adjoining building to remain close to Dejah Thoris. He receives his spoils of war—weapons, silks, furs, and food—from the retinues of the two chieftains he previously defeated. Carter also takes responsibility for the women and youths belonging to those fallen chieftains, assigning them duties within his new quarters.

**Characters:**
* **John Carter:** A Tharkian chieftain and human; increasingly focused on escaping with Dejah Thoris.
* **Lorquas Ptomel:** A fierce Tharkian leader who issues a formal warning to Carter regarding escape and combat.
* **Sarkoja:** Mentioned as a powerful female influence behind Tars Tarkas, suspected of betraying Carter.
* **Tars Tarkas:** A Tharkian warrior who treats Carter with respect and assists him in settling into his new quarters.
* **Dejah Thoris:** The captive red Martian princess; the primary motivation for Carter's escape plans.

**Settings:**
* **The Audience Chamber:** Where Lorquas Ptomel delivers his warning.
* **The Tharkian Plaza/Buildings:** A complex of structures featuring winding corridors, multi-story apartments, and an overgrown central court filled with fountains and statuary. The setting reflects a once-beautiful civilization now characterized by martial austerity.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description |
| :--- | :--- |
| tharkian_audience_chamber | Formal martial chamber used for leadership confrontations. |
| tharkian_residential_complex | Multi-story stone structures with winding corridors and overgrown courtyards. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: tharkian_audience_chamber

[[SECTION markdown]]

# Tharkian Audience Chamber

**Role:** Primary (Ceremonial/Political)

**Architecture/Geography:** A formal, imposing chamber designed for leadership confrontations and the delivery of decrees. The space is structured to emphasize the authority of the Tharkian leaders.

**Lighting and Atmosphere:** Austere, heavy, and intimidating. The atmosphere is thick with martial tension and political scrutiny.

**Scale Cues:** Large-scale interior designed to accommodate chieftains and their retinues; high ceilings or wide floor plans that dwarf individual occupants.

**Prompt Phrases:** Martial audience chamber, Tharkian leadership hall, imposing stone architecture, formal confrontation setting, austere ceremonial space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: tharkian_residential_complex

[[SECTION markdown]]

# Tharkian Residential Complex

**Role:** Primary (Living/Transit)

**Architecture/Geography:** A complex of multi-story stone buildings featuring winding corridors and interconnected apartments. Includes an overgrown central court characterized by ancient fountains and weathered statuary.

**Lighting and Atmosphere:** A blend of martial austerity and decaying elegance. The atmosphere is a mix of lived-in functionality and the remnants of a once-beautiful civilization.

**Scale Cues:** Multi-story verticality; sprawling layouts with interconnected corridors; large central courtyard acting as an environmental anchor.

**Prompt Phrases:** Winding stone corridors, multi-story Martian apartments, overgrown central plaza, ancient fountains and statuary, decaying martial civilization, Tharkian residential architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
