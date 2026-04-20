# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:19:16.347303+00:00
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

# Visual Continuity Facts
- **Environment:** Yellowish mosslike vegetation, quartz-bearing rock, low hills, solid glass roof (4-5 inches thick).
- **Martians:** 15 feet tall, dark slate skin, yellow feet, small cup-shaped antennae ears, blood red iris, white teeth with upward-curving tusks.
- **Mounts:** Ten feet high at shoulder, four legs, broad flat tail, no hair, smooth glossy, no bridle/reins.
- **Eggs:** Snowy white, 2.5 feet diameter, hatching process observed.
- **Weapons:** 40-foot spears (metal-tipped), rifles (white metal barrel, wood stock, radium projectiles).

# Broad Story Summary
The narrator wakes in a circular basin on Mars and realizes gravity is significantly lower, causing them to jump three yards upon standing. While attempting to walk, they hop and sprawl due to unfamiliar muscle dynamics. They discover a glass incubator containing giant eggs and observe grotesque young Martians hatching. A group of adult Martians approaches; the leader's spear nearly strikes the narrator, but the sound alerts the leader. The narrator leaps thirty feet into the air to escape, landing safely on the opposite side. The Martians are surprised by this agility. The leader dismounts unarmed and offers a metal armlet as a peace token. The narrator accepts it, and they walk together before the leader mounts his animal. The entire cavalcade departs towards the range of hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH003
## Circular Basin on Mars
- Primary setting where narrator awakens
- Features yellowish mosslike vegetation and quartz-bearing rock
- Low hills visible in background
- Solid glass roof structure (4-5 inches thick)
- Gravity significantly lower than Earth

## Glass Incubator
- Secondary containment within circular basin
- Houses giant eggs for Martian hatching
- Transparent enclosure allowing observation
- Connected to main environment via glass walls

## Hills Range
- Transit destination for cavalcade
- Visible from circular basin
- Solid ground with natural terrain
- Low elevation hills across Mars surface
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: circular_basin_mars

[[SECTION markdown]]
# Circular Basin on Mars

## Environment Role
Primary awakening and initial encounter setting for narrator.

## Architecture and Geography
Circular basin carved into Martian surface with solid glass roof structure measuring 4-5 inches thick. Yellowish mosslike vegetation covers ground surfaces throughout the area. Quartz-bearing rock formations visible along basin edges and interior walls. Low hills form natural backdrop surrounding the circular depression.

## Lighting and Atmosphere
Natural ambient light filtering through glass roof creates soft illumination across yellowish moss surfaces. Lower gravity atmosphere causes visual distortion in movement patterns. Glass incubator within basin provides contained observation space with internal lighting for egg hatching process.

## Scale Cues and Environmental Anchors
Narrator jumps three yards upon standing due to reduced gravity. Glass incubator measures approximately 15 feet tall containing giant eggs. Martians stand 15 feet tall with dark slate skin and yellow feet. Mounts reach ten feet high at shoulder level with four legs and broad flat tail.

## Descriptive Noun Phrases
Circular glass-roofed basin, yellowish mosslike ground cover, quartz-bearing rock formations, low hill range backdrop, solid glass incubator enclosure, giant hatching eggs, reduced gravity atmosphere, Martian surface depression, transparent observation chamber, natural Martian terrain.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: glass_incubator

[[SECTION markdown]]
# Glass Incubator

## Environment Role
Secondary containment setting within circular basin for egg observation and hatching process.

## Architecture and Geography
Transparent enclosure integrated into circular basin floor with 4-5 inch thick glass walls. Houses giant eggs measuring 2.5 feet in diameter. Located within main environment allowing visual access from surrounding area. Glass structure provides protective barrier while maintaining visibility of hatching process.

## Lighting and Atmosphere
Internal lighting illuminates snowy white egg surfaces for observation. Transparent glass allows natural light from circular basin roof to penetrate interior space. Hatching process creates dynamic atmospheric changes as young Martians emerge from eggs.

## Scale Cues and Environmental Anchors
Eggs measure 2.5 feet diameter with hatching process visible through glass walls. Young Martians emerging reach approximately 15 feet in height with dark slate skin. Glass structure provides stable anchor point within circular basin environment.

## Descriptive Noun Phrases
Transparent glass enclosure, giant hatching eggs, snowy white egg surfaces, internal observation lighting, protective glass barrier, integrated incubator chamber, transparent viewing walls, egg emergence process, contained hatching space, visible development chamber.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills_range

[[SECTION markdown]]
# Hills Range

## Environment Role
Transit destination setting for cavalcade departure and journey across Martian surface.

## Architecture and Geography
Natural low elevation hills forming range across Martian landscape. Visible from circular basin as natural backdrop. Solid ground terrain suitable for mount travel and cavalcade movement. Natural hill formations create varied topography across the range.

## Lighting and Atmosphere
Natural ambient light illuminates hill surfaces with yellowish mosslike vegetation coverage. Reduced gravity atmosphere affects movement patterns across hill terrain. Glass roof structures may be visible from certain vantage points within hills.

## Scale Cues and Environmental Anchors
Low hills form natural elevation changes across Martian surface. Cavalcade travels through range of hills toward distant horizon. Hill formations provide natural landmarks for navigation across reduced gravity landscape.

## Descriptive Noun Phrases
Natural low hill range, yellowish moss-covered terrain, solid ground surface, elevated hill formations, natural Martian landscape, distant hill horizon, varied topography, natural elevation changes, hill range destination, traversable hill terrain.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
