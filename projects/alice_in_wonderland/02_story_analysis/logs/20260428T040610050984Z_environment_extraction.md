# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:06:10.050984+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH005

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each environment item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION environment_index_markdown]] and [[SECTION markdown]] exactly as written

- do not echo this instruction block back as an example packet; return the actual packet only



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Location: Mushroom Clearing / Forest Canopy**

**Characters:**
* **Alice:** A young girl experiencing rapid physical instability (size changes, neck elongation).
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom.
* **Pigeon:** A frantic, nesting bird that mistakes Alice for a serpent.

**Events & Scene Beats:**
1.  **The Confrontation:** Alice and the Caterpillar engage in a philosophical argument regarding identity and size. The Caterpillar smokes a hookah and asks "Who are you?"
2.  **The Recitation:** To prove her memory is failing, Alice recites "You are old, Father William." The Caterpillar critiques her performance as being "wrong from beginning to end."
3.  **Size Negotiation:** The Caterpillar asks what size Alice wants to be. She requests to be slightly larger than three inches. The Caterpillar (who is exactly three inches high) reacts angrily to this suggestion.
4.  **The Departure:** The Caterpillar gets off the mushroom and crawls into the grass, providing a crucial instruction: one side of the mushroom makes you grow taller, the other shorter. He identifies the mushroom as the source before disappearing.
5.  **First Transformation (Shrinking):** Alice breaks off a piece of the right-hand side of the round mushroom and eats it. She immediately experiences a violent physical reaction where her chin strikes her foot, indicating she is shrinking rapidly.
6.  **Second Transformation (Elongation):** To counteract the shrinking, Alice eats a morsel from the left-hand side. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck rising above a sea of green leaves (the treetops).
7.  **The Pigeon Encounter:** While Alice attempts to navigate her long, flexible neck through the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!" 
8.  **The Argument:** A dialogue ensues where the Pigeon insists Alice is a serpent because of her neck; Alice insists she is a little girl. The Pigeon expresses exhaustion from guarding eggs against serpents.
9.  **Stabilization:** Alice crouches among the trees, untwisting her neck. She nibbles alternating pieces of the mushroom to regulate her height until she returns to her "usual" size.
10. **Discovery & Final Transformation:** Alice discovers a small house (four feet high) in an open clearing. To avoid frightening the inhabitants, she nibbles the right-hand bit of the mushroom again to shrink herself down to nine inches tall before approaching.

**Visual Continuity/Objects:**
* **The Mushroom:** A large, perfectly round object used as a platform and a tool for size manipulation.
* **Hookah:** Used by the Caterpillar.
* **Mushroom Fragments:** Alice holds pieces of both sides in her hands.
* **Physical State Shift:** Alice transitions from normal $\rightarrow$ tiny (chin to foot) $\rightarrow$ long-necked/serpent-like $\rightarrow$ normal $\rightarrow$ nine inches tall.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

## Mushroom Clearing
- [mushroom_clearing](mushroom_clearing)

## Forest Canopy
- [forest_canopy](forest_canopy)

## Small House Clearing
- [small_house_clearing](small_house_clearing)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: mushroom_clearing
[[SECTION markdown]]
# Mushroom Clearing

**Role:** Primary setting

**Architecture or Geography:**
A localized clearing dominated by a singular, massive, perfectly round mushroom. The mushroom serves as a platform and a central landmark within the immediate landscape.

**Lighting and Atmosphere Cues:**
Dappled light filtering through overhead foliage; mystical and surreal atmosphere; heavy with the presence of hookah smoke.

**Scale Cues and Recurring Environmental Anchors:**
The oversized, spherical mushroom acts as the primary scale anchor for character transformations. The ground level is characterized by tall grass where small creatures reside.

**Descriptive Noun Phrases:**
Giant fungal platform, perfectly round mushroom cap, hookah smoke plumes, dappled forest floor, surreal botanical clearing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: forest_canopy
[[SECTION markdown]]
# Forest Canopy

**Role:** Secondary / Transit setting

**Architecture or Geography:**
A dense, tangled layer of treetops and green leaves situated above the ground level. A labyrinthine network of branches and foliage.

**Lighting and Atmosphere Cues:**
Bright, filtered sunlight through thick greenery; chaotic and claustrophobic movement within the branches.

**Scale Cues and Recurring Environmental Anchors:**
The canopy represents a vast vertical space that becomes a restrictive cage when Alice's neck elongates. The leaves serve as a sea of green surrounding the character.

**Descriptive Noun Phrases:**
Dense leaf canopy, tangled treetops, verdant leafy labyrinth, avian nesting branches, high-altitude forest foliage.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: small_house_clearing
[[SECTION markdown]]
# Small House Clearing

**Role:** Secondary setting

**Architecture or Geography:**
An open clearing containing a small, low-profile house (approximately four feet in height). 

**Lighting and Atmosphere Cues:**
Open exposure; bright, clear lighting compared to the dense forest.

**Scale Cues and Recurring Environmental Anchors:**
The small scale of the architecture provides a new baseline for Alice's nine-inch stature. The house serves as a focal point for the transition out of the deep woods.

**Descriptive Noun Phrases:**
Diminutive cottage, low-profile woodland house, open forest clearing, miniature architectural structure.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
