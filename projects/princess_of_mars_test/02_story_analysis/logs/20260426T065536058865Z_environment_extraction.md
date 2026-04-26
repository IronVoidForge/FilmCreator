# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:55:36.059861+00:00
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
The narrator infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the Thark Jeddak, Tal Hajus. After witnessing Tal Hajus's cruel intentions and his plan to torture the Princess, the narrator intervenes, knocking the Jeddak unconscious with a single blow. The narrator, Dejah Thoris, and Sola escape the city on thoats, heading northeast across a mossy waste toward Helium.

The journey becomes perilous as the party runs out of food and water, eventually becoming lost. During their trek, they are joined by the narrator's faithful hound, Woola. After one of their thoats collapses from exhaustion, the group is spotted by a Thark chieftain scanning the area with a fieldglass. The narrator uses his Martian rifle to kill the charging chieftain and then forces Dejah Thoris and Sola to flee toward the hills to ensure their safety. As the narrator stays behind to provide cover fire with his rifle, he is eventually overwhelmed by a massive force of Thark warriors. The chapter ends with the narrator being beaten into unconsciousness after attempting a desperate defense.

**Characters:**
* **The Narrator:** A resourceful and heroic figure who rescues Dejah Thoris and sacrifices his own safety to ensure her escape.
* **Dejah Thoris:** The Princess of Helium; she displays immense dignity and courage even when facing the Thark Jeddak.
* **Sola:** A companion to Dejah Thoris who assists in the escape.
* **Tal Hajus:** The cruel and beastly Jeddak of the Tharks, characterized by his hatred for the red men of Helium.
* **Tars Tarkas:** A Thark warrior who observes the scene with deep loathing for Tal Hajus, though he does not intervene.
* **Woola:** The narrator's loyal Martian hound who tracks them through the waste.

**Settings:**
* **The City of Thark:** Specifically the brilliantly lighted apartments and the immense circular hall of the Jeddak.
* **The Mossy Waste:** A vast, trackless, and dangerous terrain between Thark and Helium.
* **The Low Mountains/Hills:** The destination the party seeks for shelter and navigation.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_city_interior](#thark_city_interior)
- [mossy_waste](#mossy_waste)
- [low_mountains_hills](#low_mountains_hills)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_interior

[[SECTION markdown]]

# Thark City Interior

**Role:** Primary (Conflict/Plot Hub)

**Architecture/Geography:** Immense circular halls, vaulted ceilings, and brilliantly lighted apartments designed for the Thark Jeddak. The scale is massive and imposing.

**Lighting/Atmosphere:** Brilliantly lit, high-contrast lighting within the apartments; grand, cavernous, and intimidating atmosphere in the central halls.

**Scale/Anchors:** Immense circular hall, large-scale architectural features of the Jeddak's palace.

**Prompt Phrases:** vast circular Thark hall, brilliantly lighted Martian apartments, cavernous stone architecture, imposing Jeddak palace interior.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_waste

[[SECTION markdown]]

# Mossy Waste

**Role:** Transit (Perilous Journey)

**Architecture/Geography:** A vast, trackless expanse of terrain characterized by thick moss coverage. It is a difficult landscape to navigate, lacking landmarks.

**Lighting/Atmosphere:** Open, exposed, and desolate; an atmosphere of exhaustion and vulnerability under the Martian sky.

**Scale/Anchors:** Vast horizon, endless mossy plains, lack of visible landmarks.

**Prompt Phrases:** trackless mossy waste, vast Martian plains, thick green moss coverage, desolate open terrain, endless mossy expanse.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: low_mountains_hills

[[SECTION markdown]]

# Low Mountains/Hills

**Role:** Secondary (Shelter/Tactical)

**Architecture/Geography:** Rugged, hilly terrain providing natural cover and elevation changes.

**Lighting/Atmosphere:** Shadowed crevices, uneven lighting due to topography, sense of refuge and concealment.

**Scale/Anchors:** Rolling hills, rocky outcrops, elevated vantage points.

**Prompt Phrases:** rugged low mountains, Martian hills, rocky outcrops for cover, shadowed hill terrain, undulating martian landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
