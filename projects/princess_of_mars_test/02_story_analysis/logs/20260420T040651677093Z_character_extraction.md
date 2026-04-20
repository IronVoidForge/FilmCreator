# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:06:51.677093+00:00
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

Chapter id: CH022

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

# Chapter Summary: I FIND DEJAH (CH022)

## Scene 1: The Announcement in Than Kosis's Apartment
John Carter is stationed in a passage behind tapestries guarding the Jeddak. Dejah Thoris enters with four soldiers, surrounded by courtiers. She stands before Than Kosis and Sab Than, radiant with smiles. She announces her engagement to Sab Than, explaining that on Barsoom women may change their mind regarding heart matters but once a promise is made, it is final. She begs Than Kosis to forget her rash words from two days ago. Than Kosis accepts the assurance and orders a proclamation issued. Dejah leaves with her guards. Carter realizes his dream of happiness is dashed as she has given herself to the son of her people's enemy.

## Scene 2: The Fight in the Antechamber
Carter leaves his post to confront Dejah Thoris. He navigates the maze of winding corridors behind the tapestries and finds her antechamber. Four guardsmen stop him, demanding an order or password. Carter refuses, tapping his long-sword as his order. The guards draw weapons; a fight ensues. Carter kills three guardsmen quickly, then the fourth within ten seconds. Dejah Thoris stands at the door of her apartment watching throughout the conflict with Sola at her back. She does not recognize him initially.

## Scene 3: Confrontation and Refusal
Carter sheathes his bloody blade and approaches Dejah Thoris. He identifies himself as John Carter, her chieftain. She sways toward him but draws back in misery, stating it is too late because she has promised herself to Sab Than. She explains that on Barsoom, a promise given is final; the ceremonies are meaningless formalities. She states she cannot wed the man who slays her husband, even in self-defense, due to custom. Carter asks for forgiveness and declares his love again. Dejah explains the custom of two kinds of women in cities: those fought for to be asked in marriage, and those fought for but never asked. She bids him farewell as "chieftain that was."

## Scene 4: Escape from Zodanga
Carter realizes he is lost and must escape the city due to suspicion regarding the dead guardsmen. He follows a spiral runway to a lower floor and hides inside a huge hanging ornament in a hall. He overhears guards discussing the dead men and Than Kosis's search. Darkness falls outside. Carter slips from his hiding place onto a balcony overlooking an avenue. He jumps through a glass wall to the ground below, escaping the palace grounds as the court searches for him.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter CH022 Character Index

| Name | Role | Presence | Description Status |
|------|------|----------|-------------------|
| John Carter | Chieftain / Protagonist | Present | Missing Physical Details |
| Dejah Thoris | Princess / Fiancée | Present | Missing Physical Details |
| Than Kosis | Courtier | Referenced/Present | Missing Physical Details |
| Sab Than | Noble / Fiancé | Referenced | Missing Physical Details |
| Sola | Guard / Companion | Present | Missing Physical Details |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (hair, eyes, build) provided in the chapter text to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

## Chapter Role
Protagonist / Chieftain of Tharks.

## Physical Presence
Referenced and Present (Stationed in passage, leaves post to confront Dejah Thoris).

## Physical Description
No specific physical description provided in the chapter text.

## Costume & Silhouette
Wears attire consistent with a chieftain; carries a long-sword.

## Continuity Traits
Identifies himself as John Carter to Dejah Thoris.

## Uncertainty Notes
Physical appearance details (hair, eyes, build) are missing from the source text and require manual description for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (hair, eyes, build) provided in the chapter text to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

## Chapter Role
Princess of Zodanga / Sab Than's fiancée.

## Physical Presence
Present (Enters apartment, stands before courtiers, watches fight).

## Physical Description
No specific physical description provided in the chapter text.

## Costume & Silhouette
Radiant with smiles; stands before Than Kosis and Sab Than.

## Continuity Traits
Announces engagement to Sab Than; refuses John Carter due to custom.

## Uncertainty Notes
Physical appearance details (hair, eyes, build) are missing from the source text and require manual description for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: than_kosis
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (hair, eyes, build) provided in the chapter text to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Than Kosis

## Chapter Role
Courtier / Sab Than's father (implied by context).

## Physical Presence
Referenced and Present (Dejah stands before him).

## Physical Description
No specific physical description provided in the chapter text.

## Costume & Silhouette
Courtier attire; accepts Dejah's engagement announcement.

## Continuity Traits
Orders proclamation issued; searches for Carter later.

## Uncertainty Notes
Physical appearance details (hair, eyes, build) are missing from the source text and require manual description for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: sab_than
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (hair, eyes, build) provided in the chapter text to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sab Than

## Chapter Role
Son of Zodanga / Dejah Thoris's fiancée.

## Physical Presence
Referenced (Dejah announces engagement to him).

## Physical Description
No specific physical description provided in the chapter text.

## Costume & Silhouette
Attire consistent with a noble/chieftain son.

## Continuity Traits
Son of her people's enemy; Dejah promises herself to him.

## Uncertainty Notes
Physical appearance details (hair, eyes, build) are missing from the source text and require manual description for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (hair, eyes, build) provided in the chapter text to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

## Chapter Role
Dejah Thoris's companion / Guard.

## Physical Presence
Present (Stands at Dejah Thoris's back during conflict).

## Physical Description
No specific physical description provided in the chapter text.

## Costume & Silhouette
Attire consistent with a guard/companion.

## Continuity Traits
Loyal to Dejah Thoris; watches Carter's confrontation.

## Uncertainty Notes
Physical appearance details (hair, eyes, build) are missing from the source text and require manual description for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
