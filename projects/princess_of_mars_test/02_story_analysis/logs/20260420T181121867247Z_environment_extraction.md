# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:11:21.867247+00:00
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

Chapter id: CH021

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

As John Carter travels toward Zodanga, he observes Barsoom's advanced irrigation systems that pump water from polar ice caps through underground conduits. During his journey, he meets members of the Zodangan nobility who express their discontent with the unjust war between Zodanga and Helium and discuss the disappearance of Princess Dejah Thoris. Upon reaching the walled city of Zodanga, Carter separates from Woola to avoid detection and enters the metropolis, noting its unique architecture designed for protection against assassination.

In the central plaza, Carter reunites with Kantos Kan, a Red Martian, who reveals his plan to infiltrate the Zodangan navy as an air scout to gain access to Prince Sab Than, who is rumored to be holding Dejah Thoris captive. Using a ruse, Kantos Kan successfully enrolls Carter into the air-scout squadron. During his training, Carter learns to pilot aircraft using the "eighth Barsoomian ray," a repulsive force of gravity derived from light.

While on a solo flight, Carter intervenes in a skirmish, saving a Red Martian scout from three Green warriors by ramming one of them and subsequently killing the remaining two on foot. The scout is revealed to be a cousin of Than Kosis, the Jeddak of Zodanga. Following their return to the city, Carter is called forward during a massive military ceremony. In recognition of his bravery in defeating the Green warriors, Than Kosis confers an honor upon him and appoints him a padwar of The Guards, granting him quarters within the palace.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH021

| Asset ID | Description |
| :--- | :--- |
| barsoomian_irrigation_conduits | Advanced underground water transport systems and polar ice cap runoff. |
| zodanga_metropolis | A massive, walled city featuring defensive architecture and central plazas. |
| zodanga_air_scout_training_range | Flight training grounds utilizing gravity-based propulsion technology. |
| zodanga_palace_quarters | High-status residential quarters within the Zodangan royal palace. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: barsoomian_irrigation_conduits

[[SECTION markdown]]

# Barsoomian Irrigation Conduits

**Role:** Transit / Secondary Setting

**Geography:** Vast underground conduit networks connecting polar ice caps to arid regions; advanced hydraulic infrastructure.

**Lighting and Atmosphere:** Cool, damp subterranean passages; rhythmic sounds of flowing water; stark contrast between the frozen poles and the dry plains.

**Scale Cues:** Massive scale of engineering; long-distance pipelines spanning planetary distances.

**Prompt Phrases:** underground water conduits, polar ice cap runoff, advanced Martian irrigation, hydraulic infrastructure, vast subterranean pipes.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_metropolis

[[SECTION markdown]]

# Zodanga Metropolis

**Role:** Primary Setting

**Architecture:** Massive walled city; defensive urban design optimized to prevent assassination; central plazas; high-density metropolitan layout.

**Lighting and Atmosphere:** Bright Martian sun over stone surfaces; bustling urban energy; sense of political tension and military presence.

**Scale Cues:** Enormous perimeter walls; wide central plazas; sprawling cityscape.

**Prompt Phrases:** walled city, defensive architecture, Zodangan metropolis, central plaza, massive fortifications, ancient Martian urban center.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_air_scout_training_range

[[SECTION markdown]]

# Zodanga Air Scout Training Range

**Role:** Secondary Setting

**Architecture:** Open flight corridors; training grounds for aerial maneuvers.

**Lighting and Atmosphere:** High altitude; bright, direct light; presence of the "eighth Barsoomian ray" (gravity-based propulsion).

**Scale Cues:** Expansive skyways; verticality of flight paths.

**Prompt Phrases:** air scout squadron training, gravity-based flight, aerial combat range, Martian aircraft maneuvers, high altitude skyway.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_quarters

[[SECTION markdown]]

# Zodanga Palace Quarters

**Role:** Primary Setting (Interior)

**Architecture:** High-status royal palace architecture; ornate and secure residential chambers.

**Lighting and Atmosphere:** Regal, controlled lighting; atmosphere of prestige and military honor.

**Scale Cues:** Grand halls; high ceilings; luxurious scale.

**Prompt Phrases:** Zodangan palace interior, royal quarters, padwar residence, ornate Martian architecture, prestigious palace chambers.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
