# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:55:33.076124+00:00
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

Chapter id: CH003

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

**Setting:** The Munchkin Country (characterized by blue houses and round domes) and the Yellow Brick Road, specifically near a large cornfield.

**Characters:** 
- **Dorothy:** A young girl traveling to the Emerald City.
- **Toto:** Dorothy's dog.
- **Boq:** A wealthy Munchkin who hosts Dorothy.
- **The Scarecrow:** A living, straw-stuffed figure perched on a pole in a cornfield.

**Events:**
- Dorothy prepares for her journey by changing into a clean gingham dress and discovering that the silver shoes belonging to the deceased Wicked Witch of the East fit her perfectly.
- She begins walking the Yellow Brick Road toward the Emerald City, observing the prosperous Munchkin farms and receiving respectful bows from the locals.
- Dorothy is invited to a celebration at the home of Boq, a wealthy Munchkin. During the festivities, Boq mistakes her for a "friendly witch" due to her silver shoes and white-and-blue clothing. 
- After a night's rest, Dorothy continues her journey. Boq warns her that the path ahead is long and potentially dangerous.
- While resting near a cornfield, Dorothy encounters a Scarecrow that comes to life. She helps him down from his pole.
- The Scarecrow explains that he lacks brains because his head is stuffed with straw. He asks Dorothy to take him to the Emerald City so the Great Oz might grant him intelligence.
- Dorothy agrees to let him join her. The chapter ends with Dorothy and the Scarecrow walking together along the Yellow Brick Road, while Toto remains skeptical of their new companion.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [munchkin_country_farms](munchkin_country_farms)
- [yellow_brick_road_transit](yellow_brick_road_transit)
- [cornfield_scarecrow_post](cornfield_scarecrow_post)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: munchkin_country_farms

[[SECTION markdown]]

# Munchkin Country Farms

**Role:** Primary / Secondary Setting

**Architecture & Geography:** Prosperous agricultural landscape featuring residential dwellings with distinct blue walls and rounded, dome-shaped roofs. Manicured farms and orderly settlements.

**Lighting & Atmosphere:** Bright, prosperous, and welcoming; a sense of idyllic communal stability.

**Scale & Anchors:** Low-slung, rounded architecture; repetitive patterns of blue domes and domestic farm structures.

**Descriptive Noun Phrases:** Blue-domed houses, rounded architectural silhouettes, prosperous Munchkin homesteads, idyllic pastoral landscape, cobalt-walled dwellings.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: yellow_brick_road_transit

[[SECTION markdown]]

# Yellow Brick Road Transit

**Role:** Transit Setting

**Architecture & Geography:** A defined, continuous path cutting through the Munchkin landscape.

**Lighting & Atmosphere:** Open-air, sunlit, and directional; serves as a guiding visual vector for travel.

**Scale & Anchors:** A singular, winding golden-hued artery that provides a sense of distance and progression toward the horizon.

**Descriptive Noun Phrases:** Winding yellow brick path, golden masonry road, sun-drenched transit route, directional pathway through countryside.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cornfield_scarecrow_post

[[SECTION markdown]]

# Cornfield Scarecrow Post

**Role:** Secondary Setting / Encounter Location

**Architecture & Geography:** A dense, tall cornfield featuring vertical stalks and a central wooden pole used for mounting figures.

**Lighting & Atmosphere:** Dappled sunlight filtering through high vegetation; sense of isolation and sudden movement within the greenery.

**Scale & Anchors:** High-reaching corn stalks creating a claustrophobic or sheltering canopy; a singular wooden post as a focal point.

**Descriptive Noun Phrases:** Towering cornstalks, dappled shade cornfield, rustic wooden mounting pole, dense agricultural foliage, rustling maize landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
