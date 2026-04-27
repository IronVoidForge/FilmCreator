Status: 70%

# Phase 10 - Shot Coverage Density Plan

## Goal

Upgrade shot planning from "one shot per story beat" into real film coverage while preserving the current shot package detail level.

The planner should support tunable coverage density:

```text
low
medium
high
legacy
```

Default should be `medium`.

`legacy` preserves the current one-shot-per-beat behavior for comparison, debugging, and low-cost validation.

The purpose is not to force every scene into a huge edit. The purpose is to let FilmCreator vary coverage density intentionally, compare results, and avoid packing too much story into too few shots.

Coverage density does not only mean "more shots." It means more editorial control when the story weight deserves it. Minor connective beats should stay economical even at medium density. Major reveals, action beats, and important dialogue should expand more aggressively.

## Research Basis

Film coverage is not just a sequence of story beats. Standard coverage uses combinations of:

- establishing / wide / master shots
- two-shots and group shots
- over-the-shoulder shots
- clean singles
- closeups and reaction shots
- inserts
- cutaways
- POV shots
- reverse angles
- movement handoff shots

Useful references:

- StudioBinder, "What's in Your Shot List" - shot sizes, OTS, wide shots
- StudioBinder, "Shot Reverse Shot: Reaction Shots, Cutaways, and Coverage" - dialogue coverage and the idea that coverage creates editorial options
- StudioBinder, "Camera Framing Techniques" - single, two-shot, three-shot, OTS, POV, insert
- B&H, "Filmmaking 101: Camera Shot Types" - establishing, master, POV, reaction, reverse angle, two-shot, cutaway

The key practical lesson:

```text
beat != shot
```

A beat is what happens. A shot is one piece of coverage for that beat.

## Current Problem

Wizard of Oz currently shows the problem clearly:

- almost every scene has 3 shots
- most scenes have 3 beats
- therefore the system is creating one shot per beat
- average target shot duration is okay, but the total scene duration is too short
- scenes read like storyboard summaries rather than cuttable movie coverage

Example issue:

```text
Scarecrow asks Queen for help
Tin Woodman builds truck
Mouse army arrives
```

This is currently 3 shots. A movie version needs the plea, the Queen's reaction, Woodman work coverage, construction inserts, mouse scale shots, wide swarm arrival, and a handoff.

## Coverage Density Definitions

Density is only one input. Final shot count should be:

```text
coverage_count = recipe(coverage_intent, beat_type, density, importance)
```

This avoids applying equal expansion to every beat.

## Coverage Intent

Add a scene-level coverage intent. In v1 this can be inferred by code from scene fields; later it can be stored explicitly in scene contracts.

Suggested intents:

```text
economical_storybook
classic_dialogue
adventure_action
wonder_reveal
suspense_investigation
montage_travel
ceremonial_tableau
```

Intent changes how density behaves:

- `economical_storybook` favors masters, readable silhouettes, and fewer cuts.
- `classic_dialogue` favors master/two-shot, singles, listener reactions, and selective OTS.
- `adventure_action` favors geography, action, impact, reaction, and handoff shots.
- `wonder_reveal` favors partial reveal, scale proof, POV, and reaction.
- `suspense_investigation` favors POV, inserts, clue details, and reaction.
- `montage_travel` favors travel geography, landmarks, passage, and transition shots.
- `ceremonial_tableau` favors group geography, speaker singles, crowd reactions, and scale.

For Wizard of Oz, Alice, Princess of Mars, and similar public-domain adventure/fantasy projects, the first profile should be:

```json
{
  "shot_coverage_profile": "classic_adventure"
}
```

`classic_adventure` should favor readable silhouettes, clear geography, wide shots for fantasy scale, reaction closeups for wonder/fear, and inserts for magical or story-important objects.

## Beat Importance

Add deterministic beat importance:

```text
minor
normal
major
set_piece
```

Meaning:

- `minor` - connective tissue, simple travel, transition, minor action
- `normal` - ordinary story beat requiring clear coverage
- `major` - emotional turn, reveal, decision, important dialogue, meaningful action
- `set_piece` - extended action, spectacle, ritual, musical/training sequence, major confrontation

Examples:

```text
medium density + minor travel beat = 1-2 shots
medium density + normal dialogue beat = 4-7 shots
medium density + major reveal beat = 5-8 shots
medium density + set_piece action beat = 10-18 shots, likely chunked
```

Importance should be stored in coverage metadata so bad calls are easy to debug.

### Low

Use when the user wants a fast, economical, illustrated-storybook pass.

Intent:

- keep shot count near current scale
- use longer shots
- create enough coverage to understand the scene, not enough for a polished edit

Targets:

```text
target shot length: 8-12 seconds
simple beat: 1 shot
dialogue beat: 2-4 shots
action beat: 3-5 shots
reveal beat: 2-4 shots
montage/travel beat: 2-5 shots
```

Minor beats can remain 1 shot in low density.

### Medium

Default.

Use when the user wants credible movie coverage without exploding cost.

Intent:

- enough variation to cut a scene
- clear subjects in each shot
- 4-7 second shot rhythm for important moments, with occasional longer masters
- not full blockbuster coverage for every minor beat

Targets:

```text
target shot length: 5-8 seconds
simple beat: 2 shots
dialogue beat: 5-9 shots
action beat: 6-12 shots
reveal beat: 5-9 shots
montage/travel beat: 4-8 shots
```

Medium should not force 6-14 shots per scene mechanically. A medium-density minor scene may still be 3-5 shots. A medium-density major scene may become 10-18 shots.

### High

Use for major scenes, action sequences, arguments, reveals, or final-quality coverage tests.

Intent:

- rich editorial coverage
- more singles, inserts, reactions, and geography resets
- still structured enough for local LLM limits

Targets:

```text
target shot length: 4-7 seconds
simple beat: 3-4 shots
dialogue beat: 8-16 shots
action beat: 10-25 shots
reveal beat: 8-14 shots
montage/travel beat: 6-14 shots
```

High density may require LLM chunking by beat group.

High should still preserve long masters for stillness, ceremony, or dread when the coverage intent calls for it.

## Runtime Planner

Per-shot duration is not enough. The planner should estimate target scene and beat duration first, then distribute shot durations across coverage roles.

V1 ranges:

```text
minor scene: 20-35 seconds
normal scene: 35-75 seconds
major scene: 75-150 seconds
set piece: 120-300 seconds eventually, capped in v1 unless explicitly requested
```

V1 shot duration ranges still apply:

```text
low: 8-12 seconds
medium: 5-8 seconds
high: 4-7 seconds
```

Runtime algorithm:

1. classify scene coverage intent
2. classify each beat type and importance
3. assign beat target seconds from importance and action/dialogue complexity
4. expand shot roles from recipe
5. distribute beat target seconds across roles
6. clamp shot seconds to density range, allowing master/tableau shots to run longer
7. clamp total scene duration to scene importance range unless explicitly marked set piece

This keeps medium density from ballooning every scene while still expanding major beats.

## Beat Classification

Add a deterministic beat classifier before shot blueprint expansion.

Inputs already available:

- beat summary
- action_start
- action_end
- active_subjects
- passive_subjects
- spatial_context
- blocking_hint
- environment_subzone
- coverage_hint
- coverage_priority
- scene summary
- visual_coverage_families
- planned_shots when present

Suggested beat types:

```text
establishing_arrival
dialogue_two_person
dialogue_group
dialogue_council_or_court
dialogue_crowd_response
reaction_emotion
action_conflict
movement_travel
reveal_wonder
investigation_discovery
object_or_magic_business
transition_handoff
```

V1 should implement only the core types first:

```text
establishing_arrival
dialogue_two_person
dialogue_group
dialogue_council_or_court
action_conflict
reveal_wonder
object_or_magic_business
movement_travel
reaction_emotion
transition_handoff
```

Treat monologue, flashback, and montage as aliases or secondary hints in v1. Do not make too many classifier branches before the basic system is debugged.

Classifier should be conservative and explainable. It can be keyword/rule based first.

Examples:

- "asks", "tells", "answers", "warns", "explains" with two active subjects -> `dialogue_two_person`
- "asks", "tells", "answers", "warns", "explains" with three or more active/passive subjects -> `dialogue_group`
- "court", "council", "audience", "queen", "king", "wizard", "throne", "assembly" -> `dialogue_council_or_court`
- "recounts", "remembers", "flashback" -> `dialogue_group` with memory/flashback coverage hints in v1
- "attacks", "fights", "chases", "rescues" -> `action_conflict`
- "arrives", "enters", "approaches" -> `establishing_arrival`
- "revealed", "appears", "manifests" -> `reveal_wonder`
- "builds", "assembles", "uses", "unlocks" -> `object_or_magic_business`
- "travels", "walks", "crosses" -> `movement_travel`

The LLM can later refine beat type, but code should produce a stable first pass.

Output debug metadata:

```json
{
  "coverage_classification": {
    "beat_type": "dialogue_group",
    "importance": "major",
    "confidence": 0.78,
    "reasons": ["summary contains warns", "active/passive subject count = 5", "scene intent = ceremonial_tableau"]
  }
}
```

Do not use an LLM for v1 classification. Keep classification deterministic and unit-testable.

## Coverage Recipes

Recipes are not rigid templates. They are ordered menus. The planner chooses a subset based on density, number of subjects, scene importance, and action complexity.

Each generated shot blueprint must still have:

- clear primary subject
- clear secondary subjects if any
- explicit start state
- explicit end state
- specific action during shot
- environment/subzone
- shot type
- shot size
- camera angle
- lens family
- motion/zoom/focus
- continuity handoff

### Establishing / Arrival Beat

Purpose:

- orient the audience
- show geography, scale, entry direction, and initial subject placement

Low:

1. establishing wide or master

Medium:

1. establishing wide / extreme wide
2. traveling medium or group shot
3. reaction single or POV to what is seen

High:

1. extreme wide geography
2. master shot with entry vector
3. group shot / two-shot moving through space
4. POV or insert of destination/obstacle
5. reaction single
6. handoff shot toward next action

Useful shot types:

```text
establishing_wide
master_wide
group_wide
traveling_medium
subject_pov
reaction_closeup
handoff_medium
```

### Dialogue: Two-Person Beat

Purpose:

- preserve speaker/listener geography
- allow emotional emphasis
- provide edit points for pacing

Low:

1. two-shot or master
2. closeup speaker / reaction listener

Medium:

1. master/two-shot
2. OTS speaker A to B
3. reverse OTS speaker B to A
4. clean single A
5. clean single B
6. listener reaction
7. optional insert/cutaway if object or subtext matters

High:

1. master/two-shot
2. dirty single / OTS A
3. dirty single / OTS B
4. clean single A
5. clean single B
6. tighter closeup A
7. tighter closeup B or listener
8. hands/prop insert
9. cutaway / environment pressure
10. emotional landing reaction

Useful shot types:

```text
master_two_shot
over_the_shoulder
reverse_over_the_shoulder
clean_single
reaction_closeup
insert_detail
cutaway
closing_reaction
```

Subject rule:

- singles must name the visible primary subject
- OTS shots must name foreground shoulder subject and featured subject
- reaction shots must state what the character is reacting to

### Dialogue: Group Beat

Purpose:

- preserve group geography
- keep the current speaker clear
- show group/listener reactions without pretending every exchange is a clean two-person reverse

Low:

1. group master
2. speaker single or group reaction

Medium:

1. group master / geography
2. speaker single
3. listener group reaction
4. key individual reaction
5. optional clean single for next speaker
6. object/location cutaway if relevant

High:

1. group master
2. speaker single
3. primary listener single
4. group reaction
5. secondary listener reaction
6. relevant insert/cutaway
7. new speaker single
8. emotional landing reaction

Useful shot types:

```text
group_master
speaker_single
listener_group_reaction
key_individual_reaction
clean_single
insert_detail
cutaway
closing_reaction
```

Rules:

- Do not overuse OTS in group scenes.
- Use OTS only when there is a clear speaker/listener pair and useful foreground geography.
- For Dorothy + companions + authority figure scenes, prefer group master, speaker single, group reaction, and key individual reactions.

### Dialogue: Council / Court / Audience Beat

Purpose:

- make hierarchy and power geography clear
- preserve the authority figure, petitioner, guards/crowd, and scale

Low:

1. ceremonial master / tableau
2. authority speaker or petitioner reaction

Medium:

1. ceremonial wide/master
2. authority speaker single
3. petitioner/group reaction
4. court/crowd response
5. scale or throne/location insert
6. decision/ultimatum closeup

High:

1. establishing ceremonial tableau
2. authority figure reveal
3. petitioner group geography
4. authority single
5. petitioner single
6. crowd/listener response
7. object/throne/symbol insert
8. reverse reaction
9. decision landing closeup
10. exit/handoff

Useful shot types:

```text
ceremonial_master
authority_single
petitioner_group
crowd_response
scale_proof_wide
symbol_insert
reaction_closeup
handoff_wide
```

### Monologue / Storytelling / Flashback Beat

Purpose:

- keep present speaker anchored
- visualize remembered action
- cut back to listener/reaction

Low:

1. speaker closeup
2. flashback image or cutaway

Medium:

1. present speaker closeup
2. listener reaction
3. flashback establishing
4. flashback action medium
5. symbolic insert or key detail
6. return reaction / handoff

High:

1. present master or two-shot
2. speaker closeup
3. listener reaction
4. flashback establishing
5. flashback subject medium
6. flashback insert detail
7. flashback consequence reaction
8. present speaker landing
9. present listener response

Useful shot types:

```text
present_speaker_closeup
listener_reaction
flashback_establishing
flashback_action
memory_insert
return_to_present_reaction
```

### Action / Conflict Beat

Purpose:

- preserve geography
- show cause/effect
- land impacts and reactions

Low:

1. wide action setup
2. impact/action shot
3. reaction/aftermath

Medium:

1. geography reset / wide
2. threat approach
3. defender action
4. impact insert
5. reaction
6. reposition / handoff

High:

1. wide geography
2. threat reveal
3. attacker movement
4. defender movement
5. object/weapon insert
6. impact shot
7. close reaction
8. reverse angle response
9. second impact or escalation
10. aftermath / handoff

Useful shot types:

```text
geography_wide
threat_reveal
action_medium
reverse_action
impact_insert
reaction_closeup
aftermath_wide
handoff_action
```

### Reveal / Wonder Beat

Purpose:

- delay and control information
- show scale
- show character reaction

Low:

1. reveal wide
2. reaction closeup

Medium:

1. approach / partial reveal
2. full reveal wide
3. scale proof shot
4. character POV or reaction
5. detail insert

High:

1. approach with obscured subject
2. partial detail
3. character anticipation
4. full reveal wide
5. scale comparison
6. POV
7. multiple reactions
8. detail insert
9. handoff to next action

Useful shot types:

```text
approach_medium
partial_reveal
reveal_wide
scale_proof_wide
subject_pov
reaction_closeup
insert_detail
```

### Object / Magic / Task Beat

Purpose:

- show hands, props, mechanics, transformation, or magic clearly

Low:

1. medium action
2. insert detail

Medium:

1. medium setup
2. hands/prop insert
3. reaction
4. result shot

High:

1. setup medium
2. hands insert
3. object closeup
4. magic/process detail
5. reaction
6. result wide/medium
7. consequence handoff

Useful shot types:

```text
task_medium
hands_insert
object_insert
process_detail
reaction_closeup
result_medium
```

### Movement / Travel / Montage Beat

Purpose:

- show passage, rhythm, progress, and continuity without over-covering minor action

Low:

1. wide travel shot

Medium:

1. wide travel geography
2. group medium
3. landmark/cutaway
4. character reaction or fatigue

High:

1. wide geography
2. moving group shot
3. feet/path insert
4. landmark POV
5. character reaction
6. transition handoff

Useful shot types:

```text
travel_wide
tracking_group
path_insert
landmark_cutaway
fatigue_reaction
transition_wide
```

## Avoiding Cookie-Cutter Repetition

The recipe system must not produce the exact same shot sequence every time.

Use controlled variation:

- choose from equivalent shot roles
- rotate between OTS, clean single, dirty single, and two-shot for dialogue
- prefer inserts only when a prop/action detail matters
- omit establishing shots when the previous shot already established geography and continuity is direct
- add reaction shots when emotional arc changes
- add POV when a character sees something important
- add scale proof for fantasy/sci-fi/worldbuilding beats
- add cutaway when context/subtext matters

### Master / Geography Reuse

Do not add a new establishing or master shot for every beat.

Use a geography reset only when:

- location changes
- blocking changes significantly
- a new group or threat enters
- action begins after dialogue
- scale/reveal matters
- the audience needs a spatial reminder before an impact/movement beat

### Emotional Punctuation

Add reaction shots only when:

- power shifts
- a decision changes
- surprise/fear/wonder occurs
- a character is excluded or observing
- the next beat depends on the emotional response

### Insert Eligibility

Use inserts only when something visible matters:

- hands doing a task
- weapon/object/key item
- map/sign/door/lock
- magical transformation
- evidence clue
- scale proof

Do not add inserts just to hit a count.

### POV Eligibility

Use POV only when:

- a character discovers something
- reveal is subjective
- fear/wonder depends on what they see
- direction/geography matters

## Planned Shots Compatibility

Scene contracts may already contain `planned_shots`. Those should be used as seed coverage roles, not as the final count.

Rule:

```text
if planned_shots exist:
  treat each planned shot as a required story/action coverage seed
  expand around it according to density, importance, and coverage intent
  preserve its subject/action/subzone where possible
  do not assume planned_shots are the complete edit
```

This lets existing scene contracts remain useful without locking the shot planner into one shot per beat.

Each recipe slot should be a role, not a fixed shot:

```json
{
  "role": "listener_reaction",
  "allowed_shot_types": ["reaction_closeup", "clean_single", "over_the_shoulder"],
  "required_subject_logic": "listener_or_witness",
  "when": "dialogue changes emotional state"
}
```

## Prompt Strategy

The LLM should not be asked to invent the coverage count from nothing.

Pipeline should send:

- coverage density
- beat classifications
- coverage recipe roles
- expanded shot blueprints
- coverage intent, beat importance, and target scene/beat seconds
- instruction to preserve shot count and shot ids
- instruction to fill all shot fields with equal detail
- instruction to keep each shot's primary subject explicit

Add to shot planner prompt:

```text
COVERAGE DENSITY:
medium

COVERAGE RULES:
- Each shot is one cuttable movie shot, not a paragraph summary.
- Preserve every supplied shot_id and shot_order.
- Do not merge story events into fewer shots.
- If a blueprint is weak, improve its details but keep its coverage role.
- Fill every shot with concrete subject, camera, blocking, start_state, end_state, and handoff.
- Every shot must name exactly one primary framed subject or a clearly framed group/environment subject.
- For group/court dialogue, prefer speaker singles, group reactions, key individual reactions, and tableau geography over excessive OTS.
- Use OTS/reverse/single/reaction/insert/cutaway roles when supplied by the blueprint.
- Keep target_seconds in the configured range unless the blueprint marks the shot as a master or transition.

EXPANDED COVERAGE BLUEPRINTS:
...
```

## LLM Chunking / Splits

The new one-call-per-scene shot planning is fine for normal medium scenes, but high-density or complex scenes need chunking.

Recommended thresholds:

```text
max shots per LLM call: 12
soft token threshold: 18,000 prompt chars
hard token threshold: 28,000 prompt chars
```

Splitting rules:

1. Build all shot blueprints deterministically first.
2. If total shots <= 12 and prompt size is below threshold, call LLM once for the scene.
3. If total shots > 12, split by beat group.
4. Each chunk includes:
   - full scene summary / scene event chain
   - all beat summaries
   - previous chunk's last shot handoff
   - next chunk's first beat goal
   - only the current chunk's expanded shot blueprints
5. After chunk calls, merge by shot_id and validate full scene count.
6. If a chunk fails validation, retry that chunk once.
7. If still failed, fall back to deterministic blueprints for that chunk only.

This preserves detail without forcing the local LLM to handle a huge 25-shot packet all at once.

## Code Integration Plan

### New Config

Add runtime/project setting:

```json
{
  "shot_coverage_density": "medium",
  "shot_coverage_profile": "classic_adventure"
}
```

Precedence:

```text
CLI argument
  overrides project config
    overrides runtime default
      overrides hardcoded default medium
```

CLI option:

```powershell
python -m orchestrator synthesize-shot-packages wizard_of_oz --coverage-density medium
```

Production/resume should pass the configured density.

### New Module

Add:

```text
orchestrator/shot_coverage.py
```

Responsibilities:

- classify beat type
- choose coverage recipe
- expand one beat into N shot roles
- assign shot ids
- calculate target seconds
- avoid repetitive recipe choices
- produce compact blueprints for `_build_shot_blueprints`

Suggested dataclasses:

```python
@dataclass(frozen=True)
class BeatClassification:
    beat_id: str
    beat_type: str
    importance: str
    confidence: float
    reasons: list[str]


@dataclass(frozen=True)
class CoverageRole:
    role: str
    allowed_shot_types: list[str]
    preferred_shot_size: str
    subject_logic: str
    purpose: str
    target_seconds_min: float
    target_seconds_max: float
    optional: bool = False


@dataclass(frozen=True)
class ShotCoverageBlueprint:
    shot_id: str
    shot_order: int
    beat_id: str
    beat_type: str
    coverage_role: str
    shot_type: str
    target_seconds: float
    subject_logic: str
    environment_logic: str
    required_detail: str
    continuity_purpose: str
```

Keep this module deterministic and unit-testable.

### Modify `orchestrator/shot_planner.py`

Current insertion point:

```text
_build_shot_blueprints(...)
```

Change from:

```text
for each beat -> one SH###
```

To:

```text
for each beat:
  classify beat
  expand coverage roles by density
  create SH### blueprint for each role
  preserve beat_id on each shot
```

Then keep the existing enrichment logic:

- subject selection
- environment selection
- camera defaults
- start/end/action handoff
- prompt seed
- shot package rendering

Do not reduce current shot package fields.

### Shot Package Metadata

Add optional fields to shot package output:

```json
{
  "coverage_density": "medium",
  "coverage_profile": "classic_adventure",
  "coverage_intent": "classic_dialogue",
  "coverage_role": "listener_group_reaction",
  "beat_type": "dialogue_group",
  "coverage_importance": "normal",
  "coverage_blueprint_source": "deterministic_v1",
  "coverage_classification": {
    "confidence": 0.78,
    "reasons": ["active/passive subject count = 5"]
  }
}
```

These fields can live on the shot package or in metadata. They are important for quality grading, debugging, and side-by-side density comparisons.

### Validation

LLM validation should reject:

- missing shot id
- extra shot id
- merged shots
- blank primary subject
- blank start/end/action
- invalid shot enum
- visible primary subject mismatch
- missing coverage role
- target seconds outside allowed range unless master/tableau exception applies

### Modify Scene Contracts Later, Not First

Do not require scene contract regeneration for the first implementation.

Phase 10 can infer beat types from existing scene contracts.

Later, scene contracts can add:

```text
beat_type
coverage_importance
target_screen_seconds
```

But Phase 10 should work without those fields.

## Validation Plan

Run a small slice in all three modes:

```powershell
python -m orchestrator synthesize-shot-packages wizard_of_oz --chapters 4 --coverage-density legacy --force
python -m orchestrator synthesize-shot-packages wizard_of_oz --chapters 4 --coverage-density low --force
python -m orchestrator synthesize-shot-packages wizard_of_oz --chapters 4 --coverage-density medium --force
python -m orchestrator synthesize-shot-packages wizard_of_oz --chapters 4 --coverage-density high --force
```

Compare:

- shots per scene
- shots per beat
- shot type diversity
- target runtime
- percentage of generic shots
- review queue count
- sample prompt quality

Expected rough results:

```text
legacy: current one-shot-per-beat behavior
low:    3-6 shots per scene for most scenes
medium: 3-5 shots for minor scenes, 6-14 shots for normal/major scenes
high:   12-30 shots per important scene, chunked when needed, but still economical for minor beats
```

## Acceptance Criteria

- Default medium density produces more than one shot per meaningful beat.
- Minor connective beats can remain economical even at medium/high density.
- Every shot remains a detailed shot package with clear subject and action state.
- Dialogue scenes distinguish two-person, group, court/council, and crowd-response coverage.
- Action scenes include geography, action, impact, and reaction coverage.
- Reveal scenes include scale and reaction coverage.
- LLM calls are chunked when a scene becomes too large.
- The user can tune `legacy`, `low`, `medium`, or `high` without changing code.
