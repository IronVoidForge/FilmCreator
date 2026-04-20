# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:51:43.145060+00:00
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

# Chapter XV: SOLA TELLS ME HER STORY - Scene Decomposition

## Immediate Events & Dialogue Beats
1.  **Recovery Scene**: John Carter regains consciousness, removes sword from body (Zad's blade), moves toward chariots bleeding and weak.
2.  **Arrival at Chariot**: Murmur of Martian applause; reaches women who dress wounds with healing agents.
3.  **Dejah Thoris Mourning**: Found lying prone on silks and furs, wracked with sobs; believes John is dead.
4.  **Sola's Explanation**: Tells John Dejah thinks he's dead because she mourns him as if he died; explains Barsoomian pride and tears (two people wept: mother from sorrow, Sarkoja from baffled rage).
5.  **Invitation to Story**: Sola promises to tell her strange story later that night in the chariot; John agrees to come.
6.  **Night Camp Scene**: Carter finds Sola working by torchlight on Tars Tarkas' trappings; she reveals loneliness and desire for his trust.
7.  **Full Story Revelation**: Sola tells complete backstory of her mother's forbidden love with a warrior (Tars Tarkas), hiding the egg, eventual hatching, Tal Hajus' cruelty, mother's death by torture, and Sarkoja's suspicion.
8.  **Father's Identity**: Sola reveals her father's name is Tars Tarkas; confirms he doesn't know she is his child or who betrayed her mother.

## Visual Continuity Details for Scene Breakdown
- **Scene 1 (Recovery)**: Ochre moss, green breast of dead Zad, sword hilt buried in flesh, bleeding wound on left breast.
- **Scene 2 (Chariot Arrival)**: Women applying healing agents, chariot interior, Martian applause murmur.
- **Scene 3 (Dejah's Mourning)**: Silks and furs, prone position, lithe form wracked with sobs, Sola standing short distance from vehicle.
- **Scene 4 (Night Camp)**: Torchlight, Tars Tarkas' trappings being worked on, gloomy thoughts of terrible past.
- **Scene 5 (Caravan March)**: Yellow landscape, two hundred and fifty chariots, advance guard riding five abreast, flankers on either side, fifty zitidars, loose thoats.

## Key Revelations for Later Scene Extraction
- **Tars Tarkas Identity**: Confirmed as Sola's father; currently present but unaware of her true identity or Sarkoja's betrayal.
- **Sarkoja's Suspicion**: Knows something about Sola's origin but hasn't exposed her yet; suspects identity of Sola's father.
- **Tal Hajus' Cruelty**: Responsible for Sola's mother's death; awaiting opportunity to crush ambition; currently cruellest of the cruel.
- **Forbidden Love Theme**: Green Martian women without love and hope; Sola lost because she has known love.
- **Secrecy Requirement**: Sola must hide her parentage and affection for her mother to survive in Tharkian society.

## Continuity Notes
- **Wound Status**: John Carter's wound healed except for weakness from loss of blood and soreness; Dejah Thoris' chest swathed in bandages (Sarkoja's dagger deflected by metal breast ornament).
- **Location Context**: Camped at foot of hills approaching southern boundary of sea; first march of large body of men and animals witnessed which raised no dust.
- **Time Progression**: Night camp after two days without drink for animals; evening meal of cheese-like food and vegetable milk before Sola's story.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter XV Character Index

| Asset ID | Canonical ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|--------------|---------|------------------|------------------------------|------------------------|
| john_carter | CH015_JC | - | true | false | false |
| dejah_thoris | CH015_DT | - | true | false | false |
| sola | CH015_SOLA | - | true | false | false |
| tars_tarkas | CH015_TT | - | false | true | true |
| zad | CH015_ZAD | - | false | true | false |
| sarkoja | CH015_SK | - | false | true | false |

**Notes:**
- Characters referenced but not physically present in this chapter (Dejah Thoris, Tars Tarkas, Sarkoja) require manual descriptions for image generation
- Zad is deceased and only referenced through wound details
- Tars Tarkas needs clarification about his current awareness of Sola's identity

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH015_JC
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter XV

**Display Name:** John Carter  
**Chapter Role:** Protagonist, recovering consciousness  
**Physical Presence:** Present in scene (Scene 1-5)  
**Physical Description:** Wound on left breast with sword hilt buried in flesh; bleeding wound; Ochre moss and green breast of dead Zad nearby; wound healed except for weakness from blood loss and soreness  
**Costume/Silhouette:** Not fully described in this chapter; wearing armor implied by sword removal  
**Continuity-Critical Traits:** Wound status (healed but weak); metal breast ornament deflected Sarkoja's dagger; recovering from two days without drink for animals  
**Uncertainty Notes:** Full body description not provided in this chapter; limited to wound and immediate surroundings

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH015_DT
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Previous chapters established her appearance; referenced as found lying prone on silks and furs, lithe form wracked with sobs  
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter XV

**Display Name:** Dejah Thoris  
**Chapter Role:** Mourning wife, referenced but not physically present in main scene  
**Physical Presence:** Referenced (Scene 3) - found lying prone on silks and furs  
**Physical Description:** Lithe form; chest swathed in bandages from Sarkoja's dagger deflection by metal breast ornament; believed John is dead  
**Costume/Silhouette:** Silks and furs; prone position; lithe form  
**Continuity-Critical Traits:** Mourning state (wracked with sobs); believes John Carter is dead; Barsoomian pride and tears context  
**Uncertainty Notes:** Not physically present in main scene; description limited to mourning posture and bandaged chest

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH015_SOLA
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Working by torchlight on Tars Tarkas' trappings; reveals loneliness and desire for trust; described as short distance from vehicle  
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter XV

**Display Name:** Sola  
**Chapter Role:** Storyteller, present in scene  
**Physical Presence:** Present (Scene 4-5) - working by torchlight on Tars Tarkas' trappings  
**Physical Description:** Working at night camp; standing short distance from chariot vehicle; gloomy thoughts of terrible past  
**Costume/Silhouette:** Not fully described; implied Tharkian attire while working on father's trappings  
**Continuity-Critical Traits:** Mother's forbidden love with Tars Tarkas; hiding egg that hatched; Tal Hajus' cruelty context; mother's death by torture; Sarkoja's suspicion about her origin; must hide parentage and affection for mother to survive in Tharkian society  
**Uncertainty Notes:** Full physical description not provided; limited to actions and emotional state

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH015_TT
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced as Sola's father; currently present but unaware of her true identity or who betrayed her mother; no physical description provided in this chapter  
clarification_required: true
clarification_reason: Character might already exist under another name or is too weakly identified for dependable image generation without clarification about current awareness state  
clarification_question: Is Tars Tarkas currently aware that Sola is his daughter and who betrayed her mother?

[[SECTION markdown]]
# Tars Tarkas - Chapter XV

**Display Name:** Tars Tarkas  
**Chapter Role:** Sola's father (unaware of her identity), referenced character  
**Physical Presence:** Referenced as present but not physically described in this chapter  
**Physical Description:** Not provided in this chapter; only known through Sola's backstory  
**Costume/Silhouette:** Trappings being worked on by torchlight at night camp  
**Continuity-Critical Traits:** Forbidden love with green Martian woman (Sola's mother); hiding the egg that eventually hatched; Tal Hajus' cruelty context; currently present but unaware of Sola's true identity or who betrayed her mother  
**Uncertainty Notes:** No physical description in this chapter; current awareness state needs clarification for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: CH015_ZAD
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Deceased character only referenced through wound details (green breast, sword hilt buried in flesh); no physical description provided  
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Zad - Chapter XV

**Display Name:** Zad  
**Chapter Role:** Deceased warrior, referenced through wound context  
**Physical Presence:** Not physically present (deceased)  
**Physical Description:** Green breast; sword hilt buried in flesh; Ochre moss nearby; dead state confirmed  
**Costume/Silhouette:** Not described beyond wound details  
**Continuity-Critical Traits:** Blade of Zad used on John Carter's wound; green breast visible at scene location  
**Uncertainty Notes:** Deceased character with limited description; only referenced through wound and immediate surroundings

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH015_SK
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced in context of suspicion about Sola's origin; not physically present in this chapter; no physical description provided  
clarification_required: false
clarification_reason: Character might already exist under another name or is too weakly identified for dependable image generation without clarification  
clarification_question: Is Sarkoja currently aware of Sola's parentage and who betrayed her mother?

[[SECTION markdown]]
# Sarkoja - Chapter XV

**Display Name:** Sarkoja  
**Chapter Role:** Antagonist, referenced through suspicion context  
**Physical Presence:** Not physically present in this chapter  
**Physical Description:** Not provided in this chapter; only known through backstory context  
**Costume/Silhouette:** Not described beyond suspicion context  
**Continuity-Critical Traits:** Suspects identity of Sola's father; knows something about Sola's origin but hasn't exposed her yet; currently cruellest of the cruel; responsible for Sola's mother's death by torture; awaiting opportunity to crush ambition  
**Uncertainty Notes:** Not physically present in this chapter; only referenced through suspicion and backstory context

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
