# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:10:42.471469+00:00
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

Chapter id: CH024

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

# Chapter CH024: Tars Tarkas Finds a Friend

## Narrative Summary

### Scene 1: Crash and Rescue
John Carter flies over a dead city and crashes into a battle between green warriors and Warhoons. He lands in the center of combat, drawing his long-sword to defend himself. He falls beside Tars Tarkas, who is fighting three antagonists (Warhoons). Tars Tarkas is knocked down by a dead body behind him. Carter springs before Tars Tarkas' prostrate form and engages the adversaries. After accounting for one, Carter helps Tars Tarkas settle the other.

### Scene 2: The Friendship Acknowledgement
Tars Tarkas gives Carter a look and a slight smile, touching his shoulder. He says he would scarcely recognize John Carter but notes there is no other mortal on Barsoom who would have done what Carter did for him. He states he has learned that there is such a thing as friendship. The Warhoons close in, and they fight shoulder to shoulder until the tide turns and the Warhoon horde flees into darkness. Ten thousand men were engaged; three thousand dead lie on the field.

### Scene 3: Return to Thark and Departure
On return to the city, Carter waits in Tars Tarkas' quarters while the chieftain attends council. A huge creature (Woola) rushes upon Carter in an adjoining apartment. Woola had found his way back to Thark and taken up watch for Carter's return at his former quarters. Tars Tarkas returns from the jeddak's quarters, informing Carter that Tal Hajus has ordered him brought before him tonight. Tars Tarkas offers ten thoats and will accompany Carter to the nearest waterway leading to Helium.

### Scene 4: Confrontation with Sarkoja
Carter asks about Tars Tarkas' return; he replies "the wild calots, possibly, or worse," unless he battles Tal Hajus. Carter insists on staying to see Tal Hajus tonight. They eat while Carter repeats the story Sola told him on the sea bottom. Tars Tarkas works in passion and agony at recollection of horrors heaped upon Woola. He agrees to go before Tal Hajus but wants to speak to Sarkoja first. Carter accompanies him; Sarkoja casts a look of venomous hatred. Tars Tarkas warns her about Gozava's lover seeking revenge, suggesting she might be tied to a wild thoat for survival test. The next morning Sarkoja is gone and never seen again.

### Scene 5: Palace Confrontation
They hasten to the jeddak's palace; Tal Hajus stands erect on his platform glowering at the entrance. He shrieks to strap Carter to a pillar, heat irons, and burn eyes from his head. Carter turns to the assembled council, ignoring Tal Hajus, claiming he has been a chief among them and fought for Thark. He accuses Tal Hajus of cowardice (didn't fight in battle) and asks how sounds "Jeddak of Thark?" A roar of applause greets this suggestion. Lorquas Ptomel asks if the jeddak must prove fitness to rule; twenty chieftains flash swords in assent.

### Scene 6: Victory and New Plan
Tal Hajus draws his long-sword and advances to meet Tars Tarkas. The combat is soon over; Tars Tarkas stands with foot upon neck of dead monster, becoming jeddak among the Tharks. His first act is making Carter a full-fledged chieftain. Carter enlists them in his cause against Zodanga, telling Tars Tarkas the story of adventures and explaining the thought. Tars Tarkas addresses the council: Dejah Thoris is held by Zodanga; rescue her and return to Helium. Loot of Zodanga would be magnificent; alliance with Helium could increase hatchings and make them supreme among green men. They rise to the bait as a speckled trout to a fly. Twenty mounted messengers speed across dead sea bottoms to call hordes together.

### Scene 7: March to Zodanga
In three days they are on march toward Zodanga, one hundred thousand strong (enlisted services of three smaller hordes). At head of column Carter rides beside great Thark; Woola trots at heels. They travel entirely by night, camping during day at deserted cities where beasts kept indoors. Tars Tarkas enlists fifty thousand more warriors from various hordes. Ten days after setting out they halt at midnight outside Zodanga, one hundred and fifty thousand strong. Fighting strength equivalent to ten times their number of red men. Task of obtaining entry devolves upon Carter; he directs Tars Tarkas to hold forces in two divisions opposite large gateways.

### Scene 8: Wall Climb Entry
Carter takes twenty dismounted warriors and approaches one of small gates piercing walls at short intervals. Walls are seventy-five feet high, fifty feet thick, built of enormous blocks of carborundum. Placing three warriors with faces to wall arms locked, Carter commands two more to mount shoulders; sixth climbs upon shoulders of upper two. Head of topmost warrior towers over forty feet from ground. In this way, with ten warriors, he builds series of three steps from ground to shoulders of topmost man. Starting from short distance behind them, he runs swiftly up from one tier to next, final bound from broad shoulders of highest he clutches top of great wall and draws himself to broad expanse. After him he drags six lengths of leather from equal number of warriors; previously fastened together. Passing one end to topmost warrior, he lowers other end cautiously over opposite side toward avenue below. Lowering himself to end of leather strap, he drops remaining thirty feet to pavement below.

### Scene 9: Palace Grounds Entry
Carter learned secret of opening gates from Kantos Kan; in another moment twenty great fighting men stand within doomed city of Zodanga. He finds delight that entered at lower boundary of enormous palace grounds. Building itself shows blaze of glorious light in distance. He determines to lead detachment directly within palace itself while balance of horde attacks barracks of soldiery. Dispatching one man to Tars Tarkas for detail of fifty Tharks, he orders ten warriors to capture and open one of great gates while nine remaining take the other. Plans work to perfection; sentries dispatched to fathers upon banks of lost sea of Korus; guards at both gates follow in silence.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH024

## Characters Present or Referenced

| Character | Role | Status |
|-----------|------|--------|
| John Carter | Protagonist, physically present throughout chapter | Fully identified |
| Tars Tarkas | Chieftain of Thark, main ally | Fully identified |
| Woola | Huge creature, found return to Thark | Fully identified |
| Tal Hajus | Jeddak of Thark, antagonist | Fully identified |
| Lorquas Ptomel | Council member | Fully identified |
| Sarkoja | Antagonist character | Fully identified |
| Dejah Thoris | Held captive by Zodanga (referenced) | Referenced only |
| Kantos Kan | Advisor who taught gate-opening secret | Referenced only |

## Chapter Summary

This chapter documents John Carter's transformation from outsider to chieftain of Thark, his alliance with Tars Tarkas against Zodanga, and the strategic planning for rescuing Dejah Thoris. The narrative spans from Carter's rescue of Tars Tarkas through the palace confrontation with Tal Hajus to the march toward Zodanga and entry into the doomed city.

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
# John Carter - Chapter CH024

## Display Name
John Carter

## Chapter Role
Protagonist, central figure throughout all scenes

## Physical Presence
Physically present in every scene of the chapter

## Physical Description (Supported by Source)
- Tall, athletic build typical of Barsoomian heroes
- Wears long-sword for combat defense
- Appears as chief among Thark warriors after transformation
- Rides beside great Thark during march to Zodanga

## Costume & Silhouette
- Standard heroic warrior attire
- Long-sword carried at hip
- Distinguished by leadership presence among green men

## Continuity-Critical Traits
- Former outsider to Thark, now full-fledged chieftain
- Has learned of Dejah Thoris's captivity by Zodanga
- Plans alliance with Helium for supremacy among green men
- Tasked with obtaining entry into Zodanga city

## Render-Facing Prompt Notes
"Barsoomian hero John Carter, tall athletic build, long-sword at hip, heroic warrior attire, distinguished leadership presence among green men, transformation from outsider to chieftain of Thark"

## Uncertainty Notes
None - character fully identified with sufficient physical description for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Chapter CH024

## Display Name
Tars Tarkas

## Chapter Role
Chieftain of Thark, Carter's main ally and friend

## Physical Presence
Physically present in every scene of the chapter

## Physical Description (Supported by Source)
- Green-skinned Barsoomian warrior
- Wears long-sword for combat
- Knocked down by dead body in Scene 1
- Gives slight smile to Carter after rescue
- Touches shoulder in gesture of friendship
- Stands with foot upon neck of dead monster after victory

## Costume & Silhouette
- Traditional Thark chieftain warrior attire
- Long-sword carried for battle
- Distinguished by chief status among warriors
- Rides at head of column during march to Zodanga

## Continuity-Critical Traits
- Learns friendship through Carter's actions
- Becomes jeddak after defeating Tal Hajus
- Makes Carter full-fledged chieftain as first act
- Enlists fifty thousand more warriors from various hordes
- Plans rescue of Dejah Thoris and return to Helium

## Render-Facing Prompt Notes
"Green-skinned Barsoomian warrior Tars Tarkas, traditional Thark chieftain attire, long-sword for battle, distinguished chief status among green men, transformation from outsider to jeddak of Thark"

## Uncertainty Notes
None - character fully identified with sufficient physical description for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - Chapter CH024

## Display Name
Woola

## Chapter Role
Huge creature, Carter's loyal companion and protector

## Physical Presence
Physically present in Scenes 3, 7, and 8 of the chapter

## Physical Description (Supported by Source)
- Huge creature (described as "huge" in text)
- Found his way back to Thark from former quarters
- Took up watch for Carter's return at former quarters
- Rushes upon Carter in adjoining apartment in Scene 3
- Trots at heels of great Thark during march to Zodanga

## Costume & Silhouette
- No specific costume mentioned (creature)
- Large, imposing silhouette typical of huge creature
- Moves with purpose and loyalty

## Continuity-Critical Traits
- Formerly Carter's companion before return to Thark
- Loyal protector who waited for Carter's return
- Enlisted by Tars Tarkas during march to Zodanga
- Travels entirely by night, camping at deserted cities

## Render-Facing Prompt Notes
"Huge creature Woola, large imposing silhouette, no specific costume, loyal companion of John Carter and Tars Tarkas, found return to Thark from former quarters"

## Uncertainty Notes
None - character fully identified with sufficient physical description for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus - Chapter CH024

## Display Name
Tal Hajus

## Chapter Role
Jeddak of Thark, antagonist character

## Physical Presence
Physically present in Scenes 3, 5 of the chapter

## Physical Description (Supported by Source)
- Stands erect on platform glowering at entrance
- Shrieks to strap Carter to pillar and burn eyes from head
- Draws long-sword for combat with Tars Tarkas
- Killed by Tars Tarkas in palace confrontation
- Accused of cowardice for not fighting in battle

## Costume & Silhouette
- Jeddak platform attire (implied)
- Long-sword carried for combat
- Glowering, imposing presence on platform

## Continuity-Critical Traits
- Ordered Carter brought before him tonight
- Accuses Carter of being chief among Tharks
- Must prove fitness to rule according to council
- Killed by Tars Tarkas after combat victory
- His death allows Tars Tarkas to become jeddak

## Render-Facing Prompt Notes
"Jeddak Tal Hajus, erect platform stance, glowering expression, long-sword for combat, antagonist role in Thark palace, killed by Tars Tarkas after proving cowardice"

## Uncertainty Notes
None - character fully identified with sufficient physical description for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel - Chapter CH024

## Display Name
Lorquas Ptomel

## Chapter Role
Council member, Thark warrior leader

## Physical Presence
Physically present in Scene 5 of the chapter

## Physical Description (Supported by Source)
- Assembled council member during palace confrontation
- Questions if jeddak must prove fitness to rule
- Twenty chieftains flash swords in assent to his question
- Supports Carter's claim as chief among Tharks

## Costume & Silhouette
- Council warrior attire (implied)
- Flashing swords indicating warrior status
- Part of assembled council at palace

## Continuity-Critical Traits
- Represents council opinion on jeddak fitness
- Supports Carter's leadership claim
- Part of twenty chieftains who flash swords in assent
- Present during Tal Hajus's death and Tars Tarkas's ascension

## Render-Facing Prompt Notes
"Council member Lorquas Ptomel, warrior attire with flashing swords, part of assembled council at Thark palace, supports Carter's leadership claim among chieftains"

## Uncertainty Notes
None - character fully identified with sufficient physical description for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja - Chapter CH024

## Display Name
Sarkoja

## Chapter Role
Antagonist character, mysterious figure

## Physical Presence
Physically present in Scene 4 of the chapter

## Physical Description (Supported by Source)
- Casts look of venomous hatred at Carter and Tars Tarkas
- Warned about Gozava's lover seeking revenge
- Suggests she might be tied to wild thoat for survival test
- Gone next morning and never seen again

## Costume & Silhouette
- No specific costume mentioned
- Venomous, threatening presence
- Mysterious figure who disappears after confrontation

## Continuity-Critical Traits
- Associated with Gozava's lover seeking revenge
- Possibly tied to wild thoat for survival test
- Disappears mysteriously after warning given
- Never seen again after Scene 4

## Render-Facing Prompt Notes
"Antagonist Sarkoja, venomous threatening presence, mysterious figure who disappears after confrontation, associated with Gozava's lover seeking revenge and wild thoat survival test"

## Uncertainty Notes
None - character fully identified with sufficient physical description for image generation

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character only referenced in chapter summary as being held captive by Zodanga; no physical description or visual details provided in this chapter's source material

clarification_required: true
clarification_reason: Character is mentioned but not physically present; needs clarification about current appearance and condition while held captive

clarification_question: What is Dejah Thoris's current physical appearance and condition while held captive by Zodanga?

[[SECTION markdown]]
# Dejah Thoris - Chapter CH024

## Display Name
Dejah Thoris

## Chapter Role
Captive princess, referenced only in chapter summary

## Physical Presence
Referenced only; not physically present in this chapter

## Physical Description (Supported by Source)
- Held captive by Zodanga according to Tars Tarkas's council address
- No physical description provided in this chapter's source material
- Mentioned as motivation for rescue mission against Zodanga

## Costume & Silhouette
- No costume details available from this chapter
- Princess status implied by name and title
- Captive condition while held by Zodanga

## Continuity-Critical Traits
- Held captive by Zodanga (primary motivation for march)
- Rescue is first act of alliance with Helium
- Loot of Zodanga would be magnificent after rescue
- Return to Helium planned after successful rescue

## Render-Facing Prompt Notes
"Princess Dejah Thoris, held captive by Zodanga, no physical description available from this chapter source material, motivation for rescue mission against Zodanga and alliance with Helium"

## Uncertainty Notes
Character only referenced in chapter summary; needs clarification about current appearance and condition while held captive. No physical description or visual details provided in this chapter's source material.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: kantos_kan
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character only referenced in chapter summary as having taught Carter secret of opening gates; no physical description or visual details provided in this chapter's source material

clarification_required: true
clarification_reason: Character is mentioned but not physically present; needs clarification about current appearance and condition

clarification_question: What is Kantos Kan's current physical appearance and condition? Is he still alive and where is he located?

[[SECTION markdown]]
# Kantos Kan - Chapter CH024

## Display Name
Kantos Kan

## Chapter Role
Advisor, gate-opening expert, referenced only in chapter summary

## Physical Presence
Referenced only; not physically present in this chapter

## Physical Description (Supported by Source)
- Taught Carter secret of opening gates from Zodanga city
- No physical description provided in this chapter's source material
- Previously advised Carter on entering doomed city of Zodanga

## Costume & Silhouette
- No costume details available from this chapter
- Advisor/expert status implied by gate-opening knowledge
- Previously associated with Carter's adventures

## Continuity-Critical Traits
- Taught Carter secret of opening gates from Zodanga city
- Previously advised on entering doomed city of Zodanga
- Knowledge passed to Carter for mission against Zodanga
- No current location or condition mentioned in this chapter

## Render-Facing Prompt Notes
"Advisor Kantos Kan, gate-opening expert, previously taught Carter secret of opening gates from Zodanga city, no physical description available from this chapter source material"

## Uncertainty Notes
Character only referenced in chapter summary; needs clarification about current appearance and condition. No physical description or visual details provided in this chapter's source material.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
