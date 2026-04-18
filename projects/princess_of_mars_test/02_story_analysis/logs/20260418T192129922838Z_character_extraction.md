# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:21:29.922838+00:00
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

# Chapter Summary: A Fair Captive from the Sky (Chapter VIII)

**Plot Overview:**
Following an incubation ceremony, Carter and Sola return to their city but are ordered back immediately upon seeing a fleet of gray airships arriving over the hills. A battle ensues where Carter's warriors demonstrate deadly accuracy against the ships. One vessel is disabled and crashes near the city. Martians loot and burn the ship before dragging a prisoner into a building, who signals Carter with hope then dejection.

**Scene Decomposition & Visual Facts:**

1.  **The Arrival (Visual Continuity):**
    *   **Object:** Twenty gray-painted airships, long and low.
    *   **Details:** Each carries a strange banner from stem to stern; odd devices painted on prows gleam in sunlight.
    *   **Action:** Ships swing slowly over the crest of the nearest hill toward the city.

2.  **The Battle (Visual Continuity):**
    *   **Martian Action:** Green warriors fire a terrific volley from building windows.
    *   **Carter's Action:** Warriors return fire with high accuracy (approx. 75% hit rate).
    *   **Targeting:** Specific points targeted: wireless finding/sighting apparatus, smaller guns, gunners, officers, crew members, upper works, steering gear/propellers.
    *   **Effect:** Banners and upper works dissolve in spurts of flame; vessels swing broadside or turn back to complete circles.

3.  **The Crash (Visual Continuity):**
    *   **Object:** One barely moving craft receives the brunt of fire, appears unmanned.
    *   **Action:** Drifts slowly with light breeze in southeasterly direction; bodies of crew strewn about decks.
    *   **Martian Response:** Warriors rush to roofs, follow retreating armada with fusillade. One ship dips below hill crests until only one is visible.

4.  **The Recovery (Visual Continuity):**
    *   **Action:** Warriors swarm onto the craft from windows just before it strikes buildings.
    *   **Equipment:** Great spears ease collision shock; grappling hooks used to haul boat to ground.
    *   **Loot:** Arms, ammunition, silks, furs, jewels, carved stone vessels, solid foods/liquids, casks of water.

5.  **The Burning (Visual Continuity):**
    *   **Action:** Warriors tow craft far out into valley; empty contents of carboys onto dead sailors/decks.
    *   **Missile:** Last warrior throws missile back onto vessel; faint spurt of flame rises.
    *   **Result:** Guy ropes released; great warship soars majestically into air, decks/upper works a mass of roaring flames. Drifts to southeast, rising higher as flames eat wooden parts.

6.  **The Prisoner (Visual Continuity):**
    *   **Appearance:** Slender, girlish figure similar to earthly women; oval and beautiful face; finely chiseled features; large/lustrous eyes; coal black waving hair caught loosely into strange coiffure; light reddish copper skin; crimson glow of cheeks; ruby lips.
    *   **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments.
    *   **Action:** Dragged roughly into nearby building by green Martian females.
    *   **Interaction:** Eyes meet Carter's; she makes a little sign with free hand (ununderstood); expression shifts from hope/renewed courage to utter dejection/loathing/contempt because he did not answer her signal.

**Continuity Notes:**
*   The city remains deserted for over a week due to fear of return attack by air craft.
*   Carter feels depressed, viewing the scene as defeat of kindred people rather than routing of horde.
*   Sola rushes up to Carter upon his emergence onto street; Lorquas Ptomel remains at deserted city until danger passed.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1
[[SECTION character_index_markdown]]
| Asset ID | Canonical Name | Role | Presence | Description Status |
| :--- | :--- | :--- | :--- | :--- |
| carter | Carter | Leader/Warrior | Referenced | Missing Physical Details |
| sola | Sola | Companion/Leader | Referenced | Missing Physical Details |
| lorquas_ptomel | Lorquas Ptomel | City Guardian | Referenced | Missing Physical Details |
| martian_prisoner | The Prisoner | Captive | Referenced | Detailed Visual Description |
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: Carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of Carter.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Carter (Chapter VIII)

## Display Name
Carter

## Chapter Role
Leader/Warrior

## Presence Status
Referenced (Eyes meet him, emerges onto street)

## Physical Description
*None provided in chapter summary.*

## Costume & Silhouette
*None provided in chapter summary.*

## Continuity-Critical Traits
*None provided in chapter summary.*

## Descriptive Noun Phrases
*Leader of warriors, city dweller.*

## Uncertainty Notes
No physical description available in chapter summary. Manual description required for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of Sola.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola (Chapter VIII)

## Display Name
Sola

## Chapter Role
Companion/Leader

## Presence Status
Referenced (Rushes up to Carter)

## Physical Description
*None provided in chapter summary.*

## Costume & Silhouette
*None provided in chapter summary.*

## Continuity-Critical Traits
*None provided in chapter summary.*

## Descriptive Noun Phrases
*Companion of Carter, city dweller.*

## Uncertainty Notes
No physical description available in chapter summary. Manual description required for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of Lorquas Ptomel.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Lorquas Ptomel (Chapter VIII)

## Display Name
Lorquas Ptomel

## Chapter Role
City Guardian/Leader

## Presence Status
Referenced (Remains at deserted city)

## Physical Description
*None provided in chapter summary.*

## Costume & Silhouette
*None provided in chapter summary.*

## Continuity-Critical Traits
*None provided in chapter summary.*

## Descriptive Noun Phrases
*Guardian of the city, leader.*

## Uncertainty Notes
No physical description available in chapter summary. Manual description required for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_prisoner
canonical_character_id: The Prisoner
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Martian Prisoner (Chapter VIII)

## Display Name
Martian Prisoner

## Chapter Role
Captive

## Presence Status
Referenced (Dragged into building, signals Carter)

## Physical Description
Slender, girlish figure similar to earthly women; oval and beautiful face; finely chiseled features; large/lustrous eyes; coal black waving hair caught loosely into strange coiffure; light reddish copper skin; crimson glow of cheeks; ruby lips.

## Costume & Silhouette
Destitute of clothes, entirely naked save for highly wrought ornaments.

## Continuity-Critical Traits
Signals Carter with hope then dejection. Dragged by green Martian females.

## Descriptive Noun Phrases
Slender girlish figure, oval beautiful face, coal black waving hair, light reddish copper skin, ruby lips, highly wrought ornaments.

## Uncertainty Notes
Identity unknown (referred to as prisoner). Physical description is sufficient for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
