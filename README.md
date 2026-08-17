# Volcengine Visual AI Knowledge Base & Skill

面向 AI Agent 和开发者的即梦 AI / Dreamina CLI / 小云雀个人 Agent、产品工作流与接口知识库。内容整理自用户提供并逐页核对的 57 个火山引擎官方文档页面及 3 份字节跳动即梦/小云雀指南，包含 27 个明确发布的 API `req_key`。

## 内容

- 能力选择与参数边界
- 面向其他 Agent 的需求问诊、能力路由和标准回答格式
- 安装后按板块确认 API、OAuth、Access Key、会员、能力开通和合规状态的安全配置向导
- 通用异步任务、状态、结果和错误处理
- 图片、视频、动作模仿、视频翻译、OmniHuman
- 即梦 CLI 的安装、OAuth、会员积分、生成命令、Session、任务查询和日志排错
- 小云雀个人 Agent CLI/Skills 的安装、Access Key 安全配置、任务路由和结果处理
- Seedance 2.5 素材限制、提示词/时间码规则、产品工作流及 UI/CLI/API 边界
- 小云雀 Agent 1.0/2.0、营销成片、短剧漫剧四阶段流程
- 快速入门、计费快照与服务条款检查清单
- 面向 AI 的机器可读文档/API 目录和查询脚本

## Agent 学习目标

加载 Skill 后，Agent 应能：

1. 解释即梦 CLI、小云雀个人 Agent CLI/Skills、小云雀产品界面、即梦模型 API 与小云雀 Agent API 的差异。
2. 根据目标产物、已有素材、时长、分辨率、画幅、人数和吞吐量选择能力。
3. 明确说明适用场景、不适用场景、硬限制、推荐值、计费和并发风险。
4. 引导完成即梦 CLI 会员/OAuth、小云雀个人 Agent 安装/Access Key 本地安全配置，或 API 实名、能力开通、AK/SK 安全配置、签名、提交、轮询、下载和监控。
5. 编排 OmniHuman 三步流程和短剧漫剧四阶段流程。
6. 提醒结果 URL 有效期、任务保留期、内容风控、合成标识、授权和备案要求。
7. 首次使用某个板块时询问配置状态并引导完成本地/服务端授权，但绝不要求用户把密钥发到聊天中。

Skill 位于 `skills/volcengine-visual-ai`。其中 `references/` 就是知识库本体，支持渐进式读取；`documents.json` 保存官方来源，`api-catalog.json` 保存接口标识。

## 使用

将 `skills/volcengine-visual-ai` 复制到 Codex skills 目录，或直接让 Agent 读取该目录：

```text
使用 $volcengine-visual-ai，帮我选择一个适合“参考商品图生成 9:16 营销视频”的接口，并给出接入方案。
```

查询接口：

```bash
python3 skills/volcengine-visual-ai/scripts/lookup_api.py --list
python3 skills/volcengine-visual-ai/scripts/lookup_api.py 图片生成4.6
python3 skills/volcengine-visual-ai/scripts/lookup_api.py jimeng_seedream46_cvtob
```

校验知识库：

```bash
python3 skills/volcengine-visual-ai/scripts/validate_catalog.py
```

## 重要说明

这是对官方文档的结构化摘要，不是官方 SDK，也不是法律意见。价格、可用性、并发、参数限制和条款可能变化；生产使用前必须核对对应官方页面和火山引擎控制台。仓库不包含也不应保存 AK/SK。
