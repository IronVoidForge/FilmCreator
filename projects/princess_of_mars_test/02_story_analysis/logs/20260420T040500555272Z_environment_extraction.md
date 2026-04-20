# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:05:00.555773+00:00
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

Chapter id: CH021

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

**Arrival at Zodanga:**
John Carter arrives at the gates of Zodanga ten days after leaving the Ptor brothers. He separates from Woola before entering the city to prevent unwelcome attention (Woola is not domesticated by red men). He enters via a letter of introduction, gaining immediate entrance to the vast walled city.

**Meeting Kantos Kan:**
In the central plaza, Carter meets Kantos Kan, who recognizes him as "John Carter" and "Darseen." They discuss Dejah Thoris's fate; she is believed dead by the Zodangans but not confirmed. Carter intends to reach Helium to report news of her possible whereabouts.

**Enlistment in Air Scouts:**
Carter joins the air-scout squadron. Kantos Kan helps him bypass initial examination checks by claiming he is John Carter (a ruse that will be discovered later). The next few days are spent learning Martian aviation and repairing dainty little contrivances (one-man aircraft powered by radium engines and eighth ray buoyancy).

**Action Sequence:**
On the fourth day, Carter makes his first flight. He saves a cousin of the Jeddak Than Kosis from three green warriors who were attacking him near a walled field. Carter rammed the nearest warrior's mount and engaged the others on foot, killing them with practiced skill. The Zodangan was wounded but survived.

**Reward and Promotion:**
A ceremony is held in the plaza to confer honors for bravery. Carter is called out by name ("John Carter, air scout!"). Than Kosis awards him a metal ornament and appoints him a padwar of The Guards, granting him quarters in his palace. Carter returns his machine to the barracks and reports to the officer in charge of the palace.

**Visual Continuity:**
*   Morning streets are practically deserted; residences resemble huge rookeries raised on metal columns.
*   Shops are not raised from the ground; doors are unbolted or barred (thievery unknown).
*   Air craft bodies are sixteen feet long, two feet wide, three inches thick.
*   The plaza covers a square mile and is bounded by palaces of royalty.
*   Mechanical apparatus serves food in cafes; no hand touches the food from raw state to table.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Zodanga Environment Index - Chapter 21

## Primary Environments

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|------|--------------|
| zodanga_gates_entrance | Zodanga Gates | Transit Setting | Arrival point, letter of introduction access |
| central_plaza_zodanga | Central Plaza | Primary Setting | Square mile plaza, royal palaces boundary |
| air_scout_barracks | Air Scout Barracks | Secondary Setting | Aviation training, aircraft repair area |
| walled_field_action | Walled Field | Action Setting | Combat zone near city perimeter |
| palace_than_kosis | Palace of Than Kosis | Primary Setting | Royal quarters, ceremony location |

## Environmental Families

1. **Zodanga Gates Entrance** - City arrival and introduction point
2. **Central Plaza Zodanga** - Main gathering and meeting space
3. **Air Scout Barracks** - Training and aircraft maintenance facility
4. **Walled Field Action** - Combat and rescue zone
5. **Palace of Than Kosis** - Royal residence and honor ceremony location

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodanga_gates_entrance

[[SECTION markdown]]
# Zodanga Gates Entrance

## Environment Role
Transit Setting - Arrival point for John Carter entering Zodanga city

## Architecture and Geography
- Massive walled city entrance with gate structure
- Letter of introduction access point
- City perimeter boundary marker
- Metal column supports visible in surrounding area

## Lighting and Atmosphere Cues
- Morning light conditions (practically deserted streets)
- Red Martian sky atmosphere
- Dusty desert environment
- Formal ceremonial entrance lighting

## Scale Cues
- Vast walled city scale
- Gate structure height relative to human figures
- City perimeter width visible from approach

## Descriptive Noun Phrases
- "walled city entrance"
- "letter of introduction access point"
- "city perimeter boundary"
- "morning deserted streets"
- "metal column supports"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: central_plaza_zodanga

[[SECTION markdown]]
# Central Plaza Zodanga

## Environment Role
Primary Setting - Main gathering and meeting space for city activities

## Architecture and Geography
- Square mile covered plaza area
- Bounded by palaces of royalty
- Central open gathering space
- Mechanical apparatus food service stations in cafes
- Shops not raised from ground level
- Doors unbolted or barred (thievery unknown)

## Lighting and Atmosphere Cues
- Morning light conditions
- Desert atmosphere with red sky
- Formal plaza lighting for ceremonies
- Open-air environment with minimal shade

## Scale Cues
- Square mile coverage area
- Palace height relative to plaza level
- Aircraft bodies sixteen feet long visible in plaza
- Crowd gathering scale during ceremonies

## Descriptive Noun Phrases
- "square mile covered plaza"
- "royal palace boundaries"
- "mechanical food service apparatus"
- "unbolted shop doors"
- "ceremony gathering space"
- "open-air desert environment"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: air_scout_barracks

[[SECTION markdown]]
# Air Scout Barracks

## Environment Role
Secondary Setting - Aviation training and aircraft maintenance facility

## Architecture and Geography
- Aircraft repair area with tools and equipment
- Training zone for Martian aviation
- Barracks structure housing air scouts
- Radium engine testing area
- Eighth ray buoyancy demonstration space
- Machine storage in barracks

## Lighting and Atmosphere Cues
- Indoor training lighting conditions
- Workshop atmosphere with mechanical apparatus
- Red sky visible through windows/doors
- Technical workspace environment

## Scale Cues
- Aircraft bodies sixteen feet long, two feet wide, three inches thick
- Radium engine size relative to human operators
- Training equipment scale for one-man aircraft
- Barracks room dimensions for aircraft storage

## Descriptive Noun Phrases
- "aircraft repair area"
- "radium engine testing zone"
- "eighth ray buoyancy demonstration space"
- "one-man aircraft storage"
- "aviation training facility"
- "mechanical apparatus workspace"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: walled_field_action

[[SECTION markdown]]
# Walled Field Action

## Environment Role
Action Setting - Combat and rescue zone near city perimeter

## Architecture and Geography
- Walled field boundary structure
- City perimeter location
- Open combat area for aerial action
- Green warrior attack zone
- Mountable terrain for warriors
- Rescue operation space

## Lighting and Atmosphere Cues
- Daylight combat conditions
- Desert atmosphere with red sky
- Action lighting for combat sequences
- Open-air field environment

## Scale Cues
- Field width relative to aircraft size (sixteen feet long)
- Mount height for warrior attacks
- Combat zone dimensions for aerial maneuvers
- Rescue area scale for human figures

## Descriptive Noun Phrases
- "walled field boundary"
- "city perimeter combat zone"
- "green warrior attack area"
- "mountable terrain for warriors"
- "aerial rescue operation space"
- "open-air combat field"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: palace_than_kosis

[[SECTION markdown]]
# Palace of Than Kosis

## Environment Role
Primary Setting - Royal residence and honor ceremony location

## Architecture and Geography
- Palace structure housing royal quarters
- Metal column raised residences nearby (huge rookeries)
- Ceremony hall for honors conferral
- Palace interior with formal spaces
- Quarters area for John Carter assignment
- Officer in charge reporting location

## Lighting and Atmosphere Cues
- Indoor palace lighting conditions
- Formal ceremony lighting
- Red sky visible through palace windows
- Royal residence atmosphere

## Scale Cues
- Palace height relative to surrounding rookeries (huge metal columns)
- Ceremony hall dimensions for honors conferral
- Quarters room size for John Carter assignment
- Metal ornament scale for award presentation

## Descriptive Noun Phrases
- "royal palace quarters"
- "ceremony hall for honors"
- "metal column raised residences"
- "huge rookeries on metal columns"
- "formal palace interior spaces"
- "officer reporting location"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
