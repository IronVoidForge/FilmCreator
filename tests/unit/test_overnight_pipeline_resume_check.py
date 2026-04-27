from pathlib import Path

from orchestrator.core.json_io import write_json
from orchestrator.overnight_pipeline_resume_check import (
    check_descriptor_enrichment,
    check_prompt_preparation,
    check_quality_grading,
    check_visual_fallbacks,
)
from orchestrator.prompt_package import PromptPackage, write_prompt_package


def _write_prompt(path: Path, *, subject_kind: str, subject_id: str, variant_name: str) -> None:
    package = PromptPackage(
        path=path,
        title=f"{subject_id} prompt",
        prompt_id=f"{subject_id}_{variant_name}_prompt",
        purpose="Resume validation test",
        workflow_type="still.t2i.klein.distilled",
        positive_prompt="cinematic readable prompt package",
        negative_prompt="blurry",
        inputs_markdown="\n".join(
            [
                f"- subject_kind: {subject_kind}",
                f"- subject_id: {subject_id}",
                "- source_artifact_ids: src",
                "- reference_mode: canonical_reference_generation",
                f"- variant_name: {variant_name}",
                "- reuse_policy: reuse canonical visual canon",
            ]
        ),
        continuity_notes_markdown="- keep continuity",
        sources_markdown="- src.json",
    )
    write_prompt_package(path, package)


def test_check_visual_fallbacks_rejects_thin_payload(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    path = project_root / "02_story_analysis" / "world" / "global" / "VISUAL_FALLBACKS.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(
        path,
        {
            "source_title": "",
            "book_visual_context": "",
            "character_fallbacks": {},
            "environment_fallbacks": {},
            "negative_terms": {},
        },
    )

    ok, reason, details = check_visual_fallbacks(project_root)

    assert ok is False
    assert "missing/empty required content" in reason
    assert details["has_context_digest"] is False


def test_check_descriptor_enrichment_rejects_wrong_chapter_coverage(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    path = project_root / "02_story_analysis" / "descriptors" / "DESCRIPTOR_INDEX.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(
        path,
        [
            {"entity_type": "character", "canonical_id": "hero", "chapter_mentions": ["CH005"]},
            {"entity_type": "environment", "canonical_id": "arena", "chapter_mentions": ["CH005"]},
        ],
    )

    ok, reason, details = check_descriptor_enrichment(project_root, "2-3")

    assert ok is False
    assert "requested chapter coverage is missing" in reason
    assert details["missing"] == ["CH002", "CH003"]


def test_check_prompt_preparation_rejects_empty_and_partial_outputs(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    descriptors = project_root / "02_story_analysis" / "descriptors" / "DESCRIPTOR_INDEX.json"
    descriptors.parent.mkdir(parents=True, exist_ok=True)
    write_json(descriptors, [{"entity_type": "character", "canonical_id": "hero", "chapter_mentions": ["CH002", "CH003"]}])

    prepared_root = project_root / "03_prompt_packages" / "prepared"
    prompt_path = prepared_root / "characters" / "hero" / "bust_portrait_prompt.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text("", encoding="utf-8")
    write_json(
        prepared_root / "PROMPT_PREPARATION_INDEX.json",
        [
            {
                "prompt_id": "hero_bust_portrait_prompt",
                "subject_kind": "character",
                "subject_id": "hero",
                "variant_name": "bust_portrait",
                "status": "canonical",
                "path": str(prompt_path),
                "chapter_mentions": ["CH002", "CH003"],
            },
            {
                "prompt_id": "arena_establishing_wide_prompt",
                "subject_kind": "environment",
                "subject_id": "arena",
                "variant_name": "establishing_wide",
                "status": "canonical",
                "path": str(prepared_root / "environments" / "arena" / "establishing_wide_prompt.md"),
                "chapter_mentions": ["CH002"],
            },
        ],
    )

    ok, reason, details = check_prompt_preparation(project_root, "2-3")

    assert ok is False
    assert "missing, empty, or invalid" in reason
    assert details["empty_files"] or details["missing_files"]


def test_check_prompt_preparation_accepts_valid_prompt_mix(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    descriptors = project_root / "02_story_analysis" / "descriptors" / "DESCRIPTOR_INDEX.json"
    descriptors.parent.mkdir(parents=True, exist_ok=True)
    write_json(descriptors, [{"entity_type": "character", "canonical_id": "hero", "chapter_mentions": ["CH002", "CH003"]}])

    prepared_root = project_root / "03_prompt_packages" / "prepared"
    char_prompt = prepared_root / "characters" / "hero" / "bust_portrait_prompt.md"
    env_prompt = prepared_root / "environments" / "arena" / "establishing_wide_prompt.md"
    shot_prompt = prepared_root / "shots" / "ch002_sc001_sh001" / "primary_keyframe_prompt.md"
    _write_prompt(char_prompt, subject_kind="character", subject_id="hero", variant_name="bust_portrait")
    _write_prompt(env_prompt, subject_kind="environment", subject_id="arena", variant_name="establishing_wide")
    _write_prompt(shot_prompt, subject_kind="shot", subject_id="ch002_sc001_sh001", variant_name="primary_keyframe")
    write_json(
        prepared_root / "PROMPT_PREPARATION_INDEX.json",
        [
            {"prompt_id": "hero_bust_portrait_prompt", "subject_kind": "character", "subject_id": "hero", "variant_name": "bust_portrait", "status": "canonical", "path": str(char_prompt), "chapter_mentions": ["CH002", "CH003"]},
            {"prompt_id": "arena_establishing_wide_prompt", "subject_kind": "environment", "subject_id": "arena", "variant_name": "establishing_wide", "status": "canonical", "path": str(env_prompt), "chapter_mentions": ["CH002"]},
            {"prompt_id": "shot_primary_keyframe_prompt", "subject_kind": "shot", "subject_id": "ch002_sc001_sh001", "variant_name": "primary_keyframe", "status": "canonical", "path": str(shot_prompt), "chapter_mentions": ["CH003"]},
        ],
    )

    ok, reason, details = check_prompt_preparation(project_root, "2-3")

    assert ok is True
    assert "canonical prompt records validated" in reason
    assert set(details["requested"]) == {"CH002", "CH003"}


def test_check_quality_grading_rejects_missing_family_summaries(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    grading_root = project_root / "02_story_analysis" / "grading"
    grading_root.mkdir(parents=True, exist_ok=True)
    write_json(
        grading_root / "QUALITY_GRADE_INDEX.json",
        {
            "project_slug": "demo",
            "total_records": 3,
            "records": [{"family": "character", "artifact_id": "hero"}],
            "family_summaries": [],
            "rerun_queue": [],
        },
    )

    ok, reason, _ = check_quality_grading(project_root)

    assert ok is False
    assert "missing family summaries" in reason


def test_check_quality_grading_accepts_valid_index_and_queue(tmp_path: Path) -> None:
    project_root = tmp_path / "demo"
    grading_root = project_root / "02_story_analysis" / "grading"
    review_root = grading_root / "review"
    review_root.mkdir(parents=True, exist_ok=True)
    write_json(
        grading_root / "QUALITY_GRADE_INDEX.json",
        {
            "project_slug": "demo",
            "total_records": 2,
            "records": [
                {"family": "character", "artifact_id": "hero"},
                {"family": "prompt_package", "artifact_id": "hero_bust_portrait_prompt"},
            ],
            "family_summaries": [
                {"family": "character", "count": 1, "grade_counts": {"A": 1}},
                {"family": "prompt_package", "count": 1, "grade_counts": {"B": 1}},
            ],
            "rerun_queue": [],
        },
    )
    write_json(
        review_root / "QUALITY_RERUN_QUEUE.json",
        [
            {
                "family": "prompt_package",
                "artifact_id": "hero_bust_portrait_prompt",
                "reason": ["thin prompt"],
            }
        ],
    )

    ok, reason, details = check_quality_grading(project_root)

    assert ok is True
    assert "family summaries, and rerun queue" in reason
    assert details["family_summaries"] == 2
    assert details["rerun_queue"] == 1
