# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:43:28.095255+00:00
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

Chapter id: CH001

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

In this chapter, John Carter introduces himself as Captain Jack Carter of Virginia. He recounts finding a gold-bearing quartz vein with Captain James K. Powell in Arizona during the winter of 1865. After locating a million dollars worth of ore, Powell leaves to purchase machinery while Carter guards the claim. On March 3, 1866, Apaches attack Powell's party. Carter pursues them, finds Powell dead surrounded by Apache tepees, and charges into the camp scattering the warriors. He retrieves Powell's body and flees into a cave after being led astray by his horse. Inside the cave, Carter lays Powell to rest and falls asleep due to exhaustion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index: Arizona Gold Rush & Apache Attack Sequence

## arizona_quartz_vein_location
**Role:** Primary Setting  
**Geography:** Desert mountain terrain with exposed gold-bearing quartz outcrop  
**Lighting:** Winter daylight, cold blue tones on rock faces  
**Atmosphere:** Tense anticipation, mining claim territory  
**Scale:** Medium-scale ore deposit, open-air excavation site  
**Anchors:** Quartz vein face, mining tools, winter snow patches

## apache_camp_tepees
**Role:** Secondary/Transit Setting  
**Geography:** Apache encampment with traditional tepee structures  
**Lighting:** Dusk/dawn transition, firelight glow from tepee openings  
**Atmosphere:** Hostile confrontation, war party gathering  
**Scale:** Medium camp size, multiple tepees clustered together  
**Anchors:** Tepee poles, smoke rising from fires, warrior formations

## cave_shelter
**Role:** Ending/Rest Setting  
**Geography:** Natural rock cave with overhang protection  
**Lighting:** Dim interior, shaft of light from entrance  
**Atmosphere:** Exhaustion, mourning, temporary sanctuary  
**Scale:** Small intimate space, single person occupancy  
**Anchors:** Cave walls, burial spot, horse tracks leading in

[[/SECTION]]
[[FILMCREATOR_PACKET]]
````
