# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:07:50.555687+00:00
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

Chapter id: CH005

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

# Chapter Summary: CH005 (Chapter V)

## Narrative Arc
The narrator continues their captivity among the Martians, focusing on the relationship with Sola and the behavior of the Martian watch dog. The chapter explores the biological anomalies of Mars, including its moons and plant-based resources, before culminating in a physical confrontation that reveals the true nature of the Martian inhabitants.

## Key Events
- **Guardian Dynamics:** Sola leaves the chamber with the narrator's "watch dog," which proves to be fiercely loyal, guarding the narrator even when left alone.
- **Room Examination:** The narrator inspects their captive room, noting mural paintings that depict earthly-like landscapes but lack animal representations, hinting at Martian biology.
- **Sustenance:** Sola returns with food and drink. The narrator learns that the "milk" is derived from a large plant rather than an animal, capable of producing significant quantities daily.
- **Sleep Cycle:** The narrator sleeps through the cold Martian night, noting the sudden temperature changes and the illumination provided by Mars' two moons.
- **Testing Loyalty:** The narrator tests the watch dog's loyalty by walking outside the building. The dog follows closely but attacks at the city edge.
- **Escape Attempt:** Using his jumping ability, the narrator leaps over the charging dog and escapes briefly to a window sill.
- **Capture:** Despite reaching the window sill, the narrator is dragged back into the room by a colossal, ape-like Martian man, ending the chapter on a cliffhanger of physical threat.

## Character Focus
- **Narrator:** Observant, adventurous, testing boundaries despite captivity.
- **Sola:** Sympathetic, kind, and caring for the narrator's needs.
- **Martian Dog:** Loyal, ferocious, fast, and protective.
- **Martian Man (Ape-like):** Colossal, hairless, white with bristly head hair, physically dominant.

## Setting Details
- **Captive Room:** Furnished with silks and furs, containing mural paintings of rare beauty.
- **Martian City:** Features deserted streets and buildings overlooking a valley.
- **Environment:** Extremely cold nights, brilliant illumination when moons are present, lack of atmosphere diffusing starlight.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH005 (Chapter V)

## Narrator / Protagonist
- **Role:** Captive observer, boundary tester
- **Status:** Referenced throughout chapter
- **Physical Presence:** Uncertain (no detailed form description)
- **Notes:** Sparse physical detail; manual description required for image generation

## Sola
- **Role:** Caregiver, sympathetic figure
- **Status:** Referenced throughout chapter
- **Physical Presence:** Uncertain (no detailed form description)
- **Notes:** Sympathetic character with sparse physical details

## Martian Dog
- **Role:** Guardian, loyal protector
- **Status:** Physically present in chamber and city
- **Physical Presence:** Present but appearance details limited
- **Notes:** Loyal, ferocious, fast; physical form not fully described

## Martian Man (Ape-like)
- **Role:** Colossal captor, physical threat
- **Status:** Appears at chapter climax
- **Physical Presence:** Present with partial description
- **Notes:** Colossal, hairless, white with bristly head hair; appearance details sparse

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH005 Narrator

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical form or appearance details provided in chapter; only behavioral traits (jumping ability) mentioned.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Narrator / Protagonist

## Chapter Role
Captive observer testing boundaries despite imprisonment among Martians.

## Physical Presence
Uncertain - no detailed physical description provided in chapter text.

## Known Traits
- Observant and adventurous
- Possesses jumping ability (used to escape dog)
- Tests loyalty of watch dog
- Can reach window sill with effort

## Appearance Notes
No physical form details available in source material. Character is primarily identified through narrative voice and actions rather than visual description.

## Continuity-Critical Traits
- Captive status throughout chapter
- Relationship with Sola (caregiver)
- Interaction with Martian dog (guardian)
- Confrontation with Martian man at chapter end

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical appearance details provided in chapter; only personality traits (sympathetic, kind, caring) mentioned.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is Sola's physical form and appearance?

[[SECTION markdown]]

# Sola

## Chapter Role
Caregiver who provides food, drink, and attention to narrator's needs.

## Physical Presence
Uncertain - no detailed physical description provided in chapter text.

## Known Traits
- Sympathetic toward narrator
- Kind and caring nature
- Brings sustenance (food and drink)
- Leaves chamber with narrator's watch dog

## Appearance Notes
No physical form details available in source material. Character is primarily identified through actions and personality rather than visual description.

## Continuity-Critical Traits
- Relationship with Narrator (caregiver/captive dynamic)
- Interaction with Martian dog (allows it to leave chamber)
- Provides plant-derived milk as sustenance

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_dog

canonical_character_id: CH005 Martian Dog

aliases: Watch Dog, Guardian Dog

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance details limited to behavioral traits (loyal, ferocious, fast); no specific form description provided.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is the Martian dog's physical form and appearance?

[[SECTION markdown]]

# Martian Dog

## Chapter Role
Loyal guardian protecting narrator from Martians.

## Physical Presence
Present - physically in chamber, follows narrator outside building, attacks at city edge.

## Known Traits
- Fiercely loyal to narrator
- Fast movement speed
- Ferocious when attacking
- Protective behavior (guards even when left alone)
- Attacks at city edge during escape attempt

## Appearance Notes
No detailed physical form description available in source material. Character is primarily identified through behavioral traits and relationship to narrator rather than visual appearance.

## Continuity-Critical Traits
- Guardian of narrator's chamber
- Allows Sola to leave with it
- Follows narrator outside building
- Attacks at city edge (tests loyalty)
- Colossal Martian man appears during escape attempt

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_man_ape

canonical_character_id: CH005 Martian Man (Ape-like)

aliases: Ape-like Martian, Colossal Martian

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical description provided is partial (colossal, hairless, white with bristly head hair); insufficient for dependable image generation.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is the Martian man's full physical form and appearance?

[[SECTION markdown]]

# Martian Man (Ape-like)

## Chapter Role
Colossal captor who appears at chapter climax to drag narrator back into room.

## Physical Presence
Present - appears at window sill during escape attempt, drags narrator back into chamber.

## Known Traits
- Colossal size
- Hairless body
- White skin tone
- Bristly head hair
- Physically dominant
- Ape-like appearance

## Appearance Notes
Partial physical description available: colossal, hairless, white with bristly head hair. Character is physically dominant and appears at chapter end as threat.

## Continuity-Critical Traits
- Captor of narrator
- Appears during escape attempt
- Drags narrator back into room from window sill
- Ends chapter on cliffhanger of physical threat

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH005 (Chapter V)

## Narrator / Protagonist
- **Role:** Captive observer, boundary tester
- **Status:** Referenced throughout chapter
- **Physical Presence:** Uncertain (no detailed form description)
- **Notes:** Sparse physical detail; manual description required for image generation

## Sola
- **Role:** Caregiver, sympathetic figure
- **Status:** Referenced throughout chapter
- **Physical Presence:** Uncertain (no detailed form description)
- **Notes:** Sympathetic character with sparse physical details

## Martian Dog
- **Role:** Guardian, loyal protector
- **Status:** Physically present in chamber and city
- **Physical Presence:** Present but appearance details limited
- **Notes:** Loyal, ferocious, fast; physical form not fully described

## Martian Man (Ape-like)
- **Role:** Colossal captor, physical threat
- **Status:** Appears at chapter climax
- **Physical Presence:** Present with partial description
- **Notes:** Colossal, hairless, white with bristly head hair; appearance details sparse

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH005 Narrator

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical form or appearance details provided in chapter; only behavioral traits (jumping ability) mentioned.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Narrator / Protagonist

## Chapter Role
Captive observer testing boundaries despite imprisonment among Martians.

## Physical Presence
Uncertain - no detailed physical description provided in chapter text.

## Known Traits
- Observant and adventurous
- Possesses jumping ability (used to escape dog)
- Tests loyalty of watch dog
- Can reach window sill with effort

## Appearance Notes
No physical form details available in source material. Character is primarily identified through narrative voice and actions rather than visual description.

## Continuity-Critical Traits
- Captive status throughout chapter
- Relationship with Sola (caregiver)
- Interaction with Martian dog (guardian)
- Confrontation with Martian man at chapter end

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical appearance details provided in chapter; only personality traits (sympathetic, kind, caring) mentioned.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is Sola's physical form and appearance?

[[SECTION markdown]]

# Sola

## Chapter Role
Caregiver who provides food, drink, and attention to narrator's needs.

## Physical Presence
Uncertain - no detailed physical description provided in chapter text.

## Known Traits
- Sympathetic toward narrator
- Kind and caring nature
- Brings sustenance (food and drink)
- Leaves chamber with narrator's watch dog

## Appearance Notes
No physical form details available in source material. Character is primarily identified through actions and personality rather than visual description.

## Continuity-Critical Traits
- Relationship with Narrator (caregiver/captive dynamic)
- Interaction with Martian dog (allows it to leave chamber)
- Provides plant-derived milk as sustenance

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_dog

canonical_character_id: CH005 Martian Dog

aliases: Watch Dog, Guardian Dog

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance details limited to behavioral traits (loyal, ferocious, fast); no specific form description provided.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is the Martian dog's physical form and appearance?

[[SECTION markdown]]

# Martian Dog

## Chapter Role
Loyal guardian protecting narrator from Martians.

## Physical Presence
Present - physically in chamber, follows narrator outside building, attacks at city edge.

## Known Traits
- Fiercely loyal to narrator
- Fast movement speed
- Ferocious when attacking
- Protective behavior (guards even when left alone)
- Attacks at city edge during escape attempt

## Appearance Notes
No detailed physical form description available in source material. Character is primarily identified through behavioral traits and relationship to narrator rather than visual appearance.

## Continuity-Critical Traits
- Guardian of narrator's chamber
- Allows Sola to leave with it
- Follows narrator outside building
- Attacks at city edge (tests loyalty)
- Colossal Martian man appears during escape attempt

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_man_ape

canonical_character_id: CH005 Martian Man (Ape-like)

aliases: Ape-like Martian, Colossal Martian

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical description provided is partial (colossal, hairless, white with bristly head hair); insufficient for dependable image generation.

clarification_required: true

clarification_reason: Needs identity clarification for dependable image generation.

clarification_question: What is the Martian man's full physical form and appearance?

[[SECTION markdown]]

# Martian Man (Ape-like)

## Chapter Role
Colossal captor who appears at chapter climax to drag narrator back into room.

## Physical Presence
Present - appears at window sill during escape attempt, drags narrator back into chamber.

## Known Traits
- Colossal size
- Hairless body
- White skin tone
- Bristly head hair
- Physically dominant
- Ape-like appearance

## Appearance Notes
Partial physical description available: colossal, hairless, white with bristly head hair. Character is physically dominant and appears at chapter end as threat.

## Continuity-Critical Traits
- Captor of narrator
- Appears during escape attempt
- Drags narrator back into room from window sill
- Ends chapter on cliffhanger of physical threat

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_PACKET]]
````
