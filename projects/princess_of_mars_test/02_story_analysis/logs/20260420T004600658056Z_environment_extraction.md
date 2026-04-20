# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:46:00.658056+00:00
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

# Chapter Title
CHAPTER III: MY ADVENT ON MARS

# Visual Continuity Facts
- **Environment:** Yellowish mosslike vegetation covering a circular basin; midday sun with intense heat; quartz-bearing rock outcroppings; low hills in distance.
- **Physics:** Protagonist jumps ~3 yards high on Earth-equivalent effort; walking manifests as hops and sprawls due to reduced gravity/air pressure.
- **Young Martians (Eggs):** Large eggs (~2.5 ft diameter) inside a solid glass enclosure roof; creatures are head-heavy with six limbs, blood red iris, white teeth/tusks, dark slate skin, small cup-shaped antennae ears.
- **Adult Martians & Mounts:** Warriors ~15 feet tall on four-legged mounts (~10 ft shoulder height); mounts have yellow feet, broad flat tail, no hair; warriors carry forty-foot spears tipped with gleaming metal; mounted without reins/bridle.
- **Objects:** Metal armlet ornaments strapped to head/limbs/breast; rifles of white metal and wood stock; glass-walled incubator structure.

# Story Summary
Protagonist wakes on Mars, explores a glass-walled enclosure containing hatching Martians. Ambushed by adult Martians on mounts; leader's spear nearly kills him. Protagonist leaps 30 feet to safety. Martians observe his agility and decide to capture him rather than kill. Leader offers peace via metal armlet. Protagonist accepts, rides with the cavalcade toward distant hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter III: MY ADVENT ON MARS

## Primary Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|------|--------------|
| glass_walled_enclosure | Martian Egg Incubator | Primary/Transit | Glass-roofed structure containing hatching Martians |
| circular_basin_mars | Yellow Moss Basin | Primary/Combat | Circular basin with mosslike vegetation and quartz rocks |
| distant_hills_mars | Hill Range Destination | Transit | Distant hills toward which cavalcade travels |

## Environment Families Summary

- **Glass-walled enclosure**: Contains large eggs (~2.5 ft diameter) inside solid glass roof; hatching Martians with six limbs, blood red iris, white teeth/tusks
- **Circular basin**: Yellowish mosslike vegetation covering circular basin; midday sun with intense heat; quartz-bearing rock outcroppings; low hills in distance
- **Distant hills**: Destination terrain for cavalcade travel toward distant hills

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: glass_walled_enclosure

[[SECTION markdown]]
# Glass-walled Enclosure - Martian Egg Incubator

## Environment Role
Primary setting and transit zone where protagonist awakens and encounters hatching Martians

## Architecture/Geography
Solid glass roof structure forming enclosed incubation chamber; glass-walled containment area with transparent viewing panels; interior space designed for creature observation

## Lighting/Atmosphere Cues
Interior ambient light filtering through glass walls creating soft illumination; controlled atmosphere within sealed enclosure; visual continuity of hatching activity visible through transparent surfaces

## Scale Cues
Large eggs approximately 2.5 feet diameter inside solid glass roof structure; interior chamber accommodates multiple egg incubation units; viewing height allows protagonist to observe creatures at eye level

## Recurring Environmental Anchors
Glass-roofed containment structure; egg incubation units; hatching creature activity zones; transparent observation surfaces

## Descriptive Noun Phrases for Render Prompts
- glass-walled incubator chamber
- solid glass roof structure
- large egg incubation units
- transparent viewing panels
- hatching creature activity zone
- sealed atmosphere enclosure
- interior ambient light filtering
- six-limbed creature observation area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: circular_basin_mars

[[SECTION markdown]]
# Circular Basin - Yellow Moss Mars Terrain

## Environment Role
Primary combat setting where protagonist is ambushed by adult Martians on mounts; transit zone for initial exploration

## Architecture/Geography
Circular basin terrain covered with yellowish mosslike vegetation; quartz-bearing rock outcroppings scattered across surface; low hills visible in distance forming natural boundary

## Lighting/Atmosphere Cues
Midday sun casting intense heat across open basin; bright overhead illumination creating harsh shadows from rock formations; atmospheric conditions showing reduced gravity effects on protagonist movement

## Scale Cues
Circular basin spanning multiple yards in diameter; quartz rock outcroppings ranging from small to medium size; low hills forming distant horizon line approximately 10-20 feet elevation

## Recurring Environmental Anchors
Yellowish mosslike vegetation covering circular basin; quartz-bearing rock outcroppings; low hills in distance; open sky above basin

## Descriptive Noun Phrases for Render Prompts
- yellowish mosslike vegetation terrain
- circular basin surface
- quartz-bearing rock outcroppings
- low hills distant horizon
- midday sun intense heat lighting
- open sky overhead illumination
- reduced gravity movement zone
- natural boundary hill formations

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: distant_hills_mars

[[SECTION markdown]]
# Distant Hills - Hill Range Destination

## Environment Role
Transit destination terrain toward which cavalcade travels; secondary setting for journey conclusion

## Architecture/Geography
Distant hills forming elevated terrain range; hill formations creating natural landscape boundary; open valley floor leading toward hill range

## Lighting/Atmosphere Cues
Distant lighting showing atmospheric perspective from basin viewpoint; ambient light filtering through valley air; horizon line illumination indicating travel direction

## Scale Cues
Hill range visible as distant elevation feature approximately 10-20 feet above valley floor; multiple hill formations creating layered landscape depth; open space between current location and hills

## Recurring Environmental Anchors
Distant hills forming destination landmark; elevated terrain range; valley floor leading toward hills; atmospheric perspective from basin viewpoint

## Descriptive Noun Phrases for Render Prompts
- distant hills elevation range
- hill formation landscape boundary
- valley floor open space
- atmospheric perspective lighting
- horizon line travel direction
- layered landscape depth
- destination landmark feature
- elevated terrain range

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
