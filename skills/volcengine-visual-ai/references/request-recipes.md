# Request and workflow recipes

## Contents

1. Configuration contract
2. Generic asynchronous recipe
3. Preflight validation recipe
4. Polling and retry recipe
5. OmniHuman recipe
6. Pippit Agent recipe
7. Short-drama recipe
8. Production logging contract

These are language-neutral implementation recipes, not copy-paste signed requests. Use an official Volcengine server SDK or canonical signing implementation.

## 1. Configuration contract

Store capability configuration separately from user input:

```json
{
  "endpoint": "https://visual.volcengineapi.com",
  "service": "cv",
  "region": "cn-north-1",
  "version": "2022-08-31",
  "req_key": "jimeng_seedream46_cvtob",
  "submit_action": "CVSync2AsyncSubmitTask",
  "query_action": "CVSync2AsyncGetResult",
  "source_document_ids": ["2275082", "2288388"]
}
```

Load AK/SK from a secret manager/runtime environment. Do not put secrets in this configuration object when it may be logged.

## 2. Generic asynchronous recipe

```text
function start_generation(capability, user_input):
    config = load_capability(capability)
    normalized = normalize(user_input)
    validation = preflight(config, normalized)
    if validation.failed:
        return local_validation_error(validation)

    fingerprint = hash(config.req_key + canonical_json(normalized))
    existing = task_store.find_active(fingerprint)
    if existing:
        return existing

    response = signed_post(
        endpoint=config.endpoint,
        query={Action: config.submit_action, Version: config.version},
        body={req_key: config.req_key, ...normalized}
    )

    require response.code == 10000
    task = persist(response.task_id, response.request_id, fingerprint)
    enqueue_poll(task)
    return task
```

Do not assume every API returns IDs at the same JSON path. Map the exact model response in a model-specific parser.

## 3. Preflight validation recipe

```text
function preflight(config, request):
    check_required_fields(request)
    check_prompt_length(request.prompt, config.prompt_limit)
    check_media_count(request.media, config.media_count)

    for media in request.media:
        check_https_downloadable_url(media.url)
        inspect_metadata_without_full_decode_when_possible(media)
        check_type_size_dimensions_ratio_duration_fps(media, config.limits)

    check_output_resolution_ratio_duration_count(request, config.output_limits)
    check_workflow_ids(request, config.workflow)
    check_idempotency(request.run_id, config.run_id_rule)
    check_rights_consent_and_policy(request)
    return all_errors_and_warnings
```

Return all deterministic validation errors at once so the caller can repair the request without repeated submissions.

## 4. Polling and retry recipe

```text
terminal_success = {"done"}
terminal_failure = {"not_found", "expired", "failed", "error"}
nonterminal = {"processing", "in_queue", "generating"}

function poll(task):
    deadline = min(task.created_at + configured_timeout, task.created_at + 12h)
    delay = initial_delay

    while now() < deadline:
        response = signed_post(query={Action: query_action, Version: version},
                               body={req_key: req_key, task_id: task.id})
        require response.code == 10000
        status = parse_status(response)
        task_store.record_poll(task, status, response.request_id)

        if status in terminal_success:
            result = parse_model_result(response)
            durable = download_all_temporary_results(result)
            task_store.complete(task, durable)
            return durable

        if status in terminal_failure:
            task_store.fail(task, status, parse_error(response))
            return failure

        sleep(delay + jitter)
        delay = min(delay * multiplier, max_delay)

    task_store.timeout(task)
```

Retry policy:

- Rate/concurrency errors: retry with backoff and local queuing.
- Transient transport errors: retry the query; retry submit only when idempotency is guaranteed.
- Input validation/content-risk errors: do not retry unchanged.
- Internal/output-risk errors: follow the selected API page because retry rules differ.

## 5. OmniHuman recipe

```text
identify_task = submit(CVSubmitTask,
    req_key="jimeng_realman_avatar_picture_create_role_omni_v15",
    image=source_image)
roles = poll(CVGetResult, identify_task)

if roles contain multiple candidate subjects:
    detection = call_sync(CVProcess,
        req_key="jimeng_realman_avatar_object_detection",
        image=source_image)
    selected_role = choose_with_user_or_business_rule(detection)
else:
    selected_role = roles.only_role

generation_task = submit(CVSubmitTask,
    req_key="jimeng_realman_avatar_picture_omni_v15",
    role=selected_role,
    audio=audio,
    resolution=target_resolution,
    prompt=prompt)
video = poll(CVGetResult, generation_task)
download(video)
```

Reject audio ≥60 seconds. Prefer shorter segments when product UX allows it.

## 6. Pippit Agent recipe

Choose the interface before building the body:

```text
if reference_videos are present:
    req_key = "pippit_iv2v_v20_cvtob_with_vinput"
else:
    req_key = "pippit_iv2v_v20_cvtob"
```

Then:

1. Validate prompt, media count/type/size, target ratio, and duration.
2. Explain that agent generation is long-running; expose progress from task status.
3. Preserve all intermediate assets returned by the agent.
4. Download the final video and relevant editable assets.
5. Record billable input-video and output duration for reconciliation.

Do not coerce reference videos into the no-reference endpoint.

## 7. Short-drama recipe

```text
analysis = run("pippit_shortplay_cvtob_script_analysis", script, ratio)
store(analysis.assets_id, analysis.thread_id, analysis.episodes)

materials = run("pippit_shortplay_cvtob_material_design",
                assets=analysis.assets,
                run_id=stable_id("materials", project_revision))
store(materials)

for episode in analysis.episodes:
    for shot in episode.shots:
        task = run(video_generation_req_key,
                   episode_id=episode.id,
                   shot_id=shot.id,
                   assets=materials,
                   run_id=stable_id("shot", episode.id, shot.id, attempt))
        store(task)

    require every required shot is done
    composition = run(matching_composition_req_key,
                      episode_id=episode.id,
                      shot_results=successful_shots)
    download(composition.video)
```

Use `.txt` or `.docx`, ≤100,000 characters, and 16:9 or 9:16. Do not submit a pure-English script under the supplied constraint. Keep `run_id` under 32 characters and scope it to stage/entity/attempt.

## 8. Production logging contract

Log these non-secret fields:

- capability, `req_key`, action, API version
- internal job ID, task ID, request ID
- sanitized request fingerprint, not raw personal media or prompt when sensitive
- input count/type/size/duration summary
- output count/duration/resolution summary
- submit, queue, generation, poll, and download timestamps
- status transitions, error code, retry decision
- billable unit estimate and console reconciliation key
- durable object path/checksum and temporary URL expiry time
- policy decision, consent/provenance reference, labeling status

Never log AK, SK, authorization headers, signed query strings, full personal media URLs, or unredacted sensitive prompts.
