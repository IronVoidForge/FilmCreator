# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:24:47.779044+00:00
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

Chapter id: CH002

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

**Scene 1: Paralysis and Indian Encounter**
*   **Visual Continuity:** Interior of cave facing cliff opening; dim light from early morning sun; vapor filling cave space; trail visible outside.
*   **Narrative:** Narrator is paralyzed (stone-like) despite mental faculties intact. Sound of approaching horses stops. Apache warriors creep stealthily along the narrow ledge. Warriors see narrator but are awestruck and fearful, unable to pass on the ledge. Moaning sound from behind narrator causes warriors to flee in terror; one brave falls headlong from cliff.
*   **Sensory Details:** Pungent odor of poisonous gas; faint vapor against daylight opening; savage eyes looking into narrator's; low distinct moaning sound.

**Scene 2: Speculation and Silence**
*   **Visual Continuity:** Interior cave remains unchanged; horse standing with dragging rein outside; dead body of friend on ledge within vision range.
*   **Narrative:** Narrator speculates on cause of paralysis (poisonous gas vs unknown). Horse wanders off in search of food/water. Silence persists from late afternoon until midnight.
*   **Sensory Details:** Dragging rein; silence of the dead; faint sounds behind narrator eventually cease.

**Scene 3: Metamorphosis and Liberation**
*   **Visual Continuity:** Interior cave flooded with moonlight; narrator standing facing unknown foe; lifeless body lying on floor.
*   **Narrative:** Awful moan returns at midnight. Narrator breaks free of paralysis via mental effort (will/nerves). Discovers his own body is now dead and naked while he stands clothed and alive. Heart pounding, cold sweat present. Cannot touch revolvers/carbine strapped to lifeless body.
*   **Sensory Details:** Sharp click like snapping steel wire; nausea; rustling sound of dead leaves; quick short gasps for breath; ancient experiment of pinching reveals vitality.

**Scene 4: Flight and Investigation**
*   **Visual Continuity:** Exterior Arizona night; starlight clear sky; rocky gorge vista below; cacti-studded flat; silvered mountains in distance.
*   **Narrative:** Narrator flees cave into starlight. Crisp mountain air acts as tonic. Pauses on ledge, upbraids self for apprehension. Decides to investigate outside. Lifts head to breathe pure night air. Sees beautiful vista of rocky gorge and cacti-studded flat under moonlight.
*   **Sensory Details:** Crisp fresh mountain air; silvered mountains; strange lights and shadows on hog back; grotesque details of stiff yet beautiful cacti.

**Scene 5: Drawn to Mars**
*   **Visual Continuity:** Heavens above landscape; large red star close to distant horizon.
*   **Narrative:** Narration turns gaze from landscape to heavens. Attention riveted by large red star near horizon. Star identified as Mars, god of war. Narrator feels spell of overpowering fascination. Longing beyond opposition; closes eyes, stretches arms toward god of vocation. Feels drawn through trackless immensity of space.
*   **Sensory Details:** Myriad stars forming gorgeous canopy; red star close to horizon; instant of extreme cold and utter darkness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1
[[SECTION environment_index_markdown]]
# Environment Index - CH002

## Cave Interior
Primary setting for paralysis and transformation. Features a cave interior facing a cliff opening, internal ledges, and vapor-filled space.

## Arizona Exterior Night
Secondary transit environment featuring rocky gorges, cacti-studded flats, and silvered mountains under starlight.

## Heavens Above Landscape
Metaphysical setting focusing on the red star (Mars) and the vast canopy of stars above the landscape.
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_interior
[[SECTION markdown]]
# Cave Interior

## Role
Primary

## Architecture or Geography
Cave interior facing cliff opening, internal ledge, floor space.

## Lighting and Atmosphere
Dim light (early morning sun/moonlight), vapor filling space, pungent odor of poisonous gas, faint vapor against daylight opening.

## Scale Cues and Anchors
Lifeless body lying on floor, horse standing outside, cliff opening visible.

## Descriptive Noun Phrases
Vapor-filled cave space, dim cliff opening, lifeless body anchor, internal ledge, stone-like paralysis zone.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_exterior_night
[[SECTION markdown]]
# Arizona Exterior Night

## Role
Secondary / Transit

## Architecture or Geography
Rocky gorge vista below, cacti-studded flat, silvered mountains in distance.

## Lighting and Atmosphere
Starlight clear sky, moonlight, crisp fresh mountain air, strange lights and shadows on hog back.

## Scale Cues and Anchors
Hog back (cactus), rocky gorge, distant mountains.

## Descriptive Noun Phrases
Cacti-studded flat, silvered mountains, starlit night vista, rocky gorge below.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: environment
asset_id: heavens_above_landscape
[[SECTION markdown]]
# Heavens Above Landscape

## Role
Secondary / Metaphysical

## Architecture or Geography
Heavens above landscape, trackless immensity of space.

## Lighting and Atmosphere
Myriad stars forming gorgeous canopy, large red star close to distant horizon, instant of extreme cold and utter darkness.

## Scale Cues and Anchors
Red star (Mars), horizon line.

## Descriptive Noun Phrases
Red star near horizon, myriad star canopy, trackless space, god of war focal point.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
