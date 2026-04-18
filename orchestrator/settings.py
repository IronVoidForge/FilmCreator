from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RuntimeSettings:
    comfy_base_url: str
    comfy_input_dir: Path
    comfy_output_dir: Path
    comfy_poll_interval_seconds: float
    comfy_timeout_seconds: float
    keep_staged_files: bool
    lmstudio_base_url: str
    lmstudio_model: str | None
    lmstudio_timeout_seconds: float


def load_runtime_settings() -> RuntimeSettings:
    return RuntimeSettings(
        comfy_base_url=os.environ.get("FILMCREATOR_COMFY_BASE_URL", "http://127.0.0.1:8188").rstrip("/"),
        comfy_input_dir=Path(os.environ.get("FILMCREATOR_COMFY_INPUT_DIR", r"C:\ComfyUIInstall\input")),
        comfy_output_dir=Path(os.environ.get("FILMCREATOR_COMFY_OUTPUT_DIR", r"C:\ComfyUIInstall\output")),
        comfy_poll_interval_seconds=float(os.environ.get("FILMCREATOR_COMFY_POLL_INTERVAL_SECONDS", "1.0")),
        comfy_timeout_seconds=float(os.environ.get("FILMCREATOR_COMFY_TIMEOUT_SECONDS", "1800.0")),
        keep_staged_files=os.environ.get("FILMCREATOR_KEEP_STAGED_FILES", "").lower() in {"1", "true", "yes"},
        lmstudio_base_url=os.environ.get("FILMCREATOR_LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1").rstrip("/"),
        lmstudio_model=os.environ.get("FILMCREATOR_LMSTUDIO_MODEL") or None,
        lmstudio_timeout_seconds=float(os.environ.get("FILMCREATOR_LMSTUDIO_TIMEOUT_SECONDS", "120.0")),
    )
