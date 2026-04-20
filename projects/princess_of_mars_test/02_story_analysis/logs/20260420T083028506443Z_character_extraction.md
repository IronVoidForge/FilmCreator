# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:30:28.506443+00:00
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

Chapter id: CH026

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

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- emit one explicit character record per meaningful character mention

- every character record must have a FILMCREATOR_RECORD wrapper with type character

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

# Chapter XXVI Summary: "Through Carnage to Joy"

## Key Events

### Naval Victory
- Tars Tarkas and Kantos Kan return reporting Zodanga completely reduced; forces destroyed or captured
- Fleet of 250 battleships carrying 100,000 green warriors sails from dock buildings
- Lesser hordes (40,000 green warriors) left behind looting and destroying stricken city with torches applied in 100 places

### Air Battle Engagement
- Helium's scarlet and yellow towers sighted; Zodangan fleet rises to meet them
- Green Martian warriors open fire on Zodangans with uncanny marksmanship
- First real air battle witnessed - Heliumite squadron defeats Zodangan fleet
- Zodangan battleships torn apart, crews plunging toward ground 1000 feet below
- Commander of entire Zodangan fleet takes fearful plunge indicating surrender

### Princess Dejah Thoris Transfer
- John Carter signals flagship that Princess Dejah Thoris is on board
- Helium's colors break from upper works as they acclaim the Princess
- Dejah Thoris boards flagship and receives officers with grace
- She introduces John Carter, saying "Helium owes her princess as well as her victory today"
- Officers impressed by his win of Thark aid for liberation campaign

### Land Campaign Continues
- Transports with thoats unloaded over difficult terrain (slings required)
- Land attack on Zodangan camp begins from three directions (north, south, east)
- Helium armies arrive at noon, crushing Zodangans between two millstones
- Carnage ceases, prisoners marched to Helium

### Triumphal Entry
- Entry into greater city as huge triumphal procession of conquering heroes
- City goes mad with joy; women and children line broad avenues
- Tharks cause wildest excitement - first armed body of green warriors enter as friends
- John Carter's name loudly cried, loads of ornaments fastened on him and Woola

### Palace Reception
- Meet Tardos Mors, Jeddak of Helium at palace steps
- Tars Tarkas speaks words of friendship between races
- Mors Kajak (father of Dejah Thoris) expresses deep emotion and gratitude
- Both rulers exchange formal greetings establishing new friendship between Tharks and Heliumites

## Characters Introduced/Featured

### Primary Characters
- **John Carter**: Hero, Jeddak of Helium, won Princess Dejah Thoris's liberation
- **Tars Tarkas**: Jeddak of Thark, great warrior and statesman of Barsoom
- **Dejah Thoris**: Princess of Helium, daughter of Mors Kajak
- **Tardos Mors**: Jeddak of Helium, grandfather of Dejah Thoris
- **Mors Kajak**: Jed of lesser Helium, father of Dejah Thoris

### Supporting Characters
- **Kantos Kan**: Green warrior companion
- **Woola**: John Carter's fierce Thark companion
- **Zodangan Fleet Commanders**: Vanquished enemy forces

## Settings and Locations

### Cities
- **Helium (Greater)**: Scarlet and yellow towers, main city of victory
- **Helium (Lesser)**: Secondary city with Mors Kajak as Jed
- **Stricken City**: Zodangan territory being destroyed by lesser hordes

### Military Installations
- **Dock Buildings**: Fleet departure point
- **Ancient Sea Bottom**: Where crashed battleships land
- **Palace Grounds**: Reception area for triumphant heroes

## Character Relationships Established

- John Carter and Dejah Thoris: Hero-princess bond, mutual respect
- Tars Tarkas and Helium Rulers: New friendship between Tharks and Heliumites
- Mors Kajak and John Carter: Father's deep emotion over daughter's liberation
- Green Warriors and Helium Citizens: First time entering as friends rather than enemies

## Military Significance

- Naval victory establishes Thark-Helium alliance
- Air battle demonstrates uncanny Martian marksmanship
- Land campaign completes liberation of Princess Dejah Thoris
- Surrender customs honored (commander's voluntary plunge)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter XXVI

## John Carter (asset_id: john_carter)
- **Canonical ID**: CH002 Protagonist
- **Aliases**: Hero, Jeddak of Helium
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: Main hero, won Princess Dejah Thoris's liberation

## Tars Tarkas (asset_id: tars_tarkas)
- **Canonical ID**: CH003 Tars Tarkas
- **Aliases**: Jeddak of Thark
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: Great warrior and statesman of Barsoom

## Dejah Thoris (asset_id: dejah_thoris)
- **Canonical ID**: CH004 Dejah Thoris
- **Aliases**: Princess of Helium, Daughter of Mors Kajak
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: Princess transferred to flagship

## Tardos Mors (asset_id: tardos_mors)
- **Canonical ID**: CH005 Tardos Mors
- **Aliases**: Jeddak of Helium, Grandfather of Dejah Thoris
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: Palace reception host

## Mors Kajak (asset_id: mors_kajak)
- **Canonical ID**: CH006 Mors Kajak
- **Aliases**: Jed of lesser Helium, Father of Dejah Thoris
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: Palace reception guest

## Kantos Kan (asset_id: kantos_kan)
- **Canonical ID**: CH007 Kantos Kan
- **Aliases**: Green warrior companion
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: John Carter's companion

## Woola (asset_id: woola)
- **Canonical ID**: CH008 Woola
- **Aliases**: Fierce Thark companion
- **Status**: Fully identified
- **Physical Description**: Sparse detail available
- **Chapter Role**: John Carter's Thark companion

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH002 Protagonist

aliases: Hero, Jeddak of Helium

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# John Carter

**Chapter Role**: Hero, Jeddak of Helium  
**Physical Presence**: Referenced throughout chapter summary  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Hero of Barsoom, Jeddak (ruler) of Helium  
- **Companions**: Kantos Kan (green warrior), Woola (Thark companion)  
- **Achievement**: Won Princess Dejah Thoris's liberation campaign  
- **Recognition**: Name loudly cried during triumphal entry; ornaments fastened on him  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Alliance Status**: Established friendship with Tharks and Heliumites  
- **Military Role**: Commander of Helium forces, signals flagship  
- **Public Reception**: Officers impressed by his win; city goes mad with joy  

## Render-Facing Prompt Notes
- Use role-based descriptors: "heroic figure," "ruler of Helium"  
- Add uncertainty markers for physical attributes  
- Focus on action and achievement rather than appearance  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Jeddak of Thark

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role**: Jeddak of Thark, Great Warrior and Statesman  
**Physical Presence**: Referenced throughout chapter summary  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Jeddak (ruler) of Thark  
- **Role**: Great warrior and statesman of Barsoom  
- **Relationship**: Speaks words of friendship between races at palace reception  
- **Companions**: John Carter, Woola  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Diplomatic Role**: Establishes new friendship between Tharks and Heliumites  
- **Military Status**: Great warrior of Barsoom  
- **Political Standing**: Ruler of Thark territory  

## Render-Facing Prompt Notes
- Use role-based descriptors: "warrior statesman," "Thark ruler"  
- Add uncertainty markers for physical attributes  
- Focus on diplomatic and military presence rather than appearance  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH004 Dejah Thoris

aliases: Princess of Helium, Daughter of Mors Kajak

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role**: Princess of Helium  
**Physical Presence**: Referenced throughout chapter summary  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Princess of Helium, Daughter of Mors Kajak  
- **Achievement**: Won liberation campaign; receives officers with grace  
- **Relationship**: Introduces John Carter to officers; "Helium owes her princess as well as her victory today"  
- **Family**: Father is Mors Kajak (Jed of lesser Helium)  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Public Reception**: Helium's colors break from upper works as they acclaim the Princess  
- **Diplomatic Role**: Introduces John Carter with grace and authority  
- **Political Status**: Daughter of Mors Kajak, ruler of Helium  

## Render-Facing Prompt Notes
- Use role-based descriptors: "princess," "Heliumite noble"  
- Add uncertainty markers for physical attributes  
- Focus on grace and authority rather than appearance  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tardos_mors

canonical_character_id: CH005 Tardos Mors

aliases: Jeddak of Helium, Grandfather of Dejah Thoris

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# Tardos Mors

**Chapter Role**: Jeddak of Helium, Grandfather of Dejah Thoris  
**Physical Presence**: Referenced at palace reception  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Jeddak (ruler) of Helium  
- **Relationship**: Grandfather of Dejah Thoris  
- **Reception Role**: Meets heroes at palace steps; exchanges formal greetings with John Carter  
- **Political Standing**: Ruler of greater city of Helium  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Diplomatic Role**: Establishes new friendship between Tharks and Heliumites  
- **Political Status**: Ruler of greater city of Helium  
- **Family Connection**: Grandfather of Dejah Thoris  

## Render-Facing Prompt Notes
- Use role-based descriptors: "Helium ruler," "elder statesman"  
- Add uncertainty markers for physical attributes  
- Focus on diplomatic presence rather than appearance  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: mors_kajak

canonical_character_id: CH006 Mors Kajak

aliases: Jed of lesser Helium, Father of Dejah Thoris

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# Mors Kajak

**Chapter Role**: Jed of lesser Helium, Father of Dejah Thoris  
**Physical Presence**: Referenced at palace reception  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Jed (ruler) of lesser Helium  
- **Relationship**: Father of Dejah Thoris  
- **Reception Role**: Expresses deep emotion and gratitude; exchanges formal greetings with John Carter  
- **Political Standing**: Ruler of secondary city of Helium  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Emotional Role**: Expresses deep emotion and gratitude over daughter's liberation  
- **Political Status**: Ruler of lesser Helium  
- **Family Connection**: Father of Dejah Thoris  

## Render-Facing Prompt Notes
- Use role-based descriptors: "lesser city ruler," "father"  
- Add uncertainty markers for physical attributes  
- Focus on emotional presence rather than appearance  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: CH007 Kantos Kan

aliases: Green warrior companion

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# Kantos Kan

**Chapter Role**: Green warrior companion  
**Physical Presence**: Referenced as John Carter's companion  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Green warrior  
- **Relationship**: Companion to John Carter  
- **Military Role**: Part of Helium forces; participates in liberation campaign  
- **Status**: Allied with Helium and Tharks  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Alliance Status**: First time entering as friends rather than enemies  
- **Military Role**: Green warrior of Barsoom  
- **Companionship**: John Carter's companion  

## Render-Facing Prompt Notes
- Use role-based descriptors: "green warrior," "Martian soldier"  
- Add uncertainty markers for physical attributes  
- Focus on military presence rather than appearance  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH008 Woola

aliases: Fierce Thark companion

is_fully_identified: true

manual_description_required: true

manual_description_reason: Chapter summary provides only role-based identification without physical attributes (height, build, hair, eyes, clothing details).

clarification_required: false

clarification_reason: Character is well-established with clear name and role.

clarification_question: 

[[SECTION markdown]]

# Woola

**Chapter Role**: Fierce Thark companion  
**Physical Presence**: Referenced as John Carter's companion  
**Description Status**: Uncertain - sparse physical detail available  

## Known Attributes
- **Title**: Fierce Thark companion  
- **Relationship**: Companion to John Carter  
- **Military Role**: Part of Helium forces; participates in liberation campaign  
- **Recognition**: Name loudly cried during triumphal entry; ornaments fastened on him  

## Physical Description Notes
- Height, build, hair color, eye color: Not specified in chapter summary  
- Clothing/costume details: Not specified in chapter summary  
- Silhouette/continuity traits: Limited to role-based identification  

## Continuity-Critical Traits
- **Alliance Status**: First time entering as friends rather than enemies  
- **Military Role**: Thark warrior of Barsoom  
- **Companionship**: John Carter's companion  

## Render-Facing Prompt Notes
- Use role-based descriptors: "Thark warrior," "fierce companion"  
- Add uncertainty markers for physical attributes  
- Focus on loyalty and martial presence rather than appearance  

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
