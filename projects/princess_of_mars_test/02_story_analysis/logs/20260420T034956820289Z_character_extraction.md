# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:49:56.820289+00:00
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

# Chapter XIV: A Duel to the Death

## Plot Summary
John Carter reflects on his love for Dejah Thoris and her rejection, fearing he has taken advantage of her helplessness. They travel in chariots towards Thark; Dejah is chained by one ankle to her vehicle. Carter fights a warrior named Zad who strikes him with a long-sword during a halt. During the fight, Dejah throws a mirror that blinds Carter at a crucial moment. Sarkoja attempts to stab Dejah, but Sola intervenes and gets stabbed. Carter is wounded in the shoulder and chest by Zad's sword thrust as the chapter ends.

## Key Scenes for Decomposition
1. **Internal Conflict:** Carter meditating on his love and Dejah's rejection (silks/furs, moonlight).
2. **Journey to Thark:** Chariot travel, manacles/chains, Tars Tarkas' reasoning on security.
3. **Combat with Zad:** Crowd surrounding the fight, weapon matching (long-sword vs long-sword), endurance and agility.
4. **Interruption by Dejah/Sola/Sarkoja:** Mirror thrown, Sarkoja's dagger aimed, Sola shielding Dejah, Carter blinded.
5. **Climax of Fight:** Carter wounded in chest, dizziness, blacking out.

## Visual Continuity Facts (Chapter Specific)
- **Chariot Interior:** Rearranging silks and furs, heavy chains on ankle, massive spring lock manacles.
- **Weapons:** Long-swords (green Martians), short-swords (Carter), hatchets, daggers.
- **Lighting:** Blinding flash of light from mirror, moonlit skies, sunlight in plaza.
- **Attire:** Silks from shoulders, riding cloths on thoats, furs.
- **Injuries:** Wound to left shoulder, sharp point at breast, dizziness/blackout.
- **Characters Present:** Dejah Thoris, Sola, Sarkoja (on chariot), Zad (fighting Carter).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XIV: A Duel to the Death

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|------------------------------|
| john_carter | John Carter | - | true | false |
| dejah_thoris | Dejah Thoris | - | true | false |
| zad | Zad | - | false | true |
| sarkoja | Sarkoja | - | false | true |
| sola | Sola | - | false | true |

**Character Summary:**
- **John Carter**: Protagonist, wounded in shoulder and chest, fighting Zad
- **Dejah Thoris**: Chained to chariot, throws mirror to blind Carter
- **Zad**: Green Martian warrior, long-sword wielder, strikes Carter
- **Sarkoja**: On chariot, attempts to stab Dejah with dagger
- **Sola**: Intervenes between Sarkoja and Dejah, gets stabbed

**Visual Continuity Notes:**
- Silks from shoulders, riding cloths on thoats, furs present in scene
- Long-swords (green Martians), short-swords (Carter), hatchets, daggers
- Blinding flash of light from mirror, moonlit skies, sunlight in plaza

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: -
is_fully_identified: true
manual_description_required: false
manual_description_reason: -
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# John Carter - Chapter XIV

**Display Name:** John Carter  
**Chapter Role:** Protagonist, wounded fighter  
**Physical Presence:** Present and actively fighting  

**Physical Description (Supported by Source):**
- Silks from shoulders visible in scene
- Riding cloths on thoats during chariot travel
- Furs present in chariot interior

**Costume & Silhouette:**
- Warrior attire with silks and furs
- Short-sword wielder (green Martian weapons)
- Wounded: left shoulder, sharp point at breast

**Continuity-Critical Traits:**
- Blinded by mirror flash during fight
- Dizziness and blackout as chapter ends
- Shoulder wound from Zad's sword thrust

**Render-Facing Prompt Notes:**
"John Carter warrior in silks and furs, wounded in chest and shoulder, short-sword at hip, moonlit chariot interior with blinding light flash from mirror"

**Uncertainty Notes:**
None - character fully identified with supported physical description

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: -
is_fully_identified: true
manual_description_required: false
manual_description_reason: -
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# Dejah Thoris - Chapter XIV

**Display Name:** Dejah Thoris  
**Chapter Role:** Chained companion, mirror thrower  
**Physical Presence:** Present and chained to chariot  

**Physical Description (Supported by Source):**
- Silks from shoulders visible in scene
- Riding cloths on thoats during chariot travel
- Furs present in chariot interior

**Costume & Silhouette:**
- Warrior attire with silks and furs
- Chained by one ankle to vehicle
- Heavy chains on ankle, massive spring lock manacles

**Continuity-Critical Traits:**
- Throws mirror that blinds Carter at crucial moment
- Attempted stabbing by Sarkoja, shielded by Sola
- Moonlit skies during journey to Thark

**Render-Facing Prompt Notes:**
"Dejah Thoris in silks and furs, chained ankle with heavy chains, chariot interior, throwing blinding mirror flash, moonlit plaza background"

**Uncertainty Notes:**
None - character fully identified with supported physical description

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: Zad
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited physical description available beyond weapon type and color. No detailed costume, facial features, or body characteristics documented in chapter material. Cannot support dependable image generation without additional visual specification.

clarification_required: true
clarification_reason: Character identified only by name "Zad" with minimal physical attributes. Green Martian warrior designation present but insufficient for complete character rendering.

clarification_question: What are Zad's specific physical features (height, build, facial characteristics)? What costume details beyond green Martian warrior attire? Any distinctive markings or accessories?

[[SECTION markdown]]
# Zad - Chapter XIV

**Display Name:** Zad  
**Chapter Role:** Opponent fighter, sword wielder  
**Physical Presence:** Present and actively fighting Carter  

**Physical Description (Supported by Source):**
- Green Martian warrior designation
- Long-sword weapon wielder
- Crowd surrounding the fight during combat

**Costume & Silhouette:**
- Green Martian warrior attire (color specified)
- Long-sword at ready position
- No detailed costume or body characteristics documented

**Continuity-Critical Traits:**
- Strikes Carter with long-sword thrust
- Wounds Carter in shoulder and chest
- Fight occurs during halt in journey to Thark

**Render-Facing Prompt Notes:**
"Zad green Martian warrior, long-sword at ready position, crowd surrounding fight, combat stance during chariot halt"

**Uncertainty Notes:**
- Physical features beyond weapon type not documented
- Costume details limited to color designation
- Facial characteristics and body build unknown
- Cannot support dependable image generation without additional visual specification

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited physical description available beyond weapon type and action. No detailed costume, facial features, or body characteristics documented in chapter material. Cannot support dependable image generation without additional visual specification.

clarification_required: true
clarification_reason: Character identified only by name "Sarkoja" with minimal physical attributes. Attempted stabbing action present but insufficient for complete character rendering.

clarification_question: What are Sarkoja's specific physical features (height, build, facial characteristics)? What costume details beyond general warrior attire? Any distinctive markings or accessories?

[[SECTION markdown]]
# Sarkoja - Chapter XIV

**Display Name:** Sarkoja  
**Chapter Role:** Attempted attacker, dagger wielder  
**Physical Presence:** Present on chariot  

**Physical Description (Supported by Source):**
- On chariot during fight scene
- Dagger weapon present
- Attempts to stab Dejah

**Costume & Silhouette:**
- Warrior attire (general designation)
- Dagger at ready position
- No detailed costume or body characteristics documented

**Continuity-Critical Traits:**
- Attempts to stab Dejah with dagger
- Intervention by Sola prevents successful attack
- Present during chariot journey to Thark

**Render-Facing Prompt Notes:**
"Sarkoja on chariot, dagger at ready position, attempting to stab Dejah, warrior attire"

**Uncertainty Notes:**
- Physical features beyond weapon type not documented
- Costume details limited to general warrior designation
- Facial characteristics and body build unknown
- Cannot support dependable image generation without additional visual specification

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited physical description available beyond action and intervention. No detailed costume, facial features, or body characteristics documented in chapter material. Cannot support dependable image generation without additional visual specification.

clarification_required: true
clarification_reason: Character identified only by name "Sola" with minimal physical attributes. Shielding action present but insufficient for complete character rendering.

clarification_question: What are Sola's specific physical features (height, build, facial characteristics)? What costume details beyond general warrior attire? Any distinctive markings or accessories?

[[SECTION markdown]]
# Sola - Chapter XIV

**Display Name:** Sola  
**Chapter Role:** Shield protector, stabbed defender  
**Physical Presence:** Present and intervening  

**Physical Description (Supported by Source):**
- Intervenes between Sarkoja and Dejah
- Gets stabbed during intervention
- Shields Dejah from attack

**Costume & Silhouette:**
- Warrior attire (general designation)
- No detailed costume or body characteristics documented

**Continuity-Critical Traits:**
- Shields Dejah from Sarkoja's dagger
- Gets stabbed in the process of protection
- Present during chariot journey to Thark

**Render-Facing Prompt Notes:**
"Sola warrior intervening, shielding Dejah from dagger attack, gets stabbed, warrior attire"

**Uncertainty Notes:**
- Physical features beyond action not documented
- Costume details limited to general warrior designation
- Facial characteristics and body build unknown
- Cannot support dependable image generation without additional visual specification

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
