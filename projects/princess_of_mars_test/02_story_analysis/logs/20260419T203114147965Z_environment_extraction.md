# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:31:14.147965+00:00
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

# Chapter Summary: CHAPTER XVI - WE PLAN ESCAPE

## Story Events
1. **Arrival in Thark:** The expedition enters the ancient city after a 30-day journey from Korad. No enthusiastic welcome occurs, but interest is aroused by the captives (John and Dejah).
2. **Housing Assignment:** John Carter is assigned a large building near the plaza. He searches for Sola and her charges before locating Woola in his quarters.
3. **Confrontation with Dejah Thoris:** John enters Dejah's apartment to propose an escape plan. He confesses his love ("I am yours, body and soul") and commands her obedience until she is safe at her father's court. She accepts his service but warns against gratitude influencing her sentiments.
4. **Threat Revealed:** Sola reports that Sarkoja has been seen at Tal Hajus's quarters. The hordes plan to throw John and Dejah to wild calots in the arena during yearly games.
5. **Escape Plan Formulated:** John proposes a supreme effort to escape. Dejah draws a map of Barsoomian territory on the marble floor using a diamond, identifying waterways and cities. They decide to take a northern waterway route to avoid suspicion.
6. **Departure Attempt:** Sola rides one thoat; John and Dejah ride the other. John leaves Thark via back gates with his animals but is discovered by warriors leaving the city (plan compromised).
7. **Return and Discovery:** John returns to Dejah's quarters via courtyards and rooftops. He overhears a conversation between a chieftain and warriors who plan to capture him upon his return, disarm him, and chain him in vaults beneath the jeddak's quarters. Sarkoja is credited with saving Dejah for Tal Hajus.

## Visual Continuity Details
- **Map Drawing:** A diamond is used to draw lines on marble floor representing waterways (straight lines) and cities (circles). Helium is pointed out far northwest.
- **Architecture Traversal:** John moves through hollow courts within buildings, crossing doorways of magnificent scale designed for large beasts. He climbs winding runways to second-story windows.
- **Animal Behavior:** Thoats and zitidars move restlessly in paddocks; bulls emit sharp squeals or grunt low gutturals. Animals are fed bits of food at gates.
- **Lighting Conditions:** Scenes occur under the approaching gloom of sunset or moonlight flooding the room. The red sun disappears behind the horizon during Sola's search.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XVI

## thark_city
- Role: Primary setting
- Architecture: Ancient city with hollow courts, magnificent doorways for large beasts, winding runways to second-story windows
- Lighting: Approaching sunset gloom, moonlight flooding rooms, red sun disappearing behind horizon
- Atmosphere: Red Barsoomian landscape visible in distance (Helium northwest)
- Scale: Large-scale architecture designed for thoats, zitidars, bulls

## john_quarters
- Role: Secondary setting
- Architecture: Large building near plaza, courtyards within buildings
- Lighting: Interior rooms with sunset approaches
- Atmosphere: Restless animal activity in paddocks, gates where animals fed

## dejah_apartment
- Role: Secondary setting
- Architecture: Apartment quarters with marble floor
- Lighting: Moonlight flooding room
- Atmosphere: Private quarters for escape planning

## courtyards_rooftops
- Role: Transit setting
- Architecture: Courtyards, doorways, rooftops connecting buildings
- Lighting: Approaching gloom of sunset
- Atmosphere: Movement through hollow courts, climbing winding runways

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_city

[[SECTION markdown]]
# Thark City - Ancient Barsoomian Metropolis

## Environment Role
Primary setting for chapter arrival and housing assignment scenes.

## Architecture & Geography
Ancient city with hollow courts within buildings, magnificent doorways designed for large beasts (thoats, zitidars, bulls), winding runways to second-story windows, back gates for departure attempts. City plaza visible near John's quarters.

## Lighting & Atmosphere
Approaching gloom of sunset under red Barsoomian sky, moonlight flooding interior rooms, red sun disappearing behind horizon during Sola's search scenes. Interior spaces with approaching evening light conditions.

## Scale Cues
Large-scale architecture designed for animal movement, hollow courts within multi-story buildings, winding runways connecting floors, gates sized for animal feeding and passage.

## Recurring Environmental Anchors
- Marble floor in Dejah's apartment (diamond drawing surface)
- Paddocks where animals move restlessly
- Gates where animals are fed bits of food
- Courtyards within building structures
- Rooftops connecting to adjacent buildings

## Descriptive Noun Phrases
Ancient Barsoomian city, hollow courts within buildings, magnificent beast doorways, winding second-story runways, red sunset gloom, moonlit interior rooms, plaza near quarters, back departure gates, animal feeding gates, rooftop courtyards.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: john_quarters

[[SECTION markdown]]
# John's Quarters - Large Building Near Plaza

## Environment Role
Secondary setting for housing assignment and animal discovery scenes.

## Architecture & Geography
Large building near city plaza, courtyards within building structure, doorways of magnificent scale, interior rooms with marble surfaces, winding runways to second-story windows.

## Lighting & Atmosphere
Interior rooms under approaching sunset gloom, moonlight flooding room spaces, red sun disappearing behind horizon during search sequences. Evening light conditions throughout.

## Scale Cues
Large-scale architecture designed for animal movement and passage, hollow courts within multi-story buildings, gates sized for animal feeding and passage.

## Recurring Environmental Anchors
- Paddocks where animals move restlessly (thoats, zitidars)
- Gates where animals are fed bits of food
- Bull quarters with sharp squeals or low gutturals
- Courtyards within building structure
- Doorways connecting to adjacent buildings

## Descriptive Noun Phrases
Large plaza building, hollow courtyard spaces, magnificent beast doorways, animal paddocks, feeding gates, second-story windows, winding runways, evening light interiors.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dejah_apartment

[[SECTION markdown]]
# Dejah's Apartment - Private Quarters with Marble Floor

## Environment Role
Secondary setting for escape plan formulation and confrontation scenes.

## Architecture & Geography
Apartment quarters with marble floor surface, interior rooms with diamond drawing capability, private quarters accessible via courtyards and rooftops, winding runways to second-story windows.

## Lighting & Atmosphere
Moonlight flooding room spaces, approaching sunset gloom under red Barsoomian sky, interior evening light conditions during escape planning scenes.

## Scale Cues
Interior rooms designed for human movement, marble floor surface large enough for diamond drawing of waterways and cities, doorways connecting to courtyards.

## Recurring Environmental Anchors
- Marble floor with diamond drawing lines (waterways straight, cities circles)
- Interior room spaces for private conversation
- Courtyard access points
- Rooftop connections to adjacent buildings
- Doorways of magnificent scale

## Descriptive Noun Phrases
Marble floor apartment, diamond drawing surface, moonlit interior rooms, courtyard access doorways, winding second-story runways, evening light quarters, private escape planning space.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: courtyards_rooftops

[[SECTION markdown]]
# Courtyards and Rooftops - Transit Movement Spaces

## Environment Role
Transit setting for movement between buildings and escape attempts.

## Architecture & Geography
Courtyards within building structures, doorways connecting buildings, rooftops linking adjacent structures, winding runways to second-story windows, hollow courts within multi-story buildings.

## Lighting & Atmosphere
Approaching gloom of sunset throughout transit spaces, moonlight flooding movement paths, red sun disappearing behind horizon during rooftop sequences. Evening light conditions for all transit scenes.

## Scale Cues
Large-scale architecture designed for animal and human passage, hollow courts within multi-story buildings, winding runways connecting floors, gates sized for animal feeding and passage.

## Recurring Environmental Anchors
- Hollow courts within building structures
- Doorways of magnificent scale for large beasts
- Winding runways to second-story windows
- Courtyards connecting adjacent buildings
- Rooftops linking building structures
- Gates where animals are fed bits of food

## Descriptive Noun Phrases
Hollow courtyard spaces, magnificent beast doorways, winding second-story runways, rooftop connections, evening light transit paths, courtyard movement spaces, hollow multi-story courts.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
