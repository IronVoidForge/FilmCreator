# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:27:19.946216+00:00
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

The protagonist awakens in a dark cave wearing strange, stiff garments. Upon exploring with a match, he discovers the mummified remains of an old woman tending a charcoal burner and a gruesome display of human skeletons hanging from the cave ceiling by rawhide thongs. 

Emerging from the cave onto a ledge, he realizes with shock that he is back on Earth in Arizona, not Mars. He reflects on his ten-year separation from Mars and his enduring love for Dejah Thoris, wondering if she survived the atmospheric crisis on her planet. The narrative shifts to twenty years after his arrival on Mars, as an older version of the protagonist sits in his study overlooking the Hudson, experiencing a vision of Dejah Thoris, a young boy, and a creature with a heart of gold, sensing that he will soon be reunited with them.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [dark_cave_interior](#dark_cave_interior)
- [arizona_ledge_overlook](#arizona_ledge_overlook)
- [hudson_river_study](#hudson_river_study)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dark_cave_interior

[[SECTION markdown]]

# Dark Cave Interior

**Role:** Primary (Initial Setting)

**Architecture/Geography:** A cramped, subterranean cavern; uneven stone walls; presence of a charcoal burner station.

**Lighting and Atmosphere:** Pitch blackness; flickering, localized light from single matches; heavy, claustrophobic atmosphere; scent of ash and decay.

**Scale/Anchors:** Mummified remains of an old woman; human skeletons suspended from the ceiling by rawhide thongs.

**Prompt Phrases:** dark limestone cavern, charcoal burner embers, hanging skeletal remains, rawhide suspension, flickering matchlight, subterranean gloom.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_ledge_overlook

[[SECTION markdown]]

# Arizona Ledge Overlook

**Role:** Secondary (Transition Setting)

**Architecture/Geography:** A high, rocky ledge overlooking an arid Arizona landscape.

**Lighting and Atmosphere:** Harsh, natural daylight; dry, desert air; sense of disorientation and shock.

**Scale/Anchors:** High elevation; vast desert horizon; rugged rock formations.

**Prompt Phrases:** high desert ledge, Arizona canyonlands, sun-drenched rocky outcrop, vast arid vista, sweeping desert landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: hudson_river_study

[[SECTION markdown]]

# Hudson River Study

**Role:** Primary (Later Timeline Setting)

**Architecture/Geography:** An interior study or library; large windows overlooking a river.

**Lighting and Atmosphere:** Soft, contemplative indoor lighting; tranquil atmosphere; sense of aging and reflection.

**Scale/Anchors:** Large window frames; view of the Hudson River; scholarly furniture.

**Prompt Phrases:** riverside study, Hudson River view, elegant interior, soft window light, contemplative scholar's room.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
