# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:28:13.402616+00:00
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

Chapter id: CH004

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

**Scene 1: Arrival at the City & Audience Chamber**
Carter arrives at the foot of mountains near a ruined city on Mars. He is brought before the Chieftain in a magnificent edifice constructed of gleaming white marble and gold. Visual continuity note: The furniture (desks, chairs) is sized for humans, creating a size mismatch with the Martians who cannot fit comfortably. The chamber features galleries and carved wooden desks.

**Scene 2: Ceremonial Introduction & Cultural Exchange**
Tars Tarkas (Vice-Chieftain) escorts Carter to the Chieftain's rostrum. A formal greeting occurs involving name exchange or ornament/shot exchange depending on familiarity. Carter learns about Martian customs: smiling is perfunctory, laughter is horrific, and humor involves death agonies or inflicting death on prisoners. Visual note: Martians are largely naked with ornaments; women have larger tusks and lighter skin color.

**Scene 3: Physical Demonstrations & Combat**
Carter performs "sak" jumps to demonstrate utility (clearing 150 feet). He is bullied by a warrior who bullies him into fighting; Carter punches the warrior in self-defense against brutality. The Martians applaud his fighting spirit and approach. Visual note: Martians laugh at Carter's misfortunes during initial attempts but cheer his combat success.

**Scene 4: Sola & Sleeping Quarters**
Carter is hungry and thirsty. Tars Tarkas sends Sola (young female, ~8 feet tall, light olive-green) to accompany him. They move to a spacious chamber decorated with mural paintings and mosaics showing signs of antiquity. Visual note: A ten-legged creature waddles in; it is the size of a Shetland pony with a frog-like head and three rows of sharp tusks.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH004
## Carter (Human)
- **Role:** Protagonist, Human visitor from Earth.
- **Status:** Physically present in the scene.
- **Notes:** Actions described include arriving at foot of mountains and jumping 150 feet ("sak"). No specific physical attributes provided in text.

## Chieftain (Martian)
- **Role:** Martian Leader, Head of the City.
- **Status:** Physically present in the Audience Chamber.
- **Notes:** General appearance described as naked with ornaments. Specific physical details for the Chieftain are not provided in the text summary.

## Tars Tarkas (Vice-Chieftain)
- **Role:** Vice-Chieftain, Escort to Carter.
- **Status:** Physically present, escorts Carter.
- **Notes:** Identified by name and title. General appearance described as naked with ornaments. Specific physical details not provided in text summary.

## Sola (Young Female Martian)
- **Role:** Young Female Martian, Companion to Carter.
- **Status:** Physically present, sent by Tars Tarkas.
- **Notes:** Height (~8 feet tall) and skin color (light olive-green) noted. Specific facial features or ornaments not detailed in text summary.

## Warrior (Unnamed Martian)
- **Role:** Martian Combatant, Bully to Carter.
- **Status:** Physically present during combat demonstration.
- **Notes:** Referred to only as "a warrior". No specific physical details provided in text summary. Unnamed character requiring clarification.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter_human
canonical_character_id: carter_human
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The text describes Carter's actions but lacks specific physical attributes such as height, build, or facial features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter
## Role
Protagonist, Human visitor from Earth.
## Presence
Physically present in the scene.
## Physical Description
Actions described: Arrives at foot of mountains, jumps 150 feet ("sak"), punches warrior. No specific height or appearance details provided in the text.
## Continuity Notes
Human size contrasted with Martian environment (furniture sized for humans).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain_martian
canonical_character_id: chieftain_martian
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The text describes general Martian appearance but lacks specific physical details for the Chieftain.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Chieftain
## Role
Martian Leader, Head of the City.
## Presence
Physically present in the Audience Chamber.
## Physical Description
General appearance described as naked with ornaments. Specific physical details for the Chieftain are not provided in the text summary.
## Continuity Notes
Located in a magnificent edifice of white marble and gold.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: Vice-Chieftain
is_fully_identified: true
manual_description_required: true
manual_description_reason: The text identifies Tars Tarkas by name but does not provide specific physical attributes.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas
## Role
Vice-Chieftain, Escort to Carter.
## Presence
Physically present, escorts Carter.
## Physical Description
General appearance described as naked with ornaments. Specific physical details are not provided in the text summary.
## Continuity Notes
Escorts Carter to the Chieftain's rostrum.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: Young Female Martian
is_fully_identified: true
manual_description_required: true
manual_description_reason: While height and skin tone are noted, details on facial features, hair, or specific ornaments are absent.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola
## Role
Young Female Martian, Companion to Carter.
## Presence
Physically present, sent by Tars Tarkas.
## Physical Description
Height: ~8 feet tall. Skin color: Light olive-green. Specific facial features or ornaments not detailed in the text summary.
## Continuity Notes
Accompanies Carter to a spacious chamber with murals and mosaics.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warrior_martian
canonical_character_id: warrior_martian
aliases: Unnamed Warrior
is_fully_identified: false
manual_description_required: true
manual_description_reason: The text refers to the character only as 'a warrior' without a name or physical description.
clarification_required: true
clarification_reason: Character lacks stable identification and specific name.
clarification_question: What is the specific name or identifier for this Martian warrior?

[[SECTION markdown]]
# Warrior
## Role
Martian Combatant, Bully to Carter.
## Presence
Physically present during combat demonstration.
## Physical Description
No specific physical details provided in the text summary. Referred to only as "a warrior".
## Continuity Notes
Bullies Carter into fighting; Carter punches him in self-defense.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
