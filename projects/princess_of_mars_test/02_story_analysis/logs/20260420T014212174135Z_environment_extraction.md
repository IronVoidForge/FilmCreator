# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:42:12.174135+00:00
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

Chapter id: CH026

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
Carter and Tars Tarkas report Zodanga fleet destroyed; Dejah Thoris transferred to Helium flagship. Land forces attack Zodangan army from north, south, east. Helium navy joins land battle against million-strong enemy. Victory parade in Helium city. Carter introduced to Jeddak of Helium (Tardos Mors) and Jed of lesser Helium (Mors Kajak).

**Visual Continuity Facts:**
Sky ships circling above fleets; green warriors firing small arms from shelters; explosions on Zodangan hulls; bodies plunging from defeated ships into loam. Thoats in slings landing near city gates. Palace steps with royal party; crowd lining avenues. Helium towers visible against sky.

**Scene Decomposition Notes:**
Naval battle sequence ends with surrender customs (commander plunge). Land battle sequence involves coordinated charge with Helium reinforcements. Political resolution scene occurs on palace steps and main portals.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Helium Flagship (naval battle primary setting)
# Zodangan Fleet Ships (enemy naval secondary setting)
# Helium City Palace Steps (political resolution primary setting)
# Sky Above Fleets (transit observation secondary setting)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: helium_flagship

[[SECTION markdown]]
Helium flagship serves as primary naval battle setting during fleet engagement. Architecture features large open deck spaces with reinforced hull plating and command stations positioned along perimeter railings. Lighting dominated by natural daylight filtering through clear sky above, supplemented by artificial floodlights mounted on superstructure. Atmosphere carries tension of active combat with smoke from explosions drifting across deck surface. Scale indicated by massive ship dimensions relative to smaller skiff craft visible in distance. Recurring environmental anchors include main command bridge entrance marked by royal insignia and cargo hold access points along starboard side. Descriptive noun phrases: reinforced hull plating, command stations, perimeter railings, smoke from explosions, cargo hold access points, royal insignia markers.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodangan_fleet_ships

[[SECTION markdown]]
Zodangan fleet ships function as secondary enemy naval setting during battle sequence. Architecture consists of angular hull designs with weapon emplacements mounted on upper decks and cargo bays accessible through reinforced bulkhead doors. Lighting characterized by harsh direct sunlight creating strong shadows across deck surfaces, with occasional smoke haze from combat damage reducing visibility. Atmosphere marked by defeated ship debris floating in air and bodies plunging into loam below waterline. Scale conveyed by multiple ships visible in formation with smaller skiff craft circling above hulls. Recurring environmental anchors include main weapon emplacements along port side and emergency escape hatches positioned near command stations. Descriptive noun phrases: angular hull designs, weapon emplacements, reinforced bulkhead doors, smoke haze from combat damage, loam below waterline, emergency escape hatches.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: helium_city_palace_steps

[[SECTION markdown]]
Helium city palace steps serve as primary political resolution setting for victory parade and royal introductions. Architecture features grand staircase leading to main palace portals with wide avenues flanking both sides, decorated with ceremonial banners hanging from overhead structures. Lighting provided by natural daylight creating bright illumination on stone surfaces, with shadows cast by palace towers visible against sky background. Atmosphere carries celebratory mood with crowd lining avenues and royal party positioned on upper steps. Scale indicated by towering palace structures rising above city skyline and wide avenue spaces accommodating large crowds. Recurring environmental anchors include main palace entrance marked by royal insignia and ceremonial banners hanging from overhead structures along avenue edges. Descriptive noun phrases: grand staircase, main palace portals, wide avenues, ceremonial banners, stone surfaces, palace towers, royal party positioning.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: sky_above_fleets

[[SECTION markdown]]
Sky above fleets functions as secondary transit observation setting for naval battle sequences. Architecture consists of open atmospheric space with no physical structures, serving as observation platform for sky ships circling above fleet formations. Lighting dominated by clear daylight conditions with minimal cloud cover, creating bright visibility across entire battlefield below. Atmosphere marked by smoke from explosions drifting upward and bodies plunging into loam visible from elevated perspective. Scale conveyed by vast open sky contrasting with smaller ship hulls below and distant city skyline on horizon. Recurring environmental anchors include distant Helium towers visible against sky background and fleet formations positioned below observation level. Descriptive noun phrases: open atmospheric space, clear daylight conditions, smoke from explosions drifting upward, bodies plunging into loam, distant Helium towers, fleet formations below.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
