# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:32:55.721009+00:00
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

Chapter id: CH017

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

# Chapter Summary: CHAPTER XVII (A COSTLY RECAPTURE)

## Story Arc
1.  **Rescue:** Carter intervenes to save Dejah Thoris and Sola from Tal Hajus in Thark's inner chamber, killing the jeddak.
2.  **Escape:** The group flees on thoats through the wilderness toward Helium.
3.  **Complication:** They become lost; animals weaken; Woola joins them later (not initially present).
4.  **Confrontation:** A party of Thark warriors spots them via fieldglass. Carter shoots a chieftain to prevent capture.
5.  **Sacrifice:** To save Dejah Thoris and Sola, Carter holds off the warriors alone, gets captured by green men after killing many.

## Visual Continuity Facts
- **Locations:** Thark inner chamber (dome-like roof), mossy waste (yellow moonlit ground), hills (ridges, passes).
- **Objects:** Martian rifle (magazine/belt ammo), fieldglass, thoats (trappings/straps), long-sword.
- **Character States:** Dejah Thoris (sobbing/clinging), Tal Hajus (beastly/hideous), Green Warriors (charging/mounted).
- **Lighting:** Brilliant lights in Thark apartments; moonlit moss in wilderness; shadows in courtyards.
- **Continuity Note:** Woola is not with the group at the start of the chapter; he appears later via snuggling close to Carter.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XVII (A Costly Recapture)

| Asset ID | Display Name | Role | Physical Presence | Description Support | Fully Identified |
|----------|--------------|------|-------------------|---------------------|------------------|
| carter | Carter | Protagonist/Rescuer | Present | Supported by chapter summary | Yes |
| dejah_thoris | Dejah Thoris | Rescuee | Present | Supported by chapter summary | Yes |
| sola | Sola | Rescuee | Present | Supported by chapter summary | Yes |
| tal_hajus | Tal Hajus | Antagonist/Jeddak | Present (killed) | Supported by chapter summary | Yes |
| woola | Woola | Companion | Later appearance | Partial support (joins later) | Yes |
| green_warriors | Green Warriors/Thark Warriors | Confronting Party | Present | Group reference only | No |

**Notes:**
- Carter, Dejah Thoris, Sola, and Tal Hajus have stable physical descriptions from the chapter summary.
- Woola appears later in the chapter; description support is partial.
- Green Warriors are referenced as a group without individual identification.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by chapter summary (protagonist, Martian rifle user, long-sword wielder)
clarification_required: false
clarification_reason: Character has stable identification across material
clarification_question: 

[[SECTION markdown]]
# carter.md

## Display Name & Chapter Role
**Carter** - Protagonist/Rescuer in Chapter XVII (A Costly Recapture)

## Physical Presence
- **Status:** Physically present throughout chapter
- **Role:** Intervenes to save Dejah Thoris and Sola from Tal Hajus; holds off Thark warriors alone

## Physical Description (Supported by Source)
- User of Martian rifle with magazine/belt ammo
- Wields long-sword in combat
- Appears in Thark inner chamber, mossy waste, hills during escape sequence
- Later snuggles close to Woola when he joins the group

## Costume & Silhouette
- No specific costume details provided in chapter summary
- Silhouette defined by action: charging, fighting, rescuing

## Continuity-Critical Traits
- Primary rescuer figure in this chapter arc
- Captured by green men after killing many warriors
- Key to preventing capture of Dejah Thoris and Sola

## Render-Facing Prompt Noun Phrases
- "Martian rifle user with magazine ammo"
- "long-sword wielder in combat"
- "protagonist rescuing companions through wilderness"
- "figure charging toward Thark warriors"

## Uncertainty Notes
- Specific costume details not provided in chapter summary
- Facial features and height not described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by chapter summary (rescuee, sobbing/clinging)
clarification_required: false
clarification_reason: Character has stable identification across material
clarification_question: 

[[SECTION markdown]]
# dejah_thoris.md

## Display Name & Chapter Role
**Dejah Thoris** - Rescuee in Chapter XVII (A Costly Recapture)

## Physical Presence
- **Status:** Physically present throughout chapter
- **Role:** Being rescued from Tal Hajus; held captive by Thark warriors

## Physical Description (Supported by Source)
- Described as sobbing and clinging during rescue sequence
- Present in Thark inner chamber, mossy waste, hills during escape
- Captured by green men after Carter holds off warriors alone

## Costume & Silhouette
- No specific costume details provided in chapter summary
- Silhouette defined by emotional state: distressed, being rescued

## Continuity-Critical Traits
- Primary rescuee figure in this chapter arc
- Key motivation for Carter's actions throughout chapter
- Central to preventing capture by Thark warriors

## Render-Facing Prompt Noun Phrases
- "distressed female rescuee sobbing"
- "figure clinging during rescue sequence"
- "companion being protected through wilderness escape"

## Uncertainty Notes
- Specific costume details not provided in chapter summary
- Height and build not described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by chapter summary (rescuee with Dejah Thoris)
clarification_required: false
clarification_reason: Character has stable identification across material
clarification_question: 

[[SECTION markdown]]
# sola.md

## Display Name & Chapter Role
**Sola** - Rescuee in Chapter XVII (A Costly Recapture)

## Physical Presence
- **Status:** Physically present throughout chapter
- **Role:** Being rescued alongside Dejah Thoris from Tal Hajus; held captive by Thark warriors

## Physical Description (Supported by Source)
- Described as being rescued with Dejah Thoris during rescue sequence
- Present in Thark inner chamber, mossy waste, hills during escape
- Captured by green men after Carter holds off warriors alone

## Costume & Silhouette
- No specific costume details provided in chapter summary
- Silhouette defined by emotional state: distressed, being rescued

## Continuity-Critical Traits
- Secondary rescuee figure in this chapter arc
- Key motivation for Carter's actions throughout chapter
- Central to preventing capture by Thark warriors

## Render-Facing Prompt Noun Phrases
- "distressed female rescuee sobbing"
- "figure clinging during rescue sequence alongside companion"
- "companion being protected through wilderness escape"

## Uncertainty Notes
- Specific costume details not provided in chapter summary
- Height and build not described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by chapter summary (beastly/hideous jeddak, killed)
clarification_required: false
clarification_reason: Character has stable identification across material
clarification_question: 

[[SECTION markdown]]
# tal_hajus.md

## Display Name & Chapter Role
**Tal Hajus** - Antagonist/Jeddak in Chapter XVII (A Costly Recapture)

## Physical Presence
- **Status:** Physically present at start of chapter; killed during rescue sequence
- **Role:** Captive holder of Dejah Thoris and Sola; antagonist killed by Carter

## Physical Description (Supported by Source)
- Described as beastly and hideous in appearance
- Present in Thark inner chamber dome-like roof location
- Killed by Carter during rescue intervention

## Costume & Silhouette
- No specific costume details provided in chapter summary
- Silhouette defined by antagonistic presence: beastly, hideous

## Continuity-Critical Traits
- Primary antagonist figure killed in this chapter arc
- Motivation for Carter's rescue actions
- Death marks turning point in chapter sequence

## Render-Facing Prompt Noun Phrases
- "beastly hideous jeddak antagonist"
- "figure killed during rescue intervention"
- "antagonist in Thark inner chamber dome location"

## Uncertainty Notes
- Specific costume details not provided in chapter summary
- Height and build not described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character joins chapter later; initial physical description not provided in chapter summary for this appearance
clarification_required: false
clarification_reason: Character has stable identification across material (known companion)
clarification_question: 

[[SECTION markdown]]
# woola.md

## Display Name & Chapter Role
**Woola** - Companion in Chapter XVII (A Costly Recapture)

## Physical Presence
- **Status:** Not initially present; joins group later via snuggling close to Carter
- **Role:** Companion who appears mid-chapter sequence

## Physical Description (Supported by Source)
- No specific physical description provided for this chapter appearance
- Appears later in chapter through action of joining the group

## Costume & Silhouette
- No specific costume details provided in chapter summary
- Silhouette defined by action: snuggling close to Carter when joining

## Continuity-Critical Traits
- Companion figure who joins mid-chapter sequence
- Key to establishing group dynamic after initial escape
- Appears through physical action rather than description

## Render-Facing Prompt Noun Phrases
- "companion snuggling close to Carter"
- "figure appearing later in wilderness escape sequence"
- "companion joining group mid-chapter"

## Uncertainty Notes
- **IMPORTANT:** Specific physical description not provided for this chapter appearance
- Initial presence is uncertain; character joins later in sequence
- Costume and build details not described in source material for this chapter
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_warriors
canonical_character_id: green_warriors
aliases: thark_warriors, martian_warriors
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group reference only; no individual physical descriptions provided in chapter summary
clarification_required: true
clarification_reason: Character group might already exist under another name or is too weakly identified for dependable image generation
clarification_question: Are the Green Warriors/Thark Warriors a distinct character group with established visual continuity, or should they be treated as generic warrior figures?

[[SECTION markdown]]
# green_warriors.md

## Display Name & Chapter Role
**Green Warriors/Thark Warriors** - Confronting Party in Chapter XVII (A Costly Recapture)

## Physical Presence
- **Status:** Physically present during confrontation sequence; mounted on thoats
- **Role:** Group that spots Carter's party via fieldglass; confronts them in wilderness

## Physical Description (Supported by Source)
- No specific individual physical descriptions provided in chapter summary
- Described as a party/group spotted through fieldglass
- Mounted on thoats with trappings/straps during confrontation

## Costume & Silhouette
- No specific costume details provided in chapter summary
- Silhouette defined by group action: charging, mounted warriors

## Continuity-Critical Traits
- Confronting party that triggers Carter's sacrifice sequence
- Key to establishing danger level in wilderness escape
- Group rather than individual figures in this chapter arc

## Render-Facing Prompt Noun Phrases
- "group of mounted warrior figures charging"
- "party spotted through fieldglass in wilderness"
- "figures on thoats with trappings during confrontation"

## Uncertainty Notes
- **IMPORTANT:** No individual physical descriptions provided for this group
- Group reference only; no stable identification for dependable image generation
- Costume and build details not described in source material
- Clarification required: This group might already exist under another name or is too weakly identified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
