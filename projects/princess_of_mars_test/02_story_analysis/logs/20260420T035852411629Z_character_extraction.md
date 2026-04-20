# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:58:52.411629+00:00
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

Chapter id: CH018

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

# Chapter 18 Summary: CHAINED IN WARHOON

## Story Events

### Consciousness & Initial Encounter
- Carter regains consciousness several hours after capture
- Waking in small room with sleeping silks, furs, and green warriors
- Ancient female tends his wounds; confirms he is fit to travel
- Dak Kova (jeddak's lieutenant) examines him, references "great games"

### The Battle Scene
- Carter brought before Jeddak Bar Comas of Warhoon hordes
- Dak Kova omits formal salutation, presents Carter for combat at games
- Bar Comas: young, scarred, decorated with human skulls and dried hands
- Dak Kova: old lieutenant, fiercely jealous, insults Bar Comas as "water-hearted weakling"
- Physical battle ensues between two green warriors using natural weapons
- Bar Comas stronger, quicker, more intelligent but ultimately defeated
- Dak Kova kills Bar Comas with single tusk thrust to groin, wedges in jaw bones
- Three days later Dak Kova assumes title of Jeddak of Warhoon

### Expedition Abandoned
- Injuries delay march significantly
- Decision made to abandon raid on Thark community until after great games
- Ten thousand warriors turn back toward Warhoon

### Carter's Imprisonment
- Introduced to cruel, bloodthirsty people through daily mortal duels (up to eight per day)
- Cast into dungeon with heavy chains attached to floor and walls
- Utter darkness prevents knowing duration of imprisonment
- Cell filled with creeping, crawling things; gleaming fiery eyes in darkness

### Escape Attempt
- Carter's hatred centers on single emissary who brings food
- Uses cunning: backs into corner when jailer approaches
- Swings chain above head, crashes links onto skull
- Dead body reveals small chain with keys dangling from throat
- Keys restore his reason; no longer jibbering idiot but sane man with escape means
- Six pairs of gleaming eyes approach then retreat in black recess

## Visual Continuity Facts

### Character Descriptions
- Green-skinned warriors: Martian physiology, natural weapons (tusks)
- Dak Kova: terribly scarred face and chest, one broken tusk, missing ear
- Bar Comas: comparatively young, frightfully scarred, decorated with human skulls and dried hands
- Carter's injuries: wounds healed rapidly by female's therapeutic applications

### Setting Details
- Warhoon warriors wear ornaments of human skulls and dried dead hands
- All greater warriors among Warhoons share these decorations indicating ferocity
- Dungeon: utter darkness, filled with creeping crawling things
- Warriors battle using nature's weapons (hands, tusks)

### Key Objects
- Chain: held Carter in dungeon, used to kill jailer
- Keys: small chain at end of dead man's neck, means of escape
- Torch: dim torch carried by food-bearer
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter 18 Character Index

- **Carter**: Protagonist, human prisoner of Warhoon.
- **Dak Kova**: Martian warrior, Jeddak's lieutenant, scarred.
- **Bar Comas**: Martian warrior, Jeddak of Warhoon hordes, scarred.
- **Ancient Female**: Unnamed healer, tends wounds.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance details (hair, eyes, build) are not provided in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
## Carter

- **Chapter Role**: Protagonist, prisoner of Warhoon.
- **Physical Presence**: Present in the small room and dungeon.
- **Visual Description**: Human physiology (inferred from 'human skulls'). Rapid wound healing observed. Mental state described as 'jibbering idiot' initially, then 'sane man'.
- **Uncertainty Notes**: Specific physical traits such as hair color, eye color, facial structure, and body build are not detailed in the chapter summary.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: dak_kova
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
## Dak Kova

- **Chapter Role**: Jeddak's lieutenant, becomes Jeddak of Warhoon.
- **Physical Presence**: Present in battle scenes and examination.
- **Visual Description**: Green-skinned Martian warrior. Terribly scarred face and chest. One broken tusk. Missing ear. Wears ornaments of human skulls and dried dead hands.
- **Continuity Notes**: Killed Bar Comas with single tusk thrust.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bar_comas
canonical_character_id: bar_comas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
## Bar Comas

- **Chapter Role**: Jeddak of Warhoon hordes.
- **Physical Presence**: Present in battle scene, killed by Dak Kova.
- **Visual Description**: Green-skinned Martian warrior. Comparatively young. Frightfully scarred. Decorated with human skulls and dried hands.
- **Continuity Notes**: Defeated by Dak Kova in combat.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: ancient_female
canonical_character_id: ancient_female
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description (hair, eyes, build) or proper name is provided in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
## Ancient Female

- **Chapter Role**: Healer/Tender.
- **Physical Presence**: Present in Carter's room.
- **Visual Description**: Referred to as 'Ancient female'.
- **Uncertainty Notes**: No physical description (hair, eyes, build) or proper name is provided in the chapter summary.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
