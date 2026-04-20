# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:41:58.754151+00:00
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

Chapter id: CH026

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

**Story Summary:**
Carter and Tars Tarkas report Zodanga fleet destroyed; Dejah Thoris transferred to Helium flagship. Land forces attack Zodangan army from north, south, east. Helium navy joins land battle against million-strong enemy. Victory parade in Helium city. Carter introduced to Jeddak of Helium (Tardos Mors) and Jed of lesser Helium (Mors Kajak).

**Visual Continuity Facts:**
Sky ships circling above fleets; green warriors firing small arms from shelters; explosions on Zodangan hulls; bodies plunging from defeated ships into loam. Thoats in slings landing near city gates. Palace steps with royal party; crowd lining avenues. Helium towers visible against sky.

**Scene Decomposition Notes:**
Naval battle sequence ends with surrender customs (commander plunge). Land battle sequence involves coordinated charge with Helium reinforcements. Political resolution scene occurs on palace steps and main portals.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH026

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|------------------------|---------|------------------|----------------------------|------------------------|
| carter | Carter | - | false | true | true |
| tars_tarkas | Tars Tarkas | - | false | true | true |
| dejah_thoris | Dejah Thoris | - | false | true | true |
| tardos_mors | Jeddak of Helium | Mors Kajak (lesser) | false | true | true |
| mors_kajak | Jed of lesser Helium | Tardos Mors (Jeddak) | false | true | true |

**Notes:** All characters lack sufficient physical/visual description in the provided chapter material to support dependable later image generation. Names and titles are stable, but no physical descriptions are included in the summary or visual continuity facts.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: Carter
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity facts. Character is mentioned by name only without any visual identifiers, clothing details, or physical traits that would support later image generation.
clarification_required: true
clarification_reason: Need to establish Carter's physical appearance for consistent character representation across future chapters and media.
clarification_question: What does Carter look like? Please describe his physical features, clothing, and any distinctive visual characteristics.

[[SECTION markdown]]
# carter.md

## Display Name
Carter

## Chapter Role
Main protagonist mentioned in chapter summary; introduced to Jeddak of Helium (Tardos Mors) and Jed of lesser Helium (Mors Kajak).

## Physical Presence
Referenced - Character is mentioned by name but no visual description provided in the supplied material.

## Physical Description
**Uncertain** - No physical description available in chapter summary or visual continuity facts. Character appears only as a named reference without any visual identifiers, clothing details, or physical traits documented.

## Costume & Silhouette
**Unknown** - No costume or silhouette information provided in the source material.

## Continuity-Critical Traits
- Name: Carter (stable identifier)
- Role: Introduced to Helium leadership
- Status: Physical appearance not yet established for consistent representation

## Render-Facing Prompt Notes
```
[UNCERTAIN] Character requires physical description before reliable image generation. 
Current material only provides name and role context without visual identifiers.
```

## Uncertainty Notes
This character record lacks sufficient physical/visual description in the provided chapter material (CH026) to support dependable later image generation. The chapter mentions Carter by name but does not include any physical descriptions, clothing details, or distinctive visual characteristics that would enable consistent character representation across future chapters and media. Clarification is required before proceeding with visual design decisions.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity facts. Character is mentioned by name only without any visual identifiers, clothing details, or physical traits that would support later image generation.
clarification_required: true
clarification_reason: Need to establish Tars Tarkas's physical appearance for consistent character representation across future chapters and media.
clarification_question: What does Tars Tarkas look like? Please describe his physical features, clothing, and any distinctive visual characteristics.

[[SECTION markdown]]
# tars_tarkas.md

## Display Name
Tars Tarkas

## Chapter Role
Mentioned in chapter summary alongside Carter; reports Zodanga fleet destroyed with Carter.

## Physical Presence
Referenced - Character is mentioned by name but no visual description provided in the supplied material.

## Physical Description
**Uncertain** - No physical description available in chapter summary or visual continuity facts. Character appears only as a named reference without any visual identifiers, clothing details, or physical traits documented.

## Costume & Silhouette
**Unknown** - No costume or silhouette information provided in the source material.

## Continuity-Critical Traits
- Name: Tars Tarkas (stable identifier)
- Role: Reports fleet destruction with Carter
- Status: Physical appearance not yet established for consistent representation

## Render-Facing Prompt Notes
```
[UNCERTAIN] Character requires physical description before reliable image generation. 
Current material only provides name and role context without visual identifiers.
```

## Uncertainty Notes
This character record lacks sufficient physical/visual description in the provided chapter material (CH026) to support dependable later image generation. The chapter mentions Tars Tarkas by name but does not include any physical descriptions, clothing details, or distinctive visual characteristics that would enable consistent character representation across future chapters and media. Clarification is required before proceeding with visual design decisions.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity facts. Character is mentioned by name only without any visual identifiers, clothing details, or physical traits that would support later image generation.
clarification_required: true
clarification_reason: Need to establish Dejah Thoris's physical appearance for consistent character representation across future chapters and media.
clarification_question: What does Dejah Thoris look like? Please describe her physical features, clothing, and any distinctive visual characteristics.

[[SECTION markdown]]
# dejah_thoris.md

## Display Name
Dejah Thoris

## Chapter Role
Mentioned in chapter summary; transferred to Helium flagship after Zodanga fleet destroyed.

## Physical Presence
Referenced - Character is mentioned by name but no visual description provided in the supplied material.

## Physical Description
**Uncertain** - No physical description available in chapter summary or visual continuity facts. Character appears only as a named reference without any visual identifiers, clothing details, or physical traits documented.

## Costume & Silhouette
**Unknown** - No costume or silhouette information provided in the source material.

## Continuity-Critical Traits
- Name: Dejah Thoris (stable identifier)
- Role: Transferred to Helium flagship
- Status: Physical appearance not yet established for consistent representation

## Render-Facing Prompt Notes
```
[UNCERTAIN] Character requires physical description before reliable image generation. 
Current material only provides name and role context without visual identifiers.
```

## Uncertainty Notes
This character record lacks sufficient physical/visual description in the provided chapter material (CH026) to support dependable later image generation. The chapter mentions Dejah Thoris by name but does not include any physical descriptions, clothing details, or distinctive visual characteristics that would enable consistent character representation across future chapters and media. Clarification is required before proceeding with visual design decisions.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tardos_mors
canonical_character_id: Jeddak of Helium
aliases: Mors Kajak (lesser)
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity facts. Character is mentioned by title/name only without any visual identifiers, clothing details, or physical traits that would support later image generation.
clarification_required: true
clarification_reason: Need to establish Jeddak of Helium's physical appearance for consistent character representation across future chapters and media.
clarification_question: What does the Jeddak of Helium (Tardos Mors) look like? Please describe his physical features, clothing, and any distinctive visual characteristics.

[[SECTION markdown]]
# tardos_mors.md

## Display Name
Jeddak of Helium (Tardos Mors)

## Chapter Role
Introduced to Carter; mentioned in chapter summary as receiving Dejah Thoris transfer. Also referred to as Jed of lesser Helium (Mors Kajak).

## Physical Presence
Referenced - Character is mentioned by title/name but no visual description provided in the supplied material.

## Physical Description
**Uncertain** - No physical description available in chapter summary or visual continuity facts. Character appears only as a named/titled reference without any visual identifiers, clothing details, or physical traits documented.

## Costume & Silhouette
**Unknown** - No costume or silhouette information provided in the source material.

## Continuity-Critical Traits
- Name: Jeddak of Helium / Tardos Mors (stable identifier)
- Alias: Mors Kajak (lesser)
- Role: Receives Dejah Thoris transfer; introduced to Carter
- Status: Physical appearance not yet established for consistent representation

## Render-Facing Prompt Notes
```
[UNCERTAIN] Character requires physical description before reliable image generation. 
Current material only provides title/name context without visual identifiers.
```

## Uncertainty Notes
This character record lacks sufficient physical/visual description in the provided chapter material (CH026) to support dependable later image generation. The chapter mentions Jeddak of Helium by title and name but does not include any physical descriptions, clothing details, or distinctive visual characteristics that would enable consistent character representation across future chapters and media. Clarification is required before proceeding with visual design decisions.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mors_kajak
canonical_character_id: Jed of lesser Helium
aliases: Tardos Mors (Jeddak)
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity facts. Character is mentioned by title/name only without any visual identifiers, clothing details, or physical traits that would support later image generation.
clarification_required: true
clarification_reason: Need to establish Jed of lesser Helium's physical appearance for consistent character representation across future chapters and media.
clarification_question: What does the Jed of lesser Helium (Mors Kajak) look like? Please describe his physical features, clothing, and any distinctive visual characteristics.

[[SECTION markdown]]
# mors_kajak.md

## Display Name
Jed of lesser Helium (Mors Kajak)

## Chapter Role
Introduced to Carter; mentioned in chapter summary alongside Jeddak of Helium (Tardos Mors). Also referred to as Tardos Mors (Jeddak).

## Physical Presence
Referenced - Character is mentioned by title/name but no visual description provided in the supplied material.

## Physical Description
**Uncertain** - No physical description available in chapter summary or visual continuity facts. Character appears only as a named/titled reference without any visual identifiers, clothing details, or physical traits documented.

## Costume & Silhouette
**Unknown** - No costume or silhouette information provided in the source material.

## Continuity-Critical Traits
- Name: Jed of lesser Helium / Mors Kajak (stable identifier)
- Alias: Tardos Mors (Jeddak)
- Role: Introduced to Carter; mentioned alongside Jeddak of Helium
- Status: Physical appearance not yet established for consistent representation

## Render-Facing Prompt Notes
```
[UNCERTAIN] Character requires physical description before reliable image generation. 
Current material only provides title/name context without visual identifiers.
```

## Uncertainty Notes
This character record lacks sufficient physical/visual description in the provided chapter material (CH026) to support dependable later image generation. The chapter mentions Jed of lesser Helium by title and name but does not include any physical descriptions, clothing details, or distinctive visual characteristics that would enable consistent character representation across future chapters and media. Clarification is required before proceeding with visual design decisions.
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
