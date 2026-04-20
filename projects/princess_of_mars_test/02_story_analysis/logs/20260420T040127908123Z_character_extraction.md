# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:01:27.908123+00:00
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

Chapter id: CH019

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

# Chapter Summary: CH019 - Battling in the Arena

**Visual Continuity Facts:**
- **Dungeon/Cell:** Dark environment; keys missing from dead jailer's body.
- **Amphitheater:** Excavated below ground surface, filled with debris, holds 20,000 Warhoons.
- **Arena:** Immense, uneven, unkempt, piled with building stone to prevent escape. Cages at ends holding victims.
- **Audience:** Seating space occupied, Dak Kova and chieftains on raised platform.
- **Victims:** Green Martian females, calots (wild dogs), mad zitidars, green warriors, women of other hordes, wild beasts.

**Story Progression:**
1. Carter regains composure, realizes keys are gone, Dejah Thoris taken to lair.
2. No food for two days, then new messenger.
3. Kantos Kan arrives as new prisoner (red Martian/Heliumite). They exchange greetings and stories.
4. Kantos details his escape from Zodanga after the defeat of battleships.
5. Caged together in amphitheater for games.
6. Games begin: Green females vs calots, then mad zitidar, etc.
7. Carter fights men/beasts easily with long-sword.
8. Final three left: Green warrior, Kantos Kan, Carter.
9. Kantos kills green warrior with thrown sword.
10. Carter and Kantos fight to death (fake out). Carter survives in darkness.
11. Carter escapes stealthily to top of amphitheater, reaches hills east of city.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH019

| Character | Role | Status | Description Availability |
|-----------|------|--------|-------------------------|
| Carter | Main protagonist, arena fighter | Physically present | Limited physical details |
| Dejah Thoris | Princess, taken to lair | Referenced only | Limited physical details |
| Kantos Kan | Red Martian prisoner, arena fighter | Physically present | Limited physical details |
| Dak Kova | Audience member on platform | Referenced only | Minimal details |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: Carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides minimal physical description (long-sword mentioned, fighting ability noted) but lacks detailed facial features, hair, skin tone, body build for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Carter - CH019

**Display Name:** Carter  
**Chapter Role:** Main protagonist, arena fighter  
**Physical Presence:** Physically present (fighting in amphitheater)  

**Physical Description:** Limited details available. Identified as having a long-sword for combat. Fighting ability noted as effective against men and beasts. One of final three survivors in arena games.

**Costume/Silhouette:** No specific costume or silhouette details provided in chapter summary. Wears standard attire for arena fighter (implied).

**Continuity-Critical Traits:** Long-sword wielder, skilled combatant, survived amphitheater games to reach hills east of city.

**Uncertainty Notes:** Physical appearance details (facial features, hair, skin tone, body build) are not sufficiently documented in this chapter for dependable later image generation. Additional physical description required for render-facing prompt writing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejath_thoris
canonical_character_id: Dejah Thoris
aliases: Princess of Mars (implied by project name)
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter only references her as taken to lair; no physical description provided in this chapter's material for dependable image generation
clarification_required: true
clarification_reason: Character may already exist under established name from earlier chapters; needs verification of current identification status
clarification_question: Is Dejah Thoris's physical appearance consistent with prior chapter documentation, or does this chapter require new descriptive details?
[[SECTION markdown]]
# Dejah Thoris - CH019

**Display Name:** Dejah Thoris  
**Chapter Role:** Princess, taken to lair (referenced character)  
**Physical Presence:** Referenced only (not physically present in amphitheater)  

**Physical Description:** No physical description provided in this chapter's material. Identified as princess and taken to lair by Carter after realizing keys are gone.

**Costume/Silhouette:** No specific costume or silhouette details available in chapter summary.

**Continuity-Critical Traits:** Principal female lead, captured/taken to lair during arena events.

**Uncertainty Notes:** Physical appearance details are not documented in this chapter for dependable later image generation. Character identification status may need clarification against prior chapter documentation. Additional physical description required for render-facing prompt writing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: Red Martian, Heliumite
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter identifies him as red Martian/Heliumite but lacks detailed physical description (facial features, hair, skin tone, body build) for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Kantos Kan - CH019

**Display Name:** Kantos Kan  
**Chapter Role:** Red Martian prisoner, arena fighter  
**Physical Presence:** Physically present (fighting in amphitheater)  

**Physical Description:** Limited details available. Identified as red Martian/Heliumite. Details escape from Zodanga after defeat of battleships. One of final three survivors in arena games.

**Costume/Silhouette:** No specific costume or silhouette details provided in chapter summary. Wears standard attire for arena fighter (implied).

**Continuity-Critical Traits:** Red Martian identity, skilled combatant with thrown sword, killed green warrior, survived fight with Carter to reach hills east of city.

**Uncertainty Notes:** Physical appearance details (facial features, hair, skin tone, body build) are not sufficiently documented in this chapter for dependable later image generation. Additional physical description required for render-facing prompt writing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: Dak Kova
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter only mentions name and location (audience member on raised platform); no physical description provided for dependable image generation
clarification_required: true
clarification_reason: Character may already exist under established name from earlier chapters; needs verification of current identification status
clarification_question: Is Dak Kova's physical appearance consistent with prior chapter documentation, or does this chapter require new descriptive details?
[[SECTION markdown]]
# Dak Kova - CH019

**Display Name:** Dak Kova  
**Chapter Role:** Audience member on raised platform (referenced character)  
**Physical Presence:** Referenced only (not physically present in amphitheater fighting)  

**Physical Description:** No physical description provided in this chapter's material. Identified as audience member seated on raised platform with chieftains.

**Costume/Silhouette:** No specific costume or silhouette details available in chapter summary.

**Continuity-Critical Traits:** Audience representative, positioned on raised platform during arena games.

**Uncertainty Notes:** Physical appearance details are not documented in this chapter for dependable later image generation. Character identification status may need clarification against prior chapter documentation. Additional physical description required for render-facing prompt writing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
