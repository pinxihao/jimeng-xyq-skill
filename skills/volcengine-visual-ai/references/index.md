# Capability index

This knowledge base summarizes 57 unique official Volcengine Jimeng AI pages supplied by the user. It records 27 published `req_key` values. Use `documents.json` as the canonical source registry and `api-catalog.json` as the canonical interface registry.

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
