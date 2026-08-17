# Video, motion, translation, and avatar APIs

## Contents

1. Video generation
2. Action imitation
3. Video translation
4. OmniHuman 1.5

## Video Generation 3.0 Pro

- `req_key`: `jimeng_ti2v_v30_pro`
- Supports text-to-video and first-frame image-to-video.
- Prompt maximum: 800 characters; the product guidance recommends about 400 or fewer.
- Input image: up to 4.7 MB and 4096×4096, short edge at least 320, aspect ratio no more than 3:1.
- `frames=121` produces about 5 seconds; `frames=241` produces about 10 seconds.
- Select only a documented aspect ratio.

## Video Generation 3.0 720P and 1080P

The supplied pages are interface landing pages, not one universal API definition.

- 720P routes to text-to-video, first-frame, first/last-frame, and camera-motion subinterfaces.
- 1080P routes to text-to-video, first-frame, and first/last-frame subinterfaces.
- Open the chosen subinterface and copy its published `req_key`; do not infer one from the landing page.

## Action Imitation

### Version 2.0

- `req_key`: `jimeng_dreamactor_m20_gen_video`
- Prefer for multi-person scenes and non-human driver subjects.
- Driver video maximum: 30 seconds.
- Output: 720P, 25 fps.
- Product snapshot: about ¥0.4 per output second, concurrency 1. Verify in the console.
- The option to remove the first second defaults to true; set it deliberately.

### Version 1.0

- `req_key`: `jimeng_dream_actor_m1_gen_video_cv`
- Requires a source image and driver video.
- Driver video maximum: 30 seconds.
- Output: 720P, 24 fps.
- Product snapshot: about ¥0.5 per output second, concurrency 1. Verify in the console.

## Video Translation 2.0

- `req_key`: `video_translate_v2_cvtob`
- Intended for one front-facing speaking subject.
- Input duration: 5–180 seconds.
- Input resolution: 360P–1080P; maximum file size 500 MB; frame rate 24–60 fps.
- Supports 29 documented target languages.
- Output frame rate: 25 fps.
- Product snapshot: about ¥0.2 per output second, concurrency 1. Verify in the console.

## OmniHuman 1.5

Use the three-step workflow:

1. Identify subjects with `jimeng_realman_avatar_picture_create_role_omni_v15` using `CVSubmitTask` / `CVGetResult`.
2. Detect/select the intended subject with `jimeng_realman_avatar_object_detection` using synchronous `CVProcess` when subject selection is needed.
3. Generate video with `jimeng_realman_avatar_picture_omni_v15` using `CVSubmitTask` / `CVGetResult`.

Constraints and guidance:

- Supports people, pets, anime characters, and multi-person images.
- Audio must be shorter than 60 seconds; the product guidance recommends 15 seconds or less for better operability.
- Output supports 720P and 1080P.
- Prompt maximum: 300 characters across documented languages.
- Apply `pe_fast_mode` only under the documented subject/composition conditions.
