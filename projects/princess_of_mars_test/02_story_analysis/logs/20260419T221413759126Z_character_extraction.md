# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T22:14:13.759126+00:00
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

# Chapter II Summary: The Escape of the Dead

## Scene 1: Paralysis Discovery (Early Morning)
Protagonist experiences paralysis in cave - muscles refuse to respond while mental faculties intact. Notices vapor filling cave, pungent odor suggesting poisonous gas. Lying facing cave opening with short trail stretch visible between cave and cliff turn. Horse standing before cave entrance with dragging rein.

## Scene 2: Apache Warriors Arrive (Early Morning)
Approaching horses noise ceases - Indians creeping stealthily along ledge toward protagonist's living tomb. War-bonneted, paint-streaked face appears around cliff shoulder with savage eyes. Warriors display awe and fear rather than aggression. Multiple faces craning over narrow ledge shoulders. Leaders pass whispered words to braves behind them.

## Scene 3: Moaning Sound & Warrior Flight (Early Morning)
Low distinct moaning sound issues from cave recesses behind protagonist. Indians turn and flee in terror, panic-stricken. One brave hurled headlong from cliff to rocks below. Wild cries echo in canyon briefly then stillness returns. Protagonist speculates on horror lurking in shadows at back.

## Scene 4: Paralysis Resolution (Late Afternoon)
Horse wanders off trail searching for food and water. Protagonist left alone with mysterious unknown companion and dead body of friend on ledge. Silence maintained until midnight when awful moan breaks upon startled ears again. Protagonist makes superhuman effort to break bonds - feeling of nausea, sharp click like steel wire snapping. Stands facing unknown foe in moonlight.

## Scene 5: Transformation Discovery (Midnight)
Moonlight floods cave revealing protagonist's own body lying lifeless on floor with staring eyes and limply resting hands. Protagonist stands naked while previously clothed - complete metamorphosis. Heart pounding from exertion, cold sweat from every pore, pinching test confirms not wraith.

## Scene 6: Escape Decision (Midnight to Early Morning)
Protagonist naked and unarmed with no desire to face unseen thing menacing. Revolvers strapped to lifeless body cannot be touched. Carbine in boot strapped to saddle, horse wandered off leaving without defense. Only alternative is flight. Leaps through opening into starlight of clear Arizona night. Crisp mountain air acts as immediate tonic.

## Scene 7: Landscape Investigation (Early Morning)
Protagonist pauses on brink of ledge upbraiding unwarranted apprehension. Reasons nothing molested during helpless hours, better judgment convinces noises from natural causes - cave conformation causing breeze sounds. Decides to investigate but first lifts head to fill lungs with pure night air. Sees beautiful vista of rocky gorge and level cacti-studded flat wrought by moonlight into soft splendor.

## Scene 8: Mars Encounter (Early Morning)
Protagonist meditating on landscape turns gaze from scene to heavens where myriad stars form gorgeous canopy. Large red star close to distant horizon captures attention with overpowering fascination - identified as Mars, god of war. Star seems calling across unthinkable void, luring protagonist like lodestone attracting iron. Longing beyond opposition - closes eyes, stretches arms toward god of vocation.

## Scene 9: Space Transition (Early Morning)
Protagonist feels drawn through trackless immensity of space with suddenness of thought. Instant of extreme cold and utter darkness marks transition point. Chapter ends at moment of space entry.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter II

| Character | Status | Identification | Description Available |
|-----------|--------|----------------|----------------------|
| Protagonist | Main Character | Unnamed | No physical description provided |
| Apache Warrior | Group Reference | Multiple unnamed individuals | Described as war-bonneted, paint-streaked faces |

*Note: This chapter contains no specifically named characters. All references are either generic (Protagonist) or group-based (Apache Warriors/Indians/Braves).*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: Protagonist, I, Unknown Companion, Mysterious Unknown Companion
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary describes only actions and transformations (paralysis, metamorphosis) without physical appearance details like height, build, hair color, or facial features that would support image generation
clarification_required: true
clarification_reason: Protagonist is unnamed in source material; need to determine if actual name exists in broader work
clarification_question: What is the protagonist's actual name in the source material?

[[SECTION markdown]]
# protagonist.md

## Display Name
Protagonist (Unnamed)

## Chapter Role
Main character experiencing paralysis, transformation, and Mars encounter

## Physical Presence
Referenced throughout chapter; physically present in scenes 1-9

## Physical Description
**Not available from source material.** Chapter summary describes:
- Muscles refusing to respond during paralysis
- Transformation from clothed to naked
- Standing facing unknown foe
- Naked body with revolvers strapped to lifeless form
- No physical appearance details (height, build, hair, eyes, etc.)

## Costume/Silhouette
**Not available from source material.** Chapter summary notes:
- Initially clothed (specific clothing not described)
- Later naked after transformation
- Revolvers strapped to body
- Carbine in boot on saddle

## Continuity-Critical Traits
- Experiences paralysis with intact mental faculties
- Undergoes complete metamorphosis from human to wraith-like state
- Transitions through space at chapter end
- No physical description supports render-facing prompts

## Uncertainty Notes
**CRITICAL:** This character record lacks sufficient physical description for dependable image generation. Source material only describes actions and transformations, not appearance details. Manual description required before any visual representation can be created.

## Render-Facing Prompt Guidance
Do not generate images without manual description. If proceeding:
- Focus on transformation sequence (paralysis → metamorphosis)
- Note clothing change from clothed to naked
- Emphasize physical reactions (cold sweat, nausea, heart pounding)
- Avoid guessing specific appearance traits

*Source limitation: Chapter II Summary contains no physical appearance details for protagonist.*
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warrior
canonical_character_id: apache_warriors
aliases: Apache Warriors, Indians, Warriors, Braves, Leaders, War-bonneted, Paint-streaked Face
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary describes group of warriors with general appearance traits (war-bonneted, paint-streaked faces) but no individual physical descriptions that would support specific character image generation
clarification_required: true
clarification_reason: Multiple unnamed individuals referenced; need to determine if specific warrior names exist in source material or if this is purely group reference
clarification_question: Do any specific Apache Warrior names exist in the source material, or are they all unnamed group members?

[[SECTION markdown]]
# apache_warrior.md

## Display Name
Apache Warrior (Unnamed Group Member)

## Chapter Role
Multiple warriors arriving at protagonist's cave; display awe and fear rather than aggression

## Physical Presence
Referenced as multiple individuals in scenes 1-3; physically present on cliff ledge

## Physical Description
**Limited from source material.** Chapter summary describes:
- War-bonneted appearance
- Paint-streaked faces
- Savage eyes
- Multiple faces craning over narrow ledge shoulders
- No individual height, build, or specific physical traits

## Costume/Silhouette
**Partial from source material.** Chapter summary notes:
- War-bonnets (headwear)
- Face paint/streaks
- No specific clothing details beyond headwear and paint

## Continuity-Critical Traits
- Display awe and fear rather than aggression toward protagonist
- Multiple individuals with leaders passing whispered words to braves
- One brave hurled headlong from cliff in terror
- Turn and flee when hearing moaning sound from cave

## Uncertainty Notes
**LIMITED:** This character record represents a group of unnamed individuals. Source material provides general appearance traits (war-bonneted, paint-streaked) but no individual physical descriptions that would support specific character image generation. Manual description required for any individual warrior representation.

## Render-Facing Prompt Guidance
Do not generate images without manual description. If proceeding:
- Focus on group dynamic (multiple warriors, leaders and braves)
- Note war-bonneted appearance and face paint
- Emphasize expressions of awe and fear rather than aggression
- Avoid guessing specific physical traits for individual warriors

*Source limitation: Chapter II Summary describes warriors as unnamed group members with general appearance traits only.*
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
