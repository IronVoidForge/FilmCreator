# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:39:49.438384+00:00
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

# Chapter XXV: The Looting of Zodanga

## Broad Story Summary
John Carter leads fifty Thark warriors into the Zodanga palace to rescue Dejah Thoris from forced marriage to Sab Than. During a ceremonial presentation, Carter interrupts the proceedings by shattering the palace window and attacking the golden chain meant to bind Dejah Thoris. A fierce battle ensues in the throne room where Carter kills both Than Kosis (father) and Sab Than (son), ultimately winning Dejah Thoris' hand in marriage despite the chaos of war surrounding them.

## Visual Continuity Facts
### Opening Sequence
- **Location**: Great gate/palace entrance
- **Characters Present**: John Carter, fifty Tharks led by Tars Tarkas
- **Key Objects**: Massive golden gates, huge hinges, palace windows
- **Visual Markers**: Fifty Tharks on mighty thoats, scarlet silk garments

### Throne Room Ceremony
- **Setting**: Audience chamber with brilliantly illuminated audience chamber
- **Characters**: Than Kosis and consort on massive golden thrones encrusted with diamonds
- **Procession Elements**: Four officers bearing huge salver with golden chain, ornaments of prince/princess
- **Key Figures**: Sab Than (muffled in scarlet silk), Dejah Thoris (princess figure)

### Combat Sequence
- **Action Points**: Window shattering, sword strikes on golden chain
- **Antagonists**: Thousand drawn swords menacing from every quarter
- **Weapons**: Long-swords, jeweled dagger (Sab Than's nuptial ornament)
- **Casualties**: Than Kosis and Sab Than both killed

### Resolution Scene
- **Location**: Throne room platform with narrow doorway behind throne
- **Characters**: John Carter, Dejah Thoris, Tars Tarkas, Kantos Kan
- **Key Objects**: Golden thrones, scarlet silks removed from figures
- **Visual Markers**: Corpses of Zodangan nobility covering floor

### Dungeon Rescue
- **Location**: Dungeons beneath palace, labyrinthine prison
- **Characters**: John Carter, dozen warriors, Kantos Kan
- **Action**: Searching for keys to open padlocks of cell and chains
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XXV: The Looting of Zodanga

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence | Description Support | Identification Status |
|----------|----------------------|--------------|------|-------------------|---------------------|----------------------|
| john_carter | john_carter | John Carter | Protagonist, rescuer | Present | Partial | Fully Identified |
| dejah_thoris | dejah_thoris | Dejah Thoris | Princess, heroine | Referenced | Sparse | Fully Identified |
| tars_tarkas | tars_tarkas | Tars Tarkas | Thark leader | Present | Sparse | Fully Identified |
| than_kosis | than_kosis | Than Kosis | Antagonist (father) | Referenced | Minimal | Needs Clarification |
| sab_than | sab_than | Sab Than | Antagonist (son/prince) | Referenced | Sparse | Fully Identified |
| kantos_kan | kantos_kan | Kantos Kan | Ally, rescuer | Present | Minimal | Needs Clarification |

*Note: Characters marked with "Needs Clarification" have insufficient physical description or identification for dependable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter provides limited physical description beyond context of leading fifty Tharks in scarlet silk garments; no detailed facial features, body type, or specific costume elements documented for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Character File

## Display Name
John Carter

## Chapter Role
Protagonist, rescuer of Dejah Thoris from forced marriage to Sab Than

## Physical Presence
**Present** - Leads fifty Thark warriors into Zodanga palace; interrupts ceremonial presentation; kills both Than Kosis and Sab Than in throne room combat

## Physical Description (Supported by Source)
- Contextual markers: Leading fifty Tharks on mighty thoats
- Garment association: Scarlet silk garments worn by Thark party
- Action context: Window shattering, sword strikes on golden chain, long-swords used in combat

## Costume & Silhouette (Known Traits)
- Associated with scarlet silk garments of Thark warriors
- Combat-ready posture during throne room battle sequence

## Continuity-Critical Traits
- Central figure in rescue mission
- Kills both antagonists (Than Kosis and Sab Than)
- Wins Dejah Thoris' hand in marriage despite war chaos

## Render-Facing Prompt Notes
"John Carter leading fifty Tharks, scarlet silk garments context, combat-ready posture, window shattering action, sword strikes on golden chain, long-swords in combat, protagonist rescuing princess figure from forced marriage ceremony"

## Uncertainty Notes
- No detailed facial features documented in chapter summary
- Specific body type or height not mentioned
- Exact costume elements beyond scarlet silk association unclear
- Detailed weapon specifications beyond "long-swords" and implied sword use not provided
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: princess figure
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter describes her only as "princess figure" and notes "scarlet silks removed from figures"; no detailed physical features, facial characteristics, or specific costume elements documented for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Character File

## Display Name
Dejah Thoris

## Chapter Role
Princess figure, heroine rescued from forced marriage to Sab Than

## Physical Presence
**Referenced** - Appears as princess figure in ceremonial procession; scarlet silks removed from her figure after rescue

## Physical Description (Supported by Source)
- Title designation: Princess figure
- Garment association: Scarlet silks (removed from figures after combat sequence)
- Contextual markers: Subject of forced marriage ceremony to Sab Than

## Costume & Silhouette (Known Traits)
- Associated with scarlet silk garments during ceremony
- Princess status indicated by ceremonial presentation context

## Continuity-Critical Traits
- Central figure in rescue mission
- Subject of forced marriage to Sab Than
- Wins hand in marriage despite war chaos after Carter kills antagonists

## Render-Facing Prompt Notes
"Dejah Thoris princess figure, scarlet silk garments during ceremony, rescued from forced marriage to Sab Than, ceremonial presentation context, golden chain meant to bind her, princess status indicated by audience chamber setting"

## Uncertainty Notes
- No detailed facial features documented in chapter summary
- Specific body type or height not mentioned
- Exact costume elements beyond scarlet silk association unclear
- Detailed jewelry or ornamentation specifications not provided
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter provides limited physical description beyond context of leading fifty Tharks; no detailed facial features, body type, or specific costume elements documented for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Character File

## Display Name
Tars Tarkas

## Chapter Role
Thark leader, ally in rescue mission

## Physical Presence
**Present** - Leads fifty Tharks into Zodanga palace; mentioned in resolution scene alongside John Carter and Dejah Thoris

## Physical Description (Supported by Source)
- Leadership role: Leading fifty Tharks on mighty thoats
- Contextual markers: Associated with scarlet silk garments of Thark party
- Action context: Present during throne room combat sequence

## Costume & Silhouette (Known Traits)
- Associated with scarlet silk garments of Thark warriors
- Leader status among Thark group

## Continuity-Critical Traits
- Central figure in rescue mission alongside John Carter
- Present during resolution scene on throne room platform
- Involved in dungeon rescue sequence searching for keys

## Render-Facing Prompt Notes
"Tars Tarkas leading fifty Tharks, scarlet silk garments context, leader among Thark warriors, present during throne room combat sequence, associated with mighty thoats, ally in rescue mission"

## Uncertainty Notes
- No detailed facial features documented in chapter summary
- Specific body type or height not mentioned
- Exact costume elements beyond scarlet silk association unclear
- Detailed weapon specifications not provided
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: than_kosis
aliases: father, antagonist (father)
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides minimal description beyond "father" designation and being killed; no physical features, body type, or costume elements documented for dependable image generation.
clarification_required: true
clarification_reason: Character identified only as "father" without full name or stable identification; insufficient visual markers for later image generation.
clarification_question: What is the full name of Than Kosis and what are his physical features, age range, and costume elements during the throne room ceremony?

[[SECTION markdown]]
# Than Kosis - Character File

## Display Name
Than Kosis (Father)

## Chapter Role
Antagonist, Zodangan noble killed in combat sequence

## Physical Presence
**Referenced** - Appears on massive golden thrones encrusted with diamonds; killed during throne room battle

## Physical Description (Supported by Source)
- Title designation: Father (of Sab Than)
- Position: Seated on massive golden thrones encrusted with diamonds
- Status: Killed during combat sequence in throne room

## Costume & Silhouette (Known Traits)
- Associated with golden thrones encrusted with diamonds
- Zodangan noble status indicated by ceremonial presentation context
- Scarlet silk garments worn during ceremony (removed from figures after combat)

## Continuity-Critical Traits
- Antagonist figure in rescue mission
- Killed by John Carter during throne room battle
- Father of Sab Than (antagonist prince/princess figure)

## Render-Facing Prompt Notes
"Than Kosis father figure, seated on massive golden thrones encrusted with diamonds, Zodangan noble status, ceremonial presentation context, killed during combat sequence, scarlet silk garments worn during ceremony"

## Uncertainty Notes
- No detailed facial features documented in chapter summary
- Specific body type or height not mentioned
- Exact costume elements beyond throne association unclear
- Detailed weapon specifications not provided
- Full name beyond "Than Kosis" designation not specified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: sab_than
aliases: prince figure, antagonist (son), Sab Than
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter describes him as "muffled in scarlet silk" and killed; no detailed facial features, body type, or specific costume elements beyond muffled scarlet silk documented for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sab Than - Character File

## Display Name
Sab Than (Prince Figure)

## Chapter Role
Antagonist, prince/princess figure forced to marry Dejah Thoris

## Physical Presence
**Referenced** - Appears muffled in scarlet silk during ceremonial presentation; killed during throne room battle

## Physical Description (Supported by Source)
- Title designation: Prince figure / son of Than Kosis
- Garment association: Muffled in scarlet silk during ceremony
- Status: Killed during combat sequence in throne room
- Weapon context: Possesses jeweled dagger as nuptial ornament

## Costume & Silhouette (Known Traits)
- Muffled in scarlet silk garments during ceremonial presentation
- Associated with golden chain meant to bind Dejah Thoris
- Jeweled dagger as nuptial ornament mentioned
- Zodangan noble status indicated by ceremonial context

## Continuity-Critical Traits
- Antagonist figure forced into marriage ceremony with Dejah Thoris
- Killed by John Carter during throne room battle
- Father of Sab Than (note: appears to be same character - father designation)
- Possesses jeweled dagger as nuptial ornament

## Render-Facing Prompt Notes
"Sab Than prince figure, muffled in scarlet silk garments during ceremonial presentation, killed during combat sequence, possesses jeweled dagger as nuptial ornament, associated with golden chain meant to bind Dejah Thoris, Zodangan noble status"

## Uncertainty Notes
- No detailed facial features documented in chapter summary
- Specific body type or height not mentioned
- Exact costume elements beyond muffled scarlet silk association unclear
- Detailed weapon specifications beyond jeweled dagger mention not provided
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: kantos_kan
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides minimal description beyond name only; no physical features, body type, or costume elements documented for dependable image generation.
clarification_required: true
clarification_reason: Character identified only by name without full physical description or stable identification markers; insufficient visual information for later image generation.
clarification_question: What are Kantos Kan's physical features, age range, and costume elements during the resolution scene and dungeon rescue sequence?

[[SECTION markdown]]
# Kantos Kan - Character File

## Display Name
Kantos Kan

## Chapter Role
Ally, rescuer in dungeon rescue sequence

## Physical Presence
**Present** - Mentioned in resolution scene alongside John Carter, Dejah Thoris, and Tars Tarkas; involved in dungeon rescue searching for keys

## Physical Description (Supported by Source)
- Name designation: Kantos Kan
- Contextual markers: Present during resolution scene on throne room platform
- Action context: Searching for keys to open padlocks of cell and chains in dungeons beneath palace

## Costume & Silhouette (Known Traits)
- No specific costume elements documented in chapter summary
- Associated with rescue mission alongside John Carter

## Continuity-Critical Traits
- Ally figure in rescue mission
- Present during resolution scene on throne room platform
- Involved in dungeon rescue sequence searching for keys to open padlocks of cell and chains

## Render-Facing Prompt Notes
"Kantos Kan ally figure, present during resolution scene on throne room platform, involved in dungeon rescue sequence searching for keys to open padlocks of cell and chains, associated with rescue mission alongside John Carter"

## Uncertainty Notes
- No detailed facial features documented in chapter summary
- Specific body type or height not mentioned
- Exact costume elements not provided
- Detailed weapon specifications not provided
- Full physical description beyond name designation not specified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
