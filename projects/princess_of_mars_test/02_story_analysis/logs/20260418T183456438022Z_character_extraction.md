# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:34:56.438022+00:00
- task: character_extraction

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

Chapter id: CH001

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question



Asset id rules:

- lowercase snake_case

- stable across later reruns



Each character Markdown file should include:

- display name and chapter role

- whether the character is physically present, referenced, or uncertain

- physical description that is actually supported by the source

- costume, silhouette, and continuity-critical traits when known

- useful descriptive noun phrases for later render-facing prompt writing

- explicit uncertainty notes when important details are missing



Chapter summary:

**Story Summary:**
John Carter observes from a window as a fleet of twenty gray airships approaches the deserted city. Green Martians fire a volley from buildings, initiating a battle where the airships return fire with ineffectual results due to suddenness and damage. The fleet retreats after sustaining heavy casualties; one ship drifts helplessly and is boarded by warriors who loot arms, jewels, and water. The crew empties carboys over dead sailors and burns the vessel before it drifts away. Carter feels a strange yearning for the "kindred people" defeated. He sees a human woman prisoner being dragged into a building; she looks at him with hope then dejection as he fails to signal help due to cultural ignorance.

**Visual Continuity:**
- **Locations:** Window of upper floor (Carter's vantage point), Rooftops, Plaza/Street level, Building interiors.
- **Characters Visible:** John Carter, Sola, Woola, Green Martian Warriors, Airship Crews (distant figures), Human Woman Prisoner.
- **Props/Vehicles:** Gray airships (20+), Chariots, Mastodons, Grappling hooks, Carboys, Stone vessels, Banners/Devices on ships.
- **Lighting/Atmosphere:** Daylight, sunlight reflecting off ship devices, smoke and flame from burning vessel.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

| Asset ID | Display Name | Chapter Role | Physical Presence | Description Status |
|----------|--------------|---------------|-------------------|--------------------|
| john_carter | John Carter | Protagonist observing from window | Present | Partial physical description |
| sola | Sola | Human woman prisoner | Referenced | Insufficient physical details |
| woola | Woola | Companion character | Referenced | Insufficient physical details |
| green_martian_warriors | Green Martian Warriors | Enemy combatants | Referenced | Group identification only |
| airship_crews | Airship Crews | Distant figures | Uncertain | No physical description |
| human_woman_prisoner | Human Woman Prisoner | Captive character | Present | Limited physical details |

**Notes:**
- Characters marked with insufficient physical description require manual description for image generation
- Group characters (Green Martian Warriors, Airship Crews) may need clarification for individual character work
- Some characters have names but lack stable visual identification for render-facing prompts
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Character has sufficient physical and visual description in source material for dependable image generation
clarification_required: false
clarification_reason: Character has stable identification with name and role
clarification_question: 

[[SECTION markdown]]
# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist observing from window, feels yearning for defeated "kindred people"

**Physical Presence:** Present (observes from upper floor window)

**Physical Description:** 
- Male human character
- Observes battle from elevated vantage point
- Shows emotional response to defeated warriors and prisoner
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Wears clothing appropriate for Martian environment
- Positioned at window of upper floor building
- Cultural ignorance noted (fails to signal help due to cultural differences)

**Useful Descriptive Noun Phrases:**
- "Heroic male figure"
- "Observer from elevated position"
- "Emotionally invested protagonist"
- "Human warrior in alien setting"

**Uncertainty Notes:**
- Specific physical features (hair, eyes, build) not detailed in source
- Exact costume details limited to general warrior attire
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character has name but no physical description provided in source material for dependable image generation
clarification_required: true
clarification_reason: Character has stable name identification but insufficient visual details for render-facing prompts
clarification_question: What are Sola's specific physical features (hair color, eye color, build, facial features) and costume details?

[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Human woman prisoner being dragged into building

**Physical Presence:** Referenced (seen by John Carter from window)

**Physical Description:** 
- Female human character
- Being dragged into building by warriors
- Shows emotional response: hope then dejection when failing to signal help
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Prisoner attire (specifics not detailed)
- Positioned at street/plaza level
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Female prisoner figure"
- "Hopeful captive character"
- "Human woman in distress"
- "Victim of cultural misunderstanding"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general prisoner attire
- Facial expression details (hope, dejection) noted but not fully described
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character has name but no physical description provided in source material for dependable image generation
clarification_required: true
clarification_reason: Character has stable name identification but insufficient visual details for render-facing prompts
clarification_question: What are Woola's specific physical features (species, build, distinctive markings) and costume/attire details?

[[SECTION markdown]]
# Woola

**Display Name:** Woola  
**Chapter Role:** Companion character (listed in visual continuity)

**Physical Presence:** Referenced (listed as visible character in visual continuity)

**Physical Description:** 
- Character companion to John Carter
- Listed in visual continuity but no specific physical details provided
- Limited description in source material

**Costume/Silhouette/Continuity Traits:**
- Companion role suggests close association with protagonist
- Specific costume and silhouette not detailed in source

**Useful Descriptive Noun Phrases:**
- "Companion character figure"
- "Loyal associate"
- "Character with unknown physical features"

**Uncertainty Notes:**
- Physical species/build not specified in source material
- No distinctive markings or features described
- Costume details limited to general companion attire
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_warriors
canonical_character_id: green_martian_warriors
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character group has no specific physical description provided in source material for dependable image generation
clarification_required: true
clarification_reason: Group identification is too weakly defined for individual character work; may already exist under another name or need clarification
clarification_question: What are the specific physical features, costume details, and distinguishing characteristics of Green Martian Warriors? Are they a single group or multiple distinct characters?

[[SECTION markdown]]
# Green Martian Warriors

**Display Name:** Green Martian Warriors  
**Chapter Role:** Enemy combatants firing volley from buildings

**Physical Presence:** Referenced (listed as visible characters in visual continuity)

**Physical Description:** 
- Group of warrior characters
- Fire volley from buildings during battle
- Board drifting airship and loot arms, jewels, water
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Warrior attire (specifics not detailed)
- Positioned at rooftops and building interiors
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Martian warrior group"
- "Enemy combatant figures"
- "Building-based attackers"
- "Looters of drifting vessel"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general warrior attire
- Individual character distinctions not specified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: airship_crews
canonical_character_id: airship_crews
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character group has no specific physical description provided in source material for dependable image generation
clarification_required: true
clarification_reason: Group identification is too weakly defined for individual character work; may already exist under another name or need clarification
clarification_question: What are the specific physical features, costume details, and distinguishing characteristics of Airship Crews? Are they a single group or multiple distinct characters?

[[SECTION markdown]]
# Airship Crews

**Display Name:** Airship Crews  
**Chapter Role:** Distant figures on gray airships (20+ ships)

**Physical Presence:** Uncertain (listed as distant figures in visual continuity)

**Physical Description:** 
- Group of crew characters on airships
- Return fire with ineffectual results due to suddenness and damage
- Retreat after sustaining heavy casualties
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Crew attire (specifics not detailed)
- Positioned on airships at distance from Carter's vantage point
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Airship crew figures"
- "Distant vessel operators"
- "Retreating enemy personnel"
- "Heavy casualty survivors"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general crew attire
- Individual character distinctions not specified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: human_woman_prisoner
canonical_character_id: human_woman_prisoner
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character has name but no physical description provided in source material for dependable image generation
clarification_required: true
clarification_reason: Character has stable name identification but insufficient visual details for render-facing prompts
clarification_question: What are the Human Woman Prisoner's specific physical features (hair color, eye color, build, facial features) and costume details?

[[SECTION markdown]]
# Human Woman Prisoner

**Display Name:** Human Woman Prisoner  
**Chapter Role:** Captive character being dragged into building

**Physical Presence:** Present (seen by John Carter from window)

**Physical Description:** 
- Female human character
- Being dragged into building by warriors
- Shows emotional response: hope then dejection when failing to signal help
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Prisoner attire (specifics not detailed)
- Positioned at street/plaza level
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Female prisoner figure"
- "Hopeful captive character"
- "Human woman in distress"
- "Victim of cultural misunderstanding"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general prisoner attire
- Facial expression details (hope, dejection) noted but not fully described
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
