from pathlib import Path

import orchestrator.lmstudio_client as lmstudio_client_module
from orchestrator.settings import RuntimeSettings


def test_lmstudio_check_discovers_v1_base_url_and_configured_model(monkeypatch) -> None:
    def fake_request(self, method: str, url: str, payload=None):  # noqa: ANN001
        assert method == "GET"
        assert payload is None
        if url == "http://127.0.0.1:1234/models":
            raise lmstudio_client_module.LMStudioError("not found")
        if url == "http://127.0.0.1:1234/v1/models":
            return {"data": [{"id": "alpha-model"}, {"id": "beta-model"}]}
        raise AssertionError(f"Unexpected URL: {url}")

    monkeypatch.setattr(lmstudio_client_module.LMStudioClient, "_request_json_absolute", fake_request)

    settings = RuntimeSettings(
        comfy_base_url="http://127.0.0.1:8188",
        comfy_input_dir=Path("input"),
        comfy_output_dir=Path("output"),
        comfy_poll_interval_seconds=1.0,
        comfy_timeout_seconds=60.0,
        keep_staged_files=False,
        lmstudio_base_url="http://127.0.0.1:1234",
        lmstudio_model="beta-model",
        lmstudio_timeout_seconds=60.0,
    )

    client = lmstudio_client_module.LMStudioClient(settings)
    summary = client.check()

    assert summary.base_url == "http://127.0.0.1:1234/v1"
    assert summary.configured_model == "beta-model"
    assert summary.resolved_model == "beta-model"
    assert summary.available_models == ["alpha-model", "beta-model"]
