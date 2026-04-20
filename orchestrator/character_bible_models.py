from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class CharacterBible:
    character_id: str
    display_name: str
    aliases: List[str] = field(default_factory=list)

    stable_visual_summary: str = ""
    physical_traits: List[str] = field(default_factory=list)
    costume_signature: str = ""

    personality: str = ""
    role: str = ""
    voice_notes: str = ""

    continuity_constraints: List[str] = field(default_factory=list)
    unresolved_ambiguities: List[str] = field(default_factory=list)

    evidence_refs: List[Dict[str, Any]] = field(default_factory=list)
    revision_history: List[Dict[str, Any]] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)
