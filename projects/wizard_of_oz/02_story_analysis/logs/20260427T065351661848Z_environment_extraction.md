# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:53:51.661848+00:00
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

**Setting:** A lush, beautiful country in the Land of Oz, characterized by colorful flowers, fruit-bearing trees, and a sparkling brook.

**Characters:**
- **Dorothy:** A young girl from Kansas, newly arrived in Oz.
- **Toto:** Dorothy's small dog.
- **The Witch of the North:** A kind, elderly woman in white with star-patterned clothing; she is a "good" witch.
- **Munchkins:** A group of small people wearing blue hats with bells and blue clothing; they live in the East.

**Events:**
- Dorothy wakes up to find her house has landed in a beautiful land after the cyclone.
- She discovers that her house accidentally landed on and killed the Wicked Witch of the East, freeing the Munchkins from bondage.
- The Witch of the North arrives to greet Dorothy and explains the geography and politics of Oz, noting that only one Wicked Witch remains (the one in the West).
- The body of the Wicked Witch of the East dries up in the sun, leaving behind a pair of enchanted silver shoes, which are given to Dorothy.
- Dorothy expresses her desire to return to Kansas, but the inhabitants explain that the land is surrounded by impassable deserts.
- Through a magical slate, the Witch of the North determines that Dorothy must travel to the Emerald City to ask the Great Wizard Oz for help.
- The Witch of the North kisses Dorothy's forehead to protect her and directs her toward the Yellow Brick Road before magically disappearing.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [oz_lush_countryside](oz_lush_countryside)
- [yellow_brick_road_pathway](yellow_brick_road_pathway)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: oz_lush_countryside

[[SECTION markdown]]

# Oz Lush Countryside

**Role:** Primary setting.

**Architecture or Geography:** A vibrant, fertile landscape featuring lush vegetation, fruit-bearing trees, and a sparkling brook. The terrain is characterized by rolling hills and dense, colorful flora.

**Lighting and Atmosphere Cues:** Bright, saturated sunlight; high-key lighting; an atmosphere of wonder, magic, and overwhelming color.

**Scale Cues and Recurring Environmental Anchors:** Expansive vistas of blooming flowers; the presence of a clear, flowing brook; large, heavy-fruiting trees that provide shade.

**Descriptive Noun Phrases:** Saturated floral meadows, sparkling crystalline brook, fruit-laden orchards, vibrant Ozian flora, sun-drenched magical landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: yellow_brick_road_pathway

[[SECTION markdown]]

# Yellow Brick Road Pathway

**Role:** Transit setting.

**Architecture or Geography:** A distinct, structured path made of yellow bricks winding through the natural landscape of Oz.

**Lighting and Atmosphere Cues:** Clear visibility; guiding light; a sense of direction and destiny within the bright environment.

**Scale Cues and Recurring Environmental Anchors:** A long, continuous line cutting through the greenery; a singular, man-made (or magic-made) geometric element amidst organic shapes.

**Descriptive Noun Phrases:** Golden brick path, winding yellow road, structured masonry trail, luminous pathway through wildflowers.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
