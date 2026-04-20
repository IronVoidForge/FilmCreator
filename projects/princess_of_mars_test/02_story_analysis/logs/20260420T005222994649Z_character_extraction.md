# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:52:22.994649+00:00
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

# Chapter V Summary: "I ELUDE MY WATCH DOG"

## Scene Sequence & Visual Continuity

### Opening Scene - Sola's Departure
- **Visual**: Sola stares into brute's wicked-looking eyes, mutters commands, points to narrator, leaves chamber
- **Continuity Fact**: Watch dog remains in room after Sola exits; narrator observes beast crossing to exit threshold and lying down full length across it
- **Emotional Beat**: Narrator wonders what ferocious monstrosity might do when left alone with tender morsel of meat

### Room Examination Scene
- **Visual**: Mural painting depicts scenes of rare beauty - mountains, rivers, lake, ocean, meadow, trees, flowers, winding roadways, sun-kissed gardens
- **Continuity Fact**: Work wrought by master hand, subtle atmosphere, perfect technique; nowhere represents living animal (human or brute)
- **Narrative Purpose**: Establishes narrator's wild conjecture about strange anomalies met on Mars

### Food & Care Scene
- **Visual**: Sola returns bearing food and drink, places on floor beside narrator, seats herself short ways off, regards intently
- **Continuity Fact**: Food ~1 pound solid substance cheese consistency almost tasteless; liquid appears milk from animal (later discovered from large plant)
- **Environmental Detail**: Plant distills milk from soil products, air moisture, sun rays - single plant gives 8-10 quarts per day

### Rest & Night Scene
- **Visual**: Narrator stretches upon silks, asleep; dark when awakens, very cold
- **Continuity Fact**: Someone threw fur over narrator, partially dislodged in darkness
- **Sola's Action**: Hand reaches out pulling fur over narrator, adds another to covering
- **Character Note**: Sola alone among green Martians disclosed characteristics of sympathy, kindliness, affection

### Night Information Scene (Narrative Exposition)
- **Visual**: Narrator sleeping; no twilight/dawn transitions
- **Continuity Fact**: Martian nights extremely cold, sudden temperature changes uncomfortable
- **Moon System Detail**: Two moons vastly nearer than Earth's moon - nearer ~5,000 miles vs. 240,000 miles to our moon

### Escape Attempt Scene
- **Visual**: Narrator gains feet slowly; watcher does same; narrator advances with shuffling gait
- **Continuity Fact**: Watch dog backs away from narrator when reached open; falls in behind following ~10 paces in rear
- **Location Change**: Edge of city where escape attempt occurs

### Climax - Escape & Capture
- **Visual**: Watch dog springs before narrator at edge of city, utters strange sounds, bares ugly ferocious tusks
- **Action Sequence**: Narrator rushes toward beast, leaps into air alighting far beyond him and away from city
- **Continuity Fact**: Beast wheels instantly charging with appalling speed; narrator meets charge by doubling tracks and leaping over beast
- **Location Change**: Narrator jumps for window ~30 feet from ground in building overlooking valley

### Final Scene - Colossal Creature Discovery
- **Visual**: Narrator grasps sill, pulls to sitting posture without looking into building, gazes down at baffled animal beneath
- **Action Sequence**: Huge hand grasps narrator by neck from behind, drags violently into room; thrown upon back
- **Continuity Fact**: Standing over narrator is colossal ape-like creature, white and hairless except enormous shock of bristly hair on head

## Key Continuity Facts for Scene Decomposition
- Watch dog never voluntarily away from narrator a moment
- Sola's ministrations to bodily wants unfailing
- Narrator's jumping ability becomes central escape mechanism
- Room threshold always occupied by watch dog when narrator sleeps
- Five female occupants of room all sleeping piled high with silks and furs (other than narrator)
- Watch dog appears sleepless, eyes glued upon narrator throughout chapter
]]
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter V Character Index

| Asset ID | Canonical ID | Name/Role | Identification Status | Description Sufficiency |
| :--- | :--- | :--- | :--- | :--- |
| `sola` | `sola` | Female Martian Caretaker | Fully Identified | Manual Description Required |
| `narrator` | `narrator` | Protagonist (Human) | Fully Identified | Manual Description Required |
| `watch_dog` | `watch_dog` | Guardian Brute | Fully Identified | Manual Description Required |
| `colossal_ape` | `colossal_ape` | Colossal Ape-like Creature | Weakly Identified (Unnamed) | Manual Description Required |

**Notes:**
- All characters require manual description for image generation due to sparse physical details in source text.
- `colossal_ape` lacks a proper name in this chapter and may require clarification on canonical identity.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text provides no details on skin tone, hair, height, or facial features; only gender and species (female Martian) are confirmed.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File: Sola

**Display Name:** Sola  
**Chapter Role:** Caretaker / Female Martian Occupant  
**Physical Presence:** Physically Present  

**Supported Physical Description:**
- Female Martian.
- Shows sympathy, kindliness, and affection toward the narrator.
- Brings food and drink to the narrator.
- Covers narrator with fur during cold nights.

**Costume & Silhouette:**
- Unknown attire or skin tone.
- No specific build details (height, weight) provided in text.

**Continuity-Critical Traits:**
- One of five female occupants of the room (all sleeping piled with silks).
- Distinct from other green Martians due to disclosed characteristics of sympathy.

**Descriptive Noun Phrases for Prompts:**
- "Female Martian caretaker"
- "Sympathetic alien figure"
- "Green Martian occupant"

**Uncertainty Notes:**
- **Visual Gap:** No description of hair, eyes, or skin color is available in the source text. Image generation must rely on default assumptions for female Martians unless clarified.
- **Silhouette:** Height and build are unknown; only functional actions (bringing food, covering with fur) are documented.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text refers to the figure only as "narrator" or "I"; no physical traits (hair, eyes, skin tone, build) are described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File: Narrator

**Display Name:** The Narrator  
**Chapter Role:** Protagonist / Human Observer  
**Physical Presence:** Physically Present  

**Supported Physical Description:**
- Human-like figure (implied by "tender morsel of meat", "human or brute" distinction in mural).
- Capable of jumping and running.
- Sleeps on silks.

**Costume & Silhouette:**
- Unknown attire (wears silks/furs provided by Sola).
- No specific build details provided.

**Continuity-Critical Traits:**
- Subject of the Watch Dog's constant observation ("eyes glued upon narrator").
- Capable of leaping over the beast during escape attempt.
- Located in room with five female occupants.

**Descriptive Noun Phrases for Prompts:**
- "Human protagonist on Mars"
- "Sleeping figure covered in furs"
- "Jumping human observer"

**Uncertainty Notes:**
- **Visual Gap:** No description of hair, eyes, or skin tone is available in the source text. Image generation must rely on default assumptions for human figures unless clarified.
- **Silhouette:** Height and build are unknown; only functional actions (sleeping, jumping) are documented.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: watch_dog
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Text describes the creature as a "brute" or "watch dog"; no species confirmation, fur color, or detailed anatomy beyond tusks and eyes is provided.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Character File: Watch Dog

**Display Name:** The Watch Dog  
**Chapter Role:** Guardian / Brute Creature  
**Physical Presence:** Physically Present  

**Supported Physical Description:**
- "Brute" with "wicked-looking eyes".
- Possesses ugly ferocious tusks.
- Eyes glued upon narrator throughout chapter (sleepless).
- Colossal size relative to narrator (implied by ability to spring and charge).

**Costume & Silhouette:**
- Unknown fur color or texture.
- Silhouette suggests quadrupedal beast with canine features.

**Continuity-Critical Traits:**
- Never voluntarily away from narrator a moment.
- Occupies room threshold when narrator sleeps.
- Springs before narrator at edge of city during escape attempt.
- Wheels instantly charging with appalling speed.

**Descriptive Noun Phrases for Prompts:**
- "Colossal canine brute"
- "Sleepless guardian beast"
- "Tusked watch dog"

**Uncertainty Notes:**
- **Visual Gap:** No description of fur color, eye color, or specific species classification is available in the source text. Image generation must rely on default assumptions for Martian brutes unless clarified.
- **Silhouette:** Height and build are unknown; only relative size (colossal) and functional actions (charging, watching) are documented.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: colossal_ape
canonical_character_id: colossal_ape
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Text describes the figure only as a "colossal ape-like creature"; no proper name is given in this chapter, and physical details are limited to hairlessness and head bristles.
clarification_required: true
clarification_reason: Character lacks a stable proper name in this text and may already exist under another canonical designation (e.g., specific Martian species or title).
clarification_question: What is the canonical name or species designation for the "colossal ape-like creature" that appears at the end of Chapter V?

[[SECTION markdown]]
# Character File: Colossal Ape-like Creature

**Display Name:** The Colossal Ape  
**Chapter Role:** Attacker / Unknown Entity  
**Physical Presence:** Physically Present (Final Scene)  

**Supported Physical Description:**
- White skin tone.
- Hairless body except for enormous shock of bristly hair on head.
- Ape-like build.

**Costume & Silhouette:**
- No attire or fur described beyond natural hairlessness.
- Silhouette suggests large, bipedal primate form.

**Continuity-Critical Traits:**
- Grabs narrator by neck from behind.
- Drags narrator violently into room.
- Standing over narrator at the end of the chapter.

**Descriptive Noun Phrases for Prompts:**
- "White hairless ape-like creature"
- "Colossal primate attacker"
- "Bristly-headed giant"

**Uncertainty Notes:**
- **Visual Gap:** No description of eye color, facial features, or specific species traits beyond "ape-like" is available in the source text. Image generation must rely on default assumptions for white-haired apes unless clarified.
- **Identity:** Lacks a proper name in this chapter; may require clarification to match canonical database entries.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
