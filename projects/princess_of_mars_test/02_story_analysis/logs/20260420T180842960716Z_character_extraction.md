# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:08:42.960716+00:00
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

Chapter id: CH020

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

**Events:**
After a failed attempt to meet Kantos Kan, the protagonist embarks on a two-week trek northwest through the Martian wilderness. During this journey, he survives on vegetable milk and narrowly avoids several beast attacks, one of which is only thwarted by the intervention of his emaciated calot, Woola. On the fifteenth day, the protagonist discovers a massive, four-square-mile atmosphere factory. After gaining entry through automated doors, he is hosted by an invisible entity and meets a withered old man who has guarded the facility for eight hundred years. Through telepathy, the protagonist learns that the plant uses a "ninth ray" to generate life-sustaining air, which is then distributed via radium pumps to five principal centers across Mars.

The situation turns dangerous when the protagonist senses the old man's murderous intent; the guardian plans to kill him to protect the factory's secrets. Using his telepathic abilities to manipulate the facility's thought-wave locks, the protagonist manages to escape with Woola. While traveling toward the central turnpike, he is intercepted by hospitable Red Martians who take him into their elevated home. To assist his journey to Zodanga, the Red Martians provide him with a disguise—anointing his skin with reddish oil and cutting his hair in the local fashion—and supply him with Zodangan money and a bullthoat. He departs for Zodanga following their advice that military service is the most effective way to gain status and trust.

**Characters:**
* **The Protagonist:** An Earthman with telepathic powers who is recognized as biologically distinct from Barsoomians; he is currently exhausted and starving.
* **Woola:** A faithful, though seemingly emaciated, calot who protects the protagonist from wild beasts.
* **The Invisible Host:** An entity within the factory that can see through the protagonist's body but cannot read his thoughts.
* **The Old Man:** A mummy-like guardian of the atmosphere pumps for eight centuries; he wears a nine-rayed diadem and attempts to kill the protagonist to protect the plant's secrets.
* **Red Martians:** A hospitable group of inhabitants who provide the protagonist with local disguises, currency, and transport.

**Settings:**
* **The Martian Wilderness:** A dangerous landscape filled with strange beasts and vegetation that yields vegetable milk.
* **The Atmosphere Factory:** A massive, highly secure concrete facility containing automated doors and machinery used to generate the Martian atmosphere via the ninth ray.
* **Red Martian Home:** A structure raised on a metal shaft for safety, reflecting local social structures and customs.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH020

- [Protagonist](#protagonist)
- [Woola](#woola)
- [The Invisible Host](#the-invisible-host)
- [The Old Man](#the-old-man)
- [Red Martians](#red-martians)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH020 Protagonist
aliases: Earthman
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance, height, build, and facial features are not described in this chapter.
clarification_required: true
clarification_reason: Needs specific physical descriptors for consistent rendering.
clarification_question: What is the protagonist's hair color, eye color, build, and approximate age?

[[SECTION markdown]]
# Protagonist
**Role:** Main Character / Traveler

**Status:** Physically Present (Exhausted/Starving)

**Physical Description:** 
An Earthman. Currently appears exhausted and starving after a two-week trek. He is biologically distinct from the local Barsoomians.

**Costume & Silhouette:** 
No specific clothing details provided in this chapter, though he receives a disguise (reddish oil on skin and local hair cutting) from the Red Martians toward the end of the chapter.

**Descriptive Noun Phrases:** 
Starving Earthman, telepathic traveler, disheveled wanderer.

**Uncertainty Notes:** 
Complete lack of facial or bodily physical characteristics.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH020 Woola
aliases: Calot
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Companion / Protector

**Status:** Physically Present

**Physical Description:** 
An emaciated calot.

**Costume & Silhouette:** 
A Martian beast/animal companion; currently thin and bony due to the trek.

**Descriptive Noun Phrases:** 
Emaciated calot, faithful Martian beast, protective animal companion.

**Uncertainty Notes:** 
Specific species morphology (size, color, number of limbs) is not detailed in this chapter beyond being a "calot."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: invisible_host
canonical_character_id: CH020 Invisible Host
aliases: Entity
is_fully_identified: false
manual_description_required: true
manual_description_reason: The character is explicitly described as an invisible entity.
clarification_required: true
clarification_reason: Nature of the entity's presence/form.
clarification_question: Does the invisible host have a physical presence that displaces air, or is it purely energy/telepathic?

[[SECTION markdown]]
# The Invisible Host
**Role:** Facility Host

**Status:** Physically Present (Invisible)

**Physical Description:** 
An entity that is invisible to the eye but capable of seeing through the protagonist's body. It cannot read thoughts.

**Costume & Silhouette:** 
N/A (Invisible).

**Descriptive Noun Phrases:** 
Invisible presence, unseen host, transparent entity.

**Uncertainty Notes:** 
Character is defined by their invisibility; no visual rendering is possible without clarification of "presence."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: old_man
canonical_character_id: CH020 Old Man
aliases: Guardian
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# The Old Man
**Role:** Antagonist / Factory Guardian

**Status:** Physically Present

**Physical Description:** 
A withered, mummy-like old man. He has guarded the facility for eight hundred years.

**Costume & Silhouette:** 
Wears a nine-rayed diadem.

**Descriptive Noun Phrases:** 
Mummy-like guardian, withered old man, ancient factory keeper.

**Uncertainty Notes:** 
None; description is consistent with a long-term hermit/guardian.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: red_martians
canonical_character_id: CH020 Red Martians
aliases: Hospitable Martians
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group identity is established, but individual physical traits are not detailed.
clarification_required: true
clarification_reason: Need specific visual markers for the "Red Martian" race.
clarification_question: What are the defining physical characteristics of a Red Martian (skin tone, height, facial features)?

[[SECTION markdown]]
# Red Martians
**Role:** Supporting Group / Guides

**Status:** Physically Present

**Physical Description:** 
A group of hospitable inhabitants of Mars. They use reddish oil to disguise others.

**Costume & Silhouette:** 
Local fashion involves specific hair cutting styles and the use of reddish oils.

**Descriptive Noun Phrases:** 
Hospitable Red Martians, local Martian dwellers, elevated home inhabitants.

**Uncertainty Notes:** 
Specific biological traits are unknown beyond their group name.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
