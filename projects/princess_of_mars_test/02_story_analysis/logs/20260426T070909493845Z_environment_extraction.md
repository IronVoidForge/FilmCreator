# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:09:09.493845+00:00
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

Chapter id: CH026

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

**Events:**
Following the total reduction of Zodanga, Tars Tarkas and Kantos Kan lead a fleet of Thark vessels and prisoners toward Helium. En route, they encounter a Zodangan fleet attempting to besiege Helium; a massive aerial battle ensues, aided by the superior marksmanship of the Thark warriors and the arrival of the Heliumite navy. The Zodangans surrender following the ritualistic suicide-plunge of their commanders. 

John Carter transfers Princess Dejah Thoris to the Heliumite flagship, where she is celebrated as a hero alongside Carter and Tars Tarkas. After the naval victory, Carter remains with the Tharks to finish the land campaign. They unload their thoats near Helium and launch a multi-pronged assault on the remaining Zodangan land forces. Despite being outnumbered, the combined Thark and Heliumite forces crush the Zodangan army. The chapter concludes with a grand triumphal procession into Helium, where John Carter is honored by Tardos Mors, Jeddak of Helium, and the royal family for his role in the victory and the rescue of the Princess.

**Characters:**
- **John Carter:** The protagonist; celebrated as a hero and savior of Dejah Thoris.
- **Dejah Thoris:** Princess of Helium; reunited with her people and honored for her resilience.
- **Tars Tarkas:** Jeddak of Thark; establishes a historic alliance between the green warriors and Helium.
- **Kantos Kan:** A prominent Thark leader.
- **Tardos Mors:** Jeddak of Helium; formally welcomes Carter and the Tharks as allies.
- **Mors Kajak:** Father of Dejah Thoris; deeply moved by her rescue.

**Settings:**
- **The Martian Skies/Sea Bottom:** The site of the intense aerial battle between the Zodangan and Heliumite fleets.
- **The Plains near Helium:** The location of the final land battle and the unloading of the Thark thoats.
- **Helium (Greater City):** The capital city, characterized by its red towers and grand palaces; the site of the victory celebration and royal reception.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [aerial_battle_skies](aerial_battle_skies)
- [helium_plains](helium_plains)
- [helium_city_interior](helium_city_interior)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: aerial_battle_skies

[[SECTION markdown]]

# Aerial Battle Skies

**Role:** Primary (Combat/Transit)

**Geography:** The vast, open Martian atmosphere; high-altitude airspace characterized by sweeping vistas and extreme verticality.

**Lighting and Atmosphere:** Bright, harsh Martian sunlight; thin atmosphere with high visibility; dynamic lighting shifts caused by moving fleets and explosions.

**Scale Cues:** Massive scale defined by the movement of Thark vessels, Zodangan fleets, and Heliumite navy ships; vast horizons.

**Prompt Phrases:** High-altitude Martian sky, aerial naval combat, sweeping atmospheric vistas, fleet formations, sunlit thin atmosphere, vertical combat space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_plains

[[SECTION markdown]]

# Helium Plains

**Role:** Secondary (Combat/Transit)

**Geography:** Expansive, flat Martian plains surrounding the capital; dusty terrain suitable for large-scale troop movements and thoat unloading.

**Lighting and Atmosphere:** Ground-level sunlight; dusty, wind-swept atmosphere; wide-open vistas with low topographical obstruction.

**Scale Cues:** Massive land battle scale; sprawling armies of Tharks and Heliumites vs. Zodangan forces; long sightlines across the plains.

**Prompt Phrases:** Expansive Martian plains, dusty battlefield, wide horizon, ground-level combat, vast open terrain, sweeping landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_city_interior

[[SECTION markdown]]

# Helium City Interior

**Role:** Primary (Social/Ceremonial)

**Geography:** The grand capital of Helium; characterized by red towers, majestic palaces, and wide ceremonial thoroughfares.

**Lighting and Atmosphere:** Grandiose and celebratory; light reflecting off red stone architecture; opulent interiors with high ceilings and royal ornamentation.

**Scale Cues:** Monumental architecture; towering spires; large-scale triumphal processions through grand city streets.

**Prompt Phrases:** Helium capital, red towers, Martian palace architecture, grand ceremonial streets, triumphant procession, majestic red stone structures, royal halls.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
