# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:03:48.082297+00:00
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
# Character Index - CH009

| Character | Role/Presence | Physical Description Status | Identification Status |
|-----------|---------------|----------------------------|----------------------|
| Carter | Protagonist, physically present | Partial (presence confirmed) | Fully identified |
| Sola | Female Martian warrior, instructs Carter | Sparse (emotional reactions noted) | Fully identified |
| Sarkoja | Guard at audience chamber | Minimal (functional role only) | Fully identified |
| Woola | Sleeping quarters occupant | Very sparse (name only) | Weakly identified |
| The Prisoner/Red Woman | Captive, discussed fate | None (only referenced) | Uncertain identification |
| Tars Tarkas | Mentioned in dialogue | None (name reference only) | Weakly identified |

**Notes:**
- Carter: Main protagonist with confirmed presence but limited physical description
- Sola: Warrior character with emotional reactions documented, minimal physical details
- Sarkoja: Functional guard role, limited descriptive information
- Woola: Minimal presence, primarily name reference in sleeping quarters context
- The Prisoner/Red Woman: Only referenced in discussions, no physical description provided
- Tars Tarkas: Name only mentioned in dialogue about Sola's defense

**Manual Description Required:** Yes for all characters (insufficient physical details for reliable image generation)
**Clarification Required:** Yes for Woola, The Prisoner/Red Woman, and Tars Tarkas (weak identification)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical description for reliable image generation. Only presence and role are confirmed; no detailed physical features, height, build, or facial characteristics documented in source material.
clarification_required: false
clarification_reason: 
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Carter - CH009 Character Profile

**Display Name:** Carter  
**Chapter Role:** Protagonist / Main Character  
**Physical Presence:** Physically present in chapter (returns from encounter with prisoner)  
**Status:** Active participant in training and social integration  

## Physical Description (Supported by Source)
- Present throughout chapter as main protagonist
- Observes expressions on Sola's face during interactions
- Receives armor and weapons fitting from female warriors
- Practices weapons daily on plaza with young Martians
- Progresses satisfactorily due to familiarity with earthly weapons

## Costume & Silhouette (Supported by Source)
- Garbed in full panoply of war after fitting process
- Receives arms and accouterments respectfully presented
- Wears armor modified for his lesser proportions by Sola and other women

## Continuity-Critical Traits
- Familiar with earthly weapons systems
- Developing relationship with female Martian warriors
- Observant of emotional reactions in others (particularly Sola)
- Convinced of Sola's friendliness toward captive prisoner

## Uncertainty Notes
**Missing Physical Details:**
- No specific height, build, or facial features documented
- No skin tone, hair color, or eye characteristics mentioned
- No age indicators provided
- No distinguishing marks or scars noted

**Render-Facing Prompt Suggestions:**
"Male protagonist in full war armor, familiar with weapons systems, observant expression, receiving instruction from female warriors, plaza training setting, Martian society context"

**Manual Description Required:** YES - Insufficient physical details for reliable image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Sparse physical description. Only emotional reactions and warrior role documented; no detailed physical features, build, or appearance characteristics provided in source material.
clarification_required: false
clarification_reason: 
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Sola - CH009 Character Profile

**Display Name:** Sola  
**Chapter Role:** Female Martian Warrior / Instructor  
**Physical Presence:** Physically present in chapter (teaches Carter, participates in fitting process)  
**Status:** Active participant in Carter's training and social integration  

## Physical Description (Supported by Source)
- Female Martian warrior with emotional capacity (shows surprise at prisoner encounter)
- Usually expressionless countenance showing emotion during key moments
- Instructs Carter on weapons mysteries
- Participates in daily plaza practice sessions

## Costume & Silhouette (Supported by Source)
- Warrior attire appropriate for combat and instruction
- Modifies armor and trappings to fit Carter's proportions
- Part of female warrior group that makes manufactured articles

## Continuity-Critical Traits
- Shows emotional reactions (surprise, sympathy)
- Instructs Carter on weapons and combat techniques
- Expresses hope for prisoner's ransom rather than execution
- Defends her interest in red woman against Sarkoja's criticism
- Hatred of cruelty motivates her actions

## Uncertainty Notes
**Missing Physical Details:**
- No specific height, build, or facial features documented
- No skin tone, hair color, or eye characteristics mentioned
- No age indicators provided
- No distinguishing marks or scars noted

**Render-Facing Prompt Suggestions:**
"Female Martian warrior with emotional capacity, usually expressionless countenance showing surprise, instructing male protagonist on weapons, plaza training setting, warrior attire appropriate for combat and instruction"

**Manual Description Required:** YES - Insufficient physical details for reliable image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Minimal physical description. Only functional role as guard and dialogue participant documented; no detailed physical features, build, or appearance characteristics provided in source material.
clarification_required: false
clarification_reason: 
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Sarkoja - CH009 Character Profile

**Display Name:** Sarkoja  
**Chapter Role:** Guard at Audience Chamber / Warrior Group Member  
**Physical Presence:** Physically present in chapter (confirms prisoner's fate, participates in discussions)  
**Status:** Active participant in prisoner fate discussions and social commentary  

## Physical Description (Supported by Source)
- Female warrior/guard role confirmed
- Part of group that makes powder, cartridges, firearms, and manufactured articles
- Forms reserves and fights with greater intelligence/ferocity than men

## Costume & Silhouette (Supported by Source)
- Warrior attire appropriate for guard duties
- Part of female warrior group responsible for production and defense

## Continuity-Critical Traits
- Angry grunts in response to Sola's sympathy for prisoner
- Scolds Sola for weakness/atavism regarding maternity responsibilities
- Warns Tars Tarkas against entrusting sentiments to Sola
- Confirms prisoner will be taken to Thark for the games before Tal Hajus
- Represents harsher faction within warrior group

## Uncertainty Notes
**Missing Physical Details:**
- No specific height, build, or facial features documented
- No skin tone, hair color, or eye characteristics mentioned
- No age indicators provided
- No distinguishing marks or scars noted

**Render-Facing Prompt Suggestions:**
"Female warrior guard with angry demeanor, scolding female protagonist for weakness, part of production and defense group, harsh faction within warrior society, plaza setting context"

**Manual Description Required:** YES - Insufficient physical details for reliable image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Very sparse physical description. Only name reference in sleeping quarters context; no detailed physical features, build, or appearance characteristics provided in source material.
clarification_required: true
clarification_reason: Character is weakly identified - only mentioned by name in sleeping quarters with Carter and others; insufficient information for reliable identification or image generation.
clarification_question: What are Woola's physical characteristics (height, build, facial features)? Is this character a Martian or human? What role does Woola play in the narrative beyond sleeping quarters presence?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Woola - CH009 Character Profile

**Display Name:** Woola  
**Chapter Role:** Sleeping Quarters Occupant / Companion  
**Physical Presence:** Uncertain (only name reference in sleeping quarters)  
**Status:** Mentioned as present in sleeping quarters with Carter, Sola, and young Martians  

## Physical Description (Supported by Source)
- No physical description provided in source material
- Only referenced by name in sleeping quarters context

## Costume & Silhouette (Supported by Source)
- No costume or silhouette information documented
- Sleeping quarters occupant status only confirmed

## Continuity-Critical Traits
- Present in sleeping quarters with Carter and others
- Adults converse desultorily before sleep including Woola
- Topic of prisoner's visit to audience chamber discussed while present

## Uncertainty Notes
**Missing Physical Details:**
- No specific height, build, or facial features documented
- No skin tone, hair color, or eye characteristics mentioned
- No age indicators provided
- No distinguishing marks or scars noted
- **Species/Origin Unknown:** Not specified whether Martian or human

**Render-Facing Prompt Suggestions:**
"Character present in sleeping quarters with Carter and female warriors, companion role, conversation participant before sleep, species origin uncertain (Martian or human?), minimal physical description available"

**Manual Description Required:** YES - Insufficient physical details for reliable image generation  
**Clarification Required:** YES - Weak identification status needs clarification
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_prisoner_red_woman
canonical_character_id: the_prisoner_red_woman
aliases: prisoner, red woman, captive  
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided. Only referenced in discussions about fate and ransom; no detailed physical features, build, or appearance characteristics documented in source material.
clarification_required: true
clarification_reason: Character is weakly identified - only referenced as prisoner/red woman without stable identification; may exist under another name or be too weakly identified for reliable image generation.
clarification_question: What are the red woman's physical characteristics (height, build, facial features)? Is she a Martian or human? What specific appearance traits distinguish her from other characters?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# The Prisoner/Red Woman - CH009 Character Profile

**Display Name:** The Prisoner / Red Woman  
**Chapter Role:** Captive / Subject of Discussion  
**Physical Presence:** Referenced only (not physically present in chapter)  
**Status:** Discussed fate and ransom value; no physical description provided  

## Physical Description (Supported by Source)
- No physical description provided in source material
- Only referenced as "prisoner" or "red woman" in discussions

## Costume & Silhouette (Supported by Source)
- No costume or silhouette information documented
- Status as captive only confirmed through discussion

## Continuity-Critical Traits
- Smallness and beauty noted by Sola as ransom value factors
- Subject of fate discussion between warrior group members
- Will be taken to Thark for exhibition at great games before Tal Hajus
- Sarkoja states they will carry her to exhibit last agonies
- Sola expresses hope for ransom rather than execution

## Uncertainty Notes
**Missing Physical Details:**
- No specific height, build, or facial features documented
- No skin tone, hair color, or eye characteristics mentioned (only "red woman" designation)
- No age indicators provided
- No distinguishing marks or scars noted
- **Species/Origin Unknown:** Not specified whether Martian or human

**Render-Facing Prompt Suggestions:**
"Captive prisoner with small stature and beauty, subject of ransom discussion, will be exhibited at great games before Tal Hajus, red woman designation, species origin uncertain (Martian or human?), no physical description available"

**Manual Description Required:** YES - Insufficient physical details for reliable image generation  
**Clarification Required:** YES - Weak identification status needs clarification
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided. Only name reference in dialogue about Sola's defense; no detailed physical features, build, or appearance characteristics documented in source material.
clarification_required: true
clarification_reason: Character is weakly identified - only mentioned by name in dialogue without direct interaction or stable identification; may exist under another name or be too weakly identified for reliable image generation.
clarification_question: What are Tars Tarkas's physical characteristics (height, build, facial features)? Is this character a Martian? What role does Tars Tarkas play in the narrative beyond being referenced in dialogue?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Tars Tarkas - CH009 Character Profile

**Display Name:** Tars Tarkas  
**Chapter Role:** Referenced Authority Figure / Leader  
**Physical Presence:** Uncertain (only name reference in dialogue)  
**Status:** Mentioned by Sola in defense of her sentiments; no direct interaction documented  

## Physical Description (Supported by Source)
- No physical description provided in source material
- Only referenced by name in dialogue about Sola's defense

## Costume & Silhouette (Supported by Source)
- No costume or silhouette information documented
- Authority figure status only confirmed through reference

## Continuity-Critical Traits
- Sola defends her interest in red woman against Sarkoja's criticism
- Sarkoja warns Tars Tarkas against entrusting such sentiments to Sola regarding maternity responsibilities
- Referenced as authority figure whose judgment matters to warrior group members

## Uncertainty Notes
**Missing Physical Details:**
- No specific height, build, or facial features documented
- No skin tone, hair color, or eye characteristics mentioned
- No age indicators provided
- No distinguishing marks or scars noted
- **Species/Origin Unknown:** Not specified whether Martian or human

**Render-Facing Prompt Suggestions:**
"Authority figure referenced in warrior group dialogue, leader whose judgment matters to female warriors, species origin uncertain (Martian or human?), no physical description available, mentioned in context of maternity responsibilities discussion"

**Manual Description Required:** YES - Insufficient physical details for reliable image generation  
**Clarification Required:** YES - Weak identification status needs clarification
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
