# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:55:25.785431+00:00
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

- if clarification is not required, still include clarification_reason and clarification_question as empty values



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

# Chapter Title
Chapter VIII - A Fair Captive from the Sky

# Scene 1: Return to City & Observation
**Action:** The procession returns to the city after the incubator ceremony. Orders are given for immediate retreat. Narrator climbs to an upper floor window to observe the cause of the sudden scurrying.
**Visuals:** Green Martians melting into building doorways like mist. View of valley and hills from window.
**Key Detail:** The narrator identifies a huge gray craft swinging over the crest of the nearest hill as the cause.

# Scene 2: Fleet Arrival & Battle Initiation
**Action:** Twenty gray ships appear, sailing slowly toward the city. Martians fire a terrific volley from building windows. Fleet returns fire with guns.
**Visuals:** Gray ships with banners and devices gleaming in sunlight. Figures crowding forward decks. Window firing positions.
**Key Detail:** The first volley catches ship crews unprepared. Bullets drop figures at explosions; banners dissolve in spurts of flame.

# Scene 3: Fleet Maneuver & Damage Assessment
**Action:** Fleet circles to position opposite the firing line, then retreats trailing off. Several craft are limping perceptibly. One ship receives the brunt of fire and seems entirely unmanned.
**Visuals:** Ships moving parallel to front, turning back. Depleted crews controlling damaged vessels. Erratic movement of the last ship.
**Key Detail:** The last ship is drifting some fifty feet above ground, helpless and unable to escape.

# Scene 4: Drifting Ship Rescue & Loot Operation
**Action:** Warriors rush to the plain to meet the drifting ship. They board with spears and grappling hooks, hauling it to ground. Systematic rifling of the vessel begins.
**Visuals:** Bodies of crew strewn about decks. Grappling hooks thrown out. Chariots requisitioned for transport. Loot includes arms, ammunition, silks, furs, jewels, stone vessels, water casks.
**Key Detail:** The ship is towed far out into the valley in a southwesterly direction after loot removal.

# Scene 5: Ship Fire & Funeral Pyre
**Action:** Warriors empty carboys upon dead bodies and decks. Last warrior throws missile back onto vessel, causing flame spurt. Guy ropes released; ship soars majestically into air as funeral pyre.
**Visuals:** Decks and upper works a mass of roaring flames. Ship drifting to southeast, rising higher. Dim vistas of distance.
**Key Detail:** The sight is described as an awe-inspiring floating funeral pyre typifying the life story of the strange creatures.

# Scene 6: Narrator's Reaction & Prisoner Discovery
**Action:** Narrator descends to street, feeling depressed by the defeat. Sola rushes up. Cavalcade returns to plaza. Narrator enters plaza and catches glimpse of prisoner being dragged into building.
**Visuals:** Narrator emerging upon street. Throng of Martians in plaza. Building portal where prisoner is dragged.
**Key Detail:** The prisoner is a slender, girlish figure similar to earthly women, wearing highly wrought ornaments but otherwise naked.

# Scene 7: The Princess Close-Up & Interaction
**Action:** Close-up of the prisoner (Dejah Thoris). Her eyes meet narrator's. She makes a sign with free hand. Look of hope fades into dejection, loathing, and contempt. She is dragged away.
**Visuals:** Oval face, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips. Eyes large and lustrous.
**Key Detail:** Narrator realizes he did not answer her signal for succor and protection due to ignorance of Martian customs.

# Scene 8: Aftermath & Safety Measures
**Action:** Lorquas Ptomel remains at deserted city until danger passed. Fear of return attack by air craft prevents recommencement of homeward march for a week.
**Visuals:** Deserted city environment. Plaza gathering.
**Key Detail:** The city remains occupied to avoid open plains with caravan of chariots and children due to fear of fleet return or reinforcements.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VIII

| Asset ID | Canonical Character ID | Display Name | Role | Identification Status | Description Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| the_narrator | the_narrator | The Narrator | Protagonist / Observer | Fully Identified | Manual Description Required |
| dejah_thoris | dejah_thoris | Dejah Thoris | Princess / Prisoner | Fully Identified | Physically Described |
| lorquas_ptomel | lorquas_ptomel | Lorquas Ptomel | Warrior Leader | Fully Identified | Manual Description Required |
| sola | sola | Sola | Companion / Messenger | Fully Identified | Manual Description Required |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_narrator
canonical_character_id: the_narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text describes actions and emotions but lacks physical appearance details (hair, skin, build) required for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# The Narrator

## Display Name & Role
**Name:** The Narrator  
**Role:** Protagonist / Observer

## Presence Status
**Status:** Referenced / Present (implied by narrative voice)  
**Note:** Character is the primary viewpoint of the chapter.

## Physical Description
**Supported Details:** None provided in this chapter.  
**Uncertainty Notes:** No physical traits (height, build, hair color, skin tone) are described in the text. Only actions ("climbs to window", "descends to street") and emotions ("depressed") are recorded.

## Costume & Silhouette
**Details:** Unknown.  
**Continuity Traits:** None specified in this chapter.

## Render-Facing Prompt Phrases
- "Male figure observing from upper floor window"
- "Depressed expression on face"
- "Standing on street level"
- "Uncertain physical build"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: the prisoner, her
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

## Display Name & Role
**Name:** Dejah Thoris  
**Role:** Princess / Prisoner

## Presence Status
**Status:** Referenced / Present (Close-up interaction)  
**Note:** Character is the central figure of interest in this chapter.

## Physical Description
**Supported Details:** 
- Slender, girlish figure similar to earthly women.
- Oval face.
- Coal black waving hair.
- Light reddish copper skin.
- Crimson cheeks.
- Ruby lips.
- Eyes large and lustrous.
- Wearing highly wrought ornaments but otherwise naked (at time of capture).

**Uncertainty Notes:** None regarding physical appearance in this chapter.

## Costume & Silhouette
**Details:** Highly wrought ornaments; otherwise naked at moment of discovery.  
**Continuity Traits:** Distinctive copper skin tone and black hair are key identifiers for Martian royalty.

## Render-Facing Prompt Phrases
- "Slender girlish figure with oval face"
- "Coal black waving hair"
- "Light reddish copper skin"
- "Crimson cheeks and ruby lips"
- "Large lustrous eyes"
- "Wearing highly wrought ornaments"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only name and location mentioned; no physical description provided in chapter.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

## Display Name & Role
**Name:** Lorquas Ptomel  
**Role:** Warrior Leader / Local

## Presence Status
**Status:** Referenced  
**Note:** Character remains at deserted city until danger passed.

## Physical Description
**Supported Details:** None provided in this chapter.  
**Uncertainty Notes:** No physical traits (height, build, hair color, skin tone) are described in the text. Only actions ("remains at deserted city") are recorded.

## Costume & Silhouette
**Details:** Unknown.  
**Continuity Traits:** None specified in this chapter.

## Render-Facing Prompt Phrases
- "Warrior figure remaining at city"
- "Uncertain physical build"
- "Martian attire (implied)"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only name and action mentioned; no physical description provided in chapter.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

## Display Name & Role
**Name:** Sola  
**Role:** Companion / Messenger

## Presence Status
**Status:** Referenced  
**Note:** Character rushes up to the narrator.

## Physical Description
**Supported Details:** None provided in this chapter.  
**Uncertainty Notes:** No physical traits (height, build, hair color, skin tone) are described in the text. Only action ("rushes up") is recorded.

## Costume & Silhouette
**Details:** Unknown.  
**Continuity Traits:** None specified in this chapter.

## Render-Facing Prompt Phrases
- "Figure rushing to narrator"
- "Uncertain physical build"
- "Martian attire (implied)"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
