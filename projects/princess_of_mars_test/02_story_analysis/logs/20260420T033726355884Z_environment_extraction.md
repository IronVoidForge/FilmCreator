# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:37:26.356386+00:00
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

# Chapter VII: CHILD-RAISING ON MARS
## Visual Continuity & Scene Facts
*   **Setting:** Plaza, Incubator enclosure, Dead Sea Bottom, Hills.
*   **Key Objects:** Three-wheeled chariots (gorgeously decorated), Mastodonian draft animals (no bit/bridle), Incubator eggs/hatchlings, Martian hounds.
*   **Characters:** Sola (narrator's companion), Tars Tarkas (chieftain), Lorquas Ptomel Jed (principal chieftain), Warriors (200+), Women/Children (forming gauntlet walls).
*   **Action Sequence:** Breakfast replica -> Procession harnessing -> Incubator hatching ceremony -> Child capture ritual -> Training session.

## Story Summary & Decomposition Notes
1.  **Procession Scene:** Sola escorts narrator to plaza where community harnesses animals to chariots. Procession moves in single file with warriors at head and rear. Narrator dragged into empty chariot, proceeds to incubator location.
2.  **Incubator Hatching:** Eggs hatch after five-year period. Young Martians (3-4 feet tall) released. Tars Tarkas explains hatching to Lorquas Ptomel. Narrator performs leap over parked chariots for entertainment.
3.  **Child-Raising Ritual:** Women and children form two solid walls leading out through chariots. Young Martians run gauntlet length; captured one at a time by women or older children. Last in line captures first to reach end.
4.  **Societal Explanation:** Narrator learns Martian child-rearing involves teaching weapons and language from infancy. No parental love exists; children are communal property. Deformed/defective young are shot. Birth rate regulated to offset death on dying planet.
5.  **Training Progression:** Sola cares for narrator and young Martian prize (male, 4 feet tall). Narrator masters walking under Martian conditions, learns language in a week, develops telepathic powers. Unique advantage: Cannot be read by others' minds.
6.  **Contextual Details:** Community size ~30k souls. Roam arid land between 40-80 degrees south latitude. Incubators built in remote fastnesses to prevent discovery by other tribes.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter VII

## Plaza
- Role: Primary setting for procession scene
- Geography: Open arid plaza space
- Atmosphere: Bright daylight, dusty air
- Scale: Large enough to accommodate chariots and warriors in formation

## Incubator Enclosure
- Role: Secondary/transit setting for hatching ceremony
- Geography: Remote fastness structure with eggs/hatchlings
- Atmosphere: Controlled environment, five-year incubation period
- Scale: Contains multiple three-wheeled chariots parked inside

## Dead Sea Bottom
- Role: Transit/secondary setting for community movement
- Geography: Arid land between 40-80 degrees south latitude
- Atmosphere: Dying planet conditions, harsh environment
- Scale: Community of ~30k souls roaming across terrain

## Hills
- Role: Secondary/transit setting for child-raising ritual
- Geography: Elevated terrain with gauntlet walls
- Atmosphere: Open sky, communal training space
- Scale: Large enough for 200+ warriors and women/children formations
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza

[[SECTION markdown]]
# Plaza Environment

## Role
Primary setting for procession scene where community harnesses animals to chariots.

## Architecture & Geography
Open arid plaza space with single-file procession path. Large enough to accommodate multiple three-wheeled chariots (gorgeously decorated) and warriors in formation at head and rear.

## Lighting & Atmosphere
Bright daylight conditions with dusty air typical of dying planet surface. High visibility for ceremonial events.

## Scale & Anchors
Large communal space supporting 30k soul community gatherings. Recurring anchors include chariot parking areas, warrior formations, and procession routes.

## Descriptive Noun Phrases
- Open arid plaza space
- Single-file procession path
- Chariot parking areas
- Warrior formation zones
- Ceremony gathering grounds
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: incubator_enclosure

[[SECTION markdown]]
# Incubator Enclosure Environment

## Role
Secondary/transit setting for hatching ceremony where five-year period eggs release young Martians.

## Architecture & Geography
Remote fastness structure built to prevent discovery by other tribes. Contains multiple three-wheeled chariots parked inside during hatching events.

## Lighting & Atmosphere
Controlled environment lighting with hatchling emergence moments. Five-year incubation period creates anticipation atmosphere.

## Scale & Anchors
Structure large enough for narrator to perform leap over parked chariots for entertainment. Recurring anchors include egg containers, hatchling release zones, and chariot parking areas.

## Descriptive Noun Phrases
- Remote fastness structure
- Egg incubation containers
- Hatchling release zones
- Chariot parking interior
- Controlled environment space
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dead_sea_bottom

[[SECTION markdown]]
# Dead Sea Bottom Environment

## Role
Transit/secondary setting for community movement across arid land between 40-80 degrees south latitude.

## Architecture & Geography
Arid land terrain with no permanent structures. Community roams across dying planet surface in remote locations.

## Lighting & Atmosphere
Harsh planetary conditions with high visibility but deteriorating environment. Dying planet atmosphere creates survival context.

## Scale & Anchors
Large roaming territory supporting 30k soul community. Recurring anchors include latitude markers, incubator fastnesses, and tribal boundaries.

## Descriptive Noun Phrases
- Arid land terrain
- Latitude marker zones (40-80 degrees south)
- Remote incubator fastnesses
- Tribal boundary areas
- Roaming territory space
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills

[[SECTION markdown]]
# Hills Environment

## Role
Secondary/transit setting for child-raising ritual where women and children form gauntlet walls.

## Architecture & Geography
Elevated terrain with open sky conditions. Large enough to accommodate 200+ warriors and women/children formations in training sessions.

## Lighting & Atmosphere
Open sky lighting with communal training atmosphere. No permanent structures, natural elevation provides gathering space.

## Scale & Anchors
Large formation space supporting gauntlet walls leading through chariots. Recurring anchors include gauntlet wall zones, chariot passage points, and warrior positioning areas.

## Descriptive Noun Phrases
- Elevated terrain space
- Gauntlet wall zones
- Chariot passage points
- Warrior positioning areas
- Communal training grounds
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
