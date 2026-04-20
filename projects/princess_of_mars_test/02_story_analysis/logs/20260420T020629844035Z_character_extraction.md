# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:06:29.844035+00:00
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

# Chapter Summary: CH001 - The Arizona Cave Entry

## Opening Context
Location: Arizona hills, March 1866. Captain John Carter alone after friend Powell's departure toward valley.

## Key Events Sequence
1. **Powell's Departure:** Powell leaves on March 3, 1866 with burros and provisions; Carter holds claim against prospectors
2. **Discovery of Threat:** Carter notices three dots appearing where Powell's trail was last seen; initially dismisses as antelope/horses but growing unease
3. **Chase Begins:** Armed with two Colt revolvers, carbine, cartridge belts; follows Powell's morning trail down mountainside
4. **Apache Tracks Found:** At dusk discovers unshod pony tracks joining Powell's trail; ponies had been galloping
5. **Water Hole Empty:** Reaches expected campsite at midnight; entirely deserted with no recent occupation signs
6. **Shots Heard:** Faint report of two shots far ahead; Carter urges horse to topmost speed up mountain trail
7. **Apache Camp Revealed:** Trail debouches onto open plateau near summit pass; discovers half a thousand red warriors clustered around object at camp center
8. **Powell's Death:** Under Arizona moonlight, Powell's body bristling with hostile arrows; confirmed dead
9. **Carter Charges:** Single-handedly charges entire warrior army shooting rapidly and whooping; Apaches flee in terror
10. **Escape Route:** Pulls Powell's body across saddle; pursued by Indians but reaches shadows of surrounding peaks
11. **Wrong Trail:** Horse enters defile leading to range summit instead of pass to valley; this mistake saves his life
12. **Cave Discovery:** Follows excellent trail around high cliff face; reaches mouth of large cave (four feet height, three to four feet wide)
13. **Powell Confirmed Dead:** Morning arrives; painstaking examination reveals no spark of life despite water forced between lips and continuous resuscitation efforts
14. **Cave Reconnaissance:** Enters cave to examine; finds large chamber possibly hundred feet diameter, thirty or forty feet height; smooth well-worn floor with evidence of remote habitation
15. **Chapter Ending State:** Carter feels pleasant drowsiness from fatigue and excitement; resists collapsing on cave floor due to Apache threat; reels drunkenly against side wall then slips prone upon cave floor

## Visual Continuity Facts
- Arizona landscape: clear beautiful mornings, sharp dawn without warning, rocky terrain with hog backs and plateaus
- Cave interior: large chamber with smooth well-worn floor, back lost in dense shadow
- Lighting conditions: Arizona moonlight throughout chase sequence; morning daylight at cave entrance
- Character positioning: Carter alone holding Powell's body on saddle; eventually collapses inside cave

## Character State at Chapter End
Carter physically exhausted from long strenuous ride and fight/pursuit excitement. Mentally resolved to write chronicle of interesting periods of life and death. Currently unconscious or semi-conscious on cave floor, unaware that this location will become his undiscovered resting place for ten years.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|------------------------------|
| john_carter | John Carter | Captain John Carter | Yes | Yes |
| powell | Powell | Friend of Carter | Yes | Yes |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Captain John Carter
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided in source material for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# john_carter.md

## Display Name
John Carter

## Chapter Role
Protagonist, survivor of Arizona cave entry sequence

## Physical Presence
Physically present throughout chapter; alone after friend Powell's departure

## Physical Description
No physical description available in source material. Character is armed with two Colt revolvers, carbine, and cartridge belts.

## Costume & Silhouette
Military-style attire implied by weapon configuration (Colt revolvers, carbine). No specific costume details provided.

## Continuity-Critical Traits
- Holds Powell's body on saddle during escape sequence
- Eventually collapses inside cave from exhaustion
- Single-handedly charges warrior army shooting rapidly and whooping
- Pursued by Indians but reaches shadows of surrounding peaks

## Render-Facing Prompt Notes
Character is physically exhausted from long strenuous ride and fight/pursuit excitement. Mentally resolved to write chronicle of interesting periods of life and death. Currently unconscious or semi-conscious on cave floor.

## Uncertainty Notes
Physical appearance, facial features, hair color, eye color, height, weight, and age are not specified in source material. Any visual representation will require manual description specification for accurate rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: powell
canonical_character_id: Powell
aliases: Friend of Carter
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided in source material for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# powell.md

## Display Name
Powell

## Chapter Role
Deceased companion of John Carter

## Physical Presence
Physically present as deceased body found in cave; referenced throughout chapter

## Physical Description
No physical description available in source material. Body is confirmed dead with no spark of life despite water forced between lips and continuous resuscitation efforts.

## Costume & Silhouette
Body bristling with hostile arrows from Apache attack. No specific clothing or uniform details provided.

## Continuity-Critical Traits
- Friend who departed toward valley on March 3, 1866 with burros and provisions
- Trail last seen where three dots appeared; initially dismissed as antelope/horses but growing unease
- Found dead under Arizona moonlight after Apache attack
- Body pulled across saddle during escape sequence
- Confirmed dead by morning examination in cave

## Render-Facing Prompt Notes
Character is deceased, body bristling with hostile arrows. Found in large cave chamber possibly hundred feet diameter, thirty or forty feet height. Morning daylight at cave entrance.

## Uncertainty Notes
Physical appearance, facial features, hair color, eye color, height, weight, and age are not specified in source material. Any visual representation will require manual description specification for accurate rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
