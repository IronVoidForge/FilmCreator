# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:17:18.847473+00:00
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

*Scene 1: Introspection & Departure*
- **Visuals:** Carter sits cross-legged in his chamber (gold/marble mosaics), then moves to the plaza/chariots. Dejah Thoris is in a departing chariot, heavily chained by one ankle to the vehicle side.
- **Story:** Carter reflects on his love for Dejah Thoris and her rejection of him due to his perceived weakness or the situation. He observes her silence and refusal to acknowledge him.

*Scene 2: The Chains & Tars Tarkas*
- **Visuals:** Carter examines the manacles (massive spring lock). Tars Tarkas intervenes, agreeing to hold the key himself rather than Sarkoja.
- **Story:** Sarkoja's cruelty is highlighted by the chains. Tars Tarkas ensures security while allowing for potential escape later.

*Scene 3: Camp Life & Earth Memories*
- **Visuals:** Carter sits cross-legged on silks in camp, moonlit skies.
- **Story:** Carter meditates on love and mortality. He recalls his family in Virginia (Carters), feeling homesick despite being a wanderer.

*Scene 4: Warhoon Incubator Incident*
- **Visuals:** An incubator with small eggs found to the right of the march. Tars Tarkas investigates with warriors. Eggs are demolished.
- **Story:** Discovery of green men's (Warhoons) incubator. Carter asks about egg size differences; Tars Tarkas explains growth period.

*Scene 5: Duel with Zad*
- **Visuals:** Zad strikes Carter's animal with a long-sword. Carter draws his own sword. Community surrounds them, leaving a clear space (100 feet diameter). Long, straight, needle-like swords flash.
- **Story:** Fight initiated by Zar striking the animal. Carter chooses to fight with same weapon. Fight is long and delayed march.

*Scene 6: The Trap & Sacrifice*
- **Visuals:** Blinding flash of light strikes Carter's eyes (mirror). Dejah Thoris throws something from hand (tiny mirror) which spins to ground. Sarkoja aims dagger at Dejah Thoris; Sola sprang between them, knife descending on her shielding breast.
- **Story:** Sarkoja blinds Carter with a mirror while trying to kill him. Dejah Thoris throws the mirror. Sola sacrifices herself to protect Dejah Thoris from Sarkoja's counter-attack during the fight.

*Scene 7: Wounding & Collapse*
- **Visuals:** Carter feels sharp point of sword at breast, throws himself on enemy. Steel tears into chest. Head whirled, knees giving beneath.
- **Story:** Carter is wounded in the duel, collapsing as darkness takes him.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Princess of Mars Chapter CH014

| Character | Role | Presence | Description Status |
|-----------|------|----------|-------------------|
| Carter | Protagonist, central figure | Physically present throughout scenes | Partially described |
| Dejah Thoris | Love interest, noblewoman | Present in Scenes 1, 6 | Partially described |
| Tars Tarkas | Giant warrior, key holder | Present in Scenes 2, 4 | Partially described |
| Sarkoja | Antagonist, cruel figure | Present in Scenes 2, 6 | Partially described |
| Sola | Sacrificial character | Referenced in Scene 6 | Uncertain description |
| Zad/Zar | Dueling opponent | Present in Scene 5 | Partially described |
| Warhoons/Green Men | Incubator inhabitants | Referenced in Scene 4 | Group, no individual details |

*Note: All characters have limited visual description support from chapter summary alone.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides minimal physical description of Carter beyond "sits cross-legged in chamber" and "moves to plaza." No detailed appearance, height, build, or distinctive features are documented. Cannot support dependable image generation without additional visual material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter.md

## Display Name
Carter

## Chapter Role
Protagonist, central figure throughout all seven scenes

## Physical Presence
Physically present in Scenes 1, 3, 5, 7; referenced in Scenes 2, 4, 6

## Physical Description (Supported by Source)
- Sits cross-legged in chamber with gold/marble mosaics
- Moves to plaza area with chariots
- Examines manacles closely
- Meditates on love and mortality
- Recalls family in Virginia (Carters)
- Feels sharp sword wound at breast in Scene 7

## Costume/Silhouette (Supported by Source)
- No specific costume details documented
- Silhouette described through actions rather than appearance
- Wears clothing appropriate for Mars setting (implied)

## Continuity-Critical Traits
- Central to love story with Dejah Thoris
- Subject of Sarkoja's attempts to kill him
- Duelist in combat scenes
- Wounded and collapses in Scene 7

## Render-Facing Prompt Notes
"Male protagonist, sits cross-legged, gold marble chamber background, Mars setting, wounded chest wound scene, contemplative expression, Virginia family memories, sword duel participant"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes Dejah Thoris as "in departing chariot, heavily chained by one ankle" and "throws something from hand (tiny mirror)." No detailed physical appearance, height, build, or distinctive features are documented. Cannot support dependable image generation without additional visual material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# dejah_thoris.md

## Display Name
Dejah Thoris

## Chapter Role
Love interest, noblewoman, central female figure

## Physical Presence
Present in Scenes 1, 6; referenced throughout chapter

## Physical Description (Supported by Source)
- In departing chariot with heavy ankle chain
- Throws tiny mirror from hand
- Silence and refusal to acknowledge Carter noted
- Subject of Sarkoja's counter-attack attempt

## Costume/Silhouette (Supported by Source)
- Noblewoman attire implied (Mars setting)
- Heavy ankle chain visible in Scene 1
- No specific costume details documented

## Continuity-Critical Traits
- Rejection of Carter due to perceived weakness/situation
- Sacrifices herself by throwing mirror to blind Sarkoja's attack
- Protected by Sola's sacrifice
- Central to love story with Carter

## Render-Facing Prompt Notes
"Female noblewoman, Mars setting, chariot scene, tiny mirror in hand, heavy ankle chain visible, contemplative expression, rejection of protagonist, protective gesture"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes Tars Tarkas as "intervenes" and "investigates with warriors." No detailed physical appearance, height, build, or distinctive features are documented. Cannot support dependable image generation without additional visual material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# tars_tarkas.md

## Display Name
Tars Tarkas

## Chapter Role
Giant warrior, key holder, investigator

## Physical Presence
Present in Scenes 2, 4; referenced throughout chapter

## Physical Description (Supported by Source)
- Intervenes in Scene 2 regarding manacles/key
- Investigates incubator with warriors in Scene 4
- Explains egg growth period to Carter
- Agrees to hold key himself rather than Sarkoja

## Costume/Silhouette (Supported by Source)
- Warrior attire implied (Mars setting)
- No specific costume details documented
- Giant warrior status implied through actions

## Continuity-Critical Traits
- Ensures security while allowing potential escape
- Investigates green men's incubator
- Explains Warhoons' egg growth to Carter
- Intervenes in key custody matter

## Render-Facing Prompt Notes
"Giant warrior, Mars setting, investigator role, warrior attire, explains eggs to protagonist, intervenes in key custody, protective stance"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes Sarkoja as "cruelty highlighted by chains" and "aims dagger at Dejah Thoris." No detailed physical appearance, height, build, or distinctive features are documented. Cannot support dependable image generation without additional visual material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# sarkoja.md

## Display Name
Sarkoja

## Chapter Role
Antagonist, cruel figure, dagger wielder

## Physical Presence
Present in Scenes 2, 6; referenced throughout chapter

## Physical Description (Supported by Source)
- Cruelty highlighted by chains in Scene 1
- Aims dagger at Dejah Thoris in Scene 6
- Blinds Carter with mirror attempt
- Counter-attack during fight sequence

## Costume/Silhouette (Supported by Source)
- No specific costume details documented
- Dagger wielder implied
- Antagonist role through actions

## Continuity-Critical Traits
- Highlights cruelty through chain usage
- Attempts to kill Carter with mirror
- Aims dagger at Dejah Thoris
- Counter-attacked during fight sequence

## Render-Facing Prompt Notes
"Female antagonist, Mars setting, cruel expression, dagger in hand, mirror-wielding attempt, aims at protagonist, counter-attack stance, villainous presence"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary only mentions Sola "sprang between them, knife descending on her shielding breast." No physical appearance, height, build, or distinctive features are documented. Cannot support dependable image generation without additional visual material.
clarification_required: true
clarification_reason: Character appears only once in chapter with minimal description. May already exist under another name or be too weakly identified for reliable character tracking.
clarification_question: Is Sola a previously established character from earlier chapters? If so, what is her canonical character ID and full physical description?

[[SECTION markdown]]
# sola.md

## Display Name
Sola

## Chapter Role
Sacrificial character, protector figure

## Physical Presence
Referenced in Scene 6 only; uncertain if physically present

## Physical Description (Supported by Source)
- Sprang between Sarkoja and Dejah Thoris
- Knife descending on her shielding breast
- Sacrifices herself to protect Dejah Thoris

## Costume/Silhouette (Supported by Source)
- No specific costume details documented
- Protective stance implied
- No distinctive features described

## Continuity-Critical Traits
- Sacrifices herself during fight sequence
- Protects Dejah Thoris from Sarkoja's counter-attack
- Single appearance in chapter summary

## Render-Facing Prompt Notes
"Female protector, Mars setting, sacrificial gesture, shielding breast with knife, protective stance between two characters, sacrifice moment"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents. **CLARIFICATION REQUIRED:** Character may already exist under another name from earlier chapters; needs canonical ID verification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: zad
aliases: zar
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes Zad as "strikes Carter's animal with a long-sword" and "draws his own sword." No detailed physical appearance, height, build, or distinctive features are documented. Cannot support dependable image generation without additional visual material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# zad.md

## Display Name
Zad (also spelled Zar)

## Chapter Role
Dueling opponent, sword wielder

## Physical Presence
Present in Scene 5; referenced throughout chapter

## Physical Description (Supported by Source)
- Strikes Carter's animal with long-sword
- Draws own sword for duel
- Fight initiated by Zar striking the animal
- Long and delayed march following fight

## Costume/Silhouette (Supported by Source)
- Warrior attire implied (Mars setting)
- No specific costume details documented
- Sword wielder through actions

## Continuity-Critical Traits
- Initiates duel with Carter
- Uses long-sword in combat
- Fight is long and delayed march
- Community surrounds them leaving clear space

## Render-Facing Prompt Notes
"Male warrior, Mars setting, long-sword in hand, duel participant, strikes animal with sword, draws own weapon, combat stance, community surrounding fight scene"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents. Note: Character name appears as both "Zad" and "Zar" in chapter - may be same person with spelling variation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warhoons_green_men
canonical_character_id: warhoons_green_men
aliases: green men
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary describes Warhoons as "green men" with incubator and eggs found. No individual physical appearance, height, build, or distinctive features are documented for any individual member. Cannot support dependable image generation without additional visual material.
clarification_required: true
clarification_reason: Character group may already exist under another name from earlier chapters. Too weakly identified for reliable individual character tracking - only referenced as group with incubator/eggs.
clarification_question: Are Warhoons/Green Men a previously established character group from earlier chapters? If so, what is their canonical character ID and full physical description for individual members?

[[SECTION markdown]]
# warhoons_green_men.md

## Display Name
Warhoons (also called Green Men)

## Chapter Role
Incubator inhabitants, egg producers

## Physical Presence
Referenced in Scene 4; uncertain if physically present

## Physical Description (Supported by Source)
- Incubator with small eggs found to right of march
- Eggs demolished by Tars Tarkas and warriors
- Green men's incubator discovered
- Carter asks about egg size differences
- Tars Tarkas explains growth period

## Costume/Silhouette (Supported by Source)
- No specific costume details documented
- "Green men" designation implies green coloration
- No individual distinctive features described

## Continuity-Critical Traits
- Incubator discovered during march
- Eggs found and demolished
- Growth period explained to Carter
- Group rather than individual characters

## Render-Facing Prompt Notes
"Group of green-skinned beings, Mars setting, incubator scene, small eggs visible, green coloration implied, group formation, egg producers"

## Uncertainty Notes
**CRITICAL:** No detailed physical appearance documented for any individual member. Height, build, hair color, eye color, facial features, or distinctive markings are not described in chapter summary. Cannot generate reliable images without additional visual material or character design documents. **CLARIFICATION REQUIRED:** Character group may already exist under another name from earlier chapters; needs canonical ID verification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
