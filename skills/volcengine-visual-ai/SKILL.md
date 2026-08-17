---
name: volcengine-visual-ai
description: Guide an Agent through selecting, enabling, integrating, validating, and troubleshooting Volcengine Jimeng AI and Pippit visual-generation APIs. Use for 即梦AI、火山引擎视觉服务、小云雀 Agent, API onboarding, req_key and action lookup, image generation/editing/upscaling, video generation/translation, action imitation, OmniHuman digital-human video, marketing-video agents, short-drama or comic-drama pipelines, media/prompt boundary validation, asynchronous task polling, pricing, errors, production readiness, and compliance.
---

# Volcengine Visual AI

Use this skill as a source-backed routing and implementation guide. Treat the official pages in `references/documents.json` as authoritative and the summaries as an integration snapshot. Recheck the official page or console before relying on pricing, availability, limits, or legal terms.

## Route the request

1. Read `references/integration-playbook.md` when guiding a new integration or when requirements are incomplete.
2. Read `references/index.md` to select a capability and workflow.
3. Read `references/capability-boundaries.md` to compare every supplied Jimeng and Pippit function and its hard/soft boundaries.
4. Read `references/common-protocol.md` before producing request code, polling logic, retries, or operational guidance.
5. Read only the relevant capability reference:
   - Image generation and editing: `references/image-apis.md`
   - Video, translation, motion, and digital humans: `references/video-apis.md`
   - Pippit agents and short drama: `references/agents-and-short-drama.md`
   - Onboarding and pricing: `references/pricing-and-onboarding.md`
   - Terms, labels, data, and public-service compliance: `references/compliance.md`
6. Read `references/request-recipes.md` when producing implementation pseudocode or reviewing an integration architecture.
7. Query `references/api-catalog.json` for exact `req_key` values. Run `scripts/lookup_api.py` when a compact lookup is faster than reading the full catalog.
8. Consult `references/documents.json` for source URLs and document update timestamps.

## Guide the user

- Ask only for missing decisions that change the API choice: desired result, available source media, target duration/resolution/aspect ratio, edit versus generation, speaker/driver count, expected throughput, and public/commercial use.
- Recommend one primary capability and mention an alternative only when it materially changes quality, cost, latency, or input requirements.
- Explain the difference between Jimeng model APIs and Pippit agent APIs before proposing an architecture.
- Lead the user through account verification, service enablement, AK/SK handling, official SDK/signing, request preflight, submission, polling, result download, monitoring, and compliance.
- Never imply that a product introduction or landing page is a callable interface.

## Produce implementation guidance

- Name the selected capability, `req_key`, action pair, supported inputs, limits, output shape, and expected billing unit.
- Use `POST https://visual.volcengineapi.com`, `Service=cv`, `Region=cn-north-1`, and `Version=2022-08-31` unless the selected official page explicitly overrides them.
- Prefer the official server SDK for request signing. Never print, hard-code, commit, or ask the user to paste an AK/SK into chat.
- Validate media type, count, size, dimensions, aspect ratio, duration, and prompt length before submission.
- Preserve `task_id`, `request_id`, and workflow identifiers in durable storage. Poll with bounded backoff and stop on terminal states.
- Download result URLs immediately; do not treat temporary result URLs as durable storage.
- Keep model-specific request bodies separate. Do not copy parameters between APIs merely because they share the same gateway actions.
- Distinguish product pages, interface pages, category pages, pricing pages, and legal pages. Never invent a `req_key` for a landing page that does not publish one.

## Use this answer contract

For integration guidance, provide these sections in order:

1. Recommended capability and why
2. Applicability and non-applicable boundaries
3. Required service enablement and credentials
4. `req_key`, endpoint, actions, and workflow
5. Input constraints and preflight checks
6. Submit/query/result handling
7. Billing, concurrency, retention, and retry cautions
8. Compliance and launch checklist
9. Exact official source links and snapshot dates

When writing code, add a configuration layer, preflight validator, task-state store, bounded poller, durable result downloader, and structured logging. Keep secrets out of source and logs.

## Handle uncertainty

- State the document snapshot date when quoting price or concurrency.
- Mark console-controlled values as dynamic and tell the user to verify the current console.
- Treat legal summaries as operational checklists, not legal advice.
- When a source and this knowledge base differ, follow the latest official source and propose updating the catalog.

## Validate changes

Run both checks after editing the knowledge base:

```bash
python3 scripts/validate_catalog.py
python3 scripts/lookup_api.py --list
```
