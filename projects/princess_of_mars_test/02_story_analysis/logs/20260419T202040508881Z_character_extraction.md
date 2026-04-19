# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:20:40.508881+00:00
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

Chapter id: CH012

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

# Chapter Summary: A Prisoner With Power

## Story Summary
**Scene 1: Audience with Lorquas Ptomel**
Carter is summoned to Lorquas Ptomel's audience chamber. Lorquas addresses Carter, acknowledging his prowess but emphasizing his status as an alien prisoner who commands obedience. Accusations are raised regarding a plot to escape with the "red girl" (Dejah Thoris). Lorquas warns that execution would follow if these accusations are proven, citing justice and custom. He specifically threatens that if Carter runs off with the red girl, he will have to answer to Tal Hajus and Tars Tarkas, risking his own life.

**Scene 2: Reflection and Meeting Tars Tarkas**
Carter leaves the chamber, realizing this is Sarkoja's persecution. He reflects on Dejah Thoris' safety at Tal Hajus' headquarters. Tars Tarkas approaches Carter in the plaza with unchanged demeanor. They discuss Carter's quarters; Tars Tarkas offers him a choice of floors in a building adjoining Sola's charges (later clarified as occupied by warriors).

**Scene 3: Spoils and Thark Customs Explanation**
Women arrive bearing spoils from the two chieftains Carter killed, including weapons, silks, furs, jewels, food, and cooking utensils. Tars Tarkas explains that these items are now Carter's by custom. He elaborates on Thark customs regarding women in retinues: they are not wives but community property, managed for instruction and sustenance. Carter declines assistance beyond food preparation and arms care.

**Scene 4: Quarters Selection and Communication Plan**
Carter ascends the winding corridor to select quarters. He chooses a front room on the third floor because it brings him nearer to Dejah Thoris' apartment on the second floor of the adjoining building. He intends to rig up a means of communication for her to signal him.

## Visual Continuity Facts
**Locations:**
- **Audience Chamber:** Interior space where Lorquas Ptomel resides; features great, hideous eyes and audience seating.
- **Plaza:** Open area outside the buildings where Carter meets Tars Tarkas after leaving the chamber.
- **Building Complex (Carter's Quarters):** Multi-story structure adjoining Dejah Thoris' residence.
    - *1st Floor:* Occupied by Tars Tarkas.
    - *2nd Floor:* Occupied by warriors and Sola's charges; Dejah Thoris resides in the adjoining building on this floor.
    - *3rd Floor:* Vacant initially, selected by Carter for his quarters.
- **Courtyard:** Enormous court overlooking back rooms of Carter's building. Overgrown with yellow moss-like vegetation but retains fountains, statuary, benches, and pergola-like structures.

**Objects & Props:**
- **Spoils Load:** Weapons, silks, furs, jewels, cooking utensils, casks of food/drink, loot from air craft.
- **Retinue Group:** Young females and youths carrying loads; described as a military unit under Carter's responsibility.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: Chapter CH012

| Name | Role | Presence Status | Description Availability |
| :--- | :--- | :--- | :--- |
| **Carter** | Protagonist, Summoned Prisoner | Physically Present | Sparse (No visual traits) |
| **Lorquas Ptomel** | Audience Chamber Host | Physically Present | Sparse (Eyes only) |
| **Dejah Thoris** | Referenced Residence Owner | Referenced Only | Sparse ("Red girl" nickname) |
| **Tars Tarkas** | Plaza Guide, Custom Explainer | Physically Present | Sparse (Demeanor only) |
| **Sarkoja** | Persecutor (Referenced) | Referenced Only | None |
| **Tal Hajus** | Authority Figure (Referenced) | Referenced Only | None |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text mentions he is an alien prisoner but provides no visual traits like build, hair, or eyes for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter

**Display Name:** Carter  
**Chapter Role:** Protagonist / Summoned Prisoner  
**Physical Presence:** Physically Present (Scenes 1-4)  

**Description:**  
Carter is the central figure summoned to Lorquas Ptomel's audience chamber. He reflects on Sarkoja's persecution and meets Tars Tarkas in the plaza. While his status as an "alien prisoner" is noted, no specific physical traits (build, hair color, eye shape) are provided in this chapter summary to support dependable image generation.  

**Continuity Traits:**  
- **Location:** Audience Chamber, Plaza, Building Complex (Quarters).  
- **Status:** Commands obedience but faces accusations regarding escape plots.  
- **Action:** Selects quarters on the third floor of a building adjoining Dejah Thoris' residence.  

**Uncertainty Notes:**  
Visual description is sparse; manual description required for rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text describes "great, hideous eyes" but lacks full body description for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Audience Chamber Host / Accuser  
**Physical Presence:** Physically Present (Scene 1)  

**Description:**  
Lorquas addresses Carter in the audience chamber, acknowledging his prowess but emphasizing his prisoner status. He raises accusations regarding a plot to escape with Dejah Thoris ("red girl"). While he is described as having "great, hideous eyes," no further physical traits (build, skin tone, clothing) are provided in this chapter summary.  

**Continuity Traits:**  
- **Location:** Audience Chamber.  
- **Action:** Warns Carter of execution if accusations are proven; cites justice and custom.  
- **Status:** Host to the prisoner.  

**Uncertainty Notes:**  
Visual description is sparse (eyes only); manual description required for rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: red girl
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only identified by nickname "red girl" and location; no physical traits like build or costume details provided in this chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

**Display Name:** Dejah Thoris  
**Chapter Role:** Referenced Residence Owner / Plot Subject  
**Physical Presence:** Referenced Only (Not physically present in scenes)  

**Description:**  
Dejah Thoris is referenced as the "red girl" by Lorquas Ptomel and Tars Tarkas. Her safety at Tal Hajus' headquarters is discussed, and she resides on the second floor of the adjoining building. No specific physical traits (build, hair color beyond nickname implication, costume) are provided in this chapter summary to support dependable image generation.  

**Continuity Traits:**  
- **Location:** Second Floor, Adjoining Building.  
- **Status:** Subject of escape plot accusations; Carter intends to rig communication for her.  
- **Action:** None (Referenced).  

**Uncertainty Notes:**  
Visual description is sparse (nickname only); manual description required for rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text mentions "unchanged demeanor" but provides no visual traits like build, hair, or eyes for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

**Display Name:** Tars Tarkas  
**Chapter Role:** Plaza Guide / Custom Explainer  
**Physical Presence:** Physically Present (Scenes 2-3)  

**Description:**  
Tars Tarkas approaches Carter in the plaza with unchanged demeanor. He discusses Carter's quarters and explains Thark customs regarding women in retinues. While his demeanor is noted, no specific physical traits (build, hair, eyes) are provided in this chapter summary to support dependable image generation.  

**Continuity Traits:**  
- **Location:** Plaza, Building Complex (1st Floor).  
- **Action:** Offers Carter a choice of floors; explains spoils and customs.  
- **Status:** Maintains unchanged demeanor throughout interaction.  

**Uncertainty Notes:**  
Visual description is sparse (demeanor only); manual description required for rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only mentioned by name in context of persecution; no visual traits provided.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja

**Display Name:** Sarkoja  
**Chapter Role:** Persecutor (Referenced)  
**Physical Presence:** Referenced Only (Not physically present in scenes)  

**Description:**  
Sarkoja is referenced by Carter as the source of his persecution ("this is Sarkoja's persecution"). No physical traits, visual description, or specific identifiers are provided in this chapter summary to support dependable image generation.  

**Continuity Traits:**  
- **Location:** None specified (Referenced).  
- **Status:** Accused of persecuting Carter.  
- **Action:** None (Referenced).  

**Uncertainty Notes:**  
Visual description is sparse (none); manual description required for rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only mentioned by name; no visual traits provided.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus

**Display Name:** Tal Hajus  
**Chapter Role:** Authority Figure (Referenced)  
**Physical Presence:** Referenced Only (Not physically present in scenes)  

**Description:**  
Tal Hajus is referenced by Lorquas Ptomel as the authority Carter would answer to ("answer to Tal Hajus"). No physical traits, visual description, or specific identifiers are provided in this chapter summary to support dependable image generation.  

**Continuity Traits:**  
- **Location:** Headquarters (Referenced).  
- **Status:** Authority figure overseeing Dejah Thoris' safety.  
- **Action:** None (Referenced).  

**Uncertainty Notes:**  
Visual description is sparse (none); manual description required for rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
