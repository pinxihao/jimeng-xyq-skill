# 小云雀 Seedance 2.5 产品使用规范

Source snapshot: ByteDance Lark product guide, last modified 2026-08-14. These are Pippit Web/App product capabilities and operating recommendations unless an installed CLI help page or a published API interface independently confirms exposure.

## Contents

- [Product scope](#product-scope)
- [Inputs and recommended ranges](#inputs-and-recommended-ranges)
- [Prompt construction](#prompt-construction)
- [Product workflows](#product-workflows)
- [Storyboard and white-model guidance](#storyboard-and-white-model-guidance)
- [Channel boundaries](#channel-boundaries)

## Product scope

The supplied guide describes Seedance 2.5 in Pippit with these product-level capabilities:

- 1080p generation, launched in the product on 2026-08-14;
- a single generation lasting 4–30 seconds;
- video extension and a Pippit long-video workflow that can produce up to five minutes through extension;
- up to 30 images, 10 videos, and 10 audio files, with at most 50 reference assets in total;
- timecode control, local/segment editing, white-model motion control, green-screen editing, and improved realism;
- 480p generation followed by product super-resolution up to 4K.

Treat “up to five minutes” as a multi-step Pippit product workflow, not as a 4–30-second single-generation limit exception or a public API guarantee.

## Inputs and recommended ranges

Hard product-level limits in the guide:

| Input | Maximum |
| --- | --- |
| Images | 30; each image up to 4K |
| Videos | 10; total referenced-video duration up to 30 seconds |
| Audio files | 10; total referenced-audio duration up to 30 seconds |
| All reference assets | 50 |

Quality/stability recommendations:

- Use 1–5 video/audio subjects for best stability; 6–10 may work with lower stability.
- Prefer 5–10-second subject video/audio clips; longer clips are less stable.
- Use image references for 1–8 subjects for best stability; 9–12 subjects are less stable.
- With more than five subjects, prefer one view per image. For multiple views, upload separate images instead of one crowded image containing every view.
- For video editing, keep the input video at 20 seconds or less when possible.
- For editing, 1–5 reference images are preferred; 6–8 may work with lower stability.
- More references are not automatically better. Remove irrelevant assets and explicitly state which asset controls which subject, shot, motion, sound, or style.

## Prompt construction

Map assets by upload order and bind every reference explicitly:

```text
图片1作为角色A外观，图片2作为商品外观；视频1只参考运镜，不参考人物；音频1作为背景音乐。
```

Follow these rules:

- Keep the prompt concise when the references already define the result precisely.
- For editing, name the changed range, the original state, the target state, and what must remain unchanged.
- For first/last-frame generation, place the mapping first, for example: `图片1作为首帧，图片5作为尾帧`.
- Make timecode sections continuous without gaps and use roughly one-second precision. Avoid both underspecification and an impossible density of events.
- State negative controls explicitly when needed: no subtitles, no dialogue, no BGM, retain original sound, or do not alter a named subject.
- Use standard shot and camera language. Explain obscure camera terms in plain visual/action language and name the timing/method of transitions.
- Describe action at the sequence level and reserve precise timing for key moments. Describe facial expressions concretely.
- Avoid contradictory instructions across text, reference assets, frames, and storyboards.

For segment editing, use this compact structure:

```text
在[时间范围/画面区域]把[原内容]改为[目标内容]；保留[人物/运镜/声音/背景]；不要改变[明确对象]。
```

Change one major variable at a time when precise control matters.

## Product workflows

The guide documents the following Pippit product workflows:

- **Immersive short film:** choose Seedance 2.5 from the Pippit Web/App creation entry and provide prompt/reference media.
- **Short Drama Agent:** use the Pippit short-drama entry for project-level script, character, shot, and episode workflows.
- **White-model control:** create or import a 3D/dynamic control preview, then use it to guide motion, camera path, composition, and lighting.
- **Viral remake:** paste a supported Douyin/Huoshan/Toutiao link, state the remake intent, and optionally add character references. The product workflow can accept source videos longer than 30 seconds.
- **Segment reshoot:** select only the segment to change, optionally annotate frames or use smart cutting, then describe the local edit. Billing is based on the selected segment duration in the documented product workflow.
- **Marketing video:** create or remake roughly 30-second influencer speech, story ads, brand films, or promotional videos, including multilingual/cross-border variants.
- **Super-long video:** select a target duration and let the product perform extension; the guide describes native product output up to five minutes.
- **Canvas:** combine dialogue with precise canvas editing, parallel sessions, synchronized assets, and short-drama canvas nodes.
- **Creative assistant:** explore trends, creative ideas, and account analysis.
- **Character library:** use the product's reusable character library described as containing more than 7,000 characters.
- **480p plus super-resolution:** generate at 480p and upscale in the product up to 4K when that workflow is appropriate.

Pippit entry: https://xyq.jianying.com/novel/list?enter_from=small_tool

## Storyboard and white-model guidance

For storyboards:

- Keep storyboards at 15 panels or fewer when possible; too many panels can cause still images, omissions, or ordering errors.
- Prefer simple line art or clean panels. Avoid excessive sharpening, clutter, and dense text.
- Map each panel to its story beat and, when useful, a continuous time range.
- Treat storyboard following as semantic guidance, not pixel-perfect track control. Use the product's precise track/fill workflow when exact replacement is required.

For white-model control:

- State exactly what the control video supplies: movement, camera, light, composition, or some combination.
- Map uploaded appearance references to each white-model character.
- Keep the written action consistent with the white-model movement.
- Use the product's 3D director/dynamic preview for timeline keyframes, role actions, camera position/movement, trajectories, and composition replication.

## Channel boundaries

Classify every claim before advising implementation:

| Claim source | What may be promised |
| --- | --- |
| This product guide | Pippit Web/App workflow and recommended use |
| Installed Pippit/Dreamina CLI help | Only commands, flags, models, and limits shown by that installed version |
| Published Volcengine API interface page | Only the documented endpoint, action, `req_key`, fields, and limits |

Do not claim that segment reshoot, social-link remake, white-model director, canvas, character library, creative assistant, five-minute extension, or 4K super-resolution is available through a CLI/API merely because it exists in the product. Route the user to Pippit Web/App unless a current command or interface page proves otherwise.

Official guide: https://bytedance.larkoffice.com/wiki/W5tHwoZIDi12dbk2z3KcFkuUnsf
