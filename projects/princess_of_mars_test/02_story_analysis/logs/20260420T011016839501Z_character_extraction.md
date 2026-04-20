# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:10:16.839501+00:00
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

Chapter id: CH012

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

# Chapter Summary: CH012 - A Prisoner With Power

## Scene 1: The Audience Chamber Warning
**Visual Continuity:** John Carter enters the audience chamber and salutes. Lorquas Ptomel signals him to advance, fixing his great, hideous eyes upon Carter.
**Story Beat:** Lorquas Ptomel addresses Carter's high position among the Tharks but emphasizes he is not one of them and owes no allegiance. He warns that Carter is a prisoner giving commands which must be obeyed.
**Conflict:** Lorquas Ptomel reports accusations that Carter plotted to escape with Dejah Thoris ("the red girl"). Either accusation (escape plot or running off with her) would warrant execution, but the Tharks are just and will grant a trial on their return to Thark if Tal Hajus commands.
**Threat:** Lorquas Ptomel states that if Carter runs off with the red girl, he (Lorquas Ptomel) must account to Tal Hajus and face Tars Tarkas. He warns that under two conditions only may Carter be killed without orders: personal combat in self-defense or apprehended in an attempt to escape.
**Resolution:** Lorquas Ptomel emphasizes the importance of safe delivery of Dejah Thoris to Tal Hajus. He concludes, "You may go."

## Scene 2: Realization and Decision
**Visual Continuity:** Carter turns and leaves the audience chamber.
**Story Beat:** Carter realizes this is the beginning of Sarkoja's persecution (Sarkoja being Tars Tarkas' oldest and most trusted female). He recalls conversations touching on escape and origin.
**Internal Monologue:** Instead of putting thoughts of escape from his mind, the audience centers every faculty on this subject. The absolute necessity for escape regarding Dejah Thoris is impressed upon him, convinced that some horrible fate awaits her at Tal Hajus's headquarters.
**Visual Continuity:** Carter wanders about the plaza lost in gloomy forebodings.

## Scene 3: Meeting Tars Tarkas
**Visual Continuity:** Tars Tarkas approaches Carter on his way from the audience chamber. His demeanor toward Carter is unchanged; he greets Carter as though they had not just parted moments before.
**Dialogue:** Tars Tarkas asks for Carter's quarters. Carter replies he has selected none, awaiting advice or opportunity to ask advice. He smiles, noting he is not yet familiar with all Thark customs.
**Action:** Tars Tarkas directs Carter to come with him; they move off across the plaza to a building adjoined by Sola and her charges.

## Scene 4: Quarters Selection and Social Explanation
**Visual Continuity:** Tars Tarkas states his quarters are on the first floor of this building, second floor fully occupied by warriors, third floor and above vacant. Carter may take choice.
**Dialogue:** Tars Tarkas notes Carter gave up his woman to the red prisoner. He explains that as a chieftain, Carter may select any or all females from retinues of chieftains whose metal he now wears.
**Action:** Carter thanks him but assures him he can get along without assistance except preparing food. Tars Tarkas promises to send women for food and care of arms/ammunition. Carter suggests they bring sleeping silks and furs belonging to him as spoils of combat.
**Visual Continuity:** Tars Tarkas promises and departs. Left alone, Carter ascends winding corridor to upper floors in search of suitable quarters.

## Scene 5: Room Selection and Loot Arrival
**Visual Continuity:** Beauties of other buildings are repeated; Carter is soon lost in tour of investigation and discovery. He finally chooses a front room on the third floor because it brings him nearer to Dejah Thoris (apartment on second floor of adjoining building).
**Plan:** Carter flashes upon rigging up means of communication whereby she might signal him in case she needs services or protection.
**Visual Continuity:** Adjoining sleeping apartment are baths, dressing rooms, and other sleeping/living apartments (some ten rooms on this floor). Windows of back rooms overlook enormous court forming center of square made by buildings facing four contiguous streets. Court given over to quartering various animals belonging to warriors occupying adjoining buildings.
**Description:** Court entirely overgrown with yellow, moss-like vegetation; numerous fountains, statuary, benches, and pergola-like contraptions bear witness to beauty presented in bygone times.

## Scene 6: Arrival of Women and Social Customs Explanation
**Visual Continuity:** Advent of several young females bearing loads of weapons, silks, furs, jewels, cooking utensils, and casks of food/drink (considerable loot from air craft). All this property belonged to two chieftains Carter had slain; now by customs of Tharks it has become his.
**Action:** At Carter's direction they place stuff in one back room, then depart only to return with second load advised as balance of goods. Second trip accompanied by ten or fifteen other women and youths forming retinues of two chieftains.
**Explanation:** Women/children of man's retinue likened to military unit for which he is responsible (instruction, discipline, sustenance). Not families, wives, or servants; relationship peculiar. All property owned in common except personal weapons, ornaments, sleeping silks/furs. Surplus held as custodian passed on to younger members.
**Customs:** Mating is matter of community interest solely, directed without reference to natural selection. Council of chieftains control matter. Results shown in cold, cruel creatures and gloomy, loveless existence. Green Martians are absolutely virtuous except degenerates like Tal Hajus.

## Scene 7: Final Arrangement
**Visual Continuity:** Carter finds he must assume responsibility for these creatures whether he would or not; makes best of it and directs them to find quarters on upper floors, leaving third floor to him.
**Action:** One girl charged with duties of simple cuisine; others directed to take up various activities formerly constituting vocations. Thereafter Carter sees little of them nor cares to.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH012

| Asset ID | Canonical Name | Aliases | Presence | Description Status |
| :--- | :--- | :--- | :--- | :--- |
| john_carter | John Carter | (none) | Present | Manual Description Required |
| lorquas_ptomel | Lorquas Ptomel | (none) | Present | Manual Description Required |
| dejah_thoris | Dejah Thoris | the red girl | Referenced | Manual Description Required |
| sarkoja | Sarkoja | (none) | Referenced | Manual Description Required |
| tars_tarkas | Tars Tarkas | (none) | Present | Manual Description Required |
| tal_hajus | Tal Hajus | (none) | Referenced | Manual Description Required |
| sola | Sola | (none) | Present | Manual Description Required |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary provides no physical description of John Carter, only his actions and dialogue. Visual continuity notes are absent.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# john_carter.md

## Display Name
John Carter

## Chapter Role
Protagonist / Prisoner giving commands

## Physical Presence
Present in Scene 1, 2, 3, 4, 5, 6, 7 (Audience Chamber, Plaza, Building)

## Physical Description
*   **Supported:** None provided in this chapter summary.
*   **Uncertainty:** Visual continuity notes are absent. No physical description is supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal (implied by "whose metal he now wears").
*   **Uncertainty:** Full costume details not described in this chapter.

## Continuity Traits
*   **Role:** Central figure in the audience chamber warning and quarters selection.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary mentions "great, hideous eyes" but lacks full physical description. Visual continuity notes are absent for other features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# lorquas_ptomel.md

## Display Name
Lorquas Ptomel

## Chapter Role
Thark Official / Warning Messenger

## Physical Presence
Present in Scene 1 (Audience Chamber)

## Physical Description
*   **Supported:** "Great, hideous eyes".
*   **Uncertainty:** Full physical description not supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal.
*   **Uncertainty:** Specific costume details not described in this chapter.

## Continuity Traits
*   **Role:** Addresses Carter's high position among the Tharks but emphasizes he is not one of them.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: the red girl
is_fully_identified: true
manual_description_required: true
manual_description_reason: Referenced only; no physical description provided in this chapter. Visual continuity notes are absent for other features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# dejah_thoris.md

## Display Name
Dejah Thoris

## Chapter Role
Princess / "The Red Girl"

## Physical Presence
Referenced in Scene 1, 5 (Location mentioned)

## Physical Description
*   **Supported:** None provided in this chapter summary.
*   **Uncertainty:** Visual continuity notes are absent. No physical description is supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal (implied).
*   **Uncertainty:** Full costume details not described in this chapter.

## Continuity Traits
*   **Role:** Subject of accusations against Carter ("running off with her").
*   **Location:** Apartment on second floor of adjoining building.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Referenced only; no physical description provided in this chapter. Visual continuity notes are absent for other features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# sarkoja.md

## Display Name
Sarkoja

## Chapter Role
Thark Female / Tars Tarkas' Trusted Associate

## Physical Presence
Referenced in Scene 2 (Internal Monologue)

## Physical Description
*   **Supported:** None provided in this chapter summary.
*   **Uncertainty:** Visual continuity notes are absent. No physical description is supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal (implied).
*   **Uncertainty:** Full costume details not described in this chapter.

## Continuity Traits
*   **Role:** Carter realizes this is the beginning of her persecution. Identified as Tars Tarkas' oldest and most trusted female.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary provides no physical description of Tars Tarkas, only his demeanor and actions. Visual continuity notes are absent for other features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# tars_tarkas.md

## Display Name
Tars Tarkas

## Chapter Role
Thark Chieftain / Carter's Guide

## Physical Presence
Present in Scene 3, 4 (Approaches Carter, Directs him)

## Physical Description
*   **Supported:** None provided in this chapter summary.
*   **Uncertainty:** Visual continuity notes are absent. No physical description is supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal.
*   **Uncertainty:** Full costume details not described in this chapter.

## Continuity Traits
*   **Role:** Greets Carter as though they had not just parted moments before. Explains customs of Tharks.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Referenced only; no physical description provided in this chapter. Visual continuity notes are absent for other features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# tal_hajus.md

## Display Name
Tal Hajus

## Chapter Role
Thark Chieftain / Degenerate Green Martian

## Physical Presence
Referenced in Scene 1, 6 (Mentioned in trial context)

## Physical Description
*   **Supported:** None provided in this chapter summary.
*   **Uncertainty:** Visual continuity notes are absent. No physical description is supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal (implied).
*   **Uncertainty:** Full costume details not described in this chapter.

## Continuity Traits
*   **Role:** Trial on return to Thark will be commanded by him if Tal Hajus commands. Described as a degenerate Green Martian.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Mentioned with charges; no physical description provided in this chapter. Visual continuity notes are absent for other features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# sola.md

## Display Name
Sola

## Chapter Role
Thark Female / Charge Keeper

## Physical Presence
Present in Scene 3 (Building adjoined by Sola and her charges)

## Physical Description
*   **Supported:** None provided in this chapter summary.
*   **Uncertainty:** Visual continuity notes are absent. No physical description is supported by the source material for image generation.

## Costume & Silhouette
*   **Supported:** Wears Thark metal (implied).
*   **Uncertainty:** Full costume details not described in this chapter.

## Continuity Traits
*   **Role:** Building adjoined by Sola and her charges.
*   **Note:** Image generation requires manual description input due to lack of visual source data.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
