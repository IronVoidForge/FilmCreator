# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:45:58.850325+00:00
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

Chapter id: CH028

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

The narrator awakens in an Arizona cave after ten years on Mars, finding strange garments that disintegrate upon rising and artifacts including matches and green powder. Inside, he discovers a mummified woman and hanging skeletons before exiting to realize he is back on Earth. He reflects on his wealth from an old mine but expresses deep longing for Dejah Thoris and the fate of Helium. The chapter concludes with a vision of her waiting in the garden on Mars, suggesting a reunion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH028

## Visible Characters

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Description |
|----------|----------------------|---------|------------------|-------------|
| protagonist | CH002 Protagonist | Narrator, Conscious Entity | false | Awakens in Arizona cave after 10 years on Mars |
| mummified_woman | CH003 Mummified Woman | - | true | Discovered inside cave as mummified woman |
| hanging_skeletons | CH004 Hanging Skeletons | - | true | Artifacts found hanging in cave |
| dejah_thoris | CH001 Dejah Thoris | Helium's beloved, Garden Vision | false | Referenced in longing and vision |

## Character Records

- [[FILMCREATOR_RECORD]] (Protagonist)
- [[FILMCREATOR_RECORD]] (Mummified Woman)
- [[FILMCREATOR_RECORD]] (Hanging Skeletons)
- [[FILMCREATOR_RECORD]] (Dejah Thoris)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter text.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Protagonist

**Chapter Role:** Narrator/Conscious Entity  
**Physical Presence:** Referenced only (awakens in cave)  
**Description:** Male consciousness after 10 years on Mars, now back on Earth. Wealth from old mine. Longs for Dejah Thoris and Helium.  
**Uncertainty Notes:** Physical form not described in chapter text. Origin unclear beyond Mars/Earth transition.  
**Continuity Traits:** Wears strange garments that disintegrate upon rising.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: mummified_woman

canonical_character_id: CH003 Mummified Woman

aliases: -

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Mummified Woman

**Chapter Role:** Discovered Artifact  
**Physical Presence:** Referenced (found inside cave)  
**Description:** Mummified woman discovered inside Arizona cave. Hanging alongside skeletons as artifacts.  
**Continuity Traits:** Mummified state, found with matches and green powder artifacts.  
**Uncertainty Notes:** No further physical description provided in chapter text.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: hanging_skeletons

canonical_character_id: CH004 Hanging Skeletons

aliases: -

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Hanging Skeletons

**Chapter Role:** Cave Artifacts  
**Physical Presence:** Referenced (found hanging in cave)  
**Description:** Multiple skeletons discovered hanging inside Arizona cave alongside mummified woman.  
**Continuity Traits:** Found with matches and green powder artifacts. Part of strange garments collection.  
**Uncertainty Notes:** No individual skeleton descriptions provided in chapter text.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH001 Dejah Thoris

aliases: Helium's beloved, Garden Vision

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only referenced in vision/reflection, no physical description in chapter text.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is Dejah Thoris's physical form and appearance?

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Vision/Longing Object  
**Physical Presence:** Referenced only (in vision/reflection)  
**Description:** Beloved of Helium, waiting in garden on Mars. Subject of protagonist's deep longing.  
**Continuity Traits:** Garden setting on Mars, awaiting reunion with protagonist.  
**Uncertainty Notes:** Physical form not described in chapter text. Only known through reflection and vision.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: helium

canonical_character_id: CH005 Helium

aliases: -

is_fully_identified: false

manual_description_required: true

manual_description_reason: Referenced as place/city, no physical description in chapter text.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the visual representation of Helium city?

[[SECTION markdown]]

# Helium

**Chapter Role:** Setting Reference  
**Physical Presence:** Referenced only (city name)  
**Description:** City in Mars where protagonist spent 10 years and longs to return. Home of Dejah Thoris.  
**Continuity Traits:** Associated with old mine wealth, garden vision setting.  
**Uncertainty Notes:** No physical description provided in chapter text beyond city reference.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: arizona_cave

canonical_character_id: CH006 Arizona Cave

aliases: Awakening Location

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Arizona Cave

**Chapter Role:** Setting/Location  
**Physical Presence:** Referenced (awakening location)  
**Description:** Cave in Arizona where protagonist awakens after 10 years on Mars. Contains strange garments, matches, green powder, mummified woman, and hanging skeletons.  
**Continuity Traits:** Disintegration of garments upon rising, artifacts collection.  
**Uncertainty Notes:** No detailed physical description of cave interior provided in chapter text.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_powder

canonical_character_id: CH007 Green Powder

aliases: Artifact

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Green Powder

**Chapter Role:** Artifact  
**Physical Presence:** Referenced (found in cave)  
**Description:** Green powder artifact discovered inside Arizona cave alongside matches and strange garments.  
**Continuity Traits:** Part of mysterious collection found with protagonist's awakening.  
**Uncertainty Notes:** No detailed physical description provided in chapter text beyond color reference.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: matches

canonical_character_id: CH008 Matches

aliases: Artifact

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Matches

**Chapter Role:** Artifact  
**Physical Presence:** Referenced (found in cave)  
**Description:** Matches artifact discovered inside Arizona cave alongside green powder and strange garments.  
**Continuity Traits:** Part of mysterious collection found with protagonist's awakening.  
**Uncertainty Notes:** No detailed physical description provided in chapter text beyond object reference.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: strange_garments

canonical_character_id: CH009 Strange Garments

aliases: Disintegrating Clothes

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Strange Garments

**Chapter Role:** Artifact/Clothing  
**Physical Presence:** Referenced (found in cave, disintegrate upon rising)  
**Description:** Strange garments discovered inside Arizona cave that disintegrate when protagonist rises.  
**Continuity Traits:** Disintegration property, part of mysterious collection with matches and green powder.  
**Uncertainty Notes:** No detailed physical description provided in chapter text beyond disintegration behavior.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: garden_vision

canonical_character_id: CH010 Garden Vision

aliases: Dejah Thoris Waiting

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only referenced in vision, no physical description in chapter text.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the visual representation of Dejah Thoris waiting in garden?

[[SECTION markdown]]

# Garden Vision

**Chapter Role:** Vision/Ending Scene  
**Physical Presence:** Referenced only (in vision)  
**Description:** Vision of Dejah Thoris waiting in garden on Mars, suggesting reunion. Concludes chapter.  
**Continuity Traits:** Garden setting on Mars, awaiting protagonist's return from Arizona cave.  
**Uncertainty Notes:** Physical form not described in chapter text beyond vision reference.  

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: earth

canonical_character_id: CH011 Earth

aliases: -

is_fully_identified: true

manual_description_required: false

manual_description_reason: -

clarification_required: false

clarification_reason: -

clarification_question: -

[[SECTION markdown]]

# Earth

**Chapter Role:** Setting Reference  
**Physical Presence:** Referenced (protagonist realizes he is back on Earth)  
**Description:** Planet where protagonist awakens in Arizona cave after 10 years on Mars. Location of old mine wealth.  
**Continuity Traits:** Associated with Arizona cave, Dejah Thoris longing, Helium memory.  
**Uncertainty Notes:** No detailed physical description provided in chapter text beyond planet reference.  

[[/SECTION]]

[[FILMCREATOR_PACKET]]
````
