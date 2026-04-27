# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:05:54.037250+00:00
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
Project slug: wizard_of_oz

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

**Setting:** A grassy field near a river, adjacent to a poppy bed.

**Characters:** 
- Dorothy
- Scarecrow
- Tin Woodman
- Toto
- The Queen of the Field Mice (and her subjects)
- The Cowardly Lion (unconscious)

**Events:**
- While traveling near the river, the Tin Woodman kills a large yellow Wildcat that was attempting to eat a small field mouse.
- The mouse reveals herself to be the Queen of all the Field Mice and pledges her people's service to the Woodman.
- Toto attempts to chase the mice, but the Woodman protects them from the dog.
- To repay the favor, the Scarecrow asks the mice to help rescue the Cowardly Lion, who is trapped in a sleep-inducing poppy bed.
- The Tin Woodman constructs a wooden truck using tree limbs and pegs.
- Thousands of mice arrive, each bringing a piece of string to act as harness lines for the vehicle.
- Dorothy wakes up from her own poppy-induced sleep to find the mice gathered around her.
- The mice, assisted by the pushing of the Scarecrow and Woodman, successfully pull the heavy Lion out of the poppy field and into the fresh air of the green fields.
- After the rescue, the Queen of the Mice promises future assistance before departing with her subjects.
- The group settles down to wait for the Lion to awaken.
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
| poppy_field_bed | A dense, sleep-inducing floral expanse. |
| grassy_riverbank_meadow | A lush transit area adjacent to a river and poppy beds. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: poppy_field_bed

[[SECTION markdown]]

# Poppy Field Bed

**Role:** Secondary / Hazard Setting

**Architecture or Geography:** A dense, sprawling expanse of vibrant red poppies; thick floral growth that creates a soft but treacherous terrain.

**Lighting and Atmosphere Cues:** Drowsy, heavy atmosphere; warm, saturated colors; hazy light filtered through thick petals; a sense of overwhelming lethargy and scent-heavy air.

**Scale Cues and Recurring Environmental Anchors:** Large-scale floral canopy; individual poppy heads appearing massive relative to small creatures (mice); a sea of red that obscures the ground.

**Descriptive Noun Phrases:** Saturated crimson poppy expanse, sleep-inducing floral thicket, dense red petal carpet, heavy scented meadow.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: grassy_riverbank_meadow

[[SECTION markdown]]

# Grassy Riverbank Meadow

**Role:** Primary / Transit Setting

**Architecture or Geography:** Open green fields adjacent to a flowing river; transition zone between the wilder poppy beds and the open road.

**Lighting and Atmosphere Cues:** Bright, natural daylight; fresh air; clear visibility; lively and restorative atmosphere compared to the poppy field.

**Scale Cues and Recurring Environmental Anchors:** Wide-open horizon; riverbank edge; patches of tall grass; large scale suitable for vehicle construction (wooden truck).

**Descriptive Noun Phrases:** Lush green meadow, sun-drenched riverbank, open grassy clearing, verdant transit field.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
