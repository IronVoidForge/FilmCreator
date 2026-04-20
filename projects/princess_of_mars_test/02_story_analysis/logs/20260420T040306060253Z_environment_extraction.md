# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:03:06.060253+00:00
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

Chapter id: CH020

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

# Chapter Summary: CH020 - The Atmosphere Factory

## Story Summary
John Carter waits two days for Kantos Kan without success, then wanders northwesterly toward a waterway. He survives two weeks of starvation and wild beast attacks using his telepathic power and long-sword. He is attacked by a large, many-legged beast but is saved by Woola, who has left Dejah Thoris due to her presumed death. Carter finds the Atmosphere Factory after fifteen days of searching. Inside, he meets an old Martian guardian who explains the ninth ray and atmosphere production process. Carter learns the doors are unlocked via telepathic thought waves. He escapes the factory using this power, reaching Zodanga farm territory. There, Red Martians provide him with food, a domestic bull-throat, reddish oil to color his body, and advice to seek military employment in Zodanga.

## Visual Continuity
- **Woola:** Appears half-starved, shadow of former self, eating the dead beast's carcass. His loyalty is emphasized despite leaving Dejah Thoris.
- **Atmosphere Factory:** Massive building with walls 150 feet thick and roof guarded by glass covering five feet thick. Doors are 20 feet thick and manipulated by telepathy.
- **Old Man's Diadem:** Wears a small collar of gold with a great ornament set with huge diamonds and a strange stone scintillating nine different rays (seven colors + two new rays).
- **Carter's Appearance:** Initially wears Green Warrior metal but is identified as Red Man figure. Later anoints body with reddish oil to resemble Red Martians, cuts hair square at back/banged in front, and renews ornaments in Zodangan style.
- **Environment:** Barsoomian scene lit by nearer moon/hurting moons. Wild beasts are described as strange, uncouth monstrosities. Farm buildings are raised 40-50 feet from ground on metal shafts operated by radium engines.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH020

## Atmosphere Factory
- Role: Primary/Secondary Setting
- Description: Massive industrial facility with thick walls and glass-covered roof, interior space for guardian interaction
- Key Features: Telepathic door manipulation, ninth ray production area, old Martian guardian quarters

## Zodanga Farm Territory
- Role: Transit/Ending Setting  
- Description: Elevated farm buildings on metal shafts, reddish oil storage, domestic bull-throat housing
- Key Features: Radium engine operated lifts, military employment recruitment center, Red Martian food distribution hub

## Wild Beast Environment
- Role: Transitional Setting
- Description: Barsoomian landscape with strange monstrosities, carcass feeding area
- Key Features: Moon-lit terrain, telepathic power activation zone, starvation survival space
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: atmosphere_factory

[[SECTION markdown]]
# Atmosphere Factory Environment

## Role
Primary and Secondary Setting - Main industrial facility where Carter meets the old Martian guardian and learns about atmosphere production

## Architecture and Geography
- Massive building structure with walls 150 feet thick
- Roof guarded by glass covering five feet thick  
- Doors 20 feet thick, manipulated via telepathic thought waves
- Interior space for guardian quarters and ninth ray production area
- Barsoomian industrial architecture style

## Lighting and Atmosphere Cues
- Moon-lit interior with nearer moon illumination
- Strange atmospheric quality from ninth ray scintillation
- Telepathic activation creates visible energy waves
- Industrial lighting mixed with natural moonlight

## Scale Cues and Environmental Anchors
- Wall thickness: 150 feet (massive industrial scale)
- Door thickness: 20 feet (imposing entryway)
- Glass roof coverage: five feet thick (protective overhead)
- Guardian quarters as interior anchor point
- Ninth ray production area as functional anchor

## Descriptive Noun Phrases for Render Prompts
- "massive industrial facility with telepathic door manipulation"
- "old Martian guardian quarters inside atmosphere factory"
- "ninth ray production chamber with scintillating energy"
- "thick glass roof covering five feet thick"
- "moon-lit interior space with telepathic activation waves"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodanga_farm_territory

[[SECTION markdown]]
# Zodanga Farm Territory Environment

## Role
Transit and Ending Setting - Where Carter arrives after escaping the factory, receives supplies and military recruitment

## Architecture and Geography
- Farm buildings raised 40-50 feet from ground on metal shafts
- Metal shafts operated by radium engines
- Reddish oil storage facilities for body coloring
- Domestic bull-throat housing quarters
- Military employment recruitment center structure

## Lighting and Atmosphere Cues
- Barsoomian farm lighting with nearer moon illumination
- Radium engine glow from metal shaft operations
- Reddish oil coloration creates warm atmospheric tone
- Farm territory landscape with elevated structures

## Scale Cues and Environmental Anchors
- Building elevation: 40-50 feet above ground (raised architecture)
- Metal shaft height as vertical anchor
- Reddish oil storage tanks as functional anchors
- Bull-throat housing quarters as domestic anchor
- Military recruitment center as social anchor

## Descriptive Noun Phrases for Render Prompts
- "elevated farm buildings on metal shafts operated by radium engines"
- "reddish oil storage facilities for body coloring"
- "domestic bull-throat housing quarters in Zodanga territory"
- "military employment recruitment center structure"
- "raised architecture 40-50 feet from ground on metal shafts"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
