from __future__ import annotations

from .parser import build_parser
from .app import dispatch


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    dispatch(args)
