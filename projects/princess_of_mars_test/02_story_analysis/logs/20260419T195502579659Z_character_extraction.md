# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:55:02.579659+00:00
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

# Chapter II: Scene Decomposition Summary

## Scene 1: Paralysis in Cave (Opening)
**Visual Continuity:** Protagonist lies facing cave opening, muscles refuse to respond to will despite mental awareness. Short trail visible between cave and cliff turn. Apache warriors positioned on narrow ledge outside, unable to pass each other. Horse with dragging rein stands before cave entrance. Friend's body within vision range on ledge.

**Story Beat:** Protagonist experiences paralysis while retaining mental faculties. Attempts to spring to feet but muscles refuse response. Notices vapor filling cave (tenuous, only noticeable against opening). Faint pungent odor reaches nostrils. Assumes poisonous gas but cannot fathom why mental faculties remain while movement impossible.

## Scene 2: Unknown Presence Frightens Warriors
**Visual Continuity:** Apache warriors on narrow ledge outside cave. One brave's face appears around shoulder of cliff, savage eyes look into protagonist's. Early morning sun falls full upon protagonist through opening. Another and more faces appear craning necks over shoulders of fellows. Each face shows awe and fear.

**Story Beat:** Stealthy sound apprises protagonist of warriors' nearness. War-bonneted, paint-streaked face cautiously appears around cliff shoulder. Warriors stand and stare with bulging eyes and dropped jaws. Unknown presence in cave recesses issues low moaning sound. Warriors turn and flee in terror, panic-stricken. One brave hurled headlong from cliff to rocks below. Wild cries echo in canyon then all still once more.

## Scene 3: Body Transformation Discovery
**Visual Continuity:** Moonlight floods cave interior. Protagonist's body lies on cave floor with eyes staring toward open ledge and hands resting limply upon ground. Protagonist stands naked against wall of cave facing unknown foe. Earlier state was clothed while lying in cave hours.

**Story Beat:** Late afternoon horse starts slowly down trail searching for food and water. Protagonist left alone with mysterious unknown companion and dead body of friend within range of vision. Midnight silence broken by awful moan from black shadows. Sound of moving thing and faint rustling as of dead leaves heard. Protagonist makes superhuman effort to break bonds through mind, will, nerves—not muscular. Something gives with momentary nausea, sharp click like snapping steel wire. Protagonist stands with back against cave wall facing unknown foe. Discovers own body lying lifeless on floor while protagonist now naked and clothed simultaneously. Heart pounding from exertion, cold sweat from every pore, pinching reveals not wraith.

## Scene 4: Escape into Arizona Night
**Visual Continuity:** Protagonist leaps through opening into starlight of clear Arizona night. Crisp fresh mountain air outside acts as immediate tonic. Vista stretches far below with beautiful rocky gorge and level cacti-studded flat wrought by moonlight into soft splendor. Silvered mountains in distance, strange lights and shadows upon hog back and arroyo, grotesque details of stiff yet beautiful cacti form enchanting picture.

**Story Beat:** Protagonist left without means of defense—revolvers strapped to lifeless body cannot be touched, carbine in boot strapped to saddle, horse wandered off. Decision crystallized by recurrence of rustling sound from thing creeping stealthily upon protagonist in darkness. Unable longer to resist temptation to escape horrible place, leaps quickly through opening into starlight. Mountain air acts as immediate tonic with new life and courage coursing through. Pauses on brink of ledge, upbraids self for unwarranted apprehension. Better judgment convinces noises must have resulted from purely natural and harmless causes—probably cave conformation such that slight breeze caused sounds heard. Decides to investigate but first lifts head to fill lungs with pure invigorating night air.

## Scene 5: Attraction to Mars (Chapter End)
**Visual Continuity:** Protagonist stands meditating on landscape. Heavens where myriad stars form gorgeous and fitting canopy for earthly scene wonders. Large red star close to distant horizon visible. Moonlight creates soft splendor and wondrous enchantment across Arizona landscape.

**Story Beat:** Protagonist turns gaze from landscape to heavens where myriad stars form gorgeous canopy. Attention riveted by large red star close to distant horizon. Feels spell of overpowering fascination—it is Mars, the god of war. For fighting man protagonist, Mars has always held power of irresistible enchantment. As gazes on that far-gone night, seems to call across unthinkable void, lure protagonist to it, draw him as lodestone attracts particle of iron. Longing beyond power of opposition. Closes eyes, stretches out arms toward god of vocation, feels self drawn with suddenness of thought through trackless immensity of space. Instant of extreme cold and utter darkness marks chapter end during space transition.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter II

| Asset ID | Canonical ID | Status | Description Available |
|----------|--------------|--------|----------------------|
| protagonist | protagonist | Fully identified | No physical description in source |
| friend_body | friend_body | Partially identified | Only referenced as dead body |
| apache_warriors | apache_warriors | Group reference | Minimal visual details |
| unknown_companion | unknown_companion | Unknown entity | Explicitly unidentified |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical appearance, clothing, or distinguishing features described in source material - only actions and mental states documented
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# protagonist

## Display Name & Chapter Role
**Protagonist** - Central figure experiencing paralysis, body transformation, and escape

## Physical Presence Status
**Referenced** - Protagonist is physically present throughout all scenes

## Physical Description (Source-Supported)
- Eyes staring toward open ledge
- Hands resting limply upon ground
- Naked against cave wall facing unknown foe
- Heart pounding from exertion
- Cold sweat from every pore

## Costume & Silhouette Traits
- Earlier state was clothed while lying in cave hours
- Revolvers strapped to lifeless body (cannot be touched)
- Carbine in boot strapped to saddle
- Horse wandered off with dragging rein

## Continuity-Critical Details
- Protagonist stands naked and clothed simultaneously after transformation
- Muscles refuse response despite mental awareness
- Cannot fathom why movement impossible while mental faculties remain

## Render-Facing Prompt Noun Phrases
- "man experiencing paralysis"
- "figure standing against cave wall"
- "person with eyes staring toward opening"
- "individual in state of transformation"
- "character drawing arms toward stars"

## Uncertainty Notes
**CRITICAL**: No physical appearance, facial features, hair color, or skin tone described in source material. Cannot generate dependable images without manual description. Source only documents actions and mental states, not visual characteristics.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: friend_body
canonical_character_id: friend_body
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only referenced as dead body of friend, no physical appearance, name, or distinguishing features described in source material
clarification_required: true
clarification_reason: Need to know who the friend was and if they exist under another stable name - currently only identified by relationship status
clarification_question: What is the friend's actual name or canonical character identity? Is this a recurring character or one-time reference?

[[SECTION markdown]]
# friend_body

## Display Name & Chapter Role
**Friend's Body** - Dead companion referenced within protagonist's vision range

## Physical Presence Status
**Referenced** - Only visible as body on ledge, not fully described

## Physical Description (Source-Supported)
- Body lying on cave floor with eyes staring toward open ledge
- Hands resting limply upon ground
- Located within range of protagonist's vision on ledge

## Costume & Silhouette Traits
- Earlier state was clothed while lying in cave hours
- No specific clothing details described beyond being "clothed"

## Continuity-Critical Details
- Body remains lifeless throughout chapter
- Protagonist discovers own body lying lifeless on floor while simultaneously standing
- Friend's body within vision range during escape decision

## Render-Facing Prompt Noun Phrases
- "dead body of friend"
- "lifeless figure on cave ledge"
- "body with eyes staring toward opening"
- "deceased companion in protagonist's vision"

## Uncertainty Notes
**CRITICAL**: No physical appearance, facial features, age, or identity described. Only relationship status known ("friend"). Cannot generate dependable images without clarification of actual character name and visual characteristics. Source material explicitly does not provide distinguishing features beyond being a dead body.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: apache_warriors
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group reference only - no individual physical descriptions provided beyond "war-bonneted, paint-streaked face" and general Apache warrior identification
clarification_required: true
clarification_reason: Need to know if this is a specific named group or generic Apache warriors - currently identified only by cultural affiliation without stable character names
clarification_question: Are these specific named Apache characters or generic warriors? Do any have individual canonical names beyond "Apache warrior"?

[[SECTION markdown]]
# apache_warriors

## Display Name & Chapter Role
**Apache Warriors** - Group of warriors positioned on narrow ledge outside cave

## Physical Presence Status
**Referenced** - Multiple warriors visible as group, not individually described

## Physical Description (Source-Supported)
- War-bonneted appearance
- Paint-streaked faces
- Savage eyes looking into protagonist's
- Faces showing awe and fear
- Standing with bulging eyes and dropped jaws

## Costume & Silhouette Traits
- War-bonnet headwear
- Face paint streaks
- Positioned on narrow ledge outside cave
- Multiple faces appearing over shoulders of fellows

## Continuity-Critical Details
- Warriors unable to pass each other on narrow ledge
- One brave hurled headlong from cliff to rocks below
- Warriors turn and flee in terror, panic-stricken
- Stealthy sound apprises protagonist of warriors' nearness

## Render-Facing Prompt Noun Phrases
- "Apache warrior group"
- "war-bonneted figures on ledge"
- "paint-streaked faces showing fear"
- "multiple warriors with bulging eyes"
- "group fleeing in terror from cave"

## Uncertainty Notes
**CRITICAL**: No individual names, physical appearances, or distinguishing features beyond cultural markers. Only identified as Apache warriors by affiliation. Cannot generate dependable images of specific individuals without clarification of whether these are named characters or generic group representation. Source material does not provide stable character identities beyond cultural identification.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: unknown_companion
canonical_character_id: unknown_companion
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Explicitly described as "unknown presence" and "mysterious unknown companion" - no physical features, appearance, or identity provided in source material
clarification_required: true
clarification_reason: Need to determine if this is a supernatural entity, living character, or other classification - currently only identified by mystery status without stable name
clarification_question: Is the unknown companion a supernatural entity, living character with hidden identity, or something else? What canonical name or classification should be assigned?

[[SECTION markdown]]
# unknown_companion

## Display Name & Chapter Role
**Unknown Companion/Presence** - Mysterious entity throughout protagonist's experience

## Physical Presence Status
**Uncertain** - Described as moving thing with faint rustling, not fully visualized

## Physical Description (Source-Supported)
- Issues low moaning sound from cave recesses
- Sound of moving thing and faint rustling as of dead leaves heard
- Something gives with momentary nausea, sharp click like snapping steel wire
- Appears in black shadows during midnight silence

## Costume & Silhouette Traits
- No specific costume or silhouette described
- Exists in darkness and shadows
- Creates sounds without visible movement initially

## Continuity-Critical Details
- Unknown presence frightens warriors causing them to flee
- Protagonist discovers own body lying lifeless while simultaneously standing
- Something creeping stealthily upon protagonist in darkness
- Protagonist left alone with mysterious unknown companion and dead body of friend

## Render-Facing Prompt Noun Phrases
- "unknown presence in cave"
- "mysterious entity from shadows"
- "figure making low moaning sounds"
- "presence causing rustling sound"
- "entity drawing protagonist through space"

## Uncertainty Notes
**CRITICAL**: No physical appearance, form, or identity described beyond being "unknown." Source material explicitly uses terms like "unknown presence," "mysterious unknown companion," and "black shadows." Cannot generate dependable images without clarification of actual nature (supernatural vs. living) and visual characteristics. This character is fundamentally unidentified by design in source material.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
