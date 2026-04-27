from __future__ import annotations

from .models import StageDefinition

STAGES = (
    StageDefinition("01","character_bibles","Character Bibles","synthesize-character-bibles","character_bible"),
    StageDefinition("02","character_visual_evidence","Character Visual Evidence","refine-character-visual-evidence","character_visual_evidence",("character_bibles",)),
    StageDefinition("03","environment_bibles","Environment Bibles","synthesize-environment-bibles","environment_bible",("character_visual_evidence",)),
    StageDefinition("07","scene_contracts","Scene Contracts","synthesize-scene-contracts","scene_contract"),
    StageDefinition("08","scene_bindings","Scene Bindings","synthesize-scene-bindings","scene_binding",("scene_contracts",)),
    StageDefinition("09","shot_packages","Shot Packages","synthesize-shot-packages","shot_package",("scene_bindings",)),
    StageDefinition("10","dialogue_timeline","Dialogue Timeline","synthesize-dialogue-timeline","dialogue_timeline",("scene_bindings",)),
    StageDefinition("11","descriptor_enrichment","Descriptor Enrichment","synthesize-descriptor-enrichment","descriptor",("shot_packages",)),
    StageDefinition("11.5","prompt_preparation","Prompt Preparation","synthesize-prompt-preparation","prompt_package",("descriptor_enrichment",)),
    StageDefinition("12","character_refs","Character References","generate-character-references","character_reference",("prompt_preparation",)),
    StageDefinition("13","environment_refs","Environment References","generate-environment-references","environment_reference",("prompt_preparation",)),
    StageDefinition("14","shot_keyframes","Shot Keyframes",None,"keyframe",("character_refs","environment_refs"),False),
    StageDefinition("15","audio","Audio",None,"audio",("shot_keyframes",),False),
    StageDefinition("16","video","Video",None,"video",("shot_keyframes",),False),
    StageDefinition("17","delivery","Delivery",None,"delivery",("video","audio"),False),
)

BY_KEY = {stage.key: stage for stage in STAGES}
