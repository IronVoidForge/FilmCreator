# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:41:33.046027+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

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

**Setting:** A mushroom in a forest setting; later, the treetops (viewed from a high vantage point).

**Characters:**
* **Alice:** A young girl experiencing fluctuating physical sizes.
* **The Caterpillar:** A languid, stern creature smoking a hookah.
* **The Pigeon:** A frantic bird mistaking Alice for a serpent.

**Events/Sequence:**
1. **The Dialogue of Identity:** The Caterpillar questions Alice's identity. Alice explains her confusion caused by frequent size changes. The Caterpillar dismisses her concerns about metamorphosis (chrysalis/butterfly) as trivial.
2. **The Poem:** To test her, the Caterpillar has Alice recite "You are old, Father William." Alice recites a version of the poem; the Caterpillar critiques it for being inaccurate.
3. **Size Discussion:** The Caterpillar asks what size Alice wants to be. She expresses a desire to be slightly larger than three inches (the Caterpillar's height). 
4. **The Departure:** The Caterpillar leaves, revealing that one side of the mushroom makes one grow taller and the other shorter. It disappears into the grass.
5. **The First Transformation:** Alice breaks off a piece of the mushroom edge and eats it. She shrinks rapidly until her chin hits her foot. 
6. **The Second Transformation:** To fix this, she eats a morsel from the other side. Her neck grows immensely long (like a serpent), while her body stays high above the trees.
7. **The Pigeon Encounter:** A large Pigeon flies into Alice's face, mistaking her long neck for a serpent. The Pigeon describes its struggle with "serpents" while hatching eggs. Alice defends her identity as a "little girl."
8. **Restoring Size:** Alice nibbles on the mushroom pieces alternately to regulate her size until she returns to her usual height.
9. **The Discovery:** Alice finds an open space containing a small house (four feet high). To avoid frightening the inhabitants, she eats more of the mushroom to shrink herself down to nine inches.

**Visual/Continuity States:**
* **Initial State:** Alice and Caterpillar at the mushroom.
* **Shrunken State:** Alice is three inches tall; her chin hits her foot after eating a piece of the mushroom.
* **Elongated State:** Alice has an immense neck, looking like a serpent among tree leaves.
* **Final State:** Alice returns to normal size, then shrinks to nine inches before approaching the house.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

* [mushroom_forest_setting](mushroom_forest_setting)
* [treetop_canopy_vantage](treetop_canopy_vantage)
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mushroom_forest_setting

[[SECTION markdown]]

# Mushroom Forest Setting

**Role:** Primary setting.

**Architecture or Geography:** A massive, oversized mushroom serving as a platform; the ground is covered in thick grass and forest floor elements. The mushroom has distinct sides that influence physical size when consumed.

**Lighting and Atmosphere Cues:** Dappled sunlight filtering through forest canopy; surreal, whimsical atmosphere with high-contrast shadows.

**Scale Cues and Recurring Environmental Anchs:** Massive fungal stalks; blades of grass appearing as tall as trees to a shrunken Alice; the mushroom cap serves as a stable table/seat.

**Useful Descriptive Noun Phrases:** Giant fungal platform, thick textured mushroom skin, forest floor micro-landscape, surrealist botanical structure.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: treetop_canopy_vantage

[[SECTION markdown]]

# Treetop Canopy Vantage

**Role:** Secondary setting / Transit-state setting.

**Architecture or Geography:** The upper reaches of the forest canopy; a high-altitude view looking down toward the ground and up into the sky.

**Lighting and Atmosphere Cues:** Bright, airy, wind-swept; intense sunlight; sense of vertigo and vast open space compared to the forest floor.

**Scale Cues and Recurring Environmental Anchs:** Distant ground far below; fluttering leaves; wide horizon lines; Alice's elongated neck bridging the gap between the canopy and the earth.

**Useful Descriptive Noun Phrases:** Aerial canopy view, wind-swept foliage, high-altitude perspective, vast sky backdrop.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
