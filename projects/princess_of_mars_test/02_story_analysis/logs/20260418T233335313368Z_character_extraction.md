# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:33:35.313368+00:00
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

Chapter id: CH008

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

**Story Summary**
The procession retreats to the city after an incubator ceremony. A fleet of twenty gray airships arrives from the hills, bearing strange banners. Green Martians fire a volley from building windows; ships return fire but suffer heavy damage due to suddenness and targeting tactics (wireless, officers). One ship is disabled and drifting southeast. Warriors rush to capture it, loot arms, food, water, and jewels, then burn the vessel before towing it away. The crew is dead or incapacitated. Carter observes from a window/balcony. Upon returning to the plaza, Carter sees the prisoner being dragged into a building by green Martian females.

**Visual Continuity**
*   **Ships:** Long, low, gray-painted vessels. Twenty in total initially. One disabled drifting southeast.
*   **Warriors:** Green Martians. Wear spears. Some climb windows to fire. Others swarm the disabled ship from sides/windows using grappling hooks.
*   **Prisoner:** Slender, girlish figure. Naked except for highly wrought ornaments. Skin is light reddish copper color. Cheeks have crimson glow. Lips are ruby. Hair is coal black, waving, caught loosely into a strange coiffure. Eyes large and lustrous. Oval face.
*   **Environment:** Deserted city buildings with upper floors and rooftops. Valley floor. Hills beyond. Open ground/plaza.
*   **Action Details:** Banners swing from stem to stern. Devices gleam in sunlight. Fire spurs from banners/upper works upon impact. Loot includes casks of water, silks, furs, stone vessels. Burning ship drifts unguided into the distance.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH008

| Asset ID | Display Name | Role | Identification Status | Description Availability |
| :--- | :--- | :--- | :--- | :--- |
| carter | Carter | Observer / Commander | Partial (Name Only) | None (Visual Unknown) |
| prisoner | The Prisoner | Captive / Subject | Full (Visual Defined) | Detailed Visual Traits |
| green_martians | Green Martians | Warriors / Attackers | Full (Species Defined) | General Species Traits |
| green_martian_females | Green Martian Females | Captors | Full (Subset Defined) | Specific Action Group |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in the chapter summary or visual continuity notes. Visual identity cannot be confirmed for image generation purposes.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter

## Display Name
Carter

## Chapter Role
Observer / Commander (Implied)

## Physical Presence
Referenced (Observes from window/balcony)

## Physical Description
*   **Supported by Source:** None. The text provides no physical description for Carter in this chapter.
*   **Visual Identity:** Unknown. Cannot be generated based on current text.

## Costume & Silhouette
*   **Supported by Source:** None.
*   **Continuity Traits:** None recorded in this chapter.

## Uncertainty Notes
*   **Critical Missing Info:** Visual appearance is entirely undefined in the provided material. Manual description required for future image generation.
*   **Context:** Carter is identified by name but lacks physical attributes in Chapter CH008.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner
canonical_character_id: prisoner
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# prisoner

## Display Name
The Prisoner

## Chapter Role
Captive / Subject of Interest

## Physical Presence
Present (Being dragged into a building)

## Physical Description
*   **Supported by Source:** Detailed visual description provided in Visual Continuity notes.
    *   **Figure:** Slender, girlish.
    *   **Skin:** Light reddish copper color.
    *   **Face:** Oval face with large and lustrous eyes.
    *   **Features:** Cheeks have crimson glow; Lips are ruby.
    *   **Hair:** Coal black, waving, caught loosely into a strange coiffure.
*   **Attire:** Naked except for highly wrought ornaments.

## Costume & Silhouette
*   **Supported by Source:** Highly wrought ornaments (jewelry/accessories).
*   **Continuity Traits:** Distinctive copper skin tone and glowing cheeks are key visual markers.

## Uncertainty Notes
*   **Status:** Visual identity is fully defined within the context of this chapter. No manual description required for image generation based on current text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martians
canonical_character_id: green_martians
aliases: warriors
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# green_martians

## Display Name
Green Martians

## Chapter Role
Warriors / Attackers

## Physical Presence
Present (Firing volleys, capturing ships)

## Physical Description
*   **Supported by Source:** Species traits defined in Visual Continuity notes.
    *   **Species:** Green Martians (implied green skin tone).
    *   **Equipment:** Wear spears.
    *   **Actions:** Climb windows to fire; swarm disabled ship from sides/windows using grappling hooks.
*   **Visual Identity:** Defined by species name and equipment usage.

## Costume & Silhouette
*   **Supported by Source:** Spears as primary weapon/tool.
*   **Continuity Traits:** Capable of vertical movement (climbing windows) and aerial/ground assault tactics.

## Uncertainty Notes
*   **Status:** Visual identity is defined by species classification and equipment. No manual description required for general representation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_females
canonical_character_id: green_martian_females
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# green_martian_females

## Display Name
Green Martian Females

## Chapter Role
Captors / Draggers

## Physical Presence
Present (Dragging prisoner into a building)

## Physical Description
*   **Supported by Source:** Subset of Green Martians. Inherits species traits (green skin, etc.).
    *   **Specific Action:** Identified as the group dragging the prisoner into the building upon return to the plaza.
*   **Visual Identity:** Defined by species classification and specific action role.

## Costume & Silhouette
*   **Supported by Source:** Spears (inherited from general Green Martians).
*   **Continuity Traits:** Distinguished from male warriors by gender and specific capture action in this chapter.

## Uncertainty Notes
*   **Status:** Visual identity is defined by species classification and specific role within the group. No manual description required for image generation based on current text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
