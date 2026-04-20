# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:19:04.616871+00:00
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

Chapter id: CH015

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

# Chapter Summary: CH015 - Sola Tells Me Her Story

## Opening Scene & Physical Recovery
- **Carter's Condition:** Consciousness returns; finds sword buried in green breast of Zad (stone dead). Wound is not dangerous due to Martian anatomy (blade passed beneath muscles).
- **Action:** Removes blade, moves toward chariots. Bleeding and weak, reaches women who dress wounds using instant healing agents.
- **Arrival at Dejah's Chariot:** Finds Sola with chest swathed in bandages (encounter with Sarkoja deflected by metal ornament). Dejah Thoris lies prone on silks/furs wracked with sobs.

## Dialogue & Emotional Beats
- **Dejah's Grief:** Sola explains Dejah thinks Carter is dead; her pride prevents admitting his existence while she mourns him as if he died.
- **Sola's Offer:** Invites Carter to hear her strange story tonight at the chariot before resuming march.
- **Carter's Promise:** Agrees to visit tonight, instructs Sola not to let Dejah know he saw her tears.

## Visual Continuity: The March
- **Caravan Spectacle:** 250 chariots, advance guard riding five abreast, flankers, 50 zitidars, loose thoats. Gleaming metal/jewels/silks create barbaric splendor.
- **Movement:** No sound from moss-covered sea bottom; silence broken only by goaded zitidars or fighting thoats. Green Martians converse in low rumbling monosyllables.
- **Environment:** Traverses trackless waste of moss; leaves no sign of passage (no dust/spoor).

## Camp & Storytelling Setup
- **Location:** Camped at foot of hills marking southern boundary of sea. Animals two days without drink but survive on moss moisture.
- **Evening:** Carter eats cheese-like food/vegetable milk, seeks out Sola working by torchlight on Tars Tarkas' trappings.
- **Sola's Loneliness:** Expresses isolation among her own people; wishes to be a true green Martian woman without love/hope but is lost due to knowing love.

## The Origin Story (Narrative Core)
- **Mother's Background:** Small, less cruel than most Thark women; roamed deserted avenues of Thark alone. Met young warrior guarding zitidars/thoats.
- **The Affair:** Secret love affair for six years; mother belonged to retinue of Tal Hajus, lover was simple warrior. Defection would mean penalty in arena.
- **Incubation:** Egg hidden beneath glass vessel on highest tower of ancient Thark. Mother visited annually for five years during incubation.
- **Father's Rise:** Lover gained distinction as warrior; planned to wrest metal from Tal Hajus to claim mother and protect child.
- **Expedition & Tragedy:** Father ordered away to ice-clad south for four years. Egg hatched while he was gone. Mother kept Sola in tower, visited nightly.
- **Sarkoja's Discovery:** Sarkoja appears at tower with loathing; demands name of partner. Mother lies and says she knows nothing to save Sola.
- **Escape & Death:** Mother wraps Sola in silks/furs, runs to outskirts towards father. Meets returning caravan (not father). Mother hides on tailboard, mixes Sola with other children.
- **Mother's Fate:** Imprisoned by Tal Hajus; tortured for name of father; dies steadfastly. Claims she killed Sola and threw body to white apes. Sarkoja suspects truth but fears exposure.
- **Father's Return:** Father returns from expedition, learns story of mother's death from Tal Hajus. Does not laugh at description; becomes cruellest of cruel.

## Conclusion & Name Reveal
- **Carter's Question:** Asks if father is with them now.
- **Sola's Answer:** Yes, but he does not know her true origin or who betrayed mother. Only she knows father's name.
- **Final Revelation:** Sola reveals father's name is **Tars Tarkas**. Trusts Carter to speak truth when time comes.

## Key Continuity Notes
- **Sola's Chest:** Swathed in bandages from Sarkoja's encounter (dagger deflected by metal ornament).
- **Dejah Thoris:** Prone on silks/furs, sobbing, believes Carter dead.
- **Tars Tarkas:** Present at rear of column with Carter; leader of Tharks; father of Sola.
- **Tal Hajus:** Chieftain responsible for mother's death; object of vengeance.
- **Sarkoja:** Antagonist who knows Sola's origin but fears exposure.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH015

| Character | Role | Status | Description Available |
|-----------|------|--------|----------------------|
| Carter | Protagonist, recovering consciousness | Present | Partial |
| Zad | Stone dead (green breast) | Referenced | None |
| Dejah Thoris | Prone on silks/furs, sobbing | Present | Limited |
| Sola | Swathed in bandages, storyteller | Present | Partial |
| Sarkoja | Antagonist, knows origin | Referenced | Limited |
| Tal Hajus | Chieftain, responsible for mother's death | Referenced | None |
| Tars Tarkas | Leader of Tharks, father of Sola | Present | Limited |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: Carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter - CH015

## Display Name & Chapter Role
**Carter** - Protagonist recovering consciousness after sword wound

## Physical Presence
Present in scene, conscious and moving toward chariots

## Physical Description (Supported by Source)
- Consciousness returns to find sword buried in green breast of Zad
- Wound not dangerous due to Martian anatomy (blade passed beneath muscles)
- Bleeding and weak when reaching women who dress wounds
- Uses instant healing agents for wound treatment

## Costume, Silhouette & Continuity Traits
- No specific costume details provided in chapter
- Moving toward chariots with bleeding wound
- Weak but functional enough to reach Dejah's chariot

## Render-Facing Prompt Noun Phrases
- Martian anatomy conscious protagonist
- Sword wound beneath muscles
- Bleeding weak figure approaching chariots
- Instant healing agent treated injury

## Uncertainty Notes
Limited costume and silhouette details available for complete image generation. Physical description focuses on wound state rather than full appearance.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: Zad
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only referenced as "green breast of Zad (stone dead)" with no physical description provided in chapter material. Cannot support dependable image generation without additional visual details.

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Zad - CH015

## Display Name & Chapter Role
**Zad** - Stone dead figure (green breast)

## Physical Presence
Referenced only, not physically present in scene

## Physical Description (Supported by Source)
- Described as "stone dead" with green breast
- No additional physical details provided in chapter material

## Costume, Silhouette & Continuity Traits
- No costume or silhouette information available
- Stone dead status indicates non-living figure

## Render-Facing Prompt Noun Phrases
- Green breast stone dead figure
- Zad referenced as deceased entity

## Uncertainty Notes
CRITICAL: No physical description provided in source material. Cannot generate dependable images without additional visual details beyond "stone dead" designation. Chapter only references this character with minimal information.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by chapter context (prone on silks/furs, sobbing)

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - CH015

## Display Name & Chapter Role
**Dejah Thoris** - Prone on silks/furs, sobbing from grief

## Physical Presence
Present in scene, lying prone on chariot

## Physical Description (Supported by Source)
- Lies prone on silks/furs wracked with sobs
- Believes Carter is dead
- Grief prevents admitting his existence while mourning him as if he died

## Costume, Silhouette & Continuity Traits
- Positioned on silks/furs in chariot
- Sobbing indicates emotional state visible to observers
- Metal ornament deflects Sarkoja's attack (chest swathed in bandages)

## Render-Facing Prompt Noun Phrases
- Prone figure on silks and furs
- Sobbing grief-stricken woman
- Bandaged chest from Sarkoja encounter
- Chariot interior prone position

## Uncertainty Notes
Limited physical description beyond emotional state and positioning. Costume details not fully specified in chapter material.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description supported by chapter context (swathed in bandages, working by torchlight)

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - CH015

## Display Name & Chapter Role
**Sola** - Swathed in bandages, storyteller, expresses loneliness

## Physical Presence
Present in scene, working by torchlight on Tars Tarkas' trappings

## Physical Description (Supported by Source)
- Chest swathed in bandages from Sarkoja's encounter (dagger deflected by metal ornament)
- Working by torchlight on Tars Tarkas' trappings
- Expresses isolation among her own people
- Wishes to be true green Martian woman without love/hope but is lost due to knowing love

## Costume, Silhouette & Continuity Traits
- Bandaged chest from Sarkoja encounter
- Working on metal/jewels/silks (barbaric splendor context)
- Positioned at foot of hills marking southern boundary of sea

## Render-Facing Prompt Noun Phrases
- Green Martian woman with bandaged chest
- Working by torchlight on trappings
- Bandages from Sarkoja encounter deflected dagger
- Expressing loneliness among own people

## Uncertainty Notes
Physical description focuses on injury (bandaged chest) rather than full appearance. Limited costume details beyond bandaging context.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only referenced as antagonist who knows Sola's origin with no physical description provided in chapter material. Cannot support dependable image generation without additional visual details.

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja - CH015

## Display Name & Chapter Role
**Sarkoja** - Antagonist who knows Sola's origin, fears exposure

## Physical Presence
Referenced in context of mother's encounter, not physically present in current scene

## Physical Description (Supported by Source)
- Appears at tower with loathing
- Demands name of partner from mother
- Knows Sola's origin but fears exposure
- Imprisoned by Tal Hajus; tortured for name of father
- Suspects truth about mother's fate but fears exposure

## Costume, Silhouette & Continuity Traits
- No specific costume or silhouette information available
- Antagonist role indicates threatening presence
- Metal ornament deflects her attack (indicates weapon use)

## Render-Facing Prompt Noun Phrases
- Antagonist antagonist figure
- Knows Sola's origin truth
- Fears exposure of knowledge
- Appears with loathing at tower

## Uncertainty Notes
CRITICAL: No physical description provided in source material. Only referenced as antagonist with no visual details beyond role context. Cannot generate dependable images without additional visual information.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only referenced as chieftain responsible for mother's death with no physical description provided in chapter material. Cannot support dependable image generation without additional visual details.

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus - CH015

## Display Name & Chapter Role
**Tal Hajus** - Chieftain responsible for mother's death, object of vengeance

## Physical Presence
Referenced in context of mother's story, not physically present in current scene

## Physical Description (Supported by Source)
- Chieftain responsible for mother's death
- Object of vengeance for Carter and Sola
- Imprisoned mother after escape attempt
- Tortured for name of father
- Does not laugh at description of mother's death; becomes cruellest of cruel

## Costume, Silhouette & Continuity Traits
- No specific costume or silhouette information available
- Chieftain status indicates leadership role
- Cruel nature indicated through actions and reactions

## Render-Facing Prompt Noun Phrases
- Thark chieftain antagonist figure
- Responsible for mother's death
- Object of vengeance target
- Becomes cruellest of cruel after story

## Uncertainty Notes
CRITICAL: No physical description provided in source material. Only referenced as chieftain with no visual details beyond role context and actions. Cannot generate dependable images without additional visual information.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only referenced as leader of Tharks and father of Sola with no physical description provided in chapter material. Cannot support dependable image generation without additional visual details.

clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - CH015

## Display Name & Chapter Role
**Tars Tarkas** - Leader of Tharks, father of Sola, present at rear of column

## Physical Presence
Present in scene at rear of column with Carter

## Physical Description (Supported by Source)
- Present at rear of column with Carter
- Leader of Tharks
- Father of Sola
- Learns story of mother's death from Tal Hajus
- Does not laugh at description; becomes cruellest of cruel

## Costume, Silhouette & Continuity Traits
- No specific costume or silhouette information available
- Positioned at rear of column
- Working on Tars Tarkas' trappings (Sola working by torchlight)

## Render-Facing Prompt Noun Phrases
- Thark leader figure
- Father of Sola
- Present at rear of column
- Learns mother's death story from Tal Hajus

## Uncertainty Notes
CRITICAL: No physical description provided in source material. Only referenced as leader and father with no visual details beyond role context. Cannot generate dependable images without additional visual information.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
