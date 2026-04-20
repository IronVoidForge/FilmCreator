# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:28:30.346672+00:00
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

Chapter id: CH005

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

**Broad Story Summary**

*Scene 1: Observation and Sustenance*
- Sola leaves the chamber with the watch dog; the narrator examines the room's mural paintings (landscapes without animals) and food supplies (plant milk).
- Narrator sleeps through the night, waking cold but covered by fur.

*Scene 2: The Escape Attempt*
- Waking in daylight, the narrator observes five female occupants sleeping and the brute guarding the threshold.
- Deciding to test the brute's loyalty, the narrator exits the room; the brute follows with a shuffling gait.
- At the city edge, the brute attacks; the narrator jumps over him into open space.

*Scene 3: The Window Jump and Capture*
- The brute chases at high speed; the narrator leaps into a window thirty feet up on a building overlooking the valley.
- Upon reaching the sill, a hand grabs the narrator from behind inside the room.
- Thrown onto the back, the narrator sees a colossal ape-like creature (white, hairless, bristly head) standing over them.

**Visual Continuity Facts**

*Room Layout & Objects*
- Threshold: Guarded by the brute throughout the chapter.
- Floor Space: Contains food containers and fur coverings.
- Window Sill: Height of approximately thirty feet; overlooks the valley.
- Mural Paintings: Depict mountains, rivers, lakes, oceans, meadows, trees, flowers, winding roadways, sun-kissed gardens; no representation of living animals.

*Characters & Appearance*
- Sola: Female Martian, sympathetic, kind, unfailing ministrations.
- Watch Dog: Brute, short legs, fast runner, loyal protector, shuffling gait when walking.
- New Guardian: Colossal ape-like creature, white and hairless except for enormous shock of bristly hair on head.

*Environmental Details*
- Lighting: Martian nights are extremely cold; illuminated by two moons (nearer moon ~5,000 miles away, further ~14,000 miles).
- Atmosphere: Very thin; fails to diffuse starlight significantly.
- Temperature: Sudden changes between day and night; narrator feels cold upon waking.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH005

## Sola
- **Role:** Female Martian occupant, sympathetic and kind
- **Status:** Referenced throughout chapter
- **Description:** Limited physical details available; primarily characterized by demeanor and actions

## Watch Dog
- **Role:** Brute guardian of threshold
- **Status:** Physically present throughout chapter
- **Description:** Short legs, fast runner, shuffling gait when walking, loyal protector

## New Guardian
- **Role:** Colossal ape-like creature
- **Status:** Appears at chapter climax
- **Description:** White and hairless except for enormous shock of bristly hair on head

## Narrator
- **Role:** Main character examining room and attempting escape
- **Status:** Physically present throughout chapter
- **Description:** Limited physical details; primarily observed through actions and perspective
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only behavioral traits (sympathetic, kind) are described; no physical appearance details provided for image generation
clarification_required: true
clarification_reason: Character may exist under different name or identification in source material
clarification_question: What is Sola's physical appearance and what name does she use when speaking?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Sola - Character Profile

## Display Name
Sola

## Chapter Role
Female Martian occupant, sympathetic and kind

## Physical Presence
Referenced throughout chapter; appears to provide care and assistance

## Physical Description
Limited details available from source material. Only behavioral traits are described (sympathetic, kind, unfailing ministrations). No physical appearance, clothing, or distinguishing features documented in this chapter.

## Costume & Silhouette
Unknown - no costume or silhouette information provided in source material

## Continuity-Critical Traits
- Provides care and assistance to narrator
- Female Martian occupant of the chamber
- Sympathetic demeanor toward narrator

## Render-Facing Prompt Notes
Requires additional physical description for image generation. Behavioral traits (sympathetic, kind) are known but need visual translation.

## Uncertainty Notes
Physical appearance is completely unknown from this chapter source material. Additional clarification needed before reliable image generation can occur.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: Watch Dog
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description is adequately detailed for image generation (short legs, fast runner, shuffling gait when walking)
clarification_required: false
clarification_reason: 
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Watch Dog - Character Profile

## Display Name
Watch Dog

## Chapter Role
Brute guardian of threshold

## Physical Presence
Physically present throughout chapter; guards room entrance and follows narrator outside

## Physical Description
Short legs, fast runner, shuffling gait when walking. Loyal protector who attacks at city edge but follows narrator's lead initially.

## Costume & Silhouette
Brute appearance with short legs and powerful build. Shuffling movement pattern when walking (distinct from running speed).

## Continuity-Critical Traits
- Guards threshold throughout chapter
- Fast runner, shuffling gait when walking
- Loyal protector who follows narrator outside room
- Attacks at city edge but allows escape attempt
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: new_guardian
canonical_character_id: New Guardian
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Detailed physical description available (colossal ape-like creature, white and hairless except for enormous shock of bristly hair on head)
clarification_required: false
clarification_reason: 
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# New Guardian - Character Profile

## Display Name
New Guardian

## Chapter Role
Colossal ape-like creature appearing at chapter climax

## Physical Presence
Appears at chapter climax when narrator reaches window sill; grabs narrator from behind inside room

## Physical Description
Colossal ape-like creature, white and hairless except for enormous shock of bristly hair on head. Standing over narrator after capture attempt.

## Costume & Silhouette
Ape-like silhouette with colossal build. White coloration with hairless body except for distinctive bristly head hair.

## Continuity-Critical Traits
- Colossal size relative to narrator
- White and hairless body
- Enormous shock of bristly hair on head
- Appears from inside room when narrator reaches window sill
- Grabs narrator from behind
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Limited physical description available; primarily observed through actions and perspective with no detailed appearance documented
clarification_required: false
clarification_reason: Character is stable identification but lacks sufficient physical details for image generation
clarification_question: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Narrator - Character Profile

## Display Name
Narrator (First Person)

## Chapter Role
Main character examining room and attempting escape

## Physical Presence
Physically present throughout chapter; examines room, sleeps, attempts escape, jumps through window

## Physical Description
Limited details available from source material. No physical appearance, clothing, or distinguishing features documented in this chapter. Character is primarily observed through actions and first-person perspective.

## Costume & Silhouette
Unknown - no costume or silhouette information provided in source material

## Continuity-Critical Traits
- Examines room's mural paintings (landscapes without animals)
- Inspects food supplies (plant milk)
- Sleeps through night, wakes cold but covered by fur
- Observes five female occupants sleeping and brute guardian
- Tests brute's loyalty by exiting room
- Jumps over attacking brute at city edge
- Leaps into window thirty feet up on building overlooking valley
- Grabs from behind when reaching window sill
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
