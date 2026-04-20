from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

from ..common import read_json
from ..manifest_tools import extract_manifest_candidate_paths
from ..scaffold import promote_asset
from ..state import load_clip_state, path_to_manifest_value, record_review_batch, resolve_user_path


@dataclass(frozen=True)
class ReviewCandidate:
    index: int
    path: str
    name: str

    def to_dict(self) -> dict[str, object]:
        return {
            "index": self.index,
            "path": self.path,
            "name": self.name,
        }


def list_review_candidates(manifest_path: str | Path) -> list[ReviewCandidate]:
    manifest_file = resolve_user_path(str(manifest_path))
    if not manifest_file.exists():
        raise FileNotFoundError(f"Run manifest not found: {manifest_file}")

    manifest = read_json(manifest_file)
    candidate_paths = extract_manifest_candidate_paths(manifest)
    if not candidate_paths:
        raise ValueError(f"No candidate outputs were recorded in manifest: {manifest_file}")

    candidates: list[ReviewCandidate] = []
    for index, candidate_path in enumerate(candidate_paths, start=1):
        resolved = resolve_user_path(candidate_path)
        candidates.append(
            ReviewCandidate(
                index=index,
                path=path_to_manifest_value(resolved),
                name=resolved.name,
            )
        )
    return candidates


def review_candidates_summary(manifest_path: str | Path) -> dict[str, object]:
    manifest_file = resolve_user_path(str(manifest_path))
    candidates = list_review_candidates(manifest_file)
    return {
        "manifest_path": path_to_manifest_value(manifest_file),
        "candidate_count": len(candidates),
        "candidates": [candidate.to_dict() for candidate in candidates],
    }


def review_and_promote_batch(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    stage: str,
    manifest_path: str | Path,
    top_two_indexes: Sequence[int],
    primary_index: int,
    promotion_target: str,
    promotion_index: int = 1,
) -> dict[str, object]:
    candidates = list_review_candidates(manifest_path)
    if len(top_two_indexes) != 2:
        raise ValueError("Exactly two finalist indexes are required.")

    top_two = [_candidate_from_index(candidates, index) for index in top_two_indexes]
    if top_two[0].index == top_two[1].index:
        raise ValueError("The top two finalists must be different candidates.")

    primary_candidate = _candidate_from_index(candidates, primary_index)
    if primary_candidate.index not in {top_two[0].index, top_two[1].index}:
        raise ValueError("The primary winner must also be one of the top two finalists.")

    review = record_review_batch(
        project_slug,
        scene_id,
        clip_id,
        stage=stage,
        manifest_path=manifest_path,
        review_decision="approve",
        chosen_primary=primary_candidate.path,
        top_two=[candidate.path for candidate in top_two],
    )
    promoted_path = promote_asset(
        project_slug,
        primary_candidate.path,
        promotion_target,
        scene_id=scene_id,
        clip_id=clip_id,
        index=promotion_index,
    )

    clip_state = load_clip_state(project_slug, scene_id, clip_id)
    manifest_file = resolve_user_path(str(manifest_path))
    manifest = read_json(manifest_file)

    return {
        "manifest_path": path_to_manifest_value(manifest_file),
        "stage": stage,
        "promotion_target": promotion_target,
        "candidates": [candidate.to_dict() for candidate in candidates],
        "top_two": [candidate.to_dict() for candidate in top_two],
        "primary": primary_candidate.to_dict(),
        "review": review,
        "promoted_path": path_to_manifest_value(promoted_path),
        "clip_state": clip_state,
        "manifest": manifest,
    }


def interactive_review_and_promote_batch(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    stage: str,
    manifest_path: str | Path,
    promotion_target: str,
    promotion_index: int = 1,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> dict[str, object]:
    candidates = list_review_candidates(manifest_path)
    output_fn("")
    output_fn("Review candidates:")
    for candidate in candidates:
        output_fn(f"  {candidate.index}. {candidate.name}")
    output_fn("")

    top1 = _prompt_candidate_index(
        candidates,
        f"Choose the first finalist [1-{len(candidates)}]: ",
        input_fn=input_fn,
        output_fn=output_fn,
    )
    top2 = _prompt_candidate_index(
        candidates,
        f"Choose the second finalist [1-{len(candidates)}]: ",
        input_fn=input_fn,
        output_fn=output_fn,
        disallowed={top1},
        disallowed_message="The second finalist must be different from the first.",
    )
    primary = _prompt_candidate_index(
        candidates,
        f"Choose the primary winner [1-{len(candidates)}]: ",
        input_fn=input_fn,
        output_fn=output_fn,
        allowed={top1, top2},
        disallowed_message="The primary winner must also be one of the top two finalists.",
    )

    result = review_and_promote_batch(
        project_slug=project_slug,
        scene_id=scene_id,
        clip_id=clip_id,
        stage=stage,
        manifest_path=manifest_path,
        top_two_indexes=[top1, top2],
        primary_index=primary,
        promotion_target=promotion_target,
        promotion_index=promotion_index,
    )

    output_fn("")
    output_fn("Review choices:")
    output_fn("Top 2 finalists:")
    for finalist in result["top_two"]:
        output_fn(f"  {finalist['index']}. {finalist['name']}")
    output_fn("Primary winner:")
    output_fn(f"  {result['primary']['index']}. {result['primary']['name']}")
    output_fn("")
    return result


def _candidate_from_index(candidates: Sequence[ReviewCandidate], index: int) -> ReviewCandidate:
    for candidate in candidates:
        if candidate.index == index:
            return candidate
    raise ValueError(f"Candidate index out of range: {index}")


def _prompt_candidate_index(
    candidates: Sequence[ReviewCandidate],
    prompt: str,
    *,
    input_fn: Callable[[str], str],
    output_fn: Callable[[str], None],
    allowed: set[int] | None = None,
    disallowed: set[int] | None = None,
    disallowed_message: str | None = None,
) -> int:
    valid_indexes = {candidate.index for candidate in candidates}
    while True:
        raw_value = input_fn(prompt).strip()
        try:
            index = int(raw_value)
        except ValueError:
            output_fn("Enter a number from the candidate list.")
            output_fn("")
            continue

        if index not in valid_indexes:
            output_fn(f"Choose a number from 1 to {len(candidates)}.")
            output_fn("")
            continue

        if disallowed and index in disallowed:
            output_fn(disallowed_message or "That choice is not allowed here.")
            output_fn("")
            continue

        if allowed is not None and index not in allowed:
            output_fn(disallowed_message or "That choice is not allowed here.")
            output_fn("")
            continue

        return index
