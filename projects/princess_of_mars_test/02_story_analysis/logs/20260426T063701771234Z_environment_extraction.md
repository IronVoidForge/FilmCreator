# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:37:01.771234+00:00
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
An enormous, ancient city situated on a low table land near the edge of a dried-up Martian sea. The city features grand, white marble buildings inlaid with gold and jewels, though they appear built for a much smaller, extinct race. A large central plaza serves as the hub for the current inhabitants—a community of Green Martians.

**Characters:**
* **The Narrator (Protagonist):** A human captive attempting to navigate Martian customs through observation and physical prowess.
* **Tars Tarkas:** A high-ranking Green Martian, vice-chieftain of the community, and a skilled statesman/warrior who acts as the narrator's escort.
* **The Chieftain:** The ruler of the local Martian community, characterized by heavy metal ornamentation and a violent temperament.
* **Sola:** A young female Martian (approx. 8 feet tall) with light olive-green skin, belonging to Tars Tarkas's retinue; she provides the narrator with food/shelter.
* **The Martian People:** A race of large, tusked creatures. They are characterized by extreme violence, a lack of empathy for suffering, and a culture where death is often viewed as entertainment.

**Key Events:**
* **Arrival at the City:** The narrator and Tars Tarkas arrive at the deserted, ancient city, which is now occupied by hundreds of Green Martians.
* **Cultural Observations:** The narrator observes Martian biology (differences between sexes/ages) and their grim social customs, including a "voluntary pilgrimage" to the river Iss and a high mortality rate due to constant warfare and dangerous sports.
* **The Audience Chamber:** The party enters a magnificent marble hall to meet the Chieftain. The narrator notes that the furniture is scaled for humans, suggesting the Martians are squatters in an older civilization's ruins.
* **The Confrontation:** After struggling to walk, the narrator accidentally strikes a Martian warrior who was mocking him. Instead of being killed, the narrator is met with laughter and applause, earning respect through his display of aggression.
* **The "Sak" Demonstration:** To prove his worth/ability, the narrator performs a massive leap (sakk) of 150 feet, impressing the crowd.
* **Request for Sustenance:** The narrator refuses to perform further jumps, instead signaling his hunger and thirst.
* **Provisioning:** Sola leads the narrator to a decorated sleeping chamber where he is given rest and encounters a small, ten-legged Martian creature resembling a pony with frog-like features.
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
| ancient_martian_city_ruins | An enormous, ancient city of white marble and gold on a table land near a dried sea. |
| chieftain_audience_chamber | A magnificent marble hall within the ruins, featuring oversized architecture and heavy metal ornamentation. |
| martian_sleeping_quarters | Decorated chambers within the city used for rest and habitation. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_martian_city_ruins

[[SECTION markdown]]

# Ancient Martian City Ruins

**Role:** Primary Setting

**Architecture & Geography:**
An enormous, sprawling city situated on a low table land near the edge of a dried-up Martian sea. The architecture consists of grand, white marble buildings inlaid with gold and precious jewels. The structures appear ancient and were originally built for a much smaller, extinct race, now occupied by larger Green Martians. Features include a large central plaza serving as a communal hub.

**Lighting & Atmosphere:**
Vast, open vistas; bright, reflective surfaces from white marble and gold inlays; dusty, arid atmosphere characteristic of a dried sea basin.

**Scale & Anchors:**
Massive scale; disproportionate architecture (buildings built for smaller beings); the central plaza acts as the primary anchor for social movement.

**Prompt Phrases:**
Ancient white marble city, gold-inlaid ruins, Martian table land, dried sea basin, grand plaza, oversized ancient architecture, jewel-encrusted masonry.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: chieftain_audience_chamber

[[SECTION markdown]]

# Chieftain Audience Chamber

**Role:** Secondary Setting / Narrative Hub

**Architecture & Geography:**
A magnificent marble hall located within the city ruins. The interior features grand scale, though the furniture is scaled for humans (suggesting a mismatch with the current Martian occupants). Decorated with heavy metal ornamentation reflecting the Chieftain's status.

**Lighting & Atmosphere:**
Grand, imposing, and ceremonial; high-contrast lighting from large halls; atmosphere of tension and violent social energy.

**Scale & Anchors:**
Large marble pillars; oversized halls; central seating/throne area for the Chieftain.

**Prompt Phrases:**
Magnificent marble hall, heavy metal ornamentation, ceremonial chamber, grand scale architecture, high-status Martian interior, gold and jewel accents.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sleeping_quarters

[[SECTION markdown]]

# Martian Sleeping Quarters

**Role:** Secondary Setting / Transit

**Architecture & Geography:**
Decorated sleeping chambers located within the city ruins, used for rest and private habitation.

**Lighting & Atmosphere:**
Dimmer, more intimate lighting compared to the plazas; decorated and sheltered atmosphere.

**Scale & Anchors:**
Enclosed rooms; domestic Martian decor; presence of small, ten-legged Martian fauna.

**Prompt Phrases:**
Decorated sleeping chamber, interior Martian dwelling, private quarters, stone walls with ornamentation, dim atmospheric lighting.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
