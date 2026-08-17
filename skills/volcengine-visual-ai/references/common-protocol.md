# Common API protocol

## Contents

1. Gateway and signing
2. Asynchronous workflow
3. Status and persistence
4. Result handling
5. Errors and retries
6. Preflight checklist

## Gateway and signing

- Endpoint: `POST https://visual.volcengineapi.com`
- Content type: `application/json`
- Service: `cv`
- Region: `cn-north-1`
- Version: `2022-08-31`
- Sign requests with Volcengine AK/SK signing or an official server SDK. Keep credentials in a secret manager or environment variables.

Most interfaces use:

- Submit: `Action=CVSync2AsyncSubmitTask`
- Query: `Action=CVSync2AsyncGetResult`

OmniHuman uses different actions by step:

- Subject identification and final generation use `CVSubmitTask` / `CVGetResult`.
- Subject detection uses synchronous `CVProcess`.

Always confirm the selected API page before fixing an action pair in code.

## Asynchronous workflow

1. Validate the request locally.
2. Submit with the exact model `req_key`.
3. Require outer `code == 10000` before reading task data.
4. Persist `task_id` and `request_id` with the request fingerprint and submit time.
5. Poll the matching query action with bounded exponential backoff and jitter.
6. Treat `done` as success. Treat `not_found`, `expired`, or an explicit failure/error state as terminal.
7. Parse model-specific response data; it may contain nested JSON strings.
8. Download results to durable object storage immediately.

Common nonterminal states include `processing`, `in_queue`, and `generating`. Tasks are generally queryable for about 12 hours. Do not poll indefinitely.

## Persistence and idempotency

Persist at least:

- capability name and `req_key`
- sanitized request fingerprint
- task and request IDs
- workflow IDs such as `assets_id`, `thread_id`, `EpisodeID`, and `run_id`
- current status, poll count, timestamps, and last error
- copied durable output URLs and checksums

For short-drama APIs, `run_id` is part of the idempotency and billing contract. Use a stable value shorter than 32 characters for a logical attempt. Reusing or omitting it incorrectly can create a new billable task or produce a query error.

## Result URLs

- Image result URLs are commonly valid for about 24 hours.
- Video result URLs are commonly valid for about 1 hour.
- These lifetimes vary by API. Download immediately and retain the original `request_id` for support.

## Errors and retries

| Code | Meaning | Default handling |
| --- | --- | --- |
| `50411` | Input image risk/control failure | Do not blindly retry; change or review input |
| `50511` | Output image risk/control failure | Retry only when the API page permits it |
| `50412` | Input text risk/control failure | Review prompt and policy |
| `50512` | Output text risk/control failure | Retry only when documented |
| `50413` | Sensitive/copyright term | Change the prompt or asset; do not evade safeguards |
| `50429` | QPS exceeded | Back off and rate-limit submissions |
| `50430` | Concurrent-task limit exceeded | Queue locally and retry later |
| `50500`, `50501` | Internal/task error | Follow the selected API page; retry only when marked retryable |

Do not implement one global retry rule. Product pages differ on whether internal and output-risk failures are billable or retryable.

## Preflight checklist

- Confirm the service is enabled in the Visual Intelligence console.
- Confirm formal/free status, concurrency, quota, and billing mode.
- Check every input URL is directly downloadable by the service.
- Check file type, size, dimensions, aspect ratio, duration, frame rate, and count.
- Check prompt language and length.
- Confirm watermark and AIGC metadata requirements.
- Confirm public-facing labeling, user authorization, content moderation, logging, and retention obligations.
- Record the official page URL and its update timestamp in implementation notes.
