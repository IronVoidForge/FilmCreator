from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


COVERAGE_DENSITIES = {"legacy", "low", "medium", "high"}
DEFAULT_COVERAGE_DENSITY = "medium"
DEFAULT_COVERAGE_PROFILE = "classic_adventure"


@dataclass(frozen=True)
class BeatClassification:
    beat_id: str
    beat_type: str
    importance: str
    confidence: float
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "beat_id": self.beat_id,
            "beat_type": self.beat_type,
            "importance": self.importance,
            "confidence": self.confidence,
            "reasons": list(self.reasons),
        }


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
    coverage_density: str
    coverage_profile: str
    coverage_intent: str
    coverage_importance: str
    coverage_blueprint_source: str
    coverage_classification: dict[str, Any]
    seed_planned_shot: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "shot_id": self.shot_id,
            "shot_order": self.shot_order,
            "beat_id": self.beat_id,
            "beat_type": self.beat_type,
            "coverage_role": self.coverage_role,
            "shot_type": self.shot_type,
            "target_seconds": self.target_seconds,
            "subject_logic": self.subject_logic,
            "environment_logic": self.environment_logic,
            "required_detail": self.required_detail,
            "continuity_purpose": self.continuity_purpose,
            "coverage_density": self.coverage_density,
            "coverage_profile": self.coverage_profile,
            "coverage_intent": self.coverage_intent,
            "coverage_importance": self.coverage_importance,
            "coverage_blueprint_source": self.coverage_blueprint_source,
            "coverage_classification": dict(self.coverage_classification),
            "seed_planned_shot": dict(self.seed_planned_shot),
        }


def normalize_coverage_density(value: object, *, default: str = DEFAULT_COVERAGE_DENSITY) -> str:
    density = str(value or "").strip().lower()
    return density if density in COVERAGE_DENSITIES else default


def infer_scene_coverage_intent(scene_contract: dict[str, Any], *, profile: str = DEFAULT_COVERAGE_PROFILE) -> str:
    text = _scene_text(scene_contract)
    if _has_any(text, "court", "council", "throne", "assembly", "audience", "ceremony", "royal"):
        return "ceremonial_tableau"
    if _has_any(text, "reveals", "revealed", "appears", "wonder", "marvel", "magic", "transforms", "glows"):
        return "wonder_reveal"
    if _has_any(text, "fight", "attack", "battle", "chase", "escape", "rescue", "struggle", "threat"):
        return "adventure_action"
    if _has_any(text, "clue", "search", "investigate", "discover", "tracks", "hidden", "secret"):
        return "suspense_investigation"
    if _has_any(text, "travel", "journey", "montage", "crosses", "road", "path", "trail"):
        return "montage_travel"
    if _has_any(text, "asks", "answers", "tells", "warns", "explains", "speaks", "says", "argues"):
        return "classic_dialogue"
    if profile == "classic_adventure":
        return "economical_storybook"
    return "economical_storybook"


def classify_beat(beat: dict[str, Any], scene_contract: dict[str, Any], *, coverage_intent: str | None = None) -> BeatClassification:
    beat_id = str(beat.get("beat_id", "")).strip().upper() or "BT001"
    text = _beat_text(beat, scene_contract)
    subjects = _subjects(beat)
    subject_count = len(subjects)
    reasons: list[str] = []
    beat_type = "transition_handoff"
    confidence = 0.55

    if _has_any(text, "court", "council", "throne", "assembly", "audience", "queen", "king", "wizard", "judge"):
        beat_type = "dialogue_council_or_court"
        confidence = 0.82
        reasons.append("court/council authority language")
    elif _has_any(text, "fight", "attacks", "attack", "chase", "rescues", "rescue", "strikes", "struggle", "battle"):
        beat_type = "action_conflict"
        confidence = 0.78
        reasons.append("conflict/action verb")
    elif _has_any(text, "revealed", "reveals", "appears", "manifests", "wonder", "marvel", "glows", "transforms"):
        beat_type = "reveal_wonder"
        confidence = 0.78
        reasons.append("reveal/wonder verb")
    elif _has_any(text, "builds", "assembles", "uses", "unlocks", "opens", "takes", "gives", "hands", "magic", "spell"):
        beat_type = "object_or_magic_business"
        confidence = 0.72
        reasons.append("object, task, or magic business")
    elif _has_any(text, "arrives", "enters", "approaches", "reaches", "returns"):
        beat_type = "establishing_arrival"
        confidence = 0.72
        reasons.append("arrival/entry verb")
    elif _has_any(text, "travels", "walks", "crosses", "journeys", "rides", "follows", "marches"):
        beat_type = "movement_travel"
        confidence = 0.72
        reasons.append("movement/travel verb")
    elif _has_any(text, "reacts", "weeps", "laughs", "fears", "trembles", "stares", "realizes", "decides"):
        beat_type = "reaction_emotion"
        confidence = 0.7
        reasons.append("reaction/emotion verb")
    elif _has_any(text, "asks", "answers", "tells", "warns", "explains", "speaks", "says", "argues", "pleads", "promises"):
        beat_type = "dialogue_group" if subject_count >= 3 else "dialogue_two_person"
        confidence = 0.74
        reasons.append(f"dialogue verb with subject count = {subject_count}")

    if coverage_intent == "ceremonial_tableau" and beat_type in {"dialogue_group", "dialogue_two_person"}:
        beat_type = "dialogue_council_or_court"
        confidence = max(confidence, 0.76)
        reasons.append("scene intent is ceremonial_tableau")

    importance = _classify_importance(beat, scene_contract, text, beat_type)
    reasons.append(f"importance = {importance}")
    return BeatClassification(
        beat_id=beat_id,
        beat_type=beat_type,
        importance=importance,
        confidence=round(confidence, 2),
        reasons=reasons,
    )


def expand_scene_coverage(
    scene_contract: dict[str, Any],
    *,
    coverage_density: str = DEFAULT_COVERAGE_DENSITY,
    coverage_profile: str = DEFAULT_COVERAGE_PROFILE,
) -> list[ShotCoverageBlueprint]:
    density = normalize_coverage_density(coverage_density)
    beats = scene_contract.get("beat_list", [])
    if not isinstance(beats, list) or not beats:
        beats = [{"beat_id": "BT001", "summary": scene_contract.get("summary", "") or scene_contract.get("production_intent", "") or scene_contract.get("scene_title", "")}]

    normalized_beats: list[dict[str, Any]] = []
    for index, raw in enumerate(beats, start=1):
        if isinstance(raw, dict):
            item = dict(raw)
        else:
            item = {"summary": str(raw or "")}
        item["beat_id"] = str(item.get("beat_id", f"BT{index:03d}")).strip().upper() or f"BT{index:03d}"
        normalized_beats.append(item)

    intent = infer_scene_coverage_intent(scene_contract, profile=coverage_profile)
    planned = [item for item in scene_contract.get("planned_shots", []) if isinstance(item, dict)]
    planned_by_beat = _planned_shots_by_beat(planned, normalized_beats)

    result: list[ShotCoverageBlueprint] = []
    shot_order = 1
    for beat in normalized_beats:
        classification = classify_beat(beat, scene_contract, coverage_intent=intent)
        seeds = planned_by_beat.get(classification.beat_id, [])
        roles = _roles_for_beat(classification, density, intent, seed_count=len(seeds))
        target_seconds = _distribute_seconds(classification, density, roles)
        for role_index, role in enumerate(roles):
            seed = seeds[role_index] if role_index < len(seeds) else {}
            shot_type = _seed_shot_type(seed) or role.allowed_shot_types[0]
            result.append(
                ShotCoverageBlueprint(
                    shot_id=f"SH{shot_order:03d}",
                    shot_order=shot_order,
                    beat_id=classification.beat_id,
                    beat_type=classification.beat_type,
                    coverage_role=role.role,
                    shot_type=shot_type,
                    target_seconds=target_seconds[role_index],
                    subject_logic=role.subject_logic,
                    environment_logic="use beat subzone or scene environment; preserve planned subzone when supplied",
                    required_detail=role.purpose,
                    continuity_purpose=_continuity_purpose(role.role, role_index, len(roles)),
                    coverage_density=density,
                    coverage_profile=coverage_profile,
                    coverage_intent=intent,
                    coverage_importance=classification.importance,
                    coverage_blueprint_source="deterministic_v1",
                    coverage_classification=classification.to_dict(),
                    seed_planned_shot=seed,
                )
            )
            shot_order += 1
    return result


def target_seconds_allowed(target_seconds: float, density: str, shot_type: str, coverage_role: str) -> bool:
    density = normalize_coverage_density(density)
    if density == "legacy":
        return 3.0 <= target_seconds <= 14.0
    lo, hi = {"low": (8.0, 12.0), "medium": (5.0, 8.0), "high": (4.0, 7.0)}[density]
    role_text = f"{shot_type} {coverage_role}".lower()
    if _has_any(role_text, "master", "tableau", "establishing", "ceremonial", "wide", "transition"):
        return 3.0 <= target_seconds <= max(hi + 8.0, 14.0)
    return lo <= target_seconds <= hi


def _roles_for_beat(classification: BeatClassification, density: str, intent: str, *, seed_count: int) -> list[CoverageRole]:
    if density == "legacy":
        return [_role("beat_summary", ["medium"], "medium", "primary beat subject", "cover the whole beat economically")]
    recipes = _recipe_table()[classification.beat_type]
    base_count = _coverage_count(classification.beat_type, density, classification.importance, intent)
    count = max(base_count, min(seed_count + (0 if density == "low" else 1), len(recipes)))
    count = min(count, len(recipes))
    if density == "high" and count > 12:
        count = 12
    return recipes[:count]


def _coverage_count(beat_type: str, density: str, importance: str, intent: str) -> int:
    table = {
        "low": {
            "establishing_arrival": 1,
            "dialogue_two_person": 2,
            "dialogue_group": 2,
            "dialogue_council_or_court": 2,
            "action_conflict": 3,
            "reveal_wonder": 2,
            "object_or_magic_business": 2,
            "movement_travel": 1,
            "reaction_emotion": 1,
            "transition_handoff": 1,
        },
        "medium": {
            "establishing_arrival": 3,
            "dialogue_two_person": 6,
            "dialogue_group": 5,
            "dialogue_council_or_court": 6,
            "action_conflict": 6,
            "reveal_wonder": 5,
            "object_or_magic_business": 4,
            "movement_travel": 2,
            "reaction_emotion": 2,
            "transition_handoff": 1,
        },
        "high": {
            "establishing_arrival": 6,
            "dialogue_two_person": 10,
            "dialogue_group": 8,
            "dialogue_council_or_court": 10,
            "action_conflict": 12,
            "reveal_wonder": 9,
            "object_or_magic_business": 7,
            "movement_travel": 6,
            "reaction_emotion": 4,
            "transition_handoff": 3,
        },
    }[density]
    count = table.get(beat_type, 1)
    if importance == "minor":
        count = max(1, count - (2 if density != "low" else 1))
    elif importance == "major":
        count += 1 if density != "low" else 0
    elif importance == "set_piece":
        count += 3 if density == "medium" else 5 if density == "high" else 1
    if intent == "economical_storybook":
        count = max(1, count - 1)
    return count


def _distribute_seconds(classification: BeatClassification, density: str, roles: list[CoverageRole]) -> list[float]:
    if density == "legacy":
        return [7.0 for _ in roles]
    lo, hi = {"low": (8.0, 12.0), "medium": (5.0, 8.0), "high": (4.0, 7.0)}[density]
    scene_factor = {"minor": 0.92, "normal": 1.0, "major": 1.08, "set_piece": 1.15}[classification.importance]
    seconds: list[float] = []
    for role in roles:
        role_text = role.role.lower()
        if any(term in role_text for term in ("master", "wide", "tableau", "establishing", "transition")):
            value = min(hi + 4.0, max(hi, (hi + 2.0) * scene_factor))
        elif any(term in role_text for term in ("insert", "impact", "detail")):
            value = max(lo, lo * scene_factor)
        else:
            value = ((lo + hi) / 2.0) * scene_factor
        seconds.append(round(value, 1))
    return seconds


def _recipe_table() -> dict[str, list[CoverageRole]]:
    return {
        "establishing_arrival": [
            _role("establishing_wide", ["establishing_wide", "master_wide"], "wide", "environment with arriving subject", "orient geography and entry direction"),
            _role("traveling_medium", ["traveling_medium", "group_wide"], "medium", "arriving subject or group", "show motion through the space"),
            _role("subject_pov_or_reaction", ["subject_pov", "reaction_closeup"], "close_up", "arriving subject", "show what is noticed and emotional response"),
            _role("handoff_medium", ["handoff_medium"], "medium", "arriving subject", "hand off toward next action"),
            _role("scale_proof_wide", ["scale_proof_wide"], "wide", "subject against environment", "prove scale"),
            _role("destination_insert", ["insert_detail"], "insert_detail", "destination detail", "mark destination or obstacle"),
        ],
        "dialogue_two_person": [
            _role("master_two_shot", ["master_two_shot"], "medium", "both speakers", "preserve speaker/listener geography"),
            _role("over_the_shoulder_a", ["over_the_shoulder"], "medium_close", "speaker A featured over listener shoulder", "cover first speaker"),
            _role("reverse_over_the_shoulder_b", ["reverse_over_the_shoulder"], "medium_close", "speaker B featured over listener shoulder", "cover reverse speaker"),
            _role("clean_single_a", ["clean_single"], "close_up", "speaker A", "isolate first emotional beat"),
            _role("clean_single_b", ["clean_single"], "close_up", "speaker B", "isolate response"),
            _role("listener_reaction", ["reaction_closeup"], "close_up", "listener", "land the listener reaction"),
            _role("insert_or_cutaway", ["insert_detail", "cutaway"], "insert_detail", "relevant object or pressure detail", "provide edit point if visible detail matters", optional=True),
            _role("tighter_closeup_a", ["clean_single", "reaction_closeup"], "close_up", "speaker A", "heighten emotion"),
            _role("tighter_closeup_b", ["clean_single", "reaction_closeup"], "close_up", "speaker B", "heighten reverse emotion"),
            _role("closing_reaction", ["closing_reaction"], "close_up", "changed listener", "punctuate the exchange"),
        ],
        "dialogue_group": [
            _role("group_master", ["group_master"], "wide", "full group", "preserve group geography"),
            _role("speaker_single", ["speaker_single"], "medium_close", "current speaker", "clarify speaker"),
            _role("listener_group_reaction", ["listener_group_reaction"], "medium", "listening group", "show group response"),
            _role("key_individual_reaction", ["key_individual_reaction"], "close_up", "key listener", "land individual reaction"),
            _role("next_speaker_single", ["clean_single", "speaker_single"], "medium_close", "next speaker", "cover next speaker"),
            _role("insert_or_cutaway", ["insert_detail", "cutaway"], "insert_detail", "object or location pressure", "add relevant visual context", optional=True),
            _role("secondary_listener_reaction", ["reaction_closeup"], "close_up", "secondary listener", "vary listener response"),
            _role("closing_reaction", ["closing_reaction"], "close_up", "group or key witness", "punctuate group beat"),
        ],
        "dialogue_council_or_court": [
            _role("ceremonial_master", ["ceremonial_master"], "wide", "authority, petitioners, and court", "establish hierarchy and power geography"),
            _role("authority_single", ["authority_single"], "medium_close", "authority figure", "cover authority statement"),
            _role("petitioner_group", ["petitioner_group"], "medium", "petitioning group", "show group position before power"),
            _role("crowd_response", ["crowd_response"], "medium", "court or crowd", "show public response"),
            _role("symbol_insert", ["symbol_insert", "insert_detail"], "insert_detail", "throne, emblem, or decision object", "anchor ceremony and stakes"),
            _role("decision_closeup", ["reaction_closeup", "closing_reaction"], "close_up", "authority or petitioner", "land decision or ultimatum"),
            _role("scale_proof_wide", ["scale_proof_wide"], "wide", "court scale", "show rank and scale"),
            _role("petitioner_single", ["clean_single"], "close_up", "lead petitioner", "isolate plea or response"),
            _role("reverse_reaction", ["reaction_closeup"], "close_up", "opposing listener", "show reverse reaction"),
            _role("handoff_wide", ["handoff_wide"], "wide", "court geography", "move toward exit or next command"),
        ],
        "action_conflict": [
            _role("geography_wide", ["geography_wide"], "wide", "full action geography", "reset space before conflict"),
            _role("threat_reveal", ["threat_reveal"], "medium", "threat", "show incoming threat"),
            _role("defender_action", ["action_medium"], "medium", "defender or protagonist", "show counter action"),
            _role("impact_insert", ["impact_insert"], "insert_detail", "impact detail", "land cause/effect"),
            _role("reaction_closeup", ["reaction_closeup"], "close_up", "affected subject", "land reaction"),
            _role("handoff_action", ["handoff_action"], "medium", "moving subject", "carry motion onward"),
            _role("reverse_action", ["reverse_action"], "medium", "opposing subject", "show reverse angle response"),
            _role("aftermath_wide", ["aftermath_wide"], "wide", "aftermath geography", "show changed positions"),
        ],
        "reveal_wonder": [
            _role("approach_medium", ["approach_medium"], "medium", "discovering subject", "delay information"),
            _role("partial_reveal", ["partial_reveal"], "close_up", "partially seen wonder", "tease detail"),
            _role("reveal_wide", ["reveal_wide"], "wide", "revealed subject/environment", "show full reveal"),
            _role("scale_proof_wide", ["scale_proof_wide"], "wide", "subject against scale reference", "prove scale"),
            _role("reaction_closeup", ["reaction_closeup"], "close_up", "witness", "show wonder/fear"),
            _role("subject_pov", ["subject_pov"], "medium", "witness POV", "make reveal subjective"),
            _role("insert_detail", ["insert_detail"], "insert_detail", "reveal detail", "show important detail"),
        ],
        "object_or_magic_business": [
            _role("task_medium", ["task_medium"], "medium", "subject performing task", "set up the action"),
            _role("hands_insert", ["hands_insert"], "insert_detail", "hands and object", "show mechanics"),
            _role("object_insert", ["object_insert"], "insert_detail", "object", "show important prop"),
            _role("result_medium", ["result_medium"], "medium", "resulting action", "show outcome"),
            _role("process_detail", ["process_detail"], "insert_detail", "process or magic detail", "show transformation"),
            _role("reaction_closeup", ["reaction_closeup"], "close_up", "observer", "show response"),
            _role("consequence_handoff", ["handoff_medium"], "medium", "changed object or subject", "hand off consequence"),
        ],
        "movement_travel": [
            _role("travel_wide", ["travel_wide"], "wide", "traveling subject or group", "show route geography"),
            _role("tracking_group", ["tracking_group"], "medium", "moving subject or group", "show travel rhythm"),
            _role("landmark_cutaway", ["landmark_cutaway"], "wide", "landmark or path", "mark progress"),
            _role("fatigue_reaction", ["fatigue_reaction"], "close_up", "traveler", "show emotional/physical state"),
            _role("path_insert", ["path_insert"], "insert_detail", "feet/path detail", "show passage"),
            _role("transition_wide", ["transition_wide"], "wide", "route ahead", "handoff to next location"),
        ],
        "reaction_emotion": [
            _role("reaction_closeup", ["reaction_closeup"], "close_up", "reacting subject", "land emotional turn"),
            _role("reverse_cause", ["subject_pov", "cutaway"], "medium", "thing being reacted to", "show cause of reaction"),
            _role("closing_reaction", ["closing_reaction"], "close_up", "changed subject", "show new state"),
            _role("handoff_medium", ["handoff_medium"], "medium", "reacting subject", "handoff to action"),
        ],
        "transition_handoff": [
            _role("handoff_medium", ["handoff_medium"], "medium", "handoff subject", "bridge to next beat"),
            _role("transition_wide", ["transition_wide"], "wide", "environment or group", "show movement between beats"),
            _role("insert_detail", ["insert_detail"], "insert_detail", "transition detail", "mark continuity detail"),
        ],
    }


def _role(role: str, shot_types: list[str], preferred_size: str, subject_logic: str, purpose: str, *, optional: bool = False) -> CoverageRole:
    lo, hi = (5.0, 8.0)
    return CoverageRole(role, shot_types, preferred_size, subject_logic, purpose, lo, hi, optional)


def _planned_shots_by_beat(planned: list[dict[str, Any]], beats: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    mapping: dict[str, list[dict[str, Any]]] = {str(beat["beat_id"]): [] for beat in beats}
    beat_ids = list(mapping)
    for index, item in enumerate(planned):
        explicit = str(item.get("beat_id", "") or item.get("beat_ids", "")).strip().upper()
        target = explicit if explicit in mapping else beat_ids[min(index, len(beat_ids) - 1)] if beat_ids else "BT001"
        mapping.setdefault(target, []).append(item)
    return mapping


def _seed_shot_type(seed: dict[str, Any]) -> str:
    for key in ("shot_type", "planned_shot_type", "coverage_role"):
        value = str(seed.get(key, "")).strip().lower()
        if value:
            return value
    return ""


def _classify_importance(beat: dict[str, Any], scene_contract: dict[str, Any], text: str, beat_type: str) -> str:
    priority = " ".join(str(beat.get(key, "")) for key in ("coverage_priority", "importance", "dramatic_importance")).lower()
    scene_text = _scene_text(scene_contract)
    combined = f"{text} {priority} {scene_text}"
    if _has_any(combined, "set piece", "set-piece", "climax", "battle", "ceremony", "ritual", "musical"):
        return "set_piece"
    if _has_any(priority, "major", "high", "critical") or _has_any(combined, "decides", "reveal", "reveals", "death", "betray", "rescues", "ultimatum"):
        return "major"
    if beat_type in {"movement_travel", "transition_handoff"} and not _has_any(combined, "danger", "lost", "pursued", "major"):
        return "minor"
    if _has_any(priority, "minor", "low", "connective"):
        return "minor"
    return "normal"


def _continuity_purpose(role: str, index: int, count: int) -> str:
    if index == 0:
        return "inherits the previous beat state and orients this beat"
    if index == count - 1:
        return "hands off the changed state to the next shot or beat"
    if "reaction" in role:
        return "captures response that motivates the next cut"
    if "insert" in role or "detail" in role:
        return "isolates visible detail for continuity"
    return "continues the beat action with a clear edit point"


def _scene_text(scene_contract: dict[str, Any]) -> str:
    values: list[str] = []
    for key in ("scene_title", "summary", "production_intent", "emotional_arc", "dominant_action_line"):
        values.append(str(scene_contract.get(key, "")))
    for key in ("visual_coverage_families", "scene_spatial_layout", "character_spatial_map"):
        value = scene_contract.get(key, [])
        if isinstance(value, list):
            values.extend(str(item) for item in value)
        else:
            values.append(str(value))
    return " ".join(values).lower()


def _beat_text(beat: dict[str, Any], scene_contract: dict[str, Any]) -> str:
    values = [
        str(beat.get("summary", "")),
        str(beat.get("markdown", "")),
        str(beat.get("action_start", "")),
        str(beat.get("action_end", "")),
        str(beat.get("blocking_hint", "")),
        str(beat.get("coverage_hint", "")),
        str(beat.get("coverage_priority", "")),
    ]
    return " ".join(values).lower()


def _subjects(beat: dict[str, Any]) -> list[str]:
    subjects: list[str] = []
    for key in ("active_subjects", "passive_subjects"):
        value = beat.get(key, [])
        if isinstance(value, list):
            subjects.extend(str(item).strip() for item in value if str(item).strip())
        elif str(value).strip():
            subjects.extend(part.strip() for part in re.split(r",|;", str(value)) if part.strip())
    seen: set[str] = set()
    ordered: list[str] = []
    for subject in subjects:
        key = subject.lower()
        if key not in seen:
            seen.add(key)
            ordered.append(subject)
    return ordered


def _has_any(text: str, *needles: str) -> bool:
    return any(needle in text for needle in needles)
