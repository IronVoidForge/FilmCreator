# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:21:49.849272+00:00
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

Chapter id: CH009

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

# Chapter IX: Language Mastery & Escape Resolution

## Visual Continuity Facts
- **Armor:** A warrior presents arms, ornaments, and accouterments at the doorway bearing a respectful yet menacing demeanor. Sola and other women remodel the trappings to fit Carter's lesser proportions. He departs garbed in the panoply of war.
- **Sleeping Quarters:** Occupied by three or four females, recently hatched young, Sola, her youthful ward (Carter), and Woola the hound. Adults converse desultorily before sleep; Carter listens keenly after mastering the language.
- **Audience Chamber:** The prisoner is seen being conducted here with unnecessary harshness by guards, contrasting with Sola's maternal kindliness toward Carter.

## Narrative Beats & Scene Decomposition

### 1. Post-Encounter Reflection
Carter wakes and glances at Sola, noting a strange expression on her countenance after witnessing the encounter with the prisoner. He admits he has learned little of the Martian tongue beyond daily needs.

### 2. Arrival & Gift Presentation
At the doorway of their building, a warrior approaches bearing arms and ornaments. He presents them to Carter with unintelligible words but a respectful/menacing bearing. Sola and women later fit the armor to Carter's proportions.

### 3. Training Montage
Sola instructs Carter in weapon mysteries. He spends hours daily practicing on the plaza with Martian young. His familiarity with earthly weapons makes him an apt pupil; he progresses satisfactorily though not yet proficient in all weapons.

### 4. Society Description (Voiceover/Context)
Women produce powder, cartridges, firearms, and manufactured articles. They form reserves in warfare. Men handle strategy, law-making, and troop maneuvering. Justice is administered by a jury of peers; there are no lawyers.

### 5. Prisoner Status & Language Push
Carter sees the prisoner briefly in the audience chamber. He overhears guards speaking to her. Driven by this, he nearly drives Sola distracted with importunities to hasten his education. Within days, he masters the tongue enough for passable conversation and full understanding.

### 6. Night Conversation & Prisoner Discussion
On the night following the prisoner's visit, the sleeping quarters' adults converse before sleep. The topic turns to the "red one." Sarkoja reveals they decided to carry her to Thark for exhibition at games before Tal Hajus. Sola expresses hope for ransom; Sarkoja reprimands her for weakness/atavism.

### 7. Sola's Defense & Carter's Realization
Sola defends her interest in the prisoner, arguing Martians live at peace with their fellows while they are always warring. Her wild outbreak shocks the women into silence. Carter realizes Sola is friendly and hates cruelty/barbarity. He feels fortunate to be in her hands rather than others.

### 8. Resolution
Carter decides not to see better conditions for escape but is willing to take chances among people like himself. He resolves to take Sola into confidence at the first opportunity to ask for aid in escaping Mars. He turns among his silks and furs and sleeps dreamless sleep.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1
[[SECTION character_index_markdown]]
# Character Index: Chapter IX

- **Carter**: Protagonist, student of war and language.
- **Sola**: Maternal protector, warrior companion.
- **Woola**: Hound companion.
- **The Red One (Prisoner)**: Captive subject of discussion.
- **Sarkoja**: Advisor, antagonist figure.

[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: john_carter
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (hair, eyes, height) for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Carter

**Display Name:** Carter  
**Chapter Role:** Protagonist / Student of War and Language  

**Presence Status:** Physically Present  
Carter is actively present in the scene, waking up, listening to conversations, practicing weapons, and sleeping.  

**Physical Description:** None Supported by Source  
The provided chapter summary does not describe specific physical features such as hair color, eye shape, or height. He is described wearing armor and silks/furs.  

**Costume & Silhouette:**  
- **Armor:** Fitted to his "lesser proportions" by Sola and women.  
- **Clothing:** Silks and furs mentioned in the resolution.  
- **Silhouette:** Warrior bearing, though specific build is not detailed.  

**Continuity Traits:**  
- Learns Martian language rapidly (within days).  
- Wears panoply of war presented by a warrior.  
- Practices on the plaza with Martian young.  

**Uncertainty Notes:**  
Physical appearance details are missing from this chapter summary and must be inferred or clarified for image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: none
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (hair, eyes, height) for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Maternal Protector / Warrior Companion  

**Presence Status:** Physically Present  
Sola is present in the sleeping quarters, at the doorway, and during conversations.  

**Physical Description:** None Supported by Source  
The text describes her demeanor ("maternal kindliness", "wild outbreak") but does not provide specific physical features like hair or eyes.  

**Costume & Silhouette:**  
- **Armor:** Fitted to Carter's proportions after presentation by a warrior.  
- **Clothing:** Implied warrior attire, though specific details are sparse.  
- **Silhouette:** Maternal yet capable of wild emotional outbursts.  

**Continuity Traits:**  
- Shows kindness toward Carter (contrasting with guards).  
- Defends her interest in the prisoner against Sarkoja.  
- Hopes for ransom for the prisoner.  

**Uncertainty Notes:**  
Specific physical appearance details are missing from this chapter summary and must be inferred or clarified for image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: none
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific breed or color details for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola

**Display Name:** Woola  
**Chapter Role:** Hound Companion  

**Presence Status:** Physically Present  
Woola is present in the sleeping quarters with the adults.  

**Physical Description:** None Supported by Source  
The text identifies him as "the hound" but does not specify breed, size, or color.  

**Costume & Silhouette:**  
- **Type:** Hound / Dog.  
- **Silhouette:** Companion animal accompanying Carter and Sola.  

**Continuity Traits:**  
- Resides in the sleeping quarters.  
- Adults converse desultorily before sleep while he is present.  

**Uncertainty Notes:**  
Specific physical appearance details (breed, color) are missing from this chapter summary and must be inferred or clarified for image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner
canonical_character_id: prisoner
aliases: red_one
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits and proper name for dependable image generation.
clarification_required: true
clarification_reason: Character is referred to only by role or color, not a personal name.
clarification_question: Does the prisoner have a specific name in the source material?
[[SECTION markdown]]
# The Red One (Prisoner)

**Display Name:** The Red One / Prisoner  
**Chapter Role:** Captive / Subject of Discussion  

**Presence Status:** Referenced  
The prisoner is seen briefly in the audience chamber and discussed by guards and women.  

**Physical Description:** None Supported by Source  
No specific physical traits are described in this chapter summary. She is referred to as "the red one".  

**Costume & Silhouette:**  
- **Status:** Prisoner / Captive.  
- **Silhouette:** Conducted with unnecessary harshness by guards.  

**Continuity Traits:**  
- Subject of Sarkoja's plan to carry her to Thark for exhibition.  
- Sola expresses hope for ransom.  
- Carter masters the language enough to understand discussions about her.  

**Uncertainty Notes:**  
Physical appearance details are missing from this chapter summary. Additionally, she is unnamed in this text and requires clarification on her identity for image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: none
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (hair, eyes, height) for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja

**Display Name:** Sarkoja  
**Chapter Role:** Advisor / Antagonist Figure  

**Presence Status:** Physically Present  
Sarkoja is present in the sleeping quarters during the night conversation.  

**Physical Description:** None Supported by Source  
The text describes her actions and dialogue but does not provide specific physical features like hair or eyes.  

**Costume & Silhouette:**  
- **Role:** Advisor to the women (implied).  
- **Silhouette:** Contrasts with Sola's kindness; reprimands Sola for weakness.  

**Continuity Traits:**  
- Reveals the plan to carry the prisoner to Thark.  
- Expresses hopelessness regarding ransom compared to Sola.  
- Reprimands Sola for "weakness/atavism".  

**Uncertainty Notes:**  
Specific physical appearance details are missing from this chapter summary and must be inferred or clarified for image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
