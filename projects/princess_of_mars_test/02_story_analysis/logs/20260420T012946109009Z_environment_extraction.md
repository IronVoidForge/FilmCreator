# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:29:46.109512+00:00
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

# Chapter Summary: Battling in the Arena

## Story Summary
John Carter regains composure after a failed escape attempt, realizing Dejah Thoris and Sola were taken to be devoured. He endures two days of hunger before Kantos Kan is brought in as a fellow prisoner. They exchange greetings ("kaor") and backstories; Kantos reveals the expedition's defeat and the futile search for Dejah Thoris by Helium fleets.

Both are caged for the arena games, which last ten days. The amphitheater fills with 20,000 Warhoons. Initial contests involve green females versus calots (wild dogs), followed by beast battles. John Carter fights men and beasts, winning easily due to strength and agility; the crowd demands he join the hordes.

The final three combatants are a giant green warrior, Kantos Kan, and John Carter. The green warrior is killed when Kantos throws his sword at the giant's heart using Martian swordsmanship. Kantos then fights John Carter. To avoid death, they stage a duel until dark. John pretends to be dead by having Kantos thrust his sword into his chest; he falls to the ground with the weapon protruding. Kantos places his foot on John's neck and delivers a final blow through the neck, but the blade slips harmlessly into the sand.

Kantos leaves to claim his freedom, instructing John to meet him in the hills east of the city. John Carter creeps to the top of the amphitheater and escapes into the untenanted portion of the dead city, reaching the hills beyond.

## Visual Continuity Facts
- **Setting:** Underground amphitheater excavated below ground surface; partially filled with debris from ruined edifices.
- **Audience:** 20,000 Warhoons seated on raised platform; Dak Kova at center of one side.
- **Cages:** Constructed at each end to hold captives until turns come; stone piled around arena to prevent escape.
- **Combatants:** Red Martians (John/Kantos), Green Warriors (Enemies), Calots (dogs), Zitidars, Mad Zitidars.
- **Weapons:** Long-swords used for combat and sword throws; daggers given to female captives.
- **Lighting:** Dim torch light in dungeon; darkness falls during final encounter between Kantos and John.
- **Exit:** Top of amphitheater leads to untenanted portion of dead city, allowing access to hills east of city.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index: Battling in the Arena

## underground_amphitheater
- Role: Primary combat setting
- Architecture: Underground amphitheater excavated below ground surface, partially filled with debris from ruined edifices
- Lighting: Dim torch light throughout; darkness falls during final encounter
- Atmosphere: 20,000 Warhoons seated on raised platform; stone piled around arena to prevent escape
- Scale: Large enclosed space accommodating massive crowd and combatants
- Anchors: Cages at each end holding captives; raised viewing platform; central arena floor

## dead_city
- Role: Transit/escape setting
- Architecture: Untenanted portion of ruined city beyond amphitheater exit
- Lighting: Dim torch light in dungeon areas; natural daylight from hills
- Atmosphere: Ruined structures, debris-filled pathways, abandoned spaces
- Scale: Extensive urban ruins connecting amphitheater to hills
- Anchors: Top of amphitheater entrance; ruined edifices; city boundaries

## hills_east_of_city
- Role: Destination/meeting point setting
- Architecture: Natural terrain east of dead city
- Lighting: Natural daylight from hilltops
- Atmosphere: Open outdoor space, natural landscape beyond urban ruins
- Scale: Elevated terrain providing vantage points over city
- Anchors: Hilltop meeting location; eastern boundary of city

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: underground_amphitheater

[[SECTION markdown]]
# Underground Amphitheater

## Environment Role
Primary combat setting for arena games lasting ten days.

## Architecture and Geography
Underground amphitheater excavated below ground surface, partially filled with debris from ruined edifices. Cages constructed at each end to hold captives until turns come. Stone piled around arena perimeter to prevent escape. Raised platform seating accommodates 20,000 Warhoons audience.

## Lighting and Atmosphere
Dim torch light illuminates dungeon areas throughout most of the games. Darkness falls during final encounter between Kantos Kan and John Carter. Crowd atmosphere demands participation from combatants.

## Scale Cues
Large enclosed space accommodating massive crowd viewing platform. Arena floor sized for multiple combatants including giant green warrior, calots (wild dogs), beast battles, and human fighters. Underground excavation depth creates natural lighting limitations.

## Environmental Anchors
- Cages at each end holding captives until turns come
- Raised Warhoon seating platform with Dak Kova at center of one side
- Stone perimeter preventing escape attempts
- Central arena floor for combat activities
- Top amphitheater exit leading to dead city

## Descriptive Noun Phrases
Underground fighting arena, stone-walled amphitheater, torch-lit dungeon space, captive holding cages, raised viewing platform, debris-filled excavation, arena perimeter stones, underground combat chamber, warhoon seating tier, amphitheater exit tunnel

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dead_city

[[SECTION markdown]]
# Dead City

## Environment Role
Transit and escape setting connecting amphitheater to hills east of city.

## Architecture and Geography
Untenanted portion of ruined city beyond amphitheater exit. Ruined structures with debris-filled pathways. Abandoned urban spaces connecting underground arena to natural hills. Exit from top of amphitheater leads through this area.

## Lighting and Atmosphere
Dim torch light in dungeon areas within city ruins. Natural daylight visible from hill approaches. Ruined atmosphere of abandoned urban space beyond active arena.

## Scale Cues
Extensive urban ruins spanning significant distance between amphitheater and hills. Multiple ruined edifices creating varied pathways through abandoned city sections.

## Environmental Anchors
- Top of amphitheater entrance point
- Untenanted portion of dead city
- Ruined edifices throughout pathways
- City boundaries marking eastern edge
- Hill access routes from urban ruins

## Descriptive Noun Phrases
Untenanted ruined city, abandoned urban space, debris-filled pathways, ruined edifices, amphitheater exit tunnel, dead city entrance, abandoned city sections, ruined urban architecture, city boundary markers, hill approach routes

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills_east_of_city

[[SECTION markdown]]
# Hills East of City

## Environment Role
Destination and meeting point setting for post-arena encounter.

## Architecture and Geography
Natural terrain east of dead city providing elevated vantage points over urban ruins. Open outdoor space beyond abandoned city boundaries. Natural landscape features including hilltops and slopes.

## Lighting and Atmosphere
Natural daylight from hilltops illuminating open terrain. Clear visibility over city from elevated positions. Outdoor atmosphere contrasting with underground arena spaces.

## Scale Cues
Elevated terrain providing commanding views of dead city below. Hilltop meeting location sized for two combatants. Natural landscape scale beyond urban ruins.

## Environmental Anchors
- Hilltop meeting location east of city
- Eastern boundary of dead city
- Vantage points overlooking urban ruins
- Natural hill slopes and ridges
- Open outdoor terrain beyond city limits

## Descriptive Noun Phrases
Elevated natural terrain, hilltop meeting point, eastern city boundary, open outdoor landscape, elevated vantage position, natural hill slopes, terrain beyond ruins, hillside approach routes, elevated meeting ground, natural landscape features

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
