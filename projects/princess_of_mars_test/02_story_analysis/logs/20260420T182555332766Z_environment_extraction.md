# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:25:55.332766+00:00
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

**Setting:**
The palace in Helium (including the rooftop shrine and sunken garden) and the massive, fortified Atmosphere Plant.

**Characters:**
* **John Carter:** Prince of Helium; hero of Barsoom.
* **Dejah Thoris:** Princess of Helium; John Carter's wife.
* **Tardos Mors:** Jeddak (Ruler) of Helium.
* **Woola:** The loyal Martian hound.
* **Sola & Tars Tarkas:** Mentioned in the context of the recent peace treaty.
* **The Assistant Keeper/Assassin:** Mentioned as the cause of the crisis.
* **A surviving technician:** An unnamed man at the Atmosphere Plant.

**Events:**
* **Peace and Prosperity:** Following a period of peace with the Tharks, John Carter and Dejah Thoris live in happiness for nine years, awaiting the hatching of their egg in a golden incubator.
* **The Crisis:** A dispatch bearer arrives with news that the keeper of the Atmosphere Plant has been murdered and the plant's engine has stopped. Air pressure across Barsoom begins to drop rapidly.
* **The Approaching Death:** As the air thins, the people of Helium face mass asphyxiation. In a sunken garden, the royal family prepares for death. Dejah Thoris falls into a coma near their egg incubator.
* **The Revelation:** In a moment of desperation, John Carter recalls nine "thought waves"—a mental key to the Atmosphere Plant's locks.
* **The Race Against Time:** John Carter commandeers a high-speed air-scout machine, stripping it of all weight to maximize speed. He flies through the thinning atmosphere toward the plant.
* **The Breach:** Arriving at the plant, John finds most workers dead or unconscious. Using his mental "thought waves," he successfully unlocks the three great doors. He instructs a surviving technician to restart the pumps before collapsing from exhaustion and lack of oxygen.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [helium_palace_complex](helium_palace_complex)
- [atmosphere_plant_fortress](atmosphere_plant_fortress)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_palace_complex

[[SECTION markdown]]

# Helium Palace Complex

**Role:** Primary / Domestic Setting

**Architecture & Geography:** A grand Martian palace featuring specialized zones including a rooftop shrine and a sunken garden. The architecture is designed for high-status living, incorporating luxury elements like golden egg incubators.

**Lighting & Atmosphere:** Initially bright and prosperous; transitions to a thin, suffocating atmosphere with dimming light as air pressure drops. The mood shifts from domestic peace to desperate, oxygen-deprived lethargy.

**Scale & Anchors:** Large-scale royal living quarters; the sunken garden serves as a focal point for the family's final moments; the golden incubator acts as a central visual anchor.

**Prompt Phrases:** Martian palace architecture, sunken garden, rooftop shrine, golden egg incubator, thinning atmosphere, oxygen deprivation, regal but desolate.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_plant_fortress

[[SECTION markdown]]

# Atmosphere Plant Fortress

**Role:** Primary / Industrial Setting

**Architecture & Geography:** A massive, fortified industrial complex. Features three great doors controlled by mental locks and heavy mechanical pump systems. The interior is a site of high-stakes machinery and large-scale engineering.

**Lighting & Atmosphere:** Harsh, industrial lighting; atmosphere becomes increasingly thin and lethal; presence of dead or unconscious workers scattered among the machinery.

**Scale & Anchors:** Massive scale; monumental doors; heavy mechanical pumps; vast industrial halls; air-scout landing zones.

**Prompt Phrases:** Fortified atmosphere plant, massive industrial doors, Martian engineering, heavy mechanical pumps, thinning air, high-speed air-scout arrival, industrial desolation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
