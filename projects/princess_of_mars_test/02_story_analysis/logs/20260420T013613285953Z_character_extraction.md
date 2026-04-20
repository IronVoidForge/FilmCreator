# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:36:13.286448+00:00
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

Chapter id: CH023

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

# Chapter XXIII: "Lost in the Sky" - Scene Breakdown

## Opening Sequence (Scenes 1-3)
**Location:** Zodanga Palace vicinity → adjoining building roof
**Action:** John Carter approaches Kantos Kan's quarters, discovers guards at entrance and rear. Uses hook strap to swing from roof of shop several doors away. Leaps between rooftops to reach open window where Kantos Kan is waiting.

**Dialogue Key Points:**
- Kantos Kan expected Carter earlier (tour of duty ended)
- News that Dejah Thoris promised hand to Sab Than fills both with dismay
- John Carter states he can solve difficulty if within sword's reach of Sab Than
- Kantos Kan reveals he loves Helium, Dejah Thoris, and Carter

## Mid-Chapter Sequence (Scenes 4-7)
**Location:** Zodanga Palace → Barracks Roof
**Action:** 
- Kantos Kan plans to kill Sab Than that night via secret entrance through pinnacle of highest tower
- John Carter climbs face of barracks building (1000 feet high) using ornamental ledges
- Reaches eaves but finds no opening through 20-foot projection
- Uses leather strap with great hook to swing from roof edge
- Kills sentry on duty, binds him, hangs him over edge

**Machine Preparation:**
- Retrieves both John Carter's machine and Kantos Kan's machine
- Makes Kantos Kan's fast behind John Carter's
- Starts engine, dives into streets below air patrol plane

## Flight Sequence (Scenes 8-12)
**Location:** Zodanga → En route to Helium
**Action:** 
- Kantos Kan drops into darkness while John Carter races through Martian sky
- Pursued by dozen air-scout craft and swift cruiser with battery of rapid-fire guns
- Uses twisting/turning tactics but losing ground
- Decides on straight-away course toward Helium
- Machine hit by well-directed shot from cruiser at prow
- Craft explodes, nearly capsized, hurtles downward through dark night

## Ending Sequence (Scenes 13-15)
**Location:** Over dead sea bottom → Approaching city
**Action:**
- Regains control after falling considerable distance
- Pursuers land in search of him
- Compass and speedometer destroyed by projectile fragment
- Morning found him over wrong city after nearly six hours
- Realizes Helium has distinctive twin towers (scarlet and yellow)

## Key Visual Continuity Facts
- High-altitude aerial pursuit with searchlights piercing night sky
- Rooftop climbing sequences showing ornate Barsoomian architecture
- Machine flight at high speed through Martian atmosphere
- Bullet impacts creating screeching sounds around craft
- Compass device described as clever little device that remains steadfastly fixed

## Critical Scene Decomposition Points
1. **Sneak Approach:** Carter's careful approach to guarded palace with multiple guards
2. **Rooftop Access:** Hook strap swing mechanism and sentry elimination
3. **Machine Retrieval:** Getting both machines ready for departure
4. **Pursuit Evasion:** Twisting/turning tactics against air-scout craft
5. **Damage Event:** Projectile hit destroying compass and speedometer
6. **Navigation Failure:** Morning arrival at wrong city due to destroyed guide
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XXIII: "Lost in the Sky"

## Characters Present or Referenced

| Name | Role | Status |
|------|------|--------|
| John Carter | Protagonist, machine pilot | Physically present |
| Kantos Kan | Antagonist/Ally figure, machine pilot | Physically present |
| Dejah Thoris | Referenced character | Not physically present |
| Sab Than | Referenced character | Not physically present |

## Notes

- John Carter and Kantos Kan are both physically present in this chapter's action sequences
- Dejah Thoris and Sab Than are only mentioned in dialogue without visual description
- All characters have stable identification by name
- No aliases or alternate names appear in this chapter's source material
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter XXIII

## Display Name & Role
**John Carter** - Main protagonist, machine pilot

## Physical Presence
Physically present throughout chapter's action sequences (approaches palace, climbs building, flies machine)

## Physical Description (Supported by Source)
- Climbs 1000-foot high barracks building using ornamental ledges
- Operates flying machine at high speed through Martian atmosphere
- Uses hook strap and leather strap with great hook for rooftop access
- Described as capable of solving difficulties "within sword's reach"

## Costume & Silhouette
- No specific costume details provided in this chapter's source material
- Machine pilot attire implied through action sequences

## Continuity-Critical Traits
- Compass device described as clever little device that remains steadfastly fixed
- Uses twisting/turning tactics during aerial pursuit evasion
- Regains control after falling considerable distance from machine damage

## Render-Facing Prompt Noun Phrases
- "1000-foot high climber"
- "machine pilot in Martian atmosphere"
- "ornate Barsoomian architecture navigator"
- "high-altitude aerial pursuer"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: kantos_kan
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Kantos Kan - Chapter XXIII

## Display Name & Role
**Kantos Kan** - Antagonist/Ally figure, machine pilot

## Physical Presence
Physically present throughout chapter's action sequences (waiting at window, plans assassination, flies machine)

## Physical Description (Supported by Source)
- Swings from roof of shop several doors away using hook strap
- Climbs face of barracks building using ornamental ledges
- Operates flying machine at high speed through Martian atmosphere
- Reveals love for Helium, Dejah Thoris, and Carter in dialogue

## Costume & Silhouette
- No specific costume details provided in this chapter's source material
- Machine pilot attire implied through action sequences

## Continuity-Critical Traits
- Plans to kill Sab Than that night via secret entrance through pinnacle of highest tower
- Makes his machine fast behind John Carter's machine for departure
- Uses leather strap with great hook to swing from roof edge
- Drops into darkness while John Carter races through Martian sky

## Render-Facing Prompt Noun Phrases
- "machine pilot in Martian atmosphere"
- "high-altitude aerial pursuer"
- "ornate Barsoomian architecture climber"
- "secret entrance planner"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description or visual details provided in this chapter's source material; only referenced in dialogue without appearance information

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter XXIII

## Display Name & Role
**Dejah Thoris** - Referenced character, love interest figure

## Physical Presence
Not physically present in this chapter; only mentioned in dialogue

## Physical Description (Supported by Source)
- No physical description provided in this chapter's source material
- Only referenced as having "promised hand to Sab Than" in dialogue

## Costume & Silhouette
- No costume or silhouette details available from this chapter's source material

## Continuity-Critical Traits
- Mentioned in context of news that fills both John Carter and Kantos Kan with dismay
- Character whose promise creates emotional stakes in the narrative

## Render-Facing Prompt Noun Phrases
- "referenced character without visual description"
- "love interest figure in dialogue-only mentions"
- "emotional stakeholder in Sab Than conflict"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: sab_than
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description or visual details provided in this chapter's source material; only referenced in dialogue without appearance information

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sab Than - Chapter XXIII

## Display Name & Role
**Sab Than** - Referenced character, antagonist figure

## Physical Presence
Not physically present in this chapter; only mentioned in dialogue

## Physical Description (Supported by Source)
- No physical description provided in this chapter's source material
- Only referenced as target of John Carter's potential intervention ("within sword's reach")

## Costume & Silhouette
- No costume or silhouette details available from this chapter's source material

## Continuity-Critical Traits
- Character whose hand being promised creates emotional stakes for both protagonists
- Target of Kantos Kan's planned assassination attempt that night

## Render-Facing Prompt Noun Phrases
- "referenced character without visual description"
- "antagonist figure in dialogue-only mentions"
- "emotional stakeholder in promise conflict"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
