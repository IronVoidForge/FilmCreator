# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:58:28.710255+00:00
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

Chapter id: CH014

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

John Carter struggles with his unspoken feelings for Dejah Thoris, fearing that a confession might burden her further; however, a misunderstanding leads to a moment of tension where Dejah withdraws from him in silent dignity. As the group prepares to depart for Thark, Carter protests the heavy chains Sarkoja has placed on Dejah's chariot, but Tars Tarkas defends it as a security measure, though he later shows a hint of compassion by unfastening her fetters during a campout. Amidst this, Carter notes the intense hatred directed toward him by Sarkoja and the warrior Zad.

The tension escalates when Dejah Thoris expresses her contempt for Carter through Sola, leaving Carter feeling profoundly homesick for Earth. During the march toward Thark, the party destroys an incubator belonging to the green men of Warhoon. The journey takes a violent turn during a rest halt when Zad provokes Carter into a formal duel. As they fight, Sarkoja uses a mirror to catch the sun and blind Carter, attempting to aid Zad in a killing blow. In the ensuing chaos, Sola heroically leaps to shield Dejah Thoris from Sarkoja's dagger, but the distraction allows Zad to land a fatal thrust in Carter's chest, leaving him fading into unconsciousness.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH014

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Sarkoja](#sarkoja)
- [Tars Tarkas](#tars_tarkas)
- [Zad](#zad)
- [Sola](#sola)
- [Warhoon Green Men](#warhoon_green_men)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Carter

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist

**Presence:** Physically Present (Injured/Unconscious)

**Description:** A man struggling with emotional tension and physical combat. He is involved in a formal duel with Zad and sustains a fatal thrust to the chest.

**Prompt Phrases:** Human male, warrior, wounded in chest, fighting Thark combatant.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: Princess of Mars

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Primary Female Lead

**Presence:** Physically Present

**Description:** A figure of dignity who experiences tension and contempt toward Carter. She is kept in heavy chains/fetters on a chariot for security during the march.

**Prompt Phrases:** Martian princess, dignified, bound by heavy chains, riding in a chariot.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH004 Sarkoja

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist

**Presence:** Physically Present

**Description:** A hostile figure who directs intense hatred toward Carter. Uses a mirror to catch sunlight to blind opponents during combat.

**Prompt Phrases:** Hostile warrior, using reflective mirror for blinding, aggressive stance.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH005 Tars Tarkas

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Supporting Character / Ally

**Presence:** Physically Present

**Description:** A leader figure who defends the use of security measures (chains) but shows compassion by unfastening Dejah's fetters during camp.

**Prompt Phrases:** Green man warrior, authoritative, compassionate gesture.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: zad

canonical_character_id: CH006 Zad

aliases: Warrior Zad

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Zad
**Role:** Antagonist / Combatant

**Presence:** Physically Present

**Description:** A warrior who harbors intense hatred for Carter and provokes him into a formal duel. He delivers the fatal thrust to Carter's chest.

**Prompt Phrases:** Aggressive warrior, combatant, wielding blade, lethal strike.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH007 Sola

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Supporting Character / Heroic Figure

**Presence:** Physically Present

**Description:** A character who acts as a messenger for Dejah's contempt and ultimately performs a heroic act by leaping to shield Dejah from Sarkoja's dagger.

**Prompt Phrases:** Heroic female, shielding others, sacrificial movement.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: warhoon_green_men

canonical_character_id: CH008 Warhoon Green Men

aliases: Green men of Warhoon

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as owners of an incubator; no specific physical traits provided.

clarification_required: true

clarification_reason: Need visual specifics for the species/group.

clarification_question: What is the physical appearance and scale of the Warhoon green men?

[[SECTION markdown]]

# Warhoon Green Men
**Role:** Referenced Group

**Presence:** Referenced

**Description:** A group associated with an incubator destroyed by the party during their march.

**Uncertainty Note:** Physical appearance is unknown beyond being "green men."
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
