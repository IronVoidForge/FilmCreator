# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:49:06.439462+00:00
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

# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Summary
The narrative begins on the third day after an incubator ceremony. The procession retreats to a city building due to an immediate order. From a window, John Carter observes the arrival of twenty large gray air craft. A battle ensues between Green Martians firing from buildings and the Air Fleet returning fire. The fleet retreats after damage; one ship is disabled and unmanned. Warriors loot the vessel (arms, jewels, water), burn it, and tow it away before it explodes. Carter witnesses a human female prisoner being dragged from the burning ship into a nearby building by Green Martian females. At the city plaza, the prisoner turns to Carter as she enters the building; he fails to respond to her signal of appeal. She is dragged away into the depths of the edifice.

## Visual Continuity
- **Air Craft:** Long, low, gray-painted vessels with strange banners and odd devices on prows. Figures crowd forward decks.
- **Green Martians:** Green skin, wear ornaments, carry spears, fire from windows/roofs.
- **Prisoner:** Slender, girlish figure. Skin is light reddish copper. Features finely chiseled. Eyes large/lustrous. Hair coal black, waving, caught loosely into a strange coiffure. Naked except for highly wrought ornaments. Cheeks crimson, lips ruby.
- **Locations:** City buildings (upper floors, windows, roofs), open ground/plaza, valley, hills beyond.
- **Action Details:** Ships swing broadside, dip below hill crests, drift southeast/southwesterly. Fire causes spurt of flame from missile impact. Guy ropes release simultaneously.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH008

## Extracted Environments

| Asset ID | Role | Primary Geography | Atmosphere Cues |
|----------|------|-------------------|-----------------|
| city_buildings | primary | urban structures, upper floors, windows, roofs | daylight, smoke from fire, missile impact flames |
| open_ground_plaza | transit | open ground, plaza area | daylight, spurt of flame from impacts |
| valley | secondary | valley floor beyond city | daylight, distant horizon |
| hills_beyond | secondary | hill crests, slopes southeast/southwesterly | daylight, dip below crests |

## Environment Families Summary

- **city_buildings**: Primary observation and action setting with multiple levels
- **open_ground_plaza**: Transit zone for fleet movement and battle effects
- **valley**: Background geography establishing scale
- **hills_beyond**: Distant geography providing directional context

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_buildings

[[SECTION markdown]]
# City Buildings - CH008 Environment

## Environment Role
Primary setting for observation and action sequences. Multiple vertical levels utilized throughout chapter.

## Architecture and Geography
- Urban structures with upper floors, windows, and roofs
- Building facades facing open plaza area
- Interior spaces accessible from exterior levels
- Rooftop positions for Green Martian firing positions
- Window openings serving as vantage points for Carter's observation

## Lighting and Atmosphere Cues
- Daylight conditions throughout primary sequences
- Smoke accumulation from fire damage
- Missile impact flames spurt from building surfaces
- Fire-induced atmospheric disturbance visible from plaza
- Light reddish copper skin tones of prisoner contrast against building interiors

## Scale Cues and Environmental Anchors
- Building height establishes vertical scale for air craft approach
- Window-to-ground distance defines observation perspective
- Rooftop elevation provides firing platform context
- Plaza proximity creates foreground-background relationship
- Valley visibility from upper levels indicates regional geography

## Descriptive Noun Phrases for Render-Facing Prompts
- "upper floor windows with daylight illumination"
- "building facades facing open plaza area"
- "rooftop positions with Green Martian firing stances"
- "interior spaces accessible from exterior levels"
- "missile impact flames spurt from building surfaces"
- "smoke accumulation from fire damage"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: open_ground_plaza

[[SECTION markdown]]
# Open Ground Plaza - CH008 Environment

## Environment Role
Transit setting for fleet movement and battle effects. Primary ground-level action zone.

## Architecture and Geography
- Open ground plaza area adjacent to city buildings
- Flat terrain suitable for air craft landing approaches
- Ground level connecting building upper floors to valley beyond
- Plaza boundaries defined by surrounding structures
- Missile impact zones on open surface

## Lighting and Atmosphere Cues
- Daylight conditions across entire plaza surface
- Spurt of flame from missile impacts visible on ground
- Fire effects creating atmospheric disturbance
- Light reflecting off building surfaces into plaza
- Smoke patterns drifting across open area

## Scale Cues and Environmental Anchors
- Plaza width establishes horizontal scale for fleet movement
- Building proximity creates foreground-background relationship
- Valley visibility beyond plaza defines regional context
- Hill crests visible from plaza provide directional reference
- Air craft approach paths defined by plaza boundaries

## Descriptive Noun Phrases for Render-Facing Prompts
- "open ground plaza area adjacent to city buildings"
- "flat terrain suitable for air craft landing approaches"
- "missile impact zones on open surface"
- "spurt of flame from missile impacts visible on ground"
- "fire effects creating atmospheric disturbance"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley

[[SECTION markdown]]
# Valley - CH008 Environment

## Environment Role
Secondary background geography establishing regional scale and context.

## Architecture and Geography
- Valley floor beyond city buildings
- Open terrain extending from plaza area
- Distant horizon line visible from upper levels
- Regional geography providing spatial orientation
- Background landscape for fleet movement context

## Lighting and Atmosphere Cues
- Daylight conditions across valley floor
- Atmospheric haze at distant horizon
- Light reflecting off valley surfaces
- Smoke patterns drifting into valley space
- Valley visibility from building windows

## Scale Cues and Environmental Anchors
- Valley depth establishes regional scale
- Distance from city buildings defines background relationship
- Hill crests beyond valley provide directional reference
- Fleet movement paths extending toward valley horizon
- Valley floor visible from plaza level

## Descriptive Noun Phrases for Render-Facing Prompts
- "valley floor beyond city buildings"
- "open terrain extending from plaza area"
- "distant horizon line visible from upper levels"
- "regional geography providing spatial orientation"
- "background landscape for fleet movement context"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills_beyond

[[SECTION markdown]]
# Hills Beyond - CH008 Environment

## Environment Role
Secondary distant geography providing directional context and scale reference.

## Architecture and Geography
- Hill crests visible from plaza and building levels
- Slopes extending southeast/southwesterly directions
- Distant terrain beyond valley floor
- Elevated positions for air craft approach paths
- Background geography defining regional boundaries

## Lighting and Atmosphere Cues
- Daylight conditions across hill surfaces
- Light reflecting off slope faces
- Atmospheric haze at distant crest lines
- Smoke patterns drifting toward hill elevations
- Hill visibility from plaza level

## Scale Cues and Environmental Anchors
- Hill elevation provides vertical scale reference
- Crest lines visible from plaza define horizon
- Fleet approach paths dip below hill crests
- Southeast/southwesterly directional orientation established
- Distant terrain beyond valley establishes regional context

## Descriptive Noun Phrases for Render-Facing Prompts
- "hill crests visible from plaza and building levels"
- "slopes extending southeast/southwesterly directions"
- "distant terrain beyond valley floor"
- "elevated positions for air craft approach paths"
- "background geography defining regional boundaries"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
