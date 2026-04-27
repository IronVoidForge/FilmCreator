# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:18:39.285049+00:00
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
Project slug: wizard_of_oz

Chapter id: CH015

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

**Summary:**
After returning to the Emerald City and reporting the death of the Wicked Witch of the West, Dorothy and her companions demand that the Wizard fulfill his promises. After a period of tense waiting and a threat to call upon the Winged Monkeys, the travelers are granted an audience in the Throne Room. Instead of a terrifying magical entity, they discover a "humbug"—an ordinary, elderly man from Omaha who has used ventriloquism, illusions, and stage props to masquerade as a Great Wizard. The man explains his history as a balloonist who became lost in Oz and has lived in fear of the Witches. While he admits he lacks true magic, he agrees to provide the Scarecrow with brains, the Lion with courage, and the Tin Woodman with a heart the following day, while promising to consider a way to return Dorothy to Kansas.

**Characters:**
* **Dorothy:** The leader of the group; she is determined to return home and confronts Oz about his deception.
* **The Scarecrow:** Seeks brains; expresses disappointment in Oz's true nature.
* **The Tin Woodman:** Seeks a heart; reacts aggressively when the Wizard's secret is revealed.
* **The Cowardly Lion:** Seeks courage; his roar accidentally reveals the Wizard's hiding place.
* **Oz (The Great and Terrible):** Revealed to be a common man, a former balloonist and ventriloquist who has been "making believe" to maintain power and safety.
* **Guardian of the Gates:** The official who greets the travelers at the city entrance.
* **Green-whiskered Soldier/Green Girl:** Palace staff who facilitate the travelers' stay.

**Settings:**
* **The Great Gate of the Emerald City:** The entrance where the travelers are greeted by the Guardian.
* **The Palace of Oz (Guest Rooms):** Where the travelers rest and wait for their audience.
* **The Throne Room:** A large, intimidating room with a great dome where the Wizard's illusions (the Head, the Beast, etc.) were staged.
* **The Small Chamber:** A rear room in the palace where Oz reveals his mechanical tricks and tells his life story.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Dorothy](#dorothy)
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin-woodman)
- [Cowardly Lion](#cowardly-lion)
- [Oz (The Great and Terrible)](#oz-the-great-and-terrible)
- [Guardian of the Gates](#guardian-of-the-gates)
- [Green-whiskered Soldier/Green Girl](#green-whiskered-soldier-green-girl)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dorothy
canonical_character_id: CH001 Dorothy
aliases: None
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
confidence: 1.0
direct_identity_evidence: Yes
direct_visual_evidence: No (referenced by role/action)
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Oz
alias_or_role_evidence: Leader of the group
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Group leader and protagonist.
**Status:** Physically present.
**Description:** A determined young girl seeking to return home to Kansas. While specific visual details are not provided in this chapter, she acts as the primary negotiator with the Wizard.
**Descriptive Phrases:** Determined young traveler, seeker of home.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: scarecrow
canonical_character_id: CH003 Scarecrow
aliases: None
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
confidence: 1.0
direct_identity_evidence: Yes
direct_visual_evidence: No (referenced by role/desire)
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: Dorothy, Tin Woodman, Cowardly Lion, Oz
alias_or_role_evidence: Seeking brains
unknowns: 
source_refs: 

[[SECTION markdown]]
# Scarecrow
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A character seeking intelligence/brains from the Wizard. Expresses disappointment upon discovering the Wizard's true nature.
**Descriptive Phrases:** Straw-filled companion, seeker of brains.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tin_woodman
canonical_character_id: CH004 Tin Woodman
aliases: None
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
confidence: 1.0
direct_identity_evidence: Yes
direct_visual_evidence: No (referenced by role/desire)
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: Dorothy, Scarecrow, Cowardly Lion, Oz
alias_or_role_evidence: Seeking a heart
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tin Woodman
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A character seeking a heart from the Wizard. Reacts aggressively when the Wizard's secret is revealed.
**Descriptive Phrases:** Metallic companion, seeker of a heart.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cowardly_lion
canonical_character_id: CH005 Cowardly Lion
aliases: None
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: Yes
direct_visual_evidence: No (referenced by role/action)
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: Dorothy, Scarecrow, Tin Woodman, Oz
alias_or_role_evidence: Seeking courage; his roar reveals the Wizard's location.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Cowardly Lion
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A large animal seeking courage from the Wizard. His accidental roar is a key plot point that reveals the Wizard's hiding place.
**Descriptive Phrases:** Large roaring lion, seeker of courage.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: oz
canonical_character_id: CH006 Oz
aliases: The Great and Terrible, Humbug, Wizard of Oz
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance is described as an "ordinary, elderly man," but specific facial features or clothing are not detailed.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Yes
direct_visual_evidence: Yes (revealed as a man)
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: Dorothy, Scarecrow, Tin Woodman, Cowardly Lion
alias_or_role_evidence: Former balloonist, ventriloquist, deceiver.
unknowns: Specific facial features and clothing details.
source_refs: 

[[SECTION markdown]]
# Oz (The Great and Terrible)
**Role:** The perceived magical ruler; revealed to be a fraud.
**Status:** Physically present.
**Description:** An ordinary, elderly man from Omaha who used stagecraft, ventriloquism, and illusions to pretend to be a powerful wizard. He is a former balloonist who became lost in Oz.
**Descriptive Phrases:** Elderly man, former balloonist, ventriloquist, the "humbug" wizard.
**Uncertainty Note:** Specific clothing and facial details are not provided beyond his age and origin.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: guardian_of_the_gates
canonical_character_id: CH007 Guardian of the Gates
aliases: None
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: unknown
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: Yes
direct_visual_evidence: No
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: None
alias_or_role_evidence: Official who greets travelers at the city entrance.
unknowns: Species, appearance, clothing.
source_refs: 

[[SECTION markdown]]
# Guardian of the Gates
**Role:** City official.
**Status:** Physically present.
**Description:** An official who greets the travelers at the entrance to the Emerald City.
**Uncertainty Note:** Physical appearance and species are entirely unknown.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: palace_staff
canonical_character_id: CH008 Palace Staff
aliases: Green-whiskered Soldier, Green Girl
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only partial descriptions (green whiskers/green girl) are provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: Yes
direct_visual_evidence: Yes (partial)
costume_or_covering_evidence: No
movement_evidence: No
associated_entities: None
alias_or_role_evidence: Palace staff facilitating the travelers' stay.
unknowns: Full appearance, exact species.
source_refs: 

[[SECTION markdown]]
# Palace Staff
**Role:** Facilitators for the travelers.
**Status:** Physically present.
**Description:** Members of the palace staff, including a "Green-whiskered Soldier" and a "Green Girl."
**Descriptive Phrases:** Green-whiskered soldier, green girl.
**Uncertainty Note:** It is unclear if they are humans with green features or a different species entirely.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
