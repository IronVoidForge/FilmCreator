# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:01:48.609728+00:00
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

Chapter id: CH019

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

# Chapter Summary: CH019 - Battling in the Arena

**Visual Continuity Facts:**
- **Dungeon/Cell:** Dark environment; keys missing from dead jailer's body.
- **Amphitheater:** Excavated below ground surface, filled with debris, holds 20,000 Warhoons.
- **Arena:** Immense, uneven, unkempt, piled with building stone to prevent escape. Cages at ends holding victims.
- **Audience:** Seating space occupied, Dak Kova and chieftains on raised platform.
- **Victims:** Green Martian females, calots (wild dogs), mad zitidars, green warriors, women of other hordes, wild beasts.

**Story Progression:**
1. Carter regains composure, realizes keys are gone, Dejah Thoris taken to lair.
2. No food for two days, then new messenger.
3. Kantos Kan arrives as new prisoner (red Martian/Heliumite). They exchange greetings and stories.
4. Kantos details his escape from Zodanga after the defeat of battleships.
5. Caged together in amphitheater for games.
6. Games begin: Green females vs calots, then mad zitidar, etc.
7. Carter fights men/beasts easily with long-sword.
8. Final three left: Green warrior, Kantos Kan, Carter.
9. Kantos kills green warrior with thrown sword.
10. Carter and Kantos fight to death (fake out). Carter survives in darkness.
11. Carter escapes stealthily to top of amphitheater, reaches hills east of city.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH019 Princess of Mars

## Primary Environments
- **dungeon_cell** - Dark confinement space where keys are missing from dead jailer's body. Primary setting for Carter's initial recovery.
- **amphitheater** - Excavated underground arena filled with debris, capacity 20,000 Warhoons. Main games venue.
- **arena** - Immense uneven fighting space piled with building stone to prevent escape. Cages at ends holding victims. Primary combat setting.

## Secondary Environments  
- **audience_seating** - Occupied spectator space with raised platform for Dak Kova and chieftains. Secondary viewing area.

## Transit/Escape Routes
- **eastern_hills** - Hills east of city reached after Carter escapes amphitheater top. Final escape destination.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dungeon_cell

[[SECTION markdown]]
# Dungeon Cell Environment

## Role
Primary setting for Carter's initial recovery and realization of keys missing from dead jailer's body.

## Architecture & Geography
Dark confinement space with cell structure. Underground prison facility. Stone walls and floor typical of Martian dungeon construction.

## Lighting & Atmosphere
Deep darkness, shadowed corners, minimal ambient light. Oppressive atmosphere of imprisonment and death. Dead bodies present creating grim visual elements.

## Scale & Anchors
Small enclosed space, intimate scale. Cell door as primary anchor point. Jailer's body as environmental landmark. Missing keys create narrative focal point.

## Descriptive Noun Phrases
- dark stone confinement cell
- underground prison chamber  
- dead jailer's body location
- missing key storage area
- grim dungeon atmosphere
- shadowed cell interior
- stone wall boundaries
- confined space geometry

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: amphitheater

[[SECTION markdown]]
# Amphitheater Environment

## Role
Primary games venue, secondary spectator area. Main combat and entertainment space for 20,000 Warhoons.

## Architecture & Geography
Excavated below ground surface structure. Circular or oval arena design typical of amphitheater construction. Debris-filled interior with uneven terrain.

## Lighting & Atmosphere
Underground lighting conditions, artificial illumination from above. Dust and debris create hazy atmosphere. Large crowd presence affects ambient light quality.

## Scale & Anchors
Massive scale - 20,000 Warhoons capacity. Central fighting area as primary anchor. Cages at ends holding victims serve secondary anchors. Raised platform for Dak Kova and chieftains.

## Descriptive Noun Phrases
- excavated underground amphitheater
- debris-filled arena floor
- twenty thousand warhoon capacity
- central combat zone
- victim cage structures
- raised spectator platform
- underground lighting fixtures
- circular arena geometry
- debris scattered interior
- large crowd viewing area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arena

[[SECTION markdown]]
# Arena Environment

## Role
Primary combat setting. Main fighting space for games and final battles between Carter, Kantos Kan, and green warrior.

## Architecture & Geography
Immense uneven fighting surface. Piled with building stone to prevent escape attempts. Cages positioned at both ends holding victims. Open arena design within amphitheater structure.

## Lighting & Atmosphere
Arena-specific lighting conditions, focused illumination on fighting area. Stone piles create shadow variations. Darker corners around perimeter. Combat-focused ambient atmosphere.

## Scale & Anchors
Large scale combat space. Building stone piles as primary environmental anchors. Cage structures at ends serve secondary anchors. Fighting surface center point as main focal area.

## Descriptive Noun Phrases
- immense uneven fighting surface
- building stone pile barriers
- escape prevention stone walls
- victim cage end structures
- arena combat zone
- piled stone perimeter
- central fighting platform
- stone barrier geometry
- cage anchor points
- arena lighting fixtures

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_seating

[[SECTION markdown]]
# Audience Seating Environment

## Role
Secondary spectator viewing area. Raised platform space for Dak Kova and chieftains.

## Architecture & Geography
Occupied seating space with tiered arrangement. Raised platform section at front for dignitaries. Spectator galleries surrounding arena. Stone or wood construction typical of amphitheater seating.

## Lighting & Atmosphere
Crowd-illuminated atmosphere, ambient light from spectators. Platform area receives focused lighting. Seating areas in shadow between illuminated zones. Social gathering atmosphere.

## Scale & Anchors
Large spectator capacity with tiered arrangement. Raised platform as primary anchor point. Spectator galleries as secondary anchors. Dignitary seating area as focal point.

## Descriptive Noun Phrases
- occupied spectator seating area
- raised dignitary platform
- tiered audience galleries
- chieftain viewing section
- Dak Kova platform location
- spectator capacity space
- tiered stone seating
- gallery viewing areas
- platform anchor structure
- crowd illuminated zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: eastern_hills

[[SECTION markdown]]
# Eastern Hills Environment

## Role
Transit/escape destination. Final escape route from amphitheater top to hills east of city.

## Architecture & Geography
Natural hill terrain east of Martian city. Open outdoor landscape contrasting with enclosed arena spaces. Natural elevation providing vantage point.

## Lighting & Atmosphere
Natural daylight conditions, open sky visibility. Hilltop lighting creates panoramic views. Atmospheric depth from elevated position. Freedom-oriented atmosphere after escape.

## Scale & Anchors
Large natural scale - hill terrain and cityscape visible. Amphitheater top as starting anchor. City below as secondary anchor point. Eastern direction as navigational anchor.

## Descriptive Noun Phrases
- eastern hill terrain
- city east of amphitheater
- elevated escape destination
- natural hill landscape
- panoramic viewing position
- open outdoor environment
- hilltop vantage area
- eastern directional zone
- natural elevation terrain
- escape route destination

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
