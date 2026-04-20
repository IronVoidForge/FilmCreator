# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:24:10.416616+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH010

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Important rules:

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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

**Chapter Title:** Champion and Chief
**Chapter ID:** CH010
**Summary:**
Early in the morning, John Carter explores outside the city limits with Woola, testing the hound's loyalty and affection. He experiences a moment of misunderstanding when he laughs at Woola's playful affection; on Mars, laughter signifies torture and death, causing him to realize his mistake immediately. Upon returning to the plaza, Carter observes Dejah Thoris before Lorquas Ptomel and the Thark chieftains. During the interrogation, Dejah Thoris explains her peaceful scientific mission from Helium and pleads for amity between the red and green men. Sarkoja is present and displays cruelty toward the prisoner. When a young warrior strikes Dejah Thoris across the face, John Carter intervenes, killing the brute in his rage. He gains the status of a Tharkian chieftain through this act, receiving the dead warrior's trappings. John Carter explains himself to Dejah Thoris, revealing his name and origin (Virginia, Earth). Tars Tarkas informs him that he is now accorded respect as a conqueror but warns him of the responsibilities attached to his new status, including the potential danger if Tal Hajus deems him unworthy. The chapter concludes with John Carter and Dejah Thoris leaving the audience chamber together, accompanied by Woola, having established a bond of protection and friendship despite their captor status.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH010 Champion and Chief

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Description Required | Clarification Required |
|----------|------------------------|---------|------------------|----------------------|------------------------|
| protagonist | CH002 Protagonist | Narrator, Conscious Entity | false | Sparse physical detail. | true |
| woola | CH003 Woola | Hound Companion | true | Loyal Mars hound. | false |
| dejah_thoris | CH004 Dejah Thoris | Princess of Helium | true | Scientific mission from Earth. | false |
| lorquas_ptomel | CH005 Lorquas Ptomel | Thark Chieftain | true | Interrogation audience member. | false |
| sarkoja | CH006 Sarkoja | Cruel Presence | true | Displays cruelty toward prisoner. | false |
| young_warrior | CH007 Young Warrior | Striking Brute | true | Killed by John Carter in rage. | false |
| tars_tarkas | CH008 Tars Tarkas | Thark Informant | true | Warns of conqueror responsibilities. | false |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Protagonist

**Chapter Role:** Narrator, Conscious Entity  
**Physical Presence:** Referenced throughout chapter  
**Physical Description:** Identified as John Carter from Virginia, Earth. Physical form on Mars not explicitly detailed in source text.  
**Costume/Silhouette:** Receives dead warrior's trappings after killing the brute. Status of Tharkian chieftain conferred through this act.  
**Continuity-Critical Traits:** Gains respect as conqueror per Tars Tarkas. Bond of protection and friendship established with Dejah Thoris despite captor status.  
**Uncertainty Notes:** Physical form on Mars remains unspecified in source material.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH003 Woola

aliases: Hound Companion

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A

clarification_required: false

clarification_reason: N/A

clarification_question: N/A

[[SECTION markdown]]

# Woola

**Chapter Role:** Loyal Mars Hound  
**Physical Presence:** Present throughout chapter  
**Physical Description:** Mars hound companion of John Carter. Testing loyalty and affection during early morning exploration outside city limits.  
**Costume/Silhouette:** None - natural animal form.  
**Continuity-Critical Traits:** Demonstrates playful affection toward Carter; receives immediate realization from Carter about laughter meaning torture on Mars. Bond of protection and friendship established with Dejah Thoris.  
**Uncertainty Notes:** Physical description limited to species identification as hound.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH004 Dejah Thoris

aliases: Princess of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A

clarification_required: false

clarification_reason: N/A

clarification_question: N/A

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Princess, Scientific Missionary  
**Physical Presence:** Present during interrogation scene  
**Physical Description:** Princess from Helium with peaceful scientific mission. Pleads for amity between red and green men.  
**Costume/Silhouette:** None - royal attire not specified in source text.  
**Continuity-Critical Traits:** Explains peaceful scientific mission from Helium. Receives protection and friendship bond with John Carter despite captor status.  
**Uncertainty Notes:** Physical description limited to species identification as human female.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH005 Lorquas Ptomel

aliases: Thark Chieftain

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A

clarification_required: false

clarification_reason: N/A

clarification_question: N/A

[[SECTION markdown]]

# Lorquas Ptomel

**Chapter Role:** Thark Chieftain, Audience Member  
**Physical Presence:** Present during interrogation scene  
**Physical Description:** Thark chieftain observing from audience chamber.  
**Costume/Silhouette:** None - Thark attire not specified in source text.  
**Continuity-Critical Traits:** Part of Thark chieftains present during Dejah Thoris's explanation and plea for amity.  
**Uncertainty Notes:** Physical description limited to species identification as Thark male.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH006 Sarkoja

aliases: Cruel Presence

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A

clarification_required: false

clarification_reason: N/A

clarification_question: N/A

[[SECTION markdown]]

# Sarkoja

**Chapter Role:** Cruel Presence  
**Physical Presence:** Present during interrogation scene  
**Physical Description:** Displays cruelty toward the prisoner.  
**Costume/Silhouette:** None - attire not specified in source text.  
**Continuity-Critical Traits:** Demonstrates cruel behavior toward Dejah Thoris during interrogation.  
**Uncertainty Notes:** Physical description limited to species identification as Thark female.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_warrior

canonical_character_id: CH007 Young Warrior

aliases: Striking Brute

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A

clarification_required: false

clarification_reason: N/A

clarification_question: N/A

[[SECTION markdown]]

# Young Warrior

**Chapter Role:** Thark Warrior, Audience Member  
**Physical Presence:** Present during interrogation scene  
**Physical Description:** Young Thark warrior who strikes Dejah Thoris across the face. Killed by John Carter in his rage.  
**Costume/Silhouette:** None - Thark attire not specified in source text.  
**Continuity-Critical Traits:** Receives dead warrior's trappings after being killed. Status of conqueror conferred through this act.  
**Uncertainty Notes:** Physical description limited to species identification as Thark male.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH008 Tars Tarkas

aliases: Thark Informant

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A

clarification_required: false

clarification_reason: N/A

clarification_question: N/A

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Thark Informant, Conqueror Advisor  
**Physical Presence:** Present during audience chamber scene  
**Physical Description:** Informs John Carter of his new status as conqueror. Warns of responsibilities attached to this position.  
**Costume/Silhouette:** None - Thark attire not specified in source text.  
**Continuity-Critical Traits:** Accords respect to John Carter as conqueror but warns of potential danger if Tal Hajus deems him unworthy.  
**Uncertainty Notes:** Physical description limited to species identification as Thark male.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: CH009 Tal Hajus

aliases: Potential Judge

is_fully_identified: false

manual_description_required: true

manual_description_reason: Referenced only, not physically present.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is Tal Hajus's role and relationship to John Carter?

[[SECTION markdown]]

# Tal Hajus

**Chapter Role:** Potential Judge of Conqueror Status  
**Physical Presence:** Not physically present in chapter  
**Physical Description:** Referenced only - potential danger if deemed unworthy by this entity.  
**Costume/Silhouette:** None - attire not specified in source text.  
**Continuity-Critical Traits:** Warned about by Tars Tarkas as potential judge of John Carter's worthiness.  
**Uncertainty Notes:** Physical description limited to species identification as Thark. Not physically present in chapter.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: red_green_men

canonical_character_id: CH010 Red and Green Men

aliases: Amity Seekers

is_fully_identified: false

manual_description_required: true

manual_description_reason: Referenced only, not physically present.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the relationship between red men (Tharks) and green men (Helium)?

[[SECTION markdown]]

# Red and Green Men

**Chapter Role:** Amity Seekers  
**Physical Presence:** Not physically present in chapter  
**Physical Description:** Referenced only - Dejah Thoris pleads for amity between these groups.  
**Costume/Silhouette:** None - attire not specified in source text.  
**Continuity-Critical Traits:** Red men = Tharks, Green men = Heliumians. Peaceful scientific mission from Helium mentioned.  
**Uncertainty Notes:** Physical description limited to species identification as human/Thark groups. Not physically present in chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
