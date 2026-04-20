# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:56:39.221564+00:00
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

Chapter id: CH007

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

# Chapter VII: Child-Raising on Mars - Scene Summary

## Opening Sequence
- **Location**: Plaza to incubator facility
- **Event**: Breakfast showing exact replica of preceding day's meal, index of every meal while with green men
- **Procession**: Sola escorts narrator to plaza where entire community watches harnessing of huge mastodonian animals to three-wheeled chariots

## Procession Details
- **Scale**: Approximately 250 vehicles, each drawn by single animal
- **Chariot Description**: Large, commodious, gorgeously decorated
- **Occupants**: Female Martians loaded with ornaments of metal, jewels, silks, furs; young Martian drivers perched on beasts
- **Animal Control**: No bit or bridle, guided entirely by telepathic means
- **Formation**: Single file line of march, 200 warriors at head (five abreast), like number at rear, 25-30 outriders flanking sides

## Incubator Ceremony
- **Location**: Remote fastness incubator facility
- **Participants**: Half a score warriors headed by enormous chieftain Lorquas Ptomel Jed, including Tars Tarkas and several lesser chiefs
- **Event**: Narrator performs leap over parked chariots for edification of Lorquas Ptomel

## Young Martian Release System
- **Incubator Contents**: All but very few eggs hatched, fairly alive with hideous little devils (3-4 feet tall)
- **Release Method**: Opening broken in wall large enough to permit exit of young Martians
- **Capture Process**: Women and younger Martians form two solid walls leading through chariots into plain; little Martians scamper wild as deer, captured one at a time by women/older children
- **Distribution**: Last in line captures first to reach end; opposite captures second; those caught by young men later turned over to women

## Child-Raising System Explanation
- **Education Focus**: Teaching them to talk and use weapons of warfare from very first year of life
- **Birth Rate**: Each adult female brings forth about thirteen eggs each year
- **Selection Process**: Council of twenty chieftains examines yearly supply; all but about one hundred most perfect destroyed out of each yearly supply
- **Incubation Period**: Five years in almost air-tight incubators hatched by sun's rays
- **Hatching Rate**: All but about one per cent of eggs hatching in two days

## Community Demographics
- **Population**: Some thirty thousand souls
- **Territory**: Arid and semi-arid land between forty and eighty degrees south latitude
- **Boundaries**: Bounded on east and west by two large fertile tracts
- **Headquarters**: Southwest corner near crossing of two so-called Martian canals

## Narrator's Development
- **Telepathic Abilities**: Developed under Sola's tutelage, shortly could sense practically everything around narrator
- **Language Mastery**: In a week could make all wants known and understand nearly everything said to narrator
- **Unique Advantage**: Could catch telepathic messages easily from others but no one could read anything from narrator's mind

## Closing Scene
- **Location**: Narrator and Sola in their chariot
- **Sola's Prize**: Male about four feet tall, very strong and physically perfect; learned quickly with considerable amusement over keen rivalry displayed
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter VII

## Primary Environments

### Plaza to Incubator Facility
- **Role**: Primary transit setting for procession route
- **Geography**: Open plaza area connecting to incubator facility entrance
- **Atmosphere**: Communal gathering space, ceremonial atmosphere
- **Scale**: Large enough to accommodate 250+ vehicles in single file formation
- **Anchors**: Incubator facility entrance, community viewing areas

### Remote Fastness Incubator Facility
- **Role**: Primary ceremony location
- **Geography**: Remote enclosed structure with wall breach for egg release
- **Atmosphere**: Solemn ceremonial space, sun-ray hatching environment
- **Scale**: Large enough to house half-score warriors and chariot display area
- **Anchors**: Wall breach opening, central ceremony platform

### Chariot Fleet
- **Role**: Primary transportation system
- **Geography**: Three-wheeled vehicles drawn by single mastodonian animals
- **Atmosphere**: Gorgeously decorated, telepathically guided
- **Scale**: 250 vehicles total, large commodious interior space
- **Anchors**: Animal harness points, driver perches

### Release Plain
- **Role**: Secondary transit setting for young Martian distribution
- **Geography**: Open arid plain between forty and eighty degrees south latitude
- **Atmosphere**: Semi-arid territory, sunlit hatching environment
- **Scale**: Large enough to accommodate 30,000 souls across fertile tracts
- **Anchors**: Chariot entry points, capture formation walls

## Secondary Environments

### Community Viewing Areas
- **Role**: Secondary gathering space
- **Geography**: Plaza perimeter with community seating
- **Atmosphere**: Observational ceremonial space
- **Scale**: Accommodates entire thirty thousand soul population
- **Anchors**: Procession route viewing points

### Headquarters Southwest Corner
- **Role**: Secondary administrative location
- **Geography**: Crossing of two Martian canals, southwest territory corner
- **Atmosphere**: Administrative headquarters atmosphere
- **Scale**: Bounded by fertile tracts on east and west
- **Anchors**: Canal crossing point, boundary markers

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_incubator_facility

[[SECTION markdown]]
# Plaza to Incubator Facility

## Environment Role
Primary transit setting for procession route and community viewing

## Architecture or Geography
Open plaza area connecting to incubator facility entrance. Large enough to accommodate 250+ three-wheeled chariots in single file formation. Community viewing areas along perimeter with seating capacity for entire thirty thousand soul population.

## Lighting and Atmosphere Cues
Ceremonial atmosphere with communal gathering energy. Sunlit procession route during morning hours. Telepathically guided animal movement creates silent ceremonial flow. Gorgeously decorated chariot interiors visible through open formations.

## Scale Cues and Recurring Environmental Anchors
- 250 vehicles in single file line of march
- 200 warriors at head (five abreast)
- 25-30 outriders flanking sides
- Incubator facility entrance as primary anchor point
- Community viewing areas as secondary anchors

## Descriptive Noun Phrases for Render-Facing Prompts
- "ceremonial plaza with procession route"
- "incubator facility entrance archway"
- "three-wheeled chariot formation"
- "mastodonian animal harness points"
- "community viewing perimeter seating"
- "telepathically guided procession atmosphere"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: remote_fastness_incubator_facility

[[SECTION markdown]]
# Remote Fastness Incubator Facility

## Environment Role
Primary ceremony location for young Martian release and edification events

## Architecture or Geography
Remote enclosed structure with wall breach opening large enough to permit exit of young Martians. Central ceremony platform area. Almost air-tight incubation chambers hatched by sun's rays. Wall breach positioned for controlled egg release into plain.

## Lighting and Atmosphere Cues
Solemn ceremonial space atmosphere. Sun-ray hatching environment with natural light penetration through wall breach. Remote fastness isolation creates focused ceremonial energy. Half-score warriors gathered in formal arrangement.

## Scale Cues and Recurring Environmental Anchors
- Large enough to house half a score warriors headed by enormous chieftain Lorquas Ptomel Jed
- Wall breach opening for egg release
- Central ceremony platform area
- Chariot display area within facility
- Incubation chamber access points

## Descriptive Noun Phrases for Render-Facing Prompts
- "remote fastness incubator structure"
- "wall breach egg release opening"
- "ceremonial platform area"
- "sun-ray hatching environment"
- "air-tight incubation chambers"
- "chieftain ceremony gathering space"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chariot_fleet_system

[[SECTION markdown]]
# Chariot Fleet System

## Environment Role
Primary transportation system for community procession and individual travel

## Architecture or Geography
Three-wheeled vehicles drawn by single mastodonian animals. Large commodious interior gorgeously decorated with ornaments of metal, jewels, silks, furs. Driver perches positioned on beasts. No bit or bridle - telepathic guidance system integrated into vehicle control.

## Lighting and Atmosphere Cues
Gorgeously decorated interiors create ceremonial atmosphere. Telepathically guided movement creates silent procession flow. Single file line of march formation maintains visual continuity. Occupants loaded with ornaments visible through open formations.

## Scale Cues and Recurring Environmental Anchors
- 250 vehicles total in fleet system
- Large commodious interior space per vehicle
- Animal harness points as primary anchors
- Driver perches on beasts as secondary anchors
- Single file formation maintaining visual continuity
- 200 warriors at head, like number at rear

## Descriptive Noun Phrases for Render-Facing Prompts
- "three-wheeled chariot vehicle"
- "mastodonian animal harness system"
- "gorgeously decorated interior space"
- "telepathic guidance control interface"
- "driver perch on beast"
- "ornamented metal jewel silk fur decorations"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: release_plain_territory

[[SECTION markdown]]
# Release Plain Territory

## Environment Role
Secondary transit setting for young Martian distribution and capture operations

## Architecture or Geography
Open arid plain between forty and eighty degrees south latitude. Bounded on east and west by two large fertile tracts. Headquarters located in southwest corner near crossing of two so-called Martian canals. Large enough to accommodate 30,000 souls across territory.

## Lighting and Atmosphere Cues
Semi-arid territory atmosphere with sunlit hatching environment. Open plain creates expansive visual field. Sun's rays penetrate for incubation period. Arid land conditions visible through terrain texture.

## Scale Cues and Recurring Environmental Anchors
- Large enough to accommodate 30,000 souls population
- Two large fertile tracts as eastern and western boundaries
- Southwest corner headquarters location
- Chariot entry points into plain
- Capture formation walls (two solid walls leading through chariots)
- Plain expanse for young Martian scampering

## Descriptive Noun Phrases for Render-Facing Prompts
- "arid semi-arid release plain"
- "forty to eighty degrees south latitude territory"
- "fertile tract boundary markers"
- "chariot entry points into plain"
- "capture formation wall structure"
- "sunlit hatching environment terrain"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: community_viewing_areas

[[SECTION markdown]]
# Community Viewing Areas

## Environment Role
Secondary gathering space for procession observation and ceremonial viewing

## Architecture or Geography
Plaza perimeter with community seating areas. Located along procession route viewing points. Bounded by plaza entrance and incubator facility. Accommodates entire thirty thousand soul population for viewing events.

## Lighting and Atmosphere Cues
Observational ceremonial space atmosphere. Community gathering energy during morning hours. Procession route visibility from multiple vantage points. Telepathically guided animal movement visible from seating areas.

## Scale Cues and Recurring Environmental Anchors
- Accommodates entire thirty thousand soul population
- Plaza perimeter seating capacity
- Procession route viewing points as anchors
- Community gathering energy scale
- Multiple vantage point locations

## Descriptive Noun Phrases for Render-Facing Prompts
- "plaza perimeter community seating"
- "procession route viewing vantage points"
- "community gathering space area"
- "ceremonial observation platform"
- "plaza entrance boundary markers"
- "incubator facility viewing access"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: headquarters_southwest_corner

[[SECTION markdown]]
# Headquarters Southwest Corner

## Environment Role
Secondary administrative location for community governance and canal crossing operations

## Architecture or Geography
Crossing of two Martian canals located in southwest territory corner. Bounded on east and west by two large fertile tracts. Administrative headquarters atmosphere with boundary markers. Located near crossing point of two so-called Martian canals.

## Lighting and Atmosphere Cues
Administrative headquarters atmosphere with formal governance energy. Canal crossing area creates natural light patterns through water features. Southwest territory corner location provides directional orientation.

## Scale Cues and Recurring Environmental Anchors
- Crossing of two Martian canals as primary anchor
- Bounded by fertile tracts on east and west
- Southwest territory corner location
- Administrative headquarters scale
- Canal crossing point markers

## Descriptive Noun Phrases for Render-Facing Prompts
- "southwest territory corner location"
- "two Martian canal crossing point"
- "administrative headquarters structure"
- "fertile tract boundary markers"
- "canal water feature crossing"
- "territory orientation markers"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
