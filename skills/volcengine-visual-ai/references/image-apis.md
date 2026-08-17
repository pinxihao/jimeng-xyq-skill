# Image APIs

## Contents

1. Generation models
2. Editing and expansion
3. Extraction
4. Upscaling

## Generation models

### Image Generation 4.6

- `req_key`: `jimeng_seedream46_cvtob`
- Accept up to 14 input images, each up to 15 MB and 4096×4096.
- Prompt length: up to 800 characters.
- Output resolution: 1K–4K; default 2K.
- Output count is constrained by `15 - input_image_count`; the document recommends no more than six outputs.
- `scale` is an integer from 1–100, default 50.
- Use `force_single` when one deterministic output is preferable for latency or cost.

### Image Generation 4.0

- `req_key`: `jimeng_t2i_v40`
- Use the 4.0 interface page for exact request parameters; do not replace it with 4.6 merely because 4.6 is newer.

### Text-to-Image 3.1 and 3.0

- 3.1 `req_key`: `jimeng_t2i_v31`
- 3.0 `req_key`: `jimeng_t2i_v30`
- Prompt length: up to 800 characters.
- `use_pre_llm` defaults to true for prompt enhancement.
- Default seed is `-1` for random generation.
- Default size is 1328×1328; supported sizes extend up to 2K subject to the documented size constraints.

### Image-to-Image 3.0 Intelligent Reference

- `req_key`: `jimeng_i2i_v30`
- Accept one reference image.
- `scale` is 0–1, default 0.5, and controls reference strength.
- Output width/height are in the 512–1536 range subject to documented size constraints.

## Editing and expansion

### Inpainting

- `req_key`: `jimeng_image2image_dream_inpaint`
- Supply the original image and a same-size grayscale mask.
- Mask value 0 keeps the region; 255 repaints the region.
- Prompt length: up to 120 characters.
- Default seed: 101.

### Outpainting

- `req_key`: `jimeng_img2img_seed3_painting_edit`
- Supports equal-ratio expansion, target-aspect expansion, per-edge expansion, and canvas-plus-mask expansion.
- Choose exactly one expansion mode and validate the resulting canvas before submission.

## Extraction

### Product Extraction

- `req_key`: `jimeng_i2i_extract_tiled_images`
- Accept one product image.
- Prompt modes cover apparel, footwear, bags, sofas, daily goods, and jewelry.
- Default output is 2048×2048; width and height are configurable from 1024–4096.
- Default seed: `-1`.

### POD Material Extraction

- `req_key`: `i2i_material_extraction`
- Use for extracting printable/design material from a product rather than isolating the product itself.
- Follow the POD interface page for its dedicated inputs and outputs.

## Intelligent Upscaling

- `req_key`: `jimeng_i2i_seed3_tilesr_cvtob`
- Accept one image up to 4.7 MB and 4096×4096.
- Source aspect ratio must be between 1:3 and 3:1.
- `resolution` supports 4K or 8K; default 4K.
- `scale` is 0–100; default 50.
