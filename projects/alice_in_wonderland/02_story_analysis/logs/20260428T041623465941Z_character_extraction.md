# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:16:23.465941+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH011

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each character item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION character_index_markdown]] and [[SECTION markdown]] exactly as written

- do not invent alternate closing tags such as [[/FIL_RECORD]], [[end_section]], or misspelled FILMCREATOR tags

- do not echo this instruction block back as an example packet; return the actual packet only



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

**Location:** The Court of Justice (an outdoor or large open court setting).
**Characters Present:** 
- Alice (growing in size)
- The King of Hearts (acting as Judge, wearing a crown over a large wig)
- The Queen of Hearts (wearing spectacles)
- The White Rabbit (Herald/Officer, carrying a trumpet and parchment scroll)
- The Knave of Hearts (Defendant, in chains, guarded by two soldiers)
- The Gryphon (Witness/Companion to Alice)
- The Jury (Twelve creatures: mix of animals and birds; writing on slates)
- Bill the Lizard (Juror)
- The Hatter (Witness, carrying a teacup and bread-and-butter)
- The March Hare (Witness/Companion to Hatter)
- The Dormouse (Witness/Companion to Hatter, prone to sleeping/being erratic)
- The Duchess's Cook (Witness, carrying a pepper-box)
- Guinea-pigs (Court spectators)
- Court Officers

**Key Events & Visual Continuity:**
- **Setting Establishment:** A large dish of tarts sits on a central table. The Knave is in chains with guards.
- **Jury Interaction:** Jurors are writing names on slates. Alice calls them "stupid things" aloud; the White Rabbit commands silence. One juror (Bill the Lizard) loses his squeaky pencil after Alice steals it; he must write with a finger (leaving no marks).
- **The Accusation:** The White Rabbit blows three trumpet blasts and reads the charge: The Knave of Hearts stole the Queen's tarts.
- **Witness 1 - The Hatter:** Enters carrying tea and bread-and-butter, accompanied by the March Hare and Dormouse. 
    - The King questions the date he began his tea (March 14th, 15th, or 16th); jurors record all three and perform math on their slates.
    - The Hatter is accused of "stealing" a hat; he explains it is for sale.
    - The Queen stares intensely at the Hatter; he becomes so nervous he bites his teacup instead of bread.
- **Alice's Physical Shift:** Alice begins to grow in size, causing discomfort to the Dormouse. The Dormouse sulkily moves to the other side of the court.
- **Hatter's Testimony:** A nonsensical exchange regarding "the twinkling of the tea." The March Hare denies saying things; the Dormouse is asleep and offers no testimony. 
- **Court Suppression:** Two guinea-pigs cheer and are "suppressed" by being put into a large canvas bag and sat upon by officers.
- **Hatter's Exit:** The Hatter drops his tea/bread, kneels, and leaves the court in a hurry without his shoes. The Queen orders his head removed, but he is gone before the officer arrives.
- **Witness 2 - The Cook:** Enters carrying a pepper-box; causes immediate sneezing among nearby spectators.
    - The King cross-examines her: "What are tarts made of?" She answers "Pepper, mostly."
    - The Dormouse (from behind) says "Treacle."
    - **The Queen's Outburst:** The Queen shrieks a series of contradictory commands to behead/suppress/pinch the Dormouse. In the ensuing chaos, the Cook disappears.
- **The Reveal:** The White Rabbit consults his list and announces the next witness: Alice.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[FILMCREATOR_RECORD type=character]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice is explicitly named and participates in the trial."
direct_visual_evidence: "Described as growing in size during the chapter."
costume_or_covering_evidence: ""
movement_evidence: "Growing in size, causing discomfort to others."
associated_entities: ["the_king_of_hearts", "the_queen_of_hearts", "the_white_rabbit", "the_gryphon"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Witness

**Status:** Physically Present (Growing in size)

**Physical Description:**
A young girl who undergoes a significant physical change during the chapter, growing larger in scale, which causes discomfort to smaller creatures like the Dormouse.

**Costume & Silhouette:**
No specific costume details provided in this chapter, but her silhouette changes as she grows.

**Descriptive Noun Phrases:**
- Growing girl
- Large-scale child
- Witness at the trial

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_king_of_hearts
canonical_character_id: king_of_hearts
aliases: ["The King"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the King of Hearts acting as Judge."
direct_visual_evidence: "Wearing a crown over a large wig."
costume_or_covering_evidence: "Crown, large wig."
movement_evidence: ""
associated_entities: ["the_queen_of_hearts", "the_knave_of_hearts"]
alias_or_role_evidence: "Acting as Judge."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The King of Hearts
**Role:** Judge

**Status:** Physically Present

**Physical Description:**
A royal figure presiding over the court.

**Costume & Silhouette:**
- Large, prominent wig
- Crown worn over the wig

**Descriptive Noun Phrases:**
- Royal judge
- King with large wig and crown

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_queen_of_hearts
canonical_character_id: queen_of_hearts
aliases: ["The Queen"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the Queen of Hearts."
direct_visual_evidence: "Wearing spectacles; stares intensely at the Hatter."
costume_or_covering_evidence: "Spectacles."
movement_evidence: "Shrieks contradictory commands."
associated_entities: ["the_king_of_hearts", "the_knave_of_hearts"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Queen of Hearts
**Role:** Accuser / Authority Figure

**Status:** Physically Present

**Physical Description:**
An intense and volatile royal figure.

**Costume & Silhouette:**
- Wearing spectacles

**Descriptive Noun Phrases:**
- Intense queen with spectacles
- Volatile royal authority

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_white_rabbit
canonical_character_id: white_rabbit
aliases: ["Herald", "Officer"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the White Rabbit."
direct_visual_evidence: "Carrying a trumpet and parchment scroll."
costume_or_covering_evidence: "Carries a trumpet and parchment scroll."
movement_evidence: "Blows three trumpet blasts; reads from a list/scroll."
associated_entities: ["alice", "the_knave_of_hearts"]
alias_or_role_evidence: "Acts as Herald/Officer."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The White Rabbit
**Role:** Herald / Officer

**Status:** Physically Present

**Physical Description:**
A small rabbit acting in an official capacity.

**Costume & Silhouette:**
- Carrying a trumpet
- Carrying a parchment scroll

**Descriptive Noun Phrases:**
- Official white rabbit
- Trumpet-bearing herald

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_knave_of_hearts
canonical_character_id: knave_of_hearts
aliases: ["Defendant"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the Knave of Hearts."
direct_visual_evidence: "In chains, guarded by soldiers."
costume_or_covering_evidence: "Bound in chains."
movement_evidence: ""
associated_entities: ["the_queen_of_hearts"]
alias_or_role_evidence: "The Defendant accused of stealing tarts."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Knave of Hearts
**Role:** Defendant

**Status:** Physically Present

**Physical Description:**
A prisoner accused of theft.

**Costume & Silhouette:**
- Bound in chains
- Under guard by soldiers

**Descriptive Noun Phrases:**
- Chained defendant
- Accused knave

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_gryphon
canonical_character_id: gryphon
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: unknown
scale_hint: unknown
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as the Gryphon."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Witness/Companion to Alice."
unknowns: ["exact morphology (wings vs quadruped details) not explicitly detailed in this text segment"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Gryphon
**Role:** Witness / Companion

**Status:** Physically Present

**Physical Description:**
A mythical creature accompanying Alice.

**Costume & Silhouette:**
Unknown based on this chapter text alone.

**Descriptive Noun Phrases:**
- Mythical gryphon companion

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_jury
canonical_character_id: jury
aliases: ["Twelve creatures"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: context_only
confidence: 0.9
direct_identity_evidence: "Identified as the Jury."
direct_visual_evidence: "A mix of animals and birds; writing on slates."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: "Twelve creatures acting as jurors."
unknowns: ["specific species for all twelve"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Jury
**Role:** Jurors

**Status:** Physically Present

**Physical Description:**
A group of twelve diverse creatures, including various animals and birds.

**Costume & Silhouette:**
- Carrying/using slates for writing

**Descriptive Noun Phrases:**
- Animal jury
- Bird and beast jurors with slates

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: bill_the_lizard
canonical_character_id: bill_the_lizard
aliases: ["Juror"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as Bill the Lizard."
direct_visual_evidence: "Uses a squeaky pencil (until it is stolen)."
costume_or_covering_evidence: ""
movement_evidence: "Writes with his finger after losing his pencil."
associated_entities: ["the_jury"]
alias_or_role_evidence: "A juror."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Bill the Lizard
**Role:** Juror

**Status:** Physically Present

**Physical Description:**
A small lizard.

**Costume & Silhouette:**
- Uses a squeaky pencil (lost)

**Descriptive Noun Phrases:**
- Squeaky pencil-using lizard
- Juror lizard

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_hatter
canonical_character_id: hatter
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the Hatter."
direct_visual_evidence: "Carrying a teacup and bread-and-butter; bites his teacup when nervous; leaves without shoes."
costume_or_covering_evidence: "Carries tea/bread; loses shoes during exit."
movement_evidence: "Kneels and leaves the court in a hurry."
associated_entities: ["the_march_hare", "the_dormouse"]
alias_or_role_evidence: "Witness."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Hatter
**Role:** Witness

**Status:** Physically Present

**Physical Description:**
A nervous individual who reacts strongly to the Queen's presence.

**Costume & Silhouette:**
- Carries a teacup and bread-and-butter
- Barefoot (at end of testimony)

**Descriptive Noun Phrases:**
- Nervous tea-carrying witness
- Barefoot Hatter

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_march_hare
canonical_character_id: march_hare
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the March Hare."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["the_hatter", "the_dormouse"]
alias_or_role_evidence: "Companion to the Hatter/Witness."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The March Hare
**Role:** Witness / Companion

**Status:** Physically Present

**Physical Description:**
A hare accompanying the Hatter.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Accompanying March Hare

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_dormouse
canonical_character_id: dormouse
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the Dormouse."
direct_visual_evidence: "Prone to sleeping; sulkily moves to the other side of court when Alice grows; offers sleepy testimony."
costume_or_covering_evidence: ""
movement_evidence: "Sleeping, sulking, moving away from growing Alice."
associated_entities: ["the_hatter", "the_march_hare"]
alias_or_role_evidence: "Witness/Companion to Hatter."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Dormouse
**Role:** Witness / Companion

**Status:** Physically Present

**Physical Description:**
A very small, sleepy creature.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Sleepy dormouse
- Tiny sulking witness

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_duchesses_cook
canonical_character_id: duchesses_cook
aliases: ["The Cook"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the Duchess's Cook."
direct_visual_evidence: "Carrying a pepper-box; causes sneezing."
costume_or_covering_evidence: "Carries a pepper-box."
movement_evidence: "Enters court, then disappears in chaos."
associated_entities: []
alias_or_role_evidence: "Witness."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Duchess's Cook
**Role:** Witness

**Status:** Physically Present (Disappears during chaos)

**Physical Description:**
A person associated with pepper.

**Costume & Silhouette:**
- Carrying a pepper-box

**Descriptive Noun Phrases:**
- Pepper-carrying cook
- Sneezing-inducing witness

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: guinea_pigs
canonical_character_id: guinea_pigs
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as Guinea-pigs."
direct_visual_evidence: "Cheering in the court; put into a large canvas bag and sat upon."
costume_or_covering_evidence: ""
movement_evidence: "Cheering, then being suppressed/bagged."
associated_entities: ["court_officers"]
alias_or_role_evidence: "Court spectators."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Guinea-pigs
**Role:** Court Spectators

**Status:** Physically Present (Suppressed)

**Physical Description:**
Small rodents.

**Costume & Silhouette:**
- Placed in a large canvas bag

**Descriptive Noun Phrases:**
- Cheering guinea-pigs
- Bagged spectators

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: court_officers
canonical_character_id: court_officers
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: group
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.9
direct_identity_evidence: "Identified as Court Officers."
direct_visual_evidence: "Guarding the Knave; sitting on the bag of guinea-pigs; attempting to behead/suppress."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["the_knave_of_hearts", "guinea_pigs"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Court Officers
**Role:** Guards / Enforcers

**Status:** Physically Present

**Physical Description:**
A group of enforcers maintaining order.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Guarding officers
- Suppressing court officials

[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
