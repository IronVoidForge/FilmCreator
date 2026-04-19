# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:51:21.004623+00:00
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

Chapter id: CH003

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

**Visual Continuity:**
- Environment: Yellowish moss terrain, glass enclosure roof (4-5 inches thick), low hills in distance.
- Flora/Fauna: Giant eggs (2.5 ft diameter), hatchlings (six legs, red eyes, white tusks), adult Martians (15 ft tall), mounts (dark slate color, four legs each side, broad tail).
- Equipment: Metal-shod spears (40 ft long), rifles (white metal/wood stock, aluminum/steel barrel).

**Narrative Arc:**
1. Waking & Gravity Test: Narrator wakes on Mars, discovers low gravity via hopping instead of walking.
2. Discovery: Finds glass incubator with hatching eggs and strange hatchlings.
3. Encounter: Adult Martians arrive; narrator nearly impaled by spear but escapes using agility leap.
4. Resolution: Martian leader approaches unarmed, offers metal armlet for peace. Narrator accepts armlet and rides off towards hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH003

## Primary Environments

### primary_moss_terrain_with_glass_roof
Yellowish moss terrain with glass enclosure roof (4-5 inches thick), low hills visible in distance. Glass incubator structure contains hatching eggs and strange hatchlings. Adult Martians appear within this space. Metal-shod spears and metal armlet interact here.

### distant_hills
Visible background geography, destination toward which narrator rides off after encounter resolution. Serves as environmental anchor and directional reference point.

## Environment Families Summary

- **primary_moss_terrain_with_glass_roof**: Primary setting where waking, gravity test, incubator discovery, and Martian encounter occur
- **distant_hills**: Transit/destination environment toward which narrator departs after peace agreement

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: primary_moss_terrain_with_glass_roof

[[SECTION markdown]]
# Primary Moss Terrain with Glass Roof

## Environment Role
Primary setting - main action space for waking, gravity test, incubator discovery, and Martian encounter sequences.

## Architecture/Geography
Yellowish moss terrain surface with glass enclosure roof (4-5 inches thick). Glass incubator structure within terrain contains hatching eggs. Low hills visible in background distance. Metal-shod spears (40 ft long) and metal armlet interact within this space.

## Lighting/Atmosphere Cues
Yellowish ambient lighting through glass roof. Low gravity atmosphere evident via hopping movement instead of walking. Glass transparency allows visibility of incubator contents from outside.

## Scale Cues/Environmental Anchors
- Giant eggs (2.5 ft diameter) within incubator structure
- Adult Martians (15 ft tall) appear within terrain space
- Hatchlings with six legs, red eyes, white tusks occupy incubator interior
- Mounts (dark slate color, four legs each side, broad tail) serve as transportation

## Descriptive Noun Phrases
Yellowish moss surface, glass enclosure roof, thick glass incubator structure, hatching egg chamber, Martian encounter space, low gravity terrain, metal-shod spear zone, adult Martian presence area, hatchling incubation zone, distant hill view.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: distant_hills

[[SECTION markdown]]
# Distant Hills

## Environment Role
Transit/destination setting - visible background geography toward which narrator rides off after peace agreement resolution.

## Architecture/Geography
Low hills in background distance, visible through glass enclosure roof. Serves as directional reference point and environmental anchor for scene composition.

## Lighting/Atmosphere Cues
Yellowish ambient lighting consistent with primary terrain. Distant visibility through glass transparency. Atmospheric depth created by hill silhouette against sky.

## Scale Cues/Environmental Anchors
- Visible from primary moss terrain through glass roof
- Serves as destination marker for narrator departure
- Background geography element in scene composition

## Descriptive Noun Phrases
Distant low hills, background hill range, visible horizon geography, directional reference point, environmental anchor silhouette, sky-line boundary, hill view through glass.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
