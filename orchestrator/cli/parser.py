from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FilmCreator pipeline CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="Report project artifact status by phase.")
    status.add_argument("project_slug", nargs="?", default="princess_of_mars_test")

    rerun = subparsers.add_parser("rerun", help="Plan a dependency-aware rerun from a phase boundary.")
    rerun.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rerun.add_argument("--from", dest="start_from", required=True)
    rerun.add_argument("--to", dest="stop_at", default=None)
    rerun.add_argument("--execute", action="store_true")
    rerun.add_argument("--chapters", default=None)

    quick = subparsers.add_parser("test-pipeline", help="Run or plan the compact quick-test pipeline.")
    quick.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    quick.add_argument("--chapters", default="2-3")
    quick.add_argument("--refresh-bibles", action="store_true")
    quick.add_argument("--character-limit", type=int, default=3)
    quick.add_argument("--environment-limit", type=int, default=3)
    quick.add_argument("--execute", action="store_true")

    bible = subparsers.add_parser("refresh-bibles", help="Refresh a limited character/environment bible slice.")
    bible.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    bible.add_argument("--character-limit", type=int, default=3)
    bible.add_argument("--environment-limit", type=int, default=3)
    bible.add_argument("--characters", action="store_true")
    bible.add_argument("--environments", action="store_true")
    bible.add_argument("--no-llm", action="store_true")
    bible.add_argument("--force", action="store_true")

    crp = subparsers.add_parser("plan-character-references")
    crp.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    crp.add_argument("--force", action="store_true")
    crp.add_argument("--limit", type=int, default=None)
    crp.add_argument("--variant", action="append", dest="variants")

    crg = subparsers.add_parser("generate-character-references")
    crg.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    crg.add_argument("--limit", type=int, default=None)
    crg.add_argument("--variant", action="append", dest="variants")
    crg.add_argument("--character-id", action="append", dest="character_ids")
    crg.add_argument("--execute", action="store_true")
    crg.add_argument("--seed", type=int, default=None)
    crg.add_argument("--workflow-id", default=None)
    crg.add_argument("--test-slice", action="store_true")

    crc = subparsers.add_parser("register-character-reference-candidate")
    crc.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    crc.add_argument("--character-id", required=True)
    crc.add_argument("--variant", required=True)
    crc.add_argument("--image-path", required=True)

    cra = subparsers.add_parser("approve-character-reference")
    cra.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    cra.add_argument("--candidate-id", required=True)

    crr = subparsers.add_parser("reject-character-reference")
    crr.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    crr.add_argument("--candidate-id", required=True)
    crr.add_argument("--reason", required=True)

    crl = subparsers.add_parser("lock-character-reference")
    crl.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    crl.add_argument("--candidate-id", required=True)

    erp = subparsers.add_parser("plan-environment-references")
    erp.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    erp.add_argument("--force", action="store_true")
    erp.add_argument("--limit", type=int, default=None)
    erp.add_argument("--variant", action="append", dest="variants")

    erg = subparsers.add_parser("generate-environment-references")
    erg.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    erg.add_argument("--limit", type=int, default=None)
    erg.add_argument("--variant", action="append", dest="variants")
    erg.add_argument("--environment-id", action="append", dest="environment_ids")
    erg.add_argument("--execute", action="store_true")
    erg.add_argument("--seed", type=int, default=None)
    erg.add_argument("--workflow-id", default=None)
    erg.add_argument("--test-slice", action="store_true")

    erc = subparsers.add_parser("register-environment-reference-candidate")
    erc.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    erc.add_argument("--environment-id", required=True)
    erc.add_argument("--variant", required=True)
    erc.add_argument("--image-path", required=True)

    era = subparsers.add_parser("approve-environment-reference")
    era.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    era.add_argument("--candidate-id", required=True)

    err = subparsers.add_parser("reject-environment-reference")
    err.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    err.add_argument("--candidate-id", required=True)
    err.add_argument("--reason", required=True)

    erl = subparsers.add_parser("lock-environment-reference")
    erl.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    erl.add_argument("--candidate-id", required=True)

    synth = subparsers.add_parser("run-stage", help="Run a focused implemented pipeline stage.")
    synth.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    synth.add_argument("stage", choices=[
        "scene_contracts",
        "scene_bindings",
        "shot_packages",
        "dialogue_timeline",
        "descriptor_enrichment",
        "prompt_preparation",
        "quality_grading",
    ])
    synth.add_argument("--chapters", default=None)
    synth.add_argument("--force", action="store_true")
    synth.add_argument("--no-llm", action="store_true")
    synth.add_argument("--limit", type=int, default=None)

    legacy = subparsers.add_parser("legacy", help="Run a legacy command through the archived compatibility surface.")
    legacy.add_argument("legacy_args", nargs=argparse.REMAINDER)

    for name in ["shot-keyframes", "audio", "video"]:
        stub = subparsers.add_parser(name, help=f"Future placeholder for {name}.")
        stub.add_argument("project_slug", nargs="?", default="princess_of_mars_test")

    return parser
