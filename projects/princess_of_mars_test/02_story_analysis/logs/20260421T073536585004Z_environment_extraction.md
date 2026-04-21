# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:35:36.585004+00:00
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
The journey begins on the cultivated agricultural tracts between the poles and Zodanga, moving into the vast, walled city of Zodanga, characterized by high-raised residences and a central square plaza.

**Events:**
* **Travel Observations:** John Carter travels toward Zodanga, observing Martian agricultural methods involving underground water conduits and highly refined flora and fauna.
* **Intelligence Gathering:** At a farmhouse, Carter speaks with a Zodangan noble who reveals that the war between Helium and Zodanga is unpopular and that Dejah Thoris is rumored to be dead following an encounter with Tharks and Warhoons.
* **Arrival at Zodanga:** Carter arrives at the gates of Zodanga. He makes the difficult decision to part ways with his loyal companion, the dog Woola, to ensure the dog's safety during his infiltration of the city.
* **Reunion with Kantos Kan:** In the central plaza, Carter reunites with Kantos Kan, a Red Martian ally. Kantos Kan reveals he is working as an air scout to find Dejah Thoris, who is reportedly being held by Prince Sab Than.
* **Infiltration:** Using a ruse facilitated by Kantos Kan, Carter enrolls in the Zodangan air-scout squadron. He spends several days learning Martian aviation and the mechanics of eighth-ray propulsion.
* **Combat and Heroism:** During a solo flight, Carter discovers a Zodangan scout (a cousin of the Jeddak) being pursued by three Green Martian warriors. Carter intervenes, killing the warriors and saving the scout.
* **Recognition:** Carter and the scout return to Zodanga. During a massive military ceremony in the plaza, Carter is publicly honored by Jeddak Than Kosis for his bravery. He is appointed a *padwar* of The Guards and granted quarters in the palace.

**Characters:**
* **John Carter:** The protagonist; an Earthman with superhuman abilities who successfully infiltrates the Zodangan military.
* **Woola:** Carter's loyal, non-domesticated Martian hound (parted with at the city gates).
* **Kantos Kan:** A Red Martian ally and air scout who assists Carter's infiltration.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **The Zodangan Scout:** A cousin of Than Kosis, rescued by Carter from Green Martians.

**Key Concepts:**
* **Eighth Ray Propulsion:** A Martian scientific discovery involving the repulsion of gravity used to power airships.
* **Zodangan Social Structure:** High-raised buildings to prevent assassination and a lack of common thievery.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [martian_agricultural_tracts](martian_agricultural_tracts)
- [zodanga_cityscape](zodanga_cityscape)
- [zodanga_central_plaza](zodanga_central_plaza)
- [zodangan_palace_quarters](zodangan_palace_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_agricultural_tracts

[[SECTION markdown]]

# Martian Agricultural Tracts

**Role:** Transit / Secondary Setting

**Geography:** Cultivated tracts located between the poles and Zodanga; characterized by highly refined flora and fauna. Features underground water conduit systems for irrigation.

**Lighting & Atmosphere:** Open, sunlit Martian plains; organized and engineered landscape.

**Scale & Anchors:** Vast stretches of managed vegetation; subterranean infrastructure visible through surface modifications.

**Prompt Phrases:** Refined Martian flora, underground water conduits, cultivated agricultural tracts, engineered landscapes, vast Martian plains.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_cityscape

[[SECTION markdown]]

# Zodanga Cityscape

**Role:** Primary Setting / Transit

**Geography:** A massive, walled city. Architecture is defined by high-raised residences designed to prevent assassination and facilitate security.

**Lighting & Atmosphere:** Urban Martian atmosphere; imposing stone or metal walls; verticality emphasized by elevated living structures.

**Scale & Anchors:** Massive defensive walls; towering residential heights; dense urban layout.

**Prompt Phrases:** Walled Martian city, high-raised residences, Zodangan architecture, fortified urban center, vertical city structures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_central_plaza

[[SECTION markdown]]

# Zodanga Central Plaza

**Role:** Primary Setting

**Geography:** A large, central open square within the city of Zodanga. Serves as a hub for military ceremonies and social gathering.

**Lighting & Atmosphere:** Grand, ceremonial lighting; wide-open spaces capable of hosting massive crowds and military parades.

**Scale & Anchors:** Massive scale; central focal point for the city; surrounded by high-raised buildings.

**Prompt Phrases:** Grand central plaza, ceremonial square, Zodangan military parade grounds, vast urban open space, monumental architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodangan_palace_quarters

[[SECTION markdown]]

# Zodangan Palace Quarters

**Role:** Primary Setting

**Geography:** Interior residential quarters located within the royal palace of Than Kosis.

**Lighting & Atmosphere:** Regal, high-status atmosphere; controlled interior lighting; secure and prestigious environment.

**Scale & Anchors:** Large-scale palatial rooms; high ceilings; proximity to the seat of power.

**Prompt Phrases:** Royal palace interiors, Zodangan noble quarters, palatial living spaces, high-status Martian architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
