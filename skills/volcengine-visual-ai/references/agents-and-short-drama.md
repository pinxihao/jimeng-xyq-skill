# Pippit agents and short-drama pipelines

## Contents

1. Video Agent 1.0
2. Video Agent 2.0
3. Marketing Agent
4. Short Drama Agent

## Video Agent 1.0

- `req_key`: `pippit_iv2v_cvtob`
- Prompt maximum: 2000 characters.
- Accept up to 50 images and videos in total.
- Image limit: 20 MB and 4096×4096 each.
- Video limit: 3 minutes and 200 MB each.
- Supported aspect ratios: 16:9, 9:16, 4:3, and 3:4.
- Duration targets include about 15 seconds, 30 seconds, and 40–60 seconds.

## Video Agent 2.0

Agent 2.0 adds Seedance 2.0 support and one-minute-plus output. A 60-second result can take roughly ten minutes; design polling and user feedback accordingly.

- With reference: `pippit_iv2v_v20_cvtob_with_vinput`
- Without reference: `pippit_iv2v_v20_cvtob`
- With-reference accepts video inputs and bills using total input-video seconds plus output seconds.
- No-reference accepts images rather than reference videos and uses the no-reference billing rule.
- Do not send video inputs to the no-reference interface.

## Marketing Agent

- `req_key`: `pippit_iv2v_cvtob_master`
- Use for agent-planned marketing-video production.
- Treat it as asynchronous and preserve task/request IDs and generated asset URLs.

## Short Drama Agent

Run the stages in order:

```text
script analysis
  -> material/character/scene image design
  -> per-episode shot video generation
  -> per-episode composition
```

### 1. Script analysis

- `req_key`: `pippit_shortplay_cvtob_script_analysis`
- Accept `.txt` or `.docx` scripts up to 100,000 characters.
- Pure-English scripts are not supported by the supplied page.
- Supported ratios: 16:9 and 9:16.
- Persist `assets_id`, `thread_id`, episode IDs, character/scene IDs, and parsed shot IDs.

### 2. Material design

- `req_key`: `pippit_shortplay_cvtob_material_design`
- Generate character, scene, and prop images based on parsed assets.
- Supply a stable optional `run_id` shorter than 32 characters for a logical attempt.

### 3. Shot video generation

- Fast 720P: `pippit_shortplay_cvtob_video_generate_fast720p`
- Pro 720P: `pippit_shortplay_cvtob_video_generate_pro720p`
- Submit per episode/shot and retain every task ID and output URL.
- Confirm all required shots are successful before composition.

### 4. Episode composition

- Fast 720P: `pippit_shortplay_cvtob_video_compose_fast720p`
- Pro 720P: `pippit_shortplay_cvtob_video_compose_pro720p`
- Composition is documented as uncharged, but upstream generation remains billable.
- Composition cannot proceed cleanly when required shots failed. Regenerate or replace failed shots before composing.

### `run_id` rule

Use a stable `run_id` per logical generation attempt. A missing or new value can be treated as a new billable task. Re-querying/reusing the same value in the wrong stage can return `50500`. Store the value together with the stage, episode, shot, and task ID.
