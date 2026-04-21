# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:29:02.889345+00:00
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
The palace of Helium and the Atmosphere Plant on Barsoom. The environment shifts from a period of peace and prosperity to one of extreme atmospheric thinning and impending asphyxiation.

**Characters:**
- **John Carter:** Prince of Helium, driven by his love for Dejah Thoris to save the planet.
- **Dejah Thoris:** Princess of Helium, facing death alongside John.
- **Tardos Mors:** Jeddak of Helium, leader during the planetary crisis.
- **Sola & Tars Tarkas:** Mentioned in the context of the recent peace between Thark and Helium.
- **Woola:** The loyal Martian hound.
- **The Assistant Keeper/Assassin:** (Mentioned) The catalyst for the atmospheric failure.

**Events:**
- **Peaceful Transition:** Following a period of celebration, the Tharks return to their lands, and John Carter and Dejah Thoris enjoy several years of happiness in Helium, awaiting the hatching of their egg.
- **The Crisis:** News arrives that the keeper of the atmosphere plant has been murdered and the engine has stopped. Air pressure begins to drop rapidly across Barsoom.
- **The Descent into Death:** As the air thins, the people of Helium succumb to asphyxiation. In a sunken garden, the royal family prepares for death. Dejah Thoris falls into a coma.
- **The Revelation:** In a moment of desperation, John Carter recalls nine "thought waves"—the secret auditory key required to operate the atmosphere plant's locks.
- **The Race Against Time:** John commandeers a high-speed air-scout machine, stripping it of all weight to reach the plant faster. He flies through the thinning atmosphere at extreme velocity.
- **The Atmosphere Plant:** John arrives at the plant to find most workers dead or unconscious. Using his mental "thought waves," he successfully unlocks the three great doors. He instructs a surviving worker to restart the pumps before collapsing from exhaustion and lack of oxygen.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH027

| Asset ID | Description |
| :--- | :--- |
| helium_palace_gardens | The royal gardens of Helium, transitioning from lush peace to a site of asphyxiation. |
| barsoomian_sky_transit | The thinning atmosphere and high-altitude flight paths during the crisis. |
| atmosphere_plant_complex | The industrial/mechanical heart of Barsoom; massive doors and pump machinery. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_palace_gardens

[[SECTION markdown]]

# Helium Palace Gardens

**Role:** Primary / Secondary (Crisis Setting)

**Architecture or Geography:** A sunken garden within the palace complex; features manicured flora and architectural elements designed for leisure, now becoming a site of terminal stillness.

**Lighting and Atmosphere Cues:** Transitioning from warm, prosperous light to a thin, hazy, and suffocating atmosphere; dimming light as oxygen levels drop; sense of heavy, stagnant air.

**Scale Cues and Recurring Environmental Anchors:** Sunken garden walls, royal seating areas, lush but wilting vegetation.

**Descriptive Noun Phrases:** Sunken palace garden, thinning Martian air, dying flora, royal asphyxiation site, hazy sunlight.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: barsoomian_sky_transit

[[SECTION markdown]]

# Barsoomian Sky Transit

**Role:** Transit Setting

**Architecture or Geography:** The open Martian sky; high-altitude flight paths above the thinning atmosphere.

**Lighting and Atmosphere Cues:** Extremely thin, translucent air; rapid loss of atmospheric density; high-velocity wind resistance; bright but increasingly hollow light.

**Scale Cues and Recurring Environmental Anchors:** Vast planetary horizon, shrinking atmospheric envelope, high-speed aerial trajectories.

**Descriptive Noun Phrases:** Thinning atmosphere, high-altitude void, velocity-streaked sky, low-pressure Martian heavens.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_plant_complex

[[SECTION markdown]]

# Atmosphere Plant Complex

**Role:** Primary (Climax Setting)

**Architecture or Geography:** A massive industrial facility; features three great mechanical doors and heavy pump machinery.

**Lighting and Atmosphere Cues:** Dim, industrial lighting; oxygen-deprived environment; heavy metallic structures; sense of mechanical stillness/failure.

**Scale Cues and Recurring Environmental Anchors:** Three great doors, massive atmospheric pumps, vast industrial halls, mechanical locks.

**Descriptive Noun Phrases:** Great atmospheric doors, massive pump machinery, industrial Martian plant, oxygen-generation facility, colossal mechanical locks.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
