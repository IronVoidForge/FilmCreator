# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:38:57.147708+00:00
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

- every character record must include a non-empty markdown section

- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown

- never omit the markdown section for any character record



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

**Visual Continuity Facts:**
- **Location:** Upper floor of a building in the deserted city, overlooking the valley.
- **Characters:** Narrator (I), Sola, Woola (hound). Lorquas Ptomel mentioned as staying at the city.
- **Enemy Ship:** Gray-painted, low craft, drifting ~50 feet above ground, unmanned/dead crew visible.
- **Prisoner:** Slender girlish figure, coal black hair, light reddish copper skin, naked except ornaments, oval face, large eyes.
- **Action:** Enemy fleet retreats after being fired upon; one ship captured and burned; prisoner dragged into building by females.

**Broad Story Summary:**
On the third day post-incubator ceremony, the procession retreats due to enemy air fleet arrival. The narrator watches from a window as green Martians fire a volley at the approaching ships. The battle results in the destruction of the enemy fleet and the capture of one flagship. After looting and burning the ship, Martian warriors bring a human female prisoner into the city. The narrator sees her face, she makes a sign for help which he fails to answer due to ignorance of customs, and she is dragged away into the building.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
| Asset ID | Canonical Character ID | Status |
| :--- | :--- | :--- |
| narrator_i | narrator_i | Fully Identified (Description Missing) |
| sola | sola | Fully Identified (Description Missing) |
| woola | woola | Fully Identified (Description Missing) |
| lorquas_ptomel | lorquas_ptomel | Fully Identified (Description Missing) |
| prisoner_human_female | prisoner_human_female | Fully Identified (Description Present) |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_i
canonical_character_id: narrator_i
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary describes the narrator's actions and observations but does not provide specific physical details such as height, build, or skin tone for the narrator themselves.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator (I)

**Chapter Role:** Observer / Battle Participant  
**Presence:** Physically Present (Watching from window)  

## Physical Description
*   **Source Support:** None provided in this chapter summary.  
*   **Known Traits:** Human (implied by contrast to Martians and prisoner).  

## Costume & Silhouette
*   **Source Support:** None provided.  
*   **Continuity Notes:** Wearing standard attire for the city dwellers or procession participants (inferred from context of "procession retreats").  

## Uncertainty Notes
> **Critical Missing Detail:** The narrator's specific physical appearance is not described in this chapter. For image generation, a default human form must be assumed or clarified based on broader story context outside this specific summary.  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The character is named in the visual continuity facts but no physical description or visual traits are provided in this chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

**Chapter Role:** Companion / Warrior (Contextual)  
**Presence:** Referenced / Present  

## Physical Description
*   **Source Support:** None provided in this chapter summary.  
*   **Known Traits:** Named character associated with the procession/fleet.  

## Costume & Silhouette
*   **Source Support:** None provided.  
*   **Continuity Notes:** Likely wearing attire consistent with city dwellers or warriors (inferred from context).  

## Uncertainty Notes
> **Critical Missing Detail:** Sola's physical appearance is not described in this chapter. For image generation, a default form must be assumed or clarified based on broader story context outside this specific summary.  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Identified as a hound, but specific breed, size, coat color, or markings are not detailed in the supplied material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola

**Chapter Role:** Hound / Companion  
**Presence:** Physically Present  

## Physical Description
*   **Source Support:** Identified as a hound.  
*   **Known Traits:** Canine species.  

## Costume & Silhouette
*   **Source Support:** None provided.  
*   **Continuity Notes:** Standard dog anatomy (inferred).  

## Uncertainty Notes
> **Critical Missing Detail:** Specific breed, size, coat color, or markings are not described in this chapter. For image generation, a generic hound form must be assumed or clarified based on broader story context outside this specific summary.  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Mentioned as staying at the city, but no physical description is provided in this chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

**Chapter Role:** City Resident  
**Presence:** Referenced (Staying at city)  

## Physical Description
*   **Source Support:** None provided in this chapter summary.  
*   **Known Traits:** Human or Martian resident of the city (inferred from context).  

## Costume & Silhouette
*   **Source Support:** None provided.  
*   **Continuity Notes:** Likely wearing attire consistent with city dwellers (inferred from context).  

## Uncertainty Notes
> **Critical Missing Detail:** Lorquas Ptomel's physical appearance is not described in this chapter. For image generation, a default form must be assumed or clarified based on broader story context outside this specific summary.  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_human_female
canonical_character_id: prisoner_human_female
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Human Female Prisoner

**Chapter Role:** Captive / Subject of Observation  
**Presence:** Physically Present (Dragged into building)  

## Physical Description
*   **Source Support:** Detailed description provided in chapter summary.  
*   **Body Type:** Slender girlish figure.  
*   **Hair:** Coal black hair.  
*   **Skin Tone:** Light reddish copper skin.  
*   **Face:** Oval face, large eyes.  

## Costume & Silhouette
*   **Source Support:** Described as naked except ornaments.  
*   **Accessories:** Ornaments (specific type not detailed).  
*   **Silhouette:** Human female form.  

## Continuity Notes
> The prisoner is a key visual element in this chapter, serving as the focal point of the narrator's observation and the Martians' capture action. Her appearance contrasts with the "green Martians" and the "gray-painted enemy ship."  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
