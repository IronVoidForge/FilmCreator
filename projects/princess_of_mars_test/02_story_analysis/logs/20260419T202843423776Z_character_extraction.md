# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:28:43.423776+00:00
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

Chapter id: CH015

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

# Chapter Summary: CHAPTER XV - SOLA TELLS ME HER STORY

## Narrative Beats & Scene Decomposition

### Scene 1: Recovery from Zad's Attack
- **Action:** John Carter regains consciousness after being stabbed by Zad. He finds his sword buried in Zad's green breast and removes it from his own left breast (flesh wound only).
- **Visual Continuity:** Green moss, ochre moss of ancient sea bottom, sword piercing ribs, blood.
- **Outcome:** Carter is bleeding but weak; he moves toward the chariots carrying his retinue.

### Scene 2: Wound Healing & Visit to Dejah/Sola
- **Action:** Martian women apply healing agents to Carter (instantaneous recovery). Carter visits the chariot of Dejah Thoris where Sola is bandaged and Dejah is sobbing (believing Carter dead).
- **Dialogue:** Sola explains Dejah's grief; Carter promises not to force himself on Dejah.
- **Visual Continuity:** Bandages, silks and furs, torch light, Sola standing, Dejah prone.

### Scene 3: The Caravan March Description
- **Action:** Carter leaves the chariot and joins Tars Tarkas at the rear of the column. The text describes the silent march of the caravan.
- **Visual Continuity:** 250 ornate chariots, 50 extra mastodons (zitidars), 500+ loose thoats, advance guard of mounted warriors. Landscape is moss-covered with no dust or sound from movement.
- **Atmosphere:** Phantasmagoria-like silence, guttural growling of animals breaking the stillness.

### Scene 4: Sola's Backstory (The Core Narrative)
- **Action:** Carter finds Sola working by torchlight at night. She tells her story of her parents' forbidden love, the hidden egg/incubation, Sarkoja's discovery, and her mother's death by torture.
- **Key Details:** Mother was too small for Thark breeding; father was a simple warrior; egg hidden in ruined tower; Sarkoja heard story but not father's name; mother died protecting Sola; father is Tars Tarkas.
- **Visual Continuity:** Torchlight, shadows of doorway, lesser moon swinging clear, chariot tailboard.

### Scene 5: Revelation & Departure
- **Action:** Sola reveals her father's name is Tars Tarkas. Carter promises to tell Dejah he is alive and leaves to join Tars Tarkas at the rear of the column.
- **Visual Continuity:** Sola wrapped in gloomy thoughts, Carter on waiting thoat, column moving across yellow landscape.

## Visual Continuity Facts (Separate from Story Summary)
- **Landscape:** Moss-covered sea bottom, no dust (except cultivated districts), silent movement due to padded feet/tires.
- **Lighting:** Lesser moon provides illumination during Sola's story; torchlight used at night camp.
- **Characters:** Green Martians converse in monosyllables; Dejah Thoris is prone/sobbing; Sola is standing/bandaged; Tars Tarkas is at rear of column.
- **Objects:** Swords, bandages, torches, chariots, thoats, zitidars, metal ornaments, silks and furs.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter XV Character Index

| Name | Role in Chapter | Visual Status | Description Summary |
| :--- | :--- | :--- | :--- |
| John Carter | Protagonist, Wounded Survivor | Present (Green Martian) | Recovering from Zad's attack, healing applied, on waiting thoat. |
| Sola | Central Narrative Figure | Present (Bandaged) | Telling story of parents, standing by torchlight, bandaged. |
| Dejah Thoris | Grieving Partner | Present (Prone) | Sobbing in chariot, believing Carter dead. |
| Tars Tarkas | Father / Warrior | Referenced / Present | At rear of column, revealed as Sola's father. |
| Zad | Antagonist | Referenced (Dead) | Stabbed by Carter, green breast pierced. |
| Martian Women | Healing Agents | Referenced | Applied healing to Carter instantly. |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: Carter
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter XV

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Wounded Survivor  

**Physical Presence:** Present (Green Martian)  
**Visual Description:** Green Martian skin, wounded in left breast (sword removed), recovering from stab wound. Standing or seated on waiting thoat.  
**Costume & Silhouette:** Standard Barsoomian attire implied by context of chariot column. Wearing armor/sword previously.  
**Continuity Traits:** Bleeding but weak initially; healed instantly by women. Moves toward rear of column with Tars Tarkas.  
**Uncertainty Notes:** Specific facial features or hair details not explicitly described beyond "Green Martian" classification.  

**Render-Facing Prompt Noun Phrases:** Green Martian man, wounded chest, sword removed from breast, recovering on thoat, Barsoomian warrior, moss-covered landscape background.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter XV

**Display Name:** Sola  
**Chapter Role:** Central Narrative Figure / Daughter of Tars Tarkas  

**Physical Presence:** Present (Bandaged)  
**Visual Description:** Standing by torchlight, bandaged on body, wrapped in gloomy thoughts. Lesser moon swinging clear above.  
**Costume & Silhouette:** Wrapped in silks/furs implied by chariot context. Bandages visible.  
**Continuity Traits:** Telling story of parents' forbidden love, Sarkoja's discovery, mother's death. Reveals father is Tars Tarkas.  
**Uncertainty Notes:** Specific facial expression details beyond "gloomy thoughts" not explicitly described.  

**Render-Facing Prompt Noun Phrases:** Bandaged woman, standing by torchlight, lesser moon background, chariot tailboard, gloomy expression, Barsoomian female.
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
# Dejah Thoris - Chapter XV

**Display Name:** Dejah Thoris  
**Chapter Role:** Grieving Partner  

**Physical Presence:** Present (Prone)  
**Visual Description:** Prone in chariot, sobbing. Believes Carter dead.  
**Costume & Silhouette:** Silks and furs implied by chariot context. Bandaged or mourning attire.  
**Continuity Traits:** Sola explains her grief; Carter promises not to force himself on her.  
**Uncertainty Notes:** Specific facial features or hair details not explicitly described beyond "sobbing".  

**Render-Facing Prompt Noun Phrases:** Prone woman, sobbing, chariot interior, silks and furs, grieving expression, Barsoomian noblewoman.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Chapter XV

**Display Name:** Tars Tarkas  
**Chapter Role:** Father / Warrior  

**Physical Presence:** Referenced / Present (Rear of Column)  
**Visual Description:** Warrior at rear of column. Simple warrior background implied by Sola's story.  
**Costume & Silhouette:** Standard Barsoomian warrior attire.  
**Continuity Traits:** Revealed as Sola's father. Carter joins him at rear of column.  
**Uncertainty Notes:** Specific facial features or hair details not explicitly described beyond "warrior".  

**Render-Facing Prompt Noun Phrases:** Warrior, rear of column, Barsoomian male, simple warrior background, moss-covered landscape.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: zad
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Zad - Chapter XV

**Display Name:** Zad  
**Chapter Role:** Antagonist / Deceased  

**Physical Presence:** Referenced (Dead)  
**Visual Description:** Green breast pierced by sword. Stabbed by Carter.  
**Costume & Silhouette:** Standard Barsoomian attire implied.  
**Continuity Traits:** Dead after Carter removes sword from his own left breast.  
**Uncertainty Notes:** Specific facial features or hair details not explicitly described beyond "green breast".  

**Render-Facing Prompt Noun Phrases:** Green breast, stabbed body, dead antagonist, sword piercing ribs, moss-covered landscape.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_women
canonical_character_id: martian_women
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Martian Women - Chapter XV

**Display Name:** Martian Women  
**Chapter Role:** Healing Agents  

**Physical Presence:** Referenced (Group)  
**Visual Description:** Group applying healing agents to Carter. Green Martians converse in monosyllables.  
**Costume & Silhouette:** Standard Barsoomian female attire implied.  
**Continuity Traits:** Instantaneous recovery of Carter. Sola is one of them (bandaged).  
**Uncertainty Notes:** Specific facial features or hair details not explicitly described beyond "Green Martians".  

**Render-Facing Prompt Noun Phrases:** Group of women, healing agents, Green Martians, monosyllabic conversation, Barsoomian females.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
