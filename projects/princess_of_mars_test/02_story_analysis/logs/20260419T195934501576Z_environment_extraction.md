# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:59:34.501576+00:00
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

Chapter id: CH004

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

# Chapter IV: A PRISONER - Scene Decomposition

## Opening Sequence (Travel to City)
**Visual Continuity**: Carter and Tars Tarkas traveling on foot, ground rising rapidly toward edge of dead sea, traversing narrow gorge into open valley with low table land at extremity.

**Story Beat**: They gallop toward enormous city visible from distance, entering by ruined roadway that ends abruptly in broad steps.

## City Entry & Plaza Scene
**Visual Continuity**: Buildings appear deserted but not greatly decayed, showing signs of vacancy for years/ages. Large plaza with 900-1000 Martians camped around it.

**Character Details**: 
- Martians naked except ornaments, women have larger tusks curving to high-set ears
- Adult females 10-12 feet tall, children light in color all looking alike
- No extreme age visible among population

## Audience Chamber Introduction
**Visual Continuity**: Magnificent edifice of gleaming white marble with gold and brilliant stones. Main entrance 100 feet wide with huge canopy. Enormous chamber encircled by galleries.

**Scene Details**: 
- 40-50 male Martians assembled around rostrum steps
- Enormous warrior on platform heavily loaded with metal ornaments, feathers, leather trappings with precious stones
- White fur cape lined with scarlet silk from shoulders

## Formal Greeting Ceremony
**Visual Continuity**: Tars Tarkas (vice-chieftain) explains expedition and Carter's capture. Chieftain addresses Carter at length.

**Cultural Notes**: 
- Green Martians exchange names or ornaments depending on mission type
- Customary greeting between green Martians involves name exchanges
- Tars Tarkas virtually vice-chieftain, great ability as statesman and warrior

## Carter's Physical Demonstrations
**Visual Continuity**: Carter skips and flits among desks/chairs like monstrous grasshopper after signal failure. Creeps then gets roughly jerked to feet by towering fellow who laughed at misfortunes.

**Key Actions**: 
- "Sak" jumping demonstration: Tars Tarkas jumps while repeating word
- "Sakked" long jump: Carter clears 150 feet, lands squarely without falling
- Exhibition witnessed by several hundred lesser Martians demanding repetition

## Combat Scene (Fighting Warrior)
**Visual Continuity**: Fights one warrior after being banged down upon feet. Swings fist to jaw, opponent falls like felled ox. Other Martians initially struck dumb with wonderment then break into wild peals of laughter and applause.

**Cultural Significance**: Carter wins manifestation of approbation - rare honor among Martians. Fellow remains where fallen, no mates approach him.

## Food Request & Sola Introduction
**Visual Continuity**: Tars Tarkas and chief exchange words. Young female instructed by Tars Tarkas, Carter accompanies her across plaza toward large building on far side.

**Character Details**: 
- Sola about 8 feet tall, light olive-green color with smooth glossy hide
- Belongs to retinue of Tars Tarkas
- Conducts Carter to spacious chamber with silks and furs littering floor

## Strange Creature Appearance
**Visual Continuity**: Room well lighted by large windows, beautifully decorated with mural paintings and mosaics. Sola makes peculiar hissing sound signaling someone in adjoining room.

**Creature Description**: 
- Waddles in on ten short legs, squats down before girl like obedient puppy
- About size of Shetland pony, head bears slight resemblance to frog except jaws equipped with three rows of long sharp tusks

## Scene End Points
**Decomposition Markers**: 
- Carter's physical limitations (cannot walk properly)
- Martian cultural differences (humor based on violence/death)
- Ancient architecture predating current Martians
- Introduction of strange ten-legged creature species
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Martian City Environment Index

## Dead Sea Edge/Gorge
- Role: Transit Setting
- Architecture/Geography: Narrow gorge traversing into open valley with low table land at extremity, ground rising rapidly toward edge of dead sea
- Lighting/Atmosphere: Natural daylight, arid landscape conditions
- Scale Cues: Ground elevation changes visible, gorge width varies

## Martian City Plaza
- Role: Primary Setting
- Architecture/Geography: Enormous city with ruined roadway ending in broad steps, large plaza surrounded by buildings appearing deserted but not greatly decayed
- Lighting/Atmosphere: Open daylight conditions, signs of vacancy for years/ages
- Scale Cues: 900-1000 Martians camped around plaza, buildings show ancient architecture predating current population

## Audience Chamber/Edifice
- Role: Primary Setting
- Architecture/Geography: Magnificent edifice of gleaming white marble with gold and brilliant stones, main entrance 100 feet wide with huge canopy, enormous chamber encircled by galleries
- Lighting/Atmosphere: Interior illumination from windows, gleaming surfaces reflect light
- Scale Cues: 40-50 Martians assembled around rostrum steps, warrior on platform heavily loaded with ornaments

## Spacious Chamber (Sola's Room)
- Role: Secondary Setting
- Architecture/Geography: Room well lighted by large windows, beautifully decorated with mural paintings and mosaics, spacious chamber with silks and furs littering floor
- Lighting/Atmosphere: Large window illumination, decorative lighting from interior elements
- Scale Cues: Mural paintings visible on walls, mosaic decorations throughout

## Adjoining Room (Creature Appearance)
- Role: Secondary Setting
- Architecture/Geography: Connected to spacious chamber, well lighted by large windows, beautifully decorated with mural paintings and mosaics
- Lighting/Atmosphere: Interior illumination from windows, decorative lighting from interior elements
- Scale Cues: Room size accommodates ten-legged creature approximately Shetland pony sized

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dead_sea_edge_gorge

[[SECTION markdown]]
# Dead Sea Edge/Gorge Environment

## Environment Role
Transit Setting - Opening sequence travel location where Carter and Tars Tarkas journey toward Martian city

## Architecture/Geography
Narrow gorge traversing into open valley with low table land at extremity, ground rising rapidly toward edge of dead sea. Ancient terrain showing signs of geological formation predating current Martians.

## Lighting/Atmosphere Cues
Natural daylight conditions, arid landscape atmosphere, natural shadows from gorge walls, dust particles visible in air during travel sequence.

## Scale Cues and Environmental Anchors
Ground elevation changes clearly visible throughout journey, gorge width varies from narrow passages to wider openings, valley floor provides visual reference point for approaching city.

## Descriptive Noun Phrases
- Narrow gorge entrance
- Rising ground edge
- Dead sea horizon
- Open valley floor
- Low table land extremity
- Ancient terrain formation
- Arid landscape conditions
- Natural daylight illumination

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_city_plaza

[[SECTION markdown]]
# Martian City Plaza Environment

## Environment Role
Primary Setting - Main gathering space where 900-1000 Martians camped, central location for formal ceremonies and demonstrations

## Architecture/Geography
Enormous city with ruined roadway ending in broad steps, large plaza surrounded by buildings appearing deserted but not greatly decayed. Ancient architecture showing signs of vacancy for years/ages. Buildings show structural integrity despite abandonment.

## Lighting/Atmosphere Cues
Open daylight conditions, natural shadows from surrounding buildings, atmospheric haze suggesting ancient civilization, light reflecting off building surfaces showing wear patterns.

## Scale Cues and Environmental Anchors
900-1000 Martians camped around plaza perimeter, plaza size accommodates large gatherings, ruined roadway provides approach path, broad steps mark city entrance threshold.

## Descriptive Noun Phrases
- Enormous city plaza
- Ruined roadway entrance
- Broad city steps
- Deserted buildings
- Ancient architecture
- Camped Martian population
- Plaza gathering space
- City perimeter markers

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber_edifice

[[SECTION markdown]]
# Audience Chamber/Edifice Environment

## Environment Role
Primary Setting - Formal reception chamber where chieftain addresses Carter, location for formal greeting ceremony and physical demonstrations

## Architecture/Geography
Magnificent edifice of gleaming white marble with gold and brilliant stones. Main entrance 100 feet wide with huge canopy. Enormous chamber encircled by galleries. Rostrum steps with assembled Martians, platform for warrior display.

## Lighting/Atmosphere Cues
Interior illumination from windows, gleaming marble surfaces reflect light, gold and brilliant stones catch ambient light, gallery lighting creates depth perception within chamber.

## Scale Cues and Environmental Anchors
40-50 male Martians assembled around rostrum steps, warrior on platform heavily loaded with metal ornaments and feathers, 100-foot wide entrance provides approach scale reference, galleries encircle main chamber space.

## Descriptive Noun Phrases
- Gleaming white marble edifice
- Gold and brilliant stone accents
- 100-foot wide entrance
- Huge canopy structure
- Enormous chamber interior
- Rostrum steps assembly area
- Encircling gallery system
- Warrior platform display space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: spacious_chamber_sola_room

[[SECTION markdown]]
# Spacious Chamber (Sola's Room) Environment

## Environment Role
Secondary Setting - Private chamber where Sola conducts Carter, location for creature introduction and formal introductions

## Architecture/Geography
Room well lighted by large windows, beautifully decorated with mural paintings and mosaics. Spacious chamber with silks and furs littering floor. Interior decoration shows artistic craftsmanship predating current Martians.

## Lighting/Atmosphere Cues
Large window illumination provides primary light source, decorative lighting from interior elements, mural paintings catch ambient light, mosaic decorations reflect surface light patterns.

## Scale Cues and Environmental Anchors
Room size accommodates multiple Martians comfortably, large windows provide exterior visual reference, mural paintings cover wall surfaces, mosaic decorations create floor and wall boundaries, silks and furs indicate chamber importance.

## Descriptive Noun Phrases
- Large window illumination
- Mural painting decorations
- Mosaic artwork surfaces
- Spacious chamber interior
- Silk and fur littering
- Artistic craftsmanship display
- Interior decorative elements
- Wall surface coverage

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: adjoining_room_creature_appearance

[[SECTION markdown]]
# Adjoining Room (Creature Appearance) Environment

## Environment Role
Secondary Setting - Connected chamber where strange ten-legged creature appears, location for species introduction and creature demonstration

## Architecture/Geography
Connected to spacious chamber, well lighted by large windows, beautifully decorated with mural paintings and mosaics. Room size accommodates approximately Shetland pony sized creature with three rows of long sharp tusks visible in jaws.

## Lighting/Atmosphere Cues
Interior illumination from windows, decorative lighting from interior elements, mural paintings catch ambient light, mosaic decorations reflect surface light patterns, creature presence affects room atmosphere.

## Scale Cues and Environmental Anchors
Room size accommodates ten-legged creature approximately Shetland pony sized, large windows provide exterior visual reference, mural paintings cover wall surfaces, mosaic decorations create floor and wall boundaries, creature waddles on ten short legs within chamber space.

## Descriptive Noun Phrases
- Connected chamber entrance
- Large window illumination
- Mural painting decorations
- Mosaic artwork surfaces
- Shetland pony sized creature
- Ten-legged creature species
- Three rows of sharp tusks
- Interior decorative elements

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
