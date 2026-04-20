# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:13:04.309876+00:00
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

Chapter id: CH025

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

**Visual Continuity:**
- **Location:** Palace of Zodanga (Audience Chamber, Entranceway Portals, Dungeons).
- **Characters:** Than Kosis (Jeddak), Sab Than (Prince), Dejah Thoris (Princess), John Carter, Tars Tarkas, Kantos Kan.
- **Objects:** Golden chain with padlock, scarlet silk robes, long-swords, jeweled dagger, golden thrones.
- **Actions:** Entry through great gate, observation of marriage ceremony, window shattering, combat on platform, rescue from dungeons.

**Story Summary:**
Carter and Tharks enter the palace to interrupt Sab Than's marriage to Dejah Thoris. Carter smashes the golden chain binding her to Zodanga. He fights Than Kosis and Sab Than; Sab Than is killed by Dejah Thoris after attempting to aid his father. Than Kosis dies in combat with Carter. Kantos Kan is rescued from dungeons using keys found on fallen nobles. Carter proposes to Dejah Thoris, who accepts amidst the conflict.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH025

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Description Required |
|----------|------------------------|---------|------------------|----------------------|
| than_kosis_jeddak | Than Kosis (Jeddak) | Jeddak, Father of Sab Than | true | true |
| sab_than_prince | Sab Than (Prince) | Prince, Son of Than Kosis | true | true |
| dejah_thoris_princess | Dejah Thoris (Princess) | Princess of Zodanga | true | true |
| john_carter | John Carter | - | true | true |
| tars_tarkas | Tars Tarkas | - | true | true |
| kantos_kan | Kantos Kan | - | true | true |

*Note: All characters require manual physical description due to sparse visual continuity data in source material.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis_jeddak
canonical_character_id: Than Kosis (Jeddak)
aliases: Jeddak, Father of Sab Than
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description; only role and actions documented. Cannot support image generation without detailed visual data.
clarification_required: false
clarification_reason: Character is clearly named with title and relationship context.
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Than Kosis (Jeddak) - Chapter CH025

**Display Name:** Than Kosis  
**Chapter Role:** Jeddak, Father of Sab Than  
**Physical Presence:** Referenced (dies in combat with John Carter)  
**Visual Continuity Data:** Sparse - no physical description provided in source material. Only known through actions: enters palace, dies fighting Carter.  
**Costume/Silhouette:** Unknown - scarlet silk robes mentioned as general palace attire but not specifically for this character.  
**Continuity-Critical Traits:** Father of Sab Than; antagonist to John Carter; dies during marriage ceremony interruption.  
**Render-Facing Prompt Notes:** "Jeddak Than Kosis, Zodanga Palace noble, combatant, father figure, antagonist role" - requires manual physical description addition for image generation.  
**Uncertainty Notes:** Physical appearance, age, distinguishing features not documented in chapter summary.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than_prince
canonical_character_id: Sab Than (Prince)
aliases: Prince, Son of Than Kosis
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description; only role and actions documented. Cannot support image generation without detailed visual data.
clarification_required: false
clarification_reason: Character is clearly named with title and relationship context.
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Sab Than (Prince) - Chapter CH025

**Display Name:** Sab Than  
**Chapter Role:** Prince, Son of Than Kosis  
**Physical Presence:** Referenced (marriage ceremony participant, killed by Dejah Thoris)  
**Visual Continuity Data:** Sparse - no physical description provided in source material. Only known through actions: marries Dejah Thoris, attempts to aid father, killed by Dejah Thoris.  
**Costume/Silhouette:** Unknown - palace noble attire mentioned generally but not specifically for this character.  
**Continuity-Critical Traits:** Groom at marriage ceremony; son of Than Kosis; killed by his intended bride after attempting to help his father.  
**Render-Facing Prompt Notes:** "Prince Sab Than, Zodanga Palace groom, antagonist role, death scene participant" - requires manual physical description addition for image generation.  
**Uncertainty Notes:** Physical appearance, age, distinguishing features not documented in chapter summary.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris_princess
canonical_character_id: Dejah Thoris (Princess)
aliases: Princess of Zodanga
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description; only role and actions documented. Cannot support image generation without detailed visual data.
clarification_required: false
clarification_reason: Character is clearly named with title and relationship context.
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Dejah Thoris (Princess) - Chapter CH025

**Display Name:** Dejah Thoris  
**Chapter Role:** Princess of Zodanga  
**Physical Presence:** Referenced (marriage ceremony participant, kills Sab Than, accepts Carter's proposal)  
**Visual Continuity Data:** Sparse - no physical description provided in source material. Only known through actions: marries Sab Than, kills him, rescues Kantos Kan, accepts Carter's proposal.  
**Costume/Silhouette:** Unknown - scarlet silk robes mentioned as general palace attire but not specifically for this character.  
**Continuity-Critical Traits:** Princess of Zodanga; intended bride of Sab Than; killer of Sab Than; rescuer of Kantos Kan; acceptor of John Carter's proposal.  
**Render-Facing Prompt Notes:** "Princess Dejah Thoris, Zodanga noble, marriage ceremony participant, combatant, protagonist role" - requires manual physical description addition for image generation.  
**Uncertainty Notes:** Physical appearance, age, distinguishing features not documented in chapter summary.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description; only role and actions documented. Cannot support image generation without detailed visual data.
clarification_required: false
clarification_reason: Character is clearly named with relationship context (enters with Tharks, proposes to Dejah Thoris).
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# John Carter - Chapter CH025

**Display Name:** John Carter  
**Chapter Role:** Protagonist, Enters Palace with Tharks  
**Physical Presence:** Referenced (enters palace, smashes golden chain, fights Than Kosis and Sab Than, rescues Kantos Kan, proposes to Dejah Thoris)  
**Visual Continuity Data:** Sparse - no physical description provided in source material. Only known through actions: enters palace with Tharks, smashes golden chain binding Dejah Thoris, fights Than Kosis and Sab Than, rescues Kantos Kan using keys from fallen nobles, proposes to Dejah Thoris who accepts.  
**Costume/Silhouette:** Unknown - no specific costume details provided in chapter summary.  
**Continuity-Critical Traits:** Enters palace with Tharks; smashes golden chain binding Dejah Thoris to Zodanga; combatant against Than Kosis and Sab Than; rescuer of Kantos Kan; proposer to Dejah Thoris.  
**Render-Facing Prompt Notes:** "John Carter, protagonist, combatant, rescue mission participant, marriage proposal scene" - requires manual physical description addition for image generation.  
**Uncertainty Notes:** Physical appearance, age, distinguishing features not documented in chapter summary.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description; only role and actions documented. Cannot support image generation without detailed visual data.
clarification_required: false
clarification_reason: Character is clearly named with relationship context (enters palace with Carter).
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Tars Tarkas - Chapter CH025

**Display Name:** Tars Tarkas  
**Chapter Role:** Enters Palace with John Carter  
**Physical Presence:** Referenced (enters palace with Carter)  
**Visual Continuity Data:** Sparse - no physical description provided in source material. Only known through actions: enters palace with John Carter.  
**Costume/Silhouette:** Unknown - no specific costume details provided in chapter summary.  
**Continuity-Critical Traits:** Companion to John Carter; enters palace during marriage ceremony interruption.  
**Render-Facing Prompt Notes:** "Tars Tarkas, companion to John Carter, palace entrance participant" - requires manual physical description addition for image generation.  
**Uncertainty Notes:** Physical appearance, age, distinguishing features not documented in chapter summary.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description; only role and actions documented. Cannot support image generation without detailed visual data.
clarification_required: false
clarification_reason: Character is clearly named with relationship context (rescued from dungeons).
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Kantos Kan - Chapter CH025

**Display Name:** Kantos Kan  
**Chapter Role:** Rescued from Dungeons  
**Physical Presence:** Referenced (rescued using keys found on fallen nobles)  
**Visual Continuity Data:** Sparse - no physical description provided in source material. Only known through actions: rescued from dungeons using keys found on Than Kosis and Sab Than after their deaths.  
**Costume/Silhouette:** Unknown - no specific costume details provided in chapter summary.  
**Continuity-Critical Traits:** Imprisoned in Zodanga dungeons; rescued by John Carter using keys from fallen nobles (Than Kosis, Sab Than).  
**Render-Facing Prompt Notes:** "Kantos Kan, dungeon prisoner, rescue mission participant" - requires manual physical description addition for image generation.  
**Uncertainty Notes:** Physical appearance, age, distinguishing features not documented in chapter summary.
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
