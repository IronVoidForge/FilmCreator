# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:11:21.081228+00:00
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

Chapter id: CH009

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

# Chapter Summary: CH009 - "I LEARN THE LANGUAGE"

**Visual Continuity Facts:**
*   **Armor Presentation:** A warrior approaches the building doorway bearing arms, ornaments, and accouterments of his kind. These are presented to the narrator with a respectful yet menacing bearing.
*   **Remodeling:** Women (including Sola) physically remodel the trappings to fit the narrator's lesser proportions.
*   **Plaza Practice:** The narrator spends hours on the plaza practicing weapons with recently hatched young Martians under Sola's instruction.
*   **Sleeping Quarters:** Occupied by three or four females, a couple of young Martians, Sola, her ward (narrator), and Woola the hound. Adults carry on desultory conversation before sleep.
*   **Audience Chamber Glimpse:** The narrator catches a fleeting glimpse of the prisoner being conducted to the great audience chamber where Lorquas Ptomel met him previously.

**Story Summary & Scene Decomposition:**

1.  **Morning Awakening & Armor:**
    *   Narrator wakes and glances at Sola, noting a strange expression on her countenance regarding the previous encounter with the prisoner.
    *   Warrior presents armor at doorway; narrator accepts it.
    *   Women fit the armor to the narrator's body.
    *   Narrator practices weapons on plaza with young Martians under Sola's instruction.

2.  **Martian Society Exposition:**
    *   Training is conducted solely by women who produce all manufactured articles (powder, cartridges, firearms).
    *   Women form reserves in time of actual warfare and fight with greater intelligence/ferocity than men.
    *   Men are trained in strategy, maneuvering large bodies of troops, making laws, and administering justice without precedent.

3.  **Prisoner Sightings & Language Learning:**
    *   Narrator sees prisoner briefly in audience chamber; notes harsh treatment by guards compared to Sola's kindness.
    *   Narrator observes prisoner exchanges words with guards, realizing they speak a common language.
    *   Narrator drives Sola distracted by importunities to hasten education; masters Martian tongue within days to carry on passable conversation.

4.  **Night Conversation & The "Red One":**
    *   Conversation among females turns to the prisoner ("red one") after her visit to audience chamber.
    *   Narrator listens keenly, fearing to question Sola directly due to strange expression noted earlier (possible jealousy).
    *   Sarkoja (older woman/guard) replies to inquiry about prisoner's fate: decided to carry her back to Thark for exhibition at great games before Tal Hajus.
    *   Sola expresses hope they would hold her for ransom; criticized by others as weak/atavistic.
    *   Sarkoja reprimands Sola, calling such sentiments degenerate and unfit for maternity responsibilities under Tars Tarkas.

5.  **Sola's Outburst & Narrator's Resolution:**
    *   Sola defends her interest, stating the prisoner has never harmed them and that Martians are inherently cruel/warring among themselves.
    *   Wild outbreak shocks other women into silence and sleep.
    *   Narrator realizes Sola's friendliness toward the captive and confirms she hates cruelty/barbarity.
    *   Narrator decides to take chances among people fashioned after his own mold rather than remaining with green men.
    *   Narrator resolves to ask Sola openly for aid at first opportunity regarding escape.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH009 "I LEARN THE LANGUAGE"

| Character | Role in Chapter | Physical Description | Identified |
|-----------|-----------------|---------------------|------------|
| Sola | Narrator's ward/guard, weapons instructor | Older woman/guard, has strange expression, defends prisoner | Partially |
| Narrator | Protagonist/ward being taught | Unknown - no physical description provided | No |
| Sarkoja | Older guard, speaks of prisoner's fate | Older woman/guard | Partially |
| Woola | Hound companion | Only mentioned as hound in sleeping quarters | No |
| Prisoner ("Red One") | Captive being discussed | Referred to as "red one", harsh treatment by guards | Partially |
| Lorquas Ptomel | Previous meeting reference | Only name mentioned, no appearance | No |
| Tars Tarkas | Referenced in speech | Only referenced, no physical description | No |

*Note: Several characters lack sufficient physical or visual description for dependable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: ward, guard
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical appearance details for Sola beyond "older woman/guard" and "strange expression on her countenance" - insufficient for image generation
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity
clarification_question: What is Sola's full physical description including hair, eyes, build, age appearance?

[[SECTION markdown]]
# Sola - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Sola  
**Chapter Role:** Narrator's ward/guard, weapons instructor, language teacher  

**Physical Presence:** Referenced throughout chapter; physically present in scenes with narrator and other women  

**Physical Description (Supported by Source):**  
- Referred to as "older woman/guard"  
- Has a "strange expression on her countenance" regarding prisoner encounter  
- Teaches weapons practice to narrator  
- Instructs narrator in Martian language within days  
- Expresses hope for prisoner ransom, criticized as weak  

**Costume/Silhouette (Supported by Source):**  
- No specific costume details provided  
- Silhouette only described through role relationships with other women and Martians  

**Continuity-Critical Traits:**  
- Shows kindness to narrator compared to guards' harsh treatment of prisoner  
- Defends prisoner against Sarkoja's reprimand  
- Has "wild outbreak" when defending prisoner, shocking others into silence  
- Narrator fears her possible jealousy regarding prisoner  

**Uncertainty Notes:**  
- No physical appearance details (hair, eyes, build, age) provided in chapter  
- No costume or silhouette specifics available  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: ward, protagonist
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical description of narrator beyond role as "ward" and "narrator" - insufficient for image generation  
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity  
clarification_question: What is the narrator's full physical description including hair, eyes, build, age appearance?

[[SECTION markdown]]
# Narrator - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Narrator (Protagonist)  
**Chapter Role:** Ward being taught weapons and language, observer of events  

**Physical Presence:** Physically present throughout chapter; practices weapons on plaza, accepts armor at doorway  

**Physical Description (Supported by Source):**  
- No physical appearance details provided in chapter  
- Referred to as "ward" and "narrator" only  
- Described through actions: accepts armor, practices weapons, masters Martian tongue within days  

**Costume/Silhouette (Supported by Source):**  
- Receives armor fitted by women to his "lesser proportions"  
- No specific costume details provided  
- Silhouette only described through relationship with narrator's body proportions  

**Continuity-Critical Traits:**  
- Observes Sola's strange expression regarding prisoner encounter  
- Practices weapons under Sola's instruction  
- Masters Martian language within days  
- Decides to take chances among people "fashioned after his own mold" rather than remaining with "green men"  
- Resolves to ask Sola openly for aid regarding escape  

**Uncertainty Notes:**  
- No physical appearance details (hair, eyes, build, age) provided in chapter  
- No costume or silhouette specifics available  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: older woman, guard
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides only "older woman/guard" description - insufficient for image generation  
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity  
clarification_question: What is Sarkoja's full physical description including hair, eyes, build, age appearance?

[[SECTION markdown]]
# Sarkoja - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Sarkoja  
**Chapter Role:** Older guard, speaks about prisoner's fate  

**Physical Presence:** Present in sleeping quarters conversation; replies to narrator's inquiry about prisoner  

**Physical Description (Supported by Source):**  
- Referred to as "older woman/guard"  
- No specific physical appearance details provided  
- Described through role relationships with Sola and other women  

**Costume/Silhouette (Supported by Source):**  
- No specific costume details provided  
- Silhouette only described through age designation as "older"  

**Continuity-Critical Traits:**  
- Replies to narrator's inquiry about prisoner's fate  
- Decides to carry prisoner back to Thark for exhibition at great games before Tal Hajus  
- Reprimands Sola, calling her sentiments "degenerate and unfit for maternity responsibilities under Tars Tarkas"  
- Part of group that criticizes Sola as weak/atavistic  

**Uncertainty Notes:**  
- No physical appearance details (hair, eyes, build, age) provided in chapter  
- No costume or silhouette specifics available  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: hound, companion
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter only mentions "Woola the hound" - no physical description provided  
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity  
clarification_question: What is Woola's full physical description including breed, size, coat color?

[[SECTION markdown]]
# Woola - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Woola  
**Chapter Role:** Hound companion in sleeping quarters  

**Physical Presence:** Mentioned as present in sleeping quarters; no specific scene details provided  

**Physical Description (Supported by Source):**  
- Only described as "Woola the hound"  
- No physical appearance details provided  
- No breed, size, or coat color information available  

**Costume/Silhouette (Supported by Source):**  
- No costume details (animals typically don't wear costumes)  
- Silhouette only described through species designation as "hound"  

**Continuity-Critical Traits:**  
- Present in sleeping quarters with three or four females and young Martians  
- Part of group that carries on desultory conversation before sleep  
- No specific behavioral traits mentioned in chapter  

**Uncertainty Notes:**  
- No physical appearance details (breed, size, coat color) provided in chapter  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_red_one
canonical_character_id: Prisoner
aliases: red one, captive
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter only refers to prisoner as "red one" and mentions harsh treatment - no physical description provided  
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity  
clarification_question: What is the prisoner's full physical description including hair, eyes, build, age appearance?

[[SECTION markdown]]
# Prisoner ("Red One") - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Prisoner (referred to as "red one")  
**Chapter Role:** Captive being discussed and observed  

**Physical Presence:** Briefly glimpsed in audience chamber; conducted to great audience chamber by guards  

**Physical Description (Supported by Source):**  
- Referred to as "red one" - possibly indicating skin tone or appearance  
- Subject of harsh treatment by guards compared to Sola's kindness  
- No specific physical appearance details provided beyond this designation  
- Exchanges words with guards, realizing they speak a common language  

**Costume/Silhouette (Supported by Source):**  
- No costume details provided  
- Silhouette only described through role as prisoner/captive  

**Continuity-Critical Traits:**  
- Subject of conversation among females after her visit to audience chamber  
- Sola expresses hope they would hold her for ransom  
- Criticized by others as weak/atavistic sentiment  
- Decided to be carried back to Thark for exhibition at great games before Tal Hajus  
- Narrator observes prisoner exchanges words with guards  

**Uncertainty Notes:**  
- No physical appearance details (hair, eyes, build, age) provided in chapter  
- "Red one" designation may refer to skin tone or other characteristic - unclear  
- No costume or silhouette specifics available  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character only mentioned by name in reference to previous meeting - no physical description provided  
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity  
clarification_question: What is Lorquas Ptomel's full physical description including hair, eyes, build, age appearance?

[[SECTION markdown]]
# Lorquas Ptomel - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Previous meeting reference (met narrator previously in audience chamber)  

**Physical Presence:** Only referenced by name; no scene presence in chapter  

**Physical Description (Supported by Source):**  
- No physical appearance details provided  
- Only mentioned as having met narrator previously in great audience chamber  
- No specific physical characteristics available  

**Costume/Silhouette (Supported by Source):**  
- No costume details provided  
- Silhouette only described through role as previous meeting reference  

**Continuity-Critical Traits:**  
- Met narrator previously in great audience chamber where prisoner was conducted  
- No other behavioral or interaction traits mentioned in chapter  

**Uncertainty Notes:**  
- No physical appearance details (hair, eyes, build, age) provided in chapter  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character only referenced in speech about maternity responsibilities - no physical description provided  
clarification_required: true
clarification_reason: Character may exist under different name or identification in broader work; needs confirmation of canonical identity  
clarification_question: What is Tars Tarkas's full physical description including hair, eyes, build, age appearance?

[[SECTION markdown]]
# Tars Tarkas - CH009 "I LEARN THE LANGUAGE"

**Display Name:** Tars Tarkas  
**Chapter Role:** Referenced in speech about maternity responsibilities under guardianship  

**Physical Presence:** Only referenced by name; no scene presence in chapter  

**Physical Description (Supported by Source):**  
- No physical appearance details provided  
- Only mentioned in Sarkoja's reprimand of Sola regarding "maternity responsibilities under Tars Tarkas"  
- No specific physical characteristics available  

**Costume/Silhouette (Supported by Source):**  
- No costume details provided  
- Silhouette only described through role as referenced authority figure  

**Continuity-Critical Traits:**  
- Referenced in context of maternity responsibilities and guardianship  
- Sarkoja calls Sola's sentiments "unfit for maternity responsibilities under Tars Tarkas"  
- No other behavioral or interaction traits mentioned in chapter  

**Uncertainty Notes:**  
- No physical appearance details (hair, eyes, build, age) provided in chapter  
- Character may have different canonical identification in broader work  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
