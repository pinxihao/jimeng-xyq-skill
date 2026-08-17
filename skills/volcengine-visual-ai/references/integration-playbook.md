# Agent integration playbook

## Contents

1. Explain the execution channels and product families
2. Collect the minimum requirements
3. Select a capability
4. Prepare the account and credentials
5. Design the integration
6. Validate before submission
7. Operate in production
8. Deliver a useful answer

## 1. Explain the execution channels and product families

Use Dreamina CLI when the caller wants a local terminal/Agent workflow backed by an eligible 即梦 membership, OAuth state, and account credits. It is appropriate for interactive or personal automation, local media paths, and CLI-managed task history. Read `dreamina-cli.md` and verify the installed version/help.

Use Pippit personal-Agent CLI/Skills when the caller wants member-account creation through a personal Agent and can configure a Pippit Access Key locally. Read `pippit-personal-agent-cli.md`; never request the key in chat or invent an undocumented credential command.

Use Pippit Web/App when the caller needs a product-only Seedance 2.5 workflow such as segment reshoot, social-link remake, 3D white-model control, canvas editing, character-library reuse, or multi-step long-video extension. Read `pippit-seedance25-product.md` and do not promise the workflow through CLI/API without separate evidence.

Use Jimeng model APIs when the caller wants direct control over one generation/editing operation, predictable input fields, and model-level output. Examples include text-to-image, inpainting, upscaling, video generation, motion imitation, translation, and OmniHuman.

Use Pippit/Xiaoyunque agent APIs when the caller wants the service to plan or orchestrate a whole video, marketing asset, or short-drama workflow. Agent APIs accept richer creative context but take longer, cost differently, and return multi-stage assets or nested workflow data.

Do not describe Pippit as a drop-in replacement for a Jimeng model API. Do not describe a Jimeng generation endpoint as an autonomous editor or story planner. Do not describe Dreamina CLI as a wrapper around the Volcengine API or attach API `req_key`/AK/SK fields to a CLI command. Do not attach Pippit product-UI capabilities to the personal-Agent CLI or public API without current command/interface evidence.

## 2. Collect the minimum requirements

Before collecting creative parameters, run the selected channel's first-use readiness checklist from `configuration-onboarding.md`. If the user requests complete setup, walk through all channels; otherwise configure only the channel required by the task.

Ask only questions that change the recommendation:

- What final artifact is needed: image, edited image, short video, translated video, digital human, marketing film, or episodic drama?
- What source media exist: none, prompt, one image, multiple images, mask, driver video, audio, reference video, or script file?
- What target duration, resolution, aspect ratio, language, and number of outputs are required?
- Are there multiple people/speakers, a non-human character, or a specific person to select?
- Is the user optimizing for quality, speed, cost, or creative automation?
- Does the user want 即梦 OAuth/member-credit terminal automation, Pippit Access-Key personal-Agent automation, Pippit product UI, or an AK/SK-signed server API?
- What peak concurrency and daily volume are expected?
- Will results be shown publicly or used commercially?

Do not ask for AK/SK, Pippit Access Key, OAuth tokens, device codes, or account identifiers. Ask only whether they are securely configured. For APIs, ask whether the capability is enabled and credentials are configured. For Dreamina CLI, ask whether membership, local installation, Web compliance confirmation, and OAuth login are ready. For Pippit personal-Agent work, ask whether membership, Node/npm, installation, and local Access-Key configuration are ready.

## 3. Select a capability

Follow this routing order:

1. Select Dreamina CLI, Pippit personal-Agent CLI/Skills, Pippit Web/App, Jimeng API, or Pippit API in `index.md`.
2. For Dreamina CLI, verify membership, installed version, subcommand help, local inputs, and `dreamina-cli.md` boundaries.
3. For Pippit personal-Agent work, verify membership, installed package/Skill instructions, local secret setup, inputs, and `pippit-personal-agent-cli.md` boundaries.
4. For Pippit product workflows, apply `pippit-seedance25-product.md` material/prompt guidance and keep product claims out of CLI/API implementation advice.
5. For APIs, eliminate candidates that violate a hard boundary in `capability-boundaries.md`.
6. Compare quality, automation level, duration, resolution, cost, and latency.
7. Select one primary capability and name an alternative only when its trade-off is useful.
8. For APIs only, verify the `req_key` and source IDs in `api-catalog.json`.

If the only supplied source is a landing page with no `req_key`, state that the caller must choose one of its linked subinterfaces before implementation.

## 4. Prepare the account and credentials

For Dreamina CLI:

1. Confirm the current membership level and credits.
2. Install/update from the official source only after any required host confirmation.
3. Run `dreamina version` and `dreamina -h`.
4. Start `dreamina login`, but require the user to complete browser authorization manually.
5. Run `dreamina user_credit` as the login/account self-check.
6. For video, complete the first Web generation/compliance confirmation before CLI submission.

For Pippit personal-Agent CLI/Skills:

1. Confirm membership and available credits/resources.
2. Confirm Node.js and `npx` are available.
3. Create the Access Key from the Pippit Web account page.
4. Run the official installer and follow its current local setup instructions.
5. Keep the Access Key in local secret storage; never send it through chat or commit it.
6. Inspect the installed Xyq Skill/Short Drama Skill before issuing a task.

For Jimeng/Pippit APIs:

Guide the user through this order:

1. Register a Volcengine account and complete real-name verification.
2. Open `https://console.volcengine.com/ai/overview`.
3. Enable the selected capability in free-trial or formal mode.
4. Confirm quota, concurrency, billing mode, and resource packages.
5. Create or assign a least-privilege API access key.
6. Store AK/SK in a secret manager or runtime environment.
7. Use an official server SDK where possible to avoid signing errors.

Never place credentials in client-side code, sample output, logs, URLs, Git history, or screenshots.

## 5. Design the integration

For CLI automation, separate command/Skill selection, local-path validation, task-ID storage, bounded querying, downloads, Session selection, version detection, credential isolation, and log redaction. Avoid resubmitting merely because a task remains non-terminal.

For API integration:

Separate the implementation into these components:

- `CapabilityConfig`: endpoint, service, region, version, `req_key`, action pair, limits.
- `PreflightValidator`: prompt and media validation before a billable submission.
- `SignedGatewayClient`: official SDK or canonical request signing.
- `TaskStore`: task/request IDs, request fingerprint, workflow IDs, status, timestamps.
- `Poller`: bounded backoff, jitter, deadline, terminal-state handling.
- `ResultParser`: model-specific nested response parsing.
- `ResultDownloader`: immediate copy to durable object storage.
- `Observability`: structured logs, latency, queue time, completion rate, errors, cost units.
- `PolicyGate`: input/output moderation, rights evidence, labeling, and audit logs.

Keep one request builder per API family. A shared gateway client is appropriate; a shared untyped request body is not.

## 6. Validate before submission

For Dreamina CLI, verify the installed command help, membership/credits, OAuth state, first-video Web confirmation, required explicit resolution flags, duration/model combination, mutually exclusive ratio versus width/height, and readable local media paths. Start with a low-cost smoke test.

For Pippit personal-Agent CLI/Skills, verify the installed package/Skill instructions, membership/resources, local Access-Key state without revealing the key, readable local inputs, and model/workflow availability. Start with a small low-cost task.

For Jimeng/Pippit APIs, run preflight checks in this order:

1. Service is enabled and account is not in arrears.
2. Required fields and workflow identifiers are present.
3. Media URLs are HTTPS and directly downloadable by the service.
4. File type, count, size, dimensions, aspect ratio, frame rate, and duration are within the selected boundary.
5. Prompt/script length and language are supported.
6. Output count, resolution, duration, and ratio form a documented combination.
7. `run_id` or other idempotency value is stable for the logical attempt.
8. Rights, consent, moderation, and public labeling requirements are satisfied.

Reject locally when a deterministic boundary is violated. Do not spend a task submission to discover a file is too large or a mask has the wrong dimensions.

## 7. Operate in production

For Dreamina CLI automation, persist `submit_id`, treat `querying` as non-terminal, avoid duplicate credit-consuming submissions, download deliberately, isolate projects with Sessions, and redact OAuth/account data from logs. For Pippit personal-Agent work, preserve the identifier and Web/result links returned by the installed Skill, query non-terminal tasks, keep the Access Key out of logs, and do not assume Dreamina's Session or `query_result` commands apply.

For API services:

- Queue submissions locally to stay below QPS and concurrency limits.
- Poll with bounded exponential backoff and an overall deadline; do not poll every few milliseconds.
- Store `request_id` for every support case.
- Treat result URLs as temporary and download immediately.
- Separate retryable infrastructure errors from content-risk and validation errors.
- Track billable units, success rate, generation latency, queue latency, download failures, and moderation failures.
- Reconcile console billing with application task records.
- Recheck source pages and console values before launches and after model/version changes.

## 8. Deliver a useful answer

An Agent's final integration answer must include:

- the chosen capability and why it fits
- what it cannot do and when to choose another capability
- exact CLI command and required flags, or for APIs the exact `req_key` and action pair
- required inputs and every material hard limit
- step-by-step submit, poll, parse, and download flow
- production retry, concurrency, expiry, and logging rules
- billing/credit snapshot labeled with its date and a product-or-console verification warning
- compliance and attribution reminders
- direct links to the selected official pages

If information is missing from the supplied pages, say so explicitly and point to the landing/subinterface page instead of guessing.
