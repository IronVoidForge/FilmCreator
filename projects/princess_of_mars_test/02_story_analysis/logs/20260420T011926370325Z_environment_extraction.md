# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:19:26.370325+00:00
- task: environment_extraction

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

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



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
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH015

## Primary Environments

| Asset ID | Environment Name | Role | Location |
|----------|------------------|------|----------|
| dejah_chariot | Dejah's Chariot | Primary Setting | Caravan Column |
| march_trackless_waste | March Trackless Waste | Transit Setting | Moss-Covered Sea Bottom |
| camp_foot_of_hills | Camp Foot of Hills | Secondary Setting | Southern Boundary of Sea |
| ancient_thark_tower | Ancient Thark Tower | Narrative Setting | Highest Tower of Ancient Thark |

## Environment Summary

This chapter features four distinct environments: the chariot where Carter arrives after removing the blade, the moss-covered march track traversing the sea bottom, the camp at the foot of hills for evening storytelling, and the ancient Thark tower referenced in Sola's origin story. Each environment supports different narrative functions from physical recovery to emotional revelation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dejah_chariot

[[SECTION markdown]]
# Dejah's Chariot - Primary Setting

## Environment Role
Primary setting where Carter arrives after removing the blade from his chest; location of immediate physical recovery and emotional confrontation with Dejah Thoris.

## Architecture/Geography
Chariot interior lined with silks and furs; prone surface for Dejah Thoris wrapped in bandages; metal ornament deflecting Sarkoja's dagger; torchlight working area for Sola on Tars Tarkas' trappings.

## Lighting/Atmosphere Cues
Torchlight illumination creating intimate evening atmosphere; green Martian presence suggested through low rumbling monosyllables; silence broken only by goaded zitidars or fighting thoats; bandaged chest swathed in white fabric contrasting with dark interior.

## Scale Cues and Environmental Anchors
Chariot interior sized for two women plus wounded man; metal ornament serving as protective anchor point; silks/furs providing soft surface texture; bandages indicating recent injury severity.

## Descriptive Noun Phrases
- Swathed chest in white bandages
- Silks and furs wracked with sobs
- Metal ornament deflecting dagger
- Torchlight working area
- Prone position on interior surface
- Bandaged wound not dangerous due to Martian anatomy
- Green breast of Zad stone dead reference

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: march_trackless_waste

[[SECTION markdown]]
# March Trackless Waste - Transit Setting

## Environment Role
Transit setting traversed by 250 chariots during advance; trackless waste of moss where no sign of passage remains; movement through southern boundary of sea.

## Architecture/Geography
Trackless waste of moss covering sea bottom; no dust or spoor left behind; moss-covered surface creating silent movement; green Martian conversational space with low rumbling monosyllables; five abreast riding formation for advance guard.

## Lighting/Atmosphere Cues
Natural daylight filtering through trackless landscape; gleaming metal/jewels/silks creating barbaric splendor against moss background; silence as primary atmospheric quality broken only by animal sounds; green Martians conversing in low rumbling monosyllables.

## Scale Cues and Environmental Anchors
250 chariots forming massive caravan spectacle; 50 zitidars integrated into formation; loose thoats providing additional movement; moss surface serving as primary ground texture; southern boundary of sea marking environmental limit.

## Descriptive Noun Phrases
- Trackless waste of moss
- No dust or spoor left behind
- Gleaming metal jewels silks barbaric splendor
- Five abreast riding formation
- Goaded zitidars breaking silence
- Fighting thoats providing sound
- Green Martians conversing low rumbling monosyllables
- Moss-covered sea bottom

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: camp_foot_of_hills

[[SECTION markdown]]
# Camp Foot of Hills - Secondary Setting

## Environment Role
Secondary setting for evening storytelling and origin story revelation; location where animals survive two days without drink using moss moisture; foot of hills marking southern boundary of sea.

## Architecture/Geography
Camp established at foot of hills; trackless waste surrounding camp area; moss-covered ground providing survival moisture source; torchlight working area for Sola on Tars Tarkas' trappings; cheese-like food and vegetable milk consumption location.

## Lighting/Atmosphere Cues
Evening torchlight creating intimate storytelling atmosphere; low rumbling monosyllables from green Martians in background; moss moisture survival creating atmospheric tension; isolation among own people suggested through lighting quality.

## Scale Cues and Environmental Anchors
Camp sized for caravan column overnight stay; hills marking southern boundary serving as environmental anchor; Tars Tarkas' trappings providing scale reference; torchlight working area defining Sola's isolation space.

## Descriptive Noun Phrases
- Foot of hills marking southern boundary
- Two days without drink survival
- Moss moisture source for animals
- Torchlight working area
- Cheese-like food and vegetable milk
- Isolation among own people
- Tars Tarkas' trappings
- Evening storytelling location

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: ancient_thark_tower

[[SECTION markdown]]
# Ancient Thark Tower - Narrative Setting

## Environment Role
Narrative setting referenced in Sola's origin story; highest tower of ancient Thark where mother kept Sola during incubation and after hatching; location of mother's annual visits and nightly care.

## Architecture/Geography
Highest tower of ancient Thark with glass vessel on top; egg hidden beneath glass vessel for five years incubation period; tower interior providing protection from Tal Hajus arena penalty; outskirts accessible through silks/furs wrapping; tailboard hiding location for escape.

## Lighting/Atmosphere Cues
Tower interior suggesting isolation and protection; glass vessel catching light during annual visits; torchlight quality implied through mother's nightly care routine; loathing atmosphere suggested through Sarkoja's discovery; ancient Thark architecture indicating historical significance.

## Scale Cues and Environmental Anchors
Highest tower providing vertical environmental anchor; glass vessel serving as protective container for egg; silks/furs wrapping providing escape mechanism; tailboard of caravan serving as hiding place; ancient Thark structure indicating historical weight.

## Descriptive Noun Phrases
- Highest tower of ancient Thark
- Glass vessel on top
- Egg hidden beneath glass vessel
- Five years incubation period
- Annual mother visits
- Nightly care routine
- Silks and furs wrapping escape
- Tailboard hiding location
- Ancient Thark architecture

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
