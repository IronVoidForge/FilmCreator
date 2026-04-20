# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:24:11.847839+00:00
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

Chapter id: CH002

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

**Scene 1: Paralysis and Indian Encounter**
*   **Visual Continuity:** Interior of cave facing cliff opening; dim light from early morning sun; vapor filling cave space; trail visible outside.
*   **Narrative:** Narrator is paralyzed (stone-like) despite mental faculties intact. Sound of approaching horses stops. Apache warriors creep stealthily along the narrow ledge. Warriors see narrator but are awestruck and fearful, unable to pass on the ledge. Moaning sound from behind narrator causes warriors to flee in terror; one brave falls headlong from cliff.
*   **Sensory Details:** Pungent odor of poisonous gas; faint vapor against daylight opening; savage eyes looking into narrator's; low distinct moaning sound.

**Scene 2: Speculation and Silence**
*   **Visual Continuity:** Interior cave remains unchanged; horse standing with dragging rein outside; dead body of friend on ledge within vision range.
*   **Narrative:** Narrator speculates on cause of paralysis (poisonous gas vs unknown). Horse wanders off in search of food/water. Silence persists from late afternoon until midnight.
*   **Sensory Details:** Dragging rein; silence of the dead; faint sounds behind narrator eventually cease.

**Scene 3: Metamorphosis and Liberation**
*   **Visual Continuity:** Interior cave flooded with moonlight; narrator standing facing unknown foe; lifeless body lying on floor.
*   **Narrative:** Awful moan returns at midnight. Narrator breaks free of paralysis via mental effort (will/nerves). Discovers his own body is now dead and naked while he stands clothed and alive. Heart pounding, cold sweat present. Cannot touch revolvers/carbine strapped to lifeless body.
*   **Sensory Details:** Sharp click like snapping steel wire; nausea; rustling sound of dead leaves; quick short gasps for breath; ancient experiment of pinching reveals vitality.

**Scene 4: Flight and Investigation**
*   **Visual Continuity:** Exterior Arizona night; starlight clear sky; rocky gorge vista below; cacti-studded flat; silvered mountains in distance.
*   **Narrative:** Narrator flees cave into starlight. Crisp mountain air acts as tonic. Pauses on ledge, upbraids self for apprehension. Decides to investigate outside. Lifts head to breathe pure night air. Sees beautiful vista of rocky gorge and cacti-studded flat under moonlight.
*   **Sensory Details:** Crisp fresh mountain air; silvered mountains; strange lights and shadows on hog back; grotesque details of stiff yet beautiful cacti.

**Scene 5: Drawn to Mars**
*   **Visual Continuity:** Heavens above landscape; large red star close to distant horizon.
*   **Narrative:** Narration turns gaze from landscape to heavens. Attention riveted by large red star near horizon. Star identified as Mars, god of war. Narrator feels spell of overpowering fascination. Longing beyond opposition; closes eyes, stretches arms toward god of vocation. Feels drawn through trackless immensity of space.
*   **Sensory Details:** Myriad stars forming gorgeous canopy; red star close to horizon; instant of extreme cold and utter darkness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter 002 Character Index

| Asset ID | Canonical Character ID | Role | Presence Status | Description Availability |
| :--- | :--- | :--- | :--- | :--- |
| narrator | narrator_princess_of_mars_ch002 | Protagonist / Observer | Physically Present (Paralyzed then Freed) | Sparse (State only) |
| apache_warriors | apache_warriors_princess_of_mars_ch002 | Antagonists / Witnesses | Physically Present (Ledge) | None (Group Identity) |
| dead_friend | dead_friend_princess_of_mars_ch002 | Deceased Companion | Physically Present (Corpse) | None (Name Unknown) |
| mars | mars_princess_of_mars_ch002 | Celestial Entity / Object | Visually Present (Sky) | Standard Astronomical |

*Note: This index summarizes characters referenced or present in the provided chapter text. Detailed descriptions are noted as sparse due to the nature of the source material.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator_princess_of_mars_ch002
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter text (only state of paralysis/death).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator

**Display Name:** Narrator
**Chapter Role:** Protagonist / Observer
**Presence Status:** Physically Present (Paralyzed then Freed)

**Physical Description:**
The source text does not provide a physical description of the narrator's body in this chapter. The character is described as "stone-like" while paralyzed and later discovers his own body is "dead and naked" while he stands clothed and alive. No gender, age, or specific features are identified in this text.

**Costume & Silhouette:**
Initially described as being unable to move (paralyzed). Later described as standing clothed while the lifeless body on the floor is naked. The narrator's silhouette changes from static/paralyzed to active/moving after breaking free of paralysis.

**Continuity-Critical Traits:**
-   State of consciousness: Intact mental faculties despite physical paralysis.
-   Vitality: Initially paralyzed, later regains movement via mental effort.
-   Body Status: Discovers his own body is dead while he stands alive.

**Uncertainty Notes:**
-   **Name:** Unknown (referred to only as "Narrator").
-   **Gender:** Not specified in this text.
-   **Physical Appearance:** No visual details provided for image generation purposes.
-   **Identity:** Cannot be reliably identified without external context from the full work.

**Render-Facing Prompt Notes:**
Use generic human form placeholders if required, noting "paralyzed state" or "standing alive" as per narrative progression. Avoid specific facial features or clothing styles not mentioned in the source text to maintain continuity with the sparse description provided here.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: apache_warriors_princess_of_mars_ch002
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group identity, no specific physical descriptions provided in this chapter text.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Apache Warriors

**Display Name:** Apache Warriors
**Chapter Role:** Antagonists / Witnesses
**Presence Status:** Physically Present (Ledge)

**Physical Description:**
The source text does not provide specific physical descriptions of the individual warriors in this chapter. They are referred to collectively as "Apache warriors" or a "brave". No facial features, height, or build are detailed in this text.

**Costume & Silhouette:**
No specific costume details are provided for the warriors in this chapter text. They are described as creeping stealthily along the narrow ledge.

**Continuity-Critical Traits:**
-   **Behavior:** Creep stealthily, see narrator but are awestruck/fearful, flee in terror.
-   **Reaction:** One brave falls headlong from cliff due to fear of moaning sound.
-   **Group Dynamic:** Act as a collective force reacting to the narrator's state.

**Uncertainty Notes:**
-   **Names:** None provided (collective noun used).
-   **Individual Appearance:** No visual details for image generation purposes.
-   **Identity:** Cannot be reliably identified without external context from the full work.

**Render-Facing Prompt Notes:**
Use generic indigenous warrior form placeholders if required, noting "stealthy movement" or "fearful reaction" as per narrative progression. Avoid specific facial features or clothing styles not mentioned in the source text to maintain continuity with the sparse description provided here.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dead_friend
canonical_character_id: dead_friend_princess_of_mars_ch002
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Name unknown, no physical description provided in this chapter text.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dead Friend

**Display Name:** Dead Friend
**Chapter Role:** Deceased Companion
**Presence Status:** Physically Present (Corpse)

**Physical Description:**
The source text does not provide a physical description of the friend's body in this chapter. The character is referred to as "dead body of friend" or "lifeless body". No specific features are detailed in this text.

**Costume & Silhouette:**
No specific costume details are provided for the dead friend in this chapter text. The body is described as lying on the floor or ledge within vision range.

**Continuity-Critical Traits:**
-   **State:** Dead/Necrotic.
-   **Location:** On ledge within vision range (Scene 2) / Lying on floor (Scene 3).
-   **Significance:** Witnessed by narrator, triggers speculation on paralysis cause.

**Uncertainty Notes:**
-   **Name:** Unknown (referred to only as "friend").
-   **Physical Appearance:** No visual details for image generation purposes.
-   **Identity:** Cannot be reliably identified without external context from the full work.

**Render-Facing Prompt Notes:**
Use generic human corpse form placeholders if required, noting "lifeless" or "naked" as per narrative progression (Scene 3). Avoid specific facial features or clothing styles not mentioned in the source text to maintain continuity with the sparse description provided here.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mars
canonical_character_id: mars_princess_of_mars_ch002
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Standard celestial object.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Mars

**Display Name:** Mars
**Chapter Role:** Celestial Entity / Object
**Presence Status:** Visually Present (Sky)

**Physical Description:**
The source text identifies the character as a "large red star close to distant horizon" and explicitly states "Star identified as Mars". It is described as the "god of war". Visual description aligns with standard astronomical representation of a red star.

**Costume & Silhouette:**
N/A (Celestial Object).

**Continuity-Critical Traits:**
-   **Appearance:** Large red star near horizon.
-   **Effect:** Exerts spell of overpowering fascination on narrator.
-   **Identification:** Identified as Mars, god of war.

**Uncertainty Notes:**
-   **Name:** Known (Mars).
-   **Physical Appearance:** Standard astronomical representation supported by text.
-   **Identity:** Clearly identified celestial body.

**Render-Facing Prompt Notes:**
Use standard red star visual representation. Note "large" and "close to horizon" as per narrative progression. Avoid anthropomorphic features unless specified in later chapters (not present here).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
