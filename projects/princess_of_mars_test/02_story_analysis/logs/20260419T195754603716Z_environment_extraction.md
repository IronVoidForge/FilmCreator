# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:57:54.603716+00:00
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

# Chapter Summary: CH003 - My Advent on Mars

## Narrative Arc
### Scene 1: Awakening and Exploration
The protagonist wakes in a deep, circular basin of yellowish moss. Realizing they are on Mars without questioning sanity or wakefulness, they explore the immediate area. They discover a low, walled enclosure (4 feet high) with a solid glass roof containing hundreds of large eggs (2.5 feet diameter). Several eggs have hatched into grotesque creatures with six limbs and independent eye movement.

### Scene 2: First Contact and Threat
A group of adult Martians approaches silently on soundless moss. The leader, mounted on a ten-foot-tall beast, nearly spears the protagonist. A rifle swing causes a metallic clatter against a spear butt, alerting the protagonist. The protagonist escapes by leaping 30 feet into the air, landing safely on the opposite side of the enclosure.

### Scene 3: Negotiation and Departure
The Martian leader dismounts unarmed and approaches with peace overtures (throwing down weapons). The protagonist responds with a bow and hand-over-heart gesture. They exchange an enormous metal armlet as a token of friendship. The protagonist rides behind one of the Martians on their mount, departing toward the range of hills in the distance.

## Visual Continuity Facts
### Martian Physiology
- **Height:** Adult warriors approx. 15 feet tall; Mounts tower 10 feet at shoulder.
- **Skin:** Dark slate color, smooth and glossy (Mounts); Light yellowish-green (Young Martians), deepening to olive green in adults.
- **Eyes:** Iris blood red (Albinos), dark pupil, very white eyeball.
- **Teeth:** Snow-white china-like teeth; lower tusks curve upward to sharp points ending near human eye level.
- **Limbs:** Two legs and two arms plus intermediary pair usable as arms or legs. Ears are small cup-shaped antennae protruding not more than an inch.

### Technology & Weapons
- **Rifles:** White metal stock with wood (intensely hard growth unknown to Earth). Barrel alloy of aluminum and steel tempered to hardness exceeding familiar steel. Effective radius 300 miles theoretical, 200 miles practical with wireless finders.
- **Spears:** Forty feet long, tipped with gleaming metal.
- **Mounts:** Four legs on either side, broad flat tail held straight out behind while running. Gaping mouth splitting head from snout to neck. Feet heavily padded and nailless.

### Environment Details
- **Vegetation:** Yellowish mosslike vegetation covering practically entire surface except frozen polar areas and cultivated districts.
- **Rock:** Slight outcroppings of quartz-bearing rock glistening in sunlight.
- **Enclosure:** Low walled structure (4 feet height), roof of solid glass (4 or 5 inches thickness).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH003 My Advent on Mars

## Extracted Environment Families

| Asset ID | Role | Primary Geography | Key Anchors |
|----------|------|-------------------|-------------|
| mars_moss_basin | primary | deep circular basin | yellowish moss, quartz-bearing rock outcroppings |
| mars_glass_enclosure | secondary | low walled structure with solid glass roof | 4-foot walls, 2.5-foot eggs, glass thickness 4-5 inches |
| mars_hills_range | transit | range of hills in distance | cultivated districts, frozen polar areas (exceptions) |
| mars_surface_general | overarching | entire planetary surface | yellowish moss coverage, rock outcroppings |

## Environment Families Summary

1. **mars_moss_basin** - Awakening location, deep circular basin covered in yellowish moss with quartz-bearing rock glistening in sunlight
2. **mars_glass_enclosure** - Exploration and threat zone, low walled structure (4 feet height) with solid glass roof containing egg collection
3. **mars_hills_range** - Departure destination, distant hills visible from enclosure toward cultivated districts
4. **mars_surface_general** - Overarching Martian environment, yellowish mosslike vegetation covering entire surface except frozen polar areas and cultivated districts

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mars_moss_basin

[[SECTION markdown]]
# Mars Moss Basin

## Environment Role
Primary setting for awakening and initial exploration sequence.

## Architecture & Geography
Deep circular basin carved into Martian surface. Yellowish mosslike vegetation covers practically entire surface except frozen polar areas and cultivated districts. Slight outcroppings of quartz-bearing rock glistening in sunlight scattered throughout.

## Lighting & Atmosphere Cues
Sunlight penetrates from above, causing quartz-bearing rock to glisten visibly. Moss provides uniform yellowish ground cover creating soft, organic texture underfoot. No shadows indicate open sky exposure.

## Scale Cues
- Basin depth: deep enough for protagonist to wake without immediate orientation issues
- Circular shape: allows 360-degree exploration from awakening point
- Moss coverage: extends across entire visible basin floor

## Recurring Environmental Anchors
- Yellowish moss ground cover (primary visual anchor)
- Quartz-bearing rock outcroppings (secondary visual anchors, glisten in sunlight)
- Basin circular geometry (spatial orientation reference)

## Descriptive Noun Phrases for Render Prompts
- deep circular yellowish moss basin
- quartz-bearing rock outcroppings glistening in sunlight
- soft organic moss ground texture
- open sky Martian surface exposure
- uniform yellowish vegetation coverage

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mars_glass_enclosure

[[SECTION markdown]]
# Mars Glass Enclosure

## Environment Role
Secondary setting for exploration, threat encounter, and egg discovery sequence.

## Architecture & Geography
Low walled structure with 4-foot height walls. Solid glass roof of 4 or 5 inches thickness covering entire enclosure interior. Contains hundreds of large eggs (2.5 feet diameter each). Several eggs have hatched into grotesque creatures with six limbs and independent eye movement.

## Lighting & Atmosphere Cues
Sunlight filters through solid glass roof, creating diffused illumination inside enclosure. Glass thickness allows light penetration while maintaining structural integrity. Interior atmosphere contains egg collection and creature activity.

## Scale Cues
- Wall height: 4 feet (low enough for easy entry/exit)
- Egg diameter: 2.5 feet each (large scale objects)
- Enclosure interior: accommodates hundreds of eggs simultaneously
- Glass roof thickness: 4-5 inches (substantial structural element)

## Recurring Environmental Anchors
- Solid glass roof (primary architectural anchor)
- Low walled structure perimeter (secondary anchor)
- Egg collection (recurring visual elements, 2.5-foot diameter)
- Hatched creatures with six limbs and independent eye movement

## Descriptive Noun Phrases for Render Prompts
- low walled enclosure with solid glass roof
- four-foot height wall structure
- hundreds of large eggs two-and-a-half feet diameter
- thick glass roof four to five inches thickness
- hatched grotesque creatures with six limbs
- independent eye movement creature details

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mars_hills_range

[[SECTION markdown]]
# Mars Hills Range

## Environment Role
Transit setting for departure sequence and destination marker.

## Architecture & Geography
Range of hills visible in distance from enclosure location. Distant hills form horizon line toward which protagonist departs on Martian mount. Cultivated districts exist as exceptions to general moss coverage within this range area.

## Lighting & Atmosphere Cues
Sunlight illuminates distant hills, creating atmospheric perspective. Hills appear as silhouette against sky from enclosure vantage point. Light conditions consistent with open Mars surface exposure.

## Scale Cues
- Distant hills: visible as horizon markers from 30-foot jump landing position
- Range view: spans multiple hill formations in distance
- Cultivated districts: smaller scale exceptions within larger moss-covered range

## Recurring Environmental Anchors
- Hills range silhouette (primary distant anchor)
- Cultivated districts (secondary exception anchors)
- Horizon line from enclosure vantage point

## Descriptive Noun Phrases for Render Prompts
- range of hills in distance
- horizon line visible from enclosure
- cultivated district exceptions within moss coverage
- atmospheric perspective on distant hills
- open Mars surface lighting conditions

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mars_surface_general

[[SECTION markdown]]
# Mars Surface General Environment

## Environment Role
Overarching planetary environment containing all specific settings.

## Architecture & Geography
Yellowish mosslike vegetation covers practically entire Martian surface except frozen polar areas and cultivated districts. Slight outcroppings of quartz-bearing rock glistening in sunlight scattered throughout landscape. Frozen polar areas exist as exceptions to general coverage. Cultivated districts exist as exceptions to general moss coverage.

## Lighting & Atmosphere Cues
Sunlight illuminates entire planetary surface, creating consistent lighting conditions across all environments. Quartz-bearing rock outcroppings glisten in sunlight across surface. No atmospheric haze mentioned except implied by distant hills visibility.

## Scale Cues
- Planetary scale: encompasses all specific environment families
- Surface coverage: yellowish moss covers practically entire surface
- Rock outcroppings: slight, scattered throughout landscape
- Polar areas: frozen exceptions at planetary extremes

## Recurring Environmental Anchors
- Yellowish mosslike vegetation (primary planetary anchor)
- Quartz-bearing rock outcroppings (secondary anchors)
- Frozen polar areas (exceptional anchors)
- Cultivated districts (exceptional anchors)

## Descriptive Noun Phrases for Render Prompts
- yellowish mosslike vegetation covering entire surface
- slight quartz-bearing rock outcroppings glistening in sunlight
- frozen polar area exceptions
- cultivated district exceptions
- open Mars planetary surface lighting
- consistent sunlight across all environments

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
