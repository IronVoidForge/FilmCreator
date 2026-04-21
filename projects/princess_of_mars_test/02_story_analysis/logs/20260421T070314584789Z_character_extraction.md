# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:03:14.584789+00:00
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

Chapter id: CH006

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

**Setting:** An interior chamber within a building in a Martian city, leading out to a plaza.

**Characters:**
- **The Protagonist:** An Earthman fighting for survival.
- **The Watch-thing:** A multi-legged, loyal, and fierce creature that serves as the protagonist's guardian.
- **The Bull Ape & Mate:** Large (10-15ft), humanoid, ape-like creatures with four arms and immense strength.
- **Tars Tarkas:** A Martian warrior who observes and respects the protagonist's combat skills.
- **Sola:** A Martian woman who shows genuine concern and solicitude for the protagonist.
- **Martian Warriors:** A group of warriors who value physical prowess and witness the protagonist's fight.

**Events:**
- The protagonist is pinned by a large, ape-like creature while its mate approaches with a stone cudgel.
- The protagonist's "watch-thing" intervenes, engaging the mate in a brutal, life-or-death struggle.
- As the watch-thing begins to lose the fight against the mate, the protagonist uses the fallen cudgel to crush the skull of the first ape.
- The second ape (the mate) returns in a rage; the protagonist initially considers fleeing but decides to stay and defend his dying guardian.
- Using earthly combat tactics—striking the chin and stomach—the protagonist manages to incapacitate the enraged ape and kills it with the cudgel.
- Tars Tarkas, Sola, and other warriors arrive, having witnessed the fight; they applaud the protagonist's bravery, viewing him through the lens of Martian values (strength/skill).
- Sola shows empathy by checking the protagonist for injuries, contrasting with the laughter of the other warriors.
- A Martian warrior attempts to execute the wounded watch-thing, but the protagonist intervenes by striking the warrior's arm, preventing the shot.
- The protagonist leaves the building with Sola and his loyal beast, having secured two unlikely allies on Mars.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH006

- [Protagonist](#protagonist)
- [The Watch-thing](#the-watch-thing)
- [Bull Ape](#bull-ape)
- [Bull Ape Mate](#bull-ape-mate)
- [Tars Tarkas](#tars-tarkas)
- [Sola](#sola)
- [Martian Warriors](#martian-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, clothing, and specific build are not described in this chapter.

clarification_required: true

clarification_reason: Needs physical description for visual consistency.

clarification_question: What is the protagonist's hair color, eye color, facial features, and current attire?

[[SECTION markdown]]

# Protagonist
**Role:** Central survivor/combatant.

**Status:** Physically present.

**Physical Description:** An Earthman capable of high-intensity combat and utilizing earthly striking tactics (chin and stomach strikes). 

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Earthman fighter, combatant, survivor.

**Uncertainty Notes:** No specific visual details provided regarding his physical appearance or clothing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watch_thing

canonical_character_id: CH005 Watch-thing

aliases: Guardian, Loyal Beast

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only described as "multi-legged" and "fierce"; lacks specific morphology or color.

clarification_required: true

clarification_reason: Needs detailed biological description for rendering.

clarification_question: What is the specific number of legs, the texture of its skin/fur, and its overall size relative to the protagonist?

[[SECTION markdown]]

# The Watch-thing
**Role:** Protagonist's loyal guardian.

**Status:** Physically present (wounded).

**Physical Description:** A multi-legged creature described as fierce and loyal. Engages in brutal combat with large apes.

**Costume/Silhouette:** Multi-legged, non-humanoid silhouette.

**Descriptive Noun Phrases:** Multi-legged beast, loyal guardian, fierce creature.

**Uncertainty Notes:** Specific anatomy (number of legs, head shape, skin texture) is undefined.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: bull_ape

canonical_character_id: CH007 Bull Ape

aliases: Large ape-like creature

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Bull Ape
**Role:** Antagonist/Combatant.

**Status:** Physically present (deceased).

**Physical Description:** Large humanoid ape-like creature, approximately 10-15ft tall. Possesses four arms and immense strength.

**Costume/Silhouette:** Massive, four-armed primate silhouette.

**Descriptive Noun Phrases:** Four-armed giant ape, massive humanoid primate, 15ft ape.

**Uncertainty Notes:** None.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: bull_ape_mate

canonical_character_id: CH007 Bull Ape Mate

aliases: The mate, enraged ape

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Bull Ape Mate
**Role:** Antagonist/Combatant.

**Status:** Physically present (deceased).

**Physical Description:** Large humanoid ape-like creature, approximately 10-15ft tall. Possesses four arms and immense strength. Characterized by rage during combat.

**Costume/Silhouette:** Massive, four-armed primate silhouette.

**Descriptive Noun Phrases:** Enraged four-armed ape, massive mate ape.

**Uncertainty Notes:** None.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH008 Tars Tarkas

aliases: Martian warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: While a known character, specific visual details for this chapter's rendering are not provided.

clarification_required: true

clarification_reason: Needs visual confirmation of Martian physiology/armor.

clarification_question: What is Tars Tarkas's specific physical appearance and armor style?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Observer/Martian ally.

**Status:** Physically present.

**Physical Description:** A Martian warrior who values strength and combat skill.

**Costume/Silhouette:** Martian warrior attire (unspecified).

**Descriptive Noun Phrases:** Respectful Martian warrior, combat observer.

**Uncertainty Notes:** Visual details of his Martian physiology and gear are missing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH009 Sola

aliases: Martian woman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Needs visual identification.

clarification_question: What is Sola's appearance, hair, and clothing?

[[SECTION markdown]]

# Sola
**Role:** Ally/Empathic Martian.

**Status:** Physically present.

**Physical Description:** A Martian woman who shows genuine concern and solicitude for the protagonist.

**Costume/Silhouette:** Martian female attire (unspecified).

**Descriptive Noun Phrases:** Concerned Martian woman, empathetic ally.

**Uncertainty Notes:** Physical appearance is not described.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH010 Martian Warriors

aliases: Group of warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: Generic group with no specific visual descriptors.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warriors
**Role:** Witnesses/Background characters.

**Status:** Physically present.

**Physical Description:** A group of Martians who value physical prowess and laugh at the protagonist's struggle, though one attempts to execute the watch-thing.

**Costume/Silhouette:** Standard Martian warrior gear (unspecified).

**Descriptive Noun Phrases:** Laughing Martian warriors, martial Martian group.

**Uncertainty Notes:** Individual features and specific armor types are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
