# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:17:26.123442+00:00
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

# Chapter II: The Escape of the Dead - Scene Decomposition Summary

## Opening Sequence (Cave Interior)
- Protagonist experiences paralysis in cave opening to daylight
- Muscles refuse to respond to will despite mental faculties intact
- Vapor filling cave, tenuous and only noticeable against daylight opening
- Faintly pungent odor from poisonous gas assumption
- Early morning sun falling full upon protagonist through opening

## Apache Warrior Appearance (Visual Continuity)
- Stealthy sound apprises of nearness
- War-bonneted, paint-streaked face thrust cautiously around cliff shoulder
- Savage eyes looking into protagonist's eyes in dim light
- Multiple faces appear: awe and fear expressions visible
- Leaders pass whispered words to braves behind them on narrow ledge

## Entity Behind Protagonist (Mysterious Presence)
- Low but distinct moaning sound issues from recesses of cave behind protagonist
- Apache warriors turn and flee in terror, panic-stricken
- One brave hurled headlong from cliff to rocks below during escape
- Wild cries echo in canyon then all still once more
- Sound not repeated but sufficient to start speculation on horror at back

## Protagonist's Paralysis State (Physical Continuity)
- Held paralyzed with back toward horrible and unknown danger
- Ferocious Apache warriors turn in wild stampede from sound
- Several faint sounds behind cease, protagonist left without interruption
- Vague conjecture about cause of paralysis
- Hope it might pass off as suddenly as fallen upon him

## Escape Sequence (Cave to Exterior)
- Late afternoon horse starts slowly down trail searching for food and water
- Protagonist alone with mysterious unknown companion and dead body of friend
- Silence from possibly midnight until morning moan breaks on startled ears
- Superhuman effort to break awful bonds: mind, will, nerves not muscular
- Sharp click as of snapping steel wire, nausea feeling
- Moonlight floods cave, protagonist discovers own body lying lifeless and clothed
- Protagonist stands naked while body remains clothed and lifeless

## Final Escape (Arizona Night Landscape)
- Protagonist leaps through opening into starlight of clear Arizona night
- Crisp fresh mountain air acts as immediate tonic
- Pausing on brink of ledge, upbraids self for unwarranted apprehension
- Better judgment convinces noises resulted from natural causes
- Lifts head to fill lungs with pure invigorating night air
- Sees beautiful vista of rocky gorge and cacti-studded flat under moonlight

## Mars Encounter (Space Transition)
- Attention riveted by large red star close to distant horizon
- Spell of overpowering fascination—it is Mars, god of war
- Fighting man feels irresistible enchantment from Mars
- Longing beyond power of opposition
- Closes eyes, stretches arms toward god of vocation
- Felt drawn with suddenness of thought through trackless immensity of space
- Instant of extreme cold and utter darkness

## Key Visual Continuity Points for Scene Decomposition
- Cave interior lighting: early morning sun → moonlight → starlight
- Character states: paralyzed clothed body → mobile naked protagonist
- Apache warrior reactions: cautious approach → terror flight → cliff fall
- Landscape transitions: cave opening → Arizona night exterior
- Sky elements: myriad stars → large red Mars star
- Space transition mechanics: cold, darkness, suddenness
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter II: The Escape of the Dead

| Character | Status | Physical Presence | Description Available |
|-----------|--------|-------------------|----------------------|
| Protagonist | Primary | Present (cave interior) | None - requires manual description |
| Apache Warriors (Leaders/Braves) | Secondary | Present (cliff exterior) | Partial - war-bonneted, paint-streaked faces |
| Dead Friend's Body | Referenced | Deceased (cave interior) | Minimal - clothed body only |

**Note:** All characters lack stable identification and physical descriptions sufficient for image generation. Manual descriptions required for all entries.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description, costume details, or facial features provided in chapter text. Protagonist's appearance is entirely unspecified beyond being clothed then naked after escape.
clarification_required: true
clarification_reason: Character lacks proper name and stable identification. Cannot determine if this is a known character type or needs specific identity clarification.
clarification_question: What is the protagonist's name, age, gender, race, and physical appearance (height, build, hair color, eye color)?

[[SECTION markdown]]
# Protagonist - Chapter II Character File

**Display Name:** Protagonist  
**Chapter Role:** Primary character experiencing paralysis, escape, and Mars encounter  
**Physical Presence:** Present in cave interior throughout opening sequence; becomes mobile after escape  

**Physical Description:** None available in source text. Protagonist is described as clothed initially, then naked after discovering paralyzed body. No facial features, body type, or distinguishing characteristics documented.

**Costume/Silhouette:** Initially clothed (garments unspecified), later naked while original body remains clothed and lifeless. No costume details beyond basic clothing state.

**Continuity-Critical Traits:** 
- State of paralysis (mind/will intact, muscles unresponsive)
- Transition from clothed to naked protagonist
- Experience of Mars encounter as fighting man feeling enchantment

**Render-Facing Prompt Notes:** Requires complete physical description specification for image generation. Cannot proceed with visual representation without manual description input.

**Uncertainty Notes:** 
- No name provided in chapter text
- Physical appearance entirely unspecified
- Race, age, gender not documented
- Facial features and body type unknown
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors_leaders
canonical_character_id: apache_warriors_leaders
aliases: leaders, chiefs
is_fully_identified: false
manual_description_required: true
manual_description_reason: Multiple warriors described collectively but no individual physical details provided. Only group characteristics (war-bonneted, paint-streaked faces) documented without specific measurements or features.
clarification_required: true
clarification_reason: Character lacks proper names and stable identification. Cannot determine if these are specific named individuals or generic warrior types requiring clarification.
clarification_question: Are the Apache warriors leaders named individuals or generic character types? What are their individual physical descriptions, names, and distinguishing features?

[[SECTION markdown]]
# Apache Warriors (Leaders) - Chapter II Character File

**Display Name:** Apache Warriors (Leaders)  
**Chapter Role:** Secondary characters approaching protagonist before escape sequence  
**Physical Presence:** Present on cliff exterior; approach cautiously then flee in terror  

**Physical Description:** War-bonneted with paint-streaked faces, savage eyes. Multiple faces appear showing awe and fear expressions. No individual physical measurements or features documented beyond collective group characteristics.

**Costume/Silhouette:** War-bonneted headwear, face paint streaks visible. Silhouette described as thrusting cautiously around cliff shoulder. No specific costume details beyond war attire.

**Continuity-Critical Traits:** 
- Cautious approach to protagonist
- Terror flight upon hearing moaning sound
- One leader hurled headlong from cliff during escape
- Whispered words between leaders and braves

**Render-Facing Prompt Notes:** Requires individual physical descriptions for each warrior. Cannot proceed with visual representation without manual description input for specific individuals.

**Uncertainty Notes:** 
- No names provided for individual warriors
- Physical appearance only partially documented (collective traits)
- Individual facial features, body types unknown
- Specific costume details beyond war attire unspecified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors_braves
canonical_character_id: apache_warriors_braves
aliases: braves, warriors behind leaders
is_fully_identified: false
manual_description_required: true
manual_description_reason: Multiple braves described collectively without individual physical details. Only group characteristics documented (turning to flee, passing whispered words) without specific measurements or features.
clarification_required: true
clarification_reason: Character lacks proper names and stable identification. Cannot determine if these are specific named individuals or generic warrior types requiring clarification.
clarification_question: Are the Apache braves named individuals or generic character types? What are their individual physical descriptions, names, and distinguishing features?

[[SECTION markdown]]
# Apache Warriors (Braves) - Chapter II Character File

**Display Name:** Apache Warriors (Braves)  
**Chapter Role:** Secondary characters following leaders; flee in terror upon hearing moaning sound  
**Physical Presence:** Present on cliff exterior behind leaders; turn and flee during escape sequence  

**Physical Description:** War-bonneted with paint-streaked faces, savage eyes. Multiple faces appear showing awe and fear expressions. No individual physical measurements or features documented beyond collective group characteristics.

**Costume/Silhouette:** War-bonneted headwear, face paint streaks visible. Silhouette described as passing whispered words to braves behind them on narrow ledge. No specific costume details beyond war attire.

**Continuity-Critical Traits:** 
- Following leaders on narrow cliff ledge
- Turning and fleeing in terror upon hearing moaning sound
- Several faint sounds cease during escape sequence
- One brave hurled headlong from cliff to rocks below

**Render-Facing Prompt Notes:** Requires individual physical descriptions for each warrior. Cannot proceed with visual representation without manual description input for specific individuals.

**Uncertainty Notes:** 
- No names provided for individual braves
- Physical appearance only partially documented (collective traits)
- Individual facial features, body types unknown
- Specific costume details beyond war attire unspecified
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dead_friend_body
canonical_character_id: dead_friend_body
aliases: friend's body, deceased companion
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced as "dead body of friend" with no physical description provided. No name, age, race, or physical features documented beyond being clothed and lifeless.
clarification_required: true
clarification_reason: Character lacks proper name and stable identification. Cannot determine if this is a specific named individual or generic reference requiring clarification.
clarification_question: What was the dead friend's name, age, gender, race, and physical appearance? Were there any distinguishing features or identifying marks on the body?

[[SECTION markdown]]
# Dead Friend's Body - Chapter II Character File

**Display Name:** Dead Friend's Body  
**Chapter Role:** Referenced character; companion whose death is discovered after escape  
**Physical Presence:** Deceased in cave interior throughout chapter; protagonist discovers body lying lifeless and clothed  

**Physical Description:** Clothed body, lifeless. No physical description beyond being covered with garments. No facial features, body type, or distinguishing characteristics documented.

**Costume/Silhouette:** Fully clothed (garments unspecified). Silhouette described as lying lifeless while protagonist stands naked nearby. No specific costume details beyond basic clothing state.

**Continuity-Critical Traits:** 
- Protagonist's companion whose death is discovered
- Body remains clothed and lifeless throughout escape sequence
- Sharp click of snapping steel wire felt when breaking bonds
- Moonlight floods cave revealing body's lifeless state

**Render-Facing Prompt Notes:** Requires complete physical description specification for image generation. Cannot proceed with visual representation without manual description input.

**Uncertainty Notes:** 
- No name provided for deceased friend
- Physical appearance entirely unspecified beyond being clothed
- Race, age, gender not documented
- Facial features and body type unknown
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
