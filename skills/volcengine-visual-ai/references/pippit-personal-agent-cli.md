# 小云雀个人 Agent 与 CLI Skill

Source snapshot: ByteDance Lark guide, read 2026-08-17. Treat the installed `@pippit-dev/cli` help and generated Skill files as authoritative for current commands.

## Contents

- [Positioning](#positioning)
- [Prerequisites](#prerequisites)
- [Installation and secure setup](#installation-and-secure-setup)
- [Choose a Skill](#choose-a-skill)
- [Results and task handling](#results-and-task-handling)
- [Failures and boundaries](#failures-and-boundaries)
- [Agent operating rules](#agent-operating-rules)

## Positioning

The Pippit CLI installer adds 小云雀 creation Skills to a personal Agent. This is a member-account workflow authenticated with a Pippit Access Key. It is separate from:

- Dreamina CLI, which uses 即梦 OAuth and member credits;
- Volcengine Pippit APIs, which use AK/SK signing and published `req_key` contracts;
- Pippit Web/App product workflows, whose UI capabilities are not automatically CLI or API capabilities.

Do not add Volcengine gateway actions, `req_key`, or AK/SK fields to a Pippit personal-Agent command unless a separate official API page explicitly requires them.

## Prerequisites

- The account must have an eligible Pippit membership. The source snapshot describes the capability as member-only because generation consumes resources.
- Create an Access Key from Pippit Home: open `https://xyq.jianying.com/home?tab_name=home`, choose the top-right CLI/API entry, and create a key.
- Confirm that the machine can run Node.js and `npx` before installation.
- Verify current membership, credit, regional, and product-access rules in Pippit because they can change.

## Installation and secure setup

Install or update from the official npm package:

```bash
npx @pippit-dev/cli@latest install
```

The supplied page does not publish a stable command-line flag for saving the Access Key. Therefore:

1. Run the installer interactively and follow its current local prompt or generated instructions.
2. Keep the Access Key in the CLI's local credential store, a secret manager, or a protected runtime environment supported by the installed version.
3. Never ask the user to paste the Access Key into chat, source code, shell history, logs, screenshots, Git commits, or issue reports.
4. Inspect the installed CLI help and installed Skill files before inventing a configuration command or environment-variable name.
5. If a key may have been exposed, revoke/rotate it in Pippit and configure a replacement locally.

## Choose a Skill

The installer guide distinguishes two creation routes:

| Need | Use | Boundary |
| --- | --- | --- |
| General creation, marketing assets, or direct image/video model calls | `Xyq Skill` | Verify the installed Skill's supported commands and models |
| Script analysis, asset design, shot generation, composition, or a short-drama project synchronized with Pippit | `Xyq Short Drama Skill` | Use its staged short-drama workflow; do not reduce it to one model call |

Release notes in the supplied page record:

- v1.0.18: canvas control and short-drama canvas-node creation;
- v1.0.1: Seedance 2.0 video generation and direct model selection;
- v1.0.0: multi-turn image/video creation through personal Agents.

These are installer-guide release notes, not a promise that every local installation exposes the same commands. Check the installed package version and Skill instructions.

## Results and task handling

- If the Agent surface can transmit media, completed images or videos may be returned directly.
- Otherwise, return the generated result link.
- A Pippit Web task link is commonly returned so the user can inspect or continue editing the task in Pippit.
- Preserve any task/session identifier returned by the installed Skill. Query a running task instead of resubmitting and consuming credits again.
- Download completed assets deliberately when durable local storage is required; do not assume a result link is permanent.

## Failures and boundaries

Check failures in this order:

1. Access Key is absent, invalid, expired, revoked, or configured in the wrong local context.
2. The account lacks the required membership.
3. Credits/resources are insufficient.
4. The task is still running and should be queried later.
5. The service returned a transient or content-policy error.

Never infer that a Pippit product-page feature is callable from the personal Agent CLI. Seedance 2.5 UI workflows such as segment reshoot, viral remake, 3D white-model control, canvas editing, and five-minute extension must be routed to the product surface unless current installed help explicitly exposes them.

## Agent operating rules

1. Ask whether the user wants Pippit personal-Agent automation, Dreamina CLI, or an AK/SK production API.
2. Confirm membership and local Node/npm readiness before installation.
3. Explain that `npx` downloads and runs the current official installer.
4. Keep Access Key creation and local secret configuration user-controlled.
5. Read the installed Skill and command help before writing exact commands.
6. Start with a small, low-cost task and preserve its task identifier.
7. Query non-terminal tasks instead of submitting duplicates.
8. State the documentation and installed-version snapshot for fast-changing model support.

Official guide: https://bytedance.larkoffice.com/wiki/JUlowWl8Bi6X8fkTKrYc70zRnVc
