# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:29:35.822788+00:00
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

Chapter id: CH014

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

**Settings:**
*   The camp and outskirts of the Thark expeditionary force during the march toward Thark.
*   A Warhoon incubator site containing small, newly-laid green Martian eggs.

**Characters:**
*   **John Carter:** A human fighting for Dejah Thoris; currently experiencing romantic tension and physical combat.
*   **Dejah Thoris:** Princess of Helium; she is offended by John's perceived social indiscretion and remains aloof/angry toward him.
*   **Tars Tarkas:** Thark chieftain; shows a pragmatic, almost human-like undercurrent of compassion by unchaining Dejah Thoris.
*   **Sola:** Dejah Thoris’s faithful companion; she attempts to mediate between the lovers and eventually sacrifices herself.
*   **Sarkoja:** A female Thark driven by intense hatred for John Carter; orchestrates a distraction to facilitate his death.
*   **Zad:** An *o mad* (warrior with one name) who challenges John Carter to a formal duel.

**Key Events:**
*   **Romantic Tension:** John Carter reflects on his unspoken love for Dejah Thoris and the cultural misunderstandings regarding courtship on Barsoom that have caused her to shun him.
*   **The Departure:** The group begins their march toward Thark. John discovers Dejah Thoris is being heavily manacled by Sarkoja, but Tars Tarkas intervenes to ensure she is treated with more dignity, eventually unchaining her himself.
*   **Warhoon Incubator:** During the march, the party discovers and destroys a Warhoon incubator, destroying small green Martian eggs.
*   **The Duel:** Zad challenges John Carter to a formal duel with long-swords. During the fight, Sarkoja uses a mirror to flash sunlight into John's eyes to blind him.
*   **Chaos in the Chariot:** As John is blinded, Dejah Thoris confronts Sarkoja. Sola leaps in front of Sarkoja’s dagger to protect the Princess, taking the blow.
*   **The Climax:** Amidst the chaos, Zad delivers a fatal thrust to John Carter's chest, and John collapses as he loses consciousness.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_expedition_march_route](thark_expedition_march_route)
- [warhoon_incubator_site](warhoon_incubator_site)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_expedition_march_route

[[SECTION markdown]]

# Thark Expedition March Route

**Role:** Primary / Transit Setting

**Architecture or Geography:** Open Martian landscape; rugged, arid terrain characteristic of the Barsoomian wilderness. The route is traversed by a marching expeditionary force including Tharks and captives.

**Lighting and Atmosphere Cues:** Harsh, direct sunlight; high-contrast shadows; dusty atmosphere; intense glare (noted during the duel).

**Scale Cues and Recurring Environmental Anchors:** Vast, sweeping horizons; wide-open vistas interrupted by localized combat zones or obstacles.

**Descriptive Noun Phrases:** Arid Martian wasteland, sun-drenched plains, rugged expedition path, high-contrast desert light, dusty Barsoomian horizon.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_incubator_site

[[SECTION markdown]]

# Warhoon Incubator Site

**Role:** Secondary Setting

**Architecture or Geography:** A localized, specialized biological site; contains clusters of small, newly-laid green Martian eggs.

**Lighting and Atmosphere Cues:** Likely sheltered or semi-enclosed compared to the open march; focused on the organic presence of the incubator.

**Scale Cues and Recurring Environmental Anchors:** Small-scale biological cluster; concentrated area of life/eggs amidst the barren landscape.

**Descriptive Noun Phrases:** Warhoon egg cluster, green Martian eggs, biological incubation site, localized organic nursery.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
