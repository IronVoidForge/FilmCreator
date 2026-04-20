# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:24:08.495261+00:00
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

**Events:**
Following the total reduction of Zodanga, Tars Tarkas and Kantos Kan lead a fleet of 250 Thark battleships and 100,000 green warriors toward Helium. En route, they encounter a Zodangan fleet attempting to besiege Helium; a massive aerial battle ensues where the combination of Heliumite naval skill and Thark small-arms fire results in a decisive victory. The chapter depicts the ritualistic surrender of Zodangan commanders, who leap to their deaths from their vessels. 

Upon reaching Helium, John Carter facilitates the transfer of Princess Dejah Thoris to the Heliumite flagship, where she publicly credits Carter for her rescue and the city's salvation. After Dejah Thoris is safely returned to her palace, Carter and Tars Tarkas lead a land assault against the remaining Zodangan ground forces. Despite being outnumbered by nearly ten to one, the Thark warriors—supported by arriving Heliumite reinforcements—crush the Zodangan camp. The chapter concludes with a grand triumphal procession into Helium, where John Carter and Tars Tarkas are honored by Jeddak Tardos Mors for forging an unprecedented alliance between the red and green races.

**Characters:**
* **John Carter:** Hero of the campaign; credited with the liberation of Dejah Thoris and the defense of Helium.
* **Tars Tarkas:** Jeddak of Thark; a legendary warrior who establishes a formal friendship with the Heliumites.
* **Dejah Thoris:** Princess of Helium; reunited with her people and honored for her resilience.
* **Tardos Mors:** Jeddak of Helium; receives the allies with profound gratitude and formalizes the alliance.
* **Mors Kajak:** Father of Dejah Thoris; a fierce warrior overcome with emotion at his daughter's return.
* **Kantos Kan:** Thark leader/warrior assisting in the campaign.

**Settings:**
* **The Martian Skies/Sea Bottom:** The site of the massive aerial naval engagement between Helium and Zodanga fleets.
* **The Plains near Helium:** The location of the final land battle and the unloading of Thark thoats.
* **Helium (Greater City):** The red-skinned capital, characterized by its magnificent architecture and celebratory atmosphere during the triumphal entry.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH026

- [John Carter](#john_carter)
- [Tars Tarkas](#tars_tarkas)
- [Dejah Thoris](#dejah_thoris)
- [Tardos Mors](#tardos_mors)
- [Mors Kajak](#mors_kajak)
- [Kantos Kan](#kantos_kan)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Hero of the campaign
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description (height, hair, eyes, clothing) provided in this chapter text.
clarification_required: true
clarification_reason: Physical appearance is not detailed in the summary.
clarification_question: What are John Carter's specific physical traits and current attire?
[[SECTION markdown]]
# John Carter
**Role:** Hero of the campaign; liberator of Dejah Thoris and defender of Helium.
**Presence:** Physically present.
**Physical Description:** Not described in this chapter.
**Costume/Silhouette:** Not described in this chapter.
**Notes:** Highly influential figure in the alliance between Red and Green races.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Jeddak of Thark
is_fully_identified: false
manual_description_required: true
manual_description_reason: While identified as a Thark, specific physical details (size, skin texture, facial features) are absent from this text.
clarification_required: true
clarification_reason: Needs visual confirmation of Thark physiology for rendering.
clarification_question: What is the specific visual appearance and scale of Tars Tarkas?
[[SECTION markdown]]
# Tars Tarkas
**Role:** Jeddak of Thark; legendary warrior and ally to Helium.
**Presence:** Physically present.
**Physical Description:** Identified as a Thark (Green race). Specific details missing.
**Costume/Silhouette:** Not described in this chapter.
**Notes:** Leading the Thark fleet and land assault.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess of Helium
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: true
clarification_reason: Needs visual details for character model.
clarification_question: What is Dejah Thoris's appearance and what was she wearing during her rescue?
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium.
**Presence:** Physically present.
**Physical Description:** Identified as a Heliumite (Red race). Specific details missing.
**Costume/Silhouette:** Not described in this chapter.
**Notes:** Recently rescued from Zodanga; credited Carter with her salvation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tardos_mors
canonical_character_id: Tardos Mors
aliases: Jeddak of Helium
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: true
clarification_reason: Needs visual details for character model.
clarification_question: What is the physical appearance and age of Tardos Mors?
[[SECTION markdown]]
# Tardos Mors
**Role:** Jeddak of Helium.
**Presence:** Physically present.
**Physical Description:** Identified as a Heliumite (Red race). Specific details missing.
**Costume/Silhouette:** Not described in this chapter.
**Notes:** Formalizes the alliance between Red and Green races.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mors_kajak
canonical_character_id: Mors Kajak
aliases: Father of Dejah Thoris
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: true
clarification_reason: Needs visual details for character model.
clarification_question: What is the physical appearance of Mors Kajak?
[[SECTION markdown]]
# Mors Kajak
**Role:** Father of Dejah Thoris; fierce warrior.
**Presence:** Physically present.
**Physical Description:** Identified as a Heliumite (Red race). Specific details missing.
**Costume/Silhouette:** Not described in this chapter.
**Notes:** Emotionally affected by his daughter's return.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: Thark leader
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: true
clarification_reason: Needs visual details for character model.
clarification_question: What is the physical appearance of Kantos Kan?
[[SECTION markdown]]
# Kantos Kan
**Role:** Thark leader/warrior.
**Presence:** Physically present.
**Physical Description:** Identified as a Thark (Green race). Specific details missing.
**Costume/Silhouette:** Not described in this chapter.
**Notes:** Part of the fleet leading the assault on Zodanga.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
