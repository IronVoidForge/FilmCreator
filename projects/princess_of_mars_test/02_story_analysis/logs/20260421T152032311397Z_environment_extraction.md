# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:20:32.311397+00:00
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

Chapter id: CH017

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

**Events:**
John Carter infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the beastly Jeddak, Tal Hajus. After witnessing Tal Hajus threaten Dejah with prolonged torture and sexual violation, Carter intervenes. Instead of using his sword, he knocks the Jeddak unconscious with a single blow, allowing him to spirit Dejah Thoris and her companion Sola away from the city.

The escape turns into a grueling trek across a two-hundred-mile mossy waste toward Helium. The party suffers from extreme exhaustion, hunger, and thirst; one of their thoats collapses from fatigue, forcing Carter, Sola, and Dejah to continue on foot or with a single animal. During their journey, they are spotted by a Thark chieftain scanning the area with a fieldglass. To ensure the women's escape, Carter uses his Martian rifle to kill the charging chieftain and then stays behind to provide cover fire against a massive force of nearly a thousand warriors. After exhausting his ammunition, Carter attempts to lead the warriors away through acrobatic maneuvers but is eventually overtaken and beaten into unconsciousness.

**Characters:**
* **John Carter:** The protagonist; heroic and selfless; uses tactical thinking and superior weaponry to protect Dejah Thoris.
* **Dejah Thoris:** Princess of Helium; maintains her royal dignity even in the face of terror; expresses profound love for Carter during the escape.
* **Sola:** Dejah Thoris's companion; assists in the escape and helps manage the fleeing thoat.
* **Tal Hajus:** The villainous, bestial Jeddak of the Tharks; characterized by cruelty and animalistic passions.
* **Tars Tarkas:** A Thark warrior who watches the scene with silent loathing for Tal Hajus, though he does not intervene.
* **Woola:** Carter's faithful Martian hound, who tracks the party through the waste.

**Settings:**
* **The City of Thark:** A fortified settlement featuring large circular halls, raised platforms, and multi-story buildings.
* **The Mossy Waste:** A vast, trackless, and desolate expanse between Thark and Helium, characterized by a lack of waterways and extreme environmental hardship.
* **The Low Mountains/Hills:** A rugged terrain toward the end of the chapter that provides both potential landmarks and dangerous ravines for pursuit.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_city_settlement](thark_city_settlement)
- [mossy_waste_expanse](mossy_waste_expanse)
- [rugged_low_mountains](rugged_low_mountains)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_settlement

[[SECTION markdown]]

# Thark City Settlement

**Role:** Primary (Conflict/Infiltration)

**Architecture & Geography:** A fortified Martian settlement featuring large circular halls, raised platforms, and multi-story structures. The layout is designed for a non-humanoid, martial species.

**Lighting & Atmosphere:** Harsh, oppressive, and intimidating; characterized by the shadows of high walls and the looming presence of stone or metal fortifications.

**Scale & Anchors:** Massive scale; large halls and elevated platforms that emphasize the height and strength of the Thark inhabitants.

**Prompt Phrases:** fortified Martian city, circular stone halls, raised combat platforms, multi-story brutalist architecture, Thark settlement.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_waste_expanse

[[SECTION markdown]]

# Mossy Waste Expanse

**Role:** Secondary (Transit/Survival)

**Architecture & Geography:** A vast, trackless, and desolate expanse. The terrain is characterized by a lack of waterways and a pervasive covering of moss-like vegetation.

**Lighting & Atmosphere:** Desolate, grueling, and exposed; an environment of extreme hardship with no natural shelter or shade.

**Scale & Anchors:** Infinite horizon; a two-hundred-mile stretch of featureless, mossy terrain that offers no landmarks for navigation.

**Prompt Phrases:** vast trackless waste, endless mossy plains, desolate Martian landscape, arid mossy expanse, barren wasteland.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: rugged_low_mountains

[[SECTION markdown]]

# Rugged Low Mountains

**Role:** Secondary (Pursuit/Tactical)

**Architecture & Geography:** Rugged, uneven terrain consisting of low hills and mountains. Features dangerous ravines and rocky outcrops.

**Lighting & Atmosphere:** Harsh sunlight and deep shadows within crevices; a sense of claustrophobia within the open landscape due to the ravines.

**Scale & Anchors:** Broken topography; irregular hilltops and narrow, treacherous ravines that serve as natural bottlenecks.

**Prompt Phrases:** rugged low mountains, rocky Martian hills, deep ravines, uneven terrain, jagged foothills.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
