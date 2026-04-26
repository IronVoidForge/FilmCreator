# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:04:18.378475+00:00
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

Chapter id: CH023

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

**Summary:**
Following the news that Princess Dejah Thoris has been promised to Sab Than of Zodanga, John Carter meets secretly with Kantos Kan. The two devise a plan to separate: Kantos Kan will infiltrate the Zodanga palace via a secret entrance in the high tower to assassinate Sab Than, while John Carter will attempt to fly to Helium.

To reach the machine sheds, John Carter performs a perilous climb up the exterior of the massive Zodanga barracks and uses a grappling hook to swing onto the roof. After subduing a sentry and hanging him over the edge to delay discovery, Carter retrieves two air machines. During their departure, they are intercepted by Zodangan air patrols. Kantos Kan dives into darkness to evade capture, while Carter engages in a high-speed chase through the Martian sky. 

Despite using a specialized Heliumite gearing trick to increase his speed, Carter's machine is struck by a projectile from a cruiser. He survives a near-fatal plunge but emerges to find his compass and speedometer destroyed. Lost and flying blindly toward what he hopes is Helium, Carter spends hours traversing the Martian landscape, eventually realizing he has missed his destination and is lost over an unfamiliar territory.

**Characters:**
* **John Carter:** An adventurer attempting to reach Helium after a narrow escape from Zodangan pursuit.
* **Kantos Kan:** A Heliumite air-scout who vows to kill Sab Than to avenge the Princess and support Carter.
* **Sab Than (Mentioned):** The ruler of Zodanga to whom Dejah Thoris is promised.
* **Dejah Thoris (Mentioned):** The Princess of Helium.
* **Zodangan Sentry:** A guard on the barracks roof who is incapacitated by Carter.

**Settings:**
* **Zodanga:** A large, heavily guarded city characterized by high-rise architecture and air patrols.
* **The Barracks:** An enormous building in Zodanga, a thousand feet high, housing the air-scout squadron.
* **The Martian Sky:** The setting for the aerial pursuit and Carter's subsequent flight.
* **Dead Sea Bottom/Unidentified Cities:** The vast, desolate landscape Carter traverses while lost.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [zodanga_urban_complex](zodanga_urban_complex)
- [martian_sky_aerial_corridors](martian_sky_aerial_corridors)
- [desolate_martian_wasteland](desolate_martian_wasteland)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_urban_complex

[[SECTION markdown]]

# Zodanga Urban Complex

**Role:** Primary / Secondary Setting

**Architecture & Geography:** A massive, heavily fortified city characterized by high-rise architecture and monumental structures. Key features include the thousand-foot-high barracks and high towers with secret access points.

**Lighting & Atmosphere:** Heavily guarded atmosphere; urban density with verticality that creates pockets of shadow and light.

**Scale & Anchors:** Massive scale; dominated by the Zodanga Barracks (1,000 ft height) and various palace towers.

**Prompt Phrases:** High-rise Martian architecture, fortified cityscapes, monumental barracks, vertical urban canyons, Zodangan stone structures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sky_aerial_corridors

[[SECTION markdown]]

# Martian Sky Aerial Corridors

**Role:** Transit Setting

**Architecture & Geography:** Open atmospheric space; high-altitude flight paths used by air patrols and individual machines.

**Lighting & Atmosphere:** High-speed aerial vistas; varying light based on altitude and time of day; presence of projectile fire and smoke trails during chases.

**Scale & Anchors:** Vast, open expanses; defined by the movement of cruisers and air machines.

**Prompt Phrases:** Martian atmosphere, high-altitude aerial chase, sweeping sky vistas, thin Martian air, sunlit sky corridors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: desolate_martian_wasteland

[[SECTION markdown]]

# Desolate Martian Wasteland

**Role:** Secondary Setting

**Architecture & Geography:** Vast, unfamiliar territory; includes dead sea bottoms and the ruins of unidentified cities. Characterized by desolation and lack of landmarks.

**Lighting & Atmosphere:** Harsh, lonely atmosphere; sense of isolation and disorientation under a vast sky.

**Scale & Anchors:** Immense scale; endless horizons and scattered, distant ruins.

**Prompt Phrases:** Desolate Martian landscape, dead sea bottom, ancient unidentified ruins, vast arid plains, lonely planetary vistas.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
