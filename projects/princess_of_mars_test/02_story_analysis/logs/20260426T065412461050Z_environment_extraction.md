# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:54:12.461050+00:00
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

Chapter id: CH016

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
After a twenty-day journey across Martian sea bottoms and canals, John Carter and his companions arrive at the great city of Thark. Upon arrival, Carter is assigned a large building in the city plaza. He reunites with Dejah Thoris and Sola, during which he formally declares his devotion to Dejah Thoris and commands her cooperation in planning an escape. Sola reveals that the priest Sarkoja has influenced Tal Hajus to sentence Dejah Thoris to death in the upcoming games. 

The trio plans a midnight escape via a northern waterway to avoid detection. Carter successfully sneaks out of the city with his thoats, but upon reaching the rendezvous point, he discovers that the plan has been compromised. Realizing the women have likely been intercepted, Carter maneuvers through the city's inner courts and uses his agility to climb into Dejah Thoris's quarters. There, he overhears a Thark chieftain instructing warriors to ambush him and imprison him in the vaults once he returns to the apartment, noting that Dejah Thoris is already in the custody of Tal Hajus.

**Characters:**
* **John Carter:** A warrior and Earthman; driven by his love for Dejah Thoris; demonstrates tactical thinking and physical prowess.
* **Dejah Thoris:** A captive princess of Helium; agrees to cooperate with Carter's escape plan.
* **Sola:** A Thark woman who harbors resentment toward her people's customs; joins the escape plot.
* **Woola:** John Carter's loyal, multi-tusked Martian hound.
* **Thark Chieftain:** An unnamed leader who orchestrates the ambush of John Carter.
* **Tal Hajus (Mentioned):** The Jeddak of Thark, who holds Dejah Thoris captive.
* **Sarkoja (Mentioned):** A powerful priest whose influence has doomed the captives.

**Settings:**
* **The Road to Thark:** A landscape of ruined cities, Martian canals, and cultivated fields with enormous trees.
* **Thark:** A massive ancient city inhabited by green Martians, characterized by grand architecture and large communal plazas.
* **Dejah Thoris's Quarters:** A large, multi-story building in the Thark plaza featuring marble floors and winding stairways.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index: CH016

- [thark_city_and_surroundings](#thark_city_and_surroundings)
- [dejah_thoris_quarters](#dejah_thoris_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_and_surroundings

[[SECTION markdown]]

# Thark City and Surroundings

**Role:** Primary / Transit Setting

**Architecture & Geography:** A massive, ancient Martian city characterized by grand, imposing architecture. The surrounding landscape includes ruined cities, vast Martian canals, and cultivated fields populated by enormous, towering trees.

**Lighting & Atmosphere:** Expansive and ancient; the scale of the ruins suggests a long-lost era. The atmosphere is defined by the transition from the wide, open vistas of the Martian sea bottoms to the dense, structured urbanity of the Thark plaza.

**Scale & Anchors:** Massive communal plazas, sprawling canal networks, and gargantuan vegetation that dwarfs travelers.

**Prompt Phrases:** Ancient Martian metropolis, grand stone architecture, vast desert canals, colossal trees, ruined cityscapes, expansive Thark plaza, Martian sea bottoms.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dejah_thoris_quarters

[[SECTION markdown]]

# Dejah Thoris's Quarters

**Role:** Secondary / Interior Setting

**Architecture & Geography:** A large, multi-story residential building situated within the central Thark plaza. The interior features polished marble floors and complex, winding stairways.

**Lighting & Atmosphere:** Formal and imposing; high-ceilinged spaces with a sense of grandeur and confinement. Lighting is dictated by the architectural layout of the inner courts and upper quarters.

**Scale & Anchors:** Multi-story verticality, winding stone stairs, marble floor surfaces, plaza-facing windows/balconies.

**Prompt Phrases:** Grand Martian interior, multi-story stone residence, polished marble floors, winding staircases, high-ceilinged chambers, Thark urban architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
