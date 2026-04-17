from __future__ import annotations

from typing import Any

from .common import REGISTRY_PATH, read_json


def load_registry() -> dict[str, Any]:
    return read_json(REGISTRY_PATH)


def get_workflow(workflow_id: str) -> dict[str, Any]:
    registry = load_registry()
    for workflow in registry["workflows"]:
        if workflow["id"] == workflow_id:
            return workflow
    raise KeyError(f"Workflow '{workflow_id}' was not found in {REGISTRY_PATH}")

