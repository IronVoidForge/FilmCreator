# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T22:12:44.851843+00:00
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

Chapter id: CH001

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

## Story Summary (CH001)

- **Opening:** Carter reflects on his agelessness and fear of death despite having died twice. He decides to write a chronicle of his life and death.
- **Backstory:** Post-Civil War veteran with Confederate funds. Carter and Powell locate a gold vein in Arizona winter 1865.
- **Inciting Incident:** Powell leaves to buy machinery; Carter guards the claim.
- **Rising Action:** Powell's party is ambushed by Apaches. Carter discovers tracks of pursuing horsemen.
- **Climax:** Carter chases the attackers. Finds Powell dead on a plateau surrounded by tepees.
- **Falling Action:** Carter shoots at warriors, escapes pursuit into a defile leading to a cave.
- **Resolution:** Enters cave entrance. Collapses from fatigue and excitement.

## Visual Continuity Facts (CH001)

- **Environment:** Arizona hills, clear mornings, moonlight nights. Terrain includes mountainside, valley, plateau, gorge, pass.
- **Lighting:** Moonlight scenes during chase; daylight at cave entry.
- **Tracks:** Powell's tracks vs. Apache pony tracks (unshod ponies).
- **Camp:** White with Indian tepees; half a thousand warriors clustered around center object.
- **Cave Interior:** Large chamber (~100ft diameter, 30-40ft height), smooth floor, dense shadow at back.
- **Weapons:** Colt revolvers (two), carbine, cartridge belts.
- **Mounts:** Saddle horse (poor beast), burros (Powell's).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index (CH001)

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|------------------------|---------|------------------|------------------------------|------------------------|
| carter | Carter | - | false | true | true |
| powell | Powell | - | false | true | true |
| apache_warriors | Apache Warriors | Apaches, Indians, warriors | false | true | true |

**Notes:** All characters lack physical/visual description in source material. Group references (Apache Warriors) are insufficiently identified for individual image generation.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: Carter
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description, clothing, or visual traits provided in chapter summary or visual continuity facts. Source material only describes agelessness and death history, not appearance.
clarification_required: true
clarification_reason: Character is central to narrative but lacks stable identification for image generation. Need physical description, distinguishing features, and visual continuity notes.
clarification_question: What are Carter's physical characteristics (age appearance, build, facial features, hair, eyes)? What clothing or gear does he wear? Are there any distinctive marks or accessories?

[[SECTION markdown]]
# carter.md

## Display Name
Carter

## Chapter Role
First-person narrator; protagonist of chronicle. Reflects on agelessness and fear of death despite having died twice. Writes life/death chronicle.

## Physical Presence
Referenced (narrator). Physically present in narrative perspective.

## Supported Physical Description
**None provided.** Source material contains no physical description, clothing details, or visual traits. Only mentions agelessness and death history.

## Costume, Silhouette, Continuity Traits
**Unknown.** No costume, silhouette, or continuity-critical traits documented in source material.

## Render-Facing Prompt Noun Phrases
- Ageless narrator
- Chronicler of life and death
- Post-Civil War veteran (per backstory)
- Guard of gold claim in Arizona winter 1865

## Uncertainty Notes
**CRITICAL:** No physical description available in source material. Cannot generate dependable images without manual description. Need: age appearance, build, facial features, hair, eyes, clothing, gear, distinguishing marks, accessories. Backstory indicates Confederate veteran with funds, but no visual confirmation of period-appropriate attire or specific physical traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: powell
canonical_character_id: Powell
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description, clothing, or visual traits provided in chapter summary or visual continuity facts. Source material only confirms death and companionship with Carter, not appearance.
clarification_required: true
clarification_reason: Character is deceased companion but lacks stable identification for image generation. Need physical description, distinguishing features, and visual continuity notes before collapse.
clarification_question: What are Powell's physical characteristics (age appearance, build, facial features, hair, eyes)? What clothing or gear does he wear? Are there any distinctive marks or accessories?

[[SECTION markdown]]
# powell.md

## Display Name
Powell

## Chapter Role
Carter's companion; co-locates gold vein with Carter. Found dead on plateau surrounded by tepees.

## Physical Presence
Referenced (deceased). Physically present in narrative until death scene.

## Supported Physical Description
**None provided.** Source material contains no physical description, clothing details, or visual traits. Only confirms companionship and death location.

## Costume, Silhouette, Continuity Traits
**Unknown.** No costume, silhouette, or continuity-critical traits documented in source material. Backstory mentions burros (mounts), but not Powell's personal gear or attire.

## Render-Facing Prompt Noun Phrases
- Deceased companion of Carter
- Gold claim locator with Carter
- Found on Arizona plateau winter 1865
- Victim of Apache ambush

## Uncertainty Notes
**CRITICAL:** No physical description available in source material. Cannot generate dependable images without manual description. Need: age appearance, build, facial features, hair, eyes, clothing, gear, distinguishing marks, accessories. Backstory indicates companion with burros (mounts), but no visual confirmation of period-appropriate attire or specific physical traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: Apache Warriors
aliases: Apaches, Indians, warriors
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group reference only; no individual physical descriptions provided. Source material mentions tracks, camp presence, and tepees but no visual details of warriors themselves.
clarification_required: true
clarification_reason: Group reference is insufficient for individual image generation. Need clarification on whether depicting group or individuals, and what distinguishing features apply to the collective or specific members.
clarification_question: Should this be depicted as a group scene or individual warriors? What are their physical characteristics (build, facial features, hair, eyes)? What clothing or gear do they wear? Are there any distinctive marks, accessories, or cultural identifiers visible?

[[SECTION markdown]]
# apache_warriors.md

## Display Name
Apache Warriors

## Chapter Role
Antagonists; ambush Powell's party. Pursue Carter after discovery of tracks. Present at camp with tepees and center object.

## Physical Presence
Referenced (group). Physically present in narrative as pursuing force and camp inhabitants.

## Supported Physical Description
**None provided.** Source material contains no physical description, clothing details, or visual traits for individual warriors. Only mentions tracks (unshod ponies), camp presence with tepees, and cluster of half a thousand warriors around center object.

## Costume, Silhouette, Continuity Traits
**Unknown.** No costume, silhouette, or continuity-critical traits documented in source material. Cultural identifiers may be inferred from Apache/Indian designation but no visual confirmation provided.

## Render-Facing Prompt Noun Phrases
- Group of half a thousand warriors
- Camp with tepees and center object
- Pursuing horsemen on unshod ponies
- Arizona plateau ambushers

## Uncertainty Notes
**CRITICAL:** Group reference only; no individual physical descriptions available. Cannot generate dependable images without manual description. Need: age appearance, build, facial features, hair, eyes, clothing, gear, distinguishing marks, accessories, cultural identifiers. Source material mentions Apache/Indian designation but provides no visual confirmation of period-appropriate attire or specific physical traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
