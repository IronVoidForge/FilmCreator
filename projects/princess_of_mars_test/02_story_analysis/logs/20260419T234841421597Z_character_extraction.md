# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:48:41.421597+00:00
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

# Chapter II: The Escape of the Dead - Scene Breakdown

## Opening Sequence: Paralysis Discovery
### Visual Facts
- Protagonist lies facing cave opening with short trail visible between cave and cliff turn
- Early morning sun falls through opening onto protagonist's body
- Short stretch of trail leads to horse standing before cave entrance
- Cave interior dim, exterior daylight visible through opening

### Story Beats
1. Protagonist experiences paralysis - muscles refuse to respond to will
2. Sound of approaching horses reaches ears while paralyzed
3. Attempts to spring to feet but discovers inability to move
4. Notices slight vapor filling cave (tenuous, only against daylight opening)
5. Faintly pungent odor reaches nostrils
6. Protagonist speculates on poisonous gas but cannot fathom mental faculties retention

## Apache Warriors Arrival Sequence
### Visual Facts
- Stealthy sound apprises protagonist of warriors' nearness
- War-bonneted, paint-streaked face cautiously around cliff shoulder
- Savage eyes look into protagonist's eyes in dim light
- Multiple faces appear (fifth total) craning necks over narrow ledge shoulders
- Each face shows picture of awe and fear
- Leaders pass back whispered words to those behind them

### Story Beats
1. Protagonist hopes warriors make short work - does not relish alternative treatment
2. Warriors stand and stare rather than approach
3. Protagonist cannot understand reason for their reaction
4. Warriors creep stealthily upon protagonist along little ledge
5. Multiple faces visible simultaneously on narrow cliff edge

## Warrior Flight Sequence
### Visual Facts
- Low but distinct moaning sound issues from cave recesses behind protagonist
- Indians turn and flee in terror, panic-stricken
- One brave hurled headlong from cliff to rocks below
- Wild cries echo in canyon for short time
- Moonlight floods cave after flight

### Story Beats
1. Moaning sound causes warriors to flee immediately
2. Frantic escape efforts cause one warrior to fall from cliff
3. Wild cries echo briefly then all becomes still once more
4. Sound not repeated but protagonist speculates on horror at back
5. Protagonist's fear measured by previous danger experiences

## Escape Sequence
### Visual Facts
- Late afternoon: horse starts slowly down trail in search of food/water
- Dead body of friend lies just within range of vision on ledge
- All silence from possibly midnight until morning moan breaks upon ears
- Moonlight floods cave during escape attempt
- Protagonist stands naked while lifeless body remains clothed

### Story Beats
1. Horse wanders off leaving protagonist alone with mysterious companion and dead body
2. Morning moan breaks on startled ears
3. Sound of moving thing and faint rustling as of dead leaves heard
4. Superhuman effort to break awful bonds (mind/will/nerves, not muscular)
5. Momentary nausea, sharp click like snapping steel wire
6. Protagonist stands with back against cave wall facing unknown foe
7. Moonlight floods cave revealing protagonist's own body lying lifeless all hours
8. Eyes staring toward open ledge, hands resting limply upon ground
9. Protagonist looks at lifeless clay then down at self in utter bewilderment
10. Clothed while lying, yet stands naked as at minute of birth

## Post-Paralysis Realization
### Visual Facts
- Heart pounding against ribs from exertion to release from anaesthesis
- Breath coming in quick short gasps
- Cold sweat stands out from every pore of body
- Ancient experiment of pinching reveals protagonist is anything other than wraith
- Revolvers strapped to lifeless body (cannot bring self to touch)
- Carbine in boot, strapped to saddle
- Horse wandered off leaving without means of defense

### Story Beats
1. Protagonist speculates on possible horror which lurked in shadows at back
2. Fear measured by previous positions of danger and those passed through since
3. Sensations endured during next few minutes would be fear if God help the coward
4. Held paralyzed with back toward horrible unknown danger from sound causing wild stampede
5. Ferocious Apache warriors turn in wild stampede like flock of sheep fleeing wolves
6. Protagonist left to contemplation of position without interruption
7. Only hope paralysis passes off as suddenly as it fell upon him

## Final Escape and Mars Vision
### Visual Facts
- Late afternoon: horse starts slowly down trail for food/water
- Dead body of friend lies just within range on ledge
- All silence from possibly midnight until morning moan breaks upon ears
- Moonlight floods cave during escape attempt
- Protagonist stands naked while lifeless body remains clothed
- Crisp fresh mountain air outside acts as immediate tonic
- Beautiful vista of rocky gorge and cacti-studded flat wrought by moonlight
- Silvered mountains in distance, strange lights and shadows on hog back and arroyo
- Large red star close to distant horizon - identified as Mars

### Story Beats
1. Protagonist decides to investigate but first lifts head to fill lungs with pure night air
2. Sees stretching far below beautiful vista of rocky gorge and cacti-studded flat
3. Moonlight creates miracle of soft splendor and wondrous enchantment
4. Arizona moonlit landscape described as few western wonders more inspiring
5. Silvered mountains, strange lights/shadows on hog back and arroyo form picture
6. Grotesque details of stiff yet beautiful cacti form picture at once enchanting and inspiring
7. As though catching first glimpse of dead and forgotten world so different from any other spot
8. Protagonist turns gaze from landscape to heavens where myriad stars form gorgeous canopy
9. Large red star close to distant horizon - identified as Mars, god of war
10. Fighting man protagonist always held power of irresistible enchantment by Mars
11. Red star seems to call across unthinkable void to lure protagonist toward it
12. Lodestone attracts particle of iron analogy for Mars attraction
13. Protagonist's longing beyond power of opposition
14. Closes eyes, stretches arms toward god of vocation
15. Feels self drawn with suddenness of thought through trackless immensity of space
16. Instant of extreme cold and utter darkness - transition to next chapter
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter II: The Escape of the Dead

## Characters Identified in This Chapter

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|----------------------|---------|------------------|----------------------------|------------------------|
| protagonist | protagonist | - | false | true | true |
| apache_warriors | apache_warriors | Indians, warriors | false | true | true |
| dead_friend | dead_friend | friend, companion | false | true | true |

## Notes on Character Identification

- **Protagonist**: Unnamed main character experiencing paralysis and supernatural events. Physical description not provided in chapter text.
- **Apache Warriors**: Group of indigenous warriors who arrive and flee from mysterious sound. Described collectively but no individual names or detailed physical descriptions.
- **Dead Friend**: Protagonist's deceased companion whose body remains on the cave ledge throughout the chapter. No name or physical details beyond being clothed.

## Continuity Considerations

All three characters lack stable identification for later image generation. The protagonist and dead friend require clarification regarding their specific identities in the Mars series. Apache warriors are a group character requiring clarification about whether any individual warriors have names.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: The chapter text describes only actions, sensations, and movements of the protagonist. No physical appearance details (height, build, hair color, eye color, facial features, etc.) are provided in the source material. Cannot support dependable image generation without additional description.
clarification_required: true
clarification_reason: This character appears to be from the Mars series but lacks a specific name or stable identification. Need to confirm whether this is a generic protagonist or a named character with established identity in the series.
clarification_question: What is the canonical name of the protagonist in the Mars series?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Protagonist - Chapter II Character File

## Display Name
Protagonist (Unnamed)

## Chapter Role
Main character experiencing paralysis and supernatural events in cave setting

## Physical Presence Status
Physically present throughout chapter; referenced as "I" or implied first-person perspective

## Physical Description
**Supported by Source:** None. The text describes only:
- Actions: lying facing cave opening, attempting to move, standing against wall
- Sensations: paralysis, cold sweat, heart pounding, nausea
- State: naked while lifeless body remains clothed

**Missing Details (Not in Source):**
- Height and build
- Hair color and style
- Eye color
- Facial features
- Skin tone
- Scars or marks
- Age indicators

## Costume/Silhouette
**Supported by Source:** None. Protagonist is described as standing naked during key moments.

**Missing Details (Not in Source):**
- Any clothing items before/after paralysis
- Silhouette characteristics

## Continuity-Critical Traits
- Experiences supernatural paralysis (muscles refuse to respond to will)
- Can feel but cannot move initially
- Later breaks free through "superhuman effort"
- Stands naked while dead friend remains clothed
- Heart pounding from exertion
- Cold sweat from pores

## Render-Facing Prompt Noun Phrases
- paralyzed human figure
- person attempting to move but unable
- naked body against cave wall
- heart pounding chest
- cold sweat on skin
- first-person perspective character
- protagonist in supernatural situation

## Uncertainty Notes
**Critical Missing Information:**
1. No physical description exists in source material - cannot generate accurate image without additional description
2. Character lacks canonical name for series identification
3. Cannot determine if this is a specific named character or generic protagonist
4. Age, ethnicity, and other demographic details unknown

**Recommendation:**
Manual description required before reliable image generation. Clarification needed regarding character identity in Mars series.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: apache_warriors
aliases: Indians, warriors
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only collective descriptions provided ("war-bonneted, paint-streaked face", "savage eyes"). No individual physical details (height, build, hair color, facial features) for any specific warrior. Cannot support dependable image generation of individual characters without additional description.
clarification_required: true
clarification_reason: Group character with no individual names or stable identification. Need to determine if any specific warriors have names in the series or if they are generic Apache characters.
clarification_question: Are there specific names for any of the Apache warriors, or are they intended as a collective group character?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Apache Warriors - Chapter II Character File

## Display Name
Apache Warriors (Unnamed Group)

## Chapter Role
Indigenous warriors who arrive at cave and flee from mysterious sound

## Physical Presence Status
Physically present in chapter; described as appearing over cliff shoulder, then fleeing

## Physical Description
**Supported by Source:** Limited collective descriptions:
- "war-bonneted" (headwear)
- "paint-streaked face" (facial markings)
- "savage eyes" (eye appearance)
- Multiple faces visible simultaneously
- Five warriors total mentioned

**Missing Details (Not in Source):**
- Height and build for individual warriors
- Hair color and style
- Eye color beyond "savage"
- Facial features beyond paint-streaked markings
- Individual distinguishing characteristics

## Costume/Silhouette
**Supported by Source:** 
- War-bonnet headwear
- Paint-streaked facial markings
- Multiple faces visible on narrow ledge shoulders

**Missing Details (Not in Source):**
- Body clothing details
- Silhouette characteristics for individual warriors

## Continuity-Critical Traits
- Arrive stealthily with "stealthy sound"
- Stand and stare rather than approach initially
- Show "awe and fear" in expressions
- Leaders pass whispered words to those behind
- Flee immediately from moaning sound
- One warrior falls headlong from cliff during flight
- Multiple faces visible simultaneously on narrow ledge

## Render-Facing Prompt Noun Phrases
- group of indigenous warriors
- war-bonneted figures
- paint-streaked faces
- savage eyes
- multiple faces on cliff edge
- five warriors total
- warriors showing awe and fear
- stealthy approaching figures

## Uncertainty Notes
**Critical Missing Information:**
1. No individual physical descriptions exist - only collective group descriptions
2. Cannot generate accurate images of specific warriors without additional description
3. Character lacks stable identification for series continuity
4. Need to determine if any individual warriors have names or are generic

**Recommendation:**
Manual description required before reliable image generation. Clarification needed regarding whether these are named characters or collective group representation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dead_friend
canonical_character_id: dead_friend
aliases: friend, companion
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only described as "dead body of friend" and "lifeless clay". No physical appearance details (height, build, hair color, facial features) provided. Cannot support dependable image generation without additional description.
clarification_required: true
clarification_reason: Character is referenced only as "friend" or "companion" with no name or stable identification in the Mars series. Need to confirm who this character was and if they have a canonical name.
clarification_question: What is the canonical name of the protagonist's deceased friend in the Mars series?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Dead Friend - Chapter II Character File

## Display Name
Dead Friend (Unnamed)

## Chapter Role
Protagonist's deceased companion whose body remains on cave ledge throughout chapter

## Physical Presence Status
Physically present as dead body throughout chapter; referenced multiple times

## Physical Description
**Supported by Source:** Limited descriptions:
- "dead body of friend"
- "lifeless clay"
- "clothed while lying" (contrast to protagonist's naked state)
- Lies just within range of vision on ledge
- Remains clothed throughout chapter

**Missing Details (Not in Source):**
- Height and build
- Hair color and style
- Eye color
- Facial features
- Clothing type or details
- Age indicators
- Cause of death (implied supernatural)

## Costume/Silhouette
**Supported by Source:** 
- Remains clothed throughout chapter
- Lies on cave ledge
- Positioned within protagonist's line of vision

**Missing Details (Not in Source):**
- Specific clothing items or style
- Silhouette characteristics

## Continuity-Critical Traits
- Body remains on ledge from beginning to end of chapter
- Protagonist stands naked while dead friend remains clothed
- "Lifeless clay" description emphasizes death state
- Triggers protagonist's supernatural awakening
- Associated with mysterious moaning sound that causes flight
- Moonlight floods cave during escape attempt near body

## Render-Facing Prompt Noun Phrases
- deceased human figure
- lifeless body on ledge
- clothed dead person
- friend's corpse
- dead companion
- lifeless clay
- body in cave setting
- moonlit dead figure

## Uncertainty Notes
**Critical Missing Information:**
1. No physical description exists beyond being "dead" and "clothed"
2. Cannot generate accurate image without additional description
3. Character lacks canonical name for series identification
4. Need to determine if this is a specific named character or generic friend reference

**Recommendation:**
Manual description required before reliable image generation. Clarification needed regarding character identity in Mars series. Consider whether this body should be rendered at all given lack of identifying details.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
