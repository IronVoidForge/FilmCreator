# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:10:02.348105+00:00
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

# Chapter III: My Advent on Mars

## Narrative Arc
1. **Awakening & Physics:** Protagonist wakes on Mars, realizes lower gravity via jumping (3 yards high). Struggles with walking mechanics (hopping/sprawling) due to unfamiliar muscular exertion.
2. **Incubator Discovery:** Finds glass-walled enclosure containing large eggs (2.5 ft diameter) hatching into six-legged creatures (later clarified as two legs/arms + intermediaries). Creatures have blood red eyes, yellowish-green bodies.
3. **Confrontation & Escape:** Adult Martians arrive on mounts (10 ft shoulder height). Leader's spear (40 ft long) nearly hits protagonist. Protagonist jumps 30 ft high to escape enclosure.
4. **First Contact Resolution:** Martians observe agility, shift intent from killing to capturing. Leader approaches unarmed, offers metal armlet. Protagonist accepts and bows.
5. **Departure:** Protagonist rides behind Martian mount with others towards hills.

## Visual Continuity
- **Environment:** Yellowish moss, low hills, midday sun.
- **Enclosure:** Glass roof (4-5 inches thick), wall height (4 feet).
- **Creatures:** Egg diameter (2.5 ft), Eye placement (side-set, protruding), Body color (light yellowish-green).
- **Martians:** Height (15 ft Earth weight), Mount shoulder height (10 ft), Spear length (40 ft).
- **Rifles:** White metal stock, aluminum/steel barrel.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter III

## Primary Settings
- **mars_surface** - Yellowish moss terrain, low hills, midday sun conditions
- **glass_enclosure** - Glass-walled structure with egg incubation interior

## Transit Settings
- **martian_mount_conveyance** - Elevated mount platform for departure journey

## Scale Anchors
- Jump height: 3 yards (Mars gravity)
- Enclosure dimensions: 4 feet wall, 4-5 inch glass roof
- Mount shoulder height: 10 feet Earth weight
- Spear length: 40 feet (leader's weapon)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mars_surface

[[SECTION markdown]]
# Mars Surface Environment

## Environment Role
Primary setting - protagonist's awakening and initial exploration space

## Architecture & Geography
- Yellowish moss covering ground surface
- Low rolling hills in background
- Open terrain with no immediate structures
- Midday sun providing consistent illumination

## Lighting & Atmosphere
- Bright midday sunlight (Earth-weight equivalent)
- Yellowish-green atmospheric tint from moss coverage
- Clear visibility across open landscape
- No shadows indicating direct overhead sun position

## Scale Cues
- Protagonist jumps 3 yards high in Mars gravity
- Walking mechanics require hopping/sprawling due to unfamiliar muscular exertion
- Open terrain allows for wide movement patterns

## Environmental Anchors
- Yellowish moss as primary ground texture
- Low hills providing distant visual reference points
- Midday sun position as temporal marker

## Descriptive Noun Phrases
- yellowish moss terrain
- low rolling hills
- midday sun conditions
- open mars landscape
- gravity-adjusted movement zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: glass_enclosure

[[SECTION markdown]]
# Glass Enclosure Environment

## Environment Role
Secondary setting - incubation and creature discovery space

## Architecture & Geography
- Glass-walled enclosure structure
- Glass roof 4-5 inches thick
- Wall height approximately 4 feet
- Contains large eggs (2.5 ft diameter)
- Interior space for six-legged creatures

## Lighting & Atmosphere
- Transparent glass allows external light penetration
- Interior illuminated by midday sun through glass roof
- Blood red eyes of creatures visible from outside
- Yellowish-green body colors of creatures

## Scale Cues
- Egg diameter: 2.5 feet
- Wall height: 4 feet
- Glass thickness: 4-5 inches
- Creatures hatching within enclosure space

## Environmental Anchors
- Glass roof as primary structural element
- Glass walls defining interior boundaries
- Eggs as incubation markers
- Hatching creatures as biological anchors

## Descriptive Noun Phrases
- glass-walled structure
- thick glass roof
- egg incubation chamber
- creature hatching zone
- transparent enclosure walls

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_mount_conveyance

[[SECTION markdown]]
# Martian Mount Conveyance Environment

## Environment Role
Transit setting - departure journey and first contact resolution space

## Architecture & Geography
- Elevated mount platform (10 ft shoulder height)
- Used for protagonist transport behind adult Martians
- Directional movement towards hills
- Open-air conveyance structure

## Lighting & Atmosphere
- Midday sun conditions maintained during transit
- Yellowish moss terrain visible below mount level
- Clear visibility of approaching hills in distance
- No enclosure - open atmospheric exposure

## Scale Cues
- Mount shoulder height: 10 feet Earth weight
- Adult Martians approximately 15 ft Earth weight
- Leader's spear: 40 feet long (visible from mount)
- Protagonist positioned behind mount during departure

## Environmental Anchors
- Elevated mount platform as primary anchor
- Directional movement towards hills
- Metal armlet as first contact marker
- Open sky above conveyance structure

## Descriptive Noun Phrases
- elevated mount platform
- open-air conveyance
- directional hill approach
- adult martian transport
- departure journey zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
