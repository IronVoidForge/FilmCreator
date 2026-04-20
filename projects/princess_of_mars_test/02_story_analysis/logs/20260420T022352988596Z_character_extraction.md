# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:23:52.988596+00:00
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

## Chapter 10: CHAMPION AND CHIEF

### Story Summary
John Carter explores the city limits with Woola, bonding over their shared understanding and affection. He witnesses a council meeting in the audience chamber where Dejah Thoris is questioned by Lorquas Ptomel regarding her expedition from Helium. A young Thark warrior insults Dejah Thoris and strikes her down; John Carter intervenes, killing the warrior to save her. Following Martian custom, he is given the dead warrior's regalia and arms, elevating his status as a chieftain. Tars Tarkas explains the customs of combat and captivity to John Carter, noting that his valor has earned him respect but also responsibility for his safe delivery to Tal Hajus. John Carter asserts his humanity and conscience before departing with Dejah Thoris and Woola from the chamber.

### Visual Continuity
- **Woola's Behavior:** Initially anxious and pleading against leaving the city; later playful and affectionate after bonding with John Carter.
- **Dejah Thoris's Demeanor:** Gives a haughty glance to John Carter upon seeing him; watches the battle with wide, staring eyes while injured.
- **The Warrior's Death:** The dead antagonist's body is stripped by another warrior; regalia and accoutrements are brought to John Carter in a respectful yet menacing manner.
- **John Carter's Status:** He wears the regalia of a Thark chieftain, which explains his freedom and tolerance in the audience chamber.
- **Tars Tarkas's Reaction:** His eyes rest upon John Carter in a quizzical manner; he addresses him directly regarding his language skills and valor.
- **Injury Details:** Dejah Thoris suffers a nosebleed from the blow; John Carter uses silk from his cape to staunch the flow.
- **Audience Chamber Setting:** The council squats on steps of a rostrum; guards stand below; prisoners are held before the entrance.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter 10 (CHAMPION AND CHIEF)

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence | Description Status |
|----------|----------------------|--------------|------|-------------------|-------------------|
| john_carter | John Carter | John Carter | Protagonist, Thark Chieftain | Present in chamber | Fully identified |
| woola | Woola | Woola | Dog companion | Present in chamber | Partially described |
| dejah_thoris | Dejah Thoris | Dejah Thoris | Princess of Helium | Present in chamber | Fully identified |
| lorquas_ptomel | Lorquas Ptomel | Lorquas Ptomel | Council member | Present in chamber | Limited description |
| thark_warrior_young | Thark Warrior (Young) | Young Thark Warrior | Antagonist warrior | Killed in chamber | Limited description |
| tars_tarkas | Tars Tarkas | Tars Tarkas | Elder/Mentor | Present in chamber | Fully identified |

**Notes:**
- All characters are present in the audience chamber setting
- John Carter wears Thark regalia elevating his status
- Dejah Thoris is injured from warrior's blow
- Young Thark Warrior is deceased and stripped of regalia
- Tars Tarkas serves as cultural guide to John Carter

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by source material (wearing Thark regalia, cape with silk)
clarification_required: false
clarification_reason: Character has stable identification across chapter
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter 10

**Display Name:** John Carter  
**Chapter Role:** Protagonist, Thark Chieftain  
**Physical Presence:** Present in audience chamber  

**Physical Description (Supported by Source):**
- Wears regalia of Thark chieftain (freedom and tolerance in chamber)
- Has cape with silk used to staunch Dejah Thoris's nosebleed
- Intervenes in battle, kills young Thark warrior

**Costume & Silhouette:**
- Thark chieftain regalia (elevated status marker)
- Cape with usable silk material
- Human form but elevated through Martian custom

**Continuity-Critical Traits:**
- Humanity and conscience asserted before departing chamber
- Valor earned him respect but also responsibility for safe delivery to Tal Hajus
- Status as chieftain explains his freedom in audience chamber

**Uncertainty Notes:**
- Specific facial features not detailed in source material
- Exact regalia design elements beyond general description

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only behavioral traits described (anxious, pleading, playful, affectionate); no physical appearance details provided in source material
clarification_required: false
clarification_reason: Character has stable identification across chapter
clarification_question: 

[[SECTION markdown]]
# Woola - Chapter 10

**Display Name:** Woola  
**Chapter Role:** Dog companion to John Carter  
**Physical Presence:** Present in audience chamber  

**Physical Description (Supported by Source):**
- None provided in source material
- Behavioral traits only: initially anxious and pleading against leaving city; later playful and affectionate after bonding with John Carter

**Costume & Silhouette:**
- Dog form (species not further specified)
- Companion animal to protagonist

**Continuity-Critical Traits:**
- Bonding arc from anxiety to playfulness with John Carter
- Present throughout chamber scenes with both characters

**Uncertainty Notes:**
- Breed, size, and color not described in source material
- Physical appearance insufficient for dependable image generation without manual description
- Behavioral continuity is primary identifier in this chapter

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by source material (haughty demeanor, nosebleed from blow, wide staring eyes while injured)
clarification_required: false
clarification_reason: Character has stable identification across chapter
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter 10

**Display Name:** Dejah Thoris  
**Chapter Role:** Princess of Helium, Council witness  
**Physical Presence:** Present in audience chamber  

**Physical Description (Supported by Source):**
- Gives haughty glance to John Carter upon seeing him
- Nosebleed from warrior's blow
- Wide, staring eyes while injured
- Questioned by Lorquas Ptomel regarding expedition from Helium

**Costume & Silhouette:**
- Princess attire (implied through status)
- Injured state during chamber scene

**Continuity-Critical Traits:**
- Haughty demeanor toward John Carter
- Injury details: nosebleed requiring silk from John Carter's cape
- Watches battle with wide, staring eyes while injured
- Status as princess of Helium established through questioning context

**Uncertainty Notes:**
- Specific facial features beyond injury not detailed in source material
- Exact costume design elements not specified

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only role described (council member questioning Dejah Thoris); no physical appearance details provided in source material
clarification_required: false
clarification_reason: Character has stable identification across chapter
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel - Chapter 10

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Council member, questioner of Dejah Thoris  
**Physical Presence:** Present in audience chamber  

**Physical Description (Supported by Source):**
- None provided in source material
- Only role described: questioning Dejah Thoris regarding expedition from Helium

**Costume & Silhouette:**
- Council member attire (implied through status)
- Squats on steps of rostrum with other council members

**Continuity-Critical Traits:**
- Questions Dejah Thoris about her expedition from Helium
- Part of council that squats on steps of rostrum in audience chamber
- Guards stand below; prisoners held before entrance (chamber setting context)

**Uncertainty Notes:**
- Physical appearance not described in source material
- Specific facial features or distinguishing marks not provided
- Role-based identification only for this chapter

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: thark_warrior_young
canonical_character_id: Thark Warrior (Young)
aliases: Young Thark Warrior, Antagonist warrior
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only role and actions described (insults Dejah Thoris, strikes her down, killed by John Carter); no physical appearance details provided in source material
clarification_required: false
clarification_reason: Character has stable identification across chapter
clarification_question: 

[[SECTION markdown]]
# Young Thark Warrior - Chapter 10

**Display Name:** Young Thark Warrior  
**Chapter Role:** Antagonist warrior, insulted Dejah Thoris  
**Physical Presence:** Killed in audience chamber  

**Physical Description (Supported by Source):**
- None provided in source material
- Actions: insults Dejah Thoris, strikes her down, killed by John Carter

**Costume & Silhouette:**
- Thark warrior attire (implied through species and role)
- Stripped of regalia and accoutrements after death by another warrior

**Continuity-Critical Traits:**
- Insults Dejah Thoris before striking her down
- Killed by John Carter to save her
- Body stripped by another warrior after death
- Regalia and accoutrements brought to John Carter in respectful yet menacing manner
- Death elevates John Carter's status as chieftain through custom

**Uncertainty Notes:**
- Physical appearance not described in source material
- Specific facial features or distinguishing marks not provided
- Only role-based identification for this chapter
- Deceased character with limited continuity beyond regalia transfer

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only role and actions described (explains customs of combat and captivity, addresses John Carter regarding language skills and valor); no physical appearance details provided in source material
clarification_required: false
clarification_reason: Character has stable identification across chapter
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Chapter 10

**Display Name:** Tars Tarkas  
**Chapter Role:** Elder/Mentor, cultural guide to John Carter  
**Physical Presence:** Present in audience chamber  

**Physical Description (Supported by Source):**
- None provided in source material
- Eyes rest upon John Carter in quizzical manner
- Addresses him directly regarding language skills and valor

**Costume & Silhouette:**
- Elder figure (implied through role)
- Cultural authority figure explaining Martian customs

**Continuity-Critical Traits:**
- Explains customs of combat and captivity to John Carter
- Notes John Carter's valor has earned him respect but also responsibility for safe delivery to Tal Hajus
- Eyes rest upon John Carter in quizzical manner during chamber scene
- Addresses John Carter directly regarding his language skills

**Uncertainty Notes:**
- Physical appearance not described in source material
- Specific facial features or distinguishing marks not provided
- Only role-based identification for this chapter
- Cultural guide function is primary identifier in this chapter

[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
