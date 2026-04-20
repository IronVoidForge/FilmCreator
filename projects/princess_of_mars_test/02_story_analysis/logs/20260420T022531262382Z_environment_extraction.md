# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:25:31.262382+00:00
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

Chapter id: CH011

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

# Chapter Summary: CHAPTER XI

## Visual Continuity Facts
- **New Quarters Location:** Building near the audience chamber; second floor overlooking the plaza.
- **Room Architecture:** Ancient beds of highly wrought metal swinging from enormous gold chains depending from marble ceilings. Elaborate wall decoration portraying human figures (fair-haired Martians in robes).
- **Character Positions:** John Carter stands protectively over Dejah Thoris; Sola acts as guide/protector; Sarkoja descends outside the quarters eavesdropping.
- **Artifacts:** Accouterments carried by John Carter (metal weapon); bedding and food utensils brought by Sola.

## Broad Story Summary
- **Arrival & Threat:** John Carter arrives with Dejah Thoris and Sola. Sarkoja attempts to assume custody of Dejah Thoris; John waves her away and threatens her demise for harming Dejah. The threat fails on Mars (men do not kill women).
- **Hierarchy Discussion:** John explains his rank as 11th chieftain to Sola. Discusses the requirement to kill Lorquas Ptomel for first place (combat or self-defense).
- **Origin Conversation:** Dejah Thoris questions John's origin, noting he speaks her language but claims recent learning. She asks if he is from Valley Dor (where a different language is spoken). He denies it, stating he is from Earth (Virginia).
- **Earth Knowledge:** Dejah expresses curiosity about Earth customs and geography. She explains Martian viewing technology allows them to see Earth events on screens.
- **Room Inspection:** John and Dejah examine the new quarters' architecture and frescoes. Dejah is captivated by the art of extinct fair-haired Martians; Sola does not notice them.
- **History Lesson:** Dejah Thoris explains Martian race mixing (Red, Dark, Yellow) due to alliance against Green Men and drying seas. Discusses lost civilization of ancient Barsoomians and the city's history as Korad.
- **Sola's Return:** Sola returns with bedding and supplies. Sarkoja is seen descending outside; they suspect eavesdropping but dismiss it for now.
- **End Scene:** John receives a summons from Lorquas Ptomel to appear in the audience chamber immediately. He bids Dejah Thoris and Sola farewell and commands Woola to remain on guard.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index

## New Quarters
- **Role:** Primary Setting
- **Location:** Second floor, building near audience chamber
- **Key Features:** Marble ceilings, gold chains, metal beds, wall frescoes
- **Atmosphere:** Ancient, ornate, intimate

## Audience Chamber
- **Role:** Secondary/Transit Setting
- **Location:** Ground level, main ceremonial space
- **Key Features:** Audience chamber architecture, formal setting
- **Atmosphere:** Ceremonial, authoritative

## Outside Plaza Area
- **Role:** Transit Setting
- **Location:** Building exterior, plaza vicinity
- **Key Features:** Eaves, descent path, eavesdropping zone
- **Atmosphere:** Observational, peripheral

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: new_quarters

[[SECTION markdown]]
# New Quarters

## Environment Role
Primary setting for chapter scene; intimate quarters where John Carter and Dejah Thoris receive accommodations.

## Architecture and Geography
Ancient beds of highly wrought metal swinging from enormous gold chains depending from marble ceilings. Elaborate wall decoration portraying human figures (fair-haired Martians in robes). Second floor location within building near audience chamber overlooking plaza.

## Lighting and Atmosphere Cues
Warm ambient light filtering through unseen sources; ornate surfaces catching reflections on metal and marble. Ancient, lived-in atmosphere with ceremonial grandeur mixed with domestic function.

## Scale Cues and Environmental Anchors
Enormous gold chains indicate monumental scale; marble ceilings suggest vast interior space; metal beds provide intimate human-scale anchors within grand architecture.

## Descriptive Noun Phrases
- Second floor quarters
- Marble ceiling chambers
- Gold chain suspension
- Wrought metal beds
- Fair-haired Martian frescoes
- Elaborate wall decoration
- Audience chamber vicinity
- Plaza overlooking location
- Ancient accommodation space
- Ornate interior quarters

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber

[[SECTION markdown]]
# Audience Chamber

## Environment Role
Secondary/transit setting; ceremonial space where John Carter receives summons to appear immediately.

## Architecture and Geography
Formal audience chamber architecture on ground level; main ceremonial space of the building complex.

## Lighting and Atmosphere Cues
Ceremonial lighting appropriate for formal proceedings; authoritative atmosphere befitting high-ranking chieftain's audience space.

## Scale Cues and Environmental Anchors
Large ceremonial space indicating building prominence; formal seating or standing areas for audience members; entrance/exit points connecting to corridors.

## Descriptive Noun Phrases
- Audience chamber interior
- Ceremonial ground level
- Formal proceedings space
- High-ranking chieftain's quarters
- Summons reception area
- Building main ceremonial hall
- Ground floor audience space
- Official meeting location
- Ceremonial architecture
- Authority space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: outside_plaza_area

[[SECTION markdown]]
# Outside Plaza Area

## Environment Role
Transit setting; exterior observation zone where Sarkoja descends and eavesdrops on quarters scene.

## Architecture and Geography
Building exterior with eaves and descent paths; plaza vicinity area adjacent to quarters building.

## Lighting and Atmosphere Cues
Natural outdoor lighting; peripheral observational atmosphere; eavesdropping zone suggesting hidden vantage points.

## Scale Cues and Environmental Anchors
Eaves indicate building height; descent path suggests vertical access; plaza provides open ground-level anchor for observation activities.

## Descriptive Noun Phrases
- Building exterior eaves
- Plaza vicinity area
- Eavesdropping observation zone
- Exterior descent path
- Building outer perimeter
- Plaza adjacent location
- Outdoor observation point
- Hidden vantage area
- Building exterior architecture
- Peripheral plaza space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
