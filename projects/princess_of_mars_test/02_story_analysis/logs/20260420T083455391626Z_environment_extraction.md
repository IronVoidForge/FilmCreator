# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:34:55.391626+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH026

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- keep the environment set small and useful

- use concise visible descriptions



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter XXVI Summary: "Through Carnage to Joy"

## Key Events

### Naval Victory
- Tars Tarkas and Kantos Kan return reporting Zodanga completely reduced; forces destroyed or captured
- Fleet of 250 battleships carrying 100,000 green warriors sails from dock buildings
- Lesser hordes (40,000 green warriors) left behind looting and destroying stricken city with torches applied in 100 places

### Air Battle Engagement
- Helium's scarlet and yellow towers sighted; Zodangan fleet rises to meet them
- Green Martian warriors open fire on Zodangans with uncanny marksmanship
- First real air battle witnessed - Heliumite squadron defeats Zodangan fleet
- Zodangan battleships torn apart, crews plunging toward ground 1000 feet below
- Commander of entire Zodangan fleet takes fearful plunge indicating surrender

### Princess Dejah Thoris Transfer
- John Carter signals flagship that Princess Dejah Thoris is on board
- Helium's colors break from upper works as they acclaim the Princess
- Dejah Thoris boards flagship and receives officers with grace
- She introduces John Carter, saying "Helium owes her princess as well as her victory today"
- Officers impressed by his win of Thark aid for liberation campaign

### Land Campaign Continues
- Transports with thoats unloaded over difficult terrain (slings required)
- Land attack on Zodangan camp begins from three directions (north, south, east)
- Helium armies arrive at noon, crushing Zodangans between two millstones
- Carnage ceases, prisoners marched to Helium

### Triumphal Entry
- Entry into greater city as huge triumphal procession of conquering heroes
- City goes mad with joy; women and children line broad avenues
- Tharks cause wildest excitement - first armed body of green warriors enter as friends
- John Carter's name loudly cried, loads of ornaments fastened on him and Woola

### Palace Reception
- Meet Tardos Mors, Jeddak of Helium at palace steps
- Tars Tarkas speaks words of friendship between races
- Mors Kajak (father of Dejah Thoris) expresses deep emotion and gratitude
- Both rulers exchange formal greetings establishing new friendship between Tharks and Heliumites

## Characters Introduced/Featured

### Primary Characters
- **John Carter**: Hero, Jeddak of Helium, won Princess Dejah Thoris's liberation
- **Tars Tarkas**: Jeddak of Thark, great warrior and statesman of Barsoom
- **Dejah Thoris**: Princess of Helium, daughter of Mors Kajak
- **Tardos Mors**: Jeddak of Helium, grandfather of Dejah Thoris
- **Mors Kajak**: Jed of lesser Helium, father of Dejah Thoris

### Supporting Characters
- **Kantos Kan**: Green warrior companion
- **Woola**: John Carter's fierce Thark companion
- **Zodangan Fleet Commanders**: Vanquished enemy forces

## Settings and Locations

### Cities
- **Helium (Greater)**: Scarlet and yellow towers, main city of victory
- **Helium (Lesser)**: Secondary city with Mors Kajak as Jed
- **Stricken City**: Zodangan territory being destroyed by lesser hordes

### Military Installations
- **Dock Buildings**: Fleet departure point
- **Ancient Sea Bottom**: Where crashed battleships land
- **Palace Grounds**: Reception area for triumphant heroes

## Character Relationships Established

- John Carter and Dejah Thoris: Hero-princess bond, mutual respect
- Tars Tarkas and Helium Rulers: New friendship between Tharks and Heliumites
- Mors Kajak and John Carter: Father's deep emotion over daughter's liberation
- Green Warriors and Helium Citizens: First time entering as friends rather than enemies

## Military Significance

- Naval victory establishes Thark-Helium alliance
- Air battle demonstrates uncanny Martian marksmanship
- Land campaign completes liberation of Princess Dejah Thoris
- Surrender customs honored (commander's voluntary plunge)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - Chapter XXVI "Through Carnage to Joy"

## Helium Greater City
- **asset_id**: helium_greater_city
- **role**: primary setting
- **description**: Main city of victory with scarlet and yellow towers, palace grounds for reception

## Stricken Zodangan Territory
- **asset_id**: stricken_zodangan_territory
- **role**: secondary setting
- **description**: Zodangan territory being destroyed by lesser hordes with torches applied in 100 places

## Dock Buildings
- **asset_id**: dock_buildings
- **role**: transit setting
- **description**: Fleet departure point for 250 battleships carrying 100,000 green warriors

## Palace Grounds
- **asset_id**: palace_grounds
- **role**: primary setting
- **description**: Reception area for triumphant heroes with formal greetings between rulers

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_greater_city



[[SECTION markdown]]

# Helium Greater City

**Role**: Primary setting - main city of victory and triumphal entry location

**Architecture/Geography**: Scarlet and yellow towers dominate the skyline; broad avenues lined with women and children; palace grounds at upper works for formal receptions

**Lighting/Atmosphere**: Daylight celebration atmosphere; city goes mad with joy; triumphant procession lighting suggests midday to afternoon timing

**Scale Cues**: Huge triumphal procession of conquering heroes; fleet of 250 battleships visible from dock buildings; ancient sea bottom nearby for crashed ships

**Environmental Anchors**: Towers, palace steps, broad avenues, dock departure point, ancient sea bottom access

**Descriptive Noun Phrases**: Victory city skyline, triumphant procession route, palace reception grounds, scarlet tower spires, yellow tower structures, liberated princess welcome area

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: stricken_zodangan_territory



[[SECTION markdown]]

# Stricken Zodangan Territory

**Role**: Secondary setting - destroyed enemy territory and transit zone for lesser hordes

**Architecture/Geography**: Stricken city under active destruction; torches applied in 100 places across the landscape; ancient sea bottom where crashed battleships land

**Lighting/Atmosphere**: Destructive atmosphere with fire and torchlight; carnage scene with green warriors looting and destroying; ominous post-battle lighting

**Scale Cues**: Lesser hordes of 40,000 green warriors operating across territory; multiple crash sites from torn apart battleships; ground 1000 feet below for plunging crews

**Environmental Anchors**: Torch-lit destruction zones, crashed battleship wreckage, ancient sea bottom landing areas, fleeing enemy remnants

**Descriptive Noun Phrases**: Destroyed Zodangan cityscape, torch-lit ruin zones, crashed battleship debris fields, looting green warrior hordes, ancient sea bottom crash sites

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dock_buildings



[[SECTION markdown]]

# Dock Buildings

**Role**: Transit setting - fleet departure point for naval victory operations

**Architecture/Geography**: Large dock structures capable of housing 250 battleships; loading areas for green warriors and supplies; maritime infrastructure at city edge

**Lighting/Atmosphere**: Daylight departure scene; bustling military activity; celebratory atmosphere as fleet sails from dock buildings

**Scale Cues**: Massive fleet capacity with 100,000 green warriors aboard; battleship docking bays; transport vessels for land campaign equipment

**Environmental Anchors**: Dock building structures, fleet departure ramps, loading platforms, maritime access points to ancient sea bottom

**Descriptive Noun Phrases**: Fleet departure docks, battleship loading areas, green warrior embarkation zones, naval victory staging ground, maritime infrastructure

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: palace_grounds



[[SECTION markdown]]

# Palace Grounds

**Role**: Primary setting - formal reception area for triumphant heroes and diplomatic greetings

**Architecture/Geography**: Palace steps at upper works; formal reception grounds for rulers; grand ceremonial architecture for state occasions

**Lighting/Atmosphere**: Daylight formal ceremony; celebratory lighting with city joy visible from palace; dignified atmosphere for ruler-to-ruler greetings

**Scale Cues**: Formal gathering of Jeddak Tardos Mors and Jed Mors Kajak; large enough for triumphal procession entry; palace grounds accommodate multiple rulers

**Environmental Anchors**: Palace steps, upper works viewing areas, formal reception platforms, city view from palace grounds

**Descriptive Noun Phrases**: Palace reception steps, ruler greeting platforms, formal ceremony grounds, upper works viewing areas, diplomatic reception zones

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_sea_bottom



[[SECTION markdown]]

# Ancient Sea Bottom

**Role**: Secondary setting - crash landing zone and maritime transition area

**Architecture/Geography**: Submerged or low-lying sea floor where crashed battleships land; ancient seabed terrain with natural formations

**Lighting/Atmosphere**: Dim underwater or twilight lighting; mysterious ancient atmosphere; post-battle wreckage scene

**Scale Cues**: Multiple crashed battleship landing sites; ground 1000 feet below for plunging crews; vast sea bottom expanse

**Environmental Anchors**: Crashed battleship wrecks, ancient seabed formations, water access points, maritime crash zones

**Descriptive Noun Phrases**: Ancient seabed terrain, crashed battleship wreckage fields, underwater landing zones, maritime crash sites, submerged battle debris

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: lesser_helium_city



[[SECTION markdown]]

# Lesser Helium City

**Role**: Secondary setting - secondary city with Mors Kajak as Jed

**Architecture/Geography**: Smaller city district separate from greater Helium; residential and administrative areas for lesser Jed territory

**Lighting/Atmosphere**: Daylight celebration atmosphere; joyous reception lighting; intimate scale compared to greater city

**Scale Cues**: Secondary city size with Mors Kajak as Jed; smaller than greater Helium but still significant; family home reception area

**Environmental Anchors**: Lesser city districts, residential areas, administrative buildings, family residence grounds

**Descriptive Noun Phrases**: Secondary city district, lesser Jed territory, family reception areas, intimate celebration zones, residential city sections

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: transit_terrain



[[SECTION markdown]]

# Transit Terrain

**Role**: Transit setting - difficult terrain for land campaign operations

**Architecture/Geography**: Difficult terrain requiring slings for transport; rough ground for thoat movement and army marches

**Lighting/Atmosphere**: Daylight military march atmosphere; dusty or rocky terrain lighting; active campaign conditions

**Scale Cues**: Land attack from three directions (north, south, east); transports with thoats unloaded over difficult terrain; army marching routes

**Environmental Anchors**: Rough ground sections, sling operation points, army march routes, transport unloading zones

**Descriptive Noun Phrases**: Difficult campaign terrain, rough ground sections, sling operation areas, army march routes, transport unloading zones

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: victory_procession_route



[[SECTION markdown]]

# Victory Procession Route

**Role**: Primary setting - triumphal procession path through greater city

**Architecture/Geography**: Broad avenues through greater Helium; ceremonial route for conquering heroes entering city

**Lighting/Atmosphere**: Daylight celebration atmosphere; city-wide joy lighting with crowds lining routes; triumphant procession lighting

**Scale Cues**: Huge triumphal procession of conquering heroes; women and children line broad avenues; loads of ornaments fastened on John Carter and Woola

**Environmental Anchors**: Broad avenue sections, crowd-lined route segments, ornament display areas, city entry points

**Descriptive Noun Phrases**: Triumphal procession route, broad avenue celebration paths, crowd-lined victory routes, ornament display zones, conquering hero entry paths

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
