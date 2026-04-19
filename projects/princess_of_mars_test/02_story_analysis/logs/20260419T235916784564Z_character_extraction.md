# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:59:16.784564+00:00
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

Chapter id: CH007

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

# Chapter Summary - CH007: Child-Raising on Mars

## Scene Sequence and Visual Continuity

### Opening Scene: Plaza with Chariots
- **Location**: Plaza where entire community is engaged in harnessing huge mastodonian animals to three-wheeled chariots
- **Visual Details**: Approximately 250 vehicles, each drawn by single animal without bit or bridle, guided entirely by telepathic means
- **Chariot Description**: Large, commodious, gorgeously decorated with ornaments of metal, jewels, silks, and furs
- **Occupants**: Female Martians loaded with ornaments seated in chariots; young Martian drivers perched on beasts' backs
- **Procession Formation**: 200 warriors at head riding five abreast; like number at rear; 25-30 outriders flanking sides
- **Visual Continuity**: Breakfast replica of preceding day's meal (index of all subsequent meals)

### Incubator Ceremony Scene
- **Location**: Terminal point of journey - incubator enclosure
- **Egg Hatching Status**: All but very few eggs hatched; incubator fairly alive with hideous little devils 3-4 feet tall
- **Narrator's Performance**: Leaps entirely over parked chariots on far side for edification of Lorquas Ptomel
- **Ceremony Mechanics**: Opening broken in wall large enough for exit; women and younger Martians form two solid walls leading through chariots into plain
- **Capture System**: Little Martians scamper wild as deer; captured one at a time by women/older children; last in line captures first to reach end of gauntlet

### Post-Ceremony Scene: Incubator Operations
- **Location**: Side of incubator where warriors stood
- **Participants**: Half score warriors headed by enormous chieftain Lorquas Ptomel Jed, including Tars Tarkas and several lesser chiefs
- **Activity**: Breaking opening in wall; women fall out of line returning to respective chariots; young men turn over captured ones to some women

### Educational Development Scene
- **Location**: Narrator's chariot with Sola holding hideous little creature
- **Teaching Focus**: Work of rearing consists solely in teaching them to talk and use weapons from first year of life
- **Parental Structure**: Young step forth into world perfectly developed except in size; unknown to mothers who would have difficulty pointing out fathers
- **Foster Mother System**: Education devolves upon females who chance to capture young leaving incubator

### Aftermath Scene: Dead City Return
- **Location**: Dead city after return from incubator journey
- **Duration**: Narrator passed several days in comparative idleness
- **Warrior Activity**: All warriors rode forth early morning; returned just before darkness fell
- **Egg Transport**: Warriors transported eggs to subterranean vaults and walled up incubator for another five years

### Training Development Scene
- **Location**: Comparative setting with Sola
- **Sola's Duties**: Now doubled - caring for young Martian as well as narrator
- **Training Method**: Both equally advanced in Martian education; Sola trains them together
- **Narrator's Progress**: In week could make all wants known and understand nearly everything said to him
- **Telepathic Development**: Shortly could sense practically everything going on around me
- **Unique Advantage**: Could catch telepathic messages easily from others, often when not intended for me; no one could read jot from my mind under any circumstances

## Character Arcs in Chapter
- **Sola**: Prize consists in male about four feet tall, very strong and physically perfect; learned quickly; narrator displays keen rivalry with amusement
- **Narrator**: Mastered intricacies of walking under Martian conditions; developed telepathic powers so that shortly could sense practically everything around me

## Location Map for Scene Decomposition
1. Plaza (chariot harnessing)
2. Incubator enclosure (ceremony operations)
3. Dead city (return and idleness period)
4. Subterranean vaults (egg storage - referenced but not visited in chapter)
5. Narrator's chariot (training with Sola)

## Key Dialogue Moments
- Tars Tarkas: "Sak" (commanding narrator to repeat performance)
- Lorquas Ptomel: Grunted something at narrator after leap; gave words of command relative to incubator
- Narrator's internal observations about Martian child-raising system and its effects on humanitarian instincts
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH007: Child-Raising on Mars

| Asset ID | Canonical Name | Role in Chapter | Physical Presence | Description Status |
|----------|----------------|------------------|-------------------|-------------------|
| sola | Sola | Foster mother/caregiver of young Martians | Present throughout multiple scenes | Manual description required |
| narrator | The Narrator | First-person protagonist experiencing Martian child-raising | Referenced as first-person narrator | Manual description required |
| lorquas_ptomel_jed | Lorquas Ptomel Jed | Enormous chieftain leading warriors | Present in post-ceremony scene | Manual description required |
| tars_tarkas | Tars Tarkas | Warrior giving commands to narrator | Referenced in dialogue moments | Manual description required |

**Note:** Groups such as "Women Martians" and "Younger Martians" are referenced but not individually identified; they lack stable identification for character records.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter mentions Sola holding a hideous little creature and caring for young Martians, but provides no detailed physical description of her appearance, features, or distinguishing visual traits necessary for dependable later image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File - Sola

**Display Name:** Sola  
**Chapter Role:** Foster mother/caregiver of young Martians  
**Physical Presence:** Present throughout multiple scenes (Educational Development Scene, Aftermath Scene, Training Development Scene)  

**Physical Description:** Not detailed beyond holding a hideous little creature. No specific features, height, or distinguishing visual traits provided in source material.

**Costume/Silhouette/Continuity Traits:** Unknown. No costume details or silhouette information available from chapter text.

**Useful Descriptive Noun Phrases for Render-Facing Prompts:** 
- Female Martian caregiver
- Foster mother of young Martians  
- Holds hideous little creature
- Trains narrator and young together

**Uncertainty Notes:** Complete lack of physical description prevents dependable later image generation. Chapter focuses on her role in child-raising system rather than visual appearance. Continuity-critical traits are not documented beyond her functional role as foster mother.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: The Narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter provides first-person narrative but contains no physical description of the narrator's appearance, features, or visual characteristics necessary for dependable later image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File - The Narrator

**Display Name:** The Narrator  
**Chapter Role:** First-person protagonist experiencing Martian child-raising system  
**Physical Presence:** Referenced throughout as first-person narrator (not visually described)  

**Physical Description:** None provided. Chapter focuses on internal experiences, telepathic development, and learning processes rather than physical appearance.

**Costume/Silhouette/Continuity Traits:** Unknown. No costume details or silhouette information available from chapter text.

**Useful Descriptive Noun Phrases for Render-Facing Prompts:** 
- First-person Martian protagonist
- Learner of telepathic powers
- Mastered walking under Martian conditions
- Receives telepathic messages from others

**Uncertainty Notes:** Complete lack of physical description prevents dependable later image generation. Narrator's identity is established through narrative voice and experiences rather than visual characteristics. Continuity-critical traits are not documented beyond functional role as protagonist experiencing child-raising system.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel_jed
canonical_character_id: Lorquas Ptomel Jed
aliases: Lorquas Ptomel (partial)
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter describes him as "enormous chieftain" but provides no detailed physical description of his appearance, features, or visual characteristics necessary for dependable later image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File - Lorquas Ptomel Jed

**Display Name:** Lorquas Ptomel Jed  
**Chapter Role:** Enormous chieftain leading warriors in post-ceremony operations  
**Physical Presence:** Present in Post-Ceremony Scene (Incubator Operations)  

**Physical Description:** Described as "enormous" but no detailed physical description of his appearance, features, or visual characteristics provided in source material.

**Costume/Silhouette/Continuity Traits:** Unknown. No costume details or silhouette information available from chapter text.

**Useful Descriptive Noun Phrases for Render-Facing Prompts:** 
- Enormous chieftain
- Leader of warriors including Tars Tarkas
- Gives commands relative to incubator operations
- Half score warriors headed by him

**Uncertainty Notes:** Only size indication ("enormous") provided, no visual details. Chapter focuses on his leadership role and command authority rather than physical appearance. Continuity-critical traits are not documented beyond functional role as chieftain leading warrior group.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter mentions Tars Tarkas giving command "Sak" but provides no physical description of his appearance, features, or visual characteristics necessary for dependable later image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File - Tars Tarkas

**Display Name:** Tars Tarkas  
**Chapter Role:** Warrior giving commands to narrator in Educational Development Scene  
**Physical Presence:** Referenced in dialogue moments (command "Sak")  

**Physical Description:** None provided. Only command dialogue mentioned, no physical description of his appearance or features.

**Costume/Silhouette/Continuity Traits:** Unknown. No costume details or silhouette information available from chapter text.

**Useful Descriptive Noun Phrases for Render-Facing Prompts:** 
- Warrior giving commands
- Part of half score warriors headed by Lorquas Ptomel Jed
- Commands narrator to repeat performance ("Sak")
- Lesser chief status implied

**Uncertainty Notes:** Complete lack of physical description prevents dependable later image generation. Character is identified only through command dialogue and warrior group membership. Continuity-critical traits are not documented beyond functional role as commanding warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
