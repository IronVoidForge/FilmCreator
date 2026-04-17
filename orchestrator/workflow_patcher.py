from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any

from .common import read_json


class WorkflowPatchError(ValueError):
    pass


PATH_TOKEN_PATTERN = re.compile(r"([^\[\].]+)|\[(\d+)\]")


def load_workflow_payload(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise WorkflowPatchError(f"Workflow at {path} must be a JSON object")
    return payload


def detect_workflow_format(payload: dict[str, Any]) -> str:
    if isinstance(payload.get("nodes"), list):
        return "editor_graph"

    if payload and all(
        isinstance(node_id, str) and isinstance(node_value, dict) and "class_type" in node_value
        for node_id, node_value in payload.items()
    ):
        return "api_prompt"

    return "unknown"


def patch_workflow_payload(
    payload: dict[str, Any],
    workflow: dict[str, Any],
    *,
    prompt_text: str | None = None,
    negative_prompt: str | None = None,
    save_prefix: str | None = None,
    seed: int | None = None,
    source_images: dict[str, str] | None = None,
) -> dict[str, Any]:
    patched = copy.deepcopy(payload)
    patch_points = workflow.get("patch_points", {})

    if prompt_text is not None:
        prompt_spec = patch_points.get("prompt_text")
        if prompt_spec is None:
            raise WorkflowPatchError(f"Workflow '{workflow['id']}' does not declare a prompt_text patch point")
        _apply_scalar_patch(patched, prompt_spec, prompt_text, label="prompt_text")

    if negative_prompt is not None:
        negative_spec = patch_points.get("negative_prompt")
        if negative_spec is None:
            raise WorkflowPatchError(f"Workflow '{workflow['id']}' does not declare a negative_prompt patch point")
        _apply_scalar_patch(patched, negative_spec, negative_prompt, label="negative_prompt")

    if save_prefix is not None:
        save_spec = patch_points.get("save_prefix")
        if save_spec is None:
            raise WorkflowPatchError(f"Workflow '{workflow['id']}' does not declare a save_prefix patch point")
        _apply_scalar_patch(patched, save_spec, save_prefix, label="save_prefix")

    if seed is not None:
        seed_spec = patch_points.get("seed")
        if seed_spec is None:
            raise WorkflowPatchError(f"Workflow '{workflow['id']}' does not declare a seed patch point")
        _apply_scalar_patch(patched, seed_spec, seed, label="seed")

    if source_images:
        source_spec = patch_points.get("source_images")
        if source_spec is None:
            raise WorkflowPatchError(f"Workflow '{workflow['id']}' does not declare source_images patch points")
        _apply_source_image_patch(patched, source_spec, source_images)

    return patched


def prune_api_prompt_to_output_nodes(payload: dict[str, Any], output_node_ids: list[int | str]) -> dict[str, Any]:
    if detect_workflow_format(payload) != "api_prompt":
        raise WorkflowPatchError("Workflow pruning is only supported for ComfyUI API prompt payloads.")

    keep: set[str] = set()

    def visit(node_id: str) -> None:
        if node_id in keep:
            return
        if node_id not in payload or not isinstance(payload[node_id], dict):
            raise WorkflowPatchError(f"Cannot prune workflow: referenced node '{node_id}' was not found.")

        keep.add(node_id)
        node_inputs = payload[node_id].get("inputs", {})
        if not isinstance(node_inputs, dict):
            return

        for value in node_inputs.values():
            for dependency_id in _extract_dependency_node_ids(value):
                visit(dependency_id)

    for output_node_id in output_node_ids:
        visit(str(output_node_id))

    return {node_id: payload[node_id] for node_id in payload if node_id in keep}


def _apply_scalar_patch(payload: dict[str, Any], spec: dict[str, Any], value: Any, *, label: str) -> None:
    if "node_id" in spec:
        target = _find_node(payload, spec["node_id"])
        _set_path_value(target, spec["path"], value, label=label)
        return

    if "node_ids" in spec:
        for node_id in spec["node_ids"]:
            target = _find_node(payload, node_id)
            _set_path_value(target, spec["path"], value, label=label)
        return

    raise WorkflowPatchError(f"Unsupported {label} patch point format: {spec}")


def _apply_source_image_patch(payload: dict[str, Any], spec: dict[str, Any], source_images: dict[str, str]) -> None:
    if "node_ids" in spec and "path" in spec:
        if len(source_images) != 1:
            source_keys = ", ".join(sorted(source_images))
            raise WorkflowPatchError(
                "This workflow expects one shared source image value, but multiple image slots were provided: "
                f"{source_keys}"
            )
        image_path = next(iter(source_images.values()))
        for node_id in spec["node_ids"]:
            target = _find_node(payload, node_id)
            _set_path_value(target, spec["path"], image_path, label="source_images")
        return

    for slot, image_path in source_images.items():
        if slot not in spec:
            raise WorkflowPatchError(f"Workflow does not declare a source image slot named '{slot}'")
        slot_spec = spec[slot]
        target = _find_node(payload, slot_spec["node_id"])
        _set_path_value(target, slot_spec["path"], image_path, label=f"source_images.{slot}")


def _extract_dependency_node_ids(value: Any) -> list[str]:
    dependencies: list[str] = []

    if isinstance(value, list):
        if len(value) == 2 and isinstance(value[0], (str, int)) and isinstance(value[1], int):
            dependencies.append(str(value[0]))
        else:
            for item in value:
                dependencies.extend(_extract_dependency_node_ids(item))
    elif isinstance(value, dict):
        for nested in value.values():
            dependencies.extend(_extract_dependency_node_ids(nested))

    return dependencies


def _find_node(payload: dict[str, Any], node_id: int | str) -> dict[str, Any]:
    node_id_str = str(node_id)

    if node_id_str in payload and isinstance(payload[node_id_str], dict):
        return payload[node_id_str]

    if isinstance(payload.get("nodes"), list):
        matches = _find_nodes_in_editor_graph(payload, int(node_id))
        if not matches:
            raise WorkflowPatchError(f"Node id {node_id} was not found in the workflow graph")
        if len(matches) > 1:
            raise WorkflowPatchError(
                f"Node id {node_id} is ambiguous across the workflow graph and subgraphs; "
                "the registry needs a more specific locator"
            )
        return matches[0]

    raise WorkflowPatchError(f"Node id {node_id} was not found in the workflow payload")


def _find_nodes_in_editor_graph(payload: dict[str, Any], node_id: int) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []

    for node in payload.get("nodes", []):
        if isinstance(node, dict) and node.get("id") == node_id:
            matches.append(node)

    definitions = payload.get("definitions", {})
    for subgraph in definitions.get("subgraphs", []):
        matches.extend(_find_nodes_in_editor_subgraph(subgraph, node_id))
    return matches


def _find_nodes_in_editor_subgraph(subgraph: dict[str, Any], node_id: int) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for node in subgraph.get("nodes", []):
        if isinstance(node, dict) and node.get("id") == node_id:
            matches.append(node)

    definitions = subgraph.get("definitions", {})
    for nested_subgraph in definitions.get("subgraphs", []):
        matches.extend(_find_nodes_in_editor_subgraph(nested_subgraph, node_id))
    return matches


def _set_path_value(target: dict[str, Any], path: str, value: Any, *, label: str) -> None:
    current: Any = target
    tokens = _parse_path_tokens(path)

    for index, token in enumerate(tokens):
        is_last = index == len(tokens) - 1
        if is_last:
            _assign_token(current, token, value, label=label, path=path)
            return
        current = _resolve_token(current, token, label=label, path=path)


def _parse_path_tokens(path: str) -> list[str | int]:
    tokens: list[str | int] = []
    for name, index in PATH_TOKEN_PATTERN.findall(path):
        if name:
            tokens.append(name)
        else:
            tokens.append(int(index))
    if not tokens:
        raise WorkflowPatchError(f"Unsupported patch path '{path}'")
    return tokens


def _resolve_token(current: Any, token: str | int, *, label: str, path: str) -> Any:
    if isinstance(token, str):
        if not isinstance(current, dict) or token not in current:
            raise WorkflowPatchError(f"Cannot resolve {label} path '{path}': missing key '{token}'")
        return current[token]

    if not isinstance(current, list) or token >= len(current):
        raise WorkflowPatchError(f"Cannot resolve {label} path '{path}': missing index [{token}]")
    return current[token]


def _assign_token(current: Any, token: str | int, value: Any, *, label: str, path: str) -> None:
    if isinstance(token, str):
        if not isinstance(current, dict) or token not in current:
            raise WorkflowPatchError(f"Cannot patch {label} at '{path}': missing key '{token}'")
        current[token] = value
        return

    if not isinstance(current, list) or token >= len(current):
        raise WorkflowPatchError(f"Cannot patch {label} at '{path}': missing index [{token}]")
    current[token] = value
