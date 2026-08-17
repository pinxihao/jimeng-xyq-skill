# Agent 首次使用配置向导

Use this checklist before the first real task in a channel and whenever authorization, membership, service enablement, or account context changes. Ask for configuration status, never secret values.

## Contents

- [Onboarding contract](#onboarding-contract)
- [Configuration matrix](#configuration-matrix)
- [Channel setup flows](#channel-setup-flows)
- [Capability enablement](#capability-enablement)
- [Safe confirmation](#safe-confirmation)
- [Required dialogue behavior](#required-dialogue-behavior)

## Onboarding contract

1. Identify the channel needed for the user's requested result.
2. Explain which account, membership, API service, and authorization method that channel uses.
3. Ask whether each required item is already configured using yes/no or status questions.
4. If an item is missing, guide the user through its official product/console flow.
5. Require the user to perform login, approval, key creation, and secret entry themselves.
6. Confirm readiness with a non-sensitive command, console status, or test request.
7. Start with a low-cost smoke test before batch or production work.

Do not force the user to configure unrelated channels. If the user asks for full installation/onboarding, walk through every row in the matrix one at a time.

## Configuration matrix

| Channel or section | Ask the user to confirm | Authorization/billing boundary |
| --- | --- | --- |
| Dreamina 即梦 CLI | Eligible membership, credits, CLI installed, OAuth login complete, first-video Web compliance confirmation when needed | 即梦 OAuth/member benefits; no Volcengine `req_key` or AK/SK |
| Pippit 小云雀 personal-Agent CLI/Skills | Pippit membership/resources, Node/npm readiness, official installer complete, Access Key configured locally, installed Xyq Skill available | Pippit Access Key/member resources; do not reuse Dreamina OAuth or Volcengine AK/SK |
| Pippit Web/App Seedance workflows | Pippit login, membership/model access, enough resources, selected product entry available | Product-account workflow; product UI availability does not prove CLI/API access |
| Jimeng image/video/motion/avatar APIs | Volcengine account and real-name verification, selected capability enabled, AK/SK configured server-side, quota/billing ready | Shared Volcengine signed gateway; exact `req_key` remains capability-specific |
| Pippit Agent/marketing/short-drama APIs | Volcengine account, selected Pippit API capability enabled, AK/SK configured server-side, concurrency/billing ready | Volcengine AK/SK API; not the personal-Agent Pippit Access Key |
| Public/commercial delivery | Rights/consent, moderation, generated-content labeling, filing/attribution requirements confirmed | Compliance gate, not an authentication method |

## Channel setup flows

### Dreamina CLI

Ask:

- “你的即梦会员和积分是否可用？”
- “本机是否已经安装 `dreamina`？”
- “是否已由你本人完成 OAuth 授权？”
- “如果要生成视频，是否已在 Web 端完成首次生成和合规确认？”

If not configured, read `dreamina-cli.md`, guide installation, start the login command, and require the user to complete browser authorization. Confirm with `dreamina version` and `dreamina user_credit`. Do not ask for OAuth tokens, device codes, or account identifiers.

### Pippit personal-Agent CLI/Skills

Ask:

- “你的小云雀会员和生成资源是否可用？”
- “本机是否可以运行 Node.js 和 `npx`？”
- “是否已运行官方安装器并安装 Xyq Skill？”
- “是否已经在小云雀创建 Access Key，并按安装器当前说明在本机完成配置？”

If not configured, read `pippit-personal-agent-cli.md`. Guide the official installer and local setup. Never request, display, copy, or validate the Access Key value through chat. Verify only that the installed Skill can perform its documented non-sensitive account/task preflight.

### Pippit Web/App

Ask whether the user is signed in, has product/member access to the selected Seedance model/workflow, and has sufficient resources. Then read `pippit-seedance25-product.md`. Do not ask for an API credential for a product-only workflow.

### Volcengine Jimeng/Pippit APIs

Ask:

- “火山引擎账号是否已实名？”
- “你要使用的具体能力是否已在视觉智能控制台开通？”
- “AK/SK 是否已在服务端密钥管理器或受保护的运行环境中配置好？”
- “当前配额、并发、计费方式和资源包是否满足这次任务？”

If not configured, read `pricing-and-onboarding.md` and the selected capability reference. Guide the user to the official console, capability enablement, least-privilege key creation, and server-side secret storage. Never ask the user to paste AK/SK into chat and never invent environment-variable names as an official requirement. When giving code, use neutral placeholders or the user's existing secret abstraction.

## Capability enablement

One Volcengine credential set may authenticate multiple enabled APIs, but enablement, quota, billing, and hard limits must be confirmed per selected section:

- image generation/editing/upscaling: read `image-apis.md`;
- video generation/translation/motion/digital humans: read `video-apis.md`;
- Pippit Agent, marketing, and short drama: read `agents-and-short-drama.md`;
- price, concurrency, and activation: read `pricing-and-onboarding.md`;
- public/commercial output: read `compliance.md`.

Do not tell the user to create a separate AK/SK for every model unless their own least-privilege policy requires it. Do require the selected service to be enabled and the exact published `req_key` to be used.

## Safe confirmation

Accept these as readiness evidence:

- the user states that the secret is stored locally/server-side;
- a redacted configuration check succeeds;
- a non-sensitive account/credit command succeeds;
- the official console shows the selected capability as enabled;
- a minimal smoke test returns a task/request ID.

Do not ask for screenshots containing secrets. If troubleshooting needs logs, ask for a redacted excerpt and name the fields to remove: AK, SK, Access Key, OAuth material, cookies, account identifiers, signed query parameters, local personal paths, and full authorization headers.

## Required dialogue behavior

Before the first real task, give a short checklist tailored to the chosen channel. Ask one compact group of status questions, then continue with every item that is already ready. Do not repeat completed setup on every request; remember or re-detect the readiness state within the current project/session.

Use this pattern:

```text
这次任务将使用[渠道/能力]，需要[会员或服务开通]和[授权方式]。
请确认：① [状态项]；② [状态项]；③ [状态项]。
无需把任何密钥发给我；只需告诉我“已在本机/服务端配置”或指出尚未完成的步骤。
```

If a user asks to configure all sections, process them in this order: Dreamina CLI, Pippit personal-Agent CLI/Skills, Pippit Web/App, Volcengine Jimeng APIs, Volcengine Pippit APIs, then compliance. Finish with a redacted readiness summary that contains statuses only, never credential values.
