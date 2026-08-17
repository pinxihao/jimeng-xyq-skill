---
name: volcengine-visual-ai
description: Guide an Agent through selecting, enabling, integrating, validating, and troubleshooting Volcengine Jimeng AI APIs, Dreamina 即梦 CLI, Pippit 小云雀 personal-Agent CLI/Skills, Pippit Web/App Seedance workflows, and Pippit visual-generation APIs. Use for 即梦AI、dreamina CLI、即梦命令行、火山引擎视觉服务、小云雀、Pippit CLI、@pippit-dev/cli、Xyq Skill、Seedance 2.5, CLI installation/login/Access-Key/session/task workflows, API onboarding, req_key and action lookup, image generation/editing/upscaling, video generation/translation, action imitation, OmniHuman digital-human video, marketing-video agents, short-drama or comic-drama pipelines, product/CLI/API capability boundaries, media/prompt validation, asynchronous task polling, pricing, errors, production readiness, and compliance.
---

# Volcengine Visual AI

Use this skill as a source-backed routing and implementation guide. Treat the official pages in `references/documents.json` as authoritative and the summaries as an integration snapshot. Recheck the official page or console before relying on pricing, availability, limits, or legal terms.

## Route the request

1. Read `references/integration-playbook.md` when guiding a new integration or when requirements are incomplete.
2. Read `references/configuration-onboarding.md` before the first real task in a channel, after authorization changes, or when the user asks to configure all modules. Ask for readiness status, never secret values.
3. Read `references/index.md` to select the execution channel and capability.
4. Read `references/dreamina-cli.md` for `dreamina` installation, OAuth, member-credit workflows, commands, sessions, result downloads, local files, version boundaries, or CLI troubleshooting.
5. Read `references/pippit-personal-agent-cli.md` for `@pippit-dev/cli`, Pippit Access Key, Xyq Skill, Xyq Short Drama Skill, personal-Agent installation, results, or task troubleshooting.
6. Read `references/pippit-seedance25-product.md` for Seedance 2.5 product inputs, prompt rules, timecodes, segment reshoot, white-model control, viral remake, canvas, marketing, long-video, storyboard, or product/CLI/API boundaries.
7. Read `references/capability-boundaries.md` to compare every supplied Jimeng and Pippit API function and its hard/soft boundaries.
8. Read `references/common-protocol.md` before producing API request code, polling logic, retries, or operational guidance.
9. Read only the relevant API capability reference:
   - Image generation and editing: `references/image-apis.md`
   - Video, translation, motion, and digital humans: `references/video-apis.md`
   - Pippit agents and short drama: `references/agents-and-short-drama.md`
   - Onboarding and pricing: `references/pricing-and-onboarding.md`
   - Terms, labels, data, and public-service compliance: `references/compliance.md`
10. Read `references/request-recipes.md` when producing implementation pseudocode or reviewing an API integration architecture.
11. Query `references/api-catalog.json` for exact API `req_key` values. Run `scripts/lookup_api.py` when a compact lookup is faster than reading the full catalog.
12. Consult `references/documents.json` for source URLs and document update timestamps.

## Guide the user

- Ask only for missing decisions that change the execution channel or capability: desired result, available source media, target duration/resolution/aspect ratio, edit versus generation, speaker/driver count, expected throughput, and public/commercial use.
- Before the first real task in the chosen channel, ask whether its membership, service enablement, local/server-side authorization, quota, and compliance prerequisites are configured. If the user requests complete onboarding, walk through every channel one at a time.
- Ask only for configuration status. Never ask the user to paste AK/SK, Pippit Access Key, OAuth tokens, device codes, cookies, or authorization headers into chat.
- Recommend one primary capability and mention an alternative only when it materially changes quality, cost, latency, or input requirements.
- Explain the difference between Dreamina CLI, Pippit personal-Agent CLI/Skills, Pippit Web/App product workflows, Jimeng model APIs, and Pippit agent APIs before proposing an architecture.
- Route 即梦 OAuth/member-credit terminal automation to Dreamina CLI. Route Pippit Access-Key/member personal-Agent work to the Pippit CLI/Skills. Route product-exclusive editing and creative workflows to Pippit Web/App. Route AK/SK production services to Jimeng or Pippit APIs.
- For Dreamina CLI, lead through membership/credits, installation, user-controlled OAuth, Web compliance confirmation, command preflight, submission, querying, and download. For Pippit personal-Agent work, lead through membership, installation, local user-controlled Access-Key setup, installed-Skill inspection, task submission/querying, and results. For APIs, lead through account verification, service enablement, AK/SK handling, official SDK/signing, request preflight, polling, monitoring, and compliance.
- Never imply that a product introduction, product UI workflow, or landing page is a callable CLI/API interface.

## Produce implementation guidance

First identify the execution channel:

- **Dreamina CLI:** use `dreamina` commands and OAuth/member state. Do not invent a `req_key`, gateway action, AK/SK requirement, or Volcengine request body.
- **Pippit personal-Agent CLI/Skills:** use the locally installed `@pippit-dev/cli` Skills and Pippit Access Key/member state. Do not invent a credential-storage flag, `req_key`, or Volcengine request body.
- **Pippit Web/App:** use for product-only Seedance 2.5 workflows; do not present UI features as programmable interfaces.
- **Jimeng/Pippit API:** use the signed Volcengine gateway and the exact published `req_key`/action pair. Do not assume CLI flags map one-to-one to API fields.

For CLI guidance:

- Identify which CLI is in use. Run `dreamina version` and relevant help for Dreamina; inspect the installed Pippit package/Skill instructions for Pippit.
- Keep Dreamina OAuth authorization and Pippit Access Key creation/configuration user-controlled.
- Validate local media paths, explicit resolution flags, membership/credits, first-video Web compliance confirmation, and model-specific duration/resolution constraints.
- Preserve the returned task identifier; use the selected CLI's query/download flow and avoid duplicate submissions.
- Keep Access Keys, tokens, device codes, user identifiers, and logs out of chat, source control, shell history, and public issue reports.

For API guidance:

- Name the selected capability, `req_key`, action pair, supported inputs, limits, output shape, and expected billing unit.
- Use `POST https://visual.volcengineapi.com`, `Service=cv`, `Region=cn-north-1`, and `Version=2022-08-31` unless the selected official page explicitly overrides them.
- Prefer the official server SDK for request signing. Never print, hard-code, commit, or ask the user to paste an AK/SK into chat.
- Validate media type, count, size, dimensions, aspect ratio, duration, and prompt length before submission.
- Preserve `task_id`, `request_id`, and workflow identifiers in durable storage. Poll with bounded backoff and stop on terminal states.
- Download result URLs immediately; do not treat temporary result URLs as durable storage.
- Keep model-specific request bodies separate. Do not copy parameters between APIs merely because they share the same gateway actions.
- Distinguish product pages, interface pages, category pages, pricing pages, and legal pages. Never invent a `req_key` for a landing page that does not publish one.

## Use this answer contract

For CLI guidance, provide these sections in order:

1. Which CLI/Skill is appropriate and why instead of product UI or API
2. Membership, credit, platform, credential, and Web-compliance prerequisites
3. Installation/version/help check and user-controlled OAuth or Access-Key setup
4. Exact installed command/Skill flow with required flags and local-path checks
5. Submit, task identifier, polling, download, and Session handling
6. Known capability/version boundaries
7. Logs and troubleshooting without exposing sensitive data

For API integration guidance, provide these sections in order:

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

After installing this skill, begin the first applicable request with the channel-specific readiness checklist from `references/configuration-onboarding.md`. Do not repeat completed onboarding unnecessarily within the same project/session.

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
