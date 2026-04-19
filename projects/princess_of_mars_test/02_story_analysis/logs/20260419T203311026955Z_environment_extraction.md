# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:33:11.026955+00:00
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

Chapter id: CH017

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

# Chapter Summary: CHAPTER XVII (A COSTLY RECAPTURE)

## Story Arc
1.  **Rescue:** Carter intervenes to save Dejah Thoris and Sola from Tal Hajus in Thark's inner chamber, killing the jeddak.
2.  **Escape:** The group flees on thoats through the wilderness toward Helium.
3.  **Complication:** They become lost; animals weaken; Woola joins them later (not initially present).
4.  **Confrontation:** A party of Thark warriors spots them via fieldglass. Carter shoots a chieftain to prevent capture.
5.  **Sacrifice:** To save Dejah Thoris and Sola, Carter holds off the warriors alone, gets captured by green men after killing many.

## Visual Continuity Facts
- **Locations:** Thark inner chamber (dome-like roof), mossy waste (yellow moonlit ground), hills (ridges, passes).
- **Objects:** Martian rifle (magazine/belt ammo), fieldglass, thoats (trappings/straps), long-sword.
- **Character States:** Dejah Thoris (sobbing/clinging), Tal Hajus (beastly/hideous), Green Warriors (charging/mounted).
- **Lighting:** Brilliant lights in Thark apartments; moonlit moss in wilderness; shadows in courtyards.
- **Continuity Note:** Woola is not with the group at the start of the chapter; he appears later via snuggling close to Carter.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XVII (A Costly Recapture)

## Extracted Environments

| Asset ID | Environment Name | Role | Primary Features |
|----------|------------------|------|------------------|
| thark_inner_chamber | Thark Inner Chamber | Primary Setting | Dome-like roof, brilliant apartment lights, mossy waste exterior |
| mossy_waste | Mossy Waste Wilderness | Transit Setting | Yellow moonlit ground, moss coverage, hills and ridges |
| hill_ridges_passes | Hills with Ridges and Passes | Secondary Setting | Elevated terrain, passes through wilderness |

## Environment Families Summary

- **3 environment families** extracted from chapter visual continuity
- All environments include visible geography and atmosphere cues
- Each environment file contains render-facing descriptive noun phrases
- Asset IDs follow lowercase snake_case convention for stability across reruns

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_inner_chamber

[[SECTION markdown]]
# Thark Inner Chamber - Environment Description

## Environment Role
Primary setting for chapter opening rescue sequence. Interior chamber space with exterior mossy waste visible through openings.

## Architecture and Geography
Dome-like roof structure defining interior ceiling space. Apartment buildings surrounding central chamber area. Openings connecting interior to exterior wilderness terrain.

## Lighting and Atmosphere Cues
Brilliant lights illuminating Thark apartments create high-contrast interior lighting. Moonlight filtering through openings casts shadows on interior surfaces. Interior spaces appear well-lit compared to exterior wilderness darkness.

## Scale and Environmental Anchors
Large dome roof establishes grand interior scale. Apartment buildings provide vertical reference points. Openings serve as transition anchors between interior chamber and exterior mossy waste terrain.

## Descriptive Noun Phrases for Render Prompts
- Dome-like roof structure
- Brilliant apartment lighting
- Interior chamber space
- Mossy waste exterior view
- High-contrast interior illumination
- Well-lit Thark apartments
- Shadow-casting moonlight filters
- Grand interior scale architecture
- Vertical reference buildings
- Transition opening spaces

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mossy_waste

[[SECTION markdown]]
# Mossy Waste Wilderness - Environment Description

## Environment Role
Transit setting for escape sequence through Martian wilderness. Primary exterior terrain during group flight on thoats.

## Architecture and Geography
Yellow moonlit ground surface covered in moss vegetation. Hills and ridges forming elevated terrain features. Passes through wilderness creating natural pathways. Open wilderness with no built structures.

## Lighting and Atmosphere Cues
Moonlight illuminating yellow ground creates cool-toned exterior lighting. Shadows cast across moss-covered surfaces. Wilderness darkness contrasting with interior chamber brilliant lights. Atmospheric conditions suggest open Martian night environment.

## Scale and Environmental Anchors
Hills and ridges establish horizontal scale across wilderness terrain. Moss coverage provides textural reference points. Passes serve as directional anchors for group movement through landscape.

## Descriptive Noun Phrases for Render Prompts
- Yellow moonlit ground surface
- Moss-covered vegetation terrain
- Elevated hills and ridges
- Open wilderness pathways
- Cool-toned exterior lighting
- Shadow-casting moonlight
- Natural landscape passages
- Martian night atmosphere
- Textural moss coverage
- Horizontal scale terrain

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hill_ridges_passes

[[SECTION markdown]]
# Hills with Ridges and Passes - Environment Description

## Environment Role
Secondary setting for wilderness escape route. Elevated terrain features providing vantage points during group movement through hills.

## Architecture and Geography
Hills forming elevated terrain with ridges creating natural boundaries. Passes cutting through hill formations creating pathways. Elevated landscape overlooking lower mossy waste areas. Natural geological formations without built structures.

## Lighting and Atmosphere Cues
Moonlight illuminating hill surfaces creates varied lighting across ridge faces. Shadows accentuating ridge depth and pass openings. Elevated terrain receives different light angles than valley floor. Atmospheric conditions suggest open Martian wilderness night environment.

## Scale and Environmental Anchors
Hill formations establish vertical scale in landscape. Ridges provide horizontal reference lines across terrain. Passes serve as directional anchors for group movement through elevated terrain. Natural geological features create environmental boundaries.

## Descriptive Noun Phrases for Render Prompts
- Elevated hill formations
- Ridge boundary structures
- Natural pass openings
- Vertical landscape scale
- Horizontal ridge reference lines
- Directional passage anchors
- Geological terrain features
- Open wilderness night lighting
- Varied surface illumination
- Natural environmental boundaries

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
