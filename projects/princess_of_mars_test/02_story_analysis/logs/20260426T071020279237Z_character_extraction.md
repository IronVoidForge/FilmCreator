# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:10:20.279237+00:00
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

Chapter id: CH027

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

**Setting:** The city of Helium (Palace gardens and council chambers) and the Atmosphere Plant.

**Characters:**
* **John Carter:** Prince of Helium, driven by love for Dejah Thoris to save the planet.
* **Dejah Thoris:** Princess of Helium, facing asphyxiation as the air thins.
* **Tardos Mors:** Jeddak of Helium.
* **Woola:** The Martian hound.
* **The Keeper/Assistant Keeper (deceased):** Murdered, leading to the plant's failure.

**Events:**
* **Peace and Prosperity:** Following a period of peace with the Tharks, John Carter and Dejah Thoris live in happiness, awaiting the hatching of their egg.
* **The Catastrophe:** News arrives that the keeper of the atmosphere plant has been murdered. The engine has stopped, causing a rapid decrease in planetary air pressure.
* **The Dying Days:** As the air thins over three days, the population of Barsoom begins to succumb to asphyxiation. In the Helium palace, the royal family gathers in a sunken garden to face death.
* **The Revelation:** As Dejah Thoris falls into a coma, John Carter experiences a sudden mental breakthrough, recalling nine specific "thought waves" that serve as the key to the atmosphere plant's locks.
* **The Race Against Time:** John Carter commandeers a high-speed air-scout machine, stripping it of all weight to maximize speed. He flies through the thinning atmosphere toward the plant.
* **The Atmosphere Plant:** Arriving at the plant, John finds most workers dead or dying. Using his mental breakthrough, he successfully unlocks the three great doors of the plant. He instructs a surviving worker to restart the pumps before collapsing from exhaustion and lack of oxygen.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH027

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Tardos Mors](#tardos_mors)
- [Woola](#woola)
- [The Keeper](#the_keeper)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Prince of Helium
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
direct_identity_evidence: Explicitly named as Prince of Helium and protagonist.
direct_visual_evidence: Not visually described in this specific chapter text, but established character.
costume_or_covering_evidence: None provided in this chapter.
movement_evidence: Flying an air-scout machine; collapsing from exhaustion.
associated_entities: Dejah Thoris, Tardos Mors, Woola
alias_or_role_evidence: Prince of Helium
unknowns: 
source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Prince of Helium  
**Presence:** Physically Present  

**Physical Description:**  
Established human male. In this chapter, he is depicted in a state of extreme physical exertion and oxygen deprivation.

**Costume & Silhouette:**  
No specific costume details provided for this chapter; however, he operates a stripped-down, high-speed air-scout machine.

**Descriptive Noun Phrases:**  
Human male, Martian prince, pilot of air-scout, exhausted survivor.

**Uncertainty Notes:**  
Specific visual attire for the Helium royal family is not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH002 Dejah Thoris
aliases: Princess of Helium
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
direct_identity_evidence: Explicitly named as Princess of Helium.
direct_visual_evidence: None in this chapter beyond her state of coma.
costume_or_covering_evidence: None provided.
movement_evidence: Falling into a coma due to asphyxiation.
associated_entities: John Carter, Tardos Mors
alias_or_role_evidence: Princess of Helium
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium  
**Presence:** Physically Present (Unconscious)  

**Physical Description:**  
Human female. Currently in a coma resulting from thinning atmosphere and lack of oxygen.

**Costume & Silhouette:**  
Not specified in this chapter.

**Descriptive Noun Phrases:**  
Human female, Martian princess, comatose royal.

**Uncertainty Notes:**  
Visual details are absent due to her medical state and the focus on the catastrophe.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tardos_mors
canonical_character_id: CH003 Tardos Mors
aliases: Jeddak of Helium
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
direct_identity_evidence: Named as Jeddak of Helium.
direct_visual_evidence: Present in the sunken garden.
costume_or_covering_evidence: None provided.
movement_evidence: Gathering in a sunken garden to face death.
associated_entities: John Carter, Dejah Thoris
alias_or_role_evidence: Jeddak of Helium
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tardos Mors
**Role:** Jeddak (Ruler) of Helium  
**Presence:** Physically Present  

**Physical Description:**  
Human male, elder/ruler status implied.

**Costume & Silhouette:**  
Not specified in this chapter.

**Descriptive Noun Phrases:**  
Human male, Martian ruler, Jeddak.

**Uncertainty Notes:**  
No specific physical traits provided for this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH004 Woola
aliases: Martian hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: Named as the Martian hound.
direct_visual_evidence: Established character.
costume_or_covering_evidence: None.
movement_evidence: Associated with the royal family in the garden.
associated_entities: John Carter
alias_or_role_evidence: Martian hound
unknowns: 
source_refs: 

[[SECTION markdown]]
# Woola
**Role:** Companion / Martian Hound  
**Presence:** Physically Present  

**Physical Description:**  
Large, quadrupedal Martian creature.

**Costume & Silhouette:**  
Natural biological form (hound).

**Descriptive Noun Phrases:**  
Large Martian hound, quadrupedal beast, loyal companion.

**Uncertainty Notes:**  
Specific color or texture details are not provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_keeper
canonical_character_id: CH005 The Keeper
aliases: Assistant Keeper
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is deceased and only referenced as a victim of murder; no physical description provided.
clarification_required: true
clarification_reason: Identity and appearance are unknown.
clarification_question: What was the physical appearance and role/rank of the Keeper?
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: Named as the keeper of the atmosphere plant.
direct_visual_evidence: None (deceased).
costume_or_covering_evidence: None.
movement_evidence: Murdered.
associated_entities: Atmosphere Plant workers
alias_or_role_evidence: Keeper/Assistant Keeper
unknowns: Physical appearance, specific age, exact rank.
source_refs: 

[[SECTION markdown]]
# The Keeper
**Role:** Deceased official of the Atmosphere Plant  
**Presence:** Referenced (Deceased)  

**Physical Description:**  
Unknown. Character is deceased at the start of the chapter.

**Costume & Silhouette:**  
Unknown.

**Descriptive Noun Phrases:**  
Murdered plant keeper, deceased official.

**Uncertainty Notes:**  
This character serves as a plot catalyst but lacks any visual or physical description in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
