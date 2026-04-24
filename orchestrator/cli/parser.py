from __future__ import annotations
import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='FilmCreator CLI')
    sp = p.add_subparsers(dest='command', required=True)
    a = sp.add_parser('status'); a.add_argument('project_slug')
    b = sp.add_parser('rerun'); b.add_argument('project_slug'); b.add_argument('--from', dest='start_from', required=True)
    c = sp.add_parser('test-pipeline'); c.add_argument('project_slug')
    return p
