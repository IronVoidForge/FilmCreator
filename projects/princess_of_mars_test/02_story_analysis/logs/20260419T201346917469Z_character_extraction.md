# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:13:46.917469+00:00
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

Chapter id: CH010

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

# Chapter Summary: CH010 - Champion and Chief

## Scene 1: Bonding Outside City Limits
*   **Action:** John Carter explores outside the city boundaries with Woola, establishing a perfect understanding between them.
*   **Visual Continuity:** Woola acts as a guard dog; his nature is tested but remains loyal. Carter uses Martian tongue to communicate affection.
*   **Outcome:** Carter returns to the city limits before his defection could be discovered by former masters.

## Scene 2: Observation of Dejah Thoris
*   **Action:** Carter regains the plaza and observes Dejah Thoris standing with guards before the entrance to the audience chamber. She gives him a haughty glance and turns her back.
*   **Visual Continuity:** Dejah's posture is described as "earthly womanly," contrasting with typical Martian cruelty. Sola is noted nearby, displaying kindliness.
*   **Context:** Lorquas Ptomel and his retinue approach the building.

## Scene 3: The Audience Chamber Dialogue
*   **Action:** Lorquas Ptomel questions Dejah Thoris about her expedition from Helium. She explains it was a scientific mission to maintain air and water supplies for all humans.
*   **Dialogue:** Dejah pleads for peace between red men (Martians) and green men (Tharks), asking them to return to the ways of common ancestors.
*   **Visual Continuity:** Sarkoja is present, displaying harshness by sinking nails into Dejah's flesh or twisting her arm. The other woman is indifferent.

## Scene 4: The Attack on Dejah Thoris
*   **Action:** A young warrior leaps from the steps and strikes Dejah Thoris a powerful blow across the face, felling her to the floor. He places his foot upon her prostrate form.
*   **Visual Continuity:** Lorquas Ptomel and Tars Tarkas react with silence or smiles; the act is considered a side-splitting witticism in Martian humor.
*   **Outcome:** Dejah Thoris is injured (nosebleed) and vulnerable.

## Scene 5: Carter's Intervention and Combat
*   **Action:** John Carter intervenes, springing upward to strike the brute in the face. He draws his sword and pistol, hooking one leg over the butt of the warrior's pistol while delivering blows to his chest.
*   **Visual Continuity:** The warrior is twelve feet tall and armed to the teeth but sinks bleeding and lifeless to the floor. Carter assumes the regalia of a chieftain due to his victory.
*   **Outcome:** Dejah Thoris is raised in Carter's arms and borne to a bench.

## Scene 6: Recognition and Warning
*   **Action:** Tars Tarkas addresses Carter, noting his proficiency in the Martian tongue (learned from Sola). He warns that failing to kill a warrior in combat would have cost him dearly under Martian customs.
*   **Dialogue:** Lorquas Ptomel offers respect and status as a Tharkian chieftain pending delivery to Tal Hajus. Tars Tarkas notes the danger of keeping prisoners for other purposes.
*   **Visual Continuity:** Carter is now treated as a conqueror; his dead antagonist's chattels (arms, accoutrements) are brought to him.

## Scene 7: Departure from Audience Chamber
*   **Action:** Carter asserts his moral code regarding Dejah Thoris's safety, stating that anyone offering injury must make a full accounting to him. He and Dejah leave the chamber with Woola.
*   **Visual Continuity:** They pass through utter silence; no Martian interferes with them.
*   **Outcome:** The chapter ends with Carter assuming the responsibilities of a chieftain, protecting Dejah Thoris and guided by his conscience.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH010

| Asset ID | Canonical ID | Name | Role | Status |
| :--- | :--- | :--- | :--- | :--- |
| john_carter | john_carter | John Carter | Protagonist / Conqueror | Present |
| woola | woola | Woola | Companion / Guard Dog | Present |
| dejah_thoris | dejah_thoris | Dejah Thoris | Princess / Subject of Protection | Present |
| lorquas_ptomel | lorquas_ptomel | Lorquas Ptomel | Tharkian Chieftain / Interrogator | Present |
| sola | sola | Sola | Martian Language Teacher (Referenced) | Referenced |
| tars_tarkas | tars_tarkas | Tars Tarkas | Tharkian Leader / Advisor | Present |
| sarkoja | sarkoja | Sarkoja | Antagonist / Other Woman | Present |
| young_warrior | young_warrior | Young Warrior (The Brute) | Attacker / Combatant | Present |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: Carter, the conqueror
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text mentions proficiency in Martian tongue and possession of sword/pistol, but lacks specific physical descriptors (hair color, skin tone, height) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

## Display Name & Role
**John Carter** (also known as **Carter**, the **conqueror**)
Primary role in Chapter CH010: Protagonist, Intervener, Protector of Dejah Thoris.

## Physical Presence
**Present.** Actively explores outside city limits with Woola, intervenes in combat, and leaves the audience chamber with Dejah Thoris.

## Physical Description (Supported by Source)
- **Attire:** Assumes regalia of a chieftain after victory; armed with sword and pistol.
- **Action:** Capable of springing upward to strike brutes; assumes moral responsibility for safety.
- **Language:** Proficient in Martian tongue (learned from Sola).

## Costume & Silhouette
- **Weaponry:** Sword, pistol.
- **Status:** Treated as a conqueror; dead antagonist's chattels brought to him.

## Continuity-Critical Traits
- **Moral Code:** Asserts that anyone offering injury must make full accounting to him.
- **Leadership:** Assumes responsibilities of a chieftain, protecting Dejah Thoris.

## Uncertainty Notes
- Specific physical features (e.g., hair color, eye color) are not described in this chapter's text.
- Height and build are implied by combat capability but not explicitly stated.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: guard dog, Woola (dog)
is_fully_identified: true
manual_description_required: true
manual_description_reason: Described only as a "guard dog" with tested nature; lacks specific breed, coat color, or size details for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola

## Display Name & Role
**Woola** (also known as **guard dog**)
Primary role in Chapter CH010: Companion, Guard Dog, Silent Witness.

## Physical Presence
**Present.** Explores outside city limits with Carter; accompanies them through the audience chamber.

## Physical Description (Supported by Source)
- **Function:** Acts as a guard dog; nature tested but remains loyal.
- **Communication:** Uses Martian tongue to communicate affection (implied bond).

## Costume & Silhouette
- **Role:** Guard dog accompanying Carter.
- **Behavior:** Silent witness in scenes of combat and departure.

## Continuity-Critical Traits
- **Loyalty:** Remains loyal despite the nature being tested.
- **Bond:** Perfect understanding between him and Carter established outside city limits.

## Uncertainty Notes
- Specific breed, fur color, or size are not described in this chapter's text.
- Visual appearance is limited to functional description ("guard dog").

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: Dejah, the earthly womanly
is_fully_identified: true
manual_description_required: true
manual_description_reason: Posture described as "earthly womanly" and injured (nosebleed), but lacks specific physical features (hair color, eyes) for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

## Display Name & Role
**Dejah Thoris** (also known as **Dejah**, the **earthly womanly**)
Primary role in Chapter CH010: Princess, Subject of Protection, Interrogated.

## Physical Presence
**Present.** Standing with guards before entrance to audience chamber; injured during attack; borne to bench by Carter.

## Physical Description (Supported by Source)
- **Posture:** Described as "earthly womanly," contrasting with typical Martian cruelty.
- **Injury:** Suffers a powerful blow across face; nosebleed; vulnerable on floor.
- **Interaction:** Gives haughty glance and turns back to Carter initially.

## Costume & Silhouette
- **Status:** Injured, prostrate form during attack; raised in Carter's arms.
- **Attitude:** Haughty glance; indifferent to Sarkoja's harshness (implied by context).

## Continuity-Critical Traits
- **Peace Plea:** Pledges for peace between red men (Martians) and green men (Tharks).
- **Protection:** Carter asserts moral code regarding her safety.
- **Departure:** Leaves chamber with Carter and Woola through utter silence.

## Uncertainty Notes
- Specific physical features (e.g., hair color, eye color) are not described in this chapter's text.
- Visual appearance is limited to functional description ("earthly womanly") and injury state.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: Lorquas, the Tharkian chieftain (pending delivery)
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in text; only actions and dialogue are described.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

## Display Name & Role
**Lorquas Ptomel** (also known as **the Tharkian chieftain**)
Primary role in Chapter CH010: Interrogator, Respectful Observer.

## Physical Presence
**Present.** Approaches building with retinue; questions Dejah Thoris; offers respect and status to Carter.

## Physical Description (Supported by Source)
- **Action:** Questions Dejah Thoris about expedition from Helium.
- **Reaction:** Offers respect and status as a Tharkian chieftain pending delivery to Tal Hajus.

## Costume & Silhouette
- **Role:** Approaches building with retinue; treated as a figure of authority.
- **Interaction:** Silent or smiling reaction to attack on Dejah Thoris (implied by context).

## Continuity-Critical Traits
- **Status:** Offers respect and status to Carter.
- **Warning:** Notes danger of keeping prisoners for other purposes (via Tars Tarkas).

## Uncertainty Notes
- Specific physical features (e.g., hair color, eye color) are not described in this chapter's text.
- Visual appearance is limited to functional description ("approaches building").

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: Sola, the Martian tongue teacher
is_fully_identified: true
manual_description_required: true
manual_description_reason: Referenced only ("learned from Sola"); no physical description provided in this chapter's text.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

## Display Name & Role
**Sola** (also known as **the Martian tongue teacher**)
Primary role in Chapter CH010: Referenced Mentor, Language Source.

## Physical Presence
**Referenced.** Not physically present in this chapter's scenes; mentioned regarding Carter's language proficiency.

## Physical Description (Supported by Source)
- **Role:** Source of Carter's Martian tongue proficiency.
- **Context:** Mentioned in Scene 6 dialogue between Tars Tarkas and Lorquas Ptomel.

## Costume & Silhouette
- **Status:** Not visually described in this chapter.
- **Interaction:** Implied connection to Carter through language learning.

## Continuity-Critical Traits
- **Language:** Carter learned Martian tongue from her.
- **Connection:** Serves as a bridge between Carter and Tharkian culture (implied).

## Uncertainty Notes
- Specific physical features (e.g., hair color, eye color) are not described in this chapter's text.
- Visual appearance is limited to functional description ("learned from Sola").

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: Tars, the Tharkian leader
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in text; only actions and dialogue are described.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

## Display Name & Role
**Tars Tarkas** (also known as **the Tharkian leader**)
Primary role in Chapter CH010: Advisor, Combatant, Authority Figure.

## Physical Presence
**Present.** Reacts with silence or smiles to attack on Dejah Thoris; addresses Carter regarding customs.

## Physical Description (Supported by Source)
- **Action:** Addresses Carter regarding proficiency in Martian tongue and customs.
- **Reaction:** Silent or smiling reaction to attack on Dejah Thoris.

## Costume & Silhouette
- **Role:** Tharkian leader/authority figure.
- **Interaction:** Warns about danger of keeping prisoners for other purposes.

## Continuity-Critical Traits
- **Customs:** Notes that failing to kill a warrior in combat would have cost Carter dearly under Martian customs.
- **Status:** Treats Carter as a conqueror; brings dead antagonist's chattels to him.

## Uncertainty Notes
- Specific physical features (e.g., hair color, eye color) are not described in this chapter's text.
- Visual appearance is limited to functional description ("reacts with silence or smiles").

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: Sarkoja, the other woman
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in text; only actions and dialogue are described.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja

## Display Name & Role
**Sarkoja** (also known as **the other woman**)
Primary role in Chapter CH010: Antagonist, Observer of Harshness.

## Physical Presence
**Present.** Present during audience chamber dialogue; displays harshness by sinking nails into Dejah's flesh or twisting her arm.

## Physical Description (Supported by Source)
- **Action:** Displays harshness by sinking nails into Dejah's flesh or twisting her arm.
- **Attitude:** Indifferent to the situation compared to others.

## Costume & Silhouette
- **Role:** Antagonist/Observer of harshness.
- **Interaction:** Indifferent to the attack on Dejah Thoris (implied by context).

## Continuity-Critical Traits
- **Harshness:** Displays harshness by sinking nails into Dejah's flesh or twisting her arm.
- **Status:** Present during audience chamber dialogue; indifferent to the situation.

## Uncertainty Notes
- Specific physical features (e.g., hair color, eye color) are not described in this chapter's text.
- Visual appearance is limited to functional description ("displays harshness").

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_warrior
canonical_character_id: young_warrior
aliases: the brute, the twelve-foot tall warrior
is_fully_identified: false
manual_description_required: true
manual_description_reason: Unnamed in text ("a young warrior", "the brute"); lacks specific physical features (hair color, skin tone) for image generation.
clarification_required: true
clarification_reason: Character is unnamed and might exist under another name or be too weakly identified for stable image generation.
clarification_question: Does this character have a proper name in the source material, or should he remain "the young warrior" / "the brute"?

[[SECTION markdown]]
# Young Warrior (The Brute)

## Display Name & Role
**Young Warrior** (also known as **the brute**, **the twelve-foot tall warrior**)
Primary role in Chapter CH010: Attacker, Combatant.

## Physical Presence
**Present.** Leaps from steps and strikes Dejah Thoris; sinks bleeding and lifeless to floor after Carter's intervention.

## Physical Description (Supported by Source)
- **Height:** Twelve feet tall.
- **Armament:** Armed to the teeth with sword and pistol.
- **Action:** Strikes Dejah Thoris a powerful blow across face; places foot upon her prostrate form.
- **Outcome:** Sinks bleeding and lifeless to floor after being struck by Carter.

## Costume & Silhouette
- **Weaponry:** Sword, pistol (hooked over butt of warrior's pistol).
- **Status:** Armed to the teeth; dead antagonist's chattels brought to Carter.

## Continuity-Critical Traits
- **Combat:** Considered a side-splitting witticism in Martian humor for the act.
- **Victory:** Carter assumes regalia of a chieftain due to victory over him.
- **Death:** Sinks bleeding and lifeless to floor; dead antagonist's chattels brought to Carter.

## Uncertainty Notes
- Specific physical features (e.g., hair color, skin tone) are not described in this chapter's text.
- Name is not provided in text ("a young warrior", "the brute").
- Visual appearance is limited to functional description ("armed to the teeth").

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
