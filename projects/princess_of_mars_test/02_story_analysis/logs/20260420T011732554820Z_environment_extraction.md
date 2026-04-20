# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:17:32.554820+00:00
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

Chapter id: CH014

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

*Scene 1: Introspection & Departure*
- **Visuals:** Carter sits cross-legged in his chamber (gold/marble mosaics), then moves to the plaza/chariots. Dejah Thoris is in a departing chariot, heavily chained by one ankle to the vehicle side.
- **Story:** Carter reflects on his love for Dejah Thoris and her rejection of him due to his perceived weakness or the situation. He observes her silence and refusal to acknowledge him.

*Scene 2: The Chains & Tars Tarkas*
- **Visuals:** Carter examines the manacles (massive spring lock). Tars Tarkas intervenes, agreeing to hold the key himself rather than Sarkoja.
- **Story:** Sarkoja's cruelty is highlighted by the chains. Tars Tarkas ensures security while allowing for potential escape later.

*Scene 3: Camp Life & Earth Memories*
- **Visuals:** Carter sits cross-legged on silks in camp, moonlit skies.
- **Story:** Carter meditates on love and mortality. He recalls his family in Virginia (Carters), feeling homesick despite being a wanderer.

*Scene 4: Warhoon Incubator Incident*
- **Visuals:** An incubator with small eggs found to the right of the march. Tars Tarkas investigates with warriors. Eggs are demolished.
- **Story:** Discovery of green men's (Warhoons) incubator. Carter asks about egg size differences; Tars Tarkas explains growth period.

*Scene 5: Duel with Zad*
- **Visuals:** Zad strikes Carter's animal with a long-sword. Carter draws his own sword. Community surrounds them, leaving a clear space (100 feet diameter). Long, straight, needle-like swords flash.
- **Story:** Fight initiated by Zar striking the animal. Carter chooses to fight with same weapon. Fight is long and delayed march.

*Scene 6: The Trap & Sacrifice*
- **Visuals:** Blinding flash of light strikes Carter's eyes (mirror). Dejah Thoris throws something from hand (tiny mirror) which spins to ground. Sarkoja aims dagger at Dejah Thoris; Sola sprang between them, knife descending on her shielding breast.
- **Story:** Sarkoja blinds Carter with a mirror while trying to kill him. Dejah Thoris throws the mirror. Sola sacrifices herself to protect Dejah Thoris from Sarkoja's counter-attack during the fight.

*Scene 7: Wounding & Collapse*
- **Visuals:** Carter feels sharp point of sword at breast, throws himself on enemy. Steel tears into chest. Head whirled, knees giving beneath.
- **Story:** Carter is wounded in the duel, collapsing as darkness takes him.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH014

## Primary Environments
- carter_chamber_gold_mosaic
- duel_arena_clear_space

## Secondary Environments  
- plaza_chariot_departure
- camp_silk_moonlit
- warhoon_incubator_zone

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: carter_chamber_gold_mosaic

[[SECTION markdown]]
**Environment Role:** Primary introspection setting

**Architecture/Geography:** Interior chamber with gold and marble mosaic flooring. Raised seating area for cross-legged meditation posture.

**Lighting/Atmosphere:** Warm ambient glow reflecting off polished surfaces. Intimate, contemplative mood during Carter's reflection scenes.

**Scale Cues:** Personal space for solitary meditation. Chamber walls frame the character's emotional journey.

**Recurring Anchors:** Mosaic floor patterns, chamber boundaries, seating platform.

**Descriptive Noun Phrases:** gold marble mosaic chamber, introspection space, polished interior surfaces, contemplative room setting.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_chariot_departure

[[SECTION markdown]]
**Environment Role:** Secondary transit/departure setting

**Architecture/Geography:** Open plaza area with chariot vehicles. Elevated platform for Dejah Thoris's departure scene.

**Lighting/Atmosphere:** Bright daylight illumination. Tense atmosphere during rejection and departure sequence.

**Scale Cues:** Large open space accommodating multiple chariots and observers. Public viewing area.

**Recurring Anchors:** Chariot vehicles, plaza boundaries, departure platform edge.

**Descriptive Noun Phrases:** open plaza ground, chariot vehicle platforms, public viewing area, daylight outdoor setting.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: camp_silk_moonlit

[[SECTION markdown]]
**Environment Role:** Secondary meditation/transit setting

**Architecture/Geography:** Camp ground with silk textiles for seating. Open-air arrangement under night sky.

**Lighting/Atmosphere:** Moonlight illumination creating soft shadows. Serene, reflective nighttime atmosphere.

**Scale Cues:** Medium camp space accommodating multiple characters. Ground-level silk seating areas.

**Recurring Anchors:** Silk textile platforms, moonlit sky overhead, camp perimeter markers.

**Descriptive Noun Phrases:** moonlit camp ground, silk textile seating, open-air night setting, reflective meditation space.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: warhoon_incubator_zone

[[SECTION markdown]]
**Environment Role:** Secondary investigation setting

**Architecture/Geography:** Incubator structure with egg storage area. March route adjacent to incubation facility.

**Lighting/Atmosphere:** Dim interior lighting within incubator. Tense investigative atmosphere during discovery scene.

**Scale Cues:** Small enclosed incubator space. Adjacent march pathway for warrior movement.

**Recurring Anchors:** Incubator structure, egg storage compartments, march route boundaries.

**Descriptive Noun Phrases:** green men incubator facility, egg storage area, investigation zone, march adjacent structure.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: duel_arena_clear_space

[[SECTION markdown]]
**Environment Role:** Primary combat setting

**Architecture/Geography:** Open arena with 100-foot diameter clear space. Community surrounding perimeter leaving central fighting area.

**Lighting/Atmosphere:** Bright daylight illumination. Intense combat atmosphere during sword fight sequence.

**Scale Cues:** Large circular clearing for duel action. Peripheral community boundary markers.

**Recurring Anchors:** Central 100-foot circle, peripheral community edge, sword flash points.

**Descriptive Noun Phrases:** hundred foot diameter arena, central fighting circle, community surrounding space, daylight combat zone.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
