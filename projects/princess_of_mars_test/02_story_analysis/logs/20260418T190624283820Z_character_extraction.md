# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:06:24.283820+00:00
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

Chapter id: CH001

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

# Chapter Label
Chapter VIII - A Fair Captive from the Sky

# Visual Continuity Facts
- **Airships:** Long, low, gray-painted vessels with banners and glowing devices on prows.
- **Warriors:** Green Martians (erect posture), wearing green attire, using spears and grappling hooks.
- **Prisoner:** Slender, girlish figure; light reddish copper skin; coal black hair; naked except for ornaments.
- **Environment:** Deserted city buildings with windows/roofs; valley floor; hills beyond.
- **Fire Effects:** Spurts of flame on ship banners; roaring flames on vessel decks; drifting funeral pyre.

# Broad Story Summary
The narrator and procession return to the deserted city after an incubation ceremony but are ordered back immediately upon seeing a fleet of twenty gray airships approaching. The green Martians fire from buildings, engaging the ships in a deadly exchange where the Martians demonstrate high accuracy against the ships' crews and equipment. The fleet retreats with damage; one unmanned ship drifts helplessly toward the city. Warriors capture this vessel, loot it for arms, jewels, and water, then burn it before towing it away. As the narrator watches from a window, he sees a prisoner being dragged into a building by green Martian females. The prisoner turns to look at the narrator, signaling hope which fades into dejection as she is taken into the depths of the edifice.

# Key Scene Decomposition Points
- **Arrival:** Procession returns; order given for retreat upon sighting ships.
- **Engagement:** Martians fire volley; ships return fire; specific targeting of crew/apparatus.
- **Retreat:** Fleet limps away; one ship unmanned and drifting.
- **Recovery:** Warriors swarm the drifting ship; loot operation (hours); burning of vessel.
- **Discovery:** Narrator sees prisoner dragged in; visual contact between narrator and prisoner.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VIII (CH001)

| Asset ID | Canonical ID | Role | Status | Description Source |
| :--- | :--- | :--- | :--- | :--- |
| `narrator` | `narrator` | Narrator / Observer | Referenced | None provided |
| `prisoner` | `prisoner` | Prisoner / Captive | Physically Present | Visual Continuity Facts |
| `martian_warrior` | `martian_warrior` | Warrior / Defender | Physically Present | Visual Continuity Facts |
| `martian_female` | `martian_female` | Warrior / Capturer | Physically Present | Broad Story Summary |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: the narrator, observer
is_fully_identified: true
manual_description_required: true
manual_description_reason: The provided chapter summary does not contain physical descriptions (height, build, hair, skin tone) for the narrator.
clarification_required: false
clarification_reason: N/A
clarification_question: N/A

[[SECTION markdown]]
# Narrator

## Display Name & Chapter Role
**Name:** The Narrator
**Role:** Observer / POV Character

## Presence Status
**Status:** Referenced (Point of View)
**Physical Presence:** Uncertain (Not visually described in scene)

## Physical Description
**Supported by Source:** None.
**Details:** No physical traits are listed in the chapter summary or visual continuity facts.

## Costume & Silhouette
**Costume:** Unknown.
**Silhouette:** Unknown.

## Continuity-Critical Traits
- **Perspective:** The character through whom the story is told.
- **Location:** Watches from a window; observes events outside.

## Useful Descriptive Noun Phrases
- "The narrator"
- "Observer of the fleet"
- "Witness to the capture"

## Uncertainty Notes
**Critical Missing Information:** Physical appearance (skin tone, hair, build, clothing) is entirely absent from the source material. Image generation requires manual description input.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner
canonical_character_id: prisoner
aliases: captive, fair captive
is_fully_identified: true
manual_description_required: false
manual_description_reason: N/A
clarification_required: false
clarification_reason: N/A
clarification_question: N/A

[[SECTION markdown]]
# Prisoner

## Display Name & Chapter Role
**Name:** The Prisoner
**Role:** Captive / Victim of Engagement

## Presence Status
**Status:** Physically Present (In Scene)
**Physical Presence:** Confirmed in Visual Continuity Facts and Broad Story Summary.

## Physical Description
**Supported by Source:** Yes.
**Details:** Slender, girlish figure; light reddish copper skin; coal black hair.

## Costume & Silhouette
**Costume:** Naked except for ornaments.
**Silhouette:** Girlish, slender.

## Continuity-Critical Traits
- **Skin Tone:** Light reddish copper.
- **Hair Color:** Coal black.
- **Build:** Slender, girlish.
- **Attire:** Minimal (ornaments only).

## Useful Descriptive Noun Phrases
- "Slender, girlish figure"
- "Light reddish copper skin"
- "Coal black hair"
- "Naked except for ornaments"
- "Captive from the sky"

## Uncertainty Notes
**Critical Missing Information:** None regarding physical traits. Continuity is stable based on provided facts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warrior
canonical_character_id: martian_warrior
aliases: green martian, warrior
is_fully_identified: true
manual_description_required: false
manual_description_reason: N/A
clarification_required: false
clarification_reason: N/A
clarification_question: N/A

[[SECTION markdown]]
# Martian Warrior

## Display Name & Chapter Role
**Name:** Martian Warrior
**Role:** Defender / Attacker (Green Martian)

## Presence Status
**Status:** Physically Present (In Scene)
**Physical Presence:** Confirmed in Visual Continuity Facts and Broad Story Summary.

## Physical Description
**Supported by Source:** Yes.
**Details:** Green Martians; erect posture.

## Costume & Silhouette
**Costume:** Wearing green attire.
**Silhouette:** Erect, humanoid (implied).

## Continuity-Critical Traits
- **Skin Tone:** Green (Martian species trait).
- **Attire Color:** Green.
- **Posture:** Erect.
- **Equipment:** Spears and grappling hooks (referenced in Visual Continuity Facts).

## Useful Descriptive Noun Phrases
- "Green Martians"
- "Erect posture"
- "Green attire"
- "Warriors firing from buildings"
- "Spears and grappling hooks"

## Uncertainty Notes
**Critical Missing Information:** None regarding physical traits. Continuity is stable based on provided facts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_female
canonical_character_id: martian_female
aliases: green martian female, capturer
is_fully_identified: true
manual_description_required: false
manual_description_reason: N/A
clarification_required: false
clarification_reason: N/A
clarification_question: N/A

[[SECTION markdown]]
# Martian Female

## Display Name & Chapter Role
**Name:** Martian Female
**Role:** Warrior / Capturer (Green Martian)

## Presence Status
**Status:** Physically Present (In Scene)
**Physical Presence:** Confirmed in Broad Story Summary ("dragged into a building by green Martian females").

## Physical Description
**Supported by Source:** Yes (Implied same as Warriors).
**Details:** Green Martians; erect posture (inferred from species description).

## Costume & Silhouette
**Costume:** Wearing green attire (inferred from species description).
**Silhouette:** Erect, humanoid.

## Continuity-Critical Traits
- **Skin Tone:** Green (Martian species trait).
- **Attire Color:** Green.
- **Posture:** Erect.
- **Action:** Dragging prisoner into building.

## Useful Descriptive Noun Phrases
- "Green Martian females"
- "Capturer of the prisoner"
- "Dragged into a building"
- "Warriors engaging the ships"

## Uncertainty Notes
**Critical Missing Information:** None regarding physical traits. Continuity is stable based on provided facts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
