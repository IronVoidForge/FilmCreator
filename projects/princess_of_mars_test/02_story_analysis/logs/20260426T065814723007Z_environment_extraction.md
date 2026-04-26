# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:58:14.723007+00:00
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

Chapter id: CH019

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

**Setting:** A subterranean amphitheater within a ruined, ancient green Martian city; later, the hills east of the Warhoon city.

**Characters:**
* **John Carter:** An Earthman and prisoner of the Warhoons.
* **Kantos Kan:** A padwar (lieutenant) from Helium and fellow prisoner.
* **Dak Kova:** The leader/chieftain of the Warhoon horde.
* **Warhoon Horde:** A bloodthirsty green Martian race hosting gladiatorial games.

**Events:**
* **Loss of Keys:** John Carter realizes his jailer's keys have been stolen by creatures in the darkness.
* **Meeting Kantos Kan:** Carter meets a fellow prisoner, Kantos Kan, who provides intelligence regarding Dejah Thoris and the current state of Helium's search efforts.
* **The Gladiatorial Games:** The prisoners are taken to an immense underground arena for a ten-day tournament where only one survivor is granted freedom.
* **Arena Combat:** Carter survives multiple bouts against men and beasts, gaining the crowd's favor. Kantos Kan uses a specialized throwing technique to defeat a massive sixteen-foot green warrior.
* **The Staged Death:** To escape, Carter and Kantos Kan conspire to fake a final duel. Kantos Kan appears to deliver a fatal blow to Carter, but actually misses his vital organs. 
* **Escape:** Under the cover of darkness, Kantos Kan claims his freedom while Carter stealthily escapes the arena to head toward the eastern hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [subterranean_amphitheater_arena](subterranean_amphitheater_arena)
- [warhoon_eastern_hills](warhoon_eastern_hills)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: subterranean_amphitheater_arena

[[SECTION markdown]]

# Subterranean Amphitheater Arena

**Role:** Primary setting (Gladiatorial arena).

**Architecture or Geography:** A massive, ancient underground amphitheater carved into the Martian crust. Part of a ruined green city. Features tiered seating for crowds and a central combat floor.

**Lighting and Atmosphere Cues:** Dimly lit by subterranean sources; heavy atmosphere of dust, blood, and crowd noise. Deep shadows in the recesses of the ruins.

**Scale Cues and Recurring Environmental Anchors:** Immense scale capable of holding massive crowds; high walls of ancient green stone; central combat pit.

**Descriptive Noun Phrases:** Ancient Martian amphitheater, subterranean arena, ruined green city architecture, tiered stone seating, dusty gladiatorial pit, cavernous combat floor.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_eastern_hills

[[SECTION markdown]]

# Warhoon Eastern Hills

**Role:** Secondary setting (Escape route/Transit).

**Architecture or Geography:** Rugged, hilly terrain located east of the Warhoon city. Natural Martian landscape.

**Lighting and Atmosphere Cues:** Nighttime lighting; darkness providing cover for stealthy movement; starlight or dim ambient Martian sky.

**Scale Cues and Recurring Environmental Anchors:** Rolling hills, rocky outcrops, uneven terrain.

**Descriptive Noun Phrases:** Rugged eastern hills, nocturnal Martian landscape, rocky hilltops, dark undulating terrain, shadow-drenched slopes.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
