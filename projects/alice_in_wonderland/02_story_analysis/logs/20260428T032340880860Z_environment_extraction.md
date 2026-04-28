# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:23:40.880860+00:00
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
* **Alice:** A young girl experiencing rapid size fluctuations and identity crises.
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom; prone to irritability and philosophical questioning.
* **Pigeon:** A frantic, nesting bird that mistakes Alice for a serpent.

**Events & Scene Breakdown:**
1.  **The Confrontation on the Mushroom:** Alice encounters the Caterpillar sitting on a large mushroom. The Caterpillar smokes a hookah and interrogates Alice regarding her identity ("Who are you?"). 
2.  **The Recitation:** After a tense exchange about Alice's changing size, the Caterpillar demands she recite "You are old, Father William." Alice performs the poem, but the Caterpillar critiques her for getting the words wrong.
3.  **Size Negotiation:** The Caterpillar asks Alice what size she wants to be. Alice requests to be slightly larger than three inches. The Caterpillar becomes angry at this request (noting it is exactly three inches high) before returning to his hookah.
4.  **The Departure & Instruction:** The Caterpillar gets off the mushroom and crawls away into the grass. Before disappearing, he reveals a crucial mechanic: one side of the mushroom makes you grow taller, and the other side makes you grow shorter.
5.  **First Transformation (Shrinking):** Alice attempts to test the mushroom. She breaks off a piece from the right-hand side and eats it. Immediately, she experiences a violent physical sensation as her chin strikes her foot; she begins shrinking rapidly.
6.  **Second Transformation (Elongation):** To counteract the shrinking, Alice hurriedly eats a morsel from the left-hand side. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck that rises above the forest canopy (the "green leaves").
7.  **The Pigeon Encounter:** While Alice struggles to maneuver her long, flexible neck through the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!" 
8.  **Identity Argument:** A dialogue ensues between the panicked Pigeon and the indignant Alice. The Pigeon insists she is a serpent because of her neck; Alice insists she is a little girl. The Pigeon remains unconvinced but eventually settles back into its nest.
9.  **Restoring Normalcy:** Alice, crouching among the trees to untangle her neck, nibbles alternating pieces of the mushroom until she successfully returns to her usual height.
10. **Discovery of the House:** Having regained her size, Alice discovers an open clearing containing a small house (approx. four feet high). 
11. **Final Transformation (Miniaturization):** To avoid frightening the inhabitants of the house, Alice nibbles on the right-hand bit of the mushroom again, successfully shrinking herself down to nine inches in height before approaching.
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
A clearing dominated by oversized, fantastical fungi. A central large mushroom serves as a platform for characters. The ground is covered in thick grass and forest floor debris.

**Lighting and Atmosphere Cues:** 
Dappled sunlight filtering through high foliage; whimsical yet slightly surreal atmosphere; heavy with the scent of hookah smoke.

**Scale Cues and Recurring Environmental Anchors:** 
The mushroom acts as a scale reference for Alice's size fluctuations. The height of the grass relative to Alice changes based on her consumption of the mushroom pieces.

**Descriptive Noun Phrases:** 
Oversized fungal platforms, thick forest floor grass, hookah smoke plumes, dappled woodland light, giant mushroom cap.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: forest_canopy
[[SECTION markdown]]
# Forest Canopy

**Role:** Secondary / Transit setting

**Architecture or Geography:** 
A dense layer of green leaves and interlocking branches high above the ground. A complex network of twigs and foliage.

**Lighting and Atmosphere Cues:** 
Bright, filtered light; airy but claustrophobic when navigating through it; sense of verticality.

**Scale Cues and Recurring Environmental Anchors:** 
The canopy serves as a boundary for Alice's elongated neck; the scale shifts from being "above" to "within" the leaves depending on her height.

**Descriptive Noun Phrases:** 
Interlocking green leaves, dense branch network, high forest ceiling, sun-drenched foliage, vertical woodland expanse.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: small_house_clearing
[[SECTION markdown]]
# Small House Clearing

**Role:** Secondary setting

**Architecture or Geography:** 
An open clearing containing a diminutive structure, approximately four feet in height.

**Lighting and Atmosphere Cues:** 
Open, bright lighting; sense of discovery and transition from the dense forest to a more structured space.

**Scale Cues and Recurring Environmental Anchors:** 
The small house serves as the primary scale anchor for Alice's miniaturization (nine inches tall).

**Descriptive Noun Phrases:** 
Diminutive cottage, miniature woodland dwelling, open forest clearing, low-profile architecture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
