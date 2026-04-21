# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:27:53.065487+00:00
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

Following the total destruction of Zodanga, Tars Tarkas and Kantos Kan lead a fleet of Thark vessels and prisoners toward Helium. En route, they encounter a Zodangan fleet attempting to besiege Helium; a massive aerial battle ensues, aided by the superior marksmanship of the Thark warriors and the arrival of the Heliumite navy. The battle concludes with a ritualistic surrender where Zodangan commanders leap to their deaths from their vessels.

John Carter transfers Princess Dejah Thoris to the Heliumite flagship, where she is celebrated as a hero and credits Carter for her rescue. Carter remains with Tars Tarkas to finalize the land campaign. After unloading Thark mounts (thoats) near Helium, the combined forces of the Tharks and the Heliumite army launch a decisive assault on the remaining Zodangan land camps. Despite being heavily outnumbered, the coalition forces crush the Zodangan resistance.

The chapter concludes with a grand triumphal procession into the city of Helium. John Carter, Tars Tarkas, and the Thark leaders are received with immense honor by Tardos Mors, Jeddak of Helium. The meeting solidifies a historic alliance between the red and green races, and Carter is personally embraced by the royal family as a savior and son of the city.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [aerial_battlefield_mars](aerial_battlefield_mars)
- [heliumite_flagship_interior](heliumite_flagship_interior)
- [zodangan_land_camps](zodangan_land_camps)
- [city_of_helium_procession_route](city_of_helium_procession_route)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: aerial_battlefield_mars

[[SECTION markdown]]

# Aerial Battlefield Mars

**Role:** Primary (Conflict Setting)

**Geography:** High-altitude Martian airspace; vast, open sky filled with intersecting flight paths of Thark vessels, Zodangan fleets, and Heliumite navy ships.

**Lighting and Atmosphere:** Harsh, direct sunlight typical of the Martian atmosphere; chaotic visual field defined by smoke from battle, projectile trails, and the glint of metal hulls.

**Scale Cues:** Massive scale involving hundreds of airborne vessels; sense of vertigo and immense verticality.

**Prompt Phrases:** vast aerial combat zone, intersecting vessel trajectories, plumes of battle smoke, high-altitude Martian sky, fleet-scale warfare.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: heliumite_flagship_interior

[[SECTION markdown]]

# Heliumite Flagship Interior

**Role:** Secondary (Character/Social Setting)

**Architecture:** Grand, ceremonial naval interior; high ceilings and spacious decks designed for both military command and royal reception.

**Lighting and Atmosphere:** Celebratory and bright; warm lighting reflecting a sense of triumph and relief.

**Scale Cues:** Large communal halls capable of hosting heroes and dignitaries; grand scale consistent with Heliumite naval prestige.

**Prompt Phrases:** ceremonial naval hall, triumphant atmosphere, grand flagship interior, polished metal surfaces, heroic reception space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodangan_land_camps

[[SECTION markdown]]

# Zodangan Land Camps

**Role:** Secondary (Conflict Setting)

**Geography:** Ground-level encampments; rugged Martian terrain occupied by retreating or besieged forces.

**Lighting and Atmosphere:** Desperate, dusty, and chaotic; atmosphere of a collapsing military position under heavy assault.

**Scale Cues:** Sprawling ground camps being overrun by coalition cavalry and infantry.

**Prompt Phrases:** besieged land camps, dusty Martian plains, crumbling military fortifications, chaotic ground skirmish site.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: city_of_helium_procession_route

[[SECTION markdown]]

# City of Helium Procession Route

**Role:** Primary (Triumphal Setting)

**Architecture:** Grand urban thoroughfares; majestic Heliumite architecture designed for public spectacle and royal processions.

**Lighting and Atmosphere:** Glorious, bright, and celebratory; high-contrast lighting from the Martian sun hitting city structures.

**Scale Cues:** Wide boulevards lined with crowds; monumental scale of the city's gates and central plazas.

**Prompt Phrases:** grand triumphal procession, majestic Heliumite streets, urban victory parade, monumental architecture, cheering crowds in city plaza.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
