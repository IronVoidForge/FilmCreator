from __future__ import annotations

from .world_refinement import RefinementSummary, refine_world_identities


def run_identity_refinement(
    project_slug: str,
    *,
    use_llm: bool = True,
    apply_merge: bool = True,
) -> RefinementSummary:
    return refine_world_identities(
        project_slug=project_slug,
        use_llm=use_llm,
        apply_changes=apply_merge,
    )
