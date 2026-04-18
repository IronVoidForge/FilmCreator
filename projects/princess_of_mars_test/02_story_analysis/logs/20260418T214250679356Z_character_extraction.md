# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:42:50.679356+00:00
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

# Chapter Title
A Fair Captive from the Sky

# Summary
The narrator returns to the city after an incubator ceremony but is ordered to retreat immediately. From a window on an upper floor, he witnesses the arrival of twenty gray airships approaching the deserted city. The green Martian warriors fire a volley from building windows, causing the fleet to return fire. A battle ensues where the fleet's sighting apparatus and crews are targeted.

# Scene Breakdown
1. **Retreat Order:** The procession debouches into open ground; orders given for hasty return. Green Martians melt into doorways within three minutes.
2. **Observation:** Narrator enters a building (same one with ape encounter) and mounts to an upper floor. He sees the cause of retreat: twenty gray airships swinging over hills.
3. **Engagement:** Each vessel carries a strange banner and odd device on prow. Figures crowd forward decks. Green Martians fire volley; foremost vessel swings broadside, returns fire, and moves parallel to front before turning back. Other vessels follow.
4. **Battle Accuracy:** Narrator notes deadly accuracy of aim (25% shots wild). Little figure on craft drops at explosion of each bullet; banners and upper works dissolve in flame.
5. **Fleet Retreat:** Twenty minutes after first volley, fleet swings trailing off. Several craft limping, barely under control. Fire ceases; energies focused on escape.
6. **Disabled Ship:** One ship receives brunt of fire, unmanned, drifting southeast. Warriors cease firing as vessel appears helpless.
7. **Capture:** Warriors rush to roofs to cover possibility of return fleet/reinforcements. Disabled ship drifts some fifty feet above ground. Warriors gallop ahead, dismount, enter building she is destined to touch.
8. **Boarding:** Just before strike, warriors swarm from windows, ease shock of collision with spears. Grappling hooks thrown; big boat hauled to ground.
9. **Looting:** Warriors search vessel stem to stern. Examine dead sailors for signs of life. Drag little figure among them (considerably less than half as tall as green Martians).
10. **Removal:** Prisoner removed to ground. Systematic rifling of vessel begins. Arms, ammunition, silks, furs, jewels, stone vessels, solid foods/liquids (including casks of water) requisitioned. Chariots transport loot.
11. **Destruction:** Lines fast to craft; towed far out into valley southwesterly. Warriors board and empty contents of carboys upon dead sailors/decks. Last warrior throws missile back; faint spurt of flame rises. Guy ropes released; warship lightened by loot removal soars majestically into air, decks/upper works mass of roaring flames.
12. **Aftermath:** Ship drifts to southeast, rising higher as flames eat wooden parts. Narrator ascends to roof and watches for hours until lost in distance. Awe-inspiring sight of floating funeral pyre.
13. **Emotional Reaction:** Narrator depressed; scene marks defeat/annihilation of forces of kindred people rather than routing by green warriors. Strange yearning toward unknown foemen; hope fleet would return.
14. **Return to Plaza:** Woola follows at heel. Sola rushes up as cavalcade returns to plaza. Homeward march given up for day; not recommenced for more than a week due to fear of return attack.
15. **Prisoner Reveal:** As Sola and I enter plaza, sight met eyes: prisoner from battle craft roughly dragged into nearby building by couple of green Martian females.
16. **Final Encounter:** Slender, girlish figure similar to earthly women. Oval face, beautiful features, large lustrous eyes, coal black waving hair caught loosely into strange coiffure. Light reddish copper skin, crimson glow cheeks, ruby lips. Destitute of clothes save for highly wrought ornaments; entirely naked.
17. **Eye Contact:** Gaze rests on me; eyes open wide in astonishment. Makes little sign with free hand (appeal for succor/protection). Look of hope fades into dejection, loathing, contempt. Dragged out of sight into depths of deserted edifice.

# Visual Continuity Facts
- **Prisoner Appearance:** Oval face, coal black waving hair, light reddish copper skin, naked save for ornaments.
- **Airships:** Gray-painted, long and low, swinging over hills with banners.
- **Green Martians:** Melting into doorways, firing from windows, swarming from windows to board disabled ship.
- **Disabled Ship:** Drifting southeast, unmanned, eventually burning and drifting away.

# Story Summary Facts
- **Incubation:** Return march after ceremony interrupted by airship attack.
- **Fleet Destruction:** Twenty ships destroyed; one captured and burned.
- **Prisoner Capture:** Human woman captured from disabled ship.
- **Emotional State:** Narrator feels depression over defeat of kindred people; hope for fleet return.
- **Location:** Green Martian city, plaza, upper floor window.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1
[[SECTION character_index_markdown]]
# Character Index - CH001

| Character | Role | Status |
| :--- | :--- | :--- |
| Narrator | Protagonist / Observer | Identified |
| Sola | Companion / Witness | Identified |
| Woola | Companion / Witness | Identified |
| Green Martian | Antagonist / Warrior | Identified (Species) |
| The Prisoner | Captive / Subject | Identified |
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: "I", "me"
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance of narrator is not described in the chapter.
clarification_required: true
clarification_question: Please describe the narrator's physical appearance and attire.
[[SECTION markdown]]
# Narrator

**Chapter Role:** Protagonist / Observer
**Physical Presence:** Present (Upper floor, Plaza)
**Description:** Not described in text.
**Notes:** Needs clarification on appearance for image generation consistency.
**Continuity:** Observes battle from window; enters plaza with Sola; witnesses prisoner capture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: None
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance of Sola is not described in the chapter.
clarification_required: true
clarification_question: Please describe Sola's physical appearance and attire.
[[SECTION markdown]]
# Sola

**Chapter Role:** Companion / Witness
**Physical Presence:** Present (Plaza)
**Description:** Not described in text.
**Notes:** Needs clarification on appearance for image generation consistency.
**Continuity:** Follows narrator; rushes up to plaza; enters with narrator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: None
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance of Woola is not described in the chapter.
clarification_required: true
clarification_question: Please describe Woola's physical appearance and attire.
[[SECTION markdown]]
# Woola

**Chapter Role:** Companion / Witness
**Physical Presence:** Present (Following Narrator)
**Description:** Not described in text.
**Notes:** Needs clarification on appearance for image generation consistency.
**Continuity:** Follows at heel; accompanies narrator home.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian
canonical_character_id: green_martian
aliases: None
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific physical build and height of Green Martians are not described in the chapter.
clarification_required: true
clarification_question: Please describe the standard physical build and attire of a Green Martian.
[[SECTION markdown]]
# Green Martian

**Chapter Role:** Antagonist / Warrior
**Physical Presence:** Present (Throughout chapter)
**Description:** Green skin, humanoid shape implied.
**Notes:** Needs clarification on build/attire for image generation consistency.
**Continuity:** Fire from windows; board disabled ship; drag prisoner; loot vessel.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner
canonical_character_id: prisoner
aliases: None
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical appearance is fully described in the chapter.
clarification_required: false
clarification_question: None
[[SECTION markdown]]
# The Prisoner

**Chapter Role:** Captive / Subject of Study
**Physical Presence:** Present (Dragged into building)
**Description:** Oval face, coal black hair, light reddish copper skin, naked save for ornaments.
**Notes:** Fully described in text; no manual description required.
**Continuity:** Dragged from disabled airship; examined by warriors; removed to ground; looted vessel.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
