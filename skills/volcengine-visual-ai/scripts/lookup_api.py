#!/usr/bin/env python3
"""Search the bundled Volcengine Visual AI API catalog."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CATALOG_PATH = Path(__file__).resolve().parent.parent / "references" / "api-catalog.json"


def load_apis() -> list[dict[str, Any]]:
    with CATALOG_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)["apis"]


def matches(api: dict[str, Any], query: str) -> bool:
    needle = query.casefold()
    fields = [api["name"], api["category"], api["req_key"], *api["source_doc_ids"]]
    return any(needle in str(value).casefold() for value in fields)


def print_table(apis: list[dict[str, Any]]) -> None:
    if not apis:
        print("No matching API.")
        return
    width = max(len(api["name"]) for api in apis)
    for api in apis:
        print(f"{api['name']:<{width}}  {api['req_key']}  [{api['category']}]")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", help="Name, req_key, category, or source document ID")
    parser.add_argument("--list", action="store_true", help="List every published interface")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a compact table")
    args = parser.parse_args()

    apis = load_apis()
    selected = apis if args.list or not args.query else [api for api in apis if matches(api, args.query)]
    if args.json:
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        print_table(selected)
    return 0 if selected else 1


if __name__ == "__main__":
    raise SystemExit(main())
