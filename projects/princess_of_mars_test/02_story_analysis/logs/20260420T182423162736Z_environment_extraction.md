# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:24:23.162736+00:00
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
Following the total reduction of Zodanga, Tars Tarkas and Kantos Kan lead a fleet of 250 Thark battleships and 100,000 green warriors toward Helium. En route, they encounter a Zodangan fleet attempting to besiege Helium; a massive aerial battle ensues where the combination of Heliumite naval skill and Thark small-arms fire results in a decisive victory. The chapter depicts the ritualistic surrender of Zodangan commanders, who leap to their deaths from their vessels. 

Upon reaching Helium, John Carter facilitates the transfer of Princess Dejah Thoris to the Heliumite flagship, where she publicly credits Carter for her rescue and the city's salvation. After Dejah Thoris is safely returned to her palace, Carter and Tars Tarkas lead a land assault against the remaining Zodangan ground forces. Despite being outnumbered by nearly ten to one, the Thark warriors—supported by arriving Heliumite reinforcements—crush the Zodangan camp. The chapter concludes with a grand triumphal procession into Helium, where John Carter and Tars Tarkas are honored by Jeddak Tardos Mors for forging an unprecedented alliance between the red and green races.

**Characters:**
* **John Carter:** Hero of the campaign; credited with the liberation of Dejah Thoris and the defense of Helium.
* **Tars Tarkas:** Jeddak of Thark; a legendary warrior who establishes a formal friendship with the Heliumites.
* **Dejah Thoris:** Princess of Helium; reunited with her people and honored for her resilience.
* **Tardos Mors:** Jeddak of Helium; receives the allies with profound gratitude and formalizes the alliance.
* **Mors Kajak:** Father of Dejah Thoris; a fierce warrior overcome with emotion at his daughter's return.
* **Kantos Kan:** Thark leader/warrior assisting in the campaign.

**Settings:**
* **The Martian Skies/Sea Bottom:** The site of the massive aerial naval engagement between Helium and Zodanga fleets.
* **The Plains near Helium:** The location of the final land battle and the unloading of Thark thoats.
* **Helium (Greater City):** The red-skinned capital, characterized by its magnificent architecture and celebratory atmosphere during the triumphal entry.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [aerial_naval_battlefield](aerial_naval_battlefield)
- [helium_plains_battleground](helium_plains_battleground)
- [helium_city_metropolis](helium_city_metropolis)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: aerial_naval_battlefield

[[SECTION markdown]]

# Aerial Naval Battlefield

**Role:** Primary (Combat Setting)

**Geography:** The vast, open Martian atmosphere acting as a sea; characterized by high-altitude currents and wide vistas.

**Lighting and Atmosphere:** Harsh, direct sunlight of the Martian sky; punctuated by flashes of small-arms fire, explosions from ship combat, and the chaotic movement of massive fleets.

**Scale Cues:** Massive scale defined by hundreds of Thark battleships and Zodangan vessels; tiny silhouettes of warriors against the vastness of the sky.

**Descriptive Noun Phrases:** High-altitude naval engagement, floating warship formations, aerial skirmish zone, Martian sky vistas, ship-to-ship combat debris.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_plains_battleground

[[SECTION markdown]]

# Helium Plains Battleground

**Role:** Secondary (Combat Setting)

**Geography:** Wide, open plains surrounding the city of Helium; dusty and rugged terrain suitable for large-scale land maneuvers.

**Lighting and Atmosphere:** Bright, sunlit Martian landscape; dust clouds kicked up by Thark thoats and retreating Zodangan ground forces.

**Scale Cues:** Expansive horizontal scale; massive concentrations of green warriors and Heliumite reinforcements clashing across the flats.

**Descriptive Noun Phrases:** Dusty Martian plains, wide battleground flats, cavalry deployment zones, trampled terrain, sprawling land assault site.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_city_metropolis

[[SECTION markdown]]

# Helium City Metropolis

**Role:** Primary (Social/Ceremonial Setting)

**Architecture:** Magnificent, grand architecture of the red-skinned capital; characterized by high towers and ceremonial plazas.

**Lighting and Atmosphere:** Celebratory, bright, and triumphant atmosphere; golden light reflecting off city structures during the triumphal procession.

**Scale Cues:** Grand urban scale; massive crowds of citizens, towering palaces, and wide thoroughfares for processions.

**Descriptive Noun Phrases:** Magnificent Heliumite architecture, grand ceremonial plazas, red-skinned capital city, triumphal procession routes, soaring palace towers.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
