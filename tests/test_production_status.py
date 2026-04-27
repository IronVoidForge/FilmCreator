from orchestrator.production_status import format_production_status, get_production_status


def test_get_production_status_appends_reference_placeholders(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_status.validation_report",
        lambda project_slug, chapters="": [
            {"stage": "story_analysis", "complete": True, "reason": "ok", "details": {}},
            {"stage": "quality_grading", "complete": False, "reason": "missing", "details": {}},
        ],
    )
    monkeypatch.setattr(
        "orchestrator.production_status.find_first_incomplete_stage",
        lambda project_slug, chapters="": "quality_grading",
    )

    summary = get_production_status("demo", chapters="2-3")

    assert summary.resume_from == "quality_grading"
    assert summary.phases[-2]["phase"] == "character_references"
    assert summary.phases[-1]["phase"] == "environment_references"
    lines = format_production_status(summary)
    assert any("Resume would start at: quality_grading" in line for line in lines)
    assert any("Reference phase completion" in line for line in lines)
