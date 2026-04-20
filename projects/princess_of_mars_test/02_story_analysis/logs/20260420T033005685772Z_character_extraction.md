# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:30:05.685772+00:00
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

# Chapter V: The Watch Dog and the Escape Attempt

## Visual Continuity Facts
- **Room Interior:** Lined with silks and furs; mural painting depicts mountains, rivers, lakes, oceans, meadows, trees, flowers, winding roadways, sun-kissed gardens. Vegetation colorings differ from Earth views. No living animals depicted in murals.
- **Sola's Appearance:** Female guardian; brings food and drink; sits short ways off regarding narrator intently.
- **Watch Dog Appearance:** Short legs; wicked-looking eyes; ferocious tusks; white hairless body (implied by later capture context); glues eyes upon narrator while sleeping.
- **Ape-like Creature Appearance:** Colossal, white, hairless except for enormous shock of bristly hair on head; stands over narrator after capture.
- **Lighting Conditions:** Dark when narrator awakes; daylight when escape attempt concludes.
- **Coverings:** Fur thrown over narrator by unseen hand (Sola); silks and furs piled high on other occupants.

## Story Summary: Scene Breakdown
- **Scene 1: Sola's Departure & Dog Introduction**
  - Sola stares into the brute's eyes, mutters commands, points to narrator, and leaves the chamber.
  - Narrator observes the beast (Martian watch dog) surveying him intently before crossing to the exit threshold and lying down full length.
  - Narrator notes this is his first experience with a Martian watch dog but destined not to be last; the beast guards him carefully during captivity, twice saving his life.

- **Scene 2: Room Inspection & Food Delivery**
  - While Sola is away, narrator examines the room minutely (mural painting details).
  - Sola returns bearing food and drink.
  - Food placed on floor: ~1 pound of solid substance (cheese-like consistency, almost tasteless).
  - Liquid is milk from a large plant (not animal source), distilling supply from soil/air/sun rays.
  - Narrator eats, feels invigorated, and sleeps for several hours until dark.

- **Scene 3: Sleep Cycle & Guardian Care**
  - Narrator wakes in darkness, feeling very cold.
  - Someone throws a fur over him; partially dislodged.
  - Hand reaches out to pull fur over narrator and add another covering.
  - Narrator presumes guardian is Sola (confirmed later).
  - Sola's characteristics: Sympathy, kindliness, affection; ministrations unfailing; care saves from suffering/hardships.

- **Scene 4: Escape Attempt Preparation**
  - Narrator feels need to learn beast's attitude toward him.
  - Believes he can escape if pursued outside building due to jumping ability.
  - Notes dog's short legs are a bar to swiftness (no jumper/runner).
  - Gains feet slowly; watcher does same.

- **Scene 5: The Escape Execution**
  - Narrator advances with shuffling gait; retains balance, makes rapid progress.
  - Brute backs away cautiously; moves to one side when narrator reaches open space.
  - Brute follows about ten paces in rear as narrator makes way along deserted street.
  - At city edge, brute springs before narrator, uttering strange sounds, baring ugly ferocious tusks.
  - Narrator rushes toward him, leaps into air, alights far beyond him and away from city.

- **Scene 6: The Chase & Capture**
  - Brute wheels instantly and charges with appalling speed (fleetest animal on Mars).
  - Narrator realizes difficulty escaping on straightaway course; doubles in tracks, leaps over brute.
  - Reaches city ahead of him; jumps for window ~30 feet from ground in building overlooking valley.
  - Grasps sill, pulls up to sitting posture without looking into building.
  - Gazed down at baffled animal beneath.
  - Exultation short-lived: Huge hand grasps narrator by neck from behind, drags violently into room.
  - Thrown upon back; beholds standing over him a colossal ape-like creature (white, hairless, bristly head).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter V: The Watch Dog and the Escape Attempt

| Character | Role | Physical Presence | Description Status |
|-----------|------|-------------------|-------------------|
| Sola | Female Guardian | Referenced (not visually present in chapter) | Manual description required |
| Watch Dog | Martian Beast | Present (surveys narrator, guards chamber) | Manual description required |
| Ape-like Creature | Colossal Capturer | Present (captures narrator at city edge) | Manual description required |

**Notes:** All characters have sparse physical descriptions insufficient for dependable image generation. Additional visual details needed for render-facing prompts.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: Female Guardian, Sympathetic Caregiver
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is sparse (female guardian who brings food/drink) - insufficient visual details for dependable image generation. Needs specific facial features, body proportions, and distinctive markings documented.
clarification_required: false
clarification_reason: Character is well-named throughout chapter with consistent identification
clarification_question: 

[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Female Guardian / Sympathetic Caregiver  
**Physical Presence:** Referenced (not visually present in chapter)  

## Physical Description Status
**Supported by Source:** Limited  
- Female guardian who brings food and drink to narrator  
- Sits short ways off regarding narrator intently  
- Shows sympathy, kindliness, affection toward narrator  
- Provides unfailing care and ministrations  

## Uncertainty Notes
**Missing Details:**
- No facial features documented (eyes, nose, mouth)
- No body proportions specified (height, build)
- No hair color or style mentioned
- No distinctive markings or accessories noted
- No skin tone or complexion described

**Render-Facing Prompt Needs:**
- Specific facial structure and expression details required
- Body type and posture documentation needed
- Hair and clothing descriptions absent from source material
- Distinctive visual identifiers not established in chapter

## Continuity-Critical Traits
- Sympathetic caregiver role confirmed through actions (food delivery, covering narrator with fur)
- Guardian identity verified by narrator presumption and later confirmation
- Caregiver functions: feeding, warming, protecting narrator from suffering/hardships
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: Watch Dog
aliases: Martian Watch Dog, Brute, Beast
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is sparse (short legs, wicked eyes, ferocious tusks) - insufficient visual details for dependable image generation. Needs specific head shape, eye structure, tusk arrangement, and body proportions documented.
clarification_required: false
clarification_reason: Character is well-named throughout chapter with consistent identification as Martian watch dog
clarification_question: 

[[SECTION markdown]]
# Watch Dog

**Display Name:** Watch Dog  
**Chapter Role:** Martian Beast / Guardian  
**Physical Presence:** Present (surveys narrator, guards chamber, follows escape attempt)  

## Physical Description Status
**Supported by Source:** Limited  
- Short legs documented  
- Wicked-looking eyes noted  
- Ferocious tusks specified  
- White hairless body implied by later capture context  
- Glues eyes upon narrator while sleeping  

## Uncertainty Notes
**Missing Details:**
- No head shape or facial structure described
- No eye color or pupil structure documented
- No tusk arrangement or size specifications
- No body proportions (length, width, height) specified
- No fur texture beyond "hairless" noted
- No tail or limb count mentioned

**Render-Facing Prompt Needs:**
- Head and facial anatomy details required
- Eye structure and expression documentation needed
- Tusk positioning and arrangement absent from source
- Body proportions and silhouette not established

## Continuity-Critical Traits
- Guardian role confirmed: guards narrator carefully during captivity
- Life-saving actions documented: twice saves narrator's life
- Physical limitations noted: short legs are bar to swiftness (no jumper/runner)
- Martian species identification: fleetest animal on Mars when charging
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: ape_like_creature
canonical_character_id: Ape-like Creature
aliases: Colossal Capturer, Huge Hand, Standing Over Narrator
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is sparse (colossal, white, hairless except for enormous shock of bristly hair on head) - insufficient visual details for dependable image generation. Needs specific facial features, body proportions, and arm/limb structure documented.
clarification_required: false
clarification_reason: Character is well-named throughout chapter with consistent identification as ape-like creature
clarification_question: 

[[SECTION markdown]]
# Ape-like Creature

**Display Name:** Ape-like Creature  
**Chapter Role:** Colossal Capturer / Guardian  
**Physical Presence:** Present (captures narrator at city edge, stands over him in room)  

## Physical Description Status
**Supported by Source:** Limited  
- Colossal size documented  
- White coloration specified  
- Hairless body noted  
- Enormous shock of bristly hair on head mentioned  
- Huge hand grasps narrator by neck from behind  

## Uncertainty Notes
**Missing Details:**
- No facial features described (eyes, nose, mouth)
- No body proportions beyond "colossal" specified
- No arm/limb structure or length documented
- No tail presence or absence noted
- No additional markings or accessories mentioned
- No posture or stance details recorded

**Render-Facing Prompt Needs:**
- Facial anatomy and expression details required
- Body proportions and scale documentation needed
- Arm and limb structure absent from source material
- Hair distribution beyond head shock not specified

## Continuity-Critical Traits
- Capturer role confirmed: drags narrator violently into room after escape attempt
- Standing posture documented: beholds standing over him in room
- Size contrast emphasized: colossal compared to narrator
- White hairless body with bristly head creates distinctive silhouette
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
