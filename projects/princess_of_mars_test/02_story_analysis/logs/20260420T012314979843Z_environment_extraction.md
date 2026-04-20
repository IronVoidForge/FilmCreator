# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:23:14.979843+00:00
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

**Story Summary:**
- **Arrival in Thark:** After 30 days on Barsoom, John Carter and Dejah Thoris enter the ancient city of Thark. They are assigned new quarters near the central plaza.
- **Meeting Allies:** John locates Sola and Woola. Woola is reunited with John after a period of separation.
- **Threat Revealed:** Sarkoja has been seen; she plans to throw Dejah Thoris to wild calots (dogs) in the arena during yearly games.
- **Escape Plan Formulated:** John proposes an escape to Helium. Sola agrees. They decide on a route via a northern waterway to avoid detection.
- **Night Departure Attempt:** John prepares two thoats for travel. He meets Dejah Thoris and Sola at the city boundary.
- **Discovery:** The plan is discovered by warriors who intend to capture John Carter upon his return alone.
- **Capture Threat:** John hides in a courtyard with his animals, then climbs back to Dejah Thoris's room. He overhears warriors planning to chain him in vaults beneath the Jeddak's quarters if he returns without her.

**Visual Continuity Facts:**
- **Architecture:** Thark features grand public buildings and large chambers; John Carter occupies a building with an entire floor. Quarters face the plaza or are assigned by community divisions.
- **Map Drawing:** Dejah Thoris draws the first map of Barsoomian territory on the marble floor using a diamond, showing waterways (straight lines) and cities (circles).
- **Night Movement:** Stealthy travel through city streets, courtyards with moss-like vegetation, and second-story windows.
- **Animals:** Thoats and zitidars move restlessly in paddocks; John Carter navigates the herd at night without saddling them initially.
- **Lighting:** Scenes transition from daylight to sunset/moonlight (wild Barsoomian heavens) affecting visibility during crossings.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Thark City Environment Index

## Primary Environments

| Asset ID | Name | Role | Key Features |
|----------|------|------|--------------|
| thark_city_quarters | Thark Quarters | Primary Setting | John Carter's floor, plaza-facing rooms |
| thark_courtyards | Thark Courtyards | Secondary Setting | Moss-like vegetation, night movement areas |
| thark_windows | Thark Windows | Transit Setting | Second-story access points, stealth routes |
| thark_paddocks | Thark Paddocks | Secondary Setting | Animal containment for thoats and zitidars |

## Environment Families

- **Living Quarters**: Buildings with entire floors assigned to Jeddak's household members
- **Public Architecture**: Grand chambers and buildings in central plaza area
- **Stealth Routes**: Night movement paths through courtyards and windows
- **Animal Areas**: Paddocks and containment spaces for Barsoomian beasts

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_city_quarters

[[SECTION markdown]]
# Thark City Quarters

## Environment Role
Primary setting - John Carter's assigned living quarters near central plaza

## Architecture and Geography
- Entire floor dedicated to household member
- Rooms face the central plaza or assigned by community divisions
- Grand public buildings with large chambers nearby
- Marble floors used for map drawing activities

## Lighting and Atmosphere Cues
- Daylight transitions to sunset/moonlight (wild Barsoomian heavens)
- Visibility affected during crossings
- Interior spaces lit by ambient light sources

## Scale Cues and Environmental Anchors
- Floor-level living space with full room dimensions
- Plaza-facing orientation provides external reference points
- Community divisions mark territorial boundaries

## Descriptive Noun Phrases
- "Plaza-facing quarters"
- "Entire floor dwelling"
- "Community division rooms"
- "Grand chamber spaces"
- "Marble floor areas"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_courtyards

[[SECTION markdown]]
# Thark Courtyards

## Environment Role
Secondary setting - Night movement and stealth travel areas

## Architecture and Geography
- Moss-like vegetation covering ground surfaces
- Courtyard spaces between buildings
- Ground-level access points for stealth movement
- Vegetation provides cover during crossings

## Lighting and Atmosphere Cues
- Sunset to moonlight transitions
- Reduced visibility during night crossings
- Wild Barsoomian heavens lighting conditions

## Scale Cues and Environmental Anchors
- Ground-level courtyard dimensions
- Building perimeters define courtyard boundaries
- Vegetation density affects movement speed

## Descriptive Noun Phrases
- "Moss-covered courtyards"
- "Ground-level stealth routes"
- "Vegetation-dense areas"
- "Building perimeter spaces"
- "Night crossing paths"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_windows

[[SECTION markdown]]
# Thark Windows

## Environment Role
Transit setting - Second-story access and stealth routes

## Architecture and Geography
- Second-story window openings
- Elevated access points between buildings
- Window frames define passage dimensions
- Vertical movement paths through building facades

## Lighting and Atmosphere Cues
- Daylight to moonlight visibility changes
- Interior light sources visible from outside
- External lighting affects interior visibility

## Scale Cues and Environmental Anchors
- Window height determines climb difficulty
- Building facade defines vertical boundaries
- Room interiors accessible through window passages

## Descriptive Noun Phrases
- "Second-story windows"
- "Elevated access points"
- "Window passage routes"
- "Building facade openings"
- "Vertical movement paths"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_paddocks

[[SECTION markdown]]
# Thark Paddocks

## Environment Role
Secondary setting - Animal containment and movement areas

## Architecture and Geography
- Enclosed spaces for animal containment
- Restless animal movement patterns
- Paddock boundaries define herd limits
- Ground surfaces suitable for animal locomotion

## Lighting and Atmosphere Cues
- Daylight to sunset transitions
- Interior lighting affects visibility
- External light sources illuminate enclosure

## Scale Cues and Environmental Anchors
- Paddock dimensions accommodate multiple animals
- Animal containment areas mark territory boundaries
- Herd movement patterns define space usage

## Descriptive Noun Phrases
- "Animal containment paddocks"
- "Herd movement areas"
- "Enclosed animal spaces"
- "Restless animal zones"
- "Ground-level enclosures"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
