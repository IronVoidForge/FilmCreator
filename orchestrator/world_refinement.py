from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from .common import ensure_dir, repo_relative
from .lmstudio_client import LMStudioClient, LMStudioError
from .scaffold import create_project
from .settings import load_runtime_settings
from .world_global import (
    global_character_directory_path,
    global_character_registry_path,
    global_environment_directory_path,
    global_environment_registry_path,
)


RefineAction = Literal[
    "keep_separate",
    "merge_into_existing",
    "rename_canonical",
    "retype_entity",
    "mark_provisional",
    "flag_for_human_review",
]


_WEAK_CHARACTER_NAMES = {
    "narrator",
    "narrator_main",
    "narrator_ch002",
    "protagonist",
    "prisoner",
    "prisoner_ch008",
    "chieftain",
    "martian_leader",
    "watch_dog",
}

_CHARACTER_ALLOWED_KINDS = {
    "individual",
    "group",
    "provisional_role",
}

_ENVIRONMENT_ALLOWED_KINDS = {
    "environment",
    "sub_location",
    "building",
    "city",
    "plaza",
    "landform",
}

_CHAPTER_SUFFIX_RE = re.compile(r"_ch\d{3}$", re.IGNORECASE)
_MAIN_SUFFIX_RE = re.compile(r"_main$", re.IGNORECASE)
_TRAILING_NUMERIC_RE = re.compile(r"_\d{3}$", re.IGNORECASE)
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
_CHAPTER_ID_RE = re.compile(r"^CH(\d{3})$", re.IGNORECASE)


@dataclass(frozen=True)
class RefinementCandidate:
    entity_type: Literal["character", "environment"]
    subject_ids: list[str]
    reason: str
    heuristic_score: int
    evidence: dict

    def to_dict(self) -> dict:
        return {
            "entity_type": self.entity_type,
            "subject_ids": self.subject_ids,
            "reason": self.reason,
            "heuristic_score": self.heuristic_score,
            "evidence": self.evidence,
        }


@dataclass(frozen=True)
class RefinementDecision:
    entity_type: Literal["character", "environment"]
    subject_ids: list[str]
    action: RefineAction
    target_id: str | None
    new_canonical_id: str | None
    new_entity_kind: str | None
    reason: str
    confidence: Literal["low", "medium", "high"]
    requires_human_review: bool

    def to_dict(self) -> dict:
        return {
            "entity_type": self.entity_type,
            "subject_ids": self.subject_ids,
            "action": self.action,
            "target_id": self.target_id,
            "new_canonical_id": self.new_canonical_id,
            "new_entity_kind": self.new_entity_kind,
            "reason": self.reason,
            "confidence": self.confidence,
            "requires_human_review": self.requires_human_review,
        }


@dataclass(frozen=True)
class RefinementSummary:
    project_slug: str
    written_files: list[str]
    candidate_count: int
    comparison_count: int
    decision_count: int
    applied_count: int
    human_review_count: int
    warnings: list[str]

    def to_dict(self) -> dict:
        return {
            "project_slug": self.project_slug,
            "written_files": self.written_files,
            "candidate_count": self.candidate_count,
            "comparison_count": self.comparison_count,
            "decision_count": self.decision_count,
            "applied_count": self.applied_count,
            "human_review_count": self.human_review_count,
            "warnings": self.warnings,
        }


class RefinementDecisionError(RuntimeError):
    def __init__(self, message: str, *, retriable: bool = False) -> None:
        super().__init__(message)
        self.retriable = retriable


class WorldIdentityRefiner:
    def __init__(self, *, project_slug: str) -> None:
        self.project_slug = project_slug
        self.project_dir = create_project(project_slug)
        self.refinement_dir = self.project_dir / "02_story_analysis" / "world" / "refinement"
        ensure_dir(self.refinement_dir)

        self.character_registry_path = global_character_registry_path(project_slug)
        self.environment_registry_path = global_environment_registry_path(project_slug)
        self.character_directory_path = global_character_directory_path(project_slug)
        self.environment_directory_path = global_environment_directory_path(project_slug)

        self.character_registry = self._load_json(self.character_registry_path)
        self.environment_registry = self._load_json(self.environment_registry_path)
        self.character_directory = self._load_json(self.character_directory_path)
        self.environment_directory = self._load_json(self.environment_directory_path)

        self._settings = None
        self._client: LMStudioClient | None = None

    def run(self, *, use_llm: bool = True, apply_changes: bool = True) -> RefinementSummary:
        warnings: list[str] = []

        candidates, comparison_count = self._generate_candidates()
        decisions: list[RefinementDecision] = []

        for candidate in candidates:
            if use_llm:
                try:
                    decision = self._classify_candidate_with_llm(candidate)
                except Exception as exc:  # noqa: BLE001
                    warnings.append(
                        f"LLM classification failed for {candidate.subject_ids}: {exc}. Falling back to human review."
                    )
                    decision = self._force_human_review(candidate, f"LLM classification failed: {exc}")
            else:
                decision = self._force_human_review(candidate, "LLM disabled for this refinement run.")

            validated_decision = self._validate_decision(candidate, decision)
            decisions.append(validated_decision)

        applied_count = 0
        human_review_count = sum(1 for decision in decisions if decision.requires_human_review)

        if apply_changes:
            for decision in decisions:
                if decision.requires_human_review:
                    continue
                if self._apply_decision(decision, warnings=warnings):
                    applied_count += 1

            self._write_json(self.character_registry_path, self.character_registry)
            self._write_json(self.environment_registry_path, self.environment_registry)
            self._rebuild_directories()
            self._write_json(self.character_directory_path, self.character_directory)
            self._write_json(self.environment_directory_path, self.environment_directory)

        candidates_path = self.refinement_dir / "REFINEMENT_CANDIDATES.json"
        decisions_path = self.refinement_dir / "REFINEMENT_DECISIONS.json"
        result_path = self.refinement_dir / "REFINEMENT_RESULT.json"
        report_path = self.refinement_dir / "REFINEMENT_REPORT.md"

        self._write_json(candidates_path, [candidate.to_dict() for candidate in candidates])
        self._write_json(decisions_path, [decision.to_dict() for decision in decisions])
        self._write_json(
            result_path,
            {
                "project_slug": self.project_slug,
                "candidate_count": len(candidates),
                "comparison_count": comparison_count,
                "decision_count": len(decisions),
                "applied_count": applied_count,
                "human_review_count": human_review_count,
                "warnings": warnings,
                "files": [
                    repo_relative(candidates_path),
                    repo_relative(decisions_path),
                    repo_relative(result_path),
                    repo_relative(report_path),
                ]
                + (
                    [
                        repo_relative(self.character_registry_path),
                        repo_relative(self.environment_registry_path),
                        repo_relative(self.character_directory_path),
                        repo_relative(self.environment_directory_path),
                    ]
                    if apply_changes
                    else []
                ),
            },
        )
        report_path.write_text(
            self._build_report(candidates=candidates, decisions=decisions, warnings=warnings),
            encoding="utf-8",
        )

        written_files = [
            repo_relative(candidates_path),
            repo_relative(decisions_path),
            repo_relative(result_path),
            repo_relative(report_path),
        ]
        if apply_changes:
            written_files.extend(
                [
                    repo_relative(self.character_registry_path),
                    repo_relative(self.environment_registry_path),
                    repo_relative(self.character_directory_path),
                    repo_relative(self.environment_directory_path),
                ]
            )

        return RefinementSummary(
            project_slug=self.project_slug,
            written_files=written_files,
            candidate_count=len(candidates),
            comparison_count=comparison_count,
            decision_count=len(decisions),
            applied_count=applied_count,
            human_review_count=human_review_count,
            warnings=warnings,
        )

    def _generate_candidates(self) -> tuple[list[RefinementCandidate], int]:
        pair_candidates: list[RefinementCandidate] = []
        seen_keys: set[tuple[str, tuple[str, ...]]] = set()

        character_ids = sorted(self.character_registry.keys())
        for index, left_id in enumerate(character_ids):
            for right_id in character_ids[index + 1 :]:
                candidate = self._maybe_character_candidate(left_id, right_id)
                if candidate is None:
                    continue
                key = (candidate.entity_type, tuple(sorted(candidate.subject_ids)))
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                pair_candidates.append(candidate)

        environment_ids = sorted(self.environment_registry.keys())
        for index, left_id in enumerate(environment_ids):
            for right_id in environment_ids[index + 1 :]:
                candidate = self._maybe_environment_candidate(left_id, right_id)
                if candidate is None:
                    continue
                key = (candidate.entity_type, tuple(sorted(candidate.subject_ids)))
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                pair_candidates.append(candidate)

        clusters = self._cluster_pair_candidates(pair_candidates)
        clusters.sort(key=lambda item: (-item.heuristic_score, item.entity_type, item.subject_ids))
        return clusters, len(pair_candidates)

    def _maybe_character_candidate(self, left_id: str, right_id: str) -> RefinementCandidate | None:
        left = self.character_registry[left_id]
        right = self.character_registry[right_id]

        score = 0
        reasons: list[str] = []

        left_root = self._root_identity_token(left_id)
        right_root = self._root_identity_token(right_id)
        left_norm = self._normalize_token(left_id)
        right_norm = self._normalize_token(right_id)
        overlap = self._alias_overlap(left, right)
        strong_overlap = bool(overlap) or left_root == right_root or self._has_prefix_relationship(left_norm, right_norm)

        if not strong_overlap:
            return None

        if left_root == right_root and left_id != right_id:
            score += 5
            reasons.append("normalized identity roots match")

        if self._has_prefix_relationship(left_norm, right_norm):
            score += 4
            reasons.append("chapter suffix or short title variant detected")

        if overlap:
            score += 4
            reasons.append(f"alias overlap: {sorted(overlap)}")

        if self._is_weak_character_name(left_id) or self._is_weak_character_name(right_id):
            score += 2
            reasons.append("one or both ids are weak/generic character names")

        if left.get("entity_kind") != right.get("entity_kind"):
            score += 2
            reasons.append(
                f"entity kind drift detected ({left.get('entity_kind')} vs {right.get('entity_kind')})"
            )

        if score < 4:
            return None

        evidence = {
            "left": self._compact_entry_summary(left_id, left),
            "right": self._compact_entry_summary(right_id, right),
        }
        return RefinementCandidate(
            entity_type="character",
            subject_ids=[left_id, right_id],
            reason="; ".join(reasons),
            heuristic_score=score,
            evidence=evidence,
        )

    def _maybe_environment_candidate(self, left_id: str, right_id: str) -> RefinementCandidate | None:
        left = self.environment_registry[left_id]
        right = self.environment_registry[right_id]

        score = 0
        reasons: list[str] = []

        left_root = self._root_identity_token(left_id)
        right_root = self._root_identity_token(right_id)
        left_norm = self._normalize_token(left_id)
        right_norm = self._normalize_token(right_id)
        overlap = self._alias_overlap(left, right)
        strong_overlap = bool(overlap) or left_root == right_root or self._has_prefix_relationship(left_norm, right_norm)

        if not strong_overlap:
            return None

        if left_root == right_root and left_id != right_id:
            score += 5
            reasons.append("normalized environment roots match")

        if self._has_prefix_relationship(left_norm, right_norm):
            score += 4
            reasons.append("chapter suffix or short title variant detected")

        if overlap:
            score += 3
            reasons.append(f"alias overlap: {sorted(overlap)}")

        if left.get("entity_kind") != right.get("entity_kind"):
            score += 1
            reasons.append(
                f"environment kind drift detected ({left.get('entity_kind')} vs {right.get('entity_kind')})"
            )

        if score < 4:
            return None

        evidence = {
            "left": self._compact_entry_summary(left_id, left),
            "right": self._compact_entry_summary(right_id, right),
        }
        return RefinementCandidate(
            entity_type="environment",
            subject_ids=[left_id, right_id],
            reason="; ".join(reasons),
            heuristic_score=score,
            evidence=evidence,
        )

    def _cluster_pair_candidates(self, pair_candidates: list[RefinementCandidate]) -> list[RefinementCandidate]:
        clusters: dict[str, set[str]] = {}
        parents: dict[str, str] = {}
        entity_types: dict[str, Literal["character", "environment"]] = {}
        all_ids: set[str] = set()

        def find(item: str) -> str:
            parents.setdefault(item, item)
            if parents[item] != item:
                parents[item] = find(parents[item])
            return parents[item]

        def union(left: str, right: str) -> None:
            left_root = find(left)
            right_root = find(right)
            if left_root != right_root:
                parents[right_root] = left_root

        for candidate in pair_candidates:
            left_id, right_id = candidate.subject_ids
            all_ids.update(candidate.subject_ids)
            entity_types[left_id] = candidate.entity_type
            entity_types[right_id] = candidate.entity_type
            union(left_id, right_id)

        for item in all_ids:
            root = find(item)
            clusters.setdefault(root, set()).add(item)

        clustered_candidates: list[RefinementCandidate] = []
        for root, members in clusters.items():
            if len(members) < 2:
                continue
            entity_type = entity_types[next(iter(members))]
            member_list = sorted(members)
            member_summaries = [self._cluster_member_summary(member_id, entity_type) for member_id in member_list]
            edge_candidates = [
                candidate
                for candidate in pair_candidates
                if set(candidate.subject_ids).issubset(members)
            ]
            ranked_members = self._rank_cluster_members(member_list, entity_type)
            representative = ranked_members[0]["canonical_id"] if ranked_members else member_list[0]
            evidence = {
                "cluster_root": root,
                "member_summaries": member_summaries,
                "pairwise_edges": [
                    {
                        "subject_ids": candidate.subject_ids,
                        "reason": candidate.reason,
                        "heuristic_score": candidate.heuristic_score,
                    }
                    for candidate in sorted(
                        edge_candidates,
                        key=lambda item: (-item.heuristic_score, item.subject_ids),
                    )
                ],
                "ranked_members": ranked_members,
                "preferred_target_id": representative,
            }
            reason = self._summarize_cluster_reason(edge_candidates, ranked_members)
            score = sum(candidate.heuristic_score for candidate in edge_candidates) + len(members) * 5
            clustered_candidates.append(
                RefinementCandidate(
                    entity_type=entity_type,
                    subject_ids=member_list,
                    reason=reason,
                    heuristic_score=score,
                    evidence=evidence,
                )
            )

        return clustered_candidates

    def _cluster_member_summary(self, canonical_id: str, entity_type: Literal["character", "environment"]) -> dict:
        registry = self.character_registry if entity_type == "character" else self.environment_registry
        entry = registry.get(canonical_id, {})
        description_layers = entry.get("description_layers", {})
        return {
            "canonical_id": canonical_id,
            "display_name": entry.get("display_name"),
            "status": entry.get("status"),
            "entity_kind": entry.get("entity_kind"),
            "aliases": entry.get("aliases", []),
            "first_seen_chapter": entry.get("first_seen_chapter"),
            "last_seen_chapter": entry.get("last_seen_chapter"),
            "chapter_mentions": entry.get("chapter_mentions", []),
            "source_count": len(entry.get("sources", [])),
            "weak_name": self._is_weak_character_name(canonical_id) if entity_type == "character" else False,
            "canonical_rank_score": self._rank_entity_candidate(canonical_id, entry, entity_type),
            "stable_canonical_descriptions": description_layers.get("stable_canonical", []),
        }

    def _rank_cluster_members(self, member_ids: list[str], entity_type: Literal["character", "environment"]) -> list[dict]:
        ranked = [
            self._cluster_member_summary(member_id, entity_type)
            for member_id in member_ids
        ]
        shortest_normalized_length = min(len(self._normalize_token(member_id)) for member_id in member_ids)
        prefix_candidates = [
            member_id
            for member_id in member_ids
            if any(
                other_id != member_id
                and self._normalize_token(other_id).startswith(self._normalize_token(member_id))
                for other_id in member_ids
            )
        ]
        for item in ranked:
            if len(self._normalize_token(item["canonical_id"])) == shortest_normalized_length:
                item["canonical_rank_score"] += 12
            if item["canonical_id"] in prefix_candidates:
                item["canonical_rank_score"] += 30
        ranked.sort(key=lambda item: (-item["canonical_rank_score"], item["canonical_id"]))
        return ranked

    def _rank_entity_candidate(self, canonical_id: str, entry: dict, entity_type: Literal["character", "environment"]) -> int:
        score = 0
        display_name = self._normalize_token(entry.get("display_name", canonical_id))
        canonical_token = self._normalize_token(canonical_id)
        aliases = {self._normalize_token(alias) for alias in entry.get("aliases", [])}
        aliases.discard("")

        if canonical_token == display_name:
            score += 10
        if entity_type == "character":
            if entry.get("status") == "canonical":
                score += 25
            if entry.get("entity_kind") != "provisional_role":
                score += 8
            if self._is_weak_character_name(canonical_id):
                score -= 20
        else:
            if entry.get("status") == "canonical":
                score += 18
            if entry.get("entity_kind") == "environment":
                score += 8
        if self._chapter_suffix_match(canonical_id):
            score -= 12
        if self._main_suffix_match(canonical_id):
            score -= 6
        score += min(len(entry.get("chapter_mentions", [])), 8) * 3
        score += min(len(entry.get("sources", [])), 8) * 2
        score += min(len(entry.get("description_layers", {}).get("stable_canonical", [])), 6) * 2
        score += min(len(aliases), 5)
        return score

    def _summarize_cluster_reason(
        self,
        pair_candidates: list[RefinementCandidate],
        ranked_members: list[dict],
    ) -> str:
        if not pair_candidates:
            return "Clustered from shared identity overlap."
        reasons: list[str] = []
        for candidate in sorted(pair_candidates, key=lambda item: (-item.heuristic_score, item.subject_ids)):
            for fragment in candidate.reason.split("; "):
                if fragment and fragment not in reasons:
                    reasons.append(fragment)
        if ranked_members:
            top = ranked_members[0]
            reasons.append(f"preferred target ranked as {top['canonical_id']} (score {top['canonical_rank_score']})")
        return "; ".join(reasons[:5])

    def _chapter_suffix_match(self, value: str) -> bool:
        return bool(_CHAPTER_SUFFIX_RE.search(value))

    def _main_suffix_match(self, value: str) -> bool:
        return bool(_MAIN_SUFFIX_RE.search(value))

    def _classify_candidate_with_llm(self, candidate: RefinementCandidate) -> RefinementDecision:
        client = self._get_client()
        system_prompt = (
            "You are FilmCreator's world-identity refinement classifier. "
            "Choose only from the allowed actions and return valid JSON only. "
            "Do not invent entities or rewrite the registry. If uncertain, flag_for_human_review."
        )
        last_error: Exception | None = None
        for compact in (False, True):
            result = client.chat_completion_result(
                system_prompt=system_prompt,
                user_prompt=self._build_classification_prompt(candidate, compact=compact),
                temperature=0.0,
            )
            if not result.is_success:
                last_error = LMStudioError(result.error_message or "LM Studio returned an unusable response.")
                continue

            try:
                payload = self._parse_json_object(result.text)
            except LMStudioError as exc:
                last_error = exc
                continue

            try:
                decision = self._decision_from_payload(payload)
                return self._validate_decision(candidate, decision)
            except RefinementDecisionError as exc:
                last_error = exc
                if exc.retriable and not compact:
                    continue
                return self._force_human_review(candidate, str(exc))

        raise LMStudioError(str(last_error) if last_error else "LM Studio returned an unusable response.")

    def _build_classification_prompt(self, candidate: RefinementCandidate, *, compact: bool) -> str:
        allowed_actions = [
            "keep_separate",
            "merge_into_existing",
            "rename_canonical",
            "retype_entity",
            "mark_provisional",
            "flag_for_human_review",
        ]
        payload: dict[str, object] = {
            "task": "classify_identity_refinement_candidate",
            "allowed_actions": allowed_actions,
            "candidate": candidate.to_dict(),
            "allowed_target_ids": [item["canonical_id"] for item in candidate.evidence.get("ranked_members", [])[:3]],
            "output_schema": {
                "entity_type": "character|environment",
                "subject_ids": ["id1", "id2"],
                "action": "allowed action",
                "target_id": "existing target id or null",
                "new_canonical_id": "new id or null",
                "new_entity_kind": "new kind or null",
                "reason": "short reason",
                "confidence": "low|medium|high",
                "requires_human_review": "bool",
            },
        }
        if compact:
            ranked_members = candidate.evidence.get("ranked_members", [])
            payload["mode"] = "compact_retry"
            payload["candidate"] = {
                "entity_type": candidate.entity_type,
                "subject_ids": candidate.subject_ids,
                "reason": candidate.reason,
                "heuristic_score": candidate.heuristic_score,
                "preferred_target_id": candidate.evidence.get("preferred_target_id"),
                "ranked_members": ranked_members[:3],
                "pairwise_edges": candidate.evidence.get("pairwise_edges", [])[:4],
            }
            payload["allowed_target_ids"] = [item["canonical_id"] for item in ranked_members[:3]]
        return json.dumps(payload, indent=2)

    def _decision_from_payload(self, payload: dict) -> RefinementDecision:
        entity_type = payload["entity_type"]
        subject_ids = list(payload["subject_ids"])
        action = payload["action"]
        target_id = payload.get("target_id")
        new_canonical_id = payload.get("new_canonical_id")
        new_entity_kind = payload.get("new_entity_kind")
        reason = str(payload.get("reason", "")).strip()
        confidence = payload.get("confidence", "low")
        requires_human_review = bool(payload.get("requires_human_review", False))
        return RefinementDecision(
            entity_type=entity_type,
            subject_ids=subject_ids,
            action=action,
            target_id=target_id,
            new_canonical_id=new_canonical_id,
            new_entity_kind=new_entity_kind,
            reason=reason,
            confidence=confidence,
            requires_human_review=requires_human_review,
        )

    def _validate_decision(
        self,
        candidate: RefinementCandidate,
        decision: RefinementDecision,
    ) -> RefinementDecision:
        allowed_actions: set[str] = {
            "keep_separate",
            "merge_into_existing",
            "rename_canonical",
            "retype_entity",
            "mark_provisional",
            "flag_for_human_review",
        }
        if decision.action not in allowed_actions:
            raise RefinementDecisionError(f"Invalid action '{decision.action}'.")

        if sorted(decision.subject_ids) != sorted(candidate.subject_ids):
            raise RefinementDecisionError("Decision subject ids did not match candidate ids.", retriable=True)

        registry = self.character_registry if candidate.entity_type == "character" else self.environment_registry
        for subject_id in candidate.subject_ids:
            if subject_id not in registry:
                raise RefinementDecisionError(f"Unknown subject id '{subject_id}'.", retriable=True)

        if decision.action == "keep_separate":
            return decision

        if decision.action == "flag_for_human_review":
            return self._force_human_review(candidate, decision.reason or "LLM requested human review.")

        if decision.confidence == "low":
            return self._force_human_review(candidate, "Low-confidence structural change blocked.")

        if decision.action == "merge_into_existing":
            if not decision.target_id or decision.target_id not in registry:
                raise RefinementDecisionError("Merge target missing or unknown.", retriable=True)
            if self._is_resolved_stub(registry[decision.target_id]):
                raise RefinementDecisionError("Merge target is already resolved into another entity.", retriable=True)
            ranked_members = [item["canonical_id"] for item in candidate.evidence.get("ranked_members", [])]
            if decision.target_id not in candidate.subject_ids:
                raise RefinementDecisionError("Merge target is not a member of the cluster.", retriable=True)
            if ranked_members and decision.target_id not in ranked_members[:3]:
                raise RefinementDecisionError(
                    f"Merge target '{decision.target_id}' is not among the top-ranked cluster members.",
                    retriable=True,
                )

        if decision.action == "rename_canonical":
            if not decision.new_canonical_id:
                raise RefinementDecisionError("Rename decision missing new_canonical_id.", retriable=True)
            if not self._is_valid_asset_id(decision.new_canonical_id):
                raise RefinementDecisionError("Rename target is not a valid asset id.", retriable=True)
            if decision.new_canonical_id in registry and decision.new_canonical_id not in candidate.subject_ids:
                raise RefinementDecisionError("Rename target already exists in the registry.", retriable=True)

        if decision.action == "retype_entity":
            if candidate.entity_type == "character":
                if decision.new_entity_kind not in _CHARACTER_ALLOWED_KINDS:
                    raise RefinementDecisionError("Invalid character entity kind.", retriable=True)
            else:
                if decision.new_entity_kind not in _ENVIRONMENT_ALLOWED_KINDS:
                    raise RefinementDecisionError("Invalid environment entity kind.", retriable=True)
            if not decision.new_entity_kind:
                raise RefinementDecisionError("Retype decision missing new_entity_kind.", retriable=True)

        if decision.action == "mark_provisional":
            if candidate.entity_type != "character":
                raise RefinementDecisionError("Environment provisional marking is not supported.")
            if not any(self._is_weak_character_name(subject_id) for subject_id in candidate.subject_ids):
                raise RefinementDecisionError("Provisional marking requires a weak character name.")

        return decision

    def _apply_decision(self, decision: RefinementDecision, *, warnings: list[str]) -> bool:
        if decision.action in {"keep_separate", "flag_for_human_review"}:
            return False

        if decision.entity_type == "character":
            registry = self.character_registry
            directory = self.character_directory
        else:
            registry = self.environment_registry
            directory = self.environment_directory

        changed = False

        if decision.action == "merge_into_existing":
            target_id = decision.target_id
            assert target_id is not None
            if target_id not in registry:
                warnings.append(f"Merge target '{target_id}' no longer exists.")
                return False
            for subject_id in decision.subject_ids:
                if subject_id == target_id:
                    continue
                if subject_id not in registry:
                    continue
                self._merge_entry_into_target(
                    registry=registry,
                    subject_id=subject_id,
                    target_id=target_id,
                    entity_type=decision.entity_type,
                    reason=decision.reason,
                )
                self._replace_references_in_registry(
                    registry,
                    old_id=subject_id,
                    new_id=target_id,
                    entity_type=decision.entity_type,
                )
                changed = True

        elif decision.action == "rename_canonical":
            new_id = decision.new_canonical_id
            assert new_id is not None
            subject_id = decision.subject_ids[0]
            changed = self._rename_entry(
                registry=registry,
                old_id=subject_id,
                new_id=new_id,
                entity_type=decision.entity_type,
                reason=decision.reason,
            )
            if changed:
                self._replace_references_in_registry(
                    registry,
                    old_id=subject_id,
                    new_id=new_id,
                    entity_type=decision.entity_type,
                )

        elif decision.action == "retype_entity":
            new_kind = decision.new_entity_kind
            assert new_kind is not None
            for subject_id in decision.subject_ids:
                entry = registry.get(subject_id)
                if entry is None:
                    continue
                old_kind = entry.get("entity_kind")
                if old_kind == new_kind:
                    continue
                entry["entity_kind"] = new_kind
                self._append_refinement_resolution_history(
                    entry,
                    action="retyped_entity",
                    reason=decision.reason,
                    target=None,
                )
                changed = True

        elif decision.action == "mark_provisional":
            for subject_id in decision.subject_ids:
                entry = registry.get(subject_id)
                if entry is None:
                    continue
                if decision.entity_type != "character":
                    continue
                if entry.get("status") != "provisional":
                    entry["status"] = "provisional"
                    entry["entity_kind"] = "provisional_role"
                    self._append_refinement_resolution_history(
                        entry,
                        action="marked_provisional",
                        reason=decision.reason,
                        target=None,
                    )
                    changed = True

        else:
            warnings.append(f"Unhandled decision action: {decision.action}")
            return False

        if changed:
            self._rebuild_directory_for_registry(registry, directory, decision.entity_type)
        return changed

    def _merge_entry_into_target(
        self,
        *,
        registry: dict,
        subject_id: str,
        target_id: str,
        entity_type: str,
        reason: str,
    ) -> None:
        subject = registry.get(subject_id)
        target = registry.get(target_id)
        if subject is None or target is None:
            return

        self._append_alias_record(target, alias=subject_id)
        for alias in subject.get("aliases", []):
            self._append_alias_record(target, alias=alias)

        for item in subject.get("alias_history", []):
            if item not in target.setdefault("alias_history", []):
                target["alias_history"].append(item)

        for source in subject.get("sources", []):
            if source not in target.setdefault("sources", []):
                target["sources"].append(source)

        for item in subject.get("source_history", []):
            if item not in target.setdefault("source_history", []):
                target["source_history"].append(item)

        for chapter_id in subject.get("chapter_mentions", []):
            if chapter_id not in target.setdefault("chapter_mentions", []):
                target["chapter_mentions"].append(chapter_id)

        if entity_type == "character":
            for item in subject.get("open_questions", []):
                if item not in target.setdefault("open_questions", []):
                    target["open_questions"].append(item)
            if target.get("status") == "provisional" and subject.get("status") == "canonical":
                target["status"] = "canonical"
            if target.get("entity_kind") == "provisional_role" and subject.get("entity_kind") in {"individual", "group"}:
                target["entity_kind"] = subject["entity_kind"]
        else:
            for item in subject.get("state_notes", []):
                if item not in target.setdefault("state_notes", []):
                    target["state_notes"].append(item)
            if target.get("entity_kind") == "environment" and subject.get("entity_kind") != "environment":
                target["entity_kind"] = subject.get("entity_kind", target.get("entity_kind"))

        target_layers = target.setdefault(
            "description_layers",
            {"initial_extracted": [], "stable_canonical": [], "chapter_specific": {}},
        )
        subject_layers = subject.get("description_layers", {})

        for item in subject_layers.get("initial_extracted", []):
            if item not in target_layers.setdefault("initial_extracted", []):
                target_layers["initial_extracted"].append(item)

        for item in subject_layers.get("stable_canonical", []):
            if item not in target_layers.setdefault("stable_canonical", []):
                target_layers["stable_canonical"].append(item)

        for chapter_id, values in subject_layers.get("chapter_specific", {}).items():
            bucket = target_layers.setdefault("chapter_specific", {}).setdefault(chapter_id, [])
            for value in values:
                if value not in bucket:
                    bucket.append(value)

        first_seen = self._earliest_chapter([target.get("first_seen_chapter"), subject.get("first_seen_chapter")])
        if first_seen:
            target["first_seen_chapter"] = first_seen

        last_seen = self._latest_chapter([target.get("last_seen_chapter"), subject.get("last_seen_chapter")])
        if last_seen:
            target["last_seen_chapter"] = last_seen

        self._append_refinement_resolution_history(
            target,
            action="merged_into_target",
            reason=reason,
            target=target_id,
        )

        subject["status"] = "resolved_into"
        if entity_type == "character":
            subject["resolved_to"] = target_id
        self._append_refinement_resolution_history(
            subject,
            action="resolved_into",
            reason=reason,
            target=target_id,
        )

    def _rename_entry(
        self,
        *,
        registry: dict,
        old_id: str,
        new_id: str,
        entity_type: str,
        reason: str,
    ) -> bool:
        if old_id == new_id or new_id in registry:
            return False

        entry = registry.pop(old_id, None)
        if entry is None:
            return False

        self._append_alias_record(entry, alias=old_id)
        entry["canonical_id"] = new_id
        entry["display_name"] = new_id
        self._append_refinement_resolution_history(
            entry,
            action="renamed_canonical",
            reason=reason,
            target=new_id,
        )
        registry[new_id] = entry
        return True

    def _replace_references_in_registry(
        self,
        registry: dict,
        *,
        old_id: str,
        new_id: str,
        entity_type: str,
    ) -> None:
        for entry_id, entry in registry.items():
            if entity_type == "character":
                resolved_to = entry.get("resolved_to")
                if resolved_to == old_id:
                    entry["resolved_to"] = new_id
            else:
                parent_id = entry.get("parent_environment_id")
                if parent_id == old_id:
                    entry["parent_environment_id"] = new_id
                children = entry.get("children", [])
                updated_children = [new_id if child == old_id else child for child in children]
                if updated_children != children:
                    entry["children"] = updated_children

            if entry_id == new_id:
                continue
            self._append_alias_record(entry, alias=old_id)

    def _append_alias_record(self, entry: dict, *, alias: str) -> None:
        normalized = self._normalize_token(alias)
        if not normalized:
            return
        aliases = entry.setdefault("aliases", [])
        if normalized not in aliases:
            aliases.append(normalized)
        history_item = {
            "chapter_id": "REFINEMENT",
            "alias": normalized,
            "source": "world_refinement",
        }
        if history_item not in entry.setdefault("alias_history", []):
            entry["alias_history"].append(history_item)

    def _append_refinement_resolution_history(
        self,
        entry: dict,
        *,
        action: str,
        reason: str,
        target: str | None,
    ) -> None:
        item = {
            "chapter_id": "REFINEMENT",
            "action": action,
            "reason": reason,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }
        if target:
            item["target"] = target
        entry.setdefault("resolution_history", []).append(item)

    def _rebuild_directories(self) -> None:
        self._rebuild_directory_for_registry(self.character_registry, self.character_directory, "character")
        self._rebuild_directory_for_registry(self.environment_registry, self.environment_directory, "environment")

    def _rebuild_directory_for_registry(self, registry: dict, directory: dict, entity_type: str) -> None:
        directory.clear()
        for canonical_id, entry in sorted(registry.items()):
            payload = {
                "canonical_id": canonical_id,
                "status": entry.get("status", "canonical"),
                "entity_kind": entry.get("entity_kind", "individual" if entity_type == "character" else "environment"),
                "aliases": entry.get("aliases", []),
                "first_seen_chapter": entry.get("first_seen_chapter"),
                "last_seen_chapter": entry.get("last_seen_chapter"),
            }
            if entity_type == "character":
                payload["resolved_to"] = entry.get("resolved_to")
            else:
                payload["parent_environment_id"] = entry.get("parent_environment_id")
            directory[canonical_id] = payload

    def _build_report(
        self,
        *,
        candidates: list[RefinementCandidate],
        decisions: list[RefinementDecision],
        warnings: list[str],
    ) -> str:
        lines: list[str] = [
            "# World Refinement Report",
            "",
            f"- project_slug: {self.project_slug}",
            f"- generated_at_utc: {datetime.now(timezone.utc).isoformat()}",
            f"- candidate_count: {len(candidates)}",
            f"- comparison_count: {sum(len(candidate.evidence.get('pairwise_edges', [])) for candidate in candidates)}",
            f"- decision_count: {len(decisions)}",
            "",
            "## Decisions",
            "",
        ]
        for decision in decisions:
            lines.append(
                f"- {decision.entity_type} {decision.subject_ids} -> {decision.action} "
                f"(target={decision.target_id or ''}, new_id={decision.new_canonical_id or ''}, "
                f"new_kind={decision.new_entity_kind or ''}, confidence={decision.confidence}, "
                f"human_review={decision.requires_human_review})"
            )
            lines.append(f"  - reason: {decision.reason}")
        if warnings:
            lines.extend(["", "## Warnings", ""])
            for warning in warnings:
                lines.append(f"- {warning}")
        lines.append("")
        return "\n".join(lines)

    def _compact_entry_summary(self, canonical_id: str, entry: dict) -> dict:
        description_layers = entry.get("description_layers", {})
        return {
            "canonical_id": canonical_id,
            "display_name": entry.get("display_name"),
            "status": entry.get("status"),
            "entity_kind": entry.get("entity_kind"),
            "aliases": entry.get("aliases", []),
            "first_seen_chapter": entry.get("first_seen_chapter"),
            "last_seen_chapter": entry.get("last_seen_chapter"),
            "chapter_mentions": entry.get("chapter_mentions", []),
            "source_count": len(entry.get("sources", [])),
            "stable_canonical_descriptions": description_layers.get("stable_canonical", []),
        }

    def _alias_overlap(self, left: dict, right: dict) -> set[str]:
        left_tokens = set(self._normalized_aliases(left))
        right_tokens = set(self._normalized_aliases(right))
        return left_tokens & right_tokens

    def _normalized_aliases(self, entry: dict) -> list[str]:
        tokens = {
            self._normalize_token(entry.get("canonical_id", "")),
            self._normalize_token(entry.get("display_name", "")),
        }
        for alias in entry.get("aliases", []):
            tokens.add(self._normalize_token(alias))
        return [token for token in tokens if token]

    def _root_identity_token(self, value: str) -> str:
        token = self._normalize_token(value)
        token = _CHAPTER_SUFFIX_RE.sub("", token)
        token = _MAIN_SUFFIX_RE.sub("", token)
        token = _TRAILING_NUMERIC_RE.sub("", token)
        return token

    def _has_prefix_relationship(self, left: str, right: str) -> bool:
        if not left or not right or left == right:
            return False
        shorter, longer = sorted([left, right], key=len)
        return longer.startswith(f"{shorter}_") and len(longer) > len(shorter) + 1

    def _is_weak_character_name(self, value: str) -> bool:
        return self._normalize_token(value) in _WEAK_CHARACTER_NAMES

    def _normalize_token(self, value: str) -> str:
        return _NON_ALNUM_RE.sub("_", str(value).strip().lower()).strip("_")

    def _is_valid_asset_id(self, value: str) -> bool:
        return bool(re.fullmatch(r"[a-z0-9_]+", value))

    def _is_resolved_stub(self, entry: dict) -> bool:
        return str(entry.get("status", "")).strip() == "resolved_into"

    def _force_human_review(self, candidate: RefinementCandidate, reason: str) -> RefinementDecision:
        return RefinementDecision(
            entity_type=candidate.entity_type,
            subject_ids=candidate.subject_ids,
            action="flag_for_human_review",
            target_id=None,
            new_canonical_id=None,
            new_entity_kind=None,
            reason=reason,
            confidence="low",
            requires_human_review=True,
        )

    def _load_json(self, path: Path) -> dict:
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))

    def _write_json(self, path: Path, data: object) -> None:
        ensure_dir(path.parent)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def _get_client(self) -> LMStudioClient:
        if self._client is None:
            if self._settings is None:
                self._settings = load_runtime_settings()
            self._client = LMStudioClient(self._settings)
        return self._client

    def _parse_json_object(self, text: str) -> dict:
        stripped = text.strip()
        if stripped.startswith("```"):
            stripped = re.sub(r"^```(?:json)?\s*", "", stripped, flags=re.IGNORECASE)
            stripped = re.sub(r"\s*```$", "", stripped)
        start = stripped.find("{")
        end = stripped.rfind("}")
        if start == -1 or end == -1 or end < start:
            raise LMStudioError("LLM response did not contain a JSON object.")
        payload = stripped[start : end + 1]
        try:
            parsed = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise LMStudioError(f"LLM returned invalid JSON: {exc}") from exc
        if not isinstance(parsed, dict):
            raise LMStudioError("LLM response JSON must be an object.")
        return parsed

    def _earliest_chapter(self, chapter_ids: list[str | None]) -> str | None:
        chapters = [chapter_id for chapter_id in chapter_ids if chapter_id]
        if not chapters:
            return None
        return sorted(chapters, key=self._chapter_sort_key)[0]

    def _latest_chapter(self, chapter_ids: list[str | None]) -> str | None:
        chapters = [chapter_id for chapter_id in chapter_ids if chapter_id]
        if not chapters:
            return None
        return sorted(chapters, key=self._chapter_sort_key)[-1]

    def _chapter_sort_key(self, chapter_id: str) -> tuple[int, str]:
        match = _CHAPTER_ID_RE.fullmatch(chapter_id.strip())
        if match:
            return (int(match.group(1)), chapter_id)
        return (10**9, chapter_id)


def refine_world_identities(
    *,
    project_slug: str,
    use_llm: bool = True,
    apply_changes: bool = True,
) -> RefinementSummary:
    refiner = WorldIdentityRefiner(project_slug=project_slug)
    return refiner.run(use_llm=use_llm, apply_changes=apply_changes)
