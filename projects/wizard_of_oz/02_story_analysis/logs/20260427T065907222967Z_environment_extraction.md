# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:59:07.222967+00:00
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

Chapter id: CH005

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

**Setting:** A forest near a small cottage and a spring of clear water; later, the Yellow Brick Road.

**Characters:** 
- Dorothy: A young girl traveling to find Oz.
- Toto: Dorothy's dog.
- Scarecrow: A companion seeking brains.
- Tin Woodman: A man made entirely of tin who has been rusted immobile for a year.

**Events:**
- After waking in the forest, Dorothy and the Scarecrow search for water and food.
- They hear groaning and discover the Tin Woodman, who is frozen in place due to rusted joints.
- Dorothy uses an oil-can from the Woodman's cottage to lubricate his neck, arms, and legs, restoring his mobility.
- The Tin Woodman joins the group, expressing a desire to ask Oz for a heart.
- As they travel, the Woodman uses his axe to clear thick branches blocking the road.
- The Woodman recounts his tragic backstory: once a human wood-chopper, he was systematically dismantled by the Wicked Witch of the East via an enchanted axe. He was rebuilt piece-by-piece with tin, but in the process, he lost his heart and his ability to love.
- A philosophical debate arises between the Scarecrow (who values brains) and the Woodman (who values a heart), leaving Dorothy conflicted as she worries about their dwindling food supplies.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [forest_and_cottage_setting](forest_and_cottage_setting)
- [yellow_brick_road](yellow_brick_road)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: forest_and_cottage_setting

[[SECTION markdown]]

# Forest and Cottage Setting

**Role:** Primary setting (initial encounter).

**Architecture or Geography:** A dense, naturalistic forest characterized by thick branches and undergrowth. Features a small, isolated cottage and a nearby spring of clear water.

**Lighting and Atmosphere Cues:** Dappled sunlight filtering through heavy canopy; organic, earthy atmosphere; sense of isolation and quietude.

**Scale Cues and Recurring Environmental Anchors:** Overhanging branches requiring clearing; the presence of the spring as a central hydration point; the small cottage as a localized shelter.

**Descriptive Noun Phrases:** Dense woodland canopy, clear forest spring, rustic isolated cottage, tangled undergrowth, dappled sunlight shadows.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: yellow_brick_road

[[SECTION markdown]]

# Yellow Brick Road

**Role:** Transit setting.

**Architecture or Geography:** A distinct, structured path cutting through the natural landscape.

**Lighting and Atmosphere Cues:** Bright, directional lighting; clear visibility along the path; sense of progression and journey.

**Scale Cues and Recurring Environmental Anchors:** The road serves as a linear guide through the forest; requires maintenance (clearing branches) to remain passable.

**Descriptive Noun Phrases:** Structured yellow pathway, winding brick road, cleared woodland trail, directional transit route.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
