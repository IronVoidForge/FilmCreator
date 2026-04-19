# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:57:26.143876+00:00
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

Chapter id: CH006

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

## Story Summary
The protagonist is captured by a bull ape creature while pinned to the ground. Another bull ape attacks with a stone cudgel, intending to brain him. The beast intervenes, fighting the first ape. The second ape arrives and fights the beast, choking it on its throat. The protagonist kills the first ape with the cudgel. He prepares to flee but sees the dying beast appealing for protection. He fights the enraged second bull ape using earthly tactics. Tars Tarkas, Sola, and warriors arrive through the doorway and applaud his bravery. A warrior attempts to shoot the beast; the protagonist stops him by striking up the arm. They return to the plaza with the beast following close at heel.

## Visual Continuity
The bull apes are 10-15 feet tall with close eyes, high lateral ears, and gorilla-like snouts. The fight involves a stone cudgel swinging in an arc. The beast has bulging eyes and blood flowing from its nostrils during the struggle. The protagonist uses earthly tactics (fist to chin, smash to stomach). Tars Tarkas and Sola enter through the doorway of the chamber. The warrior draws an evil looking pistol from its holster. The bullet striking the wooden casing of the window explodes, blowing a hole completely through the wood and masonry.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH006

| Asset ID | Canonical ID | Aliases | Fully Identified | Manual Description Required |
|----------|--------------|---------|------------------|----------------------------|
| protagonist | protagonist | - | Yes | Yes |
| tars_tarkas | tars_tarkas | - | Yes | Yes |
| sola | sola | - | Yes | Yes |
| warrior | warrior | - | Yes | Yes |

*Note: Bull apes are creatures with detailed physical descriptions in visual continuity notes.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter only refers to this character as "the protagonist" without providing any physical description, facial features, or identifying details that would support dependable image generation later.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Protagonist - CH006

**Display Name:** The Protagonist  
**Chapter Role:** Main character, central figure in the conflict

**Physical Presence:** Referenced throughout the chapter as active participant

**Physical Description:** No physical description provided in chapter summary. Character is only identified by role ("protagonist") without facial features, body type, or distinguishing marks visible in the text.

**Costume/Silhouette:** Unknown - no costume details mentioned in chapter summary.

**Continuity-Critical Traits:** Uses "earthly tactics" (fist to chin, smash to stomach) during combat with bull apes. Carries a stone cudgel used to kill first ape and prepare for fleeing.

**Render-Facing Prompt Notes:** Character requires manual description before image generation. Current text only identifies role without physical attributes.

**Uncertainty Notes:** Physical appearance, facial features, age, gender, and costume are completely unknown from chapter materials. Manual description required for dependable later image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter mentions Tars Tarkas by name but provides no physical description, facial features, or identifying details that would support dependable image generation later.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - CH006

**Display Name:** Tars Tarkas  
**Chapter Role:** Arriving figure through doorway, applauds protagonist's bravery

**Physical Presence:** Enters chamber through doorway with Sola and warriors

**Physical Description:** No physical description provided in chapter summary. Only identified by name without facial features or body type visible in text.

**Costume/Silhouette:** Unknown - no costume details mentioned in chapter summary.

**Continuity-Critical Traits:** Arrives through doorway of chamber, applauds protagonist's bravery before warrior attempts to shoot beast.

**Render-Facing Prompt Notes:** Character requires manual description before image generation. Current text only identifies name without physical attributes.

**Uncertainty Notes:** Physical appearance, facial features, age, gender, and costume are completely unknown from chapter materials. Manual description required for dependable later image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter mentions Sola by name but provides no physical description, facial features, or identifying details that would support dependable image generation later.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - CH006

**Display Name:** Sola  
**Chapter Role:** Arriving figure through doorway with Tars Tarkas and warriors

**Physical Presence:** Enters chamber through doorway alongside Tars Tarkas

**Physical Description:** No physical description provided in chapter summary. Only identified by name without facial features or body type visible in text.

**Costume/Silhouette:** Unknown - no costume details mentioned in chapter summary.

**Continuity-Critical Traits:** Arrives through doorway of chamber with Tars Tarkas and warriors, applauds protagonist's bravery.

**Render-Facing Prompt Notes:** Character requires manual description before image generation. Current text only identifies name without physical attributes.

**Uncertainty Notes:** Physical appearance, facial features, age, gender, and costume are completely unknown from chapter materials. Manual description required for dependable later image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warrior
canonical_character_id: warrior
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter mentions "a warrior" but provides no physical description, facial features, or identifying details that would support dependable image generation later.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Warrior - CH006

**Display Name:** A Warrior  
**Chapter Role:** Arriving figure through doorway, attempts to shoot beast, stopped by protagonist

**Physical Presence:** Enters chamber through doorway with Tars Tarkas and Sola

**Physical Description:** No physical description provided in chapter summary. Only identified as "a warrior" without facial features or body type visible in text.

**Costume/Silhouette:** Unknown - no costume details mentioned in chapter summary. Carries an evil-looking pistol from holster.

**Continuity-Critical Traits:** Draws pistol from holster, attempts to shoot beast on protagonist's behalf. Bullet explodes through wooden window casing and masonry when struck by protagonist.

**Render-Facing Prompt Notes:** Character requires manual description before image generation. Current text only identifies role without physical attributes.

**Uncertainty Notes:** Physical appearance, facial features, age, gender, and costume are completely unknown from chapter materials. Manual description required for dependable later image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
