# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:38:10.740259+00:00
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

Chapter id: CH024

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

# Chapter Summary: CH024 - Tars Tarkas Finds a Friend

## Scene 1: Crash and First Contact
- **Action:** John Carter's craft crashes into the center of a Thark-Warhoon battle.
- **Interaction:** He meets Tars Tarkas, who is fighting three Warhoons. They fight together; Tars Tarkas acknowledges John Carter's act of friendship.
- **Visual Detail:** Woola (the dog) rushes to them after finding his way back from John Carter's former quarters.
- **Outcome:** The battle ends with the Warhoon horde fleeing.

## Scene 2: Confrontation at Tal Hajus' Palace
- **Action:** Tars Tarkas warns of Tal Hajus's desire for revenge. They proceed to the Jeddak's palace.
- **Conflict:** Tal Hajus demands torture; John Carter defends Tars Tarkas before the Council, accusing Tal Hajus of cowardice and lack of bravery in battle.
- **Resolution:** The Council votes to challenge Tal Hajus. Tars Tarkas defeats him in combat and becomes Jeddak of Thark.

## Scene 3: Political Reorganization and New Mission
- **Action:** Tars Tarkas makes John Carter a full-fledged Chieftain.
- **Proposal:** Tars Tarkas suggests rescuing Dejah Thoris from Zodanga to unite forces against Zodangan aggression.
- **Decision:** The Council agrees enthusiastically. Messengers are sent to gather hordes.

## Scene 4: March on Zodanga
- **Action:** A force of 150,000 warriors marches toward Zodanga over ten days.
- **Logistics:** They travel by night and camp in deserted cities during the day.
- **Visual Detail:** John Carter rides beside Tars Tarkas; Woola trots at the heels of his mount.

## Scene 5: Entry into Zodanga
- **Action:** The horde halts outside Zodanga's walls (75 feet high, carborundum blocks).
- **Infiltration:** John Carter uses a human tower method with ten warriors to climb the wall and enter via a small gate.
- **Movement:** He enters at the lower boundary of the palace grounds. A detachment moves toward the palace while the main horde attacks barracks.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: CH024 - Tars Tarkas Finds a Friend

## Characters

1. **John Carter**: Protagonist / Chieftain
2. **Tars Tarkas**: Thark Warrior / Jeddak of Thark
3. **Woola**: Dog Companion
4. **Tal Hajus**: Thark Antagonist
5. **Dejah Thoris**: Rescue Target (Princess of Zodanga)

## Notes

This index lists all characters explicitly named or referenced in Chapter CH024. Visual descriptions are sparse in the source text, requiring manual description flags for image generation workflows.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The provided chapter summary describes actions and interactions but lacks specific physical descriptors (e.g., attire, build, facial features) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

## Role
Protagonist / Chieftain

## Presence
Physically present (Scene 1, 4, 5)

## Physical Description
None provided in source text.

## Continuity Traits
Rides beside Tars Tarkas; uses human tower method to climb walls.

## Notes
Visual details such as attire or specific physical features are not described in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The provided chapter summary describes actions and interactions but lacks specific physical descriptors (e.g., attire, build, facial features) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

## Role
Thark Warrior / Jeddak of Thark

## Presence
Physically present (Scene 1, 2, 4, 5)

## Physical Description
None provided in source text.

## Continuity Traits
Fights three Warhoons; defeats Tal Hajus; becomes Jeddak of Thark.

## Notes
Visual details such as attire or specific physical features are not described in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The provided chapter summary describes actions and interactions but lacks specific physical descriptors (e.g., attire, build, facial features) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola

## Role
Dog Companion

## Presence
Physically present (Scene 1, 4)

## Physical Description
None provided in source text.

## Continuity Traits
Rushes to John Carter and Tars Tarkas after finding his way back; trots at the heels of John Carter's mount.

## Notes
Visual details such as breed or specific appearance are not described in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The provided chapter summary describes actions and interactions but lacks specific physical descriptors (e.g., attire, build, facial features) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus

## Role
Thark Antagonist / Former Jeddak

## Presence
Referenced/Combatant (Scene 2)

## Physical Description
None provided in source text.

## Continuity Traits
Desires revenge; demands torture; defeated by Tars Tarkas in combat.

## Notes
Visual details such as attire or specific physical features are not described in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The provided chapter summary describes actions and interactions but lacks specific physical descriptors (e.g., attire, build, facial features) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

## Role
Rescue Target / Princess of Zodanga

## Presence
Referenced (Scene 3)

## Physical Description
None provided in source text.

## Continuity Traits
Target of rescue mission from Zodanga to unite forces against Zodangan aggression.

## Notes
Visual details such as attire or specific physical features are not described in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
