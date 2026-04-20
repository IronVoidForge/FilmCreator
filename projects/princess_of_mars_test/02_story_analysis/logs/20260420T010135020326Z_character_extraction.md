# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:01:35.020326+00:00
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

Chapter id: CH010

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

# Chapter Summary: CH010 - "CHAMPION AND CHIEF"

**Broad Story Summary:**
John Carter explores the city limits with Woola, bonding through affection before returning to the audience chamber where Dejah Thoris is held captive. Lorquas Ptomel questions Dejah Thoris regarding her expedition from Helium. A young Thark warrior insults and strikes Dejah Thoris during the proceedings. John Carter intervenes, killing the warrior in a fierce combat sequence. He assumes the dead warrior's chieftain status and regalia. Following the fight, he tends to Dejah Thoris's injuries. They engage in a significant conversation where John Carter reveals his name and origin (Virginia, Earth). Tars Tarkas explains Martian customs regarding prisoners and chieftains. John Carter asserts his moral stance against harming Dejah Thoris. He leaves the chamber with Dejah Thoris and Woola, passing through the audience hall in silence.

**Visual Continuity Facts:**
*   **Location:** Audience Chamber of Lorquas Ptomel (steps of rostrum, benches at side).
*   **Status Markers:** John Carter wears regalia of a Thark chieftain (arms, ornaments) transferred from the dead warrior.
*   **Key Props:** Silk from cape used to staunch blood; Woola's heavy neck/body for affection display.
*   **Character States:** Dejah Thoris has injuries (nosebleed); Warrior is bleeding and lifeless; John Carter is armed with short-sword.
*   **Movement:** Exit from audience chamber toward plaza/exit; Woola follows closely.

**Scene Decomposition Notes:**
*   **Intervention Sequence:** Focus on the transition from verbal debate to physical combat (striking face, drawing sword, hooking leg over pistol).
*   **Conversation Block:** Dialogue between John Carter and Dejah Thoris regarding identity and motivation; Tars Tarkas's explanation of customs.
*   **Departure:** Walking out together ignoring guards/harpies; establishing new dynamic as chieftain and prisoner.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH010 "CHAMPION AND CHIEF"

| Character | Role | Physical Presence | Description Status |
|-----------|------|-------------------|--------------------|
| John Carter | Protagonist, Chieftain | Present | Partial |
| Woola | Companion Animal | Present | Partial |
| Dejah Thoris | Captive Princess | Present | Partial |
| Lorquas Ptomel | Chamber Owner | Referenced | Uncertain |
| Tars Tarkas | Custom Explainer | Referenced | Uncertain |
| Young Thark Warrior | Combatant | Present | Minimal |

**Notes:** Several characters lack complete physical descriptions for reliable image generation. Clarification may be needed for some referenced characters.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical description details (height, build, hair color, eye color) for dependable image generation. Only regalia and weapon mentioned.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - CH010

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Thark Chieftain  

**Physical Presence:** Present (active participant in scene)  

**Supported Physical Description:**  
- Wears regalia of a Thark chieftain (arms, ornaments transferred from dead warrior)  
- Armed with short-sword  
- From Virginia, Earth (revealed during conversation)  

**Costume & Silhouette:**  
- Chieftain regalia including arms and ornaments  
- Silk from cape used to staunch blood (Dejah Thoris's injuries)  

**Continuity-Critical Traits:**  
- Moral stance against harming Dejah Thoris  
- Assumes dead warrior's chieftain status after combat  

**Uncertainty Notes:**  
- Height, build, hair color, eye color not specified in source material  
- Face description beyond regalia is unavailable for reliable rendering  

**Useful Descriptive Noun Phrases:**  
- "Thark chieftain with short-sword"  
- "Wearing transferred warrior regalia"  
- "Virginia-born Earth man on Mars"  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical description details (species, size, fur color) for dependable image generation. Only "heavy neck/body" mentioned for affection display.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - CH010

**Display Name:** Woola  
**Chapter Role:** Companion Animal  

**Physical Presence:** Present (follows John Carter closely)  

**Supported Physical Description:**  
- Heavy neck/body for affection display  
- Dog companion (implied by name and behavior)  

**Costume & Silhouette:**  
- No specific costume mentioned  
- Follows closely during departure sequence  

**Continuity-Critical Traits:**  
- Displays affection through physical contact  
- Remains with John Carter throughout chamber exit  

**Uncertainty Notes:**  
- Species confirmation (dog vs other canine) not explicitly stated in source  
- Size, fur color, eye color not specified for reliable rendering  
- Breed information unavailable  

**Useful Descriptive Noun Phrases:**  
- "Heavy-bodied companion dog"  
- "Affectionate follower"  
- "Loyal Mars companion"  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical description details (height, build, hair color, eye color) for dependable image generation. Only injuries and silk cape mentioned.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - CH010

**Display Name:** Dejah Thoris  
**Chapter Role:** Captive Princess  

**Physical Presence:** Present (held captive in audience chamber)  

**Supported Physical Description:**  
- Has injuries including nosebleed  
- Silk from cape used to staunch blood  

**Costume & Silhouette:**  
- Wears silk cape (used for medical purposes)  
- No specific costume details beyond cape mentioned  

**Continuity-Critical Traits:**  
- Questions regarding expedition from Helium  
- Receives care after warrior's death  
- New dynamic established as chieftain and prisoner  

**Uncertainty Notes:**  
- Height, build, hair color, eye color not specified in source material  
- Face description beyond injuries is unavailable for reliable rendering  
- Full costume details missing  

**Useful Descriptive Noun Phrases:**  
- "Princess with cape injuries"  
- "Captive receiving medical care"  
- "Helium expedition survivor"  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical description details (height, build, hair color, eye color) for dependable image generation. Only location ownership mentioned.
clarification_required: true
clarification_reason: Character named as location owner but may exist under different name or be too weakly identified for reliable rendering
clarification_question: Is Lorquas Ptomel the same character who owns this audience chamber, or is this a title/location reference?

[[SECTION markdown]]
# Lorquas Ptomel - CH010

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Audience Chamber Owner  

**Physical Presence:** Referenced (location owner)  

**Supported Physical Description:**  
- None specified in source material  
- Only mentioned as chamber owner and questioner of Dejah Thoris  

**Costume & Silhouette:**  
- No costume details available  
- No silhouette information provided  

**Continuity-Critical Traits:**  
- Questions Dejah Thoris regarding expedition from Helium  
- Location: Audience Chamber steps and benches at side  

**Uncertainty Notes:**  
- Physical appearance completely unavailable for reliable rendering  
- May be title reference rather than individual character  
- Insufficient identification for dependable image generation  

**Useful Descriptive Noun Phrases:**  
- "Audience chamber owner"  
- "Helium expedition questioner"  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical description details (height, build, hair color, eye color) for dependable image generation. Only custom explainer role mentioned.
clarification_required: true
clarification_reason: Character may exist under different name or be too weakly identified for reliable rendering; only functional role specified
clarification_question: Is Tars Tarkas a specific individual character or a title/role reference in Martian society?

[[SECTION markdown]]
# Tars Tarkas - CH010

**Display Name:** Tars Tarkas  
**Chapter Role:** Custom Explainer  

**Physical Presence:** Referenced (explains customs)  

**Supported Physical Description:**  
- None specified in source material  
- Only mentioned as explainer of Martian customs regarding prisoners and chieftains  

**Costume & Silhouette:**  
- No costume details available  
- No silhouette information provided  

**Continuity-Critical Traits:**  
- Explains Martian customs about prisoners and chieftains  
- Provides cultural context for John Carter's actions  

**Uncertainty Notes:**  
- Physical appearance completely unavailable for reliable rendering  
- May be title reference rather than individual character  
- Insufficient identification for dependable image generation  

**Useful Descriptive Noun Phrases:**  
- "Martian custom explainer"  
- "Prisoner and chieftain cultural guide"  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_thark_warrior
canonical_character_id: young_thark_warrior
aliases: dead warrior, bleeding warrior
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical description details (height, build, hair color, eye color) for dependable image generation. Only combat actions and death mentioned.
clarification_required: true
clarification_reason: Character may exist under different name or be too weakly identified for reliable rendering; only functional role as combatant specified
clarification_question: Is this a specific named Thark warrior or a generic combatant character in the story?

[[SECTION markdown]]
# Young Thark Warrior - CH010

**Display Name:** Young Thark Warrior  
**Chapter Role:** Combatant / Deceased  

**Physical Presence:** Present (killed during combat sequence)  

**Supported Physical Description:**  
- None specified in source material  
- Only mentioned as bleeding and lifeless after being struck/killed  

**Costume & Silhouette:**  
- No costume details available  
- Wears chieftain regalia transferred to John Carter after death  

**Continuity-Critical Traits:**  
- Insults and strikes Dejah Thoris during proceedings  
- Killed by John Carter in fierce combat sequence  
- Regalia transferred to John Carter after death  
- Arms and ornaments become John Carter's chieftain status symbols  

**Uncertainty Notes:**  
- Physical appearance completely unavailable for reliable rendering  
- May be title reference rather than individual character  
- Insufficient identification for dependable image generation  

**Useful Descriptive Noun Phrases:**  
- "Deceased Thark combatant"  
- "Regalia donor to John Carter"  
- "Helium expedition challenger"  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
