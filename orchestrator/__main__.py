from importlib import util
from pathlib import Path
import sys


def _load_legacy_main():
    legacy_cli_path = Path(__file__).with_name("cli.py")
    spec = util.spec_from_file_location("orchestrator._legacy_cli", legacy_cli_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load legacy CLI from {legacy_cli_path}")
    module = util.module_from_spec(spec)
    sys.modules.setdefault("orchestrator._legacy_cli", module)
    spec.loader.exec_module(module)
    return module.main


main = _load_legacy_main()


if __name__ == "__main__":
    main()
