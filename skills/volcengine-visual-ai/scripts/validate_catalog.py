#!/usr/bin/env python3
"""Validate the bundled document and API catalogs without network access."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
REFERENCES = ROOT / "references"
REQUIRED_REFERENCES = {
    "index.md",
    "configuration-onboarding.md",
    "integration-playbook.md",
    "capability-boundaries.md",
    "common-protocol.md",
    "image-apis.md",
    "video-apis.md",
    "agents-and-short-drama.md",
    "request-recipes.md",
    "pricing-and-onboarding.md",
    "compliance.md",
    "dreamina-cli.md",
    "pippit-personal-agent-cli.md",
    "pippit-seedance25-product.md",
    "documents.json",
    "api-catalog.json",
}


def load(name: str) -> dict:
    with (REFERENCES / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> int:
    documents_catalog = load("documents.json")
    api_catalog = load("api-catalog.json")
    documents = documents_catalog["documents"]
    apis = api_catalog["apis"]

    require(len(documents) == documents_catalog["document_count"] == 60, "expected 60 documents")
    require(len(apis) == api_catalog["api_count"] == 27, "expected 27 APIs")
    missing_references = sorted(name for name in REQUIRED_REFERENCES if not (REFERENCES / name).is_file())
    require(not missing_references, f"missing references: {missing_references}")

    doc_ids = [item["id"] for item in documents]
    require(len(doc_ids) == len(set(doc_ids)), "document IDs must be unique")
    urls = [item["url"] for item in documents]
    require(len(urls) == len(set(urls)), "document URLs must be unique")
    for item in documents:
        parsed = urlparse(item["url"])
        require(parsed.scheme == "https", f"non-HTTPS source: {item['url']}")
        require(
            parsed.netloc in {"docs.volcengine.com", "bytedance.larkoffice.com"},
            f"unexpected source host: {item['url']}",
        )
        require(item["id"] in parsed.path, f"document ID missing from URL: {item['id']}")

    req_keys = [item["req_key"] for item in apis]
    require(len(req_keys) == len(set(req_keys)), "API req_key values must be unique")
    published_keys = {key for item in documents for key in item["req_keys"]}
    require(set(req_keys) == published_keys, "API catalog and document req_key sets differ")

    known_docs = set(doc_ids)
    for api in apis:
        require(api["source_doc_ids"], f"missing source document for {api['req_key']}")
        unknown = set(api["source_doc_ids"]) - known_docs
        require(not unknown, f"unknown source documents for {api['req_key']}: {sorted(unknown)}")
        require(bool(api["submit_action"]), f"missing action for {api['req_key']}")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    placeholder = "TO" + "DO"
    require(placeholder not in skill_text, "SKILL.md still contains template markers")
    require(skill_text.startswith("---\nname: volcengine-visual-ai\n"), "invalid skill frontmatter")
    for name in REQUIRED_REFERENCES:
        require(name in skill_text or name in {"documents.json", "api-catalog.json"}, f"SKILL.md does not route to {name}")

    boundary_text = (REFERENCES / "capability-boundaries.md").read_text(encoding="utf-8")
    for req_key in req_keys:
        require(req_key in boundary_text, f"boundary guide does not cover {req_key}")

    print(f"OK: {len(documents)} documents, {len(apis)} APIs, {len(req_keys)} unique req_key values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
