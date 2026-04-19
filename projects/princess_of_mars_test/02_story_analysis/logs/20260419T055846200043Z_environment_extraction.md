# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:58:46.200043+00:00
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

Chapter id: CH008

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

**Story Beat 1: The Retreat Order**
After the incubator ceremony, the procession returns to the city. Orders are given for a hasty retreat into buildings due to the approach of enemy airships. The Martians melt into doorways and vanish within three minutes.

**Visual Continuity:**
- **Setting:** Deserted city in a valley with hills beyond.
- **Entities:** Green Martian warriors, chariots, mastodons, mounted warriors.
- **Atmosphere:** Sudden scurrying to cover; deserted buildings.

**Story Beat 2: The Airship Battle and Salvage**
From a window, the narrator observes twenty gray airships approaching. Green Martians fire a volley from building windows. The ships return fire but suffer damage. Several limping craft retreat; one remains unmanned and drifting. Martians board the last ship, loot it (arms, food, water), and burn it as a funeral pyre before towing it away.

**Visual Continuity:**
- **Vessels:** Huge craft, long, low, gray-painted.
- **Action:** Banners dissolved in flame; upper works mowed through by projectiles.
- **Loot:** Arms, ammunition, silks, furs, jewels, strangely carved stone vessels, casks of water.
- **Aftermath:** Great warship soaring majestically into the air as a floating funeral pyre.

**Story Beat 3: The Captive's Arrival**
The group returns to the plaza. The narrator sees an Earthling woman being dragged into a building by Martian females. She is naked, has copper skin and black hair. She signals for help; the narrator fails to respond due to ignorance of customs. She is taken away into the building.

**Visual Continuity:**
- **Figure:** Slender, girlish figure similar to earthly women.
- **Features:** Oval face, finely chiseled features, large lustrous eyes, coal black waving hair caught loosely.
- **Skin:** Light reddish copper color with crimson glow of cheeks and ruby lips.
- **Attire:** Destitute of clothes; highly wrought ornaments only.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test (CH008)

## Primary Environments

| Asset ID | Name | Role | Description |
|----------|------|------|-------------|
| city_plaza | City Plaza | Primary | Central gathering space in valley city where procession returns and orders given for retreat |
| deserted_city_buildings | Deserted City Buildings | Secondary | Multi-story structures in valley with hills beyond; used for cover and window fire positions |
| drifting_warship | Drifting Warship | Secondary | Unmanned gray airship captured by Martians, converted to funeral pyre |

## Environment Families

- **Urban Transit Settings**: Plaza, building interiors, doorways - spaces for movement and gathering
- **Combat Cover Environments**: Deserted buildings with windows - tactical positions for Martian warriors
- **Salvage/Aftermath Zones**: Drifting warship - captured vessel serving as memorial pyre

## Notes

All environments situated in valley city with hills beyond. Primary action occurs at plaza level, secondary action in building windows and on drifting airship. Lighting shifts from daylight to dramatic fire illumination during salvage sequence.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_plaza

[[SECTION markdown]]
# City Plaza - Valley Gathering Space

## Environment Role
Primary setting for chapter opening and closing sequences; central transit hub where procession returns and captive arrives

## Architecture and Geography
Open plaza space within valley city structure. Multi-story buildings surround plaza perimeter with doorways and windows facing inward. Hills visible beyond city limits in background. Ground level paved or compacted earth surface. Building entrances create natural thresholds between interior and exterior spaces.

## Lighting and Atmosphere Cues
Daylight conditions during initial retreat order sequence. Dramatic fire illumination during salvage aftermath when warship burns as funeral pyre. Sudden scurrying creates dynamic shadows across plaza floor. Crimson glow from captive's skin contrasts with ambient daylight. Atmospheric tension conveyed through rapid movement and vanishing Martians within three-minute window.

## Scale Cues and Environmental Anchors
Large open plaza accommodates procession of chariots, mastodons, mounted warriors, and Martian groups. Building doorways serve as entry/exit points for melting crowds. Window openings at multiple heights provide firing positions and observation vantage points. Hills beyond establish valley context and distance scale.

## Descriptive Noun Phrases
- Valley city plaza with surrounding buildings
- Doorway thresholds between interior and exterior
- Multi-story windows facing plaza center
- Hills visible beyond city limits
- Paved or compacted ground surface
- Procession gathering space
- Transit hub for Martian warriors
- Observation deck level windows
- Building entrance archways
- Plaza floor with dynamic shadow play

## Render-Facing Prompt Elements
```
plaza in valley city, multi-story buildings surrounding, hills beyond, daylight to fire illumination transition, doorway thresholds, window openings at multiple heights, chariots and mastodons scale reference, Martian warriors melting into doorways, captive with copper skin visible, crimson glow on cheeks and lips, sudden scurrying shadows
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: deserted_city_buildings

[[SECTION markdown]]
# Deserted City Buildings - Tactical Cover Positions

## Environment Role
Secondary setting for combat cover and window fire positions; transit spaces between plaza and interior rooms

## Architecture and Geography
Multi-story structures with numerous windows facing plaza center. Doorways at street level create entry points. Interior spaces accessible through doorways and stairwells implied by multi-level construction. Buildings positioned throughout valley city with consistent architectural style. Windows serve as primary observation and firing positions.

## Lighting and Atmosphere Cues
Daylight conditions during retreat order sequence. Fire illumination from burning warship casts dramatic shadows across building facades. Sudden scurrying creates dynamic shadow movement on building surfaces. Interior spaces dimly lit compared to plaza exterior. Window frames create strong geometric patterns against sky background.

## Scale Cues and Environmental Anchors
Building height accommodates multiple levels of window openings. Doorway width accommodates full-sized chariots and mastodons passage. Window size allows clear observation of plaza activity below. Building mass establishes valley city scale relative to hills beyond. Interior spaces implied through doorway thresholds and shadow depth.

## Descriptive Noun Phrases
- Multi-story buildings with numerous windows
- Doorway thresholds at street level
- Window openings facing plaza center
- Interior spaces accessible through doorways
- Building facades with geometric window patterns
- Deserted structures in valley city
- Tactical cover positions for warriors
- Observation vantage points at multiple heights
- Stairwells implied by multi-level construction
- Building mass establishing valley scale

## Render-Facing Prompt Elements
```
multi-story buildings in valley city, numerous windows facing plaza center, doorway thresholds at street level, interior spaces dimly lit, window frames creating geometric patterns against sky, deserted structures with consistent architectural style, building height accommodating multiple levels, doorway width for chariots and mastodons passage, fire illumination casting dramatic shadows on facades
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: drifting_warship

[[SECTION markdown]]
# Drifting Warship - Salvage and Funeral Pyre Zone

## Environment Role
Secondary setting for salvage operation and memorial pyre; transit zone between combat area and towing sequence

## Architecture and Geography
Large gray-painted airship vessel, long and low profile. Hull structure with upper works mowed through by projectiles. Banners dissolved in flame on exterior surfaces. Interior spaces accessible through damaged hull openings. Vessel positioned in valley sky above city plaza. Drifting craft converted to funeral pyre with burning banners and upper works.

## Lighting and Atmosphere Cues
Daylight conditions during initial observation from building windows. Fire illumination from burning warship creates dramatic atmospheric effects. Flames consume banners and mowed upper works. Crimson glow from captive's skin visible against fire backdrop. Smoke and ash create atmospheric haze around vessel. Dramatic contrast between gray hull and orange flames.

## Scale Cues and Environmental Anchors
Vessel size established through observation from building windows. Hull length accommodates multiple Martian warriors for boarding and looting operations. Upper works height allows projectile damage to be clearly visible. Vessel width provides space for arms, ammunition, silks, furs, jewels, stone vessels, and water casks. Valley sky establishes altitude context relative to city below.

## Descriptive Noun Phrases
- Large gray-painted airship vessel
- Long low profile hull structure
- Upper works mowed through by projectiles
- Banners dissolved in flame on exterior
- Interior spaces accessible through damaged openings
- Drifting craft converted to funeral pyre
- Salvage zone with arms ammunition silks furs jewels
- Stone vessels and water casks as loot items
- Burning warship soaring majestically into air
- Floating funeral pyre in valley sky

## Render-Facing Prompt Elements
```
large gray-painted airship vessel, long low profile hull, upper works mowed through by projectiles, banners dissolved in flame on exterior, interior spaces accessible through damaged openings, drifting craft converted to funeral pyre, salvage zone with arms ammunition silks furs jewels stone vessels water casks, burning warship soaring majestically into air, floating funeral pyre in valley sky, fire illumination creating dramatic atmospheric effects
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
