import pytest

from orchestrator.comfy_client import ComfyClient, ComfyExecutionError


def test_wait_for_completion_raises_execution_error(monkeypatch) -> None:
    client = ComfyClient("http://127.0.0.1:8000")
    prompt_id = "prompt-123"
    history = {
        prompt_id: {
            "outputs": {},
            "status": {
                "messages": [
                    ["execution_start", {"prompt_id": prompt_id}],
                    [
                        "execution_error",
                        {
                            "prompt_id": prompt_id,
                            "node_id": "75:64",
                            "node_type": "SamplerCustomAdvanced",
                            "exception_message": "[Errno 22] Invalid argument\n",
                        },
                    ],
                ]
            },
        }
    }
    monkeypatch.setattr(client, "get_history", lambda _: history)

    with pytest.raises(ComfyExecutionError, match="SamplerCustomAdvanced") as exc_info:
        client.wait_for_completion(prompt_id, poll_interval_seconds=0.0, timeout_seconds=0.1)

    assert exc_info.value.details["node_id"] == "75:64"


def test_collect_history_outputs_includes_video_gifs() -> None:
    client = ComfyClient("http://127.0.0.1:8000")
    history_entry = {
        "outputs": {
            "9": {
                "images": [
                    {
                        "filename": "frame.png",
                        "subfolder": "filmcreator/run",
                        "type": "output",
                    }
                ]
            },
            "150": {
                "gifs": [
                    {
                        "filename": "preview.mp4",
                        "subfolder": "filmcreator/run",
                        "type": "output",
                        "format": "video/h264-mp4",
                        "fullpath": r"C:\tmp\preview.mp4",
                    }
                ]
            },
        }
    }

    outputs = client.collect_history_outputs(history_entry)
    images = client.collect_history_images(history_entry)

    assert len(outputs) == 2
    assert images == [
        {
            "node_id": "9",
            "collection_key": "images",
            "media_kind": "image",
            "filename": "frame.png",
            "subfolder": "filmcreator/run",
            "type": "output",
            "format": "",
            "fullpath": "",
        }
    ]
    assert outputs[1]["node_id"] == "150"
    assert outputs[1]["media_kind"] == "video"
    assert outputs[1]["filename"] == "preview.mp4"
