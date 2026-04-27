# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:07:48.165953+00:00
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
Project slug: wizard_of_oz

Chapter id: CH010

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

**Summary:**
After being rescued from a field of deadly poppies by mice, the Cowardly Lion rejoins Dorothy and her companions. The group travels along the yellow brick road through a landscape dominated by green-painted houses and people dressed in emerald attire. They stop at a farmhouse for supper, where a local man informs them of the Great Oz's elusive nature; he explains that the Wizard is a shapeshifter who rarely allows anyone to see his true form. The travelers discuss their specific quests (brains, heart, courage, and returning home) before continuing to the Emerald City. Upon arrival, they encounter the Guardian of the Gates at a massive emerald-studded gate. To prevent them from being blinded by the city's intense green brilliance, the Guardian forces the entire group—including Toto—to wear green-lensed spectacles that are locked onto their heads with a key he holds. The chapter ends as the Guardian leads them into the streets of the Emerald City.

**Characters:**
* **Dorothy:** The leader of the group, seeking to return to Kansas.
* **Scarecrow:** Seeking brains from Oz.
* **Tin Woodman:** Seeking a heart from Oz.
* **Cowardly Lion:** Seeking courage from Oz; recently recovered from poppy sleep.
* **Toto:** Dorothy's dog.
* **Farmer/Woman & Family:** Residents of a green farmhouse who provide food and information about Oz.
* **Guardian of the Gates:** A small, green-skinned man who manages entry to the Emerald City and enforces the use of protective spectacles.

**Settings:**
* **The Yellow Brick Road/Green Countryside:** A beautiful landscape featuring green fences and houses.
* **The Farmhouse:** A residence where the group rests for the night.
* **The Emerald City Gates:** A high, thick green wall with an emerald-studded gate.
* **The Streets of the Emerald City:** The brilliant, glowing interior of the city reached after passing through the gates.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [green_countryside_landscape](green_countryside_landscape)
- [emerald_city_gates](emerald_city_gates)
- [emerald_city_streets](emerald_city_streets)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: green_countryside_landscape

[[SECTION markdown]]

# Green Countryside Landscape

**Role:** Transit setting / Primary travel route.

**Architecture or Geography:** A rolling landscape dominated by the Yellow Brick Road. The terrain is punctuated by green-painted houses and green fences that line the path.

**Lighting and Atmosphere Cues:** Bright, pastoral, and vibrant. The color palette is heavily saturated with greens and yellows.

**Scale Cues and Recurring Environmental Anchors:** Long stretches of the yellow brick road; repetitive patterns of green residential structures.

**Descriptive Noun Phrases:** Saturated green countryside, winding yellow brick road, emerald-hued fences, pastoral green dwellings, vibrant sunlit path.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: emerald_city_gates

[[SECTION markdown]]

# Emerald City Gates

**Role:** Secondary setting / Threshold.

**Architecture or Geography:** A massive, high, and thick green wall serving as the city perimeter. The central feature is a heavy gate studded with large, brilliant emeralds.

**Lighting and Atmosphere Cues:** Intense, shimmering light reflecting off gemstone surfaces; overwhelming brilliance that necessitates protective eyewear.

**Scale Cues and Recurring Environmental Anchors:** Massive verticality of the walls; the singular, imposing emerald-studded gateway.

**Descriptive Noun Phrases:** Colossal green fortification, emerald-studded gate, shimmering gemstone barrier, high verdant walls, blindingly bright threshold.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: emerald_city_streets

[[SECTION markdown]]

# Emerald City Streets

**Role:** Primary setting / Destination.

**Architecture or Geography:** Urban interior characterized by intense green coloration in all structures and surfaces.

**Lighting and Atmosphere Cues:** Extreme brilliance; a glowing, monochromatic green light that permeates the entire environment. High-contrast luminosity.

**Scale Cues and Recurring Environmental Anchors:** Dense urban layout; pervasive emerald glow.

**Descriptive Noun Phrases:** Luminous emerald streets, brilliant green cityscape, glowing verdant architecture, overwhelming green radiance, shimmering metropolitan interior.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
