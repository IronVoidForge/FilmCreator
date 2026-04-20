# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:33:18.250340+00:00
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

# Chapter Summary: An Air Scout for Zodanga

**Broad Story Summary:**
John Carter arrives at Zodanga after parting with his companion Woola at the city gates to ensure safety within the walled city. He enters via a letter of introduction from the Ptor brothers and proceeds to the central plaza. There, he meets Kantos Kan, an air scout who is searching for Dejah Thoris. Carter joins the Air Scout Squadron under Kantos Kan's guidance.

Over the next few days, Carter learns to fly Martian aircraft and repair them. On his fourth day, he makes his first flight and saves a cousin of the Jeddak Than Kosis from three Green Warriors who were attacking him while he was repairing his craft. Carter engages in combat, defeating the warriors with ease. Following this feat, he is decorated during a ceremony on the plain before the city by Than Kosis. He is appointed a padwar of The Guards and granted quarters in the palace of Than Kosis.

**Visual Continuity Facts:**
*   **City Layout:** Residences are raised high upon metal columns resembling steel tree trunks; shops are not raised from the ground. A vast central plaza covers a square mile, bounded by palaces and public buildings.
*   **Technology:** Airships have bodies about sixteen feet long with radium engines on top; buoyancy is provided by the eighth Barsoomian ray. Cafes serve food via mechanical apparatus where buttons indicate desires.
*   **Combat & Threats:** Green Warriors attack on flying mounts (thoats) using metal-shod spears and long-swords. They are described as "green monsters" with unmanageable animals when frightened.
*   **Ceremony Details:** The decoration ceremony involves a concourse of civilians and troops assembled on the plain; naval vessels fill the sky with streamers. Decorations are metal ornaments placed on the left arm.
*   **Character Appearance:** John Carter is recognized by his ability to bounce like a rubber ball (color change) and his Earth-like appearance compared to Martians. Woola is described as a huge brute of an undomesticated species.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Zodanga City Environment Index

## Extracted Environments

| Asset ID | Environment Name | Role | Primary Features |
|----------|------------------|------|------------------|
| zodanga_city_main | Zodanga Walled City | Primary Setting | Central plaza, raised residences on metal columns, palace buildings |
| central_plaza | Zodanga Central Plaza | Transit/Primary Setting | Square mile open space, bounded by palaces and public buildings |
| palace_than_kosis | Palace of Than Kosis | Secondary Setting | Raised quarters, ceremonial decorations, naval vessels in sky |
| plain_ceremony | Plain Before City | Primary Setting | Concourse of civilians and troops, streamers-filled sky |

## Environment Families Included

- zodanga_city_main: Main walled city structure with central plaza
- central_plaza: Open square mile area bounded by architecture
- palace_than_kosis: Than Kosis palace interior and exterior
- plain_ceremony: Ceremonial gathering space before the city

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodanga_city_main

[[SECTION markdown]]
# Zodanga Walled City

## Environment Role
Primary Setting - Main walled city structure with central plaza and residential areas

## Architecture & Geography
- Raised residences mounted on metal columns resembling steel tree trunks
- Shops positioned at ground level (not raised)
- Vast central plaza covering approximately square mile area
- Bounded by palaces and public buildings
- Walled city entrance with gates

## Lighting & Atmosphere Cues
- Earth-like appearance compared to native Martians
- Metal ornaments visible on left arm during ceremonies
- Naval vessels fill sky with streamers during decoration events
- Daylight conditions for outdoor plaza activities

## Scale Cues & Environmental Anchors
- Residences elevated high above ground level
- Shops at street level creating vertical contrast
- Palace buildings marking city boundaries
- Central plaza as open gathering space
- City gates serving entrance/exit points

## Descriptive Noun Phrases
- "Raised metal column residences"
- "Ground-level commercial shops"
- "Square mile central plaza"
- "Palace-bounded city perimeter"
- "Walled city entrance gates"
- "Steel tree trunk columns"
- "Ceremonial metal ornament decorations"
- "Naval vessel streamer displays"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: central_plaza

[[SECTION markdown]]
# Zodanga Central Plaza

## Environment Role
Transit/Primary Setting - Open square mile area bounded by palaces and public buildings

## Architecture & Geography
- Square mile open space covering vast area
- Bounded by palace structures on perimeter
- Public buildings surrounding plaza edges
- Ground-level commercial access points
- Open-air gathering space for ceremonies

## Lighting & Atmosphere Cues
- Daylight conditions for outdoor activities
- Streamers visible in sky during naval vessel displays
- Open sky above plaza area
- Metal ornament decorations visible during ceremonies
- Civilian and troop assembly lighting

## Scale Cues & Environmental Anchors
- Square mile dimensions creating vast open space
- Palace buildings marking boundaries
- Public buildings defining perimeter edges
- Ground-level access points for entry/exit
- Assembly spaces for large crowds

## Descriptive Noun Phrases
- "Square mile open plaza"
- "Palace-bounded perimeter"
- "Public building clusters"
- "Ground-level commercial access"
- "Open-air ceremony space"
- "Naval vessel streamer displays"
- "Civilian assembly grounds"
- "Troop gathering areas"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: palace_than_kosis

[[SECTION markdown]]
# Palace of Than Kosis

## Environment Role
Secondary Setting - Than Kosis palace interior and exterior with ceremonial quarters

## Architecture & Geography
- Raised palace structure with elevated quarters
- Interior spaces for decoration ceremonies
- Exterior grounds visible during naval vessel displays
- Palace entrance areas for access
- Quarters granted to decorated individuals

## Lighting & Atmosphere Cues
- Metal ornament decorations on left arm during ceremonies
- Naval vessels fill sky with streamers above palace
- Daylight conditions for outdoor ceremony events
- Ceremonial lighting for decoration events
- Open sky visible from palace grounds

## Scale Cues & Environmental Anchors
- Palace structure elevated above surrounding areas
- Quarters positioned within palace complex
- Ceremony concourse assembled on plain before palace
- Naval vessels visible in sky above palace grounds
- Metal ornament decorations as visual markers

## Descriptive Noun Phrases
- "Elevated palace quarters"
- "Ceremonial decoration spaces"
- "Palace exterior grounds"
- "Metal ornament arm decorations"
- "Naval vessel streamer displays"
- "Ceremony concourse areas"
- "Palace entrance access points"
- "Ground-level ceremony assembly"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plain_ceremony

[[SECTION markdown]]
# Plain Before City

## Environment Role
Primary Setting - Ceremonial gathering space before the city with naval vessel displays

## Architecture & Geography
- Open plain area before walled city
- Concourse space for civilian and troop assembly
- Ground-level ceremony gathering area
- Naval vessels visible in sky above plain
- Streamer-filled sky during decoration events

## Lighting & Atmosphere Cues
- Daylight conditions for outdoor ceremony activities
- Naval vessels fill sky with streamers
- Metal ornament decorations visible during ceremonies
- Open sky above plain area
- Civilian and troop assembly lighting

## Scale Cues & Environmental Anchors
- Large open plain space for mass gatherings
- City boundaries visible in distance
- Naval vessels positioned in sky above plain
- Ceremony concourse assembled on plain surface
- Streamer displays creating vertical visual elements

## Descriptive Noun Phrases
- "Ceremonial plain gathering"
- "Civilian and troop concourse"
- "Naval vessel streamer displays"
- "Metal ornament decoration areas"
- "Open sky ceremony space"
- "City-bounded plain perimeter"
- "Ground-level assembly grounds"
- "Streamer-filled sky displays"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
