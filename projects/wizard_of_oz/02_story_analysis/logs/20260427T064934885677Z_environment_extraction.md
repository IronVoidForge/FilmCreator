# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:49:34.885677+00:00
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

Chapter id: CH002

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

**Setting:** A lush, beautiful country filled with colorful flowers, fruit-bearing trees, and a sparkling brook; specifically, the land of the Munchkins in the East.

**Characters:**
- **Dorothy:** A young girl from Kansas, confused by her sudden arrival in Oz.
- **Toto:** Dorothy's small dog.
- **The Witch of the North:** A kind, elderly woman in white with star-patterned clothing; a "good" witch who provides guidance.
- **Munchkins:** A group of small people wearing blue hats and outfits; they are grateful to Dorothy for liberating them.

**Events:**
- Dorothy wakes up in the Land of Oz after her house lands safely following a cyclone.
- She discovers that her house has landed on and killed the Wicked Witch of the East, whose feet (wearing silver shoes) are visible under the house.
- The Munchkins and the Witch of the North arrive to greet Dorothy, mistakenly treating her as a "noble Sorceress" for killing the wicked ruler.
- The Witch of the East's body dries up in the sun, leaving only the enchanted silver shoes, which the Witch of the North gives to Dorothy.
- Dorothy expresses her desire to return to Kansas, but is informed that the land is surrounded by impassable deserts and ruled by other witches.
- Through a magical slate, the Witch of the North determines that Dorothy must travel to the Emerald City to ask the Great Wizard Oz for help.
- The Witch of the North kisses Dorothy's forehead to protect her and directs her toward the Yellow Brick Road.
- The Witch of the North disappears magically, leaving Dorothy to begin her journey.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - Chapter CH002

## Munchkin Country (East)
- [munchkin_country_lush_lands](munchkin_country_lush_lands)

## The Crash Site
- [house_landing_site](house_landing_site)

## Transit Routes
- [yellow_brick_road](yellow_brick_road)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: munchkin_country_lush_lands

[[SECTION markdown]]

# Munchkin Country Lush Lands

**Role:** Primary setting.

**Architecture or Geography:** A lush, fertile landscape characterized by rolling hills, fruit-bearing trees, and vibrant, colorful flower beds. A sparkling brook meanders through the terrain.

**Lighting and Atmosphere Cues:** Bright, saturated colors; high-key lighting; a sense of idyllic, magical abundance; warm and welcoming atmosphere.

**Scale Cues and Recurring Environmental Anchors:** Expansive floral vistas; rhythmic patterns of fruit trees; the gentle movement of the sparkling brook.

**Descriptive Noun Phrases:** Saturated flower meadows, fruit-laden orchards, sparkling crystalline brook, vibrant Munchkin landscape, idyllic Ozian countryside.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: house_landing_site

[[SECTION markdown]]

# House Landing Site

**Role:** Secondary setting / Event location.

**Architecture or Geography:** A localized clearing where a farmhouse has impacted the ground, creating a focal point of destruction amidst the lush greenery. Visible remains (feet in silver shoes) are partially obscured by the structure.

**Lighting and Atmosphere Cues:** Dappled sunlight; high contrast between the domesticity of the house and the magical landscape; sudden transition from cyclone chaos to eerie stillness.

**Scale Cues and Recurring Environmental Anchors:** The heavy, grounded mass of the farmhouse; the silver glint of shoes beneath the floorboards.

**Descriptive Noun Phrases:** Impacted farmhouse, crushed vegetation, silver shoe glint, localized clearing, domestic wreckage in paradise.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: yellow_brick_road

[[SECTION markdown]]

# Yellow Brick Road

**Role:** Transit setting.

**Architecture or Geography:** A distinct, structured path cutting through the natural landscape of Munchkin Country.

**Lighting and Atmosphere Cues:** Guiding light; a clear visual trail amidst the colorful chaos of the surrounding flora.

**Scale Cues and Recurring Environmental Anchors:** A continuous, winding line providing directionality toward the horizon (Emerald City).

**Descriptive Noun Phrases:** Winding yellow path, structured brick walkway, guiding transit route, golden-hued road.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
