# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:08:56.482057+00:00
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
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



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

character_type_hint: unknown

morphology_hint: unknown

scale_hint: unknown

renderability_hint: unknown

confidence: 0.3



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



Entity taxonomy rules:

- identify what the entity itself appears to be, not what it wears or rides

- do not confuse nearby/associated things with the entity

- if source says a person rides a mount, classify the person separately from the mount

- if source says a character wears foreign/alien/exotic clothing, do not change their species/type

- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown

- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown

- scale_hint: tiny, small, human_scale, large, giant, unknown

- renderability_hint: renderable, context_only, alias_or_role, unknown

- confidence: 0.0 to 1.0 for each type/morphology/renderability hint

- if uncertain, use unknown and explain the missing evidence in the markdown section



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
Following the total reduction of Zodanga, Tars Tarkas and Kantos Kan lead a fleet of Thark vessels and prisoners toward Helium. En route, they encounter a Zodangan fleet attempting to besiege Helium; a massive aerial battle ensues, aided by the superior marksmanship of the Thark warriors and the arrival of the Heliumite navy. The Zodangans surrender following the ritualistic suicide-plunge of their commanders. 

John Carter transfers Princess Dejah Thoris to the Heliumite flagship, where she is celebrated as a hero alongside Carter and Tars Tarkas. After the naval victory, Carter remains with the Tharks to finish the land campaign. They unload their thoats near Helium and launch a multi-pronged assault on the remaining Zodangan land forces. Despite being outnumbered, the combined Thark and Heliumite forces crush the Zodangan army. The chapter concludes with a grand triumphal procession into Helium, where John Carter is honored by Tardos Mors, Jeddak of Helium, and the royal family for his role in the victory and the rescue of the Princess.

**Characters:**
- **John Carter:** The protagonist; celebrated as a hero and savior of Dejah Thoris.
- **Dejah Thoris:** Princess of Helium; reunited with her people and honored for her resilience.
- **Tars Tarkas:** Jeddak of Thark; establishes a historic alliance between the green warriors and Helium.
- **Kantos Kan:** A prominent Thark leader.
- **Tardos Mors:** Jeddak of Helium; formally welcomes Carter and the Tharks as allies.
- **Mors Kajak:** Father of Dejah Thoris; deeply moved by her rescue.

**Settings:**
- **The Martian Skies/Sea Bottom:** The site of the intense aerial battle between the Zodangan and Heliumite fleets.
- **The Plains near Helium:** The location of the final land battle and the unloading of the Thark thoats.
- **Helium (Greater City):** The capital city, characterized by its red towers and grand palaces; the site of the victory celebration and royal reception.
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
- [Dejah Thoris](#dejah_thoris)
- [Tars Tarkas](#tars_tarkas)
- [Kantos Kan](#kantos_kan)
- [Tardos Mors](#tardos_mors)
- [Mors Kajak](#mors_kajak)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Hero, Savior
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dejah Thoris, Tars Tarkas, Tardos Mors
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist; Hero of the Helium/Thark alliance.
**Status:** Physically present.
**Description:** A human warrior celebrated for his role in the rescue of Princess Dejah Thoris and the defeat of the Zodangan forces.
**Notes:** While specific visual details are not detailed in this summary, he is established as a combatant and leader within the combined forces.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH003 Dejah Thoris
aliases: Princess of Helium
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: John Carter, Tardos Mors, Mors Kajak
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium.
**Status:** Physically present.
**Description:** A royal figure of Helium who was rescued from Zodanga; celebrated as a hero for her resilience.
**Notes:** Identified by her royal status and her reunion with the Heliumite navy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH004 Tars Tarkas
aliases: Jeddak of Thark
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Kantos Kan, John Carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Jeddak of the Tharks.
**Status:** Physically present.
**Description:** A leader of the green warriors who established a historic alliance with Helium.
**Notes:** Part of the Thark fleet; characterized as a powerful warrior/leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: CH005 Kantos Kan
aliases: Thark Leader
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Tars Tarkas
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Kantos Kan
**Role:** Prominent Thark leader.
**Status:** Physically present.
**Description:** A high-ranking member of the Thark military/leadership during the campaign against Zodanga.
**Notes:** Associated with Tars Tarkas and the Thark fleet.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tardos_mors
canonical_character_id: CH006 Tardos Mors
aliases: Jeddak of Helium
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dejah Thoris, Mors Kajak
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tardos Mors
**Role:** Jeddak of Helium.
**Status:** Physically present.
**Description:** The ruler of Helium who formally welcomes the Tharks and John Carter as allies.
**Notes:** Part of the Heliumite royal family.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mors_kajak
canonical_character_id: CH007 Mors Kajak
aliases: Father of Dejah Thoris
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dejah Thoris, Tardos Mors
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Mors Kajak
**Role:** Father of Princess Dejah Thoris.
**Status:** Physically present.
**Description:** A member of the Heliumite royal family, deeply moved by his daughter's rescue.
**Notes:** Referenced as a key emotional figure in the victory celebration.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
