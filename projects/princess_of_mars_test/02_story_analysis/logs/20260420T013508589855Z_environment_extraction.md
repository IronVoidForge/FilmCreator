# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:35:08.589855+00:00
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

Chapter id: CH022

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

### Story Arc
Carter witnesses Dejah Thoris promising herself to Sab Than before Than Kosis. He abandons his post to confront her in her apartments. After killing her four guards, he reveals himself as John Carter. Dejah Thoris explains she thought him dead and that Barsoomian custom binds her promise to Sab Than despite her true feelings for Carter. Realizing the promise is final by custom, Carter escapes the palace via a balcony and glass wall to avoid detection of his unauthorized presence.

### Visual Continuity
*   Apartment walls hung with tapestries hiding windows/doors.
*   Passage behind tapestries connecting chambers.
*   Antechamber containing four guards accompanying Dejah Thoris.
*   Spiral runway leading to lower floors.
*   Balcony overlooking a broad avenue of Zodanga.
*   Glass wall (20 feet high, polished glass) separating building from avenue.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH022

## Primary Settings
- apartment_dejah_thoris_main

## Secondary/Transit Settings
- antechamber_guards
- spiral_runway_lower_floors
- balcony_zodanga_avenue

---

*Note: All environments listed are stable environment families suitable for render-facing prompt writing. Each includes architecture, lighting, atmosphere, and scale cues.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: apartment_dejah_thoris_main

[[SECTION markdown]]
# Apartment - Dejah Thoris Main Chambers

## Environment Role
Primary setting for chapter confrontation scene.

## Architecture & Geography
- Interior palace apartments with tapestry-covered walls
- Hidden windows and doors concealed by hanging tapestries
- Passage behind tapestries connecting multiple chambers
- Spiral runway access to lower floors
- Balcony with glass wall separation (20 feet high polished glass)

## Lighting & Atmosphere
- Warm interior lighting filtered through tapestries
- Dim ambient light suggesting evening or night
- Polished glass reflecting interior warmth against exterior darkness
- Atmospheric tension from concealed spaces and restricted visibility

## Scale Cues
- Palace-scale architecture with multiple connected chambers
- 20-foot high glass wall separating building from avenue
- Spiral runway indicating multi-level structure
- Broad avenue of Zodanga visible from balcony

## Recurring Environmental Anchors
- Tapestry-covered walls (primary visual anchor)
- Glass wall separation (structural anchor)
- Spiral runway access point (navigation anchor)
- Balcony overlook (perspective anchor)

## Descriptive Noun Phrases for Render Prompts
- tapestry-hung palace apartment interior
- polished glass wall 20 feet high
- spiral runway lower floor access
- concealed chamber passage behind tapestries
- broad avenue of Zodanga exterior view
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: antechamber_guards

[[SECTION markdown]]
# Antechamber - Guard Accompaniment Space

## Environment Role
Secondary/transit setting for guard presence and confrontation.

## Architecture & Geography
- Interior antechamber space within palace apartments
- Contains four Barsoomian guards accompanying Dejah Thoris
- Connected to main apartment chambers via tapestry passages
- Restricted visibility due to tapestry coverage

## Lighting & Atmosphere
- Dim interior lighting consistent with main apartment
- Shadowed corners suggesting concealed spaces
- Tense atmosphere from guard presence and confrontation
- Warm but restricted light filtering through tapestries

## Scale Cues
- Chamber-scale space accommodating four guards comfortably
- Connected to larger palace structure via spiral runway
- Interior scale matching main apartment chambers
- Transitional space between private and public zones

## Recurring Environmental Anchors
- Four guard positions (primary anchor)
- Tapestry-covered walls (visual anchor)
- Connection points to spiral runway (navigation anchor)
- Hidden passage entrances (structural anchor)

## Descriptive Noun Phrases for Render Prompts
- antechamber with four Barsoomian guards
- tapestry-walled guard chamber interior
- concealed passage connection point
- restricted visibility guard space
- palace apartment transitional chamber
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: spiral_runway_lower_floors

[[SECTION markdown]]
# Spiral Runway - Lower Floor Access

## Environment Role
Transit setting for vertical palace navigation.

## Architecture & Geography
- Spiral runway structure connecting upper apartments to lower floors
- Multi-level access point within palace architecture
- Interior connection between main chambers and lower levels
- Structural element of palace vertical circulation

## Lighting & Atmosphere
- Dim lighting consistent with interior palace spaces
- Warm ambient light from upper chamber connections
- Shadowed spiral structure creating depth perception
- Atmospheric tension from restricted visibility

## Scale Cues
- Multi-level structure indicating large palace scale
- Spiral geometry suggesting significant height difference
- Connection to 20-foot glass wall balcony system
- Interior scale matching main apartment chambers

## Recurring Environmental Anchors
- Spiral structure (primary anchor)
- Lower floor connection points (navigation anchor)
- Upper chamber access portals (structural anchor)
- Glass wall balcony system connections (perspective anchor)

## Descriptive Noun Phrases for Render Prompts
- spiral runway lower floor access
- multi-level palace interior connection
- vertical circulation structure interior
- spiral geometry palace architecture
- lower floor chamber entrance point
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: balcony_zodanga_avenue

[[SECTION markdown]]
# Balcony - Zodanga Avenue Overlook

## Environment Role
Transit/escape setting for unauthorized departure.

## Architecture & Geography
- Balcony overlooking broad avenue of Zodanga
- 20 feet high polished glass wall separation
- Building exterior connection point to avenue
- Glass wall separating interior from exterior view

## Lighting & Atmosphere
- Exterior daylight contrasting with interior warmth
- Polished glass reflecting both interior and exterior light
- Atmospheric depth from building to avenue perspective
- Evening or night lighting suggesting escape timing

## Scale Cues
- 20-foot high glass wall indicating significant height
- Broad avenue of Zodanga visible from balcony
- Building-scale architecture with multi-level connections
- Exterior view scale showing city context

## Recurring Environmental Anchors
- Glass wall separation (primary anchor)
- Balcony overlook structure (perspective anchor)
- Broad avenue of Zodanga (exterior anchor)
- Building exterior connection points (structural anchor)

## Descriptive Noun Phrases for Render Prompts
- balcony overlooking broad avenue of Zodanga
- 20 feet high polished glass wall separation
- building exterior overlook perspective
- polished glass exterior view structure
- broad avenue city context exterior
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
