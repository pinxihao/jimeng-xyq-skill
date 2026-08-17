# Agent integration playbook

## Contents

1. Explain the product families
2. Collect the minimum requirements
3. Select a capability
4. Prepare the account and credentials
5. Design the integration
6. Validate before submission
7. Operate in production
8. Deliver a useful answer

## 1. Explain the product families

Use Jimeng model APIs when the caller wants direct control over one generation/editing operation, predictable input fields, and model-level output. Examples include text-to-image, inpainting, upscaling, video generation, motion imitation, translation, and OmniHuman.

Use Pippit/Xiaoyunque agent APIs when the caller wants the service to plan or orchestrate a whole video, marketing asset, or short-drama workflow. Agent APIs accept richer creative context but take longer, cost differently, and return multi-stage assets or nested workflow data.

Do not describe Pippit as a drop-in replacement for a Jimeng model API. Do not describe a Jimeng generation endpoint as an autonomous editor or story planner.

## 2. Collect the minimum requirements

Ask only questions that change the recommendation:

- What final artifact is needed: image, edited image, short video, translated video, digital human, marketing film, or episodic drama?
- What source media exist: none, prompt, one image, multiple images, mask, driver video, audio, reference video, or script file?
- What target duration, resolution, aspect ratio, language, and number of outputs are required?
- Are there multiple people/speakers, a non-human character, or a specific person to select?
- Is the user optimizing for quality, speed, cost, or creative automation?
- What peak concurrency and daily volume are expected?
- Will results be shown publicly or used commercially?

Do not ask for AK/SK values. Ask whether the capability is enabled and whether credentials are already configured in the user's environment.

## 3. Select a capability

Follow this routing order:

1. Match the desired artifact and available inputs in `index.md`.
2. Eliminate candidates that violate a hard boundary in `capability-boundaries.md`.
3. Compare quality, automation level, duration, resolution, cost, and latency.
4. Select one primary capability.
5. Name an alternative only when its trade-off is useful.
6. Verify the `req_key` and source IDs in `api-catalog.json`.

If the only supplied source is a landing page with no `req_key`, state that the caller must choose one of its linked subinterfaces before implementation.

## 4. Prepare the account and credentials

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

Run preflight checks in this order:

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
- exact `req_key` and action pair
- required inputs and every material hard limit
- step-by-step submit, poll, parse, and download flow
- production retry, concurrency, expiry, and logging rules
- pricing snapshot labeled with its date and a console-verification warning
- compliance and attribution reminders
- direct links to the selected official pages

If information is missing from the supplied pages, say so explicitly and point to the landing/subinterface page instead of guessing.
