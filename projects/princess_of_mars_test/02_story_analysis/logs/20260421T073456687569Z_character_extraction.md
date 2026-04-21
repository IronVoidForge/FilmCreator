# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:34:56.687569+00:00
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

**Setting:**
The journey begins on the cultivated agricultural tracts between the poles and Zodanga, moving into the vast, walled city of Zodanga, characterized by high-raised residences and a central square plaza.

**Events:**
* **Travel Observations:** John Carter travels toward Zodanga, observing Martian agricultural methods involving underground water conduits and highly refined flora and fauna.
* **Intelligence Gathering:** At a farmhouse, Carter speaks with a Zodangan noble who reveals that the war between Helium and Zodanga is unpopular and that Dejah Thoris is rumored to be dead following an encounter with Tharks and Warhoons.
* **Arrival at Zodanga:** Carter arrives at the gates of Zodanga. He makes the difficult decision to part ways with his loyal companion, the dog Woola, to ensure the dog's safety during his infiltration of the city.
* **Reunion with Kantos Kan:** In the central plaza, Carter reunites with Kantos Kan, a Red Martian ally. Kantos Kan reveals he is working as an air scout to find Dejah Thoris, who is reportedly being held by Prince Sab Than.
* **Infiltration:** Using a ruse facilitated by Kantos Kan, Carter enrolls in the Zodangan air-scout squadron. He spends several days learning Martian aviation and the mechanics of eighth-ray propulsion.
* **Combat and Heroism:** During a solo flight, Carter discovers a Zodangan scout (a cousin of the Jeddak) being pursued by three Green Martian warriors. Carter intervenes, killing the warriors and saving the scout.
* **Recognition:** Carter and the scout return to Zodanga. During a massive military ceremony in the plaza, Carter is publicly honored by Jeddak Than Kosis for his bravery. He is appointed a *padwar* of The Guards and granted quarters in the palace.

**Characters:**
* **John Carter:** The protagonist; an Earthman with superhuman abilities who successfully infiltrates the Zodangan military.
* **Woola:** Carter's loyal, non-domesticated Martian hound (parted with at the city gates).
* **Kantos Kan:** A Red Martian ally and air scout who assists Carter's infiltration.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **The Zodangan Scout:** A cousin of Than Kosis, rescued by Carter from Green Martians.

**Key Concepts:**
* **Eighth Ray Propulsion:** A Martian scientific discovery involving the repulsion of gravity used to power airships.
* **Zodangan Social Structure:** High-raised buildings to prevent assassination and a lack of common thievery.
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
- [Zodangan Scout](#zodangan-scout)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Carter, Earthman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist; Earthman with superhuman abilities.
**Presence:** Physically present.
**Description:** An Earthman capable of superhuman feats (implied strength/agility). Currently operating as an infiltrator within the Zodangan air-scout squadron.
**Prompt Phrases:** Earthman, superhuman strength, Martian aviator, padwar.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: Martian hound, dog
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Loyal companion.
**Presence:** Referenced (parted with at the city gates).
**Description:** A non-domesticated Martian hound.
**Prompt Phrases:** Martian hound, loyal beast, large canine.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Kantos Kan
**Role:** Red Martian ally and air scout.
**Presence:** Physically present.
**Description:** A Red Martian serving as an air scout to locate Dejah Thoris.
**Prompt Phrases:** Red Martian, air scout, ally.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: Than Kosis
aliases: Jeddak, Ruler of Zodanga
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Than Kosis
**Role:** Jeddak (Ruler) of Zodanga.
**Presence:** Physically present.
**Description:** The high ruler of the city of Zodanga; performs military ceremonies and honors warriors.
**Prompt Phrases:** Jeddak, Martian ruler, Zodangan leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zodangan_scout
canonical_character_id: Zodangan Scout
aliases: Cousin of the Jeddak
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description provided beyond his relation to the Jeddak.
clarification_required: true
clarification_reason: Physical appearance is unknown.
clarification_question: What are the specific physical features of the Zodangan scout?
[[SECTION markdown]]
# Zodangan Scout
**Role:** Rescued noble/scout.
**Presence:** Physically present.
**Description:** A member of the Zodangan military and a cousin to Jeddak Than Kosis. He was rescued from Green Martian warriors during a solo flight.
**Prompt Phrases:** Zodangan scout, royal relative, Martian aviator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
