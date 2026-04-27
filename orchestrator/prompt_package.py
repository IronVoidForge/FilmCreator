from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REQUIRED_HEADINGS = [
    "Title",
    "ID",
    "Purpose",
    "Workflow Type",
    "Positive Prompt",
    "Negative Prompt",
    "Inputs",
    "Continuity Notes",
    "Repair Notes",
    "Sources",
]

HEADING_PATTERN = re.compile(r"(?m)^# ([^\r\n]+)\s*$")


@dataclass(frozen=True)
class PromptPackage:
    path: Path
    title: str
    prompt_id: str
    purpose: str
    workflow_type: str
    positive_prompt: str
    negative_prompt: str
    inputs_markdown: str
    continuity_notes_markdown: str
    sources_markdown: str
    repair_notes_markdown: str = ""

    @property
    def sources(self) -> list[str]:
        return _parse_bullet_list(self.sources_markdown)

    @property
    def inputs(self) -> dict[str, str]:
        parsed: dict[str, str] = {}
        for line in self.inputs_markdown.splitlines():
            stripped = line.strip()
            if not stripped.startswith("- "):
                continue
            item = stripped[2:]
            if ":" not in item:
                continue
            key, value = item.split(":", 1)
            parsed[key.strip()] = value.strip()
        return parsed

    def to_manifest_dict(self) -> dict[str, object]:
        return {
            "path": str(self.path),
            "title": self.title,
            "id": self.prompt_id,
            "purpose": self.purpose,
            "workflow_type": self.workflow_type,
            "positive_prompt": self.positive_prompt,
            "negative_prompt": self.negative_prompt,
            "inputs": self.inputs,
            "continuity_notes": _parse_bullet_list(self.continuity_notes_markdown),
            "repair_notes": _parse_bullet_list(self.repair_notes_markdown),
            "sources": self.sources,
        }

    def to_markdown(self) -> str:
        input_lines = [f"- {key}: {value}" for key, value in self.inputs.items()]
        continuity_lines = _parse_bullet_list(self.continuity_notes_markdown)
        source_lines = self.sources
        repair_lines = _parse_bullet_list(self.repair_notes_markdown)

        sections = [
            "# Title",
            self.title,
            "",
            "# ID",
            self.prompt_id,
            "",
            "# Purpose",
            self.purpose,
            "",
            "# Workflow Type",
            self.workflow_type,
            "",
            "# Positive Prompt",
            self.positive_prompt,
            "",
            "# Negative Prompt",
            self.negative_prompt,
            "",
            "# Inputs",
            *input_lines,
            "",
            "# Continuity Notes",
            *[f"- {line}" for line in continuity_lines],
            "",
            "# Repair Notes",
            *[f"- {line}" for line in repair_lines],
            "",
            "# Sources",
            *[f"- {line}" for line in source_lines],
            "",
        ]
        return "\n".join(sections)


def parse_prompt_package(path: Path) -> PromptPackage:
    text = path.read_text(encoding="utf-8")
    sections = _split_sections(text)
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in sections]
    required_nonempty = [heading for heading in REQUIRED_HEADINGS if heading != "Repair Notes"]
    missing.extend(heading for heading in required_nonempty if heading in sections and not sections[heading].strip())
    if missing:
        missing_text = ", ".join(missing)
        raise ValueError(f"Prompt package {path} is missing required sections: {missing_text}")

    return PromptPackage(
        path=path,
        title=sections["Title"].strip(),
        prompt_id=sections["ID"].strip(),
        purpose=sections["Purpose"].strip(),
        workflow_type=sections["Workflow Type"].strip(),
        positive_prompt=sections["Positive Prompt"].strip(),
        negative_prompt=sections["Negative Prompt"].strip(),
        inputs_markdown=sections["Inputs"].strip(),
        continuity_notes_markdown=sections["Continuity Notes"].strip(),
        repair_notes_markdown=sections["Repair Notes"].strip(),
        sources_markdown=sections["Sources"].strip(),
    )


def write_prompt_package(path: Path, prompt_package: PromptPackage) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(prompt_package.to_markdown(), encoding="utf-8")


def _split_sections(text: str) -> dict[str, str]:
    matches = list(HEADING_PATTERN.finditer(text))
    if not matches:
        return {}

    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = text[start:end].strip()
    return sections


def _parse_bullet_list(text: str) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items
