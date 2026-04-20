# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:31:34.413636+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH020

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter Summary: Atmosphere Factory & Escape to Zodanga

## Visual Continuity Facts
*   **Carter's Appearance:** Initially described as a Red Man, he is later shown anointed with reddish oil and having his hair cut to match the prevailing fashion of Red Martians. His metal and ornaments are renewed in the style of a Zodangan gentleman.
*   **Woola's State:** Woola is depicted eating the carcass of the beast that attacked Carter, appearing half-starved and a shadow of his former self.
*   **Atmosphere Factory:** A massive building with walls 150 feet thick, featuring radium pumps and telepathic door locks. The old man wears a gold collar with a diamond-studded ornament containing a strange stone that scintillates nine rays.
*   **Transport:** Carter is given a domestic bull-thoat (size of a horse, gentle) for saddle purposes.

## Story Summary
Carter meets Woola at the Atmosphere Factory after escaping the Warhoons and surviving attacks by wild beasts. The old man explains the factory's function (producing atmosphere via the ninth ray stored in reservoirs) and warns Carter against Helium due to ongoing war. Carter realizes the old man intends to kill him but uses telepathic thought waves to unlock the massive doors and escape with Woola. They reach Zodanga outskirts, where Red Martians take them in. Carter is prepared (colored, hair cut) and given money and a bull-thoat, advised to seek military service in Zodanga to prove trustworthiness and win friends among the nobles. The old man's suspicion of Carter remains, but Carter avoids killing him due to his concern for Dejah Thoris and the planet's atmosphere.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Atmosphere Factory & Escape to Zodanga

## Primary Environments

### atmosphere_factory
- **Role:** Secondary/Transit Setting
- **Architecture:** Massive industrial building with walls 150 feet thick, radium pumps, telepathic door locks
- **Lighting/Atmosphere:** Radium-lit interior, strange stone scintillating nine rays, gold collar with diamond-studded ornament
- **Scale:** Industrial facility within Red Martian territory
- **Anchors:** Old man's residence, atmospheric reservoirs

### zodanga_outskirts
- **Role:** Arrival/Transit Setting
- **Architecture:** Red Martian territorial outskirts, military service location
- **Lighting/Atmosphere:** Red Martian environment, planetary outskirts lighting
- **Scale:** Planetary boundary zone
- **Anchors:** Bull-thoat saddle station, noble reception area

### red_martian_territory
- **Role:** Primary Setting
- **Architecture:** Zodangan gentleman territory, military service locations
- **Lighting/Atmosphere:** Red Martian atmospheric conditions, planetary lighting
- **Scale:** Full planetary environment
- **Anchors:** Bull-thoat domestic bull-thoat, noble reception areas

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: atmosphere_factory

[[SECTION markdown]]
# Atmosphere Factory

## Environment Role
Secondary/Transit Setting - Industrial facility within Red Martian territory where Carter meets Woola and learns about atmospheric production.

## Architecture & Geography
Massive building with walls 150 feet thick, featuring radium pumps throughout interior spaces. Telepathic door locks control access to atmospheric reservoirs. The facility houses the ninth ray storage systems that produce atmosphere for the planet.

## Lighting & Atmosphere Cues
Radium-lit interior creates industrial glow throughout factory floors. Strange stone scintillates nine rays in old man's gold collar with diamond-studded ornament. Telepathic thought waves unlock massive doors when activated. Atmospheric reservoirs visible through facility windows.

## Scale Cues
Industrial-scale facility spanning multiple levels. Walls 150 feet thick indicate massive construction. Bull-thoat saddle station sized for horse-equivalent domestic bull-thoat. Old man's residence integrated into factory complex.

## Recurring Environmental Anchors
- Old man's gold collar with diamond-studded ornament containing strange stone
- Radium pump systems throughout facility
- Telepathic door lock mechanisms
- Atmospheric reservoir storage areas
- Bull-thoat saddle station entrance

## Descriptive Noun Phrases for Render-Facing Prompts
"massive industrial building 150 feet thick walls", "radium-lit interior factory space", "telepathic door lock mechanism", "strange stone scintillating nine rays", "gold collar diamond-studded ornament", "atmospheric reservoir storage facility", "industrial glow radium lighting", "bull-thoat saddle station entrance"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodanga_outskirts

[[SECTION markdown]]
# Zodanga Outskirts

## Environment Role
Arrival/Transit Setting - Planetary boundary zone where Carter and Woola are taken in by Red Martians after escape from Warhoons.

## Architecture & Geography
Red Martian territorial outskirts with military service locations integrated into noble reception areas. Zodangan gentleman territory boundaries mark the transition from wild zones to civilized Red Martian lands.

## Lighting & Atmosphere Cues
Red Martian environmental lighting conditions throughout planetary outskirts. Atmospheric conditions match Red Martian territory standards. Noble reception areas feature appropriate ceremonial lighting for Zodangan gentlemen.

## Scale Cues
Planetary boundary zone spanning territorial outskirts. Military service locations sized for full planetary scale. Bull-thoat domestic bull-thoat sized for horse-equivalent saddle purposes.

## Recurring Environmental Anchors
- Bull-thoat saddle station entrance
- Noble reception area boundaries
- Military service location markers
- Red Martian territory transition zones
- Zodangan gentleman territory borders

## Descriptive Noun Phrases for Render-Facing Prompts
"Red Martian territorial outskirts", "planetary boundary zone lighting", "noble reception area ceremonial space", "military service location markers", "Zodangan gentleman territory boundaries", "bull-thoat saddle station entrance", "territorial outskirts transition zones", "ceremonial lighting noble reception"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: red_martian_territory

[[SECTION markdown]]
# Red Martian Territory

## Environment Role
Primary Setting - Full planetary environment where Carter is prepared, given money and bull-thoat, advised to seek military service in Zodanga.

## Architecture & Geography
Full Red Martian planetary territory with Zodangan gentleman territory integrated throughout. Military service locations distributed across noble reception areas. Bull-thoat domestic bull-thoat housed within territorial facilities.

## Lighting & Atmosphere Cues
Red Martian atmospheric conditions throughout full planetary environment. Planetary lighting matches Red Martian territory standards. Noble reception areas feature appropriate ceremonial lighting for Zodangan gentlemen and military service locations.

## Scale Cues
Full planetary scale environment spanning entire Red Martian territory. Military service locations sized for planetary scale operations. Bull-thoat domestic bull-thoat sized for horse-equivalent saddle purposes throughout territory.

## Recurring Environmental Anchors
- Bull-thoat domestic bull-thoat housing facilities
- Noble reception area ceremonial spaces
- Military service location distribution points
- Zodangan gentleman territory integration zones
- Planetary atmospheric storage systems

## Descriptive Noun Phrases for Render-Facing Prompts
"full Red Martian planetary environment", "Zodangan gentleman territory integration", "military service location distribution", "noble reception area ceremonial space", "bull-thoat domestic bull-thoat housing", "planetary atmospheric conditions", "ceremonial lighting Zodangan territory", "territory integration zones"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
