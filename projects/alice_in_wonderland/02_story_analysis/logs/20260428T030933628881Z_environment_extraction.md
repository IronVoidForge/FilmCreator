# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:09:33.628881+00:00
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

**Location: Mushroom Clearing / Forest Canopy / Small House Clearing**

**Characters:**
* **Alice:** A young girl experiencing rapid size fluctuations; currently struggling with identity and physical control.
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom; prone to sternness and contempt.
* **Pigeon:** An agitated bird living in a tree; perceives Alice as a serpent due to her elongated neck.

**Events & Scene Beats:**
1.  **The Confrontation:** Alice meets the Caterpillar on a mushroom. The Caterpillar questions Alice's identity ("Who are you?"). Alice explains her confusion regarding her frequent size changes.
2.  **The Poem Test:** To test Alice's memory, the Caterpillar commands her to recite "You are old, Father William." Alice recites it, but the Caterpillar declares it "wrong from beginning to end," creating a moment of tense silence.
3.  **Size Negotiation:** The Caterpillar asks what size Alice wants to be. Alice requests to be slightly larger than three inches. The Caterpillar (who is exactly three inches high) reacts angrily to being called small.
4.  **The Mushroom Instruction:** The Caterpillar crawls away into the grass, leaving Alice with a cryptic instruction: one side of the mushroom makes you grow taller, the other shorter.
5.  **First Transformation (Shrinking):** Alice breaks off a piece of the right-hand side of the round mushroom and eats it. She immediately experiences a violent physical reaction as she shrinks so rapidly that her chin strikes her foot.
6.  **Second Transformation (Elongation):** Desperate, Alice eats a morsel of the left-hand bit. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck rising above a canopy of green leaves (tree tops).
7.  **The Pigeon Encounter:** While Alice attempts to maneuver her flexible, zigzagging neck through the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!" 
8.  **Identity Dispute:** A dialogue ensues between the Pigeon and Alice. The Pigeon is convinced Alice is a serpent because of her neck; Alice insists she is a little girl. The Pigeon remains skeptical but eventually settles back into its nest.
9.  **Restoration:** Alice, still holding the mushroom pieces, nibbles alternating sides to stabilize her size. She successfully returns to her "usual" height.
10. **The Small House Discovery:** Alice discovers an open clearing containing a small house (approx. four feet high). 
11. **Final Transformation (Miniaturization):** To avoid frightening the inhabitants of the house, Alice nibbles the right-hand bit of the mushroom again, shrinking herself down to nine inches in height before approaching.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [mushroom_clearing](mushroom_clearing)
- [forest_canopy](forest_canopy)
- [small_house_clearing](small_house_clearing)
[[/SECTION]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: mushroom_clearing
[[SECTION markdown]]
# Mushroom Clearing

**Role:** Primary setting

**Architecture or Geography:**
A clearing dominated by large, oversized mushrooms. The ground is covered in thick grass and organic debris. One central mushroom serves as a platform for the Caterpillar.

**Lighting and Atmosphere Cues:**
Dappled sunlight filtering through unseen foliage; whimsical but slightly tense atmosphere; earthy tones with vibrant fungal colors.

**Scale Cues and Recurring Environmental Anchors:**
The scale is highly variable due to Alice's size fluctuations. The mushroom serves as a primary anchor, acting as both a platform and a tool for physical transformation.

**Descriptive Noun Phrases:**
Oversized fungi, thick grass blades, fungal platforms, dappled forest floor, organic textures, giant toadstool.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: forest_canopy
[[SECTION markdown]]
# Forest Canopy

**Role:** Secondary / Transit setting

**Architecture or Geography:**
A dense layer of green leaves and interlocking branches. It is a vertical space characterized by thick foliage and nesting sites.

**Lighting and Atmosphere Cues:**
High-contrast lighting; bright sunlight breaking through leaf gaps; claustrophobic greenery; sense of height and vertigo.

**Scale Cues and Recurring Environmental Anchors:**
The canopy becomes the primary environment when Alice's neck elongates, creating a sense of being trapped within a leafy labyrinth.

**Descriptive Noun Phrases:**
Dense green foliage, interlocking branches, leaf canopy, bird nests, verdant thicket, zigzagging neck path.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: small_house_clearing
[[SECTION markdown]]
# Small House Clearing

**Role:** Secondary setting

**Architecture or Geography:**
An open clearing containing a miniature house, approximately four feet in height. The architecture is scaled down to a domestic, diminutive level.

**Lighting and Atmosphere Cues:**
Open, bright lighting; sense of discovery; quiet and domestic atmosphere compared to the forest.

**Scale Cues and Recurring Environmental Anchors:**
The small house acts as the scale anchor for Alice's miniaturization (nine inches). The clearing provides a transition from the wild forest to a structured, albeit tiny, environment.

**Descriptive Noun Phrases:**
Miniature cottage, four-foot house, open woodland clearing, diminutive architecture, small-scale domesticity.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
