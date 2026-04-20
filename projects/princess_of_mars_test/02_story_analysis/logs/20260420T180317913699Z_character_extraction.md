# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:03:17.913699+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH017

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- emit one explicit character record per meaningful character mention

- every character record must have a FILMCREATOR_RECORD wrapper with type character

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

The protagonist infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the jeddak, Tal Hajus. After witnessing the depraved threats made against the Princess, the protagonist intervenes, knocking Tal Hajus unconscious and successfully leading Dejah Thoris and Sola out of the city via a rear window. The group escapes on thoats, heading northeast across a two-hundred-mile mossy waste toward Helium, traveling without food or water in a state of extreme exhaustion.

As they traverse the trackless waste, the party becomes lost and realizes they have no visible waterways. During their trek, the protagonist discovers that his faithful hound, Woola, has followed them. The journey takes a toll as one of their thoats collapses from exhaustion; the group continues with only one beast, forcing Dejah Thoris to ride while the others walk. Their progress is interrupted when they spot a large party of several hundred mounted Thark warriors emerging from a mountain pass. 

After a chieftain spots them, the protagonist uses his Martian rifle to shoot the leader, creating a distraction. To ensure their survival, he commands Sola to take Dejah Thoris on the remaining thoat and flee toward the hills. Following an emotional embrace, the protagonist stays behind to hold off the advancing warriors. Despite continuous rifle fire, he eventually runs out of ammunition as nearly a thousand warriors charge him. While attempting to evade them with extraordinary leaps, he trips on a piece of quartz and is beaten into unconsciousness by the overwhelming Thark force.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Protagonist](#protagonist)
- [Dejah Thoris](#dejah-thoris)
- [Sola](#sola)
- [Tal Hajus](#tal-hajus)
- [Woola](#woola)
- [Thark Warriors](#thark-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, age, and specific clothing/armor are not described in this chapter.

clarification_required: true

clarification_reason: Identity and physical traits need to be established for visual consistency.

clarification_question: What is the protagonist's physical appearance, build, and specific outfit?

[[SECTION markdown]]

# Protagonist
**Role:** Hero / Infiltrator

**Status:** Physically Present

**Physical Description:** 
No specific physical features (hair, eyes, height) are provided in this text. He is capable of "extraordinary leaps."

**Costume/Silhouette:** 
Wears gear suitable for infiltration and combat; carries a Martian rifle.

**Descriptive Noun Phrases:** 
Martian rifleman, agile survivor, lone defender.

**Uncertainty Notes:** 
Visual identity is entirely missing from this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: Princess

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical features or clothing details provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess / Captured Noble

**Status:** Physically Present

**Physical Description:** 
No specific physical traits are mentioned in this chapter.

**Costume/Silhouette:** 
Unknown; she is being rescued from captivity.

**Descriptive Noun Phrases:** 
Martian princess, noblewoman, captive.

**Uncertainty Notes:** 
Visual details are absent; relies on her status as a royal figure.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Companion / Escort

**Status:** Physically Present

**Physical Description:** 
No specific physical traits are mentioned.

**Costume/Silhouette:** 
Unknown.

**Descriptive Noun Phrases:** 
Companion, escort, traveler.

**Uncertainty Notes:** 
Minimal character detail provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: CH005 Tal Hajus

aliases: Jeddak

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tal Hajus
**Role:** Antagonist / Jeddak

**Status:** Referenced/Present (briefly)

**Physical Description:** 
No specific physical traits are mentioned.

**Costume/Silhouette:** 
Likely royal or high-ranking Thark attire, though not specified.

**Descriptive Noun Phrases:** 
Thark jeddak, antagonist, ruler.

**Uncertainty Notes:** 
Character is defined by his role and actions rather than visual appearance.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH006 Woola

aliases: Faithful Hound

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Companion Animal

**Status:** Physically Present

**Physical Description:** 
A faithful Martian hound.

**Costume/Silhouette:** 
Animal silhouette; follows the party across the waste.

**Descriptive Noun Phrases:** 
Martian hound, loyal beast, tracker.

**Uncertainty Notes:** 
Specific breed or size is not detailed in this text, but identified as a "hound."
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_warriors

canonical_character_id: CH007 Thark Warriors

aliases: Mounted Thark, Thark Force

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Thark Warriors
**Role:** Antagonists / Combatants

**Status:** Physically Present

**Physical Description:** 
A large group (hundreds to nearly a thousand) of mounted warriors.

**Costume/Silhouette:** 
Mounted on beasts; appearing as a massed force from a mountain pass.

**Descriptive Noun Phrases:** 
Mounted Thark, warrior horde, Martian cavalry.

**Uncertainty Notes:** 
Individual features are not described, only the collective group.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
