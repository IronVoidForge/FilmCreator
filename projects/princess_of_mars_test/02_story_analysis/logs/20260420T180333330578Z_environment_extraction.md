# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:03:33.330578+00:00
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

Chapter id: CH017

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

The protagonist infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the jeddak, Tal Hajus. After witnessing the depraved threats made against the Princess, the protagonist intervenes, knocking Tal Hajus unconscious and successfully leading Dejah Thoris and Sola out of the city via a rear window. The group escapes on thoats, heading northeast across a two-hundred-mile mossy waste toward Helium, traveling without food or water in a state of extreme exhaustion.

As they traverse the trackless waste, the party becomes lost and realizes they have no visible waterways. During their trek, the protagonist discovers that his faithful hound, Woola, has followed them. The journey takes a toll as one of their thoats collapses from exhaustion; the group continues with only one beast, forcing Dejah Thoris to ride while the others walk. Their progress is interrupted when they spot a large party of several hundred mounted Thark warriors emerging from a mountain pass. 

After a chieftain spots them, the protagonist uses his Martian rifle to shoot the leader, creating a distraction. To ensure their survival, he commands Sola to take Dejah Thoris on the remaining thoat and flee toward the hills. Following an emotional embrace, the protagonist stays behind to hold off the advancing warriors. Despite continuous rifle fire, he eventually runs out of ammunition as nearly a thousand warriors charge him. While attempting to evade them with extraordinary leaps, he trips on a piece of quartz and is beaten into unconsciousness by the overwhelming Thark force.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_city_interior](#thark_city_interior)
- [mossy_waste_plains](#mossy_waste_plains)
- [mountain_pass_threshold](#mountain_pass_threshold)
- [quartz_outcrop_terrain](#quartz_outcrop_terrain)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_interior

[[SECTION markdown]]

# Thark City Interior

**Role:** Primary (Infiltration/Conflict)

**Architecture/Geography:** Urban Martian interior, featuring high-set windows and structural layouts suitable for infiltration.

**Lighting/Atmosphere:** Dimly lit, oppressive, sense of depravity and tension.

**Scale/Anchors:** Rear escape windows, ceremonial or residential chambers of the Jeddak.

**Prompt Phrases:** Thark urban architecture, Martian palace interior, dim lighting, high-set window egress, ancient stone textures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_waste_plains

[[SECTION markdown]]

# Mossy Waste Plains

**Role:** Secondary (Transit/Survival)

**Architecture/Geography:** A vast, trackless, two-hundred-mile expanse of mossy wasteland. Lacks visible waterways or landmarks.

**Lighting/Atmosphere:** Harsh, exposed, desolate, sense of extreme exhaustion and heat.

**Scale/Anchors:** Endless horizon, featureless terrain, absence of water sources.

**Prompt Phrases:** Vast mossy waste, trackless Martian plains, desolate landscape, endless green-grey moss, arid wasteland.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mountain_pass_threshold

[[SECTION markdown]]

# Mountain Pass Threshold

**Role:** Secondary (Conflict/Ambush)

**Architecture/Geography:** A narrow opening or gateway between mountainous elevations.

**Lighting/Atmosphere:** High contrast, shadows from cliffs, sudden emergence of large groups.

**Scale/Anchors:** Narrow mountain pass, rocky ridges, vantage points for mounted warriors.

**Prompt Phrases:** Martian mountain pass, rocky canyon entrance, rugged cliffside, narrow transit corridor.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: quartz_outcrop_terrain

[[SECTION markdown]]

# Quartz Outcrop Terrain

**Role:** Secondary (Conflict/Hazard)

**Architecture/Geography:** Rugged terrain broken by sharp, protruding pieces of quartz.

**Lighting/Atmosphere:** Glinting surfaces, uneven ground, treacherous footing.

**Scale/Anchors:** Sharp quartz protrusions, jagged rock formations.

**Prompt Phrases:** Jagged quartz outcrops, crystalline rock fragments, uneven Martian terrain, sharp mineral deposits.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
