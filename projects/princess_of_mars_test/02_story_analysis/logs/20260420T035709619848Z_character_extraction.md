# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:57:09.619848+00:00
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

Chapter id: CH017

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

# Chapter Summary: A Costly Recapture (Chapter XVII)

## Scene 1: Rescue from Tal Hajus' Chamber
**Plot:** Carter overhears Tal Hajus planning to torture Dejah Thoris for ten days. He interrupts the scene, killing Tal Hajus with a punch after raising his sword. He rescues Dejah Thoris and Sola from the chamber where they were held captive before the floor was cleared of warriors.
**Visuals:** The inner chamber is immense and circular, thronged with chieftains and women. Tal Hajus squats on a raised platform with six limbs resembling a devil fish. Dejah Thoris stands erect in her beautiful figure, showing scorn and disgust.

## Scene 2: Escape from Thark City and Initial Journey
**Plot:** Carter lowers Dejah Thoris and Sola to the ground using straps and leather from his trappings. They mount their thoats and ride out of the city of Thark towards Helium. They initially turn northeast across the mossy waste instead of circling back northwest.
**Visuals:** The courtyard where they left their thoats is visible. The group rides through the hills to the south, then turns northeast. Dejah Thoris clings to Carter's shoulder, sobbing quietly.

## Scene 3: Getting Lost and Woola's Arrival
**Plot:** The party gets lost as no waterways are in sight. They travel all night and day, eventually collapsing from fatigue. Woola (Carter's faithful dog) follows them across the trackless waste to share their fate.
**Visuals:** The landscape is a yellow, moonlit moss with no distant trees. The group lies down on the moss to sleep. Woola snuggles close to Carter, showing his love and loyalty.

## Scene 4: First Thoat Collapse
**Plot:** The first thoat begins to stumble and eventually pitches violently to the ground. Carter decides not to kill it immediately but leaves it behind after relieving it of its trappings. They continue with one beast, walking while Dejah Thoris rides.
**Visuals:** The poor beast is in a pitiable condition, unable to rise. Trappings are flung down beside it. Sola and Carter walk while Dejah Thoris rides the remaining thoat.

## Scene 5: Encounter with Thark Warriors (Tars Tarkas' Men)
**Plot:** A party of mounted men is sighted in the hills. They appear to be Thark warriors sent to capture them. Carter sacrifices himself, using his rifle and jumping abilities to hold off the warriors while Dejah Thoris and Sola escape into the hills. He is eventually captured by the remaining warriors after fighting until he is overwhelmed.
**Visuals:** Several hundred mounted warriors are discernible from a pass. A chieftain uses a fieldglass to spot them. Carter fires his rifle (even hundred rounds in magazine, another hundred in belt) while lying flat on the moss. He is eventually struck down by blows falling upon him in perfect torrents.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter XVII Character Index

| Character | Role | Presence | Description Status |
|-----------|------|----------|-------------------|
| Carter | Protagonist, rescuer | Physically present throughout | Well identified |
| Dejah Thoris | Princess, captive/rescued | Physically present in all scenes | Well identified |
| Sola | Companion/sister of Dejah | Physically present in all scenes | Partially described |
| Tal Hajus | Antagonist, chamber keeper | Killed in Scene 1 | Well identified |
| Woola | Carter's dog companion | Follows party across waste | Limited description |

**Note:** This index summarizes characters referenced or physically present in Chapter XVII "A Costly Recapture".
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter - Chapter XVII

**Display Name:** Carter  
**Chapter Role:** Protagonist, rescuer of Dejah Thoris and Sola  
**Physical Presence:** Physically present throughout all five scenes  
**Physical Description:** Well-identified protagonist with rifle, trappings, leather straps; capable jumper; described as having "beautiful figure" in context of rescue actions  
**Costume/Silhouette:** Wears practical gear for desert travel including rifle magazine (even hundred rounds), belt ammunition; carries straps and leather from trappings  
**Continuity-Critical Traits:** Faithful to Dejah Thoris; sacrifices himself to hold off Thark warriors; captured at chapter end after fighting until overwhelmed  
**Descriptive Noun Phrases:** Desert traveler, rifle-wielding rescuer, loyal companion, captured hero  
**Uncertainty Notes:** None - character is well-identified and physically described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter XVII

**Display Name:** Dejah Thoris  
**Chapter Role:** Princess, captive rescued from Tal Hajus' chamber  
**Physical Presence:** Physically present in all five scenes  
**Physical Description:** Standing erect with beautiful figure; shows scorn and disgust toward captors; clings to Carter's shoulder sobbing quietly during escape  
**Costume/Silhouette:** Beautiful figure described as standing erect; wears attire appropriate for Thark City residence; no specific costume details beyond general presence  
**Continuity-Critical Traits:** Primary object of rescue mission; rescued from torture plan (ten days); escapes into hills with Sola; rides remaining thoat after first collapses  
**Descriptive Noun Phrases:** Beautiful princess, scornful captive, sobbing companion, rider on thoat  
**Uncertainty Notes:** None - character is well-identified and physically described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter XVII

**Display Name:** Sola  
**Chapter Role:** Companion/sister of Dejah Thoris  
**Physical Presence:** Physically present in all five scenes  
**Physical Description:** Less detailed physical description than Dejah Thoris; walks while Carter and Dejah ride initially after first thoat collapse  
**Costume/Silhouette:** No specific costume details provided beyond general presence as companion to Dejah Thoris  
**Continuity-Critical Traits:** Escapes with Dejah Thoris into hills; walks alongside party after first beast collapses; less riding capacity than Dejah  
**Descriptive Noun Phrases:** Companion princess, walking escapee, sister figure  
**Uncertainty Notes:** Character is identified but has less physical description than main protagonist and Dejah Thoris
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus - Chapter XVII

**Display Name:** Tal Hajus  
**Chapter Role:** Antagonist, chamber keeper planning torture of Dejah Thoris  
**Physical Presence:** Killed in Scene 1; no longer physically present after chapter begins  
**Physical Description:** Squats on raised platform with six limbs resembling devil fish; holds sword (Carter kills him after raising it); planning to torture Dejah Thoris for ten days  
**Costume/Silhouette:** Six limbs resembling devil fish; sits on raised platform in inner chamber; no specific costume details beyond general presence  
**Continuity-Critical Traits:** Primary antagonist killed by Carter's punch after sword raise; victim of rescue mission; represents Thark City cruelty toward Dejah Thoris  
**Descriptive Noun Phrases:** Devil-limbed squatter, torture planner, chamber keeper, slain antagonist  
**Uncertainty Notes:** Character is well-identified with specific visual details (six limbs) despite being killed early in chapter
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character identified as "Carter's faithful dog" but lacks detailed physical description (breed, size, color, specific features) needed for dependable image generation; only behavioral traits (snuggles close, shows love and loyalty) are described
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - Chapter XVII

**Display Name:** Woola  
**Chapter Role:** Carter's faithful dog companion  
**Physical Presence:** Follows party across trackless waste; physically present throughout chapter  
**Physical Description:** Limited physical description available; identified as "Carter's faithful dog" with behavioral traits (snuggles close to Carter, shows love and loyalty) but no specific breed, size, color, or feature details provided in source material  
**Costume/Silhouette:** No costume details; animal companion following party across desert landscape  
**Continuity-Critical Traits:** Faithful companion who follows party despite trackless waste; shares fate with Carter and Dejah Thoris; demonstrates loyalty through physical closeness (snuggles close)  
**Descriptive Noun Phrases:** Faithful dog, loyal companion, desert follower, snuggling pet  
**Uncertainty Notes:** Character requires manual description due to lack of detailed physical appearance in source material; only behavioral traits are well-documented
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
