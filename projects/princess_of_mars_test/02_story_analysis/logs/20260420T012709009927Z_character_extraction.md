# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:27:09.009927+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH018

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



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

The chapter opens with the protagonist regaining consciousness in a small room filled with sleeping silks and furs, attended by Dak Kova, the jed who captured him. Dak Kova reports to Bar Comas, the young jeddak of Warhoon, noting the tension between them. A brutal battle ensues where both warriors die; Dak Kova kills Bar Comas and assumes the title of Jeddak. The expedition is abandoned due to injuries, and the ten thousand warriors return to Warhoon city. The protagonist is chained in a dark dungeon. While Dak Kova brings food, the protagonist kills him with a chain and finds keys on his throat. Finally, six pairs of gleaming eyes approach in the darkness before retreating.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH018

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|----------------------|---------|------------------|----------------------------|------------------------|
| dak_kova | Dak Kova | Dak, Jeddak | Yes | Yes | No |
| bar_comas | Bar Comas | Jeddak of Warhoon | Yes | Yes | No |
| protagonist | Protagonist | - | No | Yes | Yes |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: Dak Kova
aliases: Dak, Jeddak
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical or visual description in chapter summary. Only role-based identifiers provided (jed who captured protagonist, brings food, killed by protagonist). No appearance details, clothing, or distinguishing features documented.
clarification_required: false
clarification_reason: Character is clearly identified with stable name and role across chapter events.
clarification_question: 

[[SECTION markdown]]
# Dak Kova - CH018

**Display Name:** Dak Kova  
**Chapter Role:** Jed who captured protagonist, later assumes title of Jeddak after killing Bar Comas  

**Physical Presence:** Referenced throughout chapter (attends protagonist in room, reports to Bar Comas, brings food, killed by protagonist)  

**Physical Description:** Unknown - insufficient detail in source material for dependable image generation. No appearance, clothing, or distinguishing features documented in chapter summary.  

**Costume/Silhouette:** Unknown - no costume details provided.  

**Continuity-Critical Traits:** Jed of Warhoon, killer of Bar Comas, assumed title of Jeddak, food-bringer to protagonist, killed by protagonist with chain.  

**Uncertainty Notes:** Manual description required due to lack of physical/visual identifiers in source. Character role is stable but appearance details are missing.  

**Render-Facing Prompt Noun Phrases:** jed of Warhoon, killer of Bar Comas, assumed title of Jeddak, food-bringer, killed by protagonist with chain

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bar_comas
canonical_character_id: Bar Comas
aliases: Jeddak of Warhoon
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical or visual description in chapter summary. Only role-based identifiers provided (young jeddak of Warhoon, tension with Dak Kova). No appearance details, clothing, or distinguishing features documented.
clarification_required: false
clarification_reason: Character is clearly identified with stable name and role across chapter events.
clarification_question: 

[[SECTION markdown]]
# Bar Comas - CH018

**Display Name:** Bar Comas  
**Chapter Role:** Young jeddak of Warhoon, killed by Dak Kova  

**Physical Presence:** Referenced throughout chapter (tension with Dak Kova, killed by Dak Kova)  

**Physical Description:** Unknown - insufficient detail in source material for dependable image generation. No appearance, clothing, or distinguishing features documented in chapter summary.  

**Costume/Silhouette:** Unknown - no costume details provided.  

**Continuity-Critical Traits:** Young jeddak of Warhoon, killed by Dak Kova, assumed title of Jeddak after death (by Dak Kova), ten thousand warriors return to Warhoon city.  

**Uncertainty Notes:** Manual description required due to lack of physical/visual identifiers in source. Character role is stable but appearance details are missing.  

**Render-Facing Prompt Noun Phrases:** young jeddak of Warhoon, killed by Dak Kova, assumed title of Jeddak after death

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: Protagonist
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical or visual description in chapter summary. No stable identification provided (no name, no appearance details). Only role-based identifiers (regaining consciousness, chained in dungeon, kills Dak Kova, finds keys on throat).
clarification_required: true
clarification_reason: Character might already exist under another name or is too weakly identified for dependable later image generation. No stable physical or visual description supports later render-facing prompt writing.
clarification_question: What is the protagonist's canonical name and what are their key physical characteristics (appearance, clothing, distinguishing features)?

[[SECTION markdown]]
# Protagonist - CH018

**Display Name:** Protagonist  
**Chapter Role:** Main character regaining consciousness in small room, chained in dungeon  

**Physical Presence:** Referenced throughout chapter (regains consciousness in small room, chained in dark dungeon, kills Dak Kova with chain, finds keys on throat)  

**Physical Description:** Unknown - insufficient detail in source material for dependable image generation. No appearance, clothing, or distinguishing features documented in chapter summary.  

**Costume/Silhouette:** Unknown - no costume details provided.  

**Continuity-Critical Traits:** Regains consciousness in small room filled with sleeping silks and furs, chained in dark dungeon, kills Dak Kova with chain, finds keys on throat, six pairs of gleaming eyes approach before retreating.  

**Uncertainty Notes:** Manual description required due to lack of physical/visual identifiers in source. Character is not fully identified (no stable name or appearance). Clarification required for dependable later image generation.  

**Render-Facing Prompt Noun Phrases:** regains consciousness in small room, chained in dark dungeon, kills Dak Kova with chain, finds keys on throat, six pairs of gleaming eyes approach

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
