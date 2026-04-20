# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:39:20.203388+00:00
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

Chapter id: CH003

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

In Chapter III, titled "My Advent on Mars," the narrator wakes up in a strange landscape on Mars, experiencing significantly lower gravity that causes him to hop instead of walk. He discovers a glass enclosure containing large eggs hatching into six-legged creatures. His exploration is interrupted by a group of Martian warriors on mounts who nearly attack him with spears. Through a display of superhuman agility, the narrator escapes their immediate grasp, impressing them with his ability to jump great distances. A leader approaches unarmed and offers an armlet as a peace gesture. The narrator accepts it, and they ride away together towards the hills, marking the beginning of his integration into Martian society.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index - Chapter III: My Advent on Mars

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Manual Description Reason | Clarification Required | Clarification Reason | Clarification Question |
|----------|------------------------|---------|------------------|----------------------------|---------------------------|------------------------|----------------------|------------------------|
| narrator_01 | The Narrator | Protagonist, First Person | true | false | - | false | - | - |
| six_legged_creatures_01 | Six-Legged Creatures | Egg Hatchlings, Martian Beasts | false | true | Insufficient physical description for dependable image generation; only mentioned as hatching from eggs with six legs | false | - | - |
| martian_warriors_01 | Martian Warriors | Martians, Warrior Group | false | true | Group reference without individual visual details; mounted warriors with spears but no specific costume or silhouette information | false | - | - |
| martian_leader_01 | Martian Leader | Leader, Armlet Giver | false | true | Individual referenced as approaching unarmed with armlet gesture; lacks physical description, costume, or continuity-critical traits | false | - | - |

[[/SECTION]]
[[FILMCREATOR_PACKET]]
````
