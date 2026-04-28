from __future__ import annotations

from pathlib import Path

from ...core.paths import repo_relative

PACKET_START_TAG = "[[FILMCREATOR_PACKET]]"
PACKET_END_TAG = "[[/FILMCREATOR_PACKET]]"
SECTION_END_TAG = "[[/SECTION]]"
PACKET_VERSION = "1"


def analysis_system_prompt() -> str:
    return "\n".join(
        [
            "You are FilmCreator's chapter analysis engine.",
            "Return only FilmCreator packets with the requested sections and records.",
            "Do not wrap the packet in code fences unless explicitly requested.",
            "Do not produce JSON-only responses.",
            "If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].",
            "Do not put another [[SECTION ...]] tag inside a section body.",
            "Copy every FILMCREATOR structural tag literally.",
            "Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.",
            "The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].",
            "Keep the response deterministic and grounded in the supplied chapter text.",
        ]
    )


def packet_contract_block(*, task_name: str, section_names: list[str], record_templates: list[tuple[str, list[str], list[str]]] | None = None) -> str:
    lines = [
        "Packet contract:",
        f"- task: {task_name}",
        f"- version: {PACKET_VERSION}",
        f"- first line: {PACKET_START_TAG}",
        f"- last line: {PACKET_END_TAG}",
    ]
    if section_names:
        lines.append(f"- required sections: {', '.join(section_names)}")
    if record_templates:
        for record_type, fields, sections in record_templates:
            lines.append(
                f"- record type {record_type}: fields={', '.join(fields) or '(none)'} sections={', '.join(sections) or '(none)'}"
            )
    return "\n".join(lines)


def chapter_summary_user_prompt(
    project_slug: str,
    chapter_source=None,
    chapter_id: str | None = None,
    chapter_markdown: str | None = None,
    degraded: bool = False,
) -> str:
    if chapter_source is not None:
        chapter_id = getattr(chapter_source, "chapter_id", chapter_id)
        chapter_markdown = getattr(chapter_source, "full_markdown", chapter_markdown)
    if chapter_id is None or chapter_markdown is None:
        raise TypeError("chapter_summary_user_prompt requires chapter_source or both chapter_id and chapter_markdown")
    requirements = [
        "- summarize the chapter at a high level for later scene extraction",
        "- keep the project summary reusable across chapters",
        "- keep the chapter summary focused on events, characters, and settings",
        "- treat the chapter summary as production evidence rather than a reader synopsis: preserve every distinct filmable event, entrance, exit, reveal, decision, object interaction, location/subzone shift, visual continuity state, and uncertainty that later scene, shot, descriptor, or prompt stages would need",
    ]
    if degraded:
        requirements = [
            "- keep both summaries concise but useful",
            "- preserve major events and named entities",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: write project summary plus chapter summary for later scene extraction.",
            packet_contract_block(task_name="chapter_summary", section_names=["project_summary_markdown", "chapter_summary_markdown"]),
            "",
            "Output format:",
            "project_summary_markdown:",
            "[[SECTION project_summary_markdown]]",
            "...project summary markdown...",
            "[[/SECTION]]",
            "",
            "chapter_summary_markdown:",
            "[[SECTION chapter_summary_markdown]]",
            "...chapter summary markdown...",
            "[[/SECTION]]",
            "",
            "Requirements:",
            *requirements,
            "",
            "Chapter source markdown:",
            chapter_markdown,
        ]
    )


def character_extraction_user_prompt(
    *,
    project_slug: str,
    chapter_source=None,
    chapter_id: str | None = None,
    chapter_summary: str | None = None,
    degraded: bool = False,
) -> str:
    if chapter_source is not None:
        chapter_id = getattr(chapter_source, "chapter_id", chapter_id)
    if chapter_id is None or chapter_summary is None:
        raise TypeError("character_extraction_user_prompt requires chapter_source or chapter_id and chapter_summary")
    record_fields = [
        "asset_id",
        "canonical_character_id",
        "aliases",
        "is_fully_identified",
        "manual_description_required",
        "manual_description_reason",
        "clarification_required",
        "clarification_reason",
        "clarification_question",
        "character_type_hint",
        "morphology_hint",
        "scale_hint",
        "renderability_hint",
        "confidence",
        "direct_identity_evidence",
        "direct_visual_evidence",
        "costume_or_covering_evidence",
        "movement_evidence",
        "associated_entities",
        "alias_or_role_evidence",
        "unknowns",
        "source_refs",
    ]
    body_requirements = [
        "- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true",
        "- explain exactly why in manual_description_reason",
        "- do not guess ornate missing details just to avoid the flag",
        "- if the chapter names a character without enough stable identification, set is_fully_identified to false",
        "- use aliases for alternate names or partial labels seen in the chapter",
        "- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question",
        "- if clarification is not required, still include clarification_reason and clarification_question as empty values",
        "- emit one explicit character record per meaningful character mention",
        "- every character record must have a FILMCREATOR_RECORD wrapper with type character",
        "- every character record must include a non-empty markdown section",
        "- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown",
        "- never omit the markdown section for any character record",
        "",
        "Entity taxonomy rules:",
        "- identify what the entity itself appears to be, not what it wears or rides",
        "- do not confuse nearby/associated things with the entity",
        "- if source says a person rides a mount, classify the person separately from the mount",
        "- if source says a character wears foreign/alien/exotic clothing, do not change their species/type",
        "- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown",
        "- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown",
        "- scale_hint: tiny, small, human_scale, large, giant, unknown",
        "- renderability_hint: renderable, context_only, alias_or_role, unknown",
        "- confidence: 0.0 to 1.0 for each type/morphology/renderability hint",
        "- if uncertain, use unknown and explain the missing evidence in the markdown section",
    ]
    if degraded:
        body_requirements = [
            "- keep one record per meaningful character mention",
            "- prefer short facts over long prose",
            "- if uncertain, use clarification_required instead of guessing",
            "- if clarification is not required, still include clarification_reason and clarification_question as empty values",
            "- still emit explicit character records; do not collapse them into index bullets only",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: extract visible and referenced characters into a character index plus one Markdown file per character.",
            packet_contract_block(task_name="character_extraction", section_names=["character_index_markdown"], record_templates=[("character", record_fields, ["markdown"])]),
            "",
            "Literal tag rules:",
            "- begin with [[FILMCREATOR_PACKET]] on its own line",
            "- end with [[/FILMCREATOR_PACKET]] on its own line",
            "- wrap each character item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]",
            "- use [[SECTION character_index_markdown]] and [[SECTION markdown]] exactly as written",
            "- do not invent alternate closing tags such as [[/FIL_RECORD]], [[end_section]], or misspelled FILMCREATOR tags",
            "- do not echo this instruction block back as an example packet; return the actual packet only",
            "",
            "Important rules:",
            *body_requirements,
            "",
            "Asset id rules:",
            "- lowercase snake_case",
            "- stable across later reruns",
            "",
            "Each character Markdown file should include:",
            "- display name and chapter role",
            "- whether the character is physically present, referenced, or uncertain",
            "- physical description that is actually supported by the source",
            "- costume, silhouette, and continuity-critical traits when known",
            "- useful descriptive noun phrases for later render-facing prompt writing",
            "- explicit uncertainty notes when important details are missing",
            "",
            "Chapter summary:",
            chapter_summary,
        ]
    )


def environment_extraction_user_prompt(
    *,
    project_slug: str,
    chapter_source=None,
    chapter_id: str | None = None,
    chapter_summary: str | None = None,
    degraded: bool = False,
) -> str:
    if chapter_source is not None:
        chapter_id = getattr(chapter_source, "chapter_id", chapter_id)
    if chapter_id is None or chapter_summary is None:
        raise TypeError("environment_extraction_user_prompt requires chapter_source or chapter_id and chapter_summary")
    notes = [
        "- include stable environment families rather than every one-off mention",
        "- prefer visible geography and atmosphere over literary abstraction",
    ]
    if degraded:
        notes = ["- keep the environment set small and useful", "- use concise visible descriptions"]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: extract environment families into an environment index plus one Markdown file per environment family.",
            packet_contract_block(task_name="environment_extraction", section_names=["environment_index_markdown"], record_templates=[("environment", ["asset_id"], ["markdown"])]),
            "",
            "Literal tag rules:",
            "- begin with [[FILMCREATOR_PACKET]] on its own line",
            "- end with [[/FILMCREATOR_PACKET]] on its own line",
            "- wrap each environment item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]",
            "- use [[SECTION environment_index_markdown]] and [[SECTION markdown]] exactly as written",
            "- do not echo this instruction block back as an example packet; return the actual packet only",
            "",
            "Asset id rules:",
            "- lowercase snake_case",
            "- stable across later reruns",
            "- emit one explicit environment record per meaningful location or setting family",
            "- every environment record must have a FILMCREATOR_RECORD wrapper with type environment",
            *notes,
            "",
            "Each environment Markdown file should include:",
            "- environment role such as primary, secondary, or transit setting",
            "- architecture or geography",
            "- lighting and atmosphere cues",
            "- scale cues and recurring environmental anchors",
            "- useful descriptive noun phrases for later render-facing prompt writing",
            "",
            "Chapter summary:",
            chapter_summary,
        ]
    )


def scene_decomposition_user_prompt(
    *,
    project_slug: str,
    chapter_source=None,
    chapter_id: str | None = None,
    chapter_summary: str | None = None,
    degraded: bool = False,
) -> str:
    if chapter_source is not None:
        chapter_id = getattr(chapter_source, "chapter_id", chapter_id)
    if chapter_id is None or chapter_summary is None:
        raise TypeError("scene_decomposition_user_prompt requires chapter_source or chapter_id and chapter_summary")
    extra_rules = [
        "Prefer dramatic and staging boundaries, not every paragraph break.",
        "Preserve major narrative function changes as separate scenes.",
        "Do not merge setup, escalation, climax, and aftermath into one scene if they have different emotional or staging functions.",
        "If the chapter includes a reveal, aftermath, or emotional payoff after action, give that material its own scene when possible.",
        "Use a new scene when location, primary objective, or emotional mode changes significantly.",
        "For action chapters, prefer a sequence like: setup scene, escalation scene, climax/action consequence scene, aftermath/reveal scene when the source supports it.",
    ]
    if degraded:
        extra_rules = [
            "Keep scene count practical, but do not collapse the ending payoff into the action scene.",
            "Prefer 4 strong scenes over 3 merged scenes when the chapter clearly contains setup, escalation, consequence, and aftermath.",
            "Create a new scene when a new emotional function begins.",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: break the chapter into a small number of coherent scenes for later beat and clip planning.",
            packet_contract_block(task_name="scene_decomposition", section_names=["scene_index_markdown"], record_templates=[("scene", ["scene_id"], ["markdown"])]),
            "",
            "Literal tag rules:",
            "- begin with [[FILMCREATOR_PACKET]] on its own line",
            "- end with [[/FILMCREATOR_PACKET]] on its own line",
            "- after [[FILMCREATOR_PACKET]], either write metadata lines like task: ... and version: ... or immediately open [[SECTION scene_index_markdown]]",
            "- never output a bare line that only says scene_index_markdown",
            "- wrap each scene item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]",
            "- use [[SECTION scene_index_markdown]] and [[SECTION markdown]] exactly as written",
            "- every scene record must contain a literal line scene_id: SC### before [[SECTION markdown]]",
            "- do not replace [[SECTION markdown]] with [[markdown]] or any alternate tag",
            "- do not echo this instruction block back as an example packet; return the actual packet only",
            "",
            "Scene id rules:",
            "- use SC### only inside the packet",
            "- start at SC001 for this chapter",
            "- do not include the chapter prefix in scene_id values",
            "- the chapter prefix will be applied externally by FilmCreator",
            *extra_rules,
            "- emit one explicit scene record per meaningful scene",
            "- every scene record must have a FILMCREATOR_RECORD wrapper with type scene",
            "Each scene Markdown file should include:",
            "- scene purpose",
            "- scene summary",
            "- participating characters",
            "- participating environments",
            "- dominant emotional shift",
            "- likely visual coverage families",
            "- likely continuity sensitivities",
            "- use plain text field labels like scene purpose: and scene summary: rather than bolded markdown labels",
            "",
            "Chapter summary:",
            chapter_summary,
        ]
    )


def scene_beats_user_prompt(*, project_slug: str, scene_id: str, scene_markdown: str, degraded: bool = False) -> str:
    extra_rules = ["- keep beats reusable for later coverage planning"]
    if degraded:
        extra_rules = ["- keep beats short and practical"]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Scene id: {scene_id}",
            "Task: deepen one scene into reusable beat bundles and update the scene breakdown with clearer staging facts.",
            packet_contract_block(task_name="scene_beats", section_names=["updated_scene_markdown", "beat_index_markdown"], record_templates=[("beat", ["beat_id"], ["markdown"])]),
            "",
            "Output format:",
            "[[FILMCREATOR_PACKET]]",
            "task: scene_beats",
            "version: 1",
            "updated_scene_markdown:",
            "[[SECTION updated_scene_markdown]]",
            "...updated scene markdown...",
            "[[/SECTION]]",
            "",
            "beat_index_markdown:",
            "[[SECTION beat_index_markdown]]",
            "...beat index markdown...",
            "[[/SECTION]]",
            "",
            "[[FILMCREATOR_RECORD]]",
            "type: beat",
            "beat_id: BT001",
            "",
            "[[SECTION markdown]]",
            "# BT001",
            "Short, grounded beat markdown.",
            "[[/SECTION]]",
            "[[/FILMCREATOR_RECORD]]",
            "",
            "Beat id rules:",
            "- use BT### within the scene",
            *extra_rules,
            "- emit one explicit beat record per meaningful beat",
            "- every beat record must have a FILMCREATOR_RECORD wrapper with type beat",
            "Each beat Markdown file should include:",
            "- beat purpose",
            "- beat start state and end state",
            "- character placement and movement logic",
            "- geography, axis, or eyeline facts when relevant",
            "- prop, vehicle, crowd, and environmental state that affects continuity",
            "- likely coverage families",
            "",
            "Scene breakdown markdown:",
            scene_markdown,
        ]
    )


def clip_planning_user_prompt(*, project_slug: str, scene_id: str, scene_markdown: str, beat_index_path: Path, degraded: bool = False) -> str:
    beat_bundle_dir = beat_index_path.parent
    beat_bundles = markdown_bundle(directory=beat_bundle_dir, exclude_names={"BEAT_INDEX.md", "README.md"})
    clip_rules = [
        "- clip = cut",
        "- use clip ids in canonical CL001 format only",
        "- every shot must get its own top-level clip id such as CL001, CL002, CL003, CL004",
        "- never use parent-child or hierarchical clip ids such as CL001_001, CL001-A, CL001.1, CL001/001, CL001a, or CL001_variant",
        "- do not append suffixes like _01, -A, _variant, _alt, or sub-shot fragments to clip ids",
        "- if you feel tempted to write CL001_001 and CL001_002, write CL001 and CL002 instead",
        "- if you need to describe an alternate angle or sub-shot, put that in the clip markdown, not the clip id",
        "- most clips should target around 5 seconds",
        "- treat continuous_follow as rare",
        "- prefer reframe_same_moment, reblock_same_scene, insert, and cutaway when appropriate",
        "- include continuity mode, composition type, starting keyframe strategy, dependency policy, fallback strategy, visible character assets, required refs, optional refs, opening keyframe intent, cut motion intent, and interval beats",
        "- identify one or two strong initial test clips if the scene allows it",
    ]
    if degraded:
        clip_rules = [
            "- keep the first clip roster small and testable",
            "- prefer independent clips",
            "- use simple canonical ids only, such as CL001, CL002, CL003",
            "- never use hierarchical ids like CL001_001 or CL001-A",
            "- do not add suffixes or variants to clip ids",
            "- keep metadata concise but complete",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Scene id: {scene_id}",
            "Task: turn the scene and beat bundles into an ordered clip roster and one clip plan per clip.",
            packet_contract_block(task_name="clip_planning", section_names=["clip_roster_markdown"], record_templates=[("clip", ["clip_id"], ["markdown"])]),
            "",
            "Output format:",
            "[[FILMCREATOR_PACKET]]",
            "task: clip_planning",
            "version: 1",
            "clip_roster_markdown:",
            "[[SECTION clip_roster_markdown]]",
            "...clip roster markdown...",
            "[[/SECTION]]",
            "",
            "[[FILMCREATOR_RECORD]]",
            "type: clip",
            "clip_id: CL001",
            "",
            "[[SECTION markdown]]",
            "# CL001",
            "Short, grounded clip markdown.",
            "[[/SECTION]]",
            "[[/FILMCREATOR_RECORD]]",
            "",
            "Clip planning rules:",
            *clip_rules,
            "- emit one explicit clip record per meaningful clip",
            "- every clip record must have a FILMCREATOR_RECORD wrapper with type clip",
            "",
            "Scene breakdown markdown:",
            scene_markdown,
            "",
            f"Beat index path: {repo_relative(beat_index_path)}",
            beat_index_path.read_text(encoding="utf-8"),
            "",
            "Beat bundle files:",
            beat_bundles or "(none)",
        ]
    )


def character_shared_prompt_user_prompt(*, project_slug: str, asset_id: str, character_breakdown_path: Path, manual_description_path: Path, degraded: bool = False) -> str:
    character_markdown = character_breakdown_path.read_text(encoding="utf-8")
    manual_description = manual_description_path.read_text(encoding="utf-8") if manual_description_path.exists() else ""
    rules = [
        "- purpose and inputs may use stable asset ids",
        "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
        "- keep prompts concrete and visible",
        "- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking",
    ]
    if degraded:
        rules = ["- keep the sections short and usable", "- preserve only the most stable visible traits", "- if uncertain, leave a short continuity note instead of inventing detail"]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Asset id: {asset_id}",
            "Task: write one reusable shared character-reference prompt draft for stable local generation.",
            packet_contract_block(task_name="character_shared_prompts", section_names=[], record_templates=[("character_prompt", ["asset_id"], ["purpose", "positive_prompt", "negative_prompt", "inputs_markdown", "continuity_notes_markdown", "repair_notes_markdown"])]),
            "",
            "Rules:",
            *rules,
            "",
            f"Character breakdown path: {repo_relative(character_breakdown_path)}",
            character_markdown,
            "",
            f"Manual character description path: {repo_relative(manual_description_path)}",
            manual_description or "(missing)",
        ]
    )


def environment_shared_prompt_user_prompt(*, project_slug: str, asset_id: str, environment_breakdown_path: Path, degraded: bool = False) -> str:
    environment_markdown = environment_breakdown_path.read_text(encoding="utf-8")
    rules = [
        "- purpose and inputs may use stable asset ids",
        "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
        "- keep prompts concrete and visible",
        "- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors",
    ]
    if degraded:
        rules = ["- keep the environment identity compact and stable", "- use short visible descriptors only"]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Asset id: {asset_id}",
            "Task: write one reusable shared environment-reference prompt draft for stable local generation.",
            packet_contract_block(task_name="environment_shared_prompts", section_names=[], record_templates=[("environment_prompt", ["asset_id"], ["purpose", "positive_prompt", "negative_prompt", "inputs_markdown", "continuity_notes_markdown", "repair_notes_markdown"])]),
            "",
            "Rules:",
            *rules,
            "",
            f"Environment breakdown path: {repo_relative(environment_breakdown_path)}",
            environment_markdown,
        ]
    )


def scene_brief_markdown(scene_path: Path) -> str:
    sections = split_sections(scene_path.read_text(encoding="utf-8"))
    desired_headings = [
        "Scene Purpose",
        "Scene Summary",
        "Participating Characters",
        "Participating Environments",
        "Dominant Emotional Shift",
        "Likely Visual Coverage Families",
        "Likely Continuity Sensitivities",
    ]
    parts: list[str] = []
    for heading in desired_headings:
        value = sections.get(heading, "").strip()
        if value:
            parts.extend([f"# {heading}", value, ""])
    if parts:
        return "\n".join(parts).strip()
    return scene_path.read_text(encoding="utf-8")


def markdown_bundle(*, directory: Path, exclude_names: set[str]) -> str:
    if not directory.exists():
        return ""
    chunks: list[str] = []
    for path in sorted(directory.glob("*.md")):
        if path.name in exclude_names:
            continue
        chunks.append(f"## {path.name}\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(chunks)


def split_sections(text: str) -> dict[str, str]:
    import re

    heading_pattern = re.compile(r"(?m)^# ([^\r\n]+)\s*$")
    matches = list(heading_pattern.finditer(text))
    if not matches:
        return {}
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = text[start:end].strip()
    return sections
