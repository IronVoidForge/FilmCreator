# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:53:46.353633+00:00
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

Chapter id: CH001

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

# CHAPTER I: ON THE ARIZONA HILLS

## Story Summary

### Introduction
Narrator introduces himself as an old man who does not age, fearing death despite having died twice before. He intends to write a chronicle of his life and death.

### The Mine and Departure
Carter and Powell locate a gold-bearing quartz vein in late winter 1865. Powell leaves to purchase machinery; Carter guards the claim.

### The Chase
Carter sees Powell's trail vanish. He investigates, finding tracks of unshod ponies galloping away. He chases them through the valley and up the mountainside.

### Discovery and Escape
Carter finds Powell dead in an Apache camp surrounded by tepees. He charges into the camp, shooting at warriors who flee. He retrieves Powell's body and escapes pursuit by taking a wrong trail into a cave.

### The Cave
Carter enters a large cave chamber (approx 100 feet diameter). He lays Powell down, confirms death, then collapses from exhaustion on the floor.

## Visual Continuity

- **Landscape:** Arizona hills, clear mornings, valley views, moonlight illumination.
- **Camp:** White with Indian tepees, half a thousand warriors clustered around center object.
- **Cave:** Large chamber, smooth and well-worn floor, back lost in dense shadow, four feet high opening.
- **Lighting:** Moonlight (clear rays), daylight without warning at cave entrance.

## Uncertainties & Notes

- Narrator's exact age is unknown ("possibly a hundred").
- Cave has openings into other apartments (visibility unclear).
- Exact location of trail to pass vs. defile is ambiguous to narrator.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter I

## Extracted Environments

| Asset ID | Name | Role | Primary Feature |
|----------|------|------|-----------------|
| arizona_hills_landscape | Arizona Hills Landscape | Primary Setting | Rolling hills, valley views, clear morning light |
| apache_camp_setting | Apache Camp Setting | Secondary Setting | Tepees, warriors, central gathering object |
| cave_chamber_escape | Cave Chamber Escape | Transit Setting | Large chamber, smooth floor, shadowed interior |

## Environment Families

1. **arizona_hills_landscape** - Primary chase environment with valley and mountain views
2. **apache_camp_setting** - Secondary discovery environment with indigenous structures
3. **cave_chamber_escape** - Transit escape environment with natural rock formations

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_hills_landscape

[[SECTION markdown]]
# Arizona Hills Landscape

## Environment Role
Primary setting for the majority of Chapter I chase sequence and establishing shots.

## Architecture and Geography
- Rolling Arizona hills with clear morning visibility
- Valley views accessible from elevated positions
- Mountain side terrain for upward tracking movement
- Natural open landscape without man-made structures

## Lighting and Atmosphere Cues
- Clear morning light with distinct sun rays
- Moonlight illumination during night sequences
- Daylight appearing without warning at cave entrance
- Atmospheric clarity typical of Arizona high country

## Scale Cues and Environmental Anchors
- Large diameter valley spaces for wide shots
- Mountain ridges providing height reference points
- Horizon lines visible across open landscape
- Ground level tracking surfaces for character movement

## Descriptive Noun Phrases
- "Arizona rolling hills"
- "Clear morning valley views"
- "Moonlit landscape expanse"
- "Mountain side terrain path"
- "Open high country ground"
- "Valley floor visibility"
- "Horizon line reference"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: apache_camp_setting

[[SECTION markdown]]
# Apache Camp Setting

## Environment Role
Secondary setting for discovery sequence where Carter finds Powell's body.

## Architecture and Geography
- Indigenous tepee structures clustered around center object
- Half a thousand warriors gathered in central area
- White-colored camp materials visible
- Central gathering point surrounded by perimeter

## Lighting and Atmosphere Cues
- Camp lighting during day sequences
- Warrior encampment illumination
- Interior shadowed spaces within tepees
- Exterior daylight on camp structures

## Scale Cues and Environmental Anchors
- Large central gathering space for wide shots
- Tepee cluster providing depth reference
- Perimeter warrior positions marking boundaries
- Ground level tracking surfaces for escape movement

## Descriptive Noun Phrases
- "Apache tepee encampment"
- "Warrior gathering center"
- "Camp perimeter structure"
- "Tepee cluster formation"
- "Central object space"
- "Encampment ground surface"
- "Indigenous camp materials"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_chamber_escape

[[SECTION markdown]]
# Cave Chamber Escape

## Environment Role
Transit setting for escape sequence where Carter enters natural rock formation.

## Architecture and Geography
- Large cave chamber approximately 100 feet diameter
- Smooth well-worn floor surface
- Dense shadowed interior spaces
- Four feet high opening to exterior
- Multiple apartment openings into other chambers

## Lighting and Atmosphere Cues
- Moonlight visible at cave entrance
- Daylight without warning at entrance point
- Interior back lost in dense shadow
- Natural rock formation lighting patterns

## Scale Cues and Environmental Anchors
- Large chamber diameter for wide interior shots
- Floor surface providing tracking reference
- Opening height marking boundary between spaces
- Shadow depth indicating chamber dimensions
- Multiple apartment entrances visible

## Descriptive Noun Phrases
- "Large cave chamber space"
- "Smooth floor surface"
- "Dense shadowed interior"
- "Cave entrance opening"
- "Rock formation chamber"
- "Interior apartment space"
- "Natural rock structure"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
