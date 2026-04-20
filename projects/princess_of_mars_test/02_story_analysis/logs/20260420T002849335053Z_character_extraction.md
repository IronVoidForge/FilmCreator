# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:28:49.335053+00:00
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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values



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
# Character Index - CH005

| Character | Role in Chapter | Status |
|-----------|-----------------|--------|
| Narrator | POV, escapes room, jumps window | Present/Referenced |
| Sola | Female Martian, caretaker | Referenced |
| Watch Dog | Brute guardian, short legs | Visible/Referenced |
| New Guardian | Colossal ape-like creature | Visible |

*Note: All characters extracted from chapter summary and visual continuity facts.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator

**Chapter Role:** POV character, escapes chamber, attempts city edge jump, captured by New Guardian

**Presence Status:** Physically present throughout chapter

**Physical Description:** 
- Humanoid figure (implied from escape actions)
- Capable of jumping thirty feet vertically
- Wears fur covering (found on floor space)
- Cold-sensitive (wakes cold at night)

**Costume & Silhouette:**
- Fur coverings present in room environment
- No specific clothing details provided in source

**Continuity-Critical Traits:**
- Escapes threshold guarded by Watch Dog
- Jumps over attacking brute at city edge
- Leaps into thirty-foot window on building overlooking valley
- Captured from behind upon reaching window sill

**Render-Facing Noun Phrases:**
- Cold-sensitive humanoid escapee
- Fur-covered figure jumping vertically
- Window-sill survivor captured by giant

**Uncertainty Notes:**
- Specific clothing items not described in source material
- Height and build dimensions not explicitly stated
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

**Chapter Role:** Female Martian caretaker, referenced in chapter summary

**Presence Status:** Referenced only (not physically present in scene)

**Physical Description:** 
- Female Martian (species confirmed)
- Sympathetic disposition
- Kind nature
- Provides unfailing ministrations

**Costume & Silhouette:**
- No specific costume details provided in source
- Feminine silhouette implied by gender designation

**Continuity-Critical Traits:**
- Leaves chamber with watch dog at chapter start
- Represents caretaker role within facility
- Associated with initial room environment

**Render-Facing Noun Phrases:**
- Female Martian caretaker figure
- Sympathetic ministrations provider
- Chamber-leaving companion

**Uncertainty Notes:**
- Physical appearance beyond gender/species not detailed
- Specific clothing or markings not described in source material
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: watch_dog
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Watch Dog

**Chapter Role:** Brute guardian, threshold protector throughout chapter

**Presence Status:** Physically present and visible

**Physical Description:** 
- Short legs
- Fast runner (high-speed chase capability)
- Loyal protector nature
- Shuffling gait when walking (distinct from running)
- Brute classification confirmed

**Costume & Silhouette:**
- No specific costume details provided in source
- Brute silhouette implied by species designation

**Continuity-Critical Traits:**
- Guards threshold throughout entire chapter
- Follows narrator with shuffling gait after exit
- Attacks at city edge (brute behavior)
- Chases at high speed to window location
- Captures narrator from behind upon reaching sill

**Render-Facing Noun Phrases:**
- Short-legged brute guardian
- Fast-running loyal protector
- Shuffling-gait threshold guard
- City-edge attacking brute

**Uncertainty Notes:**
- Specific species beyond "brute" not detailed in source
- Physical markings or distinctive features not described
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: new_guardian
canonical_character_id: new_guardian
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# New Guardian

**Chapter Role:** Colossal ape-like creature, captor at window location

**Presence Status:** Physically present and visible at chapter end

**Physical Description:** 
- Colossal size (implied by "colossal" designation)
- Ape-like classification
- White coloration
- Hairless body except for enormous shock of bristly hair on head
- Bristly head feature prominent

**Costume & Silhouette:**
- No specific costume details provided in source
- Primate silhouette implied by ape-like classification

**Continuity-Critical Traits:**
- Stands over narrator upon capture
- Located inside room overlooking valley
- Reaches through window to grab narrator from behind
- Represents final threat at chapter conclusion

**Render-Facing Noun Phrases:**
- Colossal white hairless ape creature
- Bristly-headed giant captor
- Window-sill grabbing guardian
- Valley-overlooking colossal being

**Uncertainty Notes:**
- Specific species beyond "ape-like" not detailed in source
- Height dimensions not explicitly stated (only "colossal")
- Additional physical markings or features not described
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
