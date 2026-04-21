# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:21:56.447699+00:00
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

Chapter id: CH018

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

**Summary:**
After being rescued from certain death by a group of Warhoon warriors, the protagonist regains consciousness and is prepared for transport to the main Warhoon column. He is treated by an ancient female healer and strapped to a wild thoat to be ridden as a prize for "the great games." Upon reaching the camp, he witnesses a violent power struggle between the young Jeddak Bar Comas and his insubordinate lieutenant, Dak Kova. The two engage in a savage, primal duel that results in the death of Bar Comas and the ascension of Dak Kova to leadership.

The Warhoon horde, characterized by extreme ferocity and frequent ritualistic combat, marches back to their city. The protagonist is imprisoned in a pitch-black dungeon, where he endures prolonged isolation and psychological terror amidst crawling creatures. In a moment of desperate survival, he ambushes his food deliverer with a heavy chain, killing the man and retrieving a set of keys. As he regains his sanity through this act, he is confronted by several pairs of glowing eyes in the darkness that watch him before retreating into the shadows.

**Characters:**
- **The Protagonist:** A human survivor, recovering from wounds and enduring psychological torture in captivity.
- **Dak Kova:** A scarred, ferocious Warhoon warrior/lieutenant who kills Bar Comas to become Jeddak.
- **Bar Comas:** The young, dignified Jeddak of Warhoon, killed in a duel by Dak Kova.
- **The Healer:** An ancient female Warhoon who treats the protagonist's wounds.
- **The Jailer:** A silent emissary who delivers food to the protagonist's cell.

**Settings:**
- **Warhoon Camp:** A mobile military camp characterized by extreme violence and ritualistic combat.
- **City of Warhoon:** The home of the Warhoon horde.
- **The Dungeon:** A pitch-black, terrifying subterranean cell filled with unknown crawling creatures and glowing eyes.

**Key Events:**
- The protagonist is healed and transported via thoat to the Warhoon main body.
- The duel between Bar Comas and Dak Kova, resulting in a brutal death and a change in leadership.
- The long period of isolation and sensory deprivation in the dungeon.
- The protagonist kills his jailer with a chain to obtain keys.
- The appearance of mysterious, glowing eyes watching the protagonist from the dark.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Protagonist](#protagonist)
- [Dak Kova](#dak-kova)
- [Bar Comas](#bar-comas)
- [The Healer](#the-healer)
- [The Jailer](#the-jailer)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Human survivor
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance, age, and specific clothing/gear are not described in this chapter.
clarification_required: true
clarification_reason: Identity and physical traits need establishment for visual consistency.
clarification_question: What is the protagonist's physical build, hair color, eye color, and typical attire?

[[SECTION markdown]]
# Protagonist
**Role:** Central survivor/captive.
**Status:** Physically present.
**Physical Description:** A human male currently recovering from wounds. Specific facial features and body type are unstated in this chapter.
**Costume/Silhouette:** Currently wounded and likely wearing tattered or minimal clothing suitable for a prisoner/survivor.
**Prompt Phrases:** Human survivor, wounded, captive, desperate expression.
**Uncertainty Notes:** No visual details provided regarding ethnicity, age, or specific physical traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: CH018 Dak Kova
aliases: Lieutenant, Jeddak (post-duel)
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dak Kova
**Role:** Antagonist/New Leader.
**Status:** Physically present.
**Physical Description:** A ferocious Warhoon warrior; described as scarred.
**Costume/Silhouette:** Warhoon warrior attire, likely heavy or ritualistic combat gear.
**Prompt Phrases:** Scarred Warhoon warrior, ferocious, aggressive stance, martial leader.
**Uncertainty Notes:** Specifics of the scars and exact Warhoon armor design are not detailed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bar_comas
canonical_character_id: CH018 Bar Comas
aliases: Jeddak (pre-duel)
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Bar Comas
**Role:** Fallen Leader.
**Status:** Physically present (deceased).
**Physical Description:** A young Warhoon leader; described as dignified.
**Costume/Silhouette:** Likely wears the regalia of a Jeddak.
**Prompt Phrases:** Young Warhoon leader, dignified presence, ritualistic combat attire.
**Uncertainty Notes:** Specific visual details of his dignity or regalia are implied rather than explicitly listed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_healer
canonical_character_id: CH018 Healer
aliases: Ancient female healer
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# The Healer
**Role:** Supporting character.
**Status:** Physically present.
**Physical Description:** An ancient female Warhoon.
**Costume/Silhouette:** Likely wearing healer's or elder's garments.
**Prompt Phrases:** Ancient female Warhoon, elderly, healer, wise or weathered appearance.
**Uncertainty Notes:** Specific facial features and clothing textures are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_jailer
canonical_character_id: CH018 Jailer
aliases: Food deliverer
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is a minor figure with no physical description provided.
clarification_required: true
clarification_reason: Needs visual identification to distinguish from other Warhoon.
clarification_question: What does the jailer look like and what is his specific uniform or gear?

[[SECTION markdown]]
# The Jailer
**Role:** Minor antagonist/victim.
**Status:** Physically present (deceased).
**Physical Description:** A member of the Warhoon horde; no specific features mentioned.
**Costume/Silhouette:** Likely standard Warhoon soldier or guard attire.
**Prompt Phrases:** Warhoon guard, silent, food deliverer, prisoner handler.
**Uncertainty Notes:** No physical characteristics are provided in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
