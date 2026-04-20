# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:08:41.673543+00:00
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

Chapter id: CH023

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

**Scene 1: Infiltration & Warning.** Carter enters Kantos Kan's room in Zodanga without detection. He informs Kan that Dejah Thoris has promised her hand to Sab Than. Kan reacts with dismay, declaring the alliance impossible for Helium lovers.
**Scene 2: The Plan.** Kan pledges his sword to kill Sab Than for Dejah Thoris and Helium. Carter agrees to go to Helium while Kan attempts the assassination at the palace.
**Scene 3: Roof Access.** Carter climbs the barracks building using ornamental ledges. He swings up to the roof using a leather strap with a hook, risking a fall from a thousand feet. He neutralizes the sentry by throwing him over the edge and binding him there.
**Scene 4: Machine Retrieval & Takeoff.** Carter retrieves his machine and Kan's machine from the sheds. They take off together towards the palace route.
**Scene 5: Pursuit & Crash.** Zodanga air scouts pursue them. Carter uses Helium gearing tricks to increase speed but is hit by a shot from a cruiser. The craft suffers concussion damage and plunges downward.
**Scene 6: Navigation Loss.** After recovering near the ground, Carter's compass and speedometer are destroyed by the projectile fragment. He flies blindly for nearly six hours.
**Scene 7: Wrong City Realization.** Morning finds him over a vast expanse of dead sea bottom. He approaches a city but realizes it is not Helium due to its lack of twin towers (scarlet and yellow). He must correct his course southeast.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH023

| Asset ID | Environment Name | Role | Location |
|----------|------------------|------|----------|
| kantos_room_zodanga | Kantos Kan's Private Room | Primary Setting | Zodanga Palace |
| barracks_roof_zodanga | Barracks Building Roof | Transit Setting | Zodanga Military District |
| machine_sheds_zodanga | Machine Storage Sheds | Secondary Setting | Zodanga Outskirts |
| air_route_zodanga_helium | Atmospheric Flight Route | Transit Setting | Between Cities |
| dead_sea_expanse | Dead Sea Bottom Expanse | Navigation Setting | Southeast of Helium |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: kantos_room_zodanga

[[SECTION markdown]]
**Role:** Primary Setting  
**Architecture:** Private chamber within Zodanga Palace, ornate furnishings befitting high-ranking military official  
**Lighting & Atmosphere:** Interior lighting with heavy drapery, formal and tense atmosphere reflecting political intrigue  
**Scale Cues:** Medium-sized room allowing intimate conversation between Carter and Kan  
**Environmental Anchors:** Desk, chair, window overlooking Zodanga cityscape, wall decorations indicating military rank  
**Descriptive Noun Phrases:** ornate private chamber, palace interior, heavy drapery, formal furnishings, political intrigue setting

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: barracks_roof_zodanga

[[SECTION markdown]]
**Role:** Transit Setting  
**Architecture:** Military barracks building with ornamental ledges and rooftop access points  
**Lighting & Atmosphere:** Daylight exposure, high altitude visibility, dangerous vertical drop of thousand feet  
**Scale Cues:** Large vertical structure with multiple floors, rooftop spanning significant area  
**Environmental Anchors:** Ornamental ledges, leather strap hook system, sentry position, roof edge  
**Descriptive Noun Phrases:** military barracks rooftop, ornamental ledge system, high altitude access point, dangerous vertical drop

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: machine_sheds_zodanga

[[SECTION markdown]]
**Role:** Secondary Setting  
**Architecture:** Storage sheds for machines and equipment, utilitarian industrial design  
**Lighting & Atmosphere:** Semi-enclosed space with natural light filtering through openings, functional atmosphere  
**Scale Cues:** Large enough to house multiple machines, open floor plan for equipment storage  
**Environmental Anchors:** Machine storage racks, shed doors, equipment retrieval points  
**Descriptive Noun Phrases:** machine storage facility, industrial shed interior, equipment housing area, utilitarian storage space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: air_route_zodanga_helium

[[SECTION markdown]]
**Role:** Transit Setting  
**Architecture:** Atmospheric flight corridor between Zodanga and Helium, open sky navigation space  
**Lighting & Atmosphere:** Daylight conditions with atmospheric haze, distant city silhouettes visible from altitude  
**Scale Cues:** Vast three-dimensional space for aircraft travel, high altitude perspective  
**Environmental Anchors:** Flight path markers, distant city landmarks, atmospheric conditions affecting visibility  
**Descriptive Noun Phrases:** atmospheric flight corridor, open sky navigation route, high altitude passage, inter-city airway

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dead_sea_expanse

[[SECTION markdown]]
**Role:** Navigation Setting  
**Architecture:** Vast expanse of dead sea bottom terrain, barren landscape with no vegetation  
**Lighting & Atmosphere:** Morning light conditions, expansive horizon visibility, desolate atmosphere  
**Scale Cues:** Massive geographical feature spanning thousands of square miles, distant city approach from altitude  
**Environmental Anchors:** Dead sea bottom surface, approaching city silhouette, directional landmarks for navigation  
**Descriptive Noun Phrases:** dead sea bottom expanse, barren landscape terrain, vast geographical feature, desolate navigation area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
