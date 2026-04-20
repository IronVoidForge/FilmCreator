# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:26:36.393829+00:00
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

**Visual Context:**
- Landscape: Yellowish moss, quartz rocks, low hills, frozen poles (mentioned as exception).
- Enclosure: Glass roof (4-5 inches thick), 4 feet high wall, no doors/windows on near side.
- Eggs: Snowy white, 2.5 ft diameter, hatching process visible.
- Martians: Olive green skin (darker in males), blood red iris, six limbs (young), antennae ears, longitudinal slit noses.
- Mounts: Slate color, four legs, broad flat tail, nailless feet.
- Weapons: Metal-shod spear (40 feet long), rifle (white metal/wood stock).

**Story Beats:**
1. Awakening & Gravity Check: Narrator wakes in circular basin. Tests movement; hops instead of walking due to low gravity.
2. The Incubator: Discovers glass-walled enclosure with giant eggs. Observes hatching grotesque creatures.
3. Warrior Arrival: Adult Martians approach silently on mounts. Leader's spear nearly hits narrator. Mounts described (slate color, four legs).
4. The Leap: Narrator jumps 30 feet to escape spear point. Lands safely across enclosure. Martians observe with astonishment.
5. Negotiation & Ride: Leader approaches unarmed. Offers metal armlet. Narrator accepts. Taken prisoner on mount, cavalcade rides toward hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH003

## Circular Basin (Primary Setting)
- **Role:** Primary setting where narrator awakens and discovers eggs
- **Key Features:** Glass roof enclosure, circular basin structure
- **Atmosphere:** Low gravity environment, hatching creatures visible
- **Scale:** 4-foot walls, glass thickness 4-5 inches

## Martian Hills/Landscape (Transit Setting)
- **Role:** Transit destination for cavalcade after narrator taken prisoner
- **Key Features:** Yellowish moss terrain, quartz rocks, low hills
- **Atmosphere:** Frozen poles mentioned as exception, natural landscape
- **Scale:** Open terrain suitable for mount travel

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: circular_basin_incubator

[[SECTION markdown]]
# Circular Basin Incubator Environment

## Environment Role
Primary setting - main location where chapter action unfolds

## Architecture and Geography
Circular basin structure with glass-walled enclosure. Glass roof 4-5 inches thick, 4 feet high wall on near side. No doors or windows visible on interior-facing walls. Enclosed space containing giant eggs in hatching process.

## Lighting and Atmosphere Cues
Low gravity environment creates floating sensation. Hatching grotesque creatures emit visual activity within enclosure. Glass transparency allows observation of egg contents. Interior lighting appears natural with possible external light sources filtering through glass roof.

## Scale Cues and Environmental Anchors
- 4-foot wall height defines interior boundary
- Glass thickness (4-5 inches) indicates structural importance
- Egg diameter approximately 2.5 feet provides size reference
- Circular basin shape creates central focal point
- Mounts enter from exterior, establishing spatial relationship between inside/outside

## Descriptive Noun Phrases for Render Prompts
Glass-walled incubator enclosure, circular basin structure, giant hatching eggs, low gravity interior space, transparent glass roof, enclosed observation chamber, egg-hatching activity zone, structural glass walls, interior viewing platform

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_hills_landscape

[[SECTION markdown]]
# Martian Hills Landscape Environment

## Environment Role
Transit setting - destination for cavalcade after narrator taken prisoner

## Architecture and Geography
Natural landscape featuring yellowish moss terrain, quartz rock formations, low hills. Open outdoor space suitable for mount travel. Frozen poles mentioned as exception to typical landscape features. Natural geography without man-made structures visible.

## Lighting and Atmosphere Cues
Natural daylight conditions with possible atmospheric effects from frozen elements. Landscape suggests cold Martian environment. Yellowish moss indicates specific vegetation type. Quartz rocks provide reflective surfaces in natural lighting.

## Scale Cues and Environmental Anchors
- Low hills establish elevation changes for travel route
- Quartz rock formations provide visual landmarks
- Open terrain allows mount cavalcade movement
- Frozen poles (exception) indicate extreme environmental conditions
- Natural landscape scale supports large creature/mount presence

## Descriptive Noun Phrases for Render Prompts
Yellowish moss terrain, quartz rock formations, low hill landscape, natural Martian geography, frozen pole exception, open outdoor environment, mount travel route, cold atmospheric conditions, natural landscape features, exterior viewing perspective

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
