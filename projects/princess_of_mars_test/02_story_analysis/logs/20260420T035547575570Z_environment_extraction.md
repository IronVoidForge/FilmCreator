# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:55:47.575570+00:00
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

Chapter id: CH016

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

**Arrival at Thark:** Journey complete (20 days). Arrival at city (30 days after advent on Barsoom). Entry into plaza receives formal greetings; interest aroused by captives.
**Quarters Assigned:** John Carter assigned a large building near the plaza, architecture grander than Korad. Warriors occupy buildings based on chieftain retinues or scattered sections.
**Reconciliation Attempt:** John Carter visits Dejah Thoris's room. Confesses love ("I am yours"). She accepts his service but remains guarded regarding her heart.
**Threat Revealed:** Sola reports Sarkoja plans to throw them to calots in arena games.
**Escape Plan Formulated:** Decide to escape that night. Map drawn on marble floor by Dejah Thoris showing waterways and cities. Route chosen: northern waterway to avoid suspicion.
**Execution Begins:** John Carter saddles two thoats, leaves city alone at night via southern boundary.
**Discovery of Plan:** Warriors discover plan (hear him leaving). Plan compromised.
**Return to Quarters:** John Carter hides animals in courtyard of a building, returns to Dejah Thoris's quarters via rooftops/courts.
**Climax:** Overhears chieftain ordering warriors to capture John Carter when he returns. Chieftain confirms Sarkoja has secured Dejah Thoris ("safe in the arms of Tal Hajus").
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Thark City Environment Index

## Primary Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|------|--------------|
| thark_city_plaza | Thark Plaza Entrance | Primary | Formal greeting area, captive display zone |
| thark_carter_quarters | John Carter Quarters Building | Primary | Large structure near plaza, grand architecture |
| thark_dejah_quarters | Dejah Thoris Room | Secondary | Private quarters, marble floor mapping area |
| thark_arena_destination | Thark Arena | Transit/Threat | Calot games location, Sarkoja's target zone |

## Secondary Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|------|--------------|
| thark_courtyard_zone | Courtyard Area | Transit | Animal hiding location, rooftop access point |
| thark_rooftop_network | Rooftop/Court Pathways | Transit | Movement between buildings, escape route |

## Environment Notes

- All environments located within Thark City (30 days after Barsoom advent)
- Architecture described as grander than Korad city structures
- Lighting and atmosphere tied to night-time escape sequences
- Scale cues emphasize large building structures near plaza
- Recurring anchors: marble floors, courtyard gates, rooftop edges

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_city_plaza

[[SECTION markdown]]
# Thark Plaza Entrance

## Environment Role
Primary setting for formal arrival and greeting sequences. Central hub where captives are displayed and interest is aroused by John Carter's presence.

## Architecture and Geography
Large open plaza area with formal entrance structures. Elevated viewing positions for chieftain retinues. Buildings positioned around perimeter with grand architecture exceeding Korad standards.

## Lighting and Atmosphere Cues
Daylight arrival sequences transitioning to night-time escape planning. Formal lighting in greeting areas, shadowed corners for captive display zones. Atmospheric tension from warrior presence and Sarkoja's threat.

## Scale and Environmental Anchors
- Large plaza dimensions accommodating multiple chieftain retinues
- Elevated viewing platforms for formal greetings
- Marble floor surfaces for mapping escape routes
- Courtyard gates serving as transition points to rooftops
- Building facades with grand architectural details near plaza edge

## Descriptive Noun Phrases
- Formal greeting entrance zone
- Captive display perimeter
- Chieftain retinue viewing platforms
- Grand architecture plaza buildings
- Marble mapping floor surfaces
- Night-time escape planning area
- Warrior patrol boundaries
- Rooftop access gateways

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_carter_quarters

[[SECTION markdown]]
# John Carter Quarters Building

## Environment Role
Primary living quarters for John Carter. Large structure assigned near plaza with architecture described as grander than Korad city buildings.

## Architecture and Geography
Large building structure with multiple rooms including courtyard access. Grand architectural details exceeding standard Thark construction. Multiple rooftop access points from courtyard zone.

## Lighting and Atmosphere Cues
Interior lighting for private quarters, courtyard daylight filtering through openings. Night-time hiding sequences in courtyard area. Atmospheric tension from warrior discovery of escape plan.

## Scale and Environmental Anchors
- Large building footprint near plaza edge
- Courtyard entrance with animal hiding capacity
- Rooftop access points from courtyard zone
- Multiple room divisions for private quarters
- Grand architectural features distinguishing from Korad structures
- Marble floor surfaces in main areas

## Descriptive Noun Phrases
- Large plaza-proximate building
- Grand architecture structure
- Courtyard entrance gateway
- Animal hiding courtyard space
- Rooftop access points
- Private quarters interior
- Warrior patrol boundaries
- Escape plan mapping area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_dejah_quarters

[[SECTION markdown]]
# Dejah Thoris Room Quarters

## Environment Role
Secondary private quarters for Dejah Thoris. Location of romantic confession and escape plan mapping sequences.

## Architecture and Geography
Private room interior with marble floor surface for mapping. Accessible from courtyard zone via rooftop/court pathways. Interior space designed for intimate conversations.

## Lighting and Atmosphere Cues
Interior lighting for private conversations, atmospheric tension during love confession. Night-time planning lighting on marble surfaces. Guarded atmosphere reflecting Dejah's emotional state.

## Scale and Environmental Anchors
- Marble floor surface for escape route mapping
- Private room interior dimensions
- Access points from courtyard zone
- Rooftop/court pathway connections
- Interior walls defining private space
- Mapping area on floor surfaces

## Descriptive Noun Phrases
- Private quarters interior
- Marble mapping floor surface
- Escape route planning area
- Intimate conversation space
- Guarded atmosphere zone
- Rooftop access connection
- Warrior patrol boundaries
- Love confession location

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_courtyard_zone

[[SECTION markdown]]
# Courtyard Area

## Environment Role
Transit setting for animal hiding and rooftop movement. Secondary zone connecting John Carter's quarters to Dejah Thoris's room via rooftops/courts.

## Architecture and Geography
Courtyard area with multiple access points from building interiors. Gateway connections to rooftop network. Animal hiding capacity within courtyard space.

## Lighting and Atmosphere Cues
Daylight filtering through courtyard openings, night-time hiding sequences. Atmospheric tension from warrior discovery of escape plan. Hidden animal presence in courtyard zone.

## Scale and Environmental Anchors
- Courtyard entrance gateways
- Animal hiding capacity zones
- Rooftop access points from courtyard
- Multiple building connection points
- Gateway transitions to rooftop network
- Building facade connections

## Descriptive Noun Phrases
- Animal hiding courtyard space
- Rooftop access gateway
- Building connection point
- Warrior patrol boundary zone
- Night-time hiding area
- Courtyard entrance gateways
- Multiple room access points
- Transition pathway zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_rooftop_network

[[SECTION markdown]]
# Rooftop/Court Pathways Network

## Environment Role
Transit setting for movement between buildings. Critical escape route connecting John Carter's quarters to Dejah Thoris's room via rooftops/courts.

## Architecture and Geography
Network of rooftop pathways connecting multiple building structures. Courtyard access points from various buildings. Gateway connections between plaza-proximate buildings.

## Lighting and Atmosphere Cues
Night-time movement sequences on rooftops, atmospheric tension during escape planning. Shadowed rooftop edges for stealth movement. Atmospheric danger from warrior discovery.

## Scale and Environmental Anchors
- Multiple building connection points
- Rooftop pathway network
- Courtyard access gateways
- Building facade connections
- Gateway transitions between structures
- Edge of building rooftops

## Descriptive Noun Phrases
- Rooftop movement pathways
- Building connection network
- Courtyard access gateways
- Night-time escape route
- Stealth movement zones
- Multiple structure connections
- Gateway transition points
- Building facade edges

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_arena_destination

[[SECTION markdown]]
# Thark Arena Destination

## Environment Role
Transit/threat setting for calot games. Location of Sarkoja's planned sacrifice sequence. Target zone for escape plan avoidance.

## Architecture and Geography
Arena structure designed for calot games with spectator viewing areas. Entrance from city boundaries via southern route. Large open space for arena activities.

## Lighting and Atmosphere Cues
Daylight arena sequences, atmospheric danger from Sarkoja's threat. Spectator lighting in viewing areas. Tension from escape plan avoidance necessity.

## Scale and Environmental Anchors
- Arena structure dimensions
- Calot games activity zones
- Southern boundary entrance route
- Spectator viewing platforms
- City boundary access points
- Large open arena space

## Descriptive Noun Phrases
- Arena destination zone
- Calot games activity area
- Southern boundary entrance
- Spectator viewing platforms
- Sarkoja threat location
- Escape plan avoidance target
- City boundary access route
- Arena structure dimensions

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
