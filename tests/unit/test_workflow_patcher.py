from orchestrator.common import ROOT
from orchestrator.registry_loader import get_workflow
from orchestrator.workflow_patcher import detect_workflow_format, load_workflow_payload, patch_workflow_payload


def test_patch_text_to_image_workflow_api_prompt() -> None:
    workflow = get_workflow("still.t2i.klein.distilled")
    payload = load_workflow_payload(ROOT / workflow["filename"])

    patched = patch_workflow_payload(
        payload,
        workflow,
        prompt_text="golden hour portrait",
        negative_prompt="low quality",
        save_prefix="filmcreator/demo/RUN_0001_character_reference",
        seed=12345,
    )

    assert detect_workflow_format(payload) == "api_prompt"
    assert patched["9"]["inputs"]["filename_prefix"] == "filmcreator/demo/RUN_0001_character_reference"
    assert patched["76"]["inputs"]["value"] == "golden hour portrait"
    assert patched["75:67"]["inputs"]["text"] == "low quality"
    assert patched["75:73"]["inputs"]["noise_seed"] == 12345


def test_patch_cut_motion_workflow_api_prompt() -> None:
    workflow = get_workflow("video.cut_motion.wan.i2v")
    payload = load_workflow_payload(ROOT / workflow["filename"])

    patched = patch_workflow_payload(
        payload,
        workflow,
        prompt_text="preserve the approved opening frame and use restrained duel motion only",
        negative_prompt="identity drift, new characters, blood",
        save_prefix="filmcreator/demo/RUN_0002_cut_motion",
        seed=2222,
        source_images={"source_frame": "filmcreator/RUN_0002/source_frame.png"},
    )

    assert detect_workflow_format(payload) == "api_prompt"
    assert patched["6"]["inputs"]["text"] == "preserve the approved opening frame and use restrained duel motion only"
    assert patched["7"]["inputs"]["text"] == "identity drift, new characters, blood"
    assert patched["56"]["inputs"]["image"] == "filmcreator/RUN_0002/source_frame.png"
    assert patched["58"]["inputs"]["filename_prefix"] == "filmcreator/demo/RUN_0002_cut_motion"
    assert patched["3"]["inputs"]["seed"] == 2222
