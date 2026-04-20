# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:52:53.381273+00:00
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

Chapter id: CH010

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

John Carter spends his morning exploring the outskirts of the city, attempting to deepen his bond with Woola through affection rather than mere authority. While he successfully establishes a playful connection with the creature, he remains cautious of Sola's warnings regarding the city limits. Upon returning to the plaza, Carter observes the captive Princess Dejah Thoris being guarded by Sarkoja and others. Utilizing his ability to understand the Martian tongue, he eavesdrops on a council meeting led by Lorquas Ptomel. During the proceedings, Dejah Thoris delivers a powerful plea to the Thark council, defending her people's scientific research and rebuking the green Martians for their lack of art, love, and individuality. Her speech moves several warriors, including Tars Tarkas, but the tension breaks when a young warrior strikes Dejah Thoris across the face in a display of mirthless laughter.

Carter intervenes violently, using his superior combat skills to kill the aggressor. Following Martian custom, the dead warrior's possessions are transferred to Carter, effectively elevating him to the status of a Thark chieftain. After tending to Dejah Thoris and revealing his identity as an Earthman, Carter is approached by Tars Tarkas, who questions his rapid mastery of the language and warns him of the danger his temerity has caused. Despite being informed that he remains a prisoner until they reach the headquarters of Tal Hajus, Carter delivers a defiant speech asserting that he will act according to his own conscience and protect Dejah Thoris. Impressed by his resolve, the Tharks allow Carter and Dejah Thoris to depart the chamber accompanied by Woola.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john_carter)
- [Woola](#woola)
- [Sola](#sola)
- [Dejah Thoris](#dejah_thoris)
- [Sarkoja](#sarkoja)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Young Warrior (Aggressor)](#young_warrior_aggressor)
- [Tars Tarkas](#tars_tarkas)
- [Tal Hajus](#tal_hajus)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Carter, Earthman

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Intervener

**Status:** Physically Present

**Physical Description:** An Earthman with superior combat skills and the ability to understand the Martian tongue.

**Costume/Silhouette:** Not explicitly detailed in this chapter, but possesses possessions transferred from a fallen Thark warrior.

**Prompt Phrases:** Human male, Earthman, martial prowess, defiant expression.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH003 Woola

aliases: The creature

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Companion

**Status:** Physically Present

**Physical Description:** A Martian creature capable of forming a playful connection with Carter.

**Costume/Silhouette:** Non-humanoid, Martian beast.

**Prompt Phrases:** Martian creature, loyal companion, animalistic.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What does Sola look like?

[[SECTION markdown]]

# Sola
**Role:** Warning figure / Associate of Carter

**Status:** Physically Present (referenced/interacts)

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Martian female, associate.

**Uncertainty Note:** Physical appearance is entirely unstated in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH005 Dejah Thoris

aliases: Princess Dejah Thoris

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Captive Princess / Orator

**Status:** Physically Present

**Physical Description:** A princess of the Therns/Martians; delivers a powerful, moving speech.

**Costume/Silhouette:** Captive status implied.

**Prompt Phrases:** Martian princess, regal presence, orator, captive.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH006 Sarkoja

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What is Sarkoja's physical appearance?

[[SECTION markdown]]

# Sarkoja

**Role:** Guard / Council member

**Status:** Physically Present

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Martian, guard, council member.

**Uncertainty Note:** No visual details provided in the text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH007 Lorquas Ptomel

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What does Lorquas Ptomel look like?

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Council Leader

**Status:** Physically Present

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Martian leader, council head.

**Uncertainty Note:** No visual details provided in the text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_warrior_aggressor

canonical_character_id: CH008 Young Warrior

aliases: The aggressor

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only identified by role/action.

clarification_required: true

clarification_reason: No specific physical traits provided.

clarification_question: What are the physical characteristics of the young warrior?

[[SECTION markdown]]

# Young Warrior (Aggressor)
**Role:** Antagonist / Victim of Carter

**Status:** Physically Present (deceased by end of scene)

**Physical Description:** A young Martian warrior; characterized by mirthless laughter.

**Costume/Silhouette:** Warrior attire.

**Prompt Phrases:** Young Martian warrior, aggressive, mirthless.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH009 Tars Tarkas

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What does Tars Tarkas look like?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Thark Warrior / Authority figure

**Status:** Physically Present

**Physical Description:** A Thark warrior moved by Dejah Thoris's speech; questions Carter's mastery of language.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Thark warrior, imposing presence, Martian.

**Uncertainty Note:** No visual details provided in the text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: CH010 Tal Hajus

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as a location/headquarters.

clarification_required: true

clarification_reason: Character identity is unclear (could be a person or place, though context implies a destination/entity).

clarification_question: Is Tal Hajus a person or a location?

[[SECTION markdown]]

# Tal Hajus
**Role:** Referenced entity/destination

**Status:** Referenced

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Martian headquarters, destination.

**Uncertainty Note:** Character is only mentioned as the destination for Carter's imprisonment.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
