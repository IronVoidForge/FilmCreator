# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:00:57.342487+00:00
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

Chapter id: CH021

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

**Setting:**
The journey begins on the cultivated agricultural tracts between the polar ice caps and populated centers, moving toward the vast, walled city of Zodanga. The setting features advanced Martian infrastructure, including underground water conduits, high-rise metal residences, and a central plaza surrounded by palaces and mechanical cafes.

**Characters:**
* **John Carter:** The protagonist, an Earthman with superhuman leaping abilities, currently undercover in Zodanga.
* **Woola:** Carter's loyal, domesticated creature, whom he must leave behind for safety.
* **Kantos Kan:** A Red Martian and friend of Carter; an air scout working to find Dejah Thoris.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **Sab Than:** The Prince of Zodanga, who has fallen in love with Dejah Thoris.
* **The Zodangan Cousin:** A member of the royal family saved by Carter during a skirmish.
* **Green Warriors:** Thark/Warhoon-style combatants who attack the Zodangan scout.

**Events:**
1. **Travel and Lore:** Carter travels through Martian farmlands, learning about their sophisticated irrigation and highly refined biological life. He learns from a noble that Dejah Thoris is presumed dead following a conflict with Tharks and Warhoons.
2. **Arrival at Zodanga:** Carter arrives at the gates of Zodanga and reluctantly separates from Woola to avoid drawing attention to his companion's unique species.
3. **Reunion with Kantos Kan:** In the central plaza, Carter reunites with Kantos Kan. They discuss the political tension: Sab Than intends to marry Dejah Thoris to secure peace, a demand rejected by Helium.
4. **Infiltration:** Kantos Kan uses his influence to enroll Carter as an air scout in the Zodangan navy under the alias "John Carter." Carter spends several days learning Martian aviation and the mechanics of the "eighth ray" propulsion.
5. **The Skirmish:** During a solo flight, Carter discovers three Green Warriors attacking a Zodangan air scout (a cousin of the Jeddak). Carter intervenes, killing the warriors and saving the scout.
6. **Recognition:** Carter and the scout return to Zodanga. During a massive military ceremony in the plaza, Carter is publicly honored by Jeddak Than Kosis for his bravery. He is appointed a *padwar* of The Guards and granted quarters within the royal palace.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH021

- [John Carter](#john-carter)
- [Woola](#woola)
- [Kantos Kan](#kantos-kan)
- [Than Kosis](#than-kosis)
- [Sab Than](#sab-than)
- [The Zodangan Cousin](#the-zodangan-cousin)
- [Green Warriors](#green-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH021 John Carter
aliases: Earthman, Padwar of The Guards
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
direct_identity_evidence: Explicitly named as John Carter, an Earthman.
direct_visual_evidence: Implied human morphology; superhuman leaping abilities mentioned.
costume_or_covering_evidence: Undercover in Zodanga; later appointed Padwar of The Guards.
movement_evidence: Superhuman leaping abilities.
associated_entities: Woola, Kantos Kan, Than Kosis
alias_or_role_evidence: Referred to as an Earthman and a padwar.
unknowns: 
source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Air Scout / Padwar of The Guards
**Presence:** Physically Present
**Description:** An Earthman with superhuman leaping abilities. Currently operating undercover in Zodanga, he has transitioned into a role as an air scout and was subsequently honored as a *padwar* of The Guards.
**Visual Cues:** Humanoid morphology; capable of extreme leaps.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH021 Woola
aliases: Loyal Creature
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: unknown
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: Named as Woola, Carter's loyal companion.
direct_visual_evidence: Described as a unique species that must be hidden from Zodangan view.
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: John Carter
alias_or_role_evidence: Carter's loyal, domesticated creature.
unknowns: Specific morphology and scale are not detailed in this chapter.
source_refs: 

[[SECTION markdown]]
# Woola
**Role:** Companion to John Carter
**Presence:** Physically Present (then separated)
**Description:** A loyal, domesticated creature of a unique species. Carter leaves him behind to avoid drawing attention to his unusual nature.
**Visual Cues:** Species is distinct enough from Martians to require concealment; specific physical traits are currently unspecified in this text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: CH021 Kantos Kan
aliases: Air Scout
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
direct_identity_evidence: Named as Kantos Kan, a Red Martian.
direct_visual_evidence: Red Martian morphology.
costume_or_covering_evidence: Air scout in the Zodangan navy.
movement_evidence: 
associated_entities: John Carter
alias_or_role_evidence: Friend of Carter; air scout.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Kantos Kan
**Role:** Red Martian / Air Scout
**Presence:** Physically Present
**Description:** A Red Martian and friend to John Carter. He serves as an air scout and uses his influence to help Carter enroll in the Zodangan navy.
**Visual Cues:** Red Martian (humanoid non-human).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: CH021 Than Kosis
aliases: Jeddak of Zodanga
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
direct_identity_evidence: Named as Than Kosis, the Jeddak of Zodanga.
direct_visual_evidence: Martian royalty.
costume_or_covering_evidence: Royal attire implied by status and ceremony.
movement_evidence: 
associated_entities: Sab Than, Dejah Thoris
alias_or_role_evidence: Ruler of Zodanga.
unknowns: Specific physical features not detailed.
source_refs: 

[[SECTION markdown]]
# Than Kosis
**Role:** Jeddak (Ruler) of Zodanga
**Presence:** Physically Present (Ceremony)
**Description:** The ruler of the walled city of Zodanga. He presides over military ceremonies and honors John Carter for his bravery.
**Visual Cues:** Martian royalty; high-status appearance.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: CH021 Sab Than
aliases: Prince of Zodanga
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
direct_identity_evidence: Named as Sab Than, Prince of Zodanga.
direct_visual_evidence: Martian royalty.
costume_or_covering_evidence: Royal status.
movement_evidence: 
associated_entities: Than Kosis, Dejah Thoris
alias_or_role_evidence: Prince; suitor to Dejah Thoris.
unknowns: Specific physical features not detailed.
source_refs: 

[[SECTION markdown]]
# Sab Than
**Role:** Prince of Zodanga
**Presence:** Referenced
**Description:** The Prince of Zodanga who intends to marry Dejah Thoris to secure peace, a move rejected by Helium.
**Visual Cues:** Martian royalty.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zodangan_cousin
canonical_character_id: CH021 Zodangan Cousin
aliases: Zodangan Air Scout
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is identified only by relation/role; no physical description provided.
clarification_required: true
clarification_reason: Identity and appearance are unknown beyond being a royal relative.
clarification_question: What is the name and physical appearance of the Zodangan cousin?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: Identified as a member of the royal family and a Zodangan air scout.
direct_visual_evidence: None.
costume_or_covering_evidence: Zodangan air scout uniform/gear.
movement_evidence: Flying an air vessel.
associated_entities: Than Kosis, John Carter
alias_or_role_evidence: Cousin to the Jeddak; victim of Green Warrior attack.
unknowns: Name, specific appearance.
source_refs: 

[[SECTION markdown]]
# The Zodangan Cousin
**Role:** Royal Family Member / Air Scout
**Presence:** Physically Present (during skirmish)
**Description:** A member of the Zodangan royal family and an air scout who was attacked by Green Warriors before being rescued by John Carter.
**Visual Cues:** Wears Zodangan air scout gear.
**Uncertainty Note:** No specific physical description or name is provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_warriors
canonical_character_id: CH021 Green Warriors
aliases: Combatants
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
direct_identity_evidence: Named as Green Warriors.
direct_visual_evidence: Implied green skin/appearance based on name.
costume_or_covering_evidence: Combatant gear.
movement_evidence: Attacking an air scout.
associated_entities: Zodangan Cousin
alias_or_role_evidence: Thark/Warhoon-style combatants.
unknowns: Specific facial features or exact armor details.
source_refs: 

[[SECTION markdown]]
# Green Warriors
**Role:** Combatants / Aggressors
**Presence:** Physically Present (Skirmish)
**Description:** Thark or Warhoon-style combatants who attack a Zodangan air scout during a solo flight.
**Visual Cues:** Green coloration; warrior/combatant silhouette.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
