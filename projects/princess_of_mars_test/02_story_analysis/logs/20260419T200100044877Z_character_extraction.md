# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:01:00.044877+00:00
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

# Chapter V: Visual & Narrative Continuity

**Visual Continuity Facts:**
*   **Room Layout:** The space includes a floor where food/drink are placed, silks/furs for sleeping, and a window sill approximately thirty feet from the ground overlooking a valley.
*   **Guardian Positioning:** The Watch Dog lies full length across the threshold initially, then follows ten paces behind the narrator along deserted streets before springing to intercept at the city edge.
*   **Artifacts:** Mural paintings depict earthly scenes (mountains, rivers, gardens) with different vegetation colorings; no living animals are represented in the art.
*   **Food Items:** Solid substance resembling cheese and almost tasteless; liquid is milk from a large plant that distills supply from soil/air/sun rays (yielding 8-10 quarts per day).
*   **Atmospheric Indicators:** Fur coverings are partially dislodged by cold drafts; the Watch Dog's eyes remain glued upon the narrator even while sleeping.

**Narrative Progression:**
*   **Opening:** Sola leaves the chamber after giving commands to the Watch Dog. The narrator observes the beast guarding him intently before crossing to the exit and lying down on the threshold.
*   **Observation:** While Sola is away, the narrator examines the room's paintings and food supplies. He notes the cold Martian nights and the rapid movement of the two moons (one every 7.5 hours).
*   **Interaction:** Sola returns with food and drink. The narrator eats, sleeps, and wakes to find his coverings replenished by a hand (presumed to be Sola's).
*   **Climax:** Feeling secure in his ability as a jumper, the narrator tests the Watch Dog's loyalty by attempting to leave the room. He shuffles toward the beast, who backs away. At the city edge, the dog intercepts him; the narrator leaps over the charging brute and lands far beyond him.
*   **Resolution:** The narrator attempts to escape to a window sill but is dragged back into the room by a huge hand. He finds himself on his back facing a colossal ape-like creature standing over him.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter V

| Character | Role | Status | Description |
|-----------|------|--------|-------------|
| Sola | Guardian/Hostess | Referenced | Human figure who manages the chamber and provides care |
| The Narrator | Protagonist/Jumper | Present | First-person perspective character experiencing events |
| Watch Dog | Guardian Beast | Present | Canine guardian creature with strong loyalty |
| Colossal Ape-like Creature | Unknown Entity | Present | Large ape-like being at chapter's conclusion |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical or visual description in source material - only referred to by name and actions without stable visual traits for image generation
clarification_required: true
clarification_reason: Character may already exist under another name or is too weakly identified; need clarification about species, age, and appearance
clarification_question: Is Sola a human female character? What are her approximate age, height, and distinguishing physical features?

[[SECTION markdown]]
# sola.md

## Display Name
Sola

## Chapter Role
Guardian/Hostess - manages the chamber and provides care to the narrator

## Physical Presence Status
Referenced throughout chapter (leaves chamber, returns with food/drink)

## Physical Description
**Supported by Source:** None - only referred to by name and actions without visual details

**Uncertainty Notes:** 
- No physical description provided in source material
- Cannot determine species, age, height, or distinguishing features from text alone
- Only known through her relationship with the narrator and Watch Dog
- Appears to be a caretaker/hostess figure based on context

## Costume/Silhouette/Continuity Traits
**Supported by Source:** None - no costume or silhouette details provided

**Uncertainty Notes:** 
- No costume information available in source material
- Silhouette cannot be determined without visual description
- Continuity-critical traits are unknown from text alone

## Render-Facing Prompt Noun Phrases
- "caretaker figure" (uncertain species)
- "chamber manager" (role-based descriptor)
- "hostess of the Martian dwelling" (contextual role)

## Important Uncertainty Flags
⚠️ **Manual Description Required** - Cannot generate reliable images without additional physical description
⚠️ **Clarification Needed** - Species and appearance need clarification for accurate representation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_narrator
canonical_character_id: The Narrator
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical or visual description in source material - only referred to as "the narrator" or "I" without stable visual traits for image generation
clarification_required: true
clarification_reason: Character may already exist under another name or is too weakly identified; need clarification about species, age, and appearance
clarification_question: Is the narrator a human male character? What are their approximate age, height, and distinguishing physical features?

[[SECTION markdown]]
# the_narrator.md

## Display Name
The Narrator

## Chapter Role
Protagonist/Jumper - first-person perspective character experiencing events on Mars

## Physical Presence Status
Present throughout chapter (experiences all events directly)

## Physical Description
**Supported by Source:** None - only referred to as "the narrator" or "I" without visual details

**Uncertainty Notes:** 
- No physical description provided in source material
- Cannot determine species, age, height, or distinguishing features from text alone
- Only known through their actions and experiences (jumping, eating, sleeping)
- Physical traits are completely unknown from the narrative perspective

## Costume/Silhouette/Continuity Traits
**Supported by Source:** None - no costume or silhouette details provided

**Uncertainty Notes:** 
- No costume information available in source material
- Silhouette cannot be determined without visual description
- Continuity-critical traits are unknown from text alone

## Render-Facing Prompt Noun Phrases
- "first-person protagonist" (role-based descriptor)
- "Martian jumper" (contextual role)
- "narrator of the chamber experience" (narrative function)

## Important Uncertainty Flags
⚠️ **Manual Description Required** - Cannot generate reliable images without additional physical description
⚠️ **Clarification Needed** - Species and appearance need clarification for accurate representation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: Watch Dog
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Sufficient visual description in source material - described as canine guardian with specific behaviors and physical traits
clarification_required: false
clarification_reason: Character has stable identification as a guardian beast with consistent visual references
clarification_question: 

[[SECTION markdown]]
# watch_dog.md

## Display Name
Watch Dog

## Chapter Role
Guardian Beast - loyal protector of the narrator and chamber

## Physical Presence Status
Present throughout chapter (guarding threshold, following narrator, intercepting at city edge)

## Physical Description
**Supported by Source:** 
- "lies full length across the threshold"
- "eyes remain glued upon the narrator even while sleeping"
- "charging brute" at city edge
- Canine guardian creature with strong loyalty

**Uncertainty Notes:** 
- No specific breed or size details provided
- Physical dimensions beyond general canine form are unknown

## Costume/Silhouette/Continuity Traits
**Supported by Source:** 
- Full-body guardian posture across threshold
- Eyes fixed on narrator (even during sleep)
- Canine silhouette with charging behavior at city edge

**Uncertainty Notes:** 
- No costume or accessories mentioned
- Continuity-critical traits are limited to guardian behaviors

## Render-Facing Prompt Noun Phrases
- "canine guardian beast" (species and role)
- "loyal protector" (behavioral trait)
- "threshold watcher" (position-based descriptor)
- "eyes glued upon narrator" (specific behavioral detail)
- "charging brute at city edge" (action sequence detail)

## Important Uncertainty Flags
✅ **Manual Description Not Required** - Sufficient visual description for image generation
✅ **Clarification Not Needed** - Stable identification as guardian beast

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: colossal_ape_like_creature
canonical_character_id: Colossal Ape-like Creature
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical or visual description in source material - only described as "ape-like" and "colossal" without stable visual traits for image generation
clarification_required: true
clarification_reason: Character may already exist under another name (possibly Sola) or is too weakly identified; need clarification about identity and appearance
clarification_question: Is the colossal ape-like creature a separate entity from Sola, or is it Sola in some form? What are its approximate size, species, and distinguishing features?

[[SECTION markdown]]
# colossal_ape_like_creature.md

## Display Name
Colossal Ape-like Creature

## Chapter Role
Unknown Entity - appears at chapter's conclusion standing over narrator

## Physical Presence Status
Present at chapter climax (standing over narrator on back)

## Physical Description
**Supported by Source:** 
- "ape-like creature"
- "colossal" size
- Standing over narrator in a threatening posture

**Uncertainty Notes:** 
- No specific species details beyond "ape-like"
- Exact dimensions beyond "colossal" are unknown
- Physical features beyond general ape characteristics are not described
- Relationship to other characters (possibly Sola) is unclear

## Costume/Silhouette/Continuity Traits
**Supported by Source:** 
- Colossal size relative to narrator
- Ape-like silhouette
- Standing posture over prone narrator

**Uncertainty Notes:** 
- No costume or accessories mentioned
- Continuity-critical traits are limited to size and species type

## Render-Facing Prompt Noun Phrases
- "colossal ape-like creature" (species and size)
- "standing over narrator" (position detail)
- "threatening presence at chapter end" (narrative function)

## Important Uncertainty Flags
⚠️ **Manual Description Required** - Cannot generate reliable images without additional physical description
⚠️ **Clarification Needed** - Identity and relationship to other characters need clarification for accurate representation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
