# Capability index

This knowledge base summarizes 57 unique official Volcengine Jimeng/Pippit pages plus three official ByteDance product/CLI guides supplied by the user. It records 27 published API `req_key` values. Use `documents.json` as the canonical source registry and `api-catalog.json` as the canonical API interface registry.

## Choose an execution channel

Before the first task in the chosen row, read `configuration-onboarding.md` and confirm that its membership, authorization, service enablement, quota, and compliance prerequisites are configured. Ask for status only; never request credential values.

| Need | Use | Do not confuse it with |
| --- | --- | --- |
| Local Agent/terminal automation using an eligible 即梦 membership and credits | Dreamina CLI (`dreamina`) | It does not use Volcengine AK/SK or API `req_key` values |
| Personal-Agent creation using Pippit membership and a locally configured Access Key | Pippit CLI-installed `Xyq Skill` / `Xyq Short Drama Skill` | It is not Dreamina OAuth or a Volcengine AK/SK API |
| Seedance 2.5 segment reshoot, viral remake, white-model control, canvas, long-video extension, or other product workflow | Pippit Web/App | Product UI availability does not prove CLI/API availability |
| Server-side signed integration with model-level control | Jimeng model API | It is not the member-credit CLI workflow |
| Agent-planned marketing, long-form, or short-drama workflows | Pippit 小云雀 Agent API | It is not a single Jimeng model call |

Read `dreamina-cli.md` whenever the user mentions `dreamina`, 即梦 CLI, command-line installation/login, local paths, Session, `submit_id`, `query_result`, or member credits.

Read `pippit-personal-agent-cli.md` for `@pippit-dev/cli`, Pippit Access Key, `Xyq Skill`, or `Xyq Short Drama Skill`. Read `pippit-seedance25-product.md` for Seedance 2.5 product workflows, reference-material limits, prompt/timecode rules, and UI-versus-CLI/API boundaries.

## Choose a capability

| Need | Preferred capability | Key distinction |
| --- | --- | --- |
| General text/image-to-image generation | Image Generation 4.6 | Up to 14 input images; supports 1K–4K and multi-image output |
| Stable text-to-image | Text-to-Image 3.1 or 3.0 | One image per call; prompt enhancement available |
| Reference-image transformation | Image-to-Image 3.0 Intelligent Reference | One reference image; strength is controlled by `scale` |
| Replace a masked region | Inpainting | Original and grayscale mask must have the same dimensions |
| Expand an image canvas | Outpainting | Supports aspect-ratio, edge, and canvas/mask expansion modes |
| Extract a sellable product | Product Extraction | Prompt modes cover apparel, footwear, bags, sofas, daily goods, and jewelry |
| Extract a printable/POD graphic | POD Material Extraction | Separate from product extraction; use its own `req_key` |
| Increase image resolution | Intelligent Upscaling | One image; 4K or 8K output |
| Generate a short high-quality video | Video Generation 3.0 Pro | Text-to-video or first-frame image; 5 or 10 seconds |
| Generate 720P/1080P video | Video Generation 3.0 | Landing pages route to text, first-frame, first/last-frame and camera-motion subinterfaces |
| Drive a person/character with motion | Action Imitation 2.0 | Prefer 2.0 for multi-person and non-human drivers |
| Translate speech in a video | Video Translation 2.0 | One front-facing speaker; 5–180 seconds |
| Generate a talking/dancing avatar | OmniHuman 1.5 | Three-step subject identify/detect/generate workflow |
| Produce an agent-planned video | Pippit Agent 2.0 | Choose with-reference or no-reference interface |
| Produce a marketing video | Pippit Marketing Agent | Agentic marketing-video pipeline |
| Produce episodic short drama/comic drama | Pippit Short Drama Agent | Four stages: analyze, design, generate shots, compose episode |

## Read next

- For first-use authorization/API setup and the module-by-module dialogue checklist, read `configuration-onboarding.md`.
- For first-time integration guidance and required user questions, read `integration-playbook.md`.
- For a function-by-function comparison of hard limits and non-applicable cases, read `capability-boundaries.md`.
- For endpoint, status, retry, URL-expiry, and error handling, read `common-protocol.md`.
- For implementation architecture and pseudocode, read `request-recipes.md`.
- For detailed media constraints and parameter semantics, read the domain reference.
- For exact official links and update dates, search `documents.json` by document ID or title.

## Important distinctions

- Image Generation 4.0 and 4.6 have different `req_key` values; never silently upgrade a request.
- Product Extraction and POD Material Extraction solve different segmentation tasks.
- Video Generation 3.0 720P/1080P pages are landing documents and do not themselves publish one universal `req_key`.
- OmniHuman is not a single-call workflow when the speaker/subject must be selected.
- Pippit Agent 2.0 with-reference bills using both input-video duration and output duration; no-reference accepts images only and bills differently.
- Short-drama composition requires successful shot generation for the episode and does not replace failed shots automatically.
- Dreamina CLI flags and Volcengine API parameters are separate contracts; never translate between them by name alone.
- Pippit product capabilities and Pippit personal-Agent Skills are separate contracts; require installed help or an interface page before promising programmatic support.
