# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:52:17.724092+00:00
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

Chapter id: CH001

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

**Setting:** A small, one-room farmhouse situated in the middle of the vast, colorless Kansas prairies. The landscape is characterized by gray grass and baked earth.

**Characters:**
- **Dorothy:** An orphaned young girl who maintains a sense of joy despite her surroundings.
- **Aunt Em:** Dorothy's aunt; once pretty, now hardened and gray from the harsh prairie life.
- **Uncle Henry:** Dorothy's uncle; a stern, hardworking farmer.
- **Toto:** Dorothy's small, energetic black dog.

**Events:**
- The family lives in a state of constant vigilance due to the threat of cyclones.
- A massive storm approaches from both the north and south, signaling an imminent cyclone.
- As Uncle Henry goes to tend to the livestock, Aunt Em directs Dorothy to seek shelter in the underground cyclone cellar.
- Before Dorothy can reach the trap door, a powerful cyclone hits the house, lifting it off the ground.
- The house becomes the center of the storm, carried high into the air by intense wind pressure.
- Inside the floating house, Dorothy manages to rescue Toto after he nearly falls through the open trap door.
- As the hours pass, the initial terror subsides into a rhythmic swaying; Dorothy and Toto eventually fall asleep as the house is carried miles away.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [kansas_prairie_landscape](kansas_prairie_landscape)
- [farmhouse_interior_and_cellar](farmhouse_interior_and_cellar)
- [cyclone_storm_void](cyclone_storm_void)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: kansas_prairie_landscape

[[SECTION markdown]]

# Kansas Prairie Landscape

**Role:** Primary / Transit Setting

**Architecture or Geography:** Vast, flat, and featureless expanse of the American Midwest. Characterized by endless horizons and baked, dry earth.

**Lighting and Atmosphere Cues:** Monochromatic and colorless; dominated by shades of gray and dusty sepia. Harsh, unrelenting sunlight during the day; oppressive stillness before a storm.

**Scale Cues and Recurring Environmental Anchors:** Infinite horizontal scale; tiny, isolated structures (like the farmhouse) emphasize the overwhelming emptiness of the plains.

**Descriptive Noun Phrases:** Gray grass plains, baked earth, colorless horizon, desolate prairie expanse, wind-swept dust.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: farmhouse_interior_and_cellar

[[SECTION markdown]]

# Farmhouse Interior and Cellar

**Role:** Primary Setting

**Architecture or Geography:** A small, humble one-room farmhouse. Includes a wooden floor with a heavy trap door leading to an underground cyclone cellar. Simple, utilitarian rural architecture.

**Lighting and Atmosphere Cues:** Dim, dusty interior lighting; shadows cast by storm clouds. The atmosphere is one of constant vigilance and claustrophobic tension during weather events.

**Scale Cues and Recurring Environmental Anchors:** Small-scale, intimate, and cramped. The trap door serves as the primary anchor for safety/danger transitions.

**Descriptive Noun Phrases:** One-room farmhouse, wooden floorboards, underground cyclone cellar, rustic shelter, weathered timber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cyclone_storm_void

[[SECTION markdown]]

# Cyclone Storm Void

**Role:** Secondary / Transit Setting (Dynamic)

**Architecture or Geography:** A chaotic, swirling vortex of wind and debris. A non-static environment defined by intense air pressure and centrifugal force.

**Lighting and Atmosphere Cues:** Turbulent, dark, and violent. Rapidly shifting light through thick cloud cover; high-velocity wind effects and flying dust/debris.

**Scale Cues and Recurring Environmental Anchors:** Massive, overwhelming scale that dwarfs human structures. The "eye" or center of the storm provides a rhythmic, swaying sensation.

**Descriptive Noun Phrases:** Swirling cyclone vortex, violent wind pressure, debris-filled sky, turbulent storm clouds, rotating atmospheric void.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
