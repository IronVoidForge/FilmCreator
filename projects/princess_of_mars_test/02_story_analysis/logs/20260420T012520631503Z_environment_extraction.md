# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:25:20.631503+00:00
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

# Chapter Summary: CHAPTER XVII - A COSTLY RECAPTURE

## Plot Beats

### Beat 1: The Rescue in Thark City
John Carter overhears Tal Hajus's plan to torture Dejah Thoris for ten days and claim her for one hour. Upon hearing this, Carter kills Tal Hajus with a punch while protecting Dejah Thoris from the jeddak's grasp. He rescues Dejah Thoris and Sola from the unlighted third floor of the building using straps and leather trappings, lowering them to the ground below. They escape the city of Thark through the courtyard on their thoats, heading south towards Helium.

### Beat 2: The Journey Through the Waste
The party travels through the mossy waste but gets lost due to lack of waterways. Woola joins them after sleeping near Carter. They suffer from exhaustion and hunger. One of the two thoats collapses and is left behind; they continue with one beast, walking while Dejah Thoris rides.

### Beat 3: The Pursuit by Thark Warriors
While traveling towards the hills, they spot a party of mounted Thark warriors heading southwesterly. Carter shoots a chieftain using his rifle, but is immediately pursued by the remaining warriors (some thousand men). Dejah Thoris sacrifices herself to save Carter, staying behind to die with him while he fights off the green warriors alone.

### Beat 4: The Capture
Carter fights the pursuing warriors alone, firing until his rifle is empty. He is eventually struck by a projecting piece of quartz and falls. Despite drawing his long-sword, he is overwhelmed by the torrent of blows from the green warriors and goes down to oblivion, captured by them.

## Visual Continuity Facts

### Locations
- **Thark City:** Courtyard, third floor windows, inner chamber with raised platform, winding runway.
- **Mossy Waste:** Yellow moonlit moss, hills, ridges, passes, sea bottom (flat terrain).
- **Helium:** Mentioned as the destination and home of Dejah Thoris's people.

### Character States & Objects
- **John Carter:** Armed with rifle, revolvers, sword; determined but exhausted; eventually captured.
- **Dejah Thoris:** Riding thoat; injured/threatened; sacrifices herself to save Carter.
- **Sola:** Riding thoat; loyal companion; follows Carter's commands.
- **Woola:** Faithful beast; joins the party after sleeping near Carter.
- **Tal Hajus:** Dead jeddak; killed by Carter.
- **Thoats:** Two beasts initially; one collapses and is left behind due to exhaustion.
- **Weapons:** Rifle (empty), revolvers, long-sword, fieldglass.

### Environmental Details
- **Terrain:** Yellow moss, hills, ridges, passes, waterways (missing).
- **Lighting:** Moonlit nights, daylight travel.
- **Atmosphere:** Tense pursuit, exhaustion, sacrifice, danger of capture.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XVII

## Thark City (thark_city)
**Role:** Primary setting for the rescue sequence
**Key Features:** Courtyard, third floor windows, inner chamber with raised platform, winding runway
**Lighting:** Interior shadows transitioning to courtyard daylight
**Atmosphere:** Tense pursuit, danger of capture

## Mossy Waste (mossy_waste)
**Role:** Transit setting for journey south
**Key Features:** Yellow moonlit moss, hills, ridges, passes, flat terrain
**Lighting:** Moonlit nights with daylight travel periods
**Atmosphere:** Exhaustion, sacrifice, danger of pursuit

## Helium (helium)
**Role:** Destination/mentioned location
**Key Features:** Home territory of Dejah Thoris's people
**Lighting:** Not specified in chapter
**Atmosphere:** Hopeful destination after escape

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_city

[[SECTION markdown]]
# Thark City Environment

## Overview
Primary urban setting where the rescue sequence unfolds. Multi-level structure with interior chambers and exterior courtyard spaces.

## Architecture & Geography
- **Courtyard:** Open ground level space accessible from building, used for thoat escape route
- **Third Floor Windows:** Elevated access points overlooking courtyard, windows serve as rescue extraction points
- **Inner Chamber:** Interior room with raised platform, winding runway connecting levels
- **Building Structure:** Multi-story construction with leather trappings and straps for lowering occupants

## Lighting & Atmosphere
- **Interior Spaces:** Shadowed areas transitioning to daylight at courtyard level
- **Courtyard:** Natural daylight exposure during escape sequence
- **Tension:** Dark interior shadows contrast with bright exterior pursuit lighting
- **Mood:** Urgent, dangerous, high-stakes rescue atmosphere

## Scale & Anchors
- **Vertical Scale:** Three-story building height with platform elevations
- **Horizontal Scale:** Courtyard provides open ground for thoat movement
- **Recurring Elements:** Windows as extraction points, courtyard as escape route, raised platforms as interior anchors
- **Environmental Markers:** Building edges define courtyard boundaries, window frames mark third floor level

## Descriptive Noun Phrases
- "multi-story building structure"
- "courtyard ground level space"
- "third floor windows overlooking courtyard"
- "inner chamber with raised platform"
- "winding runway connecting levels"
- "leather trappings and straps for lowering"
- "thoat escape route through courtyard"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mossy_waste

[[SECTION markdown]]
# Mossy Waste Environment

## Overview
Transit wilderness setting for journey south from Thark City toward Helium. Characterized by yellow moss terrain and challenging navigation conditions.

## Architecture & Geography
- **Yellow Moonlit Moss:** Flat terrain covering ground surface, distinctive coloration
- **Hills:** Elevated landforms providing visual landmarks and elevation changes
- **Ridges:** Linear elevated features cutting through landscape
- **Passes:** Narrow pathways between hills and ridges for travel routes
- **Sea Bottom:** Flat terrain areas resembling seabed characteristics

## Lighting & Atmosphere
- **Moonlit Nights:** Yellow-tinted illumination from moonlight reflecting off moss
- **Daylight Travel:** Natural daylight periods during journey progression
- **Tension:** Pursuit lighting creates high-stakes atmosphere
- **Mood:** Exhaustion, danger, sacrifice under challenging terrain conditions

## Scale & Anchors
- **Vertical Scale:** Hills and ridges provide elevation changes across landscape
- **Horizontal Scale:** Wide open moss plains with distant hills as horizon markers
- **Recurring Elements:** Yellow moss patches, hill silhouettes, ridge lines, pass openings
- **Environmental Markers:** Hill tops define passes, ridge edges mark terrain boundaries, moss color indicates ground type

## Descriptive Noun Phrases
- "yellow moonlit moss terrain"
- "hills and ridges landscape features"
- "passes between elevated landforms"
- "flat sea bottom terrain areas"
- "moonlit night illumination"
- "daylight travel periods"
- "moss-covered ground surface"
- "distant hills as horizon markers"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: helium

[[SECTION markdown]]
# Helium Environment

## Overview
Destination location mentioned throughout chapter. Home territory of Dejah Thoris's people, representing the goal of escape journey.

## Architecture & Geography
- **Home Territory:** Settlement area belonging to Dejah Thoris's people
- **Destination Location:** End point of southward journey from Thark City
- **Cultural Setting:** Associated with Dejah Thoris's heritage and people
- **Geographic Position:** South of Thark City, beyond mossy waste terrain

## Lighting & Atmosphere
- **Not Specified:** Chapter does not provide lighting details for this location
- **Implied Hopeful:** Destination represents safety and home after escape
- **Mood:** Anticipated relief and reunion atmosphere

## Scale & Anchors
- **Scale:** Not detailed in chapter summary
- **Recurring Elements:** Mentioned as destination throughout narrative
- **Environmental Markers:** Cultural association with Dejah Thoris's people
- **Narrative Function:** Goal location driving journey progression

## Descriptive Noun Phrases
- "home territory of Dejah Thoris's people"
- "destination beyond mossy waste"
- "southward journey endpoint"
- "cultural settlement area"
- "safe haven after escape"
- "people's homeland location"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
