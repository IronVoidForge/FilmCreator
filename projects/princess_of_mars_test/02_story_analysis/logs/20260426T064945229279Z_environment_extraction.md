# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:49:45.229279+00:00
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

Chapter id: CH013

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
The city of the green Martian horde (under Lorquas Ptomel) and its surrounding plazas; the Martian night under two moons.

**Characters:**
* **John Carter:** An Earthman who has integrated into Thark culture, learning their arts of war and animal husbandry.
* **Tars Tarkas:** A Thark warrior/leader who instructs Carter in combat.
* **Dejah Thoris:** A Red Martian Princess; the love interest of John Carter.
* **Sola:** Dejah Thoris's companion.
* **Lorquas Ptomel:** The leader of the green Martian community.

**Events:**
* **Training and Domestication:** Following a battle with air ships, the community remains in the city for several days. During this time, Carter learns to ride "thoats" (large, vicious beasts). Unlike the Tharks who use force, Carter uses a combination of authority and kindness to tame them. His success is so great that he teaches Tars Tarkas and other warriors his method, resulting in more docile mounts and earning him a gold anklet from Lorquas Ptomel as a reward.
* **The Departure:** After seven days, the community prepares to march toward Thark. 
* **Meeting Dejah Thoris:** Carter meets Dejah Thoris and Sola in the plaza. He learns that the older women of the Thark retinue have been intentionally separating him from Dejah Thoris and forcing her into arduous labor (mixing radium-based explosives) out of jealousy of her noble lineage.
* **Romantic Development:** Carter and Dejah Thoris share a private moment walking through the city at night. They discuss Martian warfare, the nature of enemies, and their mutual feelings. Dejah Thoris hints at the significance of Carter calling her "my chieftain," though he does not yet fully grasp the weight of the term. The chapter concludes with the realization of Carter's deep love for her during a quiet moment under the Martian moons.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [green_martian_city_complex](green_martian_city_complex)
- [martian_night_plaza](martian_night_plaza)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: green_martian_city_complex

[[SECTION markdown]]

# Green Martian City Complex

**Role:** Primary setting (community hub and training grounds).

**Architecture & Geography:** A sprawling urban settlement inhabited by the green Martian horde; contains specialized areas for animal husbandry, domestication of thoats, and communal living.

**Lighting & Atmosphere:** Harsh, functional daylight; dusty and active during training sessions; sense of organized martial community.

**Scale & Anchors:** Large-scale enclosures for vicious beasts (thoats); wide thoroughfares for marching columns; central hubs for leadership presence.

**Prompt Phrases:** Martian urban sprawl, green Martian architecture, thoat pens, animal husbandry grounds, dusty martial encampment, Thark settlement.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_night_plaza

[[SECTION markdown]]

# Martian Night Plaza

**Role:** Secondary setting (romantic and social interaction).

**Architecture & Geography:** Open public squares within the city; wide plazas used for both labor (mixing explosives) and private walks.

**Lighting & Atmosphere:** Nocturnal; illuminated by the dual light of two Martian moons; quiet, intimate, and vast.

**Scale & Anchors:** Expansive open spaces; silhouettes of city structures against a two-moon sky; large scale under celestial bodies.

**Prompt Phrases:** Dual moonlit sky, Martian night plaza, vast nocturnal landscape, twin moons, shadows of Martian architecture, romantic moonlight.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
