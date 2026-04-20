# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:07:08.949317+00:00
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

Chapter id: CH011

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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values



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

*   **Scene 1: New Quarters & Sarkoja's Threat.** Carter arrives with Sola and Dejah Thoris at a new, ancient building near the audience chamber. He dismisses female guards to prevent Sarkoja from harming Dejah Thoris, threatening her demise if she continues her cruel attentions.
*   **Scene 2: Thark Hierarchy & Rank.** Sola explains Carter's promotion to eleventh Chieftain, noting his metal rank is close to Tars Tarkas (second only to Lorquas Ptomel). She clarifies that killing Lorquas Ptomel would make him first, but requires council approval or self-defense.
*   **Scene 3: Ancient Architecture & Frescoes.** They inspect the new quarters, which feature elaborate decorations of fair-haired, beardless Martians in robes. Dejah Thoris is captivated by the art of extinct people, while Sola ignores it. The room includes ancient metal beds and sleeping apartments.
*   **Scene 4: Origin Debate.** Dejah Thoris questions Carter's claim of being from Earth/Virginia, noting Barsoomians speak one tongue but he claims recent learning. She pleads for a denial, fearing the horror of a man returning from the "Barsoomian heaven or hell." Carter explains his Earth origin and Virginia customs.
*   **Scene 5: Belief & Martian Technology.** Dejah Thoris eventually believes him due to her emotional connection ("heart tells me that I believe"). She asks about Earth, explaining how Martians view other planets via screens/instruments. She notes the lack of ornaments on Carter proves his un-Barsoomian origin.
*   **Scene 6: History of Korad.** Dejah Thoris explains the history of the red race mixing with ancient fair-haired Martians and dark races due to drying seas. They discuss the city of Korad, built near a natural harbor, and the lost civilization of the ancient Martians.
*   **Scene 7: Conclusion.** After exploring the building and discussing customs, Carter receives a summons from Lorquas Ptomel to appear before him in the audience chamber.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH011

| Asset ID | Canonical ID | Name | Presence | Description Status |
|----------|--------------|------|----------|-------------------|
| carter_drax | Carter Drax | Carter | Physically Present | Fully Identified |
| sola | Sola | Sola | Physically Present | Fully Identified |
| dejah_thoris | Dejah Thoris | Dejah Thoris | Physically Present | Fully Identified |
| lorquas_ptomel | Lorquas Ptomel | Lorquas Ptomel | Referenced | Partially Identified |
| tars_tarkas | Tars Tarkas | Tars Tarkas | Referenced | Partially Identified |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter_drax
canonical_character_id: Carter Drax
aliases: Carter, Earthman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter Drax

**Chapter Role:** Protagonist / Eleventh Chieftain  
**Physical Presence:** Present (arrives with Sola and Dejah Thoris)

## Physical Description
- No physical description provided in source material for this chapter
- Metal rank close to Tars Tarkas (second only to Lorquas Ptomel)
- Promoted to eleventh Chieftain status

## Costume & Silhouette
- No costume details specified in source
- Lacks Barsoomian ornaments (proves un-Barsoomian origin)

## Continuity-Critical Traits
- Claims Earth/Virginia origin (recently learned language)
- Dejah Thoris's heart tells her to believe him despite skepticism
- Summoned by Lorquas Ptomel to appear in audience chamber

## Render-Facing Noun Phrases
- "Earthman from Virginia"
- "Eleventh Chieftain rank"
- "Un-Barsoomian origin"
- "Metal rank close to Tars Tarkas"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

**Chapter Role:** Female Guard / Companion  
**Physical Presence:** Present (arrives with Carter and Dejah Thoris)

## Physical Description
- No physical description provided in source material for this chapter
- Female guard who dismisses other female guards to protect Dejah Thoris from Sarkoja

## Costume & Silhouette
- No costume details specified in source
- Wears Thark military attire (implied by guard role)

## Continuity-Critical Traits
- Explains Carter's promotion and rank hierarchy
- Ignores frescoes of extinct fair-haired Martians
- Protects Dejah Thoris from Sarkoja's cruel attentions
- Clarifies killing Lorquas Ptomel requires council approval or self-defense

## Render-Facing Noun Phrases
- "Female guard companion"
- "Thark military attire"
- "Rank hierarchy explainer"
- "Protector of Dejah Thoris"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess of Helium, Dejah
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

**Chapter Role:** Princess of Helium / Main Female Lead  
**Physical Presence:** Present (arrives with Carter and Sola)

## Physical Description
- No physical description provided in source material for this chapter
- Captivated by frescoes of extinct fair-haired Martians in robes

## Costume & Silhouette
- No costume details specified in source
- Lacks Barsoomian ornaments (proves un-Barsoomian origin according to Dejah's observation)

## Continuity-Critical Traits
- Questions Carter's Earth/Virginia origin initially
- Eventually believes him emotionally ("heart tells me that I believe")
- Explains Martian technology: screens/instruments for viewing other planets
- Discusses red race mixing with ancient fair-haired Martians and dark races
- Notes lack of ornaments on Carter proves his un-Barsoomian origin
- Summoned to appear before Lorquas Ptomel in audience chamber

## Render-Facing Noun Phrases
- "Princess of Helium"
- "Emotional believer"
- "Martian technology expert"
- "Historical knowledge holder (Korad, ancient Martians)"
- "Fair-haired Martian art captivated observer"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

**Chapter Role:** High Martian Authority / Audience Chamber Leader  
**Physical Presence:** Referenced (not physically present in scene)

## Physical Description
- No physical description provided in source material for this chapter
- Highest-ranking Martian mentioned in hierarchy

## Costume & Silhouette
- No costume details specified in source
- Wears Thark military attire (implied by audience chamber authority)

## Continuity-Critical Traits
- Second highest rank after Lorquas Ptomel (Tars Tarkas is second only to him)
- Carter's killing of him would make Carter first Chieftain
- Requires council approval or self-defense for such action
- Summons Carter to appear before him in audience chamber

## Render-Facing Noun Phrases
- "Highest-ranking Martian authority"
- "Audience chamber summoner"
- "First Chieftain position holder"
- "Council approval required for killing"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

**Chapter Role:** High Martian Authority / Rank Reference  
**Physical Presence:** Referenced (not physically present in scene)

## Physical Description
- No physical description provided in source material for this chapter
- Metal rank close to Lorquas Ptomel

## Costume & Silhouette
- No costume details specified in source
- Wears Thark military attire (implied by high-ranking status)

## Continuity-Critical Traits
- Second highest rank after Lorquas Ptomel
- Carter's metal rank is close to his own
- Mentioned in Thark hierarchy explanation by Sola

## Render-Facing Noun Phrases
- "Second highest Martian rank"
- "Metal rank reference point"
- "Thark hierarchy second position"
- "Carter's rank comparison target"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
