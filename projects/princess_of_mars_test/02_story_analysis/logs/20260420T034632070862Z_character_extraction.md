# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:46:32.070862+00:00
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

# Chapter Summary: CH012 - A Prisoner with Power

**Story Arc:**
*   **Interrogation:** Lorquas Ptomel addresses John Carter, acknowledging his prowess but warning him of his precarious position (prisoner yet chieftain). Accusations arise regarding a plot to escape with Dejah Thoris. Execution is threatened unless Tal Hajus commands otherwise.
*   **Warning:** Lorquas warns that if John runs off with the "red girl," he must account to Tal Hajus and Tars Tarkas. He states they await only two excuses for killing John: self-defense or attempted escape.
*   **Realization:** John leaves the audience chamber, realizing this is Sarkoja's persecution. He recalls conversations about escape and origin.
*   **Quarters Offered:** Tars Tarkas approaches John in the plaza. Offers him quarters on the third floor of a building adjoining Sola's residence. The first floor is occupied by Tars Tarkas; second by Sola/charges.
*   **Retinue & Loot:** Women and youths arrive bearing weapons, silks, furs, jewels, cooking utensils, food, and loot from air craft (property of two slain chieftains). John directs them to find quarters on upper floors.
*   **Room Selection:** John chooses a front room on the third floor to be near Dejah Thoris's apartment (second floor) to rig up communication means.
*   **Cultural Exposition:** John observes the Thark retinue customs: women and children are military units for which he is responsible, not wives or servants. Property is communal; surplus is passed to younger members. Mating is community-directed.

**Visual Continuity Facts:**
*   **Audience Chamber:** Lorquas Ptomel signals John to advance; his great, hideous eyes fix upon John.
*   **Plaza:** John wanders in gloomy forebodings; Tars Tarkas approaches with unchanged demeanor.
*   **Building Layout:** Three floors visible. First occupied by Tars Tarkas. Second by Sola and charges. Third vacant for John.
*   **Loot Items:** Weapons, silks, furs, jewels, cooking utensils, casks of food/drink, air craft loot.
*   **Court View:** Back rooms overlook an enormous court with yellow moss-like vegetation, fountains, statuary, benches, and pergola-like contraptions.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH012

| Character | Role | Status | Description Quality |
|-----------|------|--------|---------------------|
| Lorquas Ptomel | Audience chamber official | Present | Partial physical description |
| John Carter | Protagonist | Present | Main character, stable identification |
| Tars Tarkas | Plaza figure | Present | Minimal physical description |
| Dejah Thoris | Referenced love interest | Not present | No physical description available |
| Tal Hajus | Warning authority | Not present | Only mentioned in dialogue |
| Sola | Building occupant | Not directly visible | Second floor resident only |
| Sarkoja | Persecutor (realized) | Referenced | Name only, no visual details |

**Note:** This index documents all characters referenced or present in Chapter CH012. Physical descriptions vary from detailed to minimal based on source material availability.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas_Ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only "great, hideous eyes" described; insufficient physical details for reliable image generation
clarification_required: false
clarification_question: 

[[SECTION markdown]]
# lorquas_ptomel

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Audience chamber official addressing John Carter  
**Physical Presence:** Present in audience chamber, great hideous eyes fix upon John  
**Physical Description:** Great, hideous eyes (primary visual feature noted)  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** Signals John to advance; maintains presence during interrogation scene  

**Uncertainty Notes:** Limited physical description available. Only eye features documented. Full appearance uncertain for render-facing generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John_Carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Protagonist with stable identification throughout chapter; physical presence confirmed
clarification_required: false
clarification_question: 

[[SECTION markdown]]
# john_carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist, prisoner yet chieftain  
**Physical Presence:** Present throughout chapter (audience chamber, plaza, quarters)  
**Physical Description:** Not explicitly detailed in source material; protagonist status confirmed  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** Recognized by Lorquas Ptomel and Tars Tarkas; realizes persecution is Sarkoja's work  

**Uncertainty Notes:** As protagonist, physical description may be sparse in this chapter. Stable identification maintained for continuity purposes.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars_Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only "unchanged demeanor" noted; insufficient physical details for reliable image generation
clarification_required: false
clarification_question: 

[[SECTION markdown]]
# tars_tarkas

**Display Name:** Tars Tarkas  
**Chapter Role:** Plaza figure, building occupant (first floor)  
**Physical Presence:** Present in plaza, approaches John with unchanged demeanor  
**Physical Description:** Unchanged demeanor (behavioral trait only)  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** Occupies first floor of three-story building; second floor by Sola/charges  

**Uncertainty Notes:** Minimal physical description available. Behavioral consistency noted but full appearance uncertain for render-facing generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah_Thoris
aliases: red girl
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced as "red girl"; no physical description available in source material
clarification_required: true
clarification_question: Does Dejah Thoris have established visual details from prior chapters that should inform this character's appearance?

[[SECTION markdown]]
# dejah_thoris

**Display Name:** Dejah Thoris  
**Chapter Role:** Referenced love interest, not physically present  
**Physical Presence:** Not present in chapter (only referenced)  
**Physical Description:** None available in source material; only "red girl" epithet noted  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** John Carter realizes persecution is Sarkoja's work; quarters chosen to be near her apartment  

**Uncertainty Notes:** Character not physically present. Only referenced by name and epithet. Physical description unavailable for reliable image generation. Clarification needed on established visual details from prior story context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal_Hajus
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned in warning dialogue; no physical description or presence in chapter
clarification_required: true
clarification_question: Is Tal Hajus a new character introduction or an established authority figure with prior visual details?

[[SECTION markdown]]
# tal_hajus

**Display Name:** Tal Hajus  
**Chapter Role:** Warning authority (mentioned only)  
**Physical Presence:** Not present in chapter (only referenced in dialogue)  
**Physical Description:** None available; only name mentioned in warning about John's execution  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** Authority over John's life/death decisions; two excuses for killing John noted  

**Uncertainty Notes:** Character not physically present. Only referenced in dialogue warning. No physical description available for reliable image generation. Clarification needed on character status and prior visual details.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced as second floor occupant; no physical description or direct presence in chapter
clarification_required: true
clarification_question: Is Sola a new character introduction or an established figure with prior visual details from story context?

[[SECTION markdown]]
# sola

**Display Name:** Sola  
**Chapter Role:** Building occupant (second floor)  
**Physical Presence:** Not directly visible in chapter (only referenced as resident)  
**Physical Description:** None available; only building location noted  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** Second floor of three-story building; charges occupy same space  

**Uncertainty Notes:** Character not directly visible. Only referenced as second floor occupant. No physical description available for reliable image generation. Clarification needed on character status and prior visual details.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced by name in John's realization; no physical description or presence in chapter
clarification_required: true
clarification_question: Is Sarkoja a new character introduction or an established antagonist with prior visual details from story context?

[[SECTION markdown]]
# sarkoja

**Display Name:** Sarkoja  
**Chapter Role:** Persecutor (realized by John)  
**Physical Presence:** Not present in chapter (only referenced by name)  
**Physical Description:** None available; only name noted in John's realization about persecution  
**Costume/Silhouette:** Not described in source material  
**Continuity Traits:** John realizes this is her persecution; conversations about escape and origin recalled  

**Uncertainty Notes:** Character not physically present. Only referenced by name in protagonist's realization. No physical description available for reliable image generation. Clarification needed on character status and prior visual details from story context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
