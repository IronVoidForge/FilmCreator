# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:26:36.276146+00:00
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

Chapter id: CH014

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

# Chapter Summary: A Duel to the Death (CH014)

## Narrative Overview
This chapter details the departure from Korad and the journey toward Thark. John Carter grapples with his feelings for Dejah Thoris, who avoids him due to perceived humiliation regarding her captivity. The narrative focuses on logistics of travel, security measures involving chains, and a climactic duel with a warrior named Zad that is interrupted by Dejah Thoris's intervention.

## Scene Breakdown

### Scene 1: Departure and Internal Conflict
- **Setting:** Camp near Korad, morning departure for Thark.
- **Action:** Carter reflects on his love for Dejah Thoris while she avoids him. He observes her chained to the chariot.
- **Dialogue:** Discussion with Sola regarding the key to the manacles (held by Sarkoja).
- **Resolution:** Carter intervenes with Tars Tarkas regarding the chains, agreeing to custody of the key for safety until Thark is reached.

### Scene 2: Camp Life and Incubator Incident
- **Setting:** Camp during the march.
- **Action:** Carter observes Zad (o mad) and Sarkoja's interaction. An incubator belonging to Warhoon green men is found; eggs are destroyed by Tars Tarkas' warriors.
- **Lore:** Explanation of egg growth rates on Barsoom (small at laying, growing over five years).

### Scene 3: The Duel with Zad
- **Setting:** Camp halt during the march.
- **Action:** Zad strikes Carter's animal; Carter engages in a duel using long-swords.
- **Combat:** Long fight involving parries and thrusts. Zad blinds Carter with a flash of light (mirror).
- **Climax:** Dejah Thoris, Sola, and Sarkoja watch from the chariot. Dejah Thoris throws the mirror to blind Carter's enemy but Sarkoja attacks her; Sola attempts to shield Dejah Thoris and is struck by Sarkoja's dagger.
- **Ending:** Carter is wounded in the shoulder/chest, blinded momentarily, and collapses as the chapter concludes.

## Visual Continuity Facts

### Character Appearance & Attire
- **John Carter:** Wears silks and furs; divided riding cloths between two thoats (animals).
- **Dejah Thoris:** Queenly carriage, heavily chained by one ankle to chariot side; wears silks and furs.
- **Sarkoja:** Black, venomous look; wields dagger and mirror.
- **Zad:** Hulking brute, uses long-sword.

### Props & Objects
- **Chains/Manacles:** Massive spring lock on Dejah Thoris' ankle; key held by Sarkoja initially.
- **Weapons:** Long-swords (needle-like), short-swords, daggers, hatchets.
- **Mirror:** Small object used to blind Carter during the duel.
- **Incubator:** Little enclosure with small eggs (Warhoon).

### Setting Details
- **Chariot:** Side of vehicle where Dejah Thoris is chained; doorway leading to quarters.
- **Camp:** Moon-haunted ground, velvety carpeting of moss.
- **Sky:** Nearer moon of Barsoom racing through western sky.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: A Duel to the Death (CH014)

| Character | Role in Chapter | Physical Presence | Description Notes |
| :--- | :--- | :--- | :--- |
| **John Carter** | Protagonist, Combatant | Present | Wears silks/furs; riding cloths between thoats. |
| **Dejah Thoris** | Queenly Figure, Captive | Present | Chained by ankle to chariot; wears silks/furs. |
| **Sarkoja** | Antagonist, Duel Observer | Present | Black/venomous look; wields dagger and mirror. |
| **Zad** | Combatant, Warrior | Present | Hulking brute; uses long-sword. |
| **Sola** | Defender, Chariot Occupant | Present (Chariot) | Actions only; physical description sparse. |
| **Tars Tarkas** | Advisor, Chain Custodian | Present (Camp) | Actions only; physical description sparse. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

**Chapter Role:** Protagonist, Combatant, Chain Custodian Agreement.

**Physical Presence:** Present (Camp near Korad, Chariot side, Camp halt).

**Physical Description:** Wears silks and furs. Divided riding cloths between two thoats (animals).

**Costume & Silhouette:** Distinguished by riding attire suitable for Barsoom travel. Silks suggest status or specific cultural dress. Furs indicate practicality against the environment.

**Continuity-Critical Traits:**
-   **Riding Cloths:** Specific arrangement between two animals (thoats).
-   **Chains/Manacles:** Intervenes regarding custody of key for Dejah Thoris' safety.
-   **Combat Style:** Uses long-swords (needle-like) in duel with Zad.

**Uncertainty Notes:** None based on current text; physical description is sufficient for image generation context within the chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

**Chapter Role:** Queenly Figure, Captive, Duel Observer.

**Physical Presence:** Present (Chariot side, Chariot quarters).

**Physical Description:** Wears silks and furs. Heavily chained by one ankle to chariot side.

**Costume & Silhouette:** Queenly carriage suggests regal attire despite captivity. Chains are a major visual element indicating her status as prisoner.

**Continuity-Critical Traits:**
-   **Ankle Chain:** Massive spring lock on ankle; key held by Sarkoja initially, then custody transferred to Carter/Tars Tarkas.
-   **Chariot Attachment:** Chained to side of vehicle; doorway leading to quarters visible.
-   **Combat Intervention:** Throws mirror to blind enemy during duel with Zad.

**Uncertainty Notes:** None based on current text; physical description is sufficient for image generation context within the chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja

**Chapter Role:** Antagonist, Duel Observer, Dagger Wielder.

**Physical Presence:** Present (Chariot side, Camp halt).

**Physical Description:** Black, venomous look. Wields dagger and mirror.

**Costume & Silhouette:** Dark appearance suggests menacing or shadowy aesthetic. Venomous look implies facial expression or aura of danger.

**Continuity-Critical Traits:**
-   **Weapons:** Dagger (used to strike Sola), Mirror (used to blind Carter).
-   **Key Custody:** Initially holds key to Dejah Thoris' manacles.
-   **Combat Action:** Attacks Dejah Thoris during duel intervention; strikes Sola with dagger.

**Uncertainty Notes:** None based on current text; physical description is sufficient for image generation context within the chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: zad
aliases: o mad
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Zad

**Chapter Role:** Combatant, Warrior.

**Physical Presence:** Present (Camp halt during march).

**Physical Description:** Hulking brute. Uses long-sword.

**Costume & Silhouette:** Brute appearance suggests large, possibly muscular build. Long-sword indicates specific combat specialization.

**Continuity-Critical Traits:**
-   **Combat Style:** Engages Carter in duel using long-swords (needle-like).
-   **Blind Flash:** Uses mirror to blind Carter during fight.
-   **Animal Strike:** Strikes Carter's animal before engaging Carter directly.

**Uncertainty Notes:** None based on current text; physical description is sufficient for image generation context within the chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is sparse in the chapter; only actions (shielding Dejah Thoris, being struck by dagger) are described. Visual details for image generation are missing.

[[SECTION markdown]]
# Sola

**Chapter Role:** Defender, Chariot Occupant.

**Physical Presence:** Present (Chariot side).

**Physical Description:** Sparse in chapter text. Actions include shielding Dejah Thoris and being struck by Sarkoja's dagger.

**Costume & Silhouette:** Unknown based on current text. Requires manual description for image generation consistency.

**Continuity-Critical Traits:**
-   **Combat Action:** Attempts to shield Dejah Thoris during duel intervention.
-   **Injury:** Struck by Sarkoja's dagger while shielding Dejah Thoris.

**Uncertainty Notes:** Physical appearance is not described in the chapter summary. Visual details (hair, clothing, build) are missing and must be defined for later image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is sparse in the chapter; only actions (intervening regarding chains, agreeing to custody of key) are described. Visual details for image generation are missing.

[[SECTION markdown]]
# Tars Tarkas

**Chapter Role:** Advisor, Chain Custodian Agreement.

**Physical Presence:** Present (Camp near Korad).

**Physical Description:** Sparse in chapter text. Actions include intervening regarding chains and agreeing to custody of key.

**Costume & Silhouette:** Unknown based on current text. Requires manual description for image generation consistency.

**Continuity-Critical Traits:**
-   **Chain Custody:** Intervenes with Carter regarding chains; agrees to custody of key for safety until Thark is reached.
-   **Warrior Leadership:** Warriors under his command destroy Warhoon green men's incubator eggs.

**Uncertainty Notes:** Physical appearance is not described in the chapter summary. Visual details (hair, clothing, build) are missing and must be defined for later image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
