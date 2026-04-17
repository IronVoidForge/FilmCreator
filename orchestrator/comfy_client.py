from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any


class ComfyExecutionError(RuntimeError):
    def __init__(self, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.details = details or {}


class ComfyClient:
    def __init__(self, base_url: str, *, timeout_seconds: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    def ping(self) -> dict[str, Any]:
        return self._request_json("GET", "/queue")

    def submit_prompt(self, prompt: dict[str, Any], *, client_id: str | None = None) -> dict[str, Any]:
        payload: dict[str, Any] = {"prompt": prompt}
        if client_id:
            payload["client_id"] = client_id
        return self._request_json("POST", "/prompt", payload)

    def get_history(self, prompt_id: str) -> dict[str, Any]:
        return self._request_json("GET", f"/history/{prompt_id}")

    def wait_for_completion(
        self,
        prompt_id: str,
        *,
        poll_interval_seconds: float = 1.0,
        timeout_seconds: float = 1800.0,
    ) -> dict[str, Any]:
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            history = self.get_history(prompt_id)
            if prompt_id in history:
                history_entry = history[prompt_id]
                execution_error = self._extract_execution_error(prompt_id, history_entry)
                if execution_error is not None:
                    raise execution_error
                if history_entry.get("outputs"):
                    return history_entry
            time.sleep(poll_interval_seconds)
        raise TimeoutError(f"Timed out waiting for ComfyUI prompt {prompt_id} to finish")

    def collect_history_outputs(self, history_entry: dict[str, Any]) -> list[dict[str, str]]:
        outputs: list[dict[str, str]] = []
        output_type_map = {
            "images": "image",
            "gifs": "video",
            "files": "file",
        }

        for node_id, node_output in history_entry.get("outputs", {}).items():
            for collection_key, media_kind in output_type_map.items():
                for item in node_output.get(collection_key, []):
                    outputs.append(
                        {
                            "node_id": str(node_id),
                            "collection_key": collection_key,
                            "media_kind": media_kind,
                            "filename": item["filename"],
                            "subfolder": item.get("subfolder", ""),
                            "type": item.get("type", "output"),
                            "format": item.get("format", ""),
                            "fullpath": item.get("fullpath", ""),
                        }
                    )
        return outputs

    def collect_history_images(self, history_entry: dict[str, Any]) -> list[dict[str, str]]:
        return [
            output
            for output in self.collect_history_outputs(history_entry)
            if output.get("media_kind") == "image"
        ]

    def _extract_execution_error(
        self,
        prompt_id: str,
        history_entry: dict[str, Any],
    ) -> ComfyExecutionError | None:
        status = history_entry.get("status", {})
        messages = status.get("messages", [])
        for message in messages:
            if not isinstance(message, list) or len(message) < 2:
                continue
            event_name = message[0]
            details = message[1] if isinstance(message[1], dict) else {}
            if event_name != "execution_error":
                continue

            node_id = details.get("node_id")
            node_type = details.get("node_type")
            exception_message = str(details.get("exception_message", "unknown ComfyUI execution error")).strip()

            parts = [f"ComfyUI execution failed for prompt {prompt_id}"]
            if node_id:
                parts.append(f"at node {node_id}")
            if node_type:
                parts.append(f"({node_type})")

            message_text = " ".join(parts)
            if exception_message:
                message_text = f"{message_text}: {exception_message}"

            return ComfyExecutionError(message_text, details=details)
        return None

    def _request_json(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        data = None
        headers = {"Content-Type": "application/json"}
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"ComfyUI request {method} {url} failed: HTTP {exc.code} {body}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Could not reach ComfyUI at {url}: {exc.reason}") from exc
