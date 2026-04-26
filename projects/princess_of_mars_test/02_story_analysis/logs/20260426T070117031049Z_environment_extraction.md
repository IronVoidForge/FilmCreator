# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:01:17.031049+00:00
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

Chapter id: CH021

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
The journey begins on the cultivated agricultural tracts between the polar ice caps and populated centers, moving toward the vast, walled city of Zodanga. The setting features advanced Martian infrastructure, including underground water conduits, high-rise metal residences, and a central plaza surrounded by palaces and mechanical cafes.

**Characters:**
* **John Carter:** The protagonist, an Earthman with superhuman leaping abilities, currently undercover in Zodanga.
* **Woola:** Carter's loyal, domesticated creature, whom he must leave behind for safety.
* **Kantos Kan:** A Red Martian and friend of Carter; an air scout working to find Dejah Thoris.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **Sab Than:** The Prince of Zodanga, who has fallen in love with Dejah Thoris.
* **The Zodangan Cousin:** A member of the royal family saved by Carter during a skirmish.
* **Green Warriors:** Thark/Warhoon-style combatants who attack the Zodangan scout.

**Events:**
1. **Travel and Lore:** Carter travels through Martian farmlands, learning about their sophisticated irrigation and highly refined biological life. He learns from a noble that Dejah Thoris is presumed dead following a conflict with Tharks and Warhoons.
2. **Arrival at Zodanga:** Carter arrives at the gates of Zodanga and reluctantly separates from Woola to avoid drawing attention to his companion's unique species.
3. **Reunion with Kantos Kan:** In the central plaza, Carter reunites with Kantos Kan. They discuss the political tension: Sab Than intends to marry Dejah Thoris to secure peace, a demand rejected by Helium.
4. **Infiltration:** Kantos Kan uses his influence to enroll Carter as an air scout in the Zodangan navy under the alias "John Carter." Carter spends several days learning Martian aviation and the mechanics of the "eighth ray" propulsion.
5. **The Skirmish:** During a solo flight, Carter discovers three Green Warriors attacking a Zodangan air scout (a cousin of the Jeddak). Carter intervenes, killing the warriors and saving the scout.
6. **Recognition:** Carter and the scout return to Zodanga. During a massive military ceremony in the plaza, Carter is publicly honored by Jeddak Than Kosis for his bravery. He is appointed a *padwar* of The Guards and granted quarters within the royal palace.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH021

- [martian_agricultural_tracts](martian_agricultural_tracts)
- [zodanga_city_gates](zodanga_city_gates)
- [zodanga_central_plaza](zodanga_central_plaza)
- [zodangan_aviation_training_grounds](zodangan_aviation_training_grounds)
- [royal_palace_quarters](royal_palace_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_agricultural_tracts

[[SECTION markdown]]

# Martian Agricultural Tracts

**Role:** Transit setting.

**Geography:** Vast, cultivated tracts of land situated between the polar ice caps and major population centers. Features advanced irrigation systems including underground water conduits.

**Lighting/Atmosphere:** Open sky, bright Martian sun, highly refined biological life, organized and engineered landscape.

**Scale/Anchors:** Expansive horizons, network of subterranean pipes, rhythmic patterns of cultivated vegetation.

**Prompt Phrases:** vast cultivated plains, advanced irrigation conduits, engineered Martian farmlands, biological refinement, open planetary vistas.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_city_gates

[[SECTION markdown]]

# Zodanga City Gates

**Role:** Transit setting / Threshold.

**Geography:** Massive, walled entrance to the city of Zodanga. High-security perimeter marking the transition from wild plains to urban infrastructure.

**Lighting/Atmosphere:** Imposing, monumental, high-contrast shadows against massive walls.

**Scale/Anchors:** Enormous defensive walls, heavy gate structures, transition point for travelers.

**Prompt Phrases:** colossal city walls, fortified Zodangan gates, monumental masonry, urban threshold, imposing defensive architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_central_plaza

[[SECTION markdown]]

# Zodanga Central Plaza

**Role:** Primary setting.

**Geography:** A massive urban hub surrounded by palaces and mechanical cafes. High-density area featuring high-rise metal residences.

**Lighting/Atmosphere:** Bustling, vibrant, metallic reflections, social hub atmosphere, grand scale.

**Scale/Anchors:** Surrounding palaces, towering metal residential structures, central gathering space for military ceremonies.

**Prompt Phrases:** sprawling urban plaza, high-rise metal architecture, mechanical cafes, palace-lined square, bustling Martian metropolis, ceremonial assembly ground.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodangan_aviation_training_grounds

[[SECTION markdown]]

# Zodangan Aviation Training Grounds

**Role:** Secondary setting.

**Geography:** Specialized training area for air scouts, likely integrated with the city's verticality or outskirts.

**Lighting/Atmosphere:** High altitude, windy, technical, focused on mechanical propulsion.

**Scale/Anchors:** Flight paths, eighth-ray propulsion mechanics, aerial maneuvering zones.

**Prompt Phrases:** aviation training airspace, eighth-ray propulsion arrays, aerial scout training grounds, high-altitude flight corridors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: royal_palace_quarters

[[SECTION markdown]]

# Royal Palace Quarters

**Role:** Primary setting (Interior).

**Geography:** High-status residential area within the central palace complex of Zodanga.

**Lighting/Atmosphere:** Opulent, prestigious, secure, interior lighting.

**Scale/Anchors:** Grand palace halls, elite living quarters, proximity to the Jeddak's seat of power.

**Prompt Phrases:** opulent royal chambers, high-status Martian residence, palatial interior, elite guard quarters, grand architectural detail.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
