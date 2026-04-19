# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:50:27.186220+00:00
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

# Chapter Summary: CH008 - A Fair Captive from the Sky

## Visual Continuity Facts
- **Airships:** Long, low, gray-painted vessels with banners and upper works; drift southeast after burning.
- **Warriors:** Green-skinned Martians wearing chariots or mounted on mastodons; carry spears and firearms.
- **Captive:** Slender, girlish figure; light reddish copper skin; coal black hair in loose coiffure; naked save for ornaments.
- **Environment:** Open valley, city buildings with upper floors/windows, outlying hills.

## Narrative Beats
1.  **Return Order:** Carter and Sola return home after incubation ceremony but retreat immediately upon seeing airships.
2.  **Fleet Arrival:** Twenty gray ships approach; Green warriors fire a volley from building windows.
3.  **Battle Exchange:** Fleet returns fire with guns; Green warriors demonstrate high accuracy targeting crew/apparatus.
4.  **Retreat & Crash:** Fleet limps away; one unmanned ship drifts toward city buildings, fifty feet above ground.
5.  **Looting & Burning:** Warriors swarm the crashed ship, loot arms/food/water, tow it out, then burn it while drifting southeast.
6.  **Emotional Reaction:** Carter feels depressed, interpreting the event as a defeat of his people rather than a victory.
7.  **Captive Discovery:** As Carter returns to plaza, he sees a human woman being dragged into a building by Green Martians.
8.  **Failed Interaction:** Woman looks at Carter; he fails to signal help due to ignorance of customs; she is dragged away in dejection.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH008

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|------------------------|---------|------------------|----------------------------|------------------------|
| carter_ch008 | Carter | - | true | true | false |
| sola_ch008 | Sola | - | true | true | false |
| captive_human_ch008 | The Captive/Human Woman | - | false | true | true |

**Notes:**
- Carter and Sola have no physical/visual description in this chapter for image generation
- The Captive has visual details but lacks stable identification (unnamed, unclear origin)
- All three require manual descriptions for dependable later rendering
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter_ch008
canonical_character_id: Carter
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description, facial features, or visual details provided in chapter summary for image generation; only narrative actions and emotional states documented
clarification_required: false
clarification_reason: -
clarification_question: -
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Carter

**Display Name:** Carter  
**Chapter Role:** Protagonist, Witness to Martian Attack  
**Physical Presence:** Present (sees captive, feels depressed after battle)  

## Physical Description
*Not supported by source material in this chapter.*

## Costume & Silhouette
*Not supported by source material in this chapter.*

## Continuity-Critical Traits
- Returns home after incubation ceremony with Sola  
- Interprets airship fleet retreat as defeat of his people  
- Fails to signal help to captive due to ignorance of customs  
- Emotionally affected by battle outcome  

## Render-Facing Prompt Notes
- Requires manual description for dependable image generation  
- Emotional state: depressed, concerned about people's safety  
- Cultural context: unfamiliar with Martian customs  
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_ch008
canonical_character_id: Sola
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description, facial features, or visual details provided in chapter summary for image generation; only mentioned as returning home with Carter
clarification_required: false
clarification_reason: -
clarification_question: -
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Companion to Carter, Witness to Martian Attack  
**Physical Presence:** Referenced (returns home with Carter)  

## Physical Description
*Not supported by source material in this chapter.*

## Costume & Silhouette
*Not supported by source material in this chapter.*

## Continuity-Critical Traits
- Returns home after incubation ceremony with Carter  
- Retreats immediately upon seeing airships  
- No individual actions or dialogue documented in this chapter  

## Render-Facing Prompt Notes
- Requires manual description for dependable image generation  
- Limited information available; may need clarification on relationship to Carter  
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captive_human_ch008
canonical_character_id: The Captive/Human Woman
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Visual description provided (slender, girlish figure; light reddish copper skin; coal black hair in loose coiffure; naked save for ornaments) but lacks stable identification (unnamed, unclear origin beyond being human woman dragged by Martians); cannot reliably generate images without clarification on identity and background
clarification_required: true
clarification_reason: Character is visually described but not named; unclear if this is a specific known character or generic captive; need to determine if she has established identity in broader narrative
clarification_question: Is this human woman a specific named character from the broader Princess of Mars narrative, or a generic captive without individual identity? If named, what is her canonical name and background?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# The Captive/Human Woman

**Display Name:** The Captive/Human Woman  
**Chapter Role:** Human Prisoner, Witness to Carter's Helplessness  
**Physical Presence:** Referenced (seen being dragged by Martians)  

## Physical Description
- Slender, girlish figure  
- Light reddish copper skin tone  
- Coal black hair in loose coiffure  
- Naked save for ornaments  

## Costume & Silhouette
- Wears only ornaments (no clothing specified)  
- Being dragged into building by Green Martians  

## Continuity-Critical Traits
- Carter sees her being dragged but fails to signal help due to ignorance of customs  
- Woman looks at Carter in dejection before being taken away  
- Represents failed cross-cultural interaction in this chapter  

## Render-Facing Prompt Notes
- Visual description supported but identification unclear  
- Requires clarification on whether she is a specific named character or generic captive  
- Emotionally distressed (dejected, helpless)  
- Cultural context: human woman captured by Martians  
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
