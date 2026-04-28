from orchestrator.story_authoring import _TaskAttempt, _best_attempt_raw_response, _record_repair_focus


def test_record_repair_focus_detects_missing_type() -> None:
    attempts = [
        _TaskAttempt(
            kind="normal",
            status="parse_failed",
            log_path="log.md",
            message="Packet record is missing required field 'type'.",
            raw_response="[[FILMCREATOR_PACKET]]",
        )
    ]

    assert _record_repair_focus(attempts) == "missing_type"


def test_best_attempt_raw_response_prefers_longest_response() -> None:
    attempts = [
        _TaskAttempt(kind="normal", status="parse_failed", log_path="a", message="x", raw_response="short"),
        _TaskAttempt(kind="same_prompt_retry", status="parse_failed", log_path="b", message="y", raw_response="much longer response"),
    ]

    assert _best_attempt_raw_response(attempts) == "much longer response"
