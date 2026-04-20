# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:06:25.120696+00:00
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

**Setting:** A subterranean amphitheater within a ruined green Martian city; later, the hills east of the city.

**Characters:**
- **John Carter:** A prisoner of the Warhoon, fighting for survival in the arena.
- **Kantos Kan:** A padwar (lieutenant) from Helium and a fellow prisoner; becomes a close ally to Carter.
- **Dak Kova:** The leader/chieftain of the Warhoon horde.
- **Warhoon Horde:** A bloodthirsty green Martian community hosting gladiatorial games.

**Events:**
- **Loss of Keys:** After being left in darkness, John Carter realizes his jailer's keys have been stolen by creatures from the nearby lair.
- **Meeting Kantos Kan:** Carter meets a fellow prisoner, Kantos Kan of Helium. Kan provides intelligence regarding Dejah Thoris, noting that she and Sola likely escaped into the hills near a waterway. He also details the failed search efforts by Helium's fleets.
- **The Gladiatorial Games:** The prisoners are taken to an immense, excavated amphitheater for a ten-day tournament. The games involve pitting humans, green warriors, and ferocious Martian beasts against one another until only one victor remains.
- **Arena Combat:** Carter survives multiple bouts against men and beasts using his superior strength and agility. Kantos Kan survives by using a specialized long-distance sword throw to kill a massive sixteen-foot northern warrior.
- **The Escape Plan:** As the final two combatants, Carter and Kantos Kan conspire to fake Carter's death. Under the cover of darkness, Kantos Kan performs a staged killing blow that fails to strike a vital organ. 
- **Escape:** Believing Carter dead, the crowd disperses. Carter crawls from the arena and successfully reaches the hills east of the city to begin his escape.
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
- [ruined_martian_city_hills](ruined_martian_city_hills)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: subterranean_amphitheater_arena

[[SECTION markdown]]

# Subterranean Amphitheater Arena

**Role:** Primary setting (combat and spectacle).

**Architecture/Geography:** An immense, excavated amphitheater carved directly into the Martian crust. It is part of a larger ruined green city. The structure features tiered seating for crowds and a central combat floor designed to accommodate both human warriors and massive beasts.

**Lighting and Atmosphere:** Harsh, dramatic lighting typical of gladiatorial arenas; heavy atmosphere characterized by dust, blood, and the roar of a bloodthirsty crowd. Transitions from bright spectacle during games to oppressive darkness during prisoner transit or escape attempts.

**Scale Cues:** Massive scale; capable of holding large crowds and accommodating sixteen-foot warriors and ferocious beasts. The verticality of the excavated walls provides a sense of enclosure and dread.

**Prompt Phrases:** Excavated stone amphitheater, ruined green Martian architecture, subterranean arena, gladiatorial combat pit, massive scale, dust-filled atmosphere, tiered spectator seating, ancient carved rock.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ruined_martian_city_hills

[[SECTION markdown]]

# Ruined Martian City Hills

**Role:** Secondary setting (transit and escape).

**Architecture/Geography:** Rolling hills located east of the ruined green city. The terrain is characterized by proximity to waterways and rugged, natural Martian topography.

**Lighting and Atmosphere:** Open-air lighting; potentially moonlight or dim Martian sun. A sense of isolation and survivalist tension.

**Scale Cues:** Expansive landscape; vast hillsides providing cover for fugitives but offering little protection from the elements or pursuit.

**Prompt Phrases:** Rugged Martian hills, eastern outskirts of ruined city, rocky terrain, proximity to waterways, desolate landscape, twilight atmosphere, scrubland topography.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
