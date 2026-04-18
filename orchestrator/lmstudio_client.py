from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib import error, request

from .settings import RuntimeSettings


class LMStudioError(RuntimeError):
    """Raised when the local LM Studio API is unreachable or returns invalid data."""


@dataclass(frozen=True)
class LMStudioCheckSummary:
    base_url: str
    configured_model: str | None
    resolved_model: str
    available_models: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "base_url": self.base_url,
            "configured_model": self.configured_model,
            "resolved_model": self.resolved_model,
            "available_models": self.available_models,
        }


class LMStudioClient:
    def __init__(self, settings: RuntimeSettings) -> None:
        self._settings = settings
        self._api_base_url = self._discover_api_base_url()

    @property
    def api_base_url(self) -> str:
        return self._api_base_url

    def check(self) -> LMStudioCheckSummary:
        available_models = self.list_models()
        resolved_model = self.resolve_model(available_models)
        return LMStudioCheckSummary(
            base_url=self.api_base_url,
            configured_model=self._settings.lmstudio_model,
            resolved_model=resolved_model,
            available_models=available_models,
        )

    def list_models(self) -> list[str]:
        payload = self._request_json("GET", "/models")
        data = payload.get("data")
        if not isinstance(data, list):
            raise LMStudioError("LM Studio returned an unexpected /models payload.")

        models: list[str] = []
        for item in data:
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                models.append(item["id"])
        if not models:
            raise LMStudioError("LM Studio did not report any available models.")
        return models

    def resolve_model(self, available_models: list[str] | None = None) -> str:
        models = available_models or self.list_models()
        configured = self._settings.lmstudio_model
        if configured:
            if configured not in models:
                available = ", ".join(models)
                raise LMStudioError(
                    f"Configured LM Studio model '{configured}' was not found. Available models: {available}"
                )
            return configured
        return models[0]

    def chat_completion(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        model: str | None = None,
    ) -> str:
        resolved_model = model or self.resolve_model()
        payload = self._request_json(
            "POST",
            "/chat/completions",
            {
                "model": resolved_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "temperature": temperature,
            },
        )
        try:
            choice = payload["choices"][0]
            message = choice["message"]
            content = message["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise LMStudioError(f"LM Studio returned an unexpected chat completion payload: {exc}") from exc

        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text" and isinstance(item.get("text"), str):
                    parts.append(item["text"])
            if parts:
                return "\n".join(parts)
        raise LMStudioError("LM Studio returned a chat completion without text content.")

    def _discover_api_base_url(self) -> str:
        original = self._settings.lmstudio_base_url.rstrip("/")
        candidates = [original]
        if not original.endswith("/v1"):
            candidates.append(f"{original}/v1")

        for candidate in candidates:
            try:
                self._request_json_absolute("GET", f"{candidate}/models")
                return candidate
            except LMStudioError:
                continue

        attempted = ", ".join(candidates)
        raise LMStudioError(
            f"Could not reach LM Studio at any expected API base URL. Tried: {attempted}"
        )

    def _request_json(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._request_json_absolute(method, f"{self.api_base_url}{path}", payload)

    def _request_json_absolute(
        self,
        method: str,
        url: str,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        data = None
        headers = {"Accept": "application/json"}
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = request.Request(url=url, data=data, method=method, headers=headers)
        timeout = self._settings.lmstudio_timeout_seconds
        try:
            with request.urlopen(req, timeout=timeout) as response:
                body = response.read().decode("utf-8")
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise LMStudioError(f"LM Studio HTTP error {exc.code} from {url}: {body}") from exc
        except error.URLError as exc:
            raise LMStudioError(f"Could not connect to LM Studio at {url}: {exc.reason}") from exc
        except TimeoutError as exc:
            raise LMStudioError(f"Timed out waiting for LM Studio at {url}") from exc

        try:
            return json.loads(body)
        except json.JSONDecodeError as exc:
            raise LMStudioError(f"LM Studio did not return valid JSON from {url}: {exc}") from exc
