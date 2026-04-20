# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:28:51.866566+00:00
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

Chapter id: CH013

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

# Chapter Summary: CHAPTER XIII (LOVE-MAKING ON MARS)

## Story Summary
Following the battle with air ships, the Thark community remains in the city for safety, abandoning their march home until they are assured the ships will not return. During this period of inactivity, John Carter undergoes intensive training with Tars Tarkas in Thark customs and warfare, specifically learning to ride and guide thoats. He demonstrates that kindness is more effective than violence in training these beasts, earning a reward from Lorquas Ptomel—a massive gold anklet—for his regiment of docile mounts.

On the eve of their departure march toward Thark city, John Carter arranges a secret meeting with Dejah Thoris on a great avenue leading into the plaza. They discuss the warriors' jealousy and dangerous treatment of her. An intimate moment occurs where John places his arm around her shoulder, confirming mutual affection. The chapter concludes with John's internal realization that he has loved Dejah Thoris since their first meeting in Korad, solidifying their bond despite the hostile environment.

## Visual Continuity Facts
### Locations and Environment
- **City Courtyard/Plaza:** Where the community resides and where training takes place.
- **Great Avenue:** Leads into the plaza from the east; setting for the secret meeting.
- **Martian Night:** Lighted by two moons, with Earth visible in the luminous green eye above.

### Objects and Artifacts
- **Thoats:** Great beasts used as mounts; dangerous but tractable when trained.
- **Pistol:** Used by John to subdue unresponsive thoats during training.
- **Gold Anklet:** Reward presented by Lorquas Ptomel from his own leg.
- **Silks:** Worn by John, removed and thrown across Dejah's shoulders for warmth.
- **Radium Powder/Projectiles:** Mentioned in context of Thark warfare (exploding bullets).

### Character Actions and States
- **John Carter:** Instructed in riding, training beasts, walking with Dejah, removing silks, placing arm on shoulder.
- **Dejah Thoris:** Absent from quarters during day, walking with Sola, meeting John secretly, smiling at John's approach.
- **Tars Tarkas:** Present for instruction (past tense in specific scenes), observing John's training.
- **Lorquas Ptomel:** Present for reward ceremony (mentioned).

### Time and Sequence
- **Day to Night Transition:** Occurs during the conversation on the avenue.
- **Eve of Departure:** The meeting happens immediately before the march resumes.
- **Duration:** Several days of inactivity followed by the specific evening event.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CHAPTER XIII (LOVE-MAKING ON MARS)

| Character | Asset ID | Status | Description Quality |
|-----------|----------|--------|---------------------|
| John Carter | john_carter | Present/Referenced | Well-documented with physical actions |
| Dejah Thoris | dejah_thoris | Referenced/Present | Visual details supported by source |
| Tars Tarkas | tars_tarkas | Referenced | Past tense instruction scenes |
| Lorquas Ptomel | lorquas_ptomel | Referenced | Minimal visual detail |

*Note: All characters extracted from Chapter XIII. Physical descriptions vary in completeness.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter XIII

**Display Name:** John Carter  
**Chapter Role:** Protagonist, Active Participant in Training and Romance Scene  
**Physical Presence:** Present throughout chapter (training beasts, walking with Dejah)  

**Supported Physical Description:**  
- Instructed in riding thoats by Tars Tarkas  
- Demonstrates kindness over violence when training beasts  
- Removes silks from body to throw across Dejah's shoulders  
- Places arm around Dejah Thoris' shoulder during intimate moment  
- Uses pistol to subdue unresponsive thoats  

**Costume/Silhouette Traits:**  
- Wears silks (removed and thrown)  
- No specific costume details beyond silks mentioned  

**Continuity-Critical Notes:**  
- Shows mutual affection with Dejah Thoris  
- Internal realization of love since first meeting in Korad  
- Reward recipient: gold anklet from Lorquas Ptomel  

**Uncertainty Notes:**  
- Specific facial features not described in source material  
- Height/weight measurements absent from chapter text
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter XIII

**Display Name:** Dejah Thoris  
**Chapter Role:** Love Interest, Secret Meeting Partner  
**Physical Presence:** Referenced throughout, present for secret meeting on avenue  

**Supported Physical Description:**  
- Walking with Sola during day (absent from quarters)  
- Smiles at John's approach during secret meeting  
- Receives silks thrown across shoulders for warmth  
- Discusses warriors' jealousy and dangerous treatment of her  

**Costume/Silhouette Traits:**  
- Silks worn (receives John's removed silks)  
- No specific costume details beyond silks mentioned  

**Continuity-Critical Notes:**  
- Mutual affection confirmed with John Carter  
- Jealous warriors' treatment discussed openly  
- Meeting occurs on eve of departure march toward Thark city  

**Uncertainty Notes:**  
- Specific facial features not described in source material  
- Height/weight measurements absent from chapter text
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only referenced in past tense instruction scenes; no physical description provided for image generation support
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Chapter XIII

**Display Name:** Tars Tarkas  
**Chapter Role:** Trainer/Instructor, Past Reference  
**Physical Presence:** Referenced (past tense in specific instruction scenes)  

**Supported Physical Description:**  
- Instructs John Carter in Thark customs and warfare  
- Observes John's training with thoats  
- No physical description provided in chapter text  

**Costume/Silhouette Traits:**  
- No costume details mentioned in source material  

**Continuity-Critical Notes:**  
- Past tense reference indicates instruction completed before current scenes  
- Associated with Thark community and warfare traditions  

**Uncertainty Notes:**  
- Physical appearance completely absent from chapter description  
- Cannot support dependable image generation without manual description  
- Silhouette and costume traits unknown
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only mentioned as present for reward ceremony; no physical description provided for image generation support
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel - Chapter XIII

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Reward Presenter, Community Member  
**Physical Presence:** Referenced (present for reward ceremony)  

**Supported Physical Description:**  
- Presents gold anklet as reward to John Carter  
- Removes anklet from own leg to give as reward  
- No physical description provided in chapter text  

**Costume/Silhouette Traits:**  
- No costume details mentioned in source material  

**Continuity-Critical Notes:**  
- Associated with Thark community and reward traditions  
- Gold anklet specifically noted as coming from his own leg  

**Uncertainty Notes:**  
- Physical appearance completely absent from chapter description  
- Cannot support dependable image generation without manual description  
- Silhouette and costume traits unknown
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
