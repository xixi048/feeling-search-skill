# 商店上架物料包 · feeling-search

> 用途：把 `feeling-search` 推到国内外技能商店时，手填字段都已写好，直接复制即可。
> 更新日期：2026-10-27 · 对应版本：**v1.0.1**

---

## 0. 本轮实际提交（有回执才算数）

| 渠道 | 结果 | 回执 |
|---|---|---|
| GitHub（公开仓库） | ✅ 已推送 v1.0.0 + topics + description | `e4eb9d0` / tag `v1.0.0`，仓库 `xixi048/feeling-search-skill` |
| **skillstore.io** | ✅ 处理中（机器人会开 PR + 安全审计） | submission `3a741d97-761c-4a08-89b3-f2619fc7ee34`，status `processing` |
| **skillsmd.dev** | ✅ 已提交待审 | id `0b5155fe-952e-4fcd-9219-e9299b3bd5c6` |
| **buildwithclaude** | ✅ PR 已开 | [PR #569](https://github.com/davepoon/buildwithclaude/pull/569) |
| **VoltAgent/awesome-agent-skills** | ✅ PR 已开（Specialized Domains 组） | [PR #1276](https://github.com/VoltAgent/awesome-agent-skills/pull/1276) |
| **自建发现端点** | ✅ HTTP 200 | `https://xixi048.github.io/feeling-search-skill/.well-known/agent-skills/index.json` |
| **ClawHub (openclaw)** | ⏸ 卡在许可条款 | CLI 报 `MIT-0 license terms must be accepted`，需在 clawhub 网页账户接受一次 |
| **skillbay.sh** | ⏸ 等联系邮箱 | 匿名 quick 提交需 `contactEmail`，审核后会邮件索要 before/after 证据 |
| 自动索引型（skills.sh / SkillsMP / LobeHub / claude-plugins.dev） | 🟡 等爬虫 | 布局与 topics 已就位；SkillsMP 需 ≥2 stars |
| Cow Skill Hub / 腾讯 SkillHub(skillhub.cn) / Cindy / 讯飞 Astron | ⏸ 需登录 | 入口见 §6；zip 已备：`dist/feeling-search-v1.0.1-skillroot.zip`（34 KB，SKILL.md 在包根） |
| MCP 目录群（Smithery / Glama / mcp.so / PulseMCP） | ⏸ 下一步 | 需先交付可跑的 MCP server，不在本轮"推送"范围 |

## 1. 关键 URL（别填错）

| 用途 | URL |
|---|---|
| 仓库首页 | `https://github.com/xixi048/feeling-search-skill` |
| **技能目录（推荐填这个）** | `https://github.com/xixi048/feeling-search-skill/tree/main/skills/feeling-search` |
| 线上站点 | `https://xiximm.cloud` |
| 发现端点 | `https://xixi048.github.io/feeling-search-skill/.well-known/agent-skills/index.json` |

⚠️ 本机 git remote 被 `insteadof` 改写成 ghfast 镜像，提交商店时必须换成原始地址。
本仓库 push 走的是 `git@github.com:`（SSH over 443），不受影响。

## 1.5 需本人登录的渠道 · 直达入口

| 渠道 | 入口 | 登录后动作 | 需要的物料 |
|---|---|---|---|
| **ClawHub (openclaw)** | `https://clawhub.ai` | 账户里接受一次 **MIT-0 发布条款**（CLI 无此开关），之后一条 `clawhub publish` 即可 | slug `feeling-search`，仓库 URL，commit SHA |
| **skillbay.sh** | `https://skillbay.sh` | 匿名提交走 quick 表单；有账号可直接登录挂 $5 标价 | `dist/*.zip` + 联系邮箱（审核后会邮件索要 before/after 证据） |
| **腾讯 SkillHub** | `https://skillhub.cn` | 网页提交（旧域名 skillhub.tencent.com 已 301） | `dist/*.zip` 或 GitHub 导入 |
| **讯飞 Astron SkillHub** | `https://skill.xfyun.cn/publish` | 讯飞账号登录发布 | `dist/*.zip`，中文区文案见 §3 |

⚠️ Cow Skill Hub 官方域名未核实（Web + GitHub/Google OAuth，匿名 POST 返回 401），找到入口后再补。

包根 zip 位于仓库 `dist/feeling-search-v1.0.1-skillroot.zip`，SKILL.md 已在包根（Cow / SkillHub 类上传型渠道要求）。

## 2. 定价：免费引流 + 付费渠道标价

| 渠道 | 定价 | 说明 |
|---|---|---|
| skillstore / skillsmd / buildwithclaude / awesome 列表 / 自建端点 | 免费引流 | 这些渠道本身不支持收费 |
| **skillbay.sh** | **$5**（≈¥35） | 平台 0 抽成；定价字段需 seller 账号 + Stripe，先匿名提交占曝光位 |
| 扣子 Coze 技能商店 | ¥0.5/次 起 或 ¥9.9/月 | 约 70% 分成；需入驻商户，属"移植"不是"推送" |
| GPT Store / Windows Agent Store | $4.99 | 需相应开发者账号，属移植 |

技能本身在 API 侧另有计费（云端 analyze $0.10/次，x402 或支付宝两条轨道）——
**商店标价与 API 计费是两回事**：商店卖的是"技能包 + 本地词典档"，本地档永远免费。

## 3. 各渠道展示文案

### 英文区（ClawHub / skillstore / SkillsMP / skillbay）

- **Name:** feeling-search
- **Tagline:** Turn a vague feeling into concrete visual style
- **Short:** One colloquial sentence in, art-direction vocabulary out — 762 feeling words, 598 visual styles.
- **Long:** "I want it to feel like…" is where art direction starts and where vocabulary runs out.
  feeling-search is the lookup table between a mood and the name of a style. Describe a mood in plain
  Chinese or English and get back the feeling words it hits plus the visual styles those words map to,
  each with a name, a one-line definition and the words that triggered it. Runs free on a local cached
  lexicon (works offline after the first pull); a paid cloud call is used only when nothing matches
  locally and you explicitly allow it.

### 中文区（腾讯 SkillHub / Cow Skill Hub / 讯飞 Astron / 扣子）

- **显示名：** 感觉检索
- **简介：** 用你的感觉检索美术风格 —— 一句口语进去，762 个感受词、598 个视觉风格出来
- **分类：** 设计 / 美术 / 创意工具
- **标签：** 美术风格、氛围、情绪、图像生成、概念设计、游戏美术

## 4. 审核说明模板（安全审查用得上）

> 零第三方依赖，Python 3.8+，只用标准库。无 `eval` / `exec` / `subprocess` / 动态 import。
> 唯一的磁盘写入是用户自己缓存目录下的词表文件（`~/.cache/feeling-search/`），
> 另有 `--offline` 可完全断网。
> 默认走免费的本地词典档；付费端点只在本地零命中且调用方显式 `--allow-cloud` 时才会请求，
> 没配额度 token 时服务端回 402，技能会如实报错，不会把本地结果伪装成云端结果
> （`source` 只有 `local` / `cloud` 两个值）。
> 包内不含任何数据集与图片（3 个文件，34 KB）。

## 5. 下一步（按性价比排序）

1. **在 `https://clawhub.ai` 接受 MIT-0 条款** → 一条 `clawhub publish` 就能发出去（CLI 已登录 xixi048）
2. **补一个联系邮箱** → 提交 skillbay（付费渠道，标价 $5）
3. 等 skillstore 机器人开 PR（5–10 分钟），PR 上通常会有安全审计结论，按需回复
4. 登录型渠道：Cow Skill Hub / 腾讯 SkillHub / 讯飞 Astron 用 `dist/*.zip` 走 GitHub 导入
5. 想上 MCP 目录群，先把 feeling-search 已有的 MCP server 独立出来（那是另一个项目）
