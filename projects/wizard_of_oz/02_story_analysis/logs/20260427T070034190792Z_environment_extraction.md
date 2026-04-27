# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:00:34.190792+00:00
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

Chapter id: CH006

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

**Setting:** A thick, dark forest where the Yellow Brick Road is partially obscured by dried branches and dead leaves.

**Characters:** 
- Dorothy
- Toto
- Scarecrow
- Tin Woodman
- The Cowardly Lion (New Character)

**Events:**
- While walking through the woods, the group is ambushed by a large Lion that attacks the Scarecrow and the Tin Woodman.
- Dorothy defends Toto by slapping the Lion on the nose and calling him a coward.
- The Lion reveals his true nature: despite being the "King of Beasts," he is paralyzed by fear and lacks courage, which makes him deeply unhappy.
- After hearing about the group's quest to see Oz, the Lion decides to join them to ask for courage.
- During their continued journey, the Tin Woodman accidentally steps on a beetle; his subsequent tears of regret cause his jaw to rust shut.
- The Scarecrow uses the oil-can to fix the Tin Woodman, and the Woodman vows to walk more carefully to avoid harming any living creatures.
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
| thick_dark_forest | A dense, overgrown woodland path partially obscured by debris. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thick_dark_forest

[[SECTION markdown]]

# Thick Dark Forest

**Role:** Primary setting for encounter and transit.

**Architecture or Geography:** A dense, claustrophobic woodland characterized by a heavy canopy of interlocking branches. The ground is uneven, covered in a thick layer of dried leaves, decaying organic matter, and fallen branches that partially obscure the Yellow Brick Road.

**Lighting and Atmosphere Cues:** Dim, dappled lighting filtering through a thick ceiling of foliage. High-contrast shadows created by skeletal branches. A sense of oppressive gloom and dampness.

**Scale Cues and Recurring Environmental Anchors:** Massive, ancient tree trunks serving as vertical anchors; the winding, partially hidden path of the Yellow Brick Road acting as the primary directional guide.

**Descriptive Noun Phrases:** Dense woodland thicket, decaying forest floor, skeletal branch canopy, obscured yellow brick path, dappled gloom, overgrown forest corridor.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
