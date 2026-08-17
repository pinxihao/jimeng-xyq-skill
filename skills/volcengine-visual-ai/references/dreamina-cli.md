# Dreamina 即梦 CLI

Source snapshot: ByteDance Lark guide, last modified 2026-08-05; latest listed release v1.4.15 (2026-08-01). Treat current `dreamina version` and command help as authoritative for installed behavior.

## Contents

- [Positioning and routing](#positioning-and-routing)
- [Prerequisites and installation](#prerequisites-and-installation)
- [Login and account checks](#login-and-account-checks)
- [Generation commands](#generation-commands)
- [Asynchronous tasks and downloads](#asynchronous-tasks-and-downloads)
- [Sessions](#sessions)
- [Version-sensitive boundaries](#version-sensitive-boundaries)
- [Local files and troubleshooting](#local-files-and-troubleshooting)
- [Agent operating rules](#agent-operating-rules)

## Positioning and routing

Dreamina CLI is a local command-line client for Agent and automation workflows. It uses an eligible 即梦 membership, OAuth session, and account credits. It is not the Volcengine Visual API gateway.

Use the CLI when the user wants terminal/local-Agent automation and accepts member-credit billing. Use Jimeng/Pippit APIs when the user needs AK/SK-signed server integration, published `req_key` contracts, or production service controls.

Never invent a CLI `req_key`, API action, AK/SK requirement, or `visual.volcengineapi.com` request. Never translate a CLI flag into an API field without checking that API's own documentation.

## Prerequisites and installation

- Availability snapshot: advanced membership or above; generated content consumes membership benefits or credits at the same standard as the Web Agent mode. Verify current product rules.
- Video compliance prerequisite: complete the first video generation and required confirmation in the Web product before submitting video through the CLI.
- Local media paths must exist on the machine running the command. Prefer validated absolute paths in automation.
- Installing or updating executes a remote official installer. Obtain any confirmation required by the host environment before running it.

Install or update:

```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

Verify:

```bash
dreamina -h
dreamina version
```

If `dreamina` is not found, reopen the terminal, apply the installer-provided `PATH` export, then rerun the installer only if needed.

## Login and account checks

Standard flow:

1. Run `dreamina login`.
2. Surface `verification_uri` and `user_code` to the user without publishing other login material.
3. Require the user to open the authorization page and approve OAuth manually.
4. Wait for the command to finish.
5. Run `dreamina user_credit` to verify remaining credits, user identity, and membership level.

Commands:

| Command | Purpose | Boundary |
| --- | --- | --- |
| `dreamina login` | Login or reuse local OAuth state | User completes browser authorization |
| `dreamina login --headless` | Print authorization material without blocking | Follow with `checklogin`; user still authorizes |
| `dreamina login checklogin --device_code=... --poll=30` | Check headless authorization | `--poll=0` checks once |
| `dreamina relogin` | Clear local OAuth state and log in again | Use to switch accounts |
| `dreamina logout` | Clear local OAuth state | Does not delete tasks or configuration |
| `dreamina user_credit` | Check account and credits | Run before diagnosing generation failures |

Do not have an Agent complete the browser authorization. The guide records an `非法应用` failure when an Agent-provided login URL was used; manual Web login and authorization resolved it. Do not expose `device_code`, tokens, logs, or account identifiers.

## Generation commands

Run `dreamina <subcommand> -h` first because model names, required flags, duration, and resolution support change across releases.

| Task | Subcommand | Core flags |
| --- | --- | --- |
| Text to image | `text2image` | `--prompt`, `--ratio` or paired `--width/--height`, `--resolution_type`, `--model_version`, `--generate_num` |
| Image to image | `image2image` | `--images`, `--prompt`, ratio or paired dimensions, `--resolution_type`, `--generate_num` |
| Text to video | `text2video` | `--prompt`, `--duration`, `--ratio`, `--video_resolution`, `--model_version` |
| Image to video | `image2video` | `--image`, `--prompt`, `--duration`, `--video_resolution`, `--model_version` |
| First/last-frame video | `frames2video` | `--first`, `--last`, `--prompt`, `--duration`, `--video_resolution`, `--model_version` |
| Multi-frame video | `multiframe2video` | `--images`, `--prompt`, `--video_resolution`; 3+ images may use transition parameters shown by help |
| Multimodal reference video | `multimodal2video` | `--image`, `--video`, `--audio`, `--prompt`, `--duration`, `--model_version` |
| Image upscale | `image_upscale` | `--image`, `--resolution_type`; 4K/8K require VIP eligibility |

Minimal examples:

```bash
dreamina text2image --prompt="一只戴墨镜的橘猫" --ratio=1:1 --resolution_type=2k --poll=30
dreamina image2image --images ./input.png --prompt="改成水彩风格" --resolution_type=2k --poll=30
dreamina text2video --prompt="镜头推进" --duration=5 --ratio=16:9 --video_resolution=720p --poll=30
dreamina frames2video --first ./start.png --last ./end.png --prompt="季节过渡" --duration=5 --video_resolution=720p --poll=30
dreamina multimodal2video --image ./input.png --audio ./music.mp3 --prompt="生成电影感短片" --model_version=seedance2.5 --duration=5 --video_resolution=720p --poll=30
```

For multiple reference images, pass files with `--images` as supported by the selected subcommand and describe them as `图片1`, `图片2` in upload order. The CLI snapshot does not support the Web `@图片` mention syntax.

## Asynchronous tasks and downloads

Most generation is asynchronous. `--poll=30` submits and waits up to 30 seconds. A non-terminal response can return `querying` with a `submit_id`.

```bash
dreamina query_result --submit_id=YOUR_SUBMIT_ID
dreamina query_result --submit_id=YOUR_SUBMIT_ID --download_dir=./downloads
dreamina list_task --gen_status=success
```

Persist `submit_id` immediately. Do not treat a polling timeout as generation failure. Query again later, and download completed results to a controlled local directory.

## Sessions

Sessions organize task history by project; they do not create separate accounts or billing pools. The default session is `0`.

```bash
dreamina session create "项目名"
dreamina session list
dreamina session search "关键词"
dreamina session rename SESSION_ID "新名字"
dreamina session delete SESSION_ID
dreamina text2image --session=SESSION_ID --prompt="产品海报" --ratio=16:9 --resolution_type=2k --poll=30
```

Deleting a Session should not be presented as deleting generated assets everywhere; verify current Web/mobile retention behavior separately.

## Version-sensitive boundaries

- v1.4.15: `text2video`, `image2video`, `frames2video`, and `multimodal2video` support `--model_version=seedance2.5`; documented output is 480P/720P and 4–30 seconds. Multimodal reference audio/video or audio-only input is documented as 2–30 seconds.
- v1.4.14: image generation requires explicit `--resolution_type`; video generation requires explicit `--video_resolution`.
- v1.4.14: `text2image` and `image2image` accept paired `--width` and `--height`; they cannot be combined with `--ratio`.
- v1.4.14: multi-frame video accepts `--video_resolution` values documented as 720P or 1080P.
- v1.4.12: Seedream 5.0 Pro support was added; reinstall/update if the installed build does not expose it.
- v1.4.10: `text2image` and `image2image` accept `generate_num` from 1 to 10; Seedance 2.0 VIP added 4K support.

The guide's comments mention capabilities under development or not documented in the main command table, including cancellation, digital humans, music/voice, `@` mentions, masks, and video-to-video. Treat comments as non-normative. Verify with the installed command help; never promise availability from a comment.

## Local files and troubleshooting

| Path | Purpose |
| --- | --- |
| `~/.dreamina_cli/tasks.db` | Local task database used by history/query flows |
| `~/.dreamina_cli/logs/` | Runtime logs |
| `~/.dreamina_cli/version.json` | Installer version metadata |
| `~/.dreamina_cli/dreamina/SKILL.md` | CLI-provided Agent instructions |

Troubleshooting order:

1. Run `dreamina version`, update the CLI, and rerun the relevant `-h` command.
2. Run `dreamina user_credit`; resolve login, membership, or credit failures first.
3. For `AigcComplianceConfirmationRequired`, complete the required confirmation in the Web product.
4. For `querying`, preserve `submit_id` and use `query_result`; inspect `list_task` before resubmitting and spending more credits.
5. For media upload errors, validate existence, permissions, size/type, and use a local absolute path; then inspect logs.
6. When escalating, provide the complete command with secrets removed, error text, CLI version, relevant log excerpt, and `submit_id`.

Never publish the full log directory or terminal output without checking for OAuth material, user identifiers, local paths, or other sensitive data.

## Agent operating rules

1. Ask whether the user wants member-credit CLI automation or AK/SK API integration.
2. Before installation, explain that the official command downloads and executes an installer.
3. Keep OAuth authorization user-controlled; do not click the final authorization action for the user.
4. Run version/help checks before constructing model-specific commands.
5. Validate credits, compliance confirmation, required explicit resolution flags, duration, local paths, and mutually exclusive ratio/dimension flags.
6. Default to a low-cost `text2image` smoke test before video or batch generation.
7. Preserve `submit_id`, poll without duplicate resubmission, and download results deliberately.
8. State the document and installed-version snapshot when describing rapidly changing CLI capabilities.

Official guide: https://bytedance.larkoffice.com/wiki/FVTwwm0bGiishxkKOoScdHR2nsg
