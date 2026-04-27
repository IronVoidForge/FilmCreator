# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:28:58.946857+00:00
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

Chapter id: CH020

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

**Setting:** The Dainty China Country, a land characterized by a smooth, white, platter-like floor, tiny colorful china houses, and inhabitants made entirely of fragile porcelain.

**Characters:** 
- Dorothy
- Scarecrow
- Tin Woodman
- Cowardly Lion
- Toto
- A China Milkmaid (and her cow)
- A beautiful China Princess
- Mr. Joker (a cracked, foolish China Clown)

**Events:**
- The travelers use a wooden ladder built by the Tin Woodman to climb over a high wall into the Dainty China Country.
- Upon entering, they realize the extreme fragility of the land. Dorothy and her friends must move with extreme caution to avoid breaking anything or anyone.
- A mishap occurs when Dorothy startles a china cow, causing it to kick over a milkmaid; the cow breaks a leg and the milkmaid suffers a nick in her elbow.
- Dorothy meets a beautiful China Princess who explains that while they are pretty, being mended after a break ruins their beauty. The Princess also explains that if they are taken away from their country, they become stiff and lose their ability to move freely.
- They encounter Mr. Joker, a clown covered in cracks from standing on his head too often.
- After traveling through the country for an hour, the group reaches the far wall. While climbing over it, the Lion accidentally smashes a china church with his tail.
- The group successfully exits the China Country, reflecting on the perils of traveling through such a brittle land.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index: Dainty China Country

- [dainty_china_country](#dainty_china_country)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dainty_china_country

[[SECTION markdown]]

# Dainty China Country

**Role:** Primary setting (transitional territory).

**Architecture & Geography:** A landscape defined by a smooth, white, platter-like floor that serves as the ground. The terrain is populated by tiny, colorful china houses and delicate porcelain structures, including small churches.

**Lighting & Atmosphere:** High-key, bright, and reflective lighting due to the polished surfaces. The atmosphere is one of extreme fragility, tension, and precariousness; every movement carries the threat of shattering.

**Scale & Anchors:** Miniature scale relative to the travelers. Recurring anchors include the high perimeter walls that enclose the country and the smooth, seamless white ground plane.

**Descriptive Noun Phrases:** Polished porcelain floor, miniature china village, fragile ceramic architecture, brittle landscape, reflective white platter terrain, tiny colorful porcelain dwellings.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
