# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:31:14.338861+00:00
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

Chapter id: CH020

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

# Chapter Summary: Atmosphere Factory & Escape to Zodanga

## Visual Continuity Facts
*   **Carter's Appearance:** Initially described as a Red Man, he is later shown anointed with reddish oil and having his hair cut to match the prevailing fashion of Red Martians. His metal and ornaments are renewed in the style of a Zodangan gentleman.
*   **Woola's State:** Woola is depicted eating the carcass of the beast that attacked Carter, appearing half-starved and a shadow of his former self.
*   **Atmosphere Factory:** A massive building with walls 150 feet thick, featuring radium pumps and telepathic door locks. The old man wears a gold collar with a diamond-studded ornament containing a strange stone that scintillates nine rays.
*   **Transport:** Carter is given a domestic bull-thoat (size of a horse, gentle) for saddle purposes.

## Story Summary
Carter meets Woola at the Atmosphere Factory after escaping the Warhoons and surviving attacks by wild beasts. The old man explains the factory's function (producing atmosphere via the ninth ray stored in reservoirs) and warns Carter against Helium due to ongoing war. Carter realizes the old man intends to kill him but uses telepathic thought waves to unlock the massive doors and escape with Woola. They reach Zodanga outskirts, where Red Martians take them in. Carter is prepared (colored, hair cut) and given money and a bull-thoat, advised to seek military service in Zodanga to prove trustworthiness and win friends among the nobles. The old man's suspicion of Carter remains, but Carter avoids killing him due to his concern for Dejah Thoris and the planet's atmosphere.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: Atmosphere Factory & Escape to Zodanga (CH020)

## Characters Identified in Chapter

| Character | Role | Physical Description Status |
|-----------|------|-----------------------------|
| Carter | Protagonist, escaped from Warhoons | Manual description required - sparse details |
| Woola | Companion, half-starved beast-eater | Manual description required - minimal physical traits |
| The Old Man | Atmosphere Factory worker, suspicious of Carter | Manual description required - limited visual information |

## Notes on Character Identification

- All three characters are fully identified by name in the chapter text
- Physical descriptions are insufficient for dependable image generation
- No alternate names or partial labels observed in this chapter
- Characters may require additional clarification for render-facing prompts

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is sparse - only mentions Red Man appearance, reddish oil anointment, hair cut to match fashion, metal/ornaments renewed in Zodangan style. Insufficient detail for dependable image generation without additional clarification.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter.md

## Display Name: Carter

### Chapter Role: Protagonist - Escaped from Warhoons, Taken to Zodanga

### Physical Presence Status: Physically Present and Referenced

### Supported Physical Description:
- Initially described as a Red Man
- Later shown anointed with reddish oil
- Hair cut to match Red Martian fashion
- Metal and ornaments renewed in style of Zodangan gentleman
- Given money upon arrival at Zodanga outskirts

### Costume, Silhouette, Continuity-Critical Traits:
- Red skin tone (Martian appearance)
- Wears metal/ornaments in Zodangan gentleman style
- Hair styled to match prevailing Martian fashion
- Carries bull-thoat for saddle purposes after preparation

### Render-Facing Noun Phrases:
- Red-skinned Martian man
- Zodangan gentleman attire with metal ornaments
- Anointed reddish oil on skin
- Bull-thoat companion animal

### Uncertainty Notes:
- Facial features not described in detail
- Specific ornament designs unknown
- Exact clothing items beyond "metal and ornaments" not specified
- Height, build, and other physical dimensions not mentioned

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is minimal - only mentions half-starved state and shadow of former self after eating beast carcass. Insufficient detail for dependable image generation without additional clarification.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# woola.md

## Display Name: Woola

### Chapter Role: Companion - Carter's Half-Starved Beast-Eater

### Physical Presence Status: Physically Present and Referenced

### Supported Physical Description:
- Depicted eating the carcass of the beast that attacked Carter
- Appears half-starved and a shadow of his former self
- Companion to Carter throughout escape from Warhoons

### Costume, Silhouette, Continuity-Critical Traits:
- Unknown physical appearance beyond companion status
- No specific costume or ornamentation described
- Continuity-critical trait: loyal companion despite starvation state

### Render-Facing Noun Phrases:
- Starved Martian companion
- Beast-eater after attack survival
- Shadow of former self (implies previous fuller state)

### Uncertainty Notes:
- Physical appearance completely unknown beyond "companion" status
- No facial features, body type, or distinguishing marks described
- Costume and accessories not mentioned at all
- Relationship to Carter's physical description unclear

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_old_man
canonical_character_id: the_old_man
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is limited - only mentions gold collar with diamond-studded ornament containing strange stone that scintillates nine rays. Insufficient detail for dependable image generation without additional clarification.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# the_old_man.md

## Display Name: The Old Man

### Chapter Role: Atmosphere Factory Worker - Suspicious of Carter

### Physical Presence Status: Physically Present and Referenced

### Supported Physical Description:
- Wears a gold collar with diamond-studded ornament
- Ornament contains strange stone that scintillates nine rays
- Works at the Atmosphere Factory
- Shows suspicion toward Carter

### Costume, Silhouette, Continuity-Critical Traits:
- Gold collar with diamond-studded ornament (continuity-critical)
- Strange scintillating stone in ornament (nine rays)
- No other costume details described
- Silhouette not specified beyond "old man" designation

### Render-Facing Noun Phrases:
- Old Martian factory worker
- Gold collar with diamond-studded ornament
- Scintillating nine-ray stone artifact
- Suspicious demeanor toward Carter

### Uncertainty Notes:
- Facial features and expression not described in detail
- Body type, height, and build unknown
- Additional clothing items beyond collar not mentioned
- Hair color/style not specified
- Overall physical appearance beyond "old man" designation unclear

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
