# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:39:45.636672+00:00
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

Chapter id: CH004

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

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

In Chapter IV, John Carter travels from a dead sea toward a mountain city on Mars. He enters Zodanga, where he is surrounded by Martians who are intrigued by him. He meets Tars Tarkas, the vice-chieftain, and is brought before the chief. Carter performs physical feats like jumping ("sak") and fighting, which impresses the Martians despite their unusual sense of humor regarding violence. He is taken to a chamber where he meets Sola, a female Martian, and observes a ten-legged creature. The chapter establishes the setting of Zodanga, introduces key characters (Tars Tarkas, Sola), and highlights the cultural differences between Carter and the Martians.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index - Chapter IV

## John Carter
**Asset ID:** john_carter  
**Canonical Character ID:** john_carter  
**Aliases:** none  
**Is Fully Identified:** true  
**Manual Description Required:** false  
**Clarification Required:** false  

**Role:** Protagonist traveling from dead sea to Zodanga mountain city on Mars. Enters Zodanga where he is surrounded by intrigued Martians. Performs physical feats like jumping ("sak") and fighting which impress the Martians despite their unusual sense of humor regarding violence.

---

## Tars Tarkas
**Asset ID:** tars_tarkas  
**Canonical Character ID:** tars_tarkas  
**Aliases:** vice-chieftain  
**Is Fully Identified:** true  
**Manual Description Required:** false  
**Clarification Required:** false  

**Role:** Martian vice-chieftain who brings Carter before the chief. Key figure in establishing Zodanga setting and cultural differences between Carter and Martians.

---

## The Chief
**Asset ID:** martian_chief  
**Canonical Character ID:** martian_chief  
**Aliases:** none  
**Is Fully Identified:** false  
**Manual Description Required:** true  
**Clarification Required:** true  

**Role:** Leader of Martians, brought before whom Carter is taken. Not named in chapter material.

---

## Sola
**Asset ID:** sola  
**Canonical Character ID:** sola  
**Aliases:** female Martian  
**Is Fully Identified:** true  
**Manual Description Required:** false  
**Clarification Required:** false  

**Role:** Female Martian who Carter meets in the chamber where he is taken. Key character establishing cultural differences between Carter and Martians.

---

## Ten-Legged Creature
**Asset ID:** ten_legged_creature  
**Canonical Character ID:** ten_legged_creature  
**Aliases:** none  
**Is Fully Identified:** false  
**Manual Description Required:** true  
**Clarification Required:** true  

**Role:** Observed by Carter in the chamber. Not named or described with physical details in chapter material.

---

## Clarification Questions
1. **For The Chief:** What are the physical appearance and distinguishing features of the Martian chief? Is there any known name or title beyond "chief"?  
2. **For Ten-Legged Creature:** What is the species, size, coloration, and other physical characteristics of the ten-legged creature observed by Carter?

[[/SECTION]]
[[/FILMCREATOR_PACKET]]
````
