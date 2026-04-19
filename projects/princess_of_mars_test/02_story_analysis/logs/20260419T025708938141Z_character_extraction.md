# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:57:08.938141+00:00
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

Chapter id: CH008

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

# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Beats (Decomposition Ready)
1.  **Return Interrupted:** Procession returns to city after incubation ceremony; sudden retreat order given immediately upon entering open ground.
2.  **Fleet Sighting:** Carter observes gray-painted airships approaching from hill crest; fleet count approximates twenty vessels.
3.  **Battle Engagement:** Green Martians fire first volley; enemy ships return fire with high accuracy targeting specific weak points (guns, officers, steering).
4.  **Ship Disabled:** One vessel limps erratically, unmanned, drifting southeast. Warriors rush to intercept before it hits buildings.
5.  **Looting & Burning:** Warriors board disabled ship, remove loot (arms, jewels, water), empty carboys over dead sailors, then burn vessel from within using missile.
6.  **Emotional Aftermath:** Carter feels depression and yearning for the enemy fleet; fears return attack; city remains deserted for a week.
7.  **Captive Discovery:** As prisoners are dragged into building, Carter sees a slender girlish figure with copper skin and black hair. She signals him before being taken inside.

## Visual Continuity Facts
- **Airships:** Long, low, gray-painted hulls; banners swung from stem to stern; odd devices painted on prow.
- **Warriors:** Green Martians; mounted or in chariots; fire from windows/roofs; carry spears and grappling hooks.
- **Disabled Ship:** Drifting southeast at approx fifty feet altitude; decks and upper works mass of roaring flames later; wooden parts eaten away.
- **Captive Appearance:** Slender, girlish figure; oval face; light reddish copper skin; coal black waving hair (loose coiffure); naked except highly wrought ornaments; crimson cheeks/ruby lips.
- **Locations:** City plaza, building upper floors/windows, open ground/valley, outlying hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH008

## Extracted Characters

| Asset ID | Canonical ID | Display Name | Role | Physical Presence | Description Status |
|----------|--------------|--------------|------|-------------------|-------------------|
| carter | carter | Carter | Observer/Narrator | Present | No physical description in chapter |
| captive | princess_of_mars | The Captive | Signal-sender | Present | Detailed visual description provided |

## Notes

- **Carter**: Main observer throughout chapter; no physical or visual description given in text. Character is physically present in city plaza/building but lacks renderable details.

- **The Captive**: Slender girlish figure with copper skin and black hair seen by Carter before being taken inside building. Detailed physical description provided but canonical name not explicitly stated in chapter text.

## Uncertainty Flags

- Both characters require manual descriptions due to insufficient visual/physical details for dependable image generation
- The Captive requires clarification regarding canonical identity (Princess of Mars)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided for character in chapter text
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter - Chapter CH008

## Display Name
Carter

## Chapter Role
Observer/Narrator

## Physical Presence
Present - physically located in city plaza/building throughout chapter

## Physical Description
**Status:** No physical or visual description provided in chapter text

**Supported Details:** None from source material

**Uncertainty Notes:** 
- Character serves as primary observer but lacks any physical description in this chapter
- Cannot generate dependable images without manual description intervention
- Role is clear (observer/narrator) but visual identity is undefined in source

## Costume, Silhouette, Continuity Traits
**Status:** Not described in chapter text

**Supported Details:** None from source material

**Continuity-Critical Traits:** 
- Observer position: city plaza/building upper floors/windows
- No costume or silhouette details available for render-facing prompts

## Render-Facing Prompt Noun Phrases
- "observer character" (placeholder)
- "city plaza location" (contextual)
- "no physical description - requires manual intervention" (uncertainty flag)

## Uncertainty Summary
This character lacks any physical or visual description in the provided chapter text. While their role as observer is clear, no renderable details exist for dependable image generation. Manual description required before proceeding with visual production.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captive
canonical_character_id: princess_of_mars
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character visually described but canonical name not provided in chapter text
clarification_required: true
clarification_reason: Character is clearly Princess of Mars from story context but chapter does not explicitly name her; requires confirmation of intended identity
clarification_question: Is this slender girlish figure with copper skin and black hair intended to be Princess of Mars?

[[SECTION markdown]]
# The Captive - Chapter CH008

## Display Name
The Captive

## Chapter Role
Signal-sender / Prisoner

## Physical Presence
Present - seen by Carter before being taken inside building

## Physical Description
**Status:** Detailed visual description provided in chapter text

**Supported Details:** 
- Slender, girlish figure
- Oval face
- Light reddish copper skin
- Coal black waving hair (loose coiffure)
- Naked except highly wrought ornaments
- Crimson cheeks/ruby lips

**Uncertainty Notes:** 
- Canonical name not explicitly stated in chapter text
- Physical description is complete but identity confirmation needed

## Costume, Silhouette, Continuity Traits
**Status:** Partially described in chapter text

**Supported Details:** 
- Silhouette: slender, girlish figure
- Hair: coal black, waving, loose coiffure
- Skin tone: light reddish copper
- Adornments: highly wrought ornaments (no specific costume details)
- Facial features: oval face, crimson cheeks, ruby lips

**Continuity-Critical Traits:** 
- Signal-sender gesture made to Carter before capture
- Taken inside building as prisoner
- No specific costume or armor described beyond ornaments

## Render-Facing Prompt Noun Phrases
- "slender girlish figure" (silhouette)
- "copper skin tone" (color)
- "coal black waving hair" (hair description)
- "highly wrought ornaments" (adornments)
- "oval face with crimson cheeks and ruby lips" (facial features)

## Uncertainty Summary
This character has complete physical description but lacks explicit canonical naming in chapter text. While visual details are renderable, identity confirmation is required before proceeding. Clarification needed regarding whether this figure represents Princess of Mars from the story context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
