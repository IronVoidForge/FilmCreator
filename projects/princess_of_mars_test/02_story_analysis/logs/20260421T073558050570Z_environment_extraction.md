# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:35:58.050570+00:00
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

Chapter id: CH016

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

**Setting:** The ancient, sprawling city of Thark, characterized by massive, grand architecture and divided into quarters for different communities under the rule of Tal Hajus.

**Characters:**
* **John Carter:** A human warrior attempting to orchestrate an escape for Dejah Thoris.
* **Dejah Thoris:** Princess of Helium, currently a captive of the Tharks.
* **Sola:** A Thark woman who harbors sympathies for the protagonists.
* **Tal Hajus:** The Jeddak (ruler) of Thark.
* **Woola:** John Carter's loyal, multi-tusked Martian hound.
* **Sarkoja:** A Thark priest/advisor whose machinations threaten the protagonists.

**Events:**
* **The Journey to Thark:** John Carter, Dejah Thoris, and Sola travel for twenty days across sea bottoms and canals, moving stealthily under cover of darkness to avoid Martian patrols.
* **Arrival in Thark:** The group enters the city of Thark, where they are assigned quarters based on their status as captives/warriors. John Carter occupies a large building near the central plaza.
* **The Declaration:** John Carter visits Dejah Thoris and formally declares his devotion to her, commanding her to assist him in her own escape. 
* **The Threat Revealed:** Sola arrives with news that Sarkoja has advised Tal Hajus to throw Dejah Thoris to the wild dogs in the upcoming yearly games.
* **Escape Planning:** Using a map drawn by Dejah Thoris on a marble floor, the trio decides to flee via a northern waterway that leads toward Helium, hoping to bypass the more heavily patrolled southern routes.
* **The Failed Rendezvous:** John Carter slips out of the city at night with his thoats (mounts) to meet the women at the city edge. However, he discovers that the escape plan has been compromised by Thark warriors.
* **The Ambush Plot:** After hiding his animals in a courtyard, John Carter attempts to return to Dejah Thoris's quarters. He overhears a Thark chieftain instructing warriors to ambush him and take him to the vaults beneath the Jeddak's quarters, while Dejah Thoris is being taken directly to Tal Hajus.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH016

- [thark_city_quarters](thark_city_quarters)
- [martian_sea_bottoms_and_canals](martian_sea_bottoms_and_canals)
- [jeddak_vaults_and_quarters](jeddak_vaults_and_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_quarters

[[SECTION markdown]]

# Thark City Quarters

**Role:** Primary setting.

**Architecture or Geography:** A sprawling, ancient metropolis characterized by massive, grand architecture. The city is divided into distinct quarters based on community and status. Features include central plazas, large stone buildings, and marble-floored chambers used for planning.

**Lighting and Atmosphere Cues:** Grandiose but oppressive; shadows cast by monolithic structures; nocturnal atmosphere during stealth movements; high-contrast lighting between open plazas and enclosed quarters.

**Scale Cues and Recurring Environmental Anchors:** Massive scale of buildings; wide central plazas; large marble floors; walled courtyards used for stabling mounts.

**Descriptive Noun Phrases:** Monolithic Thark architecture, sprawling ancient metropolis, grand stone plazas, marble-floored chambers, shadowed city quarters, massive urban canyons.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sea_bottoms_and_canals

[[SECTION markdown]]

# Martian Sea Bottoms and Canals

**Role:** Transit setting.

**Architecture or Geography:** Low-lying terrain consisting of dried sea bottoms and winding canal networks used for stealthy travel.

**Lighting and Atmosphere Cues:** Dark, nocturnal environments; moonlight reflecting off canal waters; low visibility; sense of isolation and vulnerability.

**Scale Cues and Recurring Environmental Anchors:** Expansive, flat sea beds; narrow, winding waterways; long stretches of desolate terrain.

**Descriptive Noun Phrases:** Desolate sea bottoms, winding Martian canals, moonlit canal banks, vast aquatic basins, shadowy waterway routes.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: jeddak_vaults_and_quarters

[[SECTION markdown]]

# Jeddak's Vaults and Quarters

**Role:** Secondary setting / High-security location.

**Architecture or Geography:** The central seat of power for Tal Hajus, featuring elevated quarters and subterranean vaults located beneath the main residence.

**Lighting and Atmosphere Cues:** Dimly lit, claustrophobic, and highly controlled; heavy shadows in the vaults; sense of confinement and imminent threat.

**Scale Cues and Recurring Environmental Anchors:** Subterranean chambers; fortified residential structures; central seat of authority.

**Descriptive Noun Phrases:** Fortified Jeddak quarters, subterranean stone vaults, dark ritualistic chambers, high-security Thark stronghold.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
