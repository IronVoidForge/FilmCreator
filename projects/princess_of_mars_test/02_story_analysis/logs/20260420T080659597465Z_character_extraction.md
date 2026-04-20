# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:06:59.597465+00:00
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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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

# Chapter CH020 Summary

## Overview
John Carter waits for Kantos Kan but leaves towards the waterway after two days. He wanders for two weeks, surviving on vegetable milk and protected by telepathy from beasts. He reunites with Woola, who has left Dejah Thoris (presumed dead). They find the Atmosphere Factory. Carter enters via telepathic means and meets the old guardian of the plant. He learns about the ninth ray and the machinery sustaining Mars' atmosphere. The guardian intends to kill him but Carter escapes using telepathy on the locks. He reaches a farm near Zodanga, where red Martians help him rest, dye his skin, and provide resources, advising him to seek military employment in Zodanga to prove his trustworthiness before attempting to reach Helium (which is at war).

## Key Characters
- **John Carter**: The protagonist, currently a Red Martian in appearance but of Barsoomian origin. He possesses telepathic abilities that allow him to read thoughts and manipulate locks.
- **Woola**: Carter's calot (companion), who has left Dejah Thoris due to her presumed death. He is starving and loyal.
- **The Old Guardian**: A dried-up Martian man wearing a gold diadem with the ninth ray stone. He guards the Atmosphere Factory and belongs to all Barsoom. He intends to kill Carter for the "best good of Barsoom."
- **Red Martians (Farmers)**: The inhabitants of the farm near Zodanga who assist Carter after his escape from the factory.

## Key Settings
- **The Atmosphere Factory**: A massive building with walls 150 feet thick and a roof guarded by glass. It contains machinery to produce artificial atmosphere using the ninth ray.
- **The Barsoomian Landscape**: Wastelands, hills, and waterways where Carter wanders for weeks.
- **Zodanga Farm**: A location near Zodanga with concrete buildings raised on metal shafts, inhabited by government officers and their families.

## Plot Points
1.  **Waiting and Departure**: Carter waits for Kantos Kan for two days without success before heading towards the nearest waterway.
2.  **The Wandering**: Carter survives two weeks of wandering, attacked by wild beasts but saved by telepathic warnings. He meets Woola again.
3.  **Discovery of the Factory**: Carter finds the Atmosphere Factory and enters via a speaking tube/telepathic door mechanism.
4.  **Meeting the Guardian**: Carter is questioned by an invisible host and meets the old man who explains the ninth ray and the atmosphere production process.
5.  **The Threat**: The guardian reveals he plans to kill Carter after checking the pumps, fearing for Barsoom's safety.
6.  **Escape**: Carter uses telepathy to unlock the doors and escapes with Woola.
7.  **Recovery at Zodanga**: Carter reaches a farm near Zodanga where red Martians help him rest, dye his skin to match their race, and provide money and a bull-thoat.
8.  **Advice**: The Martians advise Carter to seek military employment in Zodanga to prove his trustworthiness before attempting to reach Helium.
````

## Raw Response
````text

````
