# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:23:12.023775+00:00
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

Chapter id: CH022

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
The interior of the palace in Zodanga, specifically the private apartments of Jeddak Than Kosis, various winding corridors, antechambers, and a great hall overlooking a balcony.

**Characters:**
* **John Carter:** A human warrior serving as a guard for Than Kosis; he is searching for Dejah Thoris.
* **Dejah Thoris:** The Princess of Helium, who has unexpectedly pledged herself to Sab Than to ensure peace.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **Sab Than:** The Prince of Zodanga and son of Than Kosis.
* **Notan:** The royal psychologist.
* **Guardsmen:** Four unnamed Zodangan soldiers killed by Carter during his confrontation.

**Events:**
* **The Betrayal:** While stationed behind a tapestry to guard Than Kosis, John Carter witnesses Dejah Thoris enter the chamber and publicly declare her intention to marry Sab Than, effectively abandoning her previous feelings for Carter.
* **The Confrontation:** Distraught, Carter abandons his post to find Dejah Thoris. He is intercepted by four guards in an antechamber. After a fierce combat lasting twenty minutes, Carter kills all four guardsmen.
* **The Reunion:** Carter confronts Dejah Thoris. She recognizes him but reveals that due to Barsoomian custom, her promise to Sab Than is binding and she can no longer be his. She explains that her previous offense toward him was a misunderstanding of Martian marriage customs.
* **The Escape:** As the palace enters an uproar following the discovery of the dead guards, Carter hides in a large hanging ornament in a great hall. He overhears the royal psychologist describing him as a superhuman stranger and Than Kosis ordering a massive manhunt. 
* **Departure:** Under the cover of darkness, Carter escapes the palace by leaping from a balcony to a glass wall and into the streets of Zodanga.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH022

## Palace Settings
- [zodanga_palace_interior](#zodanga_palace_interior)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_interior

[[SECTION markdown]]

# Zodanga Palace Interior

**Role:** Primary / Secondary Setting

**Architecture & Geography:**
A complex network of royal quarters including private apartments, winding corridors, and formal antechambers. Features include heavy tapestries used for concealment, large hanging ornaments/decorations in great halls, and expansive balconies overlooking the city. The architecture is characterized by grand scale and ceremonial layouts.

**Lighting & Atmosphere:**
Varies from the intimate, perhaps dimly lit private chambers to the high-tension atmosphere of the corridors. Includes moments of sudden darkness during escape sequences and the transition from indoor palace light to the nocturnal atmosphere of the Zodangan streets.

**Scale & Anchors:**
Large-scale halls capable of hosting public declarations; narrow, winding transit corridors; massive decorative hanging elements used for hiding; high balconies providing verticality and extreme drops.

**Prompt Phrases:**
Zodangan royal architecture, winding palace corridors, ceremonial antechambers, heavy woven tapestries, grand hall with hanging ornaments, high stone balcony, Martian palace interior, sweeping Zodangan vistas.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
