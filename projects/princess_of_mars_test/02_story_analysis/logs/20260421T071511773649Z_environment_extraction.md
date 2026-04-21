# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:15:11.773649+00:00
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

Chapter id: CH010

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

**Chapter Title:** Champion and Chief
**Setting:** The city of the Tharks (Green Martians); specifically, the outskirts near low hills/ravines and the interior audience chamber of Lorquas Ptomel.

**Characters:**
*   **John Carter:** The protagonist; an Earthman who has mastered some Martian tongue and is learning the social codes of Barsoom.
*   **Woola:** A large, loyal Martian creature (white ape/hound-like) serving as Carter's guardian.
*   **Sola:** A kind and civilized green Martian woman who acts as Carter's instructress.
*   **Dejah Thoris:** The Princess of Helium; a captive red-skinned human woman.
*   **Tars Tarkas:** A Thark warrior/chieftain who oversees Carter's custody.
*   **Lorquas Ptomel:** A Thark chieftain presiding over the council.
*   **Sarkoja:** A cruel green Martian woman acting as a guard for the prisoner.

**Key Events:**
1.  **Bonding with Woola:** Early in the morning, Carter explores the city limits. He attempts to test his bond with Woola through affection rather than command. The interaction succeeds, establishing a deep, mutual understanding and loyalty between the man and the beast.
2.  **The Audience Chamber Observation:** Carter observes the trial of Dejah Thoris. He witnesses the brutality of the green Martian guards (specifically Sarkoja) and hears Dejah Thoris deliver a sophisticated plea for peace and scientific cooperation to the Thark council.
3.  **The Violent Outburst:** During a moment of tension, a young Thark warrior strikes Dejah Thoris across the face in a display of "mirthless laughter." 
4.  **Carter's Intervention:** Driven by rage, Carter intervenes and engages the warrior in single combat. Despite the size difference, Carter kills the warrior using superior technique and ferocity.
5.  **Ascension to Chieftain Status:** By killing a warrior, Carter inadvertently wins the "spoils" and honors of the deceased. He is recognized by the Tharks as a chieftain, granting him a degree of freedom and respect within their society.
6.  **The Confrontation with Tars Tarkas:** Tars Tarkas questions Carter's sudden proficiency in the language and warns him of the dangers of his "unprecedented temerity." Carter asserts his moral code, declaring that he will protect Dejah Thoris from any future insult or injury.
7.  **Departure:** Recognized as a man of valor, Carter and Dejah Thoris (accompanied by Woola) exit the chamber, with Carter assuming the responsibility of her protector under his new status as a Thark chieftain.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_outskirts_ravines](thark_outskirts_ravines)
- [thark_audience_chamber](thark_audience_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_outskirts_ravines

[[SECTION markdown]]

# Thark Outskirts Ravines

**Role:** Primary / Transit Setting

**Architecture or Geography:** Rugged Martian terrain consisting of low, rolling hills and deep, jagged ravines. The landscape is characterized by rocky outcrops and the outskirts of the Thark city limits.

**Lighting and Atmosphere Cues:** Harsh, direct Martian sunlight; dusty atmosphere with high visibility; open-air exposure.

**Scale Cues and Recurring Environmental Anchors:** Expansive vistas of barren hills; narrow ravine passages; proximity to the sprawling, primitive Thark settlement.

**Descriptive Noun Phrases:** Jagged ravines, rolling Martian hills, rocky outcrops, sun-scorched terrain, dusty outskirts, desolate canyons.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_audience_chamber

[[SECTION markdown]]

# Thark Audience Chamber

**Role:** Primary Setting

**Architecture or Geography:** A large, imposing interior chamber designed for council and judgment. The space is built to accommodate the massive scale of Green Martian warriors.

**Lighting and Atmosphere Cues:** Dimly lit interior; shadows cast by high ceilings or structural elements; atmosphere of tension, brutality, and formal gravity.

**Scale Cues and Recurring Environmental Anchors:** Large central floor for combat/trials; elevated areas for chieftains; cavernous volume to accommodate Thark warriors.

**Descriptive Noun Phrases:** Cavernous council chamber, brutalist interior, chieftain's dais, shadowed hall, primitive assembly space, high-ceilinged stone chamber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
