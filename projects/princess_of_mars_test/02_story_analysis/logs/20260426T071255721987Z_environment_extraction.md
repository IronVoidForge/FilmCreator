# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:12:55.721987+00:00
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

Chapter id: CH028

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

**Setting:** An Arizona cave (Earth) and a study overlooking the Hudson River (Earth).

**Characters:**
- **John Carter:** The protagonist, now living on Earth.
- **The Mummified Woman:** A deceased figure found in the cave.
- **Dejah Thoris (Mentioned):** Carter's lost love on Mars.
- **A Little Boy and a "Hideous Creature" (Visionary/Imagined):** Seen by Carter in a vision of his potential future or reunion.

**Events:**
- John Carter awakens in a dark cave in Arizona, clothed in strange garments that crumble upon movement.
- He discovers the mummified remains of an old woman tending a charcoal burner with green powder, surrounded by hanging human skeletons.
- Upon exiting the cave, Carter realizes he is back on Earth, looking out over the Arizona landscape.
- A temporal jump occurs: Carter reflects on the twenty years that have passed since his return to Earth. He has become wealthy from an untouched mine but remains consumed by longing for Mars and Dejah Thoris.
- In his study by the Hudson, Carter experiences a vision or profound feeling while looking at Mars through his window, sensing that Dejah Thoris and a child are waiting for him across space.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [arizona_cave_system](arizona_cave_system)
- [arizona_desert_landscape](arizona_desert_landscape)
- [hudson_river_study](hudson_river_study)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_cave_system

[[SECTION markdown]]

# Arizona Cave System

**Role:** Primary (Opening)

**Architecture or Geography:** A dark, subterranean cavern; narrow passages containing charcoal burner stations; presence of hanging human skeletons and ancient mummified remains.

**Lighting and Atmosphere Cues:** Deep shadows, oppressive darkness, claustrophobic, dusty, smelling of old decay and charcoal.

**Scale Cues and Recurring Environmental Anchors:** Low ceilings, skeletal remains as vertical anchors, stone walls.

**Descriptive Noun Phrases:** Subterranean limestone chamber, hanging skeletal remains, ancient mummified figure, dark cavernous void, charcoal burner's nook.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_desert_landscape

[[SECTION markdown]]

# Arizona Desert Landscape

**Role:** Secondary (Transition)

**Architecture or Geography:** Arid, rocky terrain; vast open vistas characteristic of the American Southwest.

**Lighting and Atmosphere Cues:** Harsh sunlight, high contrast, dry heat, expansive sky.

**Scale Cues and Recurring Environmental Anchors:** Distant mesas, sweeping desert plains, horizon line.

**Descriptive Noun Phrases:** Sun-drenched desert expanse, arid rocky terrain, vast Arizona vista, rugged southwestern landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: hudson_river_study

[[SECTION markdown]]

# Hudson River Study

**Role:** Primary (Reflective)

**Architecture or Geography:** An upscale, wealthy interior study; large windows overlooking the Hudson River.

**Lighting and Atmosphere Cues:** Soft indoor lighting, contemplative mood, view of the night sky/Mars through glass, sense of isolation despite wealth.

**Scale Cues and Recurring Environmental Anchors:** Large window frame, river horizon, celestial bodies visible in the sky.

**Descriptive Noun Phrases:** Riverfront study, panoramic Hudson River view, wealthy scholar's interior, nocturnal celestial observation point.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
