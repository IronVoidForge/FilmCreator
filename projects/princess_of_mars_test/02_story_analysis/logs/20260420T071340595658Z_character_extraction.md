# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:13:40.595658+00:00
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

Chapter id: CH008

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

**Chapter Title:** CHAPTER VIII / A FAIR CAPTIVE FROM THE SKY

**Summary of Events:**
Following the incubator ceremony, the procession returns to the Green Martian city. Upon entering the open ground, orders are given for an immediate retreat as a massive enemy air fleet (twenty gray ships) approaches from the hills. The Green Martians fire a volley from their buildings, initiating a battle. The enemy fleet responds with gunfire, but the initial volley catches them off guard. The Green Martians demonstrate deadly accuracy, targeting specific points on the enemy vessels (guns, officers, crew). After twenty minutes, the fleet retreats, damaged and limping. One ship is disabled and captured by the Green Martians. The warriors loot the vessel of arms, food, and valuables, then set it ablaze before towing it away.

**Character Interactions:**
The Narrator observes the battle from a window in a building. Woola follows close at heel. Sola rushes to the Narrator upon return. During the aftermath, the Narrator sees a prisoner being dragged into a building by Green Martian females. The prisoner is revealed to be a slender, girlish figure resembling an earthly woman with coal-black hair and reddish-copper skin. She makes eye contact with the Narrator, signaling hope which fades into dejection when he fails to respond.

**Settings:**
- **Green Martian City:** Buildings, upper floors, windows, plaza.
- **Valley/Hills:** Where the enemy fleet approaches and retreats.
- **Martian Plains:** Where the battle takes place.

**Key Takeaways for Scene Extraction:**
- The arrival of the enemy air fleet marks a significant escalation in conflict.
- The capture of the ship introduces a new element: the human captive.
- The emotional connection between the Narrator and the Earth girl is established through visual contact and unspoken signals.
- The setting shifts from active battle to the aftermath, focusing on the prisoner's fate.
````

## Raw Response
````text

````
