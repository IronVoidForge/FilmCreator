# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:54:12.475582+00:00
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

Chapter id: CH004

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

## Scene Breakdown (Story Summary)

### Scene 1: Journey to the City
*   **Action:** Narrator and guard travel ten miles; ground rises rapidly.
*   **Location:** Edge of dead sea, foot of mountains, narrow gorge, open valley, table land.
*   **Visual:** Enormous city beheld at far extremity of valley. Ruined roadway leads to edge of table land with broad steps.

### Scene 2: Observation of Martians in the City
*   **Action:** Narrator observes Martians camped on plaza and surrounding buildings (approx. 900-1000 creatures).
*   **Visual Details:** Naked except ornaments; women have larger tusks curving to ears, lighter bodies, rudimentary nails. Children look alike, light in color.
*   **Societal Info:** Life expectancy details (maturity ~40 years, voluntary pilgrimage at 1000 years). Death causes: sickness (rare), voluntary pilgrimage (~20%), violent death (duels, hunting, aviation, war).

### Scene 3: Arrival at the Chieftain's Building
*   **Action:** Party surrounded by hundreds of creatures; leader stilled clamor. Proceed to magnificent edifice (low, enormous area, white marble/gold/stones).
*   **Visual:** Main entrance 100 feet wide with huge canopy. No stairway, gentle incline to first floor. Chamber encircled by galleries, dotted with wooden desks/chairs sized for humans.
*   **Ceremony:** Martians assembled around rostrum (40-50 males). Chieftain squats on platform (enormous warrior loaded with ornaments/feathers/leather). Greeting ritual: Names exchanged (Tars Tarkas and Chieftain titles).

### Scene 4: Physical Limitations & Martial Interaction
*   **Action:** Narrator lowered to ground. Captor explains expedition/capture. Narrator replies in English to show lack of understanding; smiles slightly.
*   **Visual:** Martians examine narrator's muscles/skin texture. Furniture mismatch (Martians too large for desks/chairs).
*   **Conflict:** Narrator skips/flits like grasshopper, bruises self. Punches a towering fellow who laughed heartily; opponent falls like felled ox. Martians break into wild peals of laughter/applause.

### Scene 5: "Sak" Exhibition & Demands
*   **Action:** Chieftain orders narrator to perform "sak". Narrator jumps 150 feet successfully, lands squarely. Returns by easy jumps.
*   **Conflict:** Narrator hungry/thirsty; ignores commands, motions mouth/stomach. Tars Tarkas and chief exchange words.
*   **Action:** Narration accompanied young female (Sola) to sleeping quarters.

### Scene 6: Sleeping Quarters & New Creature
*   **Location:** Spacious chamber in building fronting plaza.
*   **Visual:** Well lighted by large windows; decorated with mural paintings and mosaics (touch of antiquity). Silks/furs on floor.
*   **Action:** Sola seated, makes hissing sound. New Martian wonder waddles in on ten short legs (size of Shetland pony, frog-like head, three rows of long sharp tusks).

## Visual Details (Continuity for Scene Decomposition)

### Architecture & Materials
*   **Primary Material:** Gleaming white marble inlaid with gold and brilliant stones.
*   **Structure:** Low buildings covering enormous areas; main entrance 100 feet wide with huge canopy above entrance hall.
*   **Interior:** Chamber encircled by galleries, dotted with highly carved wooden desks and chairs sized for humans (not Martians).
*   **Decoration:** Mural paintings and mosaics on sleeping quarters; silks and furs littering floors.

### Martian Appearance & Features
*   **General:** Naked except for ornaments; bodies smaller and lighter in color than males.
*   **Women:** Tusks much larger in proportion to height, curving nearly to high-set ears; rudiments of nails on fingers/toes.
*   **Height:** Adult females range from ten to twelve feet; young female (Sola) about eight feet tall.
*   **Children:** Light in color, even lighter than women; all look precisely alike.

### Creature Features
*   **Legs:** Ten short legs (waddling like an obedient puppy).
*   **Head:** Slight resemblance to frog head, except jaws equipped with three rows of long, sharp tusks.
*   **Size:** About the size of a Shetland pony.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Chapter 4

| Asset ID | Environment Name | Role | Primary Feature |
|----------|------------------|------|-----------------|
| edge_dead_sea_mountain_foot | Edge of Dead Sea / Mountain Foot | Transit Setting | Rising ground, valley approach |
| narrow_gorge_open_valley | Narrow Gorge / Open Valley | Transit Setting | Terrain transition, city view |
| table_land_ruined_roadway | Table Land with Ruined Roadway | Primary Setting | Broad steps, marble/gold stones |
| martian_city_plaza | Martian City Plaza | Primary Setting | 900-1000 creatures, open gathering space |
| chieftain_building_magnificent_edifice | Chieftain's Building / Magnificent Edifice | Primary Setting | White marble, gold inlay, enormous area |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: edge_dead_sea_mountain_foot

[[SECTION markdown]]
**Environment Role:** Transit Setting  
**Architecture/Geography:** Edge of dead sea terrain transitioning to mountain foot; ground rises rapidly over ten-mile journey  
**Lighting/Atmosphere:** Natural daylight, open valley approach, atmospheric perspective toward distant city  
**Scale Cues:** Ten-mile travel distance, enormous city beheld at far extremity of valley  
**Descriptive Noun Phrases:** Rising dead sea edge, mountain foot approach, valley terrain transition, distant city silhouette, ruined roadway leading to table land

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: narrow_gorge_open_valley

[[SECTION markdown]]
**Environment Role:** Transit Setting  
**Architecture/Geography:** Narrow gorge opening into expansive valley; terrain features during approach to city  
**Lighting/Atmosphere:** Natural daylight, atmospheric depth toward distant city view, open sky above gorge  
**Scale Cues:** Valley width accommodating enormous city at extremity, gorge narrowing perspective  
**Descriptive Noun Phrases:** Gorge-to-valley transition, valley floor approach, distant city silhouette, open sky passage, terrain elevation change

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: table_land_ruined_roadway

[[SECTION markdown]]
**Environment Role:** Primary Setting  
**Architecture/Geography:** Table land with ruined roadway leading to edge; broad steps structure, gleaming white marble inlaid with gold and brilliant stones  
**Lighting/Atmosphere:** Natural daylight, open plaza illumination, stone surface reflections, atmospheric clarity toward city  
**Scale Cues:** Main entrance 100 feet wide with huge canopy, enormous area covered by low buildings, no stairway with gentle incline to first floor  
**Descriptive Noun Phrases:** Table land edge, ruined roadway approach, broad marble steps, white marble and gold inlay, enormous building area, main entrance canopy

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_city_plaza

[[SECTION markdown]]
**Environment Role:** Primary Setting  
**Architecture/Geography:** Open plaza surrounded by buildings; gathering space for 900-1000 Martians, open-air assembly area  
**Lighting/Atmosphere:** Natural daylight, open sky illumination, atmospheric openness of city plaza, natural light on marble surfaces  
**Scale Cues:** Plaza accommodating 900-1000 creatures, buildings surrounding open space, human-sized furniture within chamber encircled by galleries  
**Descriptive Noun Phrases:** City plaza gathering, open-air assembly space, surrounded building perimeter, creature camp area, open sky plaza illumination

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chieftain_building_magnificent_edifice

[[SECTION markdown]]
**Environment Role:** Primary Setting  
**Architecture/Geography:** Magnificent edifice with low profile covering enormous area; white marble and gold stones, main entrance 100 feet wide with huge canopy above entrance hall  
**Lighting/Atmosphere:** Well lighted by large windows, mural paintings and mosaics decoration, silks and furs on floor creating warm interior atmosphere  
**Scale Cues:** Chamber encircled by galleries, furniture sized for humans (not Martians), ten short legs creature size reference, sleeping quarters spacious chamber fronting plaza  
**Descriptive Noun Phrases:** Magnificent white marble edifice, gold inlay stones, enormous low building area, main entrance canopy, gallery-encircled chamber, human-sized carved wooden desks and chairs, mural painting decorations, mosaic floor art, silk and fur interior furnishings

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
