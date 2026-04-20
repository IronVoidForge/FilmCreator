# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:40:52.073335+00:00
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

**Scene 1: Training and Arms.** A warrior presents arms to Nell; women remodel the trappings for his smaller size. Sola instructs him in weapons mysteries. He practices on the plaza with young Martians, progressing satisfactorily due to familiarity with earthly weapons.

**Scene 2: Martian Society Structure.** Women are described as artisans producing powder, cartridges, and firearms. Men handle strategy and law. Justice is swift; there are no lawyers. The training of defense/offense is conducted solely by women.

**Scene 3: Prisoner's Fate.** Nell sees the prisoner briefly being taken to the audience chamber. Guards treat her harshly; Sola treats him kindly. He learns the Martian language quickly due to the incentive of the prisoner's situation.

**Scene 4: Night Conversation.** Women discuss the prisoner's death throes. Sarkoja states she will be exhibited at games before Tal Hajus. Sola expresses hope for ransom; others scold her for weakness and softness. Sola defends compassion, arguing against their constant bloodshed and lack of peace.

**Scene 5: Nell's Resolution.** Overhearing the conversation confirms Sola's friendliness and hatred of cruelty. Nell decides to take Sola into confidence at the first opportunity to ask for aid in escaping with the prisoner. He sleeps after resolving this plan.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH009

| Character | Role | Status | Description Available |
|-----------|------|--------|----------------------|
| Nell | Protagonist, Warrior Trainee | Physically Present | Limited physical description |
| Sola | Weapons Instructor, Compassionate Martian | Physically Present | Limited physical description |
| The Prisoner | Captive, Audience Chamber Subject | Referenced | Minimal physical description |
| Sarkoja | Exhibition Candidate, Games Participant | Referenced | No physical description |
| Tal Hajus | Games Authority Reference | Referenced | No physical description |
| Young Martians | Training Partners | Physically Present | Group reference only |

**Note:** All characters lack detailed physical descriptions suitable for image generation. Manual descriptions required for all.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: nell
canonical_character_id: CH009_NELL
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No detailed physical description provided in chapter summary; only context of warrior training and interaction with Sola available
clarification_required: false
clarification_reason: Character is clearly identified as protagonist throughout chapter
clarification_question: 

[[SECTION markdown]]
# Nell - CH009

**Display Name:** Nell  
**Chapter Role:** Protagonist, Warrior Trainee  
**Physical Presence:** Physically present in training scenes (Scene 1), referenced in conversations (Scene 3-5)  

**Physical Description:** Limited information available. Identified as a warrior receiving instruction from Sola in weapons mysteries. Practices on plaza with young Martians. No specific physical features documented in chapter summary.

**Costume/Silhouette:** Warrior attire implied through training context. Smaller size noted when women remodel trappings for him (Scene 1).

**Continuity-Critical Traits:** 
- Receives instruction from Sola
- Overhears conversations about prisoner's fate
- Decides to take Sola into confidence regarding escape plan
- Learns Martian language quickly due to prisoner situation incentive

**Uncertainty Notes:** 
- No detailed physical description provided for image generation
- Physical features beyond warrior context not documented
- Appearance details must be inferred from training and interaction context

**Render-Facing Prompt Noun Phrases:** 
- Warrior trainee receiving weapons instruction
- Smaller size requiring trappings adjustment
- Protagonist with compassionate Martian instructor
- Learning Martian language through prisoner situation incentive
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH009_SOLA
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No detailed physical description provided in chapter summary; only interaction context with Nell and other Martians available
clarification_required: false
clarification_reason: Character is clearly identified as weapons instructor throughout chapter
clarification_question: 

[[SECTION markdown]]
# Sola - CH009

**Display Name:** Sola  
**Chapter Role:** Weapons Instructor, Compassionate Martian  
**Physical Presence:** Physically present in training scenes (Scene 1), referenced in conversations (Scene 4-5)  

**Physical Description:** Limited information available. Identified as weapons instructor teaching Nell weapons mysteries. Treats him kindly while others treat prisoner harshly. No specific physical features documented in chapter summary.

**Costume/Silhouette:** Martian attire implied through training context. No specific costume details provided beyond general warrior/trainer role.

**Continuity-Critical Traits:** 
- Instructs Nell in weapons mysteries
- Treats Nell kindly while others treat prisoner harshly
- Expresses hope for prisoner ransom
- Defends compassion against constant bloodshed
- Nell decides to take Sola into confidence regarding escape plan
- Represents compassionate faction among Martians

**Uncertainty Notes:** 
- No detailed physical description provided for image generation
- Physical features beyond instructor context not documented
- Appearance details must be inferred from training and interaction context

**Render-Facing Prompt Noun Phrases:** 
- Weapons instructor teaching warrior trainee
- Compassionate Martian defending against bloodshed
- Kind treatment contrasting with harsh prisoner guards
- Hopeful for prisoner ransom situation
- Representative of compassionate faction among Martians
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_prisoner
canonical_character_id: CH009_PRISONER
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No detailed physical description provided in chapter summary; only context of captivity and death throes discussion available
clarification_required: false
clarification_reason: Character is clearly identified as prisoner throughout chapter
clarification_question: 

[[SECTION markdown]]
# The Prisoner - CH009

**Display Name:** The Prisoner  
**Chapter Role:** Captive, Audience Chamber Subject  
**Physical Presence:** Referenced in conversations (Scene 3-5), briefly seen being taken to audience chamber (Scene 3)  

**Physical Description:** Limited information available. Identified as prisoner being taken to audience chamber. Death throes discussed by women. No specific physical features documented in chapter summary.

**Costume/Silhouette:** Captive attire implied through imprisonment context. No specific costume details provided beyond general prisoner role.

**Continuity-Critical Traits:** 
- Being taken to audience chamber with harsh guard treatment
- Death throes discussed by female Martians
- Sarkoja states she will be exhibited at games before Tal Hajus
- Sola expresses hope for ransom
- Others scold Sarkoja for weakness regarding prisoner
- Nell decides to take Sola into confidence regarding escape plan with prisoner

**Uncertainty Notes:** 
- No detailed physical description provided for image generation
- Physical features beyond captive context not documented
- Appearance details must be inferred from imprisonment and death throes context

**Render-Facing Prompt Noun Phrases:** 
- Captive being taken to audience chamber
- Death throes discussed by female Martians
- Subject of exhibition at games before Tal Hajus
- Ransom hope expressed by Sola
- Escape plan subject with Nell and Sola
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH009_SARKOJA
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No detailed physical description provided in chapter summary; only brief reference to exhibition statement available
clarification_required: false
clarification_reason: Character is clearly identified by name in chapter
clarification_question: 

[[SECTION markdown]]
# Sarkoja - CH009

**Display Name:** Sarkoja  
**Chapter Role:** Exhibition Candidate, Games Participant  
**Physical Presence:** Referenced in conversations (Scene 4)  

**Physical Description:** Limited information available. Identified as female Martian who states she will be exhibited at games before Tal Hajus. No specific physical features documented in chapter summary.

**Costume/Silhouette:** Games participant attire implied through exhibition context. No specific costume details provided beyond general participant role.

**Continuity-Critical Traits:** 
- States she will be exhibited at games before Tal Hajus
- Women discuss her death throes (Scene 4)
- Sola expresses hope for ransom regarding her
- Others scold her for weakness and softness regarding prisoner situation
- Represents exhibition candidate among female Martians

**Uncertainty Notes:** 
- No detailed physical description provided for image generation
- Physical features beyond exhibition context not documented
- Appearance details must be inferred from games participant context

**Render-Facing Prompt Noun Phrases:** 
- Exhibition candidate at games before Tal Hajus
- Female Martian subject of death throes discussion
- Ransom hope expressed by Sola regarding her
- Subject of scolding for weakness among female Martians
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: CH009_TAL_HAJUS
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No detailed physical description provided in chapter summary; only brief reference as games authority available
clarification_required: false
clarification_reason: Character is clearly identified by name in chapter
clarification_question: 

[[SECTION markdown]]
# Tal Hajus - CH009

**Display Name:** Tal Hajus  
**Chapter Role:** Games Authority Reference  
**Physical Presence:** Referenced only (Scene 4)  

**Physical Description:** Limited information available. Identified as authority figure before whom Sarkoja will be exhibited at games. No specific physical features documented in chapter summary.

**Costume/Silhouette:** Games authority attire implied through reference context. No specific costume details provided beyond general authority role.

**Continuity-Critical Traits:** 
- Authority figure before whom Sarkoja will be exhibited at games
- Reference point for female Martian exhibition status
- Minimal interaction shown in chapter summary

**Uncertainty Notes:** 
- No detailed physical description provided for image generation
- Physical features beyond authority context not documented
- Appearance details must be inferred from games authority reference context
- Character has minimal presence in chapter compared to others

**Render-Facing Prompt Noun Phrases:** 
- Games authority figure for Sarkoja exhibition
- Reference point for female Martian status
- Minimal interaction character in chapter summary
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_martians
canonical_character_id: CH009_YOUNG_MARTIANS
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group reference only; no individual physical descriptions provided in chapter summary
clarification_required: true
clarification_reason: Character is a group rather than individual; may exist under different collective name or be too weakly identified as individuals
clarification_question: Are the young Martians referenced as a specific named group, or should they be treated as unnamed training partners?

[[SECTION markdown]]
# Young Martians - CH009

**Display Name:** Young Martians  
**Chapter Role:** Training Partners  
**Physical Presence:** Physically present in training scenes (Scene 1)  

**Physical Description:** Limited information available. Identified as group Nell practices weapons with on plaza. No specific physical features documented for individuals in chapter summary.

**Costume/Silhouette:** Martian attire implied through training context. No specific costume details provided beyond general young warrior role.

**Continuity-Critical Traits:** 
- Nell practices weapons mysteries with them on plaza
- Progressing satisfactorily due to familiarity with earthly weapons
- Group reference rather than individual characters
- Training partners for protagonist's weapon instruction

**Uncertainty Notes:** 
- No detailed physical description provided for image generation
- Physical features beyond training context not documented
- Appearance details must be inferred from young warrior training context
- Character is a group rather than individual; may need clarification on naming convention

**Render-Facing Prompt Noun Phrases:** 
- Young warriors serving as training partners
- Group Nell practices weapons with on plaza
- Training subjects for protagonist's weapon instruction
- Progressing satisfactorily due to earthly weapons familiarity
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
