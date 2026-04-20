# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:29:04.934071+00:00
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

Chapter id: CH005

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

**Broad Story Summary**

*Scene 1: Observation and Sustenance*
- Sola leaves the chamber with the watch dog; the narrator examines the room's mural paintings (landscapes without animals) and food supplies (plant milk).
- Narrator sleeps through the night, waking cold but covered by fur.

*Scene 2: The Escape Attempt*
- Waking in daylight, the narrator observes five female occupants sleeping and the brute guarding the threshold.
- Deciding to test the brute's loyalty, the narrator exits the room; the brute follows with a shuffling gait.
- At the city edge, the brute attacks; the narrator jumps over him into open space.

*Scene 3: The Window Jump and Capture*
- The brute chases at high speed; the narrator leaps into a window thirty feet up on a building overlooking the valley.
- Upon reaching the sill, a hand grabs the narrator from behind inside the room.
- Thrown onto the back, the narrator sees a colossal ape-like creature (white, hairless, bristly head) standing over them.

**Visual Continuity Facts**

*Room Layout & Objects*
- Threshold: Guarded by the brute throughout the chapter.
- Floor Space: Contains food containers and fur coverings.
- Window Sill: Height of approximately thirty feet; overlooks the valley.
- Mural Paintings: Depict mountains, rivers, lakes, oceans, meadows, trees, flowers, winding roadways, sun-kissed gardens; no representation of living animals.

*Characters & Appearance*
- Sola: Female Martian, sympathetic, kind, unfailing ministrations.
- Watch Dog: Brute, short legs, fast runner, loyal protector, shuffling gait when walking.
- New Guardian: Colossal ape-like creature, white and hairless except for enormous shock of bristly hair on head.

*Environmental Details*
- Lighting: Martian nights are extremely cold; illuminated by two moons (nearer moon ~5,000 miles away, further ~14,000 miles).
- Atmosphere: Very thin; fails to diffuse starlight significantly.
- Temperature: Sudden changes between day and night; narrator feels cold upon waking.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test (Chapter CH005)

## Primary Environments

| Asset ID | Name | Role | Key Features |
|----------|------|------|--------------|
| chamber_room | The Chamber | Primary Setting | Interior room with murals, food containers, fur coverings, threshold guarded by brute |
| city_edge | City Edge | Transit Setting | Open space at building perimeter where brute attacks narrator |
| window_building_valley_view | Window Building Overlooking Valley | Secondary Setting | Thirty-foot high window sill overlooking valley, interior hand grab point |

## Environmental Families

1. **Interior Chamber Space** - Main living quarters with mural paintings and food supplies
2. **City Perimeter Zone** - Boundary area between building structure and open space
3. **Valley View Platform** - Elevated observation point with interior capture mechanism

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chamber_room

[[SECTION markdown]]
# The Chamber

## Environment Role
Primary Setting - Main living quarters where narrator, Sola, and watch dog reside

## Architecture & Geography
Interior room space with threshold guarded by brute. Contains floor area for food containers and fur coverings. Window sill height approximately thirty feet overlooking valley below.

## Lighting & Atmosphere Cues
Martian nights extremely cold; illumination from two moons (nearer moon ~5,000 miles away, further ~14,000 miles). Very thin atmosphere fails to diffuse starlight significantly. Sudden temperature changes between day and night create cold sensation upon waking.

## Scale & Environmental Anchors
- Threshold: Guarded by brute throughout chapter
- Floor Space: Contains food containers and fur coverings  
- Window Sill: Height of approximately thirty feet; overlooks valley
- Mural Paintings: Depict mountains, rivers, lakes, oceans, meadows, trees, flowers, winding roadways, sun-kissed gardens; no representation of living animals

## Descriptive Noun Phrases
- Interior chamber with mural paintings
- Food supply containers on floor
- Fur coverings for warmth
- Threshold guarded by brute
- Thirty-foot window sill overlooking valley
- Martian two-moon illumination
- Thin atmospheric lighting conditions
- Cold waking environment
- Landscape murals without animal representation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_edge

[[SECTION markdown]]
# City Edge

## Environment Role
Transit Setting - Boundary zone between building structure and open space where escape attempt occurs

## Architecture & Geography
Open perimeter area at building edge. Transition zone between interior room and exterior valley view. Attack point for brute during narrator's escape attempt.

## Lighting & Atmosphere Cues
Daylight conditions during escape attempt. Martian atmospheric thinness creates direct starlight visibility without significant diffusion. Temperature shifts between day and night create cold sensation.

## Scale & Environmental Anchors
- Building perimeter boundary
- Open space beyond building edge
- Attack zone for brute
- Jump point from thirty-foot window sill
- Valley view visible from edge position

## Descriptive Noun Phrases
- Building perimeter edge
- Open space at city boundary
- Brute attack zone
- Escape attempt location
- Thirty-foot jump distance
- Valley view from building edge
- Daylight atmospheric conditions
- Thin Martian air exposure
- Cold temperature transition zone
- Perimeter guard threshold

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: window_building_valley_view

[[SECTION markdown]]
# Window Building Overlooking Valley

## Environment Role
Secondary Setting - Elevated observation platform with interior capture mechanism

## Architecture & Geography
Thirty-foot high window on building overlooking valley. Interior room space where hand grabs narrator from behind. Exterior sill serves as jump point into open space. Colossal ape-like creature visible standing over narrator upon reaching sill.

## Lighting & Atmosphere Cues
Martian two-moon illumination during night scenes. Very thin atmosphere creates direct starlight without diffusion. Cold temperature conditions create sudden warming sensation when covered by fur. Daylight visibility during escape attempt.

## Scale & Environmental Anchors
- Window height: Approximately thirty feet
- Interior hand grab point from behind
- Exterior sill overlooking valley
- Colossal white hairless ape-like creature standing position
- Building structure framing window opening
- Valley view platform below

## Descriptive Noun Phrases
- Thirty-foot high window opening
- Interior capture hand grab point
- Exterior jump sill overlooking valley
- White hairless colossal creature standing position
- Building frame window structure
- Valley observation platform
- Two-moon illuminated night scene
- Thin atmospheric lighting conditions
- Cold temperature environment
- Interior room space with exterior access

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
