# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:14:03.729785+00:00
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

Chapter id: CH013

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

**Setting:** The Yellow Castle in the Land of the West; a rocky plain; a tall tree with a smooth trunk.

**Characters:** Dorothy, the Cowardly Lion, the Tin Woodman, the Scarecrow, the Winkies (Yellow People), and the Winged Monkeys (mentioned).

**Events:**
- **Liberation:** Following the death of the Wicked Witch, Dorothy frees the Cowardly Lion from his prison and declares the Winkies free from slavery. The Winkies celebrate their freedom with a feast.
- **Rescuing the Tin Woodman:** Dorothy and the Lion lead a group of Winkies to a rocky plain where they find the battered and rusted Tin Woodman. They carry him back to the Yellow Castle, where Winkie tinsmiths spend three days and nights repairing his body, leaving him with several patches but fully functional.
- **Rescuing the Scarecrow:** The group searches for the Scarecrow and finds his clothes discarded in a tall tree by the Winged Monkeys. Using a newly repaired axe (featuring a gold handle and polished blade), the Tin Woodman chops down the tree. The group retrieves the clothes, stuffs them with fresh straw, and restores the Scarecrow.
- **Departure Preparations:** Reunited and rested, the group decides to return to the Emerald City to claim their rewards from the Wizard. 
- **Farewell Gifts:** As they prepare to leave, the Winkies present the travelers with precious gifts: golden collars for Toto and the Lion, a diamond bracelet for Dorothy, a gold-headed walking stick for the Scarecrow, and a jewel-encrusted silver oil-can for the Tin Woodman.
- **The Golden Cap:** While gathering food, Dorothy discovers the Golden Cap in the Witch's cupboard. Finding it pretty, she decides to wear it as she travels. The group sets off toward the Emerald City.
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
- [Cowardly Lion](#cowardly-lion)
- [Tin Woodman](#tin-woodman)
- [Scarecrow](#scarecrow)
- [Winkies](#winkies)
- [Winged Monkeys](#winged-monkeys)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

aliases: 

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

direct_identity_evidence: Dorothy is named as the protagonist leading the group.

direct_visual_evidence: Receives a diamond bracelet; wears the Golden Cap.

costume_or_covering_evidence: Wears the Golden Cap (discovered in Witch's cupboard).

movement_evidence: Leads the Lion and Winkies; travels toward Emerald City.

associated_entities: Cowardly Lion, Tin Woodman, Scarecrow, Toto, Winkies

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Leader of the group.
**Status:** Physically present.

### Description
A young human girl traveling with her companions. In this chapter, she is noted for wearing a "pretty" Golden Cap discovered in the Wicked Witch's cupboard. She receives a diamond bracelet as a gift from the Winkies.

### Visual Cues
- **Costume/Accessories:** The Golden Cap; a diamond bracelet.
- **Noun Phrases:** Young girl, traveler, wearer of the golden cap.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: cowardly_lion

canonical_character_id: CH003 Cowardly Lion

aliases: Lion

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

direct_identity_evidence: Explicitly named as the Cowardly Lion.

direct_visual_evidence: Freed from prison; receives a golden collar.

costume_or_covering_evidence: Wears a golden collar.

movement_evidence: Walks with Dorothy and the Winkies.

associated_entities: Dorothy, Winkies, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Companion / Former prisoner.
**Status:** Physically present.

### Description
A large animal (lion) who was previously held in prison by the Wicked Witch. He is liberated by Dorothy and joins the journey to the Emerald City.

### Visual Cues
- **Costume/Accessories:** A golden collar gifted by the Winkies.
- **Noun Phrases:** Large lion, golden-collared lion, freed prisoner.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: CH004 Tin Woodman

aliases: 

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

direct_identity_evidence: Explicitly named as the Tin Woodman.

direct_visual_evidence: Battered and rusted; repaired with several patches by tinsmiths.

costume_or_covering_evidence: Metal body; carries a newly repaired axe with a gold handle and polished blade; receives a jewel-encrusted silver oil-can.

movement_evidence: Carried back to the castle; uses an axe to chop down a tree.

associated_entities: Dorothy, Scarecrow, Winkies

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Companion / Warrior.
**Status:** Physically present.

### Description
A humanoid entity made of tin. He was found in a battered and rusted state on a rocky plain but was repaired by Winkie tinsmiths. He now features several visible patches on his body.

### Visual Cues
- **Costume/Accessories:** A polished axe with a gold handle; a jewel-encrusted silver oil-can.
- **Physical Traits:** Patched metal body, rusted surfaces (partially repaired).
- **Noun Phrases:** Patched tin man, metallic humanoid, polished axe-wielder.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH005 Scarecrow

aliases: 

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

direct_identity_evidence: Explicitly named as the Scarecrow.

direct_visual_evidence: Found as discarded clothes in a tree; restored with fresh straw.

costume_or_covering_evidence: Clothes (restored); receives a gold-headed walking stick.

movement_evidence: Restored and joins the group for travel.

associated_entities: Dorothy, Tin Woodman, Winkies

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Companion.
**Status:** Physically present.

### Description
A humanoid entity composed of straw and clothing. After being found discarded in a tree, he was refilled with fresh straw and his clothes were restored.

### Visual Cues
- **Costume/Accessories:** A gold-headed walking stick.
- **Physical Traits:** Straw-stuffed body, cloth clothing.
- **Noun Phrases:** Straw man, stuffed humanoid, walking stick user.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winkies

canonical_character_id: CH006 Winkies

aliases: Yellow People

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

confidence: 0.9

direct_identity_evidence: Named as the Winkies (Yellow People).

direct_visual_evidence: Perform repairs on the Tin Woodman; host a feast; present gifts to travelers.

costume_or_covering_evidence: Not explicitly described, but associated with "Yellow" identity.

movement_evidence: Celebrate freedom; carry the Tin Woodman; gather food.

associated_entities: Dorothy, Tin Woodman, Scarecrow, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Winkies
**Role:** Subjects / Allies.
**Status:** Physically present.

### Description
A group of people (referred to as the Yellow People) who were previously enslaved by the Wicked Witch but are now free. They are skilled craftsmen, specifically tinsmiths.

### Visual Cues
- **Color/Theme:** Associated with the color yellow.
- **Noun Phrases:** Yellow people, Winkie craftsmen, liberated subjects.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winged_monkeys

canonical_character_id: CH007 Winged Monkeys

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description of their appearance or morphology provided, only that they are "Winged Monkeys."

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: creature

morphology_hint: winged

scale_hint: unknown

renderability_hint: renderable

confidence: 0.5

direct_identity_evidence: Named as Winged Monkeys.

direct_visual_evidence: Left Scarecrow's clothes in a tree.

costume_or_covering_evidence: 

movement_evidence: Implied flight/presence in trees.

associated_entities: Scarecrow

alias_or_role_evidence: 

unknowns: Physical appearance, scale, specific monkey species.

source_refs: 

[[SECTION markdown]]

# Winged Monkeys
**Role:** Antagonists (referenced).
**Status:** Referenced.

### Description
A group of creatures mentioned as having discarded the Scarecrow's clothes in a tall tree. Their exact appearance is not described beyond their name.

### Visual Cues
- **Traits:** Possess wings.
- **Uncertainty Note:** Physical morphology and scale are unknown; they are only identified by name.
- **Noun Phrases:** Winged primates, flying monkeys.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
