# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:57:31.447222+00:00
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
An enormous, ancient city situated on a low table land near the edge of a dried-up Martian sea. The city features magnificent marble and gold architecture that appears far too large for its current inhabitants, suggesting it was built by a forgotten, more advanced race. Key locations include a central plaza and a grand audience chamber filled with human-sized furniture that the Martians struggle to use.

**Characters:**
* **The Narrator (Protagonist):** An Earthman captured by Martians; physically much smaller than his captors but capable of surprising feats of strength and agility.
* **Tars Tarkas:** A high-ranking Green Martian, vice-chieftain of the community, and a skilled statesman/warrior who acts as the narrator's escort.
* **The Chieftain:** The ruler of the local Martian community, adorned in elaborate metal, feather, and silk regalia.
* **Sola:** A young female Martian (approx. 8 feet tall) with light olive-green skin, belonging to Tars Tarkas's retinue; she provides the narrator with food/sustenance.
* **The Martians:** A race of ten-foot-tall, multi-legged creatures characterized by extreme violence, a lack of empathy for suffering, and a culture where death is often treated as a source of amusement.

**Key Events:**
* **Arrival at the City:** The narrator and Tars Tarkas arrive at the deserted, ancient city and enter the central plaza, which is populated by hundreds of Martians.
* **The Audience:** The narrator is presented to the Chieftain in a grand hall. He observes the discrepancy between the Martian biology and the human-sized furniture, noting the antiquity of the ruins.
* **Demonstration of Strength:** After being mocked for his clumsy movement, the narrator punches a Martian warrior who treats him roughly. To his surprise, this act of violence earns him respect and applause from the crowd.
* **The "Sak" Test:** The narrator is commanded to perform "sak" (jumping). He successfully clears 150 feet in a single leap, impressing the assembly.
* **Demand for Sustenance:** Refusing to jump again until his needs are met, the narrator signals his hunger and thirst through gestures.
* **Introduction to Sola:** Tars Tarkas assigns Sola to care for the narrator. She leads him to a decorated sleeping chamber, where he encounters a small, ten-legged Martian creature resembling a pony with a frog-like head and three rows of tusks.
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
| ancient_martian_city_plaza | A massive, open central plaza within an oversized marble and gold city. |
| grand_audience_chamber | An immense hall featuring disproportionately large furniture and ancient architecture. |
| martian_sleeping_chamber | A decorated private room containing small Martian fauna. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_martian_city_plaza

[[SECTION markdown]]

# Ancient Martian City Plaza

**Role:** Primary / Transit Setting

**Architecture & Geography:** An enormous, open-air central plaza situated on a low table land near the edge of a dried-up Martian sea. The surrounding city is composed of magnificent marble and gold architecture, characterized by an ancient, advanced style that feels vastly oversized for its current inhabitants.

**Lighting & Atmosphere:** Expansive, sun-drenched scale; open sky; sense of vastness and antiquity.

**Scale & Anchors:** Massive stone paving; hundreds of ten-foot-tall Martian figures; distant ruins of a dried sea bed; monumental scale that dwarfs human proportions.

**Prompt Phrases:** Ancient marble city, gold-trimmed architecture, massive open plaza, dried Martian sea horizon, colossal scale, sunlit ruins, ancient civilization.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: grand_audience_chamber

[[SECTION markdown]]

# Grand Audience Chamber

**Role:** Primary Setting

**Architecture & Geography:** A cavernous, high-ceilinged hall within the central city. The interior features grand, ancient architecture and furniture that is human-sized but appears small or misplaced relative to the ten-foot-tall Martian occupants.

**Lighting & Atmosphere:** Grandiose, imposing, ceremonial; shadows cast by massive structures; atmosphere of formal power and ancient weight.

**Scale & Anchors:** Disproportionate furniture; high vaulted ceilings; central dais for the Chieftain; monumental scale cues.

**Prompt Phrases:** Grand audience hall, oversized marble architecture, ceremonial chamber, disproportionate furniture, ancient Martian throne room, cavernous interior.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sleeping_chamber

[[SECTION markdown]]

# Martian Sleeping Chamber

**Role:** Secondary Setting

**Architecture & Geography:** A decorated, enclosed private room within the city.

**Lighting & Atmosphere:** Intimate but alien; decorated surfaces; domestic Martian atmosphere.

**Scale & Anchors:** Decorated walls; presence of small ten-legged Martian creatures (pony-like with frog heads and tusks).

**Prompt Phrases:** Decorated sleeping chamber, Martian interior, intimate ancient room, exotic fauna, alien domesticity.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
