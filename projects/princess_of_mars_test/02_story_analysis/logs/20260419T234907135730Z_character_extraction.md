# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:49:07.135730+00:00
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

| Asset ID | Canonical Character ID | Display Name | Status | Physical Presence |
|----------|------------------------|--------------|--------|-------------------|
| protagonist | protagonist | Protagonist (Unnamed First-Person Narrator) | Fully Identified | Physically Present |
| apache_warriors | apache_warriors | Apache Warriors (Indians) | Fully Identified | Physically Present |
| dead_friend | deceased_companion | Dead Body of Friend | Partially Identified | Referenced (Deceased) |

## Character Descriptions

### Protagonist
The unnamed first-person narrator experiencing paralysis in the cave. Physically present throughout the chapter, described as naked with visible physical reactions (heart pounding, cold sweat). Fully identified as the central character despite lacking a proper name.

### Apache Warriors
A group of five Apache warriors who arrive stealthily at the cave entrance. Described with war-bonneted attire and paint-streaked faces. Physically present but flee in terror upon hearing moaning sounds from the cave recesses.

### Dead Body of Friend
The deceased companion lying on the ledge within range of vision. Referenced throughout as a clothed dead body. Not fully identified beyond being "friend" or "companion." Limited physical description available (clothed, lifeless).

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: first-person narrator, unnamed protagonist
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Protagonist - Chapter II Character File

## Display Name
Protagonist (Unnamed First-Person Narrator)

## Chapter Role
Central character experiencing paralysis and eventual escape from cave

## Physical Presence
**Physically Present** - The protagonist is physically present throughout the entire chapter, lying in the cave facing the opening.

## Physical Description (Supported by Source)
- Naked body with visible physical reactions
- Heart pounding against ribs from exertion
- Cold sweat standing out from every pore of body
- Muscles refusing to respond to will during paralysis
- Standing naked while lifeless body remains clothed
- Eyes staring toward open ledge, hands resting limply upon ground

## Costume/Silhouette/Continuity Traits
- No clothing (stands naked throughout chapter)
- Revolvers strapped to lifeless body (cannot bring self to touch)
- Carbine in boot, strapped to saddle
- Positioned with back against cave wall facing unknown foe

## Render-Facing Noun Phrases
- Naked human figure in dim cave environment
- Human experiencing physical paralysis
- Person with visible cold sweat on skin
- Lifeless body standing upright while clothed companion lies down
- Human facing open ledge with staring eyes

## Uncertainty Notes
- Proper name not provided (first-person narrator convention)
- Specific age, height, or build not described beyond general human form
- Facial features not detailed in source material

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: apache_warriors
aliases: Indians, warriors, five faces
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Apache Warriors - Chapter II Character File

## Display Name
Apache Warriors (Indians)

## Chapter Role
Stealthy visitors who arrive at cave and flee in terror upon hearing moaning sounds

## Physical Presence
**Physically Present** - Five warriors physically present at cliff shoulder, then creep along ledge, then flee entirely from cave

## Physical Description (Supported by Source)
- War-bonneted attire
- Paint-streaked faces
- Savage eyes looking into protagonist's eyes in dim light
- Multiple faces visible simultaneously on narrow cliff edge
- Each face showing picture of awe and fear
- Leaders passing whispered words to those behind them

## Costume/Silhouette/Continuity Traits
- Five warriors total (fifth face mentioned)
- Stealthy movement along little ledge
- Turn in wild stampede like flock of sheep fleeing wolves
- One brave hurled headlong from cliff to rocks below
- Wild cries echo in canyon for short time

## Render-Facing Noun Phrases
- Group of five warriors with war-bonneted attire
- Warriors with paint-streaked faces and savage eyes
- Multiple faces showing awe and fear simultaneously
- Warriors creeping stealthily along narrow cliff edge
- Five warriors fleeing in terror from cave moaning

## Uncertainty Notes
- Individual warrior names not provided (treated as group)
- Specific tribal identification beyond "Apache" or "Indians"
- Exact number confirmed as five faces total

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dead_friend
canonical_character_id: deceased_companion
aliases: friend, companion, lifeless body
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited physical description available - only described as "dead body" or "lifeless body" with clothed state. No specific name, age, build, or detailed features provided beyond being deceased companion.

clarification_required: true
clarification_reason: Character might already exist under another name or is too weakly identified for reliable image generation without additional clarification about identity and relationship to protagonist.

clarification_question: What is the proper name of the friend/deceased companion? Is this a specific character from earlier chapters (Chapter I) or an unnamed deceased individual?

[[SECTION markdown]]
# Dead Body of Friend - Chapter II Character File

## Display Name
Dead Body of Friend (Deceased Companion)

## Chapter Role
Lifeless companion lying on ledge within range of vision; catalyst for protagonist's escape attempt

## Physical Presence
**Referenced (Deceased)** - The dead body is physically present as a corpse on the ledge, not as a living character. Referenced throughout chapter as "dead body," "lifeless body," or "friend."

## Physical Description (Supported by Source)
- Dead body lying just within range of vision on ledge
- Clothed while lying (contrast with protagonist's naked state)
- Lifeless body remains clothed during escape attempt
- No detailed physical features described beyond deceased state

## Costume/Silhouette/Continuity Traits
- Fully clothed (unlike protagonist who stands naked)
- Lying position throughout chapter
- Positioned on ledge within range of vision
- Revolvers and carbine associated with lifeless body's equipment

## Render-Facing Noun Phrases
- Clothed dead body lying on rocky ledge
- Lifeless human figure in prone position
- Deceased companion with visible clothing
- Dead body contrasting with standing naked protagonist
- Corpse positioned near cave opening

## Uncertainty Notes
- **NOT FULLY IDENTIFIED** - Only known as "friend" or "companion" without proper name
- **MANUAL DESCRIPTION REQUIRED** - Limited physical description beyond deceased state and clothed condition
- Specific identity, age, build, or relationship details not provided in source material
- May be character from earlier chapter (Chapter I) requiring clarification about continuity

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
