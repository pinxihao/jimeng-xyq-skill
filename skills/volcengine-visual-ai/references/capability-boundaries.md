# Jimeng and Pippit capability boundaries

## Contents

1. How to read the boundaries
2. Jimeng image functions
3. Jimeng video, motion, translation, and avatar functions
4. Pippit/Xiaoyunque agent functions
5. Cross-function boundaries

## 1. How to read the boundaries

Hard limits are request-rejection or workflow-breaking boundaries stated in the supplied pages. Recommendations are quality/latency guidance and can be tuned. Pricing and concurrency are snapshots and must be verified in the console.

## 2. Jimeng image functions

### Image Generation 4.6

- Use for: prompt generation, multi-image reference, general image creation.
- `req_key`: `jimeng_seedream46_cvtob`.
- Inputs: prompt plus 0–14 images.
- Hard limits: 800-character prompt; each image ≤15 MB and ≤4096×4096; output resolution 1K–4K; output count ≤`15 - input_count`.
- Controls: `scale` 1–100, default 50; default resolution 2K; `force_single` for one output.
- Recommendation: keep outputs ≤6.
- Do not use for: pixel-precise mask editing, dedicated product cutout, or simple upscaling.

### Image Generation 4.0

- Use for: 4.0 generation behavior required by an existing integration.
- `req_key`: `jimeng_t2i_v40`.
- Boundary: follow document 1817045 for the exact field combinations; do not send 4.6-only fields.
- Do not use for: an automatic “latest model” upgrade without output regression testing.

### Text-to-Image 3.1

- Use for: single-image text generation with the 3.1 model.
- `req_key`: `jimeng_t2i_v31`.
- Hard limits: prompt ≤800 characters; output size must satisfy documented limits up to 2K.
- Defaults: 1328×1328, `seed=-1`, `use_pre_llm=true`.
- Do not use for: reference-image transformation or multi-image composition.

### Text-to-Image 3.0

- Use for: single-image text generation with a stable 3.0 integration.
- `req_key`: `jimeng_t2i_v30`.
- Hard limits/defaults: same high-level prompt and size boundaries summarized for 3.1; verify model-specific fields in document 1616429.
- Do not use for: image-conditioned generation.

### Image-to-Image 3.0 Intelligent Reference

- Use for: transform one reference image while controlling reference strength.
- `req_key`: `jimeng_i2i_v30`.
- Inputs: one reference image plus prompt.
- Hard limits: output width/height in the documented 512–1536 range.
- Control: `scale` 0–1, default 0.5.
- Do not use for: exact masked replacement, canvas extension, or multiple reference images.

### Inpainting

- Use for: replace or regenerate a selected image region.
- `req_key`: `jimeng_image2image_dream_inpaint`.
- Inputs: original image, grayscale mask, prompt.
- Hard limits: original and mask dimensions must match; prompt ≤120 characters.
- Mask semantics: 0 keeps pixels; 255 repaints pixels.
- Default: seed 101.
- Do not use for: global style transfer or expanding beyond the original canvas.

### Outpainting

- Use for: expand content beyond the original canvas.
- `req_key`: `jimeng_img2img_seed3_painting_edit`.
- Modes: equal-ratio, target-aspect, per-edge, or explicit canvas plus mask.
- Boundary: choose one coherent expansion mode and validate canvas/mask geometry.
- Do not use for: editing an interior region without changing the canvas.

### Product Extraction

- Use for: isolate a sellable product from one image.
- `req_key`: `jimeng_i2i_extract_tiled_images`.
- Inputs: one image and one of the documented product prompt modes.
- Modes: apparel, footwear, bags, sofas, daily goods, jewelry.
- Output: default 2048×2048; width/height 1024–4096; default seed `-1`.
- Do not use for: extracting a printable artwork from a product surface.

### POD Material Extraction

- Use for: extract printable/design material for print-on-demand customization.
- `req_key`: `i2i_material_extraction`.
- Boundary: treat it as a separate task from product extraction and follow document 1925087 for request fields.
- Do not use for: general background removal when the desired asset is the physical product.

### Intelligent Upscaling

- Use for: improve one image to 4K or 8K.
- `req_key`: `jimeng_i2i_seed3_tilesr_cvtob`.
- Hard limits: one image; ≤4.7 MB; ≤4096×4096; aspect ratio from 1:3 to 3:1.
- Controls: 4K/8K, default 4K; `scale` 0–100, default 50.
- Do not use for: semantic editing, object replacement, or new composition.

## 3. Jimeng video, motion, translation, and avatar functions

### Video Generation 3.0 Pro

- Use for: short high-quality text-to-video or first-frame image-to-video.
- `req_key`: `jimeng_ti2v_v30_pro`.
- Hard limits: prompt ≤800 characters; image ≤4.7 MB and ≤4096×4096; short edge ≥320; image aspect ratio ≤3:1.
- Duration: `frames=121` ≈5 seconds; `frames=241` ≈10 seconds.
- Recommendation: keep prompt around 400 characters or fewer.
- Do not use for: minute-long agent-planned videos or driver-motion transfer.

### Video Generation 3.0 720P

- Use for: 720P text, first-frame, first/last-frame, or camera-motion generation.
- Boundary: document 1792710 is a landing page. Select its linked subinterface and use the published subinterface `req_key`.
- Do not invent one universal `req_key`.

### Video Generation 3.0 1080P

- Use for: 1080P text, first-frame, or first/last-frame generation.
- Boundary: document 1792711 is a landing page. Select its linked subinterface and use the published subinterface `req_key`.
- Camera-motion routing is not listed in the supplied 1080P landing page.

### Action Imitation 1.0

- Use for: transfer motion from one driver video to an image using the original model.
- `req_key`: `jimeng_dream_actor_m1_gen_video_cv`.
- Hard limit: driver video ≤30 seconds.
- Output: 720P, 24 fps.
- Snapshot: concurrency 1; about ¥0.5/output second.
- Do not use when multi-person/non-human support requires version 2.0.

### Action Imitation 2.0

- Use for: multi-person and non-human motion driving.
- `req_key`: `jimeng_dreamactor_m20_gen_video`.
- Hard limit: driver video ≤30 seconds.
- Output: 720P, 25 fps.
- Behavior: removing the first second defaults to true; set it explicitly.
- Snapshot: concurrency 1; RTF about 18; about ¥0.4/output second.
- Do not use for lip-synced translation or audio-driven avatar generation.

### Video Translation 2.0

- Use for: translate a speaking person's video while adapting speech/lip movement.
- `req_key`: `video_translate_v2_cvtob`.
- Hard limits: one front-facing speaker; 5–180 seconds; 360P–1080P; ≤500 MB; 24–60 fps.
- Output: 25 fps; 29 documented target languages.
- Snapshot: concurrency 1; about ¥0.2/output second.
- Do not use for: multiple simultaneous speakers, voice-free video, or arbitrary video editing.

### OmniHuman 1.5

- Use for: drive a person, pet, anime character, or selected subject with audio.
- Step 1 `req_key`: `jimeng_realman_avatar_picture_create_role_omni_v15`.
- Step 2 `req_key`: `jimeng_realman_avatar_object_detection`.
- Step 3 `req_key`: `jimeng_realman_avatar_picture_omni_v15`.
- Hard limits: audio <60 seconds; prompt ≤300 characters.
- Output: 720P or 1080P.
- Recommendation: audio ≤15 seconds for easier latency/quality control.
- Boundary: use subject detection when the source contains multiple candidate subjects.
- Do not use for: motion copied from a driver video; use Action Imitation instead.

## 4. Pippit/Xiaoyunque agent functions

### Intelligent Video Agent 1.0

- Use for: agent-planned video from a prompt and mixed image/video references.
- `req_key`: `pippit_iv2v_cvtob`.
- Hard limits: prompt ≤2000 characters; ≤50 media items; image ≤20 MB and ≤4096×4096; video ≤3 minutes and ≤200 MB.
- Ratios: 16:9, 9:16, 4:3, 3:4.
- Duration targets: about 15s, 30s, or 40–60s.
- Do not use for: a single direct model shot where latency and parameter control matter more than planning.

### Intelligent Video Agent 2.0 with reference

- Use for: longer agent-planned videos with image/video references and Seedance 2.0 support.
- `req_key`: `pippit_iv2v_v20_cvtob_with_vinput`.
- Boundary: video references are accepted and their total duration contributes to billing with output duration.
- Expectation: a 60-second result can take roughly ten minutes.
- Do not use when no video reference is needed and the no-reference billing/input model is preferable.

### Intelligent Video Agent 2.0 without reference

- Use for: agent-planned videos from prompt and image inputs without reference video.
- `req_key`: `pippit_iv2v_v20_cvtob`.
- Hard boundary: do not send reference videos to this interface.
- Expectation: supports one-minute-plus output; design long-running polling and progress UX.

### Marketing Video Agent

- Use for: autonomous marketing-film planning and generation.
- `req_key`: `pippit_iv2v_cvtob_master`.
- Boundary: treat outputs and intermediate assets as an agent workflow, not one model frame/shot.
- Do not use when the caller needs a deterministic single-shot generation interface.

### Short Drama/Comic Drama: script analysis

- Use for: parse a script into episodes, assets, scenes, and shots.
- `req_key`: `pippit_shortplay_cvtob_script_analysis`.
- Hard limits: `.txt` or `.docx`; ≤100,000 characters; pure-English script unsupported; ratio 16:9 or 9:16.
- Persist: `assets_id`, `thread_id`, `EpisodeID`, asset IDs, shot IDs.

### Short Drama/Comic Drama: material design

- Use for: generate character, scene, and prop images from parsed assets.
- `req_key`: `pippit_shortplay_cvtob_material_design`.
- Boundary: keep asset IDs aligned with the script-analysis result.
- Idempotency: optional `run_id` <32 characters; store it per logical attempt.

### Short Drama/Comic Drama: shot generation

- Fast 720P `req_key`: `pippit_shortplay_cvtob_video_generate_fast720p`.
- Pro 720P `req_key`: `pippit_shortplay_cvtob_video_generate_pro720p`.
- Use fast for throughput/cost-sensitive drafts and Pro for the documented higher-quality path.
- Boundary: generate and track every required episode shot before composition.

### Short Drama/Comic Drama: episode composition

- Fast 720P `req_key`: `pippit_shortplay_cvtob_video_compose_fast720p`.
- Pro 720P `req_key`: `pippit_shortplay_cvtob_video_compose_pro720p`.
- Billing: composition is documented as uncharged; upstream generation is billable.
- Hard boundary: failed/missing required shots prevent a valid composition; regenerate or replace them first.
- Keep fast generation with fast composition and Pro generation with Pro composition unless the official page documents another combination.

## 5. Cross-function boundaries

- Temporary outputs: image URLs are commonly about 24 hours; video URLs commonly about 1 hour. Download immediately.
- Task lookup: asynchronous tasks are generally retained for about 12 hours.
- Result safety: `code=10000` only validates the outer request; still inspect task status and result payload.
- Concurrency: account/service console values override documentation snapshots.
- Retry: never retry input-risk or deterministic validation failures unchanged.
- Pricing: quote only with the source update date and tell the user to verify the console.
- Public use: preserve synthetic-media labels, display required Jimeng attribution, and implement moderation, rights, filing, and logging controls.
