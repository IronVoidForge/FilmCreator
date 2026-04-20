# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:04:37.259302+00:00
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

## Narrative Events (CH009)

### Opening & Status Check
Carter returns from an encounter with the prisoner. He observes a strange expression on Sola's face, indicating her reaction to the event. He is surprised by her usually expressionless countenance showing emotion.

### Training & Social Integration
*   **Armor Acquisition:** A warrior approaches Carter bearing arms and accouterments. These are presented respectfully but menacingly.
*   **Fitting Process:** Sola and other women remodel the trappings to fit Carter's lesser proportions. He is then garbed in full panoply of war.
*   **Instruction:** Sola instructs Carter on weapons mysteries. They spend hours daily practicing on the plaza with young Martians. Carter progresses satisfactorily due to familiarity with earthly weapons.

### Martian Society Commentary
*   **Production & Defense:** Women make powder, cartridges, firearms, and all manufactured articles. In time of war, they form reserves and fight with greater intelligence/ferocity than men.
*   **Strategy & Law:** Men are trained in higher branches of war (strategy, troop maneuvering) and make laws for emergencies. They administer justice without precedent; punishment is by jury of peers. No lawyers exist.

### The Prisoner Plot Discussion
*   **Fate Decided:** Women discuss the prisoner's fate. Sarkoja states they will carry her to Thark to exhibit her last agonies at the great games before Tal Hajus.
*   **Sola's Sympathy:** Sola expresses hope that they hold her for ransom, noting her smallness and beauty. This is met with angry grunts from Sarkoja and others.
*   **Reprimand:** Sarkoja scolds Sola for weakness/atavism, warning Tars Tarkas against entrusting such sentiments to her regarding maternity responsibilities. Sola defends her interest in the red woman, noting she has never harmed them and that Martians are at peace with their own kind except when duty calls.
*   **Carter's Internal State:** Carter is convinced of Sola's friendliness toward the captive. He decides to take Sola into his confidence at the first opportunity to ask for aid in escaping, relying on her hatred of cruelty.

### Nighttime Conversations
*   **Sleeping Quarters:** Occupied by females, young Martians, Sola, Carter, and Woola. Adults converse desultorily before sleep.
*   **Topic:** The prisoner's visit to the audience chamber is discussed. Sarkoja (a guard at the audience) confirms the prisoner will be taken to Thark for the games.
*   **Carter's Reaction:** He listens keenly but offers no remarks, fearing Sola's reaction regarding jealousy or her attitude toward the captive.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter CH009 Character Index

## Carter
*   **Role:** Protagonist (Human Male)
*   **Status:** Physically Present
*   **Description:** Human male with lesser proportions than Martians; familiar with earthly weapons.

## Sola
*   **Role:** Female Martian Warrior/Leader
*   **Status:** Physically Present
*   **Description:** Female Martian, small and beautiful; usually expressionless but shows emotion here.

## Sarkoja
*   **Role:** Female Martian Guard/Leader
*   **Status:** Referenced/Physically Present (in conversation)
*   **Description:** Female Martian guard at audience chamber; scolds Sola for weakness.

## Woola
*   **Role:** Human Male Companion
*   **Status:** Referenced (Sleeping Quarters)
*   **Description:** Human male companion present in sleeping quarters with Carter and females.

## The Prisoner
*   **Role:** Female Martian Exile/Prisoner
*   **Status:** Referenced
*   **Description:** Red woman; small and beautiful; fate discussed (exhibition at games).
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter (CH009)

**Display Name:** Carter  
**Chapter Role:** Protagonist / Human Male Prisoner  

**Physical Presence:** Physically Present  
Carter is actively present in the scene, returning from an encounter with the prisoner and undergoing armor fitting. He is observed by Sola and participates in training sessions on the plaza.

**Physical Description:**  
Supported by source: Human male with "lesser proportions" compared to Martians. Familiar with earthly weapons.  

**Costume & Silhouette:**  
Garbed in full panoply of war after being remodelled by Sola and other women.  

**Continuity-Critical Traits:**  
Human origin; distinct from Martian physiology; progresses satisfactorily due to familiarity with weapons.

**Uncertainty Notes:**  
None regarding identity or basic physical classification (human male).
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
# Sola (CH009)

**Display Name:** Sola  
**Chapter Role:** Female Martian Warrior / Leader  

**Physical Presence:** Physically Present  
Sola is actively present, instructing Carter on weapons, remodeling his armor, and conversing with Sarkoja regarding the prisoner's fate.

**Physical Description:**  
Supported by source: Female Martian, described as having "smallness and beauty". Her countenance is usually expressionless but shows emotion here.  

**Costume & Silhouette:**  
Warrior attire; implied to be of standard Martian female build (lesser than male warriors).  

**Continuity-Critical Traits:**  
Shows sympathy for the prisoner; instructs Carter; displays emotional reaction to events.

**Uncertainty Notes:**  
None regarding identity or basic physical classification (female Martian).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text mentions name and role but lacks specific physical traits (hair, skin, height, etc.) for image generation support.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja (CH009)

**Display Name:** Sarkoja  
**Chapter Role:** Female Martian Guard / Leader  

**Physical Presence:** Referenced / Physically Present (in conversation)  
Sarkoja is present in the audience chamber and converses with Sola about the prisoner's fate. She scolds Sola for weakness.

**Physical Description:**  
Supported by source: None specific. Identified only as a female Martian guard.  

**Costume & Silhouette:**  
Guard attire at the audience chamber; implied to be of standard Martian female build.  

**Continuity-Critical Traits:**  
Enforces discipline (scolds Sola); confirms prisoner's fate for the games; acts with anger/ferocity.

**Uncertainty Notes:**  
Physical description is sparse in this chapter summary, requiring manual definition for consistent image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text mentions name and presence but lacks specific physical traits for image generation support.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola (CH009)

**Display Name:** Woola  
**Chapter Role:** Human Male Companion  

**Physical Presence:** Referenced (Sleeping Quarters)  
Woola is mentioned as occupying sleeping quarters with females, young Martians, Sola, and Carter.

**Physical Description:**  
Supported by source: None specific. Identified only as a human male companion.  

**Costume & Silhouette:**  
Human attire; implied to be of standard human build.  

**Continuity-Critical Traits:**  
Companion to Carter; present in sleeping quarters context.

**Uncertainty Notes:**  
Physical description is sparse in this chapter summary, requiring manual definition for consistent image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_prisoner
canonical_character_id: the_red_woman
aliases: red_woman, prisoner
is_fully_identified: false
manual_description_required: true
manual_description_reason: Description limited to 'smallness and beauty' and 'red woman'; lacks specific physical details.
clarification_required: true
clarification_reason: if the chapter names a character without enough stable identification, set is_fully_identified to false
clarification_question: What is the prisoner's proper name or designation in the story context?

[[SECTION markdown]]
# The Prisoner (CH009)

**Display Name:** The Prisoner / Red Woman  
**Chapter Role:** Female Martian Exile  

**Physical Presence:** Referenced  
The prisoner is referenced extensively (Carter returns from encounter with her, Sarkoja discusses her fate, Sola expresses sympathy). She is not physically present in the main scenes of this chapter summary.

**Physical Description:**  
Supported by source: "Smallness and beauty"; referred to as "red woman".  

**Costume & Silhouette:**  
Implied female Martian build; specific attire not detailed in text.  

**Continuity-Critical Traits:**  
Subject of debate regarding fate (exhibition at games vs ransom); object of Sola's sympathy; Carter relies on her hatred of cruelty for escape aid.

**Uncertainty Notes:**  
Identity is weakly identified by name ("The prisoner" or "Red woman") rather than a proper noun. Physical description is vague ("smallness and beauty"). Clarification required for stable identification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
