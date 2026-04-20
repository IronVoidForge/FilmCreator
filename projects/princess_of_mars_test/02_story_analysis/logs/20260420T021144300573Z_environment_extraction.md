# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:11:44.300573+00:00
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

# Visual Continuity Facts
*   **Cityscape:** White marble city with ruined roadway entrance; broad steps leading to table land; plaza surrounded by buildings.
*   **Audience Chamber:** Low building, wide entrance (100 feet), canopy over hall; chamber dotted with carved wooden desks and chairs; rostrum platform.
*   **Martian Appearance:** 10-12 feet tall; naked except ornaments; females have larger tusks and nails on fingers/toes; light olive-green skin (Sola).
*   **Props & Furnishings:** Gleaming white marble inlaid with gold/stones; metal ornaments, feathers, leather trappings; human-sized desks/chairs (too small for Martians); ten-legged creature (frog-headed pony) waddles into room.

# Story Summary Beats
1.  **Arrival at City:** Carter and Tars Tarkas enter the city via ruined roadway; traverse narrow gorge to open valley; approach foot of mountains.
2.  **Audience Chamber Introduction:** ~50 Martians gathered around rostrum; Tars Tarkas (vice-chieftain) explains Carter's capture; formal greeting exchanged between leaders.
3.  **"Sak" Demonstration:** Chieftain requests performance; Carter jumps "sak" successfully, clearing 150 feet; wins approbation from crowd.
4.  **Hunger Negotiation:** Carter demands food/water instead of more jumping; Sola instructed to take him away; they cross plaza toward large building.
5.  **Accommodation:** Sola leads Carter to spacious chamber decorated with murals/mosaics; introduces ten-legged creature (frog-headed pony).

# Scene Decomposition Notes
*   **Scene 1: City Entry.** Focus on transition from mountain gorge to city plaza; visual of white marble architecture.
*   **Scene 2: Audience Chamber.** Focus on size mismatch between Martians and furniture; formal greeting ritual; Tars Tarkas' explanation.
*   **Scene 3: Sak Performance.** Focus on Carter's physical exertion; crowd reaction (laughter/applause); successful jump mechanics.
*   **Scene 4: Negotiation.** Focus on Carter's hunger cues; Sola's intervention; transition from plaza to accommodation building.
*   **Scene 5: Accommodation.** Focus on chamber interior details; introduction of ten-legged creature; establishing rest period.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Chapter 4

## Primary Environments

| Asset ID | Name | Role | Description |
|----------|------|------|-------------|
| city_plaza_entrance | City Plaza Entrance | Transit Setting | White marble city with ruined roadway entrance; broad steps leading to table land; plaza surrounded by buildings |
| audience_chamber | Audience Chamber | Primary Setting | Low building, wide 100-foot entrance, canopy over hall; chamber dotted with carved wooden desks and chairs; rostrum platform |
| accommodation_chamber | Accommodation Chamber | Primary Setting | Spacious chamber decorated with murals/mosaics; ten-legged creature (frog-headed pony) waddles into room |

## Environment Families Summary

- **Cityscape Family**: White marble architecture, ruined roadway, plaza geography
- **Interior Chamber Family**: Low buildings, wide entrances, canopy structures, furniture arrangements
- **Accommodation Interior**: Murals, mosaics, decorative elements, creature introductions

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_plaza_entrance

[[SECTION markdown]]
# City Plaza Entrance

## Environment Role
Transit Setting - Primary entry point into Martian territory

## Architecture and Geography
- White marble city architecture with ruined roadway entrance
- Broad steps leading to table land
- Plaza surrounded by buildings on multiple sides
- Mountain gorge transition zone at approach foot

## Lighting and Atmosphere Cues
- Natural daylight filtering through mountain gorge
- Bright white marble reflecting ambient light
- Ruined roadway suggesting ancient civilization decay
- Open valley atmosphere with clear visibility

## Scale Cues and Environmental Anchors
- 10-12 foot tall Martian figures (Sola) as reference scale
- Human-sized furniture appears too small for Martians
- Plaza dimensions accommodate large gatherings (~50 Martians visible)
- Mountain gorge provides natural framing boundary

## Descriptive Noun Phrases
- "White marble cityscape"
- "Ruined roadway entrance"
- "Broad steps to table land"
- "Surrounded plaza architecture"
- "Mountain gorge transition zone"
- "Ancient civilization decay markers"
- "Open valley atmosphere"

## Render-Facing Prompt Elements
- Primary material: white marble with gold inlay
- Secondary material: stone roadway ruins
- Atmospheric element: clear mountain valley lighting
- Scale reference: 10-12 foot humanoid figures
- Anchor points: plaza center, ruined entrance archway

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber

[[SECTION markdown]]
# Audience Chamber

## Environment Role
Primary Setting - Formal gathering space for Martian leadership

## Architecture and Geography
- Low building structure with wide 100-foot entrance
- Canopy covering the hall interior
- Chamber dotted with carved wooden desks and chairs
- Rostrum platform at front of chamber
- Wide entrance facilitating crowd movement

## Lighting and Atmosphere Cues
- Interior lighting from canopy overhead
- Formal gathering atmosphere with ~50 Martians present
- Carved wood elements catching ambient light
- Platform rostrum creating focal point illumination

## Scale Cues and Environmental Anchors
- Human-sized desks/chairs too small for 10-12 foot Martians
- Rostrum platform as primary anchor point
- Canopy structure defining chamber boundaries
- Carved wooden furniture as recurring visual motif

## Descriptive Noun Phrases
- "Low building entrance"
- "Wide 100-foot doorway"
- "Canopy over hall interior"
- "Carved wooden desks and chairs"
- "Rostrum platform focal point"
- "Formal gathering space"
- "Ancient craftsmanship markers"

## Render-Facing Prompt Elements
- Primary material: white marble with gold/stones inlay
- Secondary material: carved wood furniture (desks, chairs)
- Atmospheric element: formal gathering lighting
- Scale reference: 10-12 foot humanoid figures vs human-sized furniture
- Anchor points: rostrum platform, canopy structure, wide entrance archway

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: accommodation_chamber

[[SECTION markdown]]
# Accommodation Chamber

## Environment Role
Primary Setting - Rest and recovery space for Carter

## Architecture and Geography
- Spacious chamber interior with decorative elements
- Murals and mosaics on walls
- Ten-legged creature (frog-headed pony) introduction space
- Large building accommodation structure

## Lighting and Atmosphere Cues
- Interior lighting highlighting murals and mosaics
- Restful atmosphere after physical exertion
- Decorative wall elements catching ambient light
- Spacious interior allowing creature movement

## Scale Cues and Environmental Anchors
- Chamber dimensions accommodate large creature (ten-legged pony)
- Murals and mosaics as primary visual anchors
- Spacious interior defining chamber boundaries
- Creature introduction as recurring environmental element

## Descriptive Noun Phrases
- "Spacious chamber interior"
- "Decorative murals on walls"
- "Intricate mosaic patterns"
- "Ten-legged creature space"
- "Frog-headed pony anchor"
- "Restful accommodation area"
- "Large building interior"

## Render-Facing Prompt Elements
- Primary material: white marble with gold/stones inlay
- Secondary material: murals and mosaics on walls
- Atmospheric element: restful interior lighting
- Scale reference: ten-legged creature (frog-headed pony) as anchor
- Anchor points: mural sections, mosaic patterns, creature introduction zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
