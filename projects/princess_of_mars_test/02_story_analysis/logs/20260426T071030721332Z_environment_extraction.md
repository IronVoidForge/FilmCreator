# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:10:30.722330+00:00
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

Chapter id: CH027

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

**Setting:** The city of Helium (Palace gardens and council chambers) and the Atmosphere Plant.

**Characters:**
* **John Carter:** Prince of Helium, driven by love for Dejah Thoris to save the planet.
* **Dejah Thoris:** Princess of Helium, facing asphyxiation as the air thins.
* **Tardos Mors:** Jeddak of Helium.
* **Woola:** The Martian hound.
* **The Keeper/Assistant Keeper (deceased):** Murdered, leading to the plant's failure.

**Events:**
* **Peace and Prosperity:** Following a period of peace with the Tharks, John Carter and Dejah Thoris live in happiness, awaiting the hatching of their egg.
* **The Catastrophe:** News arrives that the keeper of the atmosphere plant has been murdered. The engine has stopped, causing a rapid decrease in planetary air pressure.
* **The Dying Days:** As the air thins over three days, the population of Barsoom begins to succumb to asphyxiation. In the Helium palace, the royal family gathers in a sunken garden to face death.
* **The Revelation:** As Dejah Thoris falls into a coma, John Carter experiences a sudden mental breakthrough, recalling nine specific "thought waves" that serve as the key to the atmosphere plant's locks.
* **The Race Against Time:** John Carter commandeers a high-speed air-scout machine, stripping it of all weight to maximize speed. He flies through the thinning atmosphere toward the plant.
* **The Atmosphere Plant:** Arriving at the plant, John finds most workers dead or dying. Using his mental breakthrough, he successfully unlocks the three great doors of the plant. He instructs a surviving worker to restart the pumps before collapsing from exhaustion and lack of oxygen.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [helium_palace_sunken_gardens](helium_palace_sunken_gardens)
- [atmosphere_plant_complex](atmosphere_plant_complex)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_palace_sunken_gardens

[[SECTION markdown]]

# Helium Palace Sunken Gardens

**Role:** Primary / Secondary (Tragedy/Climax setting)

**Architecture & Geography:** A sunken, tiered garden within the royal palace of Helium. Features manicured Martian flora and architectural elements designed for leisure and aesthetic beauty, now serving as a site of communal mourning and respiratory distress.

**Lighting & Atmosphere:** Increasingly thin, hypoxic atmosphere; heavy sense of stillness and impending death; lighting shifts from peaceful prosperity to the dim, suffocating shadows of an oxygen-depleted world.

**Scale & Anchors:** Large-scale terraced gardens; royal seating areas; central botanical features acting as anchors for the dying population.

**Prompt Phrases:** Sunken Martian garden, tiered palace terraces, thinning atmosphere, hypoxic stillness, dying Barsoomian flora, regal desolation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_plant_complex

[[SECTION markdown]]

# Atmosphere Plant Complex

**Role:** Primary (Action/Resolution setting)

**Architecture & Geography:** A massive industrial facility characterized by three great doors and heavy mechanical pumping systems. A sprawling, high-stakes technological hub essential to planetary survival.

**Lighting & Atmosphere:** Industrial, cavernous, and increasingly desolate; atmosphere is characterized by extreme oxygen deprivation and the presence of deceased/dying workers; sense of mechanical urgency vs. biological failure.

**Scale & Anchors:** Massive scale; three great doors (mechanical locks); heavy industrial pumps; high-speed air-scout flight paths leading to the facility.

**Prompt Phrases:** Massive Martian atmosphere plant, industrial pump station, three great mechanical doors, oxygen-depleted interior, cavernous machinery, dying industrial complex.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
