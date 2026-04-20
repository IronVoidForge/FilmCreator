# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:43:52.923391+00:00
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

Chapter id: CH004

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
The chapter begins with a journey across a rising landscape toward the edge of a long-dead Martian sea. The party arrives at an enormous, ancient city situated on a low table land. The city features grand, white marble and gold architecture that appears far too large for its current inhabitants, suggesting it was built by a long-extinct race. Key locations include a central plaza and a magnificent audience chamber filled with oversized furniture.

**Characters:**
* **The Narrator (Human):** A captive being escorted through the Martian city. He struggles with his physical inadequacy compared to the Martians but demonstrates strength and agility.
* **Tars Tarkas:** A Green Martian vice-chieftain, described as a capable statesman and warrior. He acts as the narrator's escort/guard.
* **The Chieftain:** The ruler of the local community, an enormous warrior adorned in metal, feathers, and silk.
* **Sola:** A young female Martian (approx. 8 feet tall) with light olive-green skin, belonging to Tars Tarkas's retinue. She provides the narrator with food and shelter.
* **The Martians (Green Men):** A violent, multi-legged species. They are characterized by their lack of clothing (except ornaments), large tusks, and a culture that finds humor in death and suffering.

**Key Events:**
* **Arrival at the City:** The narrator and Tars Tarkas enter a deserted but grand city, discovering it is populated by hundreds of Green Martians.
* **The Audience Chamber:** The party enters a massive hall to meet the Chieftain. The narrator observes that the Martian's furniture is scaled for humans, implying an older, lost civilization.
* **Physical Confrontation:** After struggling to walk due to his different physiology, the narrator accidentally strikes a Martian who was mocking him. Instead of being punished, he is met with laughter and applause, earning a rare sign of respect.
* **The "Sak" Demonstration:** To prove his worth/ability, the narrator performs a massive leap (sakk) of 150 feet, impressing the gathered warriors.
* **Request for Sustenance:** The narrator refuses to perform further jumps until he is fed and watered, using gestures to communicate his hunger.
* **Introduction to Sola and Martian Fauna:** Tars Tarkas assigns Sola to care for the narrator. She leads him to a decorated sleeping chamber, where the narrator encounters a small, ten-legged, frog-like creature with three rows of tusks that acts as a pet.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_martian_city](#ancient_martian_city)
- [chieftain_audience_chamber](#chieftain_audience_chamber)
- [solas_sleeping_chamber](#solas_sleeping_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_martian_city

[[SECTION markdown]]

# Ancient Martian City

**Role:** Primary / Transit Setting

**Architecture & Geography:** A vast, sprawling city situated on a low table land near the edge of a long-dead Martian sea. The architecture is characterized by grand, white marble structures and gold accents. The scale is immense, designed for much larger beings than the current inhabitants.

**Lighting & Atmosphere:** Expansive, open vistas; sense of ancient desolation mixed with active, violent life; bright, high-contrast sunlight reflecting off white stone and gold.

**Scale & Anchors:** Enormous city gates; wide plazas; massive marble columns; views of the dead sea horizon.

**Prompt Phrases:** Ancient Martian metropolis, white marble ruins, gold filigree architecture, table land plateau, dead sea basin, colossal scale, sun-bleached stone.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: chieftain_audience_chamber

[[SECTION markdown]]

# Chieftain's Audience Chamber

**Role:** Primary Setting

**Architecture & Geography:** A magnificent, oversized hall within the central city structures. The interior is dominated by furniture that is disproportionately large for humans, suggesting a lost civilization of giants.

**Lighting & Atmosphere:** Grandiose and intimidating; cavernous shadows contrasted with bright light hitting gold ornaments; high-status ceremonial atmosphere.

**Scale & Anchors:** Oversized thrones/seating; massive floor space; towering ceilings; central gathering area for warriors.

**Prompt Phrases:** Colossal audience hall, oversized Martian furniture, grand marble chamber, ceremonial hall, intimidating scale, golden accents, cavernous interior.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: solas_sleeping_chamber

[[SECTION markdown]]

# Sola's Sleeping Chamber

**Role:** Secondary Setting

**Architecture & Geography:** A decorated, private living space within the city. It is more intimate than the public halls but still retains the grander scale of Martian construction.

**Lighting & Atmosphere:** Domesticated yet alien; softer lighting compared to the plazas; sense of shelter and respite.

**Scale & Anchors:** Decorated walls; sleeping areas; presence of small, exotic Martian fauna (ten-legged frog-like creatures).

**Prompt Phrases:** Decorated Martian living quarters, intimate stone chamber, alien domestic interior, soft light, ornate sleeping area.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
