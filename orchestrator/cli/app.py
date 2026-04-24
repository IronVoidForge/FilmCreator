from __future__ import annotations
import json
from .status import run_status
from .rerun import plan_rerun
from .test_pipeline import run_quick_test


def dispatch(args) -> None:
    if args.command == 'status':
        summary = run_status(args.project_slug)
    elif args.command == 'rerun':
        summary = plan_rerun(args.project_slug, args.start_from)
    elif args.command == 'test-pipeline':
        summary = run_quick_test(args.project_slug)
    else:
        raise SystemExit(f'Unknown command: {args.command}')
    print(json.dumps(summary.to_dict(), indent=2))
