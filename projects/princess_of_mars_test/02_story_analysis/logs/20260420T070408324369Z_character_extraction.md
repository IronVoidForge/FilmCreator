# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:04:08.324369+00:00
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

Chapter id: CH004

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

# Chapter IV: A PRISONER Summary

## Setting
Carter and his escort, Tars Tarkas, travel approximately ten miles before reaching the foot of mountains. They traverse a narrow gorge and enter an open valley containing a low table land with an enormous ruined city. The buildings show signs of extreme antiquity, possibly belonging to a long-extinct race, as they are deserted and not greatly decayed.

## Characters
- **John Carter:** The human protagonist, currently a prisoner but attempting to gain favor through physical demonstration.
- **Tars Tarkas:** Vice-chieftain of the community, escort, statesman, and warrior. He explains the situation regarding Carter's capture.
- **Martians (Green Men):** Approximately nine hundred creatures camped in the city. They are naked except for ornaments, have large tusks, long legs, and vary in height (adult females 10-12 feet).
- **Sola:** A young female Martian about eight feet tall, light olive-green, belonging to Tars Tarkas' retinue. She takes Carter to his quarters.
- **Principal Chieftain:** Ruler of the community, seated on a rostrum during the assembly.

## Events
1.  **Arrival at City:** Carter and Tars Tarkas enter the city through a ruined roadway. They observe the Martians camped in the plaza and buildings.
2.  **Martian Culture:** The text details Martian life expectancy (average 300 years after maturity, up to 1000 without violence), their violent death causes (duels, war, hunting), and their voluntary pilgrimage down the river Iss at age 1000.
3.  **Audience Chamber:** Carter is lowered to the ground and brought before the chieftain. A greeting ceremony occurs where names are exchanged between Tars Tarkas and the chieftain.
4.  **Physical Struggles:** Carter attempts to walk but fails, skipping like a grasshopper and bruising himself. He fights a Martian guard after being forced to stand, winning applause for his ability to fight back.
5.  **Demonstration of "Sak":** The Martians demand Carter perform the jump ("sak"). He succeeds in clearing 150 feet and landing squarely.
6.  **Demanding Sustenance:** Hungry and thirsty, Carter ignores further commands to jump and instead signals for food/water. Tars Tarkas arranges for him to be taken by a young female (Sola).
7.  **Quarters:** Sola leads Carter to a spacious chamber decorated with murals and mosaics. She signals for a ten-legged creature to appear, which waddles in like an obedient puppy.

## Key Observations
- The Martians are initially hostile but show approval when Carter demonstrates strength or humor (smiling).
- The architecture suggests a civilization older than the current inhabitants.
- Carter's human physiology is a liability for Martian tasks but becomes an asset when he adapts to their expectations (jumping, fighting).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter IV

## John Carter
- **Role:** Human protagonist, prisoner attempting to gain favor through physical demonstration
- **Status:** Physically present in chapter
- **Description:** Human physiology (sparse physical detail)

## Tars Tarkas
- **Role:** Vice-chieftain of the community, escort, statesman, warrior
- **Status:** Physically present in chapter
- **Description:** Martian (implied), sparse physical detail provided

## Martians/Green Men
- **Role:** Approximately 900 creatures camped in the city
- **Status:** Referenced throughout chapter
- **Description:** Naked except for ornaments, large tusks, long legs, adult females 10-12 feet tall

## Sola
- **Role:** Young female Martian, belongs to Tars Tarkas' retinue
- **Status:** Physically present in chapter
- **Description:** About 8 feet tall, light olive-green coloration

## Principal Chieftain
- **Role:** Ruler of the community, seated on rostrum during assembly
- **Status:** Referenced throughout chapter
- **Description:** Sparse physical detail provided

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail - human physiology noted but no specific appearance description.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# John Carter

**Chapter Role:** Human protagonist, prisoner attempting to gain favor through physical demonstration

**Physical Presence:** Physically present in chapter

**Physical Description:** Human physiology (sparse detail - no specific appearance description provided)

**Costume/Silhouette:** None specified - human form implied

**Continuity-Critical Traits:** 
- Human physiology is a liability for Martian tasks but becomes an asset when adapting to their expectations
- Attempts walking but fails, skipping like a grasshopper and bruising himself
- Successfully performs the jump ("sak") clearing 150 feet

**Uncertainty Notes:** Physical appearance details are sparse - no specific height, weight, hair color, or facial features described in source material.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH002 Tars Tarkas

aliases: Vice-chieftain, Statesman, Warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail - Martian identity implied but no specific appearance description provided.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation.

clarification_question: What is Tars Tarkas's physical form and origin?

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Vice-chieftain of the community, escort, statesman, warrior

**Physical Presence:** Physically present in chapter

**Physical Description:** Martian (implied from context), sparse physical detail provided

**Costume/Silhouette:** None specified - Martian form implied

**Continuity-Critical Traits:** 
- Explains situation regarding Carter's capture
- Seated on rostrum during assembly
- Arranges for Carter to be taken by Sola after demonstration of "sak"

**Uncertainty Notes:** Physical appearance details are sparse - no specific height, weight, hair color, or facial features described in source material.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: martians_green_men

canonical_character_id: CH003 Martians/Green Men

aliases: Green Men, Naked Creatures, Ornamented Beings

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient physical description provided in source material.

clarification_required: false

clarification_reason: N/A - identity is stable and well-documented.

clarification_question: N/A

[[SECTION markdown]]

# Martians/Green Men

**Chapter Role:** Approximately 900 creatures camped in the city, inhabitants of the ruined civilization

**Physical Presence:** Referenced throughout chapter (approximately 900 individuals)

**Physical Description:** 
- Naked except for ornaments
- Large tusks
- Long legs
- Adult females: 10-12 feet tall
- Average life expectancy: 300 years after maturity, up to 1000 without violence
- Death causes: duels, war, hunting
- Voluntary pilgrimage down river Iss at age 1000

**Costume/Silhouette:** Ornamented (specific ornaments not detailed), naked body form

**Continuity-Critical Traits:** 
- Initially hostile but show approval when Carter demonstrates strength or humor
- Architecture suggests civilization older than current inhabitants
- Demand Carter perform the jump ("sak")
- Camped in city plaza and buildings

**Uncertainty Notes:** Specific height variation for males not detailed; ornament types unspecified.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: Young Female Martian, Tars Tarkas' Retinue Member

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient physical description provided in source material.

clarification_required: false

clarification_reason: N/A - identity is stable and well-documented.

clarification_question: N/A

[[SECTION markdown]]

# Sola

**Chapter Role:** Young female Martian, belongs to Tars Tarkas' retinue

**Physical Presence:** Physically present in chapter

**Physical Description:** 
- About 8 feet tall
- Light olive-green coloration
- Young female

**Costume/Silhouette:** None specified - naked body form implied (consistent with general Martian description)

**Continuity-Critical Traits:** 
- Takes Carter to his quarters after demonstration of "sak"
- Signals for ten-legged creature to appear in chamber
- Leads Carter through spacious chamber decorated with murals and mosaics

**Uncertainty Notes:** Specific ornamentation not detailed; facial features unspecified.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: principal_chieftain

canonical_character_id: CH005 Principal Chieftain

aliases: Ruler, Assembly Leader

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail - ruler identity noted but no specific appearance description provided.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation.

clarification_question: What is the Principal Chieftain's physical form and origin?

[[SECTION markdown]]

# Principal Chieftain

**Chapter Role:** Ruler of the community, seated on rostrum during assembly

**Physical Presence:** Referenced throughout chapter (seated on rostrum)

**Physical Description:** Sparse physical detail provided - ruler identity noted but no specific appearance description

**Costume/Silhouette:** None specified - Martian form implied

**Continuity-Critical Traits:** 
- Seated on rostrum during assembly
- Greeting ceremony occurs where names are exchanged between Tars Tarkas and the chieftain
- Carter is lowered to ground and brought before the chieftain

**Uncertainty Notes:** Physical appearance details are sparse - no specific height, weight, hair color, or facial features described in source material.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: ten_legged_creature

canonical_character_id: CH006 Ten-Legged Creature

aliases: Obedient Puppy, Chamber Attendant

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail - creature type noted but no specific appearance description provided.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation.

clarification_question: What is the ten-legged creature's physical form and origin?

[[SECTION markdown]]

# Ten-Legged Creature

**Chapter Role:** Chamber attendant, signals for by Sola

**Physical Presence:** Physically present in chapter (waddles in like obedient puppy)

**Physical Description:** Sparse physical detail - creature type noted but no specific appearance description provided

**Costume/Silhouette:** None specified - ten-legged form implied

**Continuity-Critical Traits:** 
- Waddles in like an obedient puppy
- Appears in chamber decorated with murals and mosaics
- Signals for by Sola to appear

**Uncertainty Notes:** Physical appearance details are sparse - no specific height, weight, hair color, or facial features described in source material.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_guard

canonical_character_id: CH007 Martian Guard

aliases: Guard, Enforcer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail - guard role noted but no specific appearance description provided.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation.

clarification_question: What is the Martian guard's physical form and origin?

[[SECTION markdown]]

# Martian Guard

**Chapter Role:** Enforcer, forces Carter to stand

**Physical Presence:** Physically present in chapter (forces Carter to fight)

**Physical Description:** Sparse physical detail - guard role noted but no specific appearance description provided

**Costume/Silhouette:** None specified - naked body form implied (consistent with general Martian description)

**Continuity-Critical Traits:** 
- Forces Carter to stand after being lowered to ground
- Carter fights this guard after being forced to stand, winning applause for ability to fight back

**Uncertainty Notes:** Physical appearance details are sparse - no specific height, weight, hair color, or facial features described in source material.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_PACKET]]
````
