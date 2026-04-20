# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:32:17.702420+00:00
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

Chapter id: CH006

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

# Chapter Summary: A Fight That Won Friends

## Scene 1: The Bull Ape Confrontation
**Action:** The protagonist is pinned to the ground by a bull ape holding him with one huge foot. The ape jabbers and gesticulates at another creature behind it. A mate approaches bearing a mighty stone cudgel intended to brain the protagonist.
**Visual Continuity:** The bull ape is described as having intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, and snouts/teeth like an African gorilla. It is "not unlovely" compared to green Martians.
**Climax:** A bolt of myriad-legged horror (the beast) hurled itself through the doorway onto the executioner's breast. The ape holding the protagonist leaps through the window, but its mate engages in a death struggle with the beast.

## Scene 2: The Battle and Protagonist's Intervention
**Action:** The protagonist witnesses the battle between the beast and the bull ape. The beast gains an advantage by sinking fangs into the ape's breast, but the ape locks the throat of the guardian. The beast weakens (eyes bulging, blood from nostrils).
**Visual Continuity:** Both creatures roll back and forth on the floor without emitting sound of fear or pain. The beast's eyes bulge completely from sockets; blood flows from nostrils.
**Intervention:** The protagonist gains his feet, backs against the wall, and seizes the cudgel. He crashes it full upon the head of the ape, crushing his skull as though it had been an eggshell.

## Scene 3: Arrival of Tars Tarkas and Warriors
**Action:** Immediately after the blow, a new danger appears. The bull ape's mate returns to the scene roaring in rage at his lifeless fellow. The protagonist considers flight but is drawn back by the beast's pitiful appeal for protection.
**Visual Continuity:** The protagonist throws the cudgel as heavily as possible at the advancing bulk of the mate, striking him just below the knees. He follows with a smashing left to the pit of the stomach.
**Resolution:** The mate reeled and fell upon the floor doubled up with pain. The protagonist leaps over his prostrate body and finishes the monster before he could regain his feet.

## Scene 4: Martians Witness the Victory
**Action:** A low laugh rings out behind the protagonist. He turns to behold Tars Tarkas, Sola, and three or four warriors standing in the doorway. They offer zealously guarded applause for his feats.
**Visual Continuity:** The Martians are devoid of finer sentiments; they worship physical prowess. Sola is sober with apparent solicitude, unlike others whose faces were twisted in laughter. She rushes to examine the protagonist's body for wounds.

## Scene 5: Saving the Beast from Execution
**Action:** Tars Tarkas and warriors enter and stand over the rapidly reviving brute (the beast). They seem deep in argument. A warrior draws an evil-looking pistol intending to put an end to the creature.
**Visual Continuity:** The protagonist springs forward and strikes up the warrior's arm. The bullet striking the wooden casing of the window explodes, blowing a hole completely through the wood and masonry.
**Resolution:** The protagonist kneels beside the beast, raises it to its feet, and motions for it to follow him. The Martians look on with ludicrous surprise.

## Scene 6: Return to the Plaza
**Action:** Tars Tarkas signs that the protagonist be left to his own devices. They return to the plaza with the great beast following close at heel. Sola grasps the protagonist tightly by the arm.
**Visual Continuity:** The beast follows close at heel; Sola grasps me tightly by the arm.
**Conclusion:** The protagonist now has two friends on Mars: a young woman (Sola) and a dumb brute (the beast).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH006

## The Protagonist (John Carter)
- **Role:** Main character, central figure in all scenes
- **Status:** Physically present throughout the chapter
- **Description:** Limited physical details provided; primarily identified through actions and interactions

## Tars Tarkas
- **Role:** Martian warrior, leader of the Martians
- **Status:** Appears in doorway during victory celebration
- **Description:** Martian warrior with no specific physical features detailed in chapter summary

## Sola
- **Role:** Young woman/Martian, protagonist's friend
- **Status:** Approaches protagonist after battle, examines for wounds
- **Description:** Sober demeanor unlike other laughing Martians; shows concern for protagonist

## The Bull Ape (The Beast)
- **Role:** Central creature in fight scenes
- **Status:** Physically present throughout action sequences
- **Description:** Gorilla-like with intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, snouts/teeth like African gorilla

## The Bull Ape's Mate
- **Role:** Second bull ape in fight scenes
- **Status:** Approaches after first bull ape is killed
- **Description:** Similar physical characteristics to first bull ape; engages in death struggle with beast
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: john_carter
aliases: "me", "protagonist"
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary only mentions protagonist's actions and reactions, no specific physical features like height, build, hair color, or distinctive marks"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Protagonist - Character File

## Display Name
The Protagonist (John Carter)

## Chapter Role
Main character, central figure in all scenes

## Physical Presence
Physically present throughout the chapter

## Physical Description
Limited details provided in chapter summary. The protagonist is primarily identified through actions and interactions rather than physical features. No specific height, build, hair color, or distinctive marks are mentioned in the source material.

## Costume and Silhouette
No costume details provided in chapter summary. Silhouette not described beyond general human form implied by context of Mars setting.

## Continuity-Critical Traits
- Central figure in all action sequences
- Receives wounds examined by Sola
- Uses cudgel as weapon against bull apes
- Saves the beast from execution
- Gains two friends on Mars (Sola and the beast)

## Descriptive Noun Phrases for Render-Facing Prompts
- "protagonist of Mars adventure"
- "young man with determined expression"
- "witness to Martian battle"
- "hero saving creature from execution"
- "friend to both woman and beast"

## Uncertainty Notes
Physical appearance details are uncertain due to limited description in chapter summary. Height, build, hair color, eye color, and distinctive marks cannot be reliably determined from source material. Costume and accessories not described beyond general context of Mars setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: "Martian warrior"
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary only mentions Tars Tarkas as a Martian warrior with no specific physical features like height, build, or distinctive marks"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Tars Tarkas - Character File

## Display Name
Tars Tarkas

## Chapter Role
Martian warrior, leader of the Martians

## Physical Presence
Appears in doorway during victory celebration (Scene 4) and enters with warriors (Scene 5)

## Physical Description
Limited details provided in chapter summary. Identified as a Martian warrior but no specific physical features like height, build, or distinctive marks are mentioned in the source material.

## Costume and Silhouette
No costume details provided in chapter summary. Silhouette not described beyond general human form implied by context of Mars setting.

## Continuity-Critical Traits
- Signs that protagonist be left to his own devices (Scene 6)
- Enters with warriors to stand over the reviving beast (Scene 5)
- Offers zealously guarded applause for protagonist's feats (Scene 4)
- Appears sober with apparent solicitude unlike other laughing Martians

## Descriptive Noun Phrases for Render-Facing Prompts
- "Martian warrior leader"
- "figure in doorway offering applause"
- "warrior deep in argument with others"
- "leader returning to plaza with beast"
- "Martian devoid of finer sentiments"

## Uncertainty Notes
Physical appearance details are uncertain due to limited description in chapter summary. Height, build, hair color, eye color, and distinctive marks cannot be reliably determined from source material. Costume and accessories not described beyond general context of Mars setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: "young woman", "Martian woman"
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary only mentions Sola as a young woman with no specific physical features like height, build, or distinctive marks"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Sola - Character File

## Display Name
Sola

## Chapter Role
Young woman/Martian, protagonist's friend

## Physical Presence
Appears in doorway during victory celebration (Scene 4) and grasps protagonist by arm (Scene 6)

## Physical Description
Limited details provided in chapter summary. Identified as a young woman but no specific physical features like height, build, or distinctive marks are mentioned in the source material.

## Costume and Silhouette
No costume details provided in chapter summary. Silhouette not described beyond general human form implied by context of Mars setting.

## Continuity-Critical Traits
- Sober with apparent solicitude unlike others whose faces were twisted in laughter (Scene 4)
- Rushes to examine protagonist's body for wounds (Scene 4)
- Grasps protagonist tightly by the arm (Scene 6)
- Represents protagonist's two friends on Mars along with the beast (Conclusion)

## Descriptive Noun Phrases for Render-Facing Prompts
- "young woman showing concern"
- "Martian with sober demeanor"
- "figure examining wounds with care"
- "friend grasping arm tightly"
- "young woman among laughing Martians"

## Uncertainty Notes
Physical appearance details are uncertain due to limited description in chapter summary. Height, build, hair color, eye color, and distinctive marks cannot be reliably determined from source material. Costume and accessories not described beyond general context of Mars setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape
canonical_character_id: bull_ape
aliases: "the beast", "brute"
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary only mentions the bull ape as having intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, and snouts/teeth like an African gorilla. No specific height, build, or distinctive marks"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# The Bull Ape - Character File

## Display Name
The Bull Ape (The Beast)

## Chapter Role
Central creature in fight scenes, protagonist's friend

## Physical Presence
Physically present throughout action sequences (Scene 1-3) and follows close at heel after victory (Conclusion)

## Physical Description
Gorilla-like with intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, snouts/teeth like African gorilla. Not unlovely compared to green Martians. Eyes bulge completely from sockets; blood flows from nostrils during battle.

## Costume and Silhouette
No costume details provided in chapter summary. Silhouette not described beyond general ape form with intermediary arms/legs.

## Continuity-Critical Traits
- Pinned to ground by bull ape holding protagonist (Scene 1)
- Bull ape's mate approaches bearing mighty stone cudgel (Scene 1)
- Beast gains advantage by sinking fangs into ape's breast (Scene 2)
- Ape locks throat of guardian (Scene 2)
- Protagonist finishes the monster before it could regain feet (Scene 3)
- Tars Tarkas and warriors stand over rapidly reviving brute (Scene 5)
- Beast follows close at heel after victory (Conclusion)

## Descriptive Noun Phrases for Render-Facing Prompts
- "gorilla-like creature with intermediary limbs"
- "beast with high-set lateral ears"
- "creature not unlovely compared to Martians"
- "brute with bulging eyes and blood from nostrils"
- "dumb brute following close at heel"

## Uncertainty Notes
Physical appearance details are uncertain due to limited description in chapter summary. Height, build, weight, and distinctive marks cannot be reliably determined from source material beyond the gorilla-like characteristics mentioned. Costume and accessories not described beyond general context of Mars setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape_mate
canonical_character_id: bull_ape_mate
aliases: "bull ape's mate", "mate"
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary only mentions the bull ape's mate as having intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, and snouts/teeth like an African gorilla. No specific height, build, or distinctive marks"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# The Bull Ape's Mate - Character File

## Display Name
The Bull Ape's Mate

## Chapter Role
Second bull ape in fight scenes, antagonist to protagonist

## Physical Presence
Approaches after first bull ape is killed (Scene 3) and engages in death struggle with beast (Scene 1)

## Physical Description
Similar physical characteristics to first bull ape: intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, snouts/teeth like African gorilla. Roaring in rage at lifeless fellow.

## Costume and Silhouette
No costume details provided in chapter summary. Silhouette not described beyond general ape form with intermediary arms/legs.

## Continuity-Critical Traits
- Approaches bearing mighty stone cudgel intended to brain protagonist (Scene 1)
- Returns roaring in rage at lifeless fellow (Scene 3)
- Protagonist throws cudgel at advancing bulk just below knees (Scene 3)
- Protagonist follows with smashing left to pit of stomach (Scene 3)
- Mate reeled and fell upon floor doubled up with pain (Scene 3)

## Descriptive Noun Phrases for Render-Facing Prompts
- "second bull ape approaching in rage"
- "mate roaring at lifeless fellow"
- "ape with intermediary arms and legs"
- "creature advancing bulk below knees"
- "bull ape mate doubled up with pain"

## Uncertainty Notes
Physical appearance details are uncertain due to limited description in chapter summary. Height, build, weight, and distinctive marks cannot be reliably determined from source material beyond the gorilla-like characteristics mentioned. Costume and accessories not described beyond general context of Mars setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
