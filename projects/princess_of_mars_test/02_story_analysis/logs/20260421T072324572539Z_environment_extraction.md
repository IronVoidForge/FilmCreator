# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:23:24.572539+00:00
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
After a twenty-day journey through ruined cities and across Martian canals, John Carter and his companions arrive at the great city of Thark. Upon arrival, Carter is assigned a large building in the city plaza. He reunites with Dejah Thoris and Sola, during which he formally declares his devotion to Dejah Thoris and commands her cooperation in planning an escape. Sola informs them that the priest Sarkoja has spoken to Tal Hajus, and Dejah Thoris is slated to be thrown to the wild calots in a forthcoming arena game. 

The trio devises an escape plan: they will travel north via a distant waterway to avoid detection by the Tharks. Carter prepares his thoats and attempts to meet the women at the city's edge under the cover of night. However, he discovers that the plan has been compromised after overhearing mounted warriors discussing the failed rendezvous. To avoid capture with his large animals, Carter hides the thoats in a courtyard filled with moss-like vegetation. He then infiltrates Dejah Thoris's quarters by climbing through a second-story window, only to overhear a Thark chieftain ordering warriors to ambush him and imprison him in the vaults once he returns to the room.

**Characters:**
* **John Carter:** A warrior and Earthman; driven by his love for Dejah Thoris; currently planning an escape from Thark.
* **Dejah Thoris:** A captive princess of Helium; agrees to cooperate with Carter's plan.
* **Sola:** A Thark woman who harbors resentment toward her people's customs; joins the escape plot.
* **Woola:** John Carter's loyal, multi-tusked Martian hound.
* **Thark Chieftain:** An unnamed leader who has organized an ambush for Carter.

**Settings:**
* **The Road to Thark:** A landscape of ruined cities, canals, and cultivated fields with enormous trees.
* **The City of Thark:** A massive ancient city inhabited by thirty thousand green men; characterized by grand architecture and large, hollow-courtyard buildings.
* **Dejah Thoris's Quarters:** A large, multi-story building in the central plaza of Thark.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description |
| :--- | :--- |
| martian_wilderness_corridor | Ruined cities, canals, and cultivated fields with massive trees. |
| city_of_thark | Massive ancient urban center with grand architecture and hollow courtyards. |
| thark_plaza_quarters | Multi-story residential/official buildings within the central plaza. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_wilderness_corridor

[[SECTION markdown]]

# Martian Wilderness Corridor

**Role:** Transit setting

**Geography:** A vast landscape featuring ruined ancient cities, winding Martian canals, and cultivated fields interspersed with enormous, towering trees.

**Lighting and Atmosphere:** Expansive vistas; varying light based on time of day; sense of ancient desolation mixed with life-sustaining waterways.

**Scale Cues:** Enormous tree canopies; wide canal networks; sprawling ruins that dwarf travelers.

**Prompt Phrases:** Ruined Martian cities, winding canals, cultivated fields, colossal trees, vast desert vistas, ancient debris.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: city_of_thark

[[SECTION markdown]]

# City of Thark

**Role:** Primary setting

**Architecture:** A massive, ancient urban complex characterized by grand, imposing architecture and buildings designed around large, hollow courtyards.

**Lighting and Atmosphere:** High-density urban environment; shadows cast by massive structures; bustling atmosphere of a city inhabited by thousands.

**Scale Cues:** Massive scale of stone/metal structures; wide plazas; high walls; dense population density.

**Prompt Phrases:** Ancient Martian metropolis, grand monolithic architecture, hollow courtyard buildings, massive urban sprawl, Tharkian stone structures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_plaza_quarters

[[SECTION markdown]]

# Thark Plaza Quarters

**Role:** Secondary setting

**Architecture:** Large, multi-story buildings located within the central plaza; features second-story windows and interior rooms/vaults. Includes nearby courtyards with moss-like vegetation.

**Lighting and Atmosphere:** Interior shadows; moonlight for night infiltration; enclosed courtyard lighting.

**Scale Cues:** Multi-level verticality; large window apertures; sprawling plaza surroundings.

**Prompt Phrases:** Multi-story stone quarters, central plaza buildings, second-story windows, mossy courtyards, interior vaults, urban residential architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
