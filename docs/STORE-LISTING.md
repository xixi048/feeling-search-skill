# 商店上架物料包 · feeling-search

> 用途：把 `feeling-search` 推到国内外技能商店时，手填字段都已写好，直接复制即可。
> 更新日期：2026-10-27 · 对应版本：**v1.0.2**（定位改为「商业级美术对照表 / 美术风格大全 / 美术风格 AI 提示词大全」）

---

## 0. 本轮实际提交（2026-10-27 复查，有回执才算数）

| 渠道 | 结果 | 回执 |
|---|---|---|
| GitHub（公开仓库） | ✅ 已推送 + topics + description | 仓库 `xixi048/feeling-search-skill`，tag `v1.0.0` → `v1.0.2` |
| **skillstore.io** | ✅ **已收录**（机器审核 `safe`，PR 已合并） | submission `3a741d97-761c-4a08-89b3-f2619fc7ee34` → status **`published`**；合并 PR [aiskillstore/marketplace#3948](https://github.com/aiskillstore/marketplace/pull/3948)（`/xixi048-feeling-search`，risk safe） |
| **buildwithclaude** | 🟡 PR 开着，**无人驳回** | [PR #569](https://github.com/davepoon/buildwithclaude/pull/569) · state `OPEN` · mergeable · 0 comments |
| **VoltAgent/awesome-agent-skills** | 🟡 PR 开着，**无人驳回** | [PR #1276](https://github.com/VoltAgent/awesome-agent-skills/pull/1276) · state `OPEN` · mergeable · 0 comments |
| **自建发现端点** | ✅ HTTP 200 | `https://xixi048.github.io/feeling-search-skill/.well-known/agent-skills/index.json` |
| **skillsmd.dev** | ✅ 已重提（原单掉单） | 旧 id `0b5155fe-…` → `HTTP 404 Submission not found`；新 id **`5e42b97d-edaa-4dfd-b4de-6e0f5c8dbab7`**（v1.0.2 文案）。注：该站按仓库解析 GitHub，偶发瞬时 `repo not found` 404，重试即通 |
| **skillstore.io 内容刷新** | ✅ 已重提（2026-10-27） | 新 submission `0dd1668f-e82c-4144-a18f-f2d0c92f4d2b` → `pending`，ETA 5–10 分钟（此前被 1 小时冷却 409 挡，冷却后重提成功） |
| **skillsmd.dev 再次提交** | ✅ 已提交（2026-10-27） | 新 id `eea63cc9-e656-4900-aa95-9c8c21102360`（v1.0.2 文案） |
| **skillbay.sh** | ✅ 已提交（2026-10-27） | `HTTP 201` 已提交待人工审核。**付费版（$5）需邀请 + Stripe**，匿名单只能占曝光位 |
| **WorkBuddy 开放平台** | ✅ 已提交（审核中） | 技能 `os_3782f91f36d4b688` v1.0.2「感觉检索 · 美术对照表」，分类「内容创作」，类目「工具 - 信息查询 / 工具 - 图片处理」，价格**免费**（先过审才能开收款）。**内测抽 1%，国内最优**。审核 7 个工作日 |
| **WorkBuddy 连接器（MCP）** | ✅ 已提交（审核中） | 连接器 `oc_5d13e5d566d17e7a` v1.0.2，远程 `https://xiximm.cloud/mcp`（streamableHttp）。包在 `feeling-search-mcp/connector/`。审核 10–15 分钟生效，但**连接器不能挂价** |
| **虾评 XiaPing（扣子生态）** | ✅ **已上架**（试用版） | skill `86fcb1aa-1ae9-42ba-9d1c-fad51571add1` v1.0.2，分类「创意设计」，`requires_api_key=false`。安全检测**通过**、重复检测**通过**。账号 `xixi048`（Agent 自注册，A2）。试用版转正要 20 篇评测 + 加权 ≥4 |
| **扣子 Coze 技能商店** | ❌ 走不通（资质墙） | 2026-05 起改申请制：需专业领域（自媒体/金融/法律/电商/科研/教育/健康医疗）+ 资质证明。美术/设计不在其中，通用工具官方建议改投虾评。付费另需商户入驻 |
| **扣子编程技能生成** | ⚠️ 已生成但不入库 | 项目 `7701155255446437942` 生成了 `feeling-search.skill` 包，但 `save_to_my_skill` 报 `COZE_API_TOKEN is missing`（平台侧凭证缺失），无法进「我的技能」 |
| **扣子 Coze（按次付费）** | ⏸ 待商户入驻 | 需签协议开收款；可切分「本地免费 / 云端 ¥0.5 一次」。前提是先过资质关 |
| **ClawHub (openclaw)** | ⏸ 卡在 MIT-0 勾选 | 见 §1.5：**不是账户设置，是发布表单上的一个勾选框**，CLI 无此参数 |
| **skillbay.sh** | ⏸ 等联系邮箱 | 匿名 quick 提交需 `contactEmail`，审核后会邮件索要 before/after 证据 |
| 自动索引型（SkillsMP / LobeHub / claude-plugins.dev） | 🟡 等爬虫 | 布局与 topics 已就位；SkillsMP 需 ≥2 stars |
| Cow Skill Hub / 腾讯 SkillHub(skillhub.cn) / Cindy / 讯飞 Astron | ⏸ 需登录 | 入口见 §1.5；zip：`dist/feeling-search-v1.0.2-skillroot.zip`（14 KB，SKILL.md 在包根） |
| MCP 目录群（Smithery / Glama / mcp.so / PulseMCP） | ⏸ 下一步 | 需先交付可跑的 MCP server，不在本轮"推送"范围 |

**结论：截至 2026-10-27，除 skillsmd 掉单外，没有一条是「被驳回」。** 两个 PR 都还挂在待审队列里。

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
| **ClawHub (openclaw)** | `https://clawhub.ai/skills/publish` | 表单里勾一个 **MIT-0 复选框**再提交（见下方说明） | slug `feeling-search`，仓库 URL，commit SHA |
| **skillbay.sh** | `https://skillbay.sh` | 匿名提交走 quick 表单；有账号可直接登录挂 $5 标价 | `dist/*.zip` + 联系邮箱（审核后会邮件索要 before/after 证据） |
| **腾讯 SkillHub** | `https://skillhub.cn` | 网页提交（旧域名 skillhub.tencent.com 已 301） | `dist/*.zip` 或 GitHub 导入 |
| **讯飞 Astron SkillHub** | `https://skill.xfyun.cn/publish` | 讯飞账号登录发布 | `dist/*.zip`，中文区文案见 §3 |

⚠️ Cow Skill Hub 官方域名未核实（Web + GitHub/Google OAuth，匿名 POST 返回 401），找到入口后再补。

### ClawHub 的 MIT-0 到底在说什么（2026-10-27 从站上前端确认）

ClawHub 发布页原文两条：

1. `All skills published on ClawHub are licensed under MIT-0. Free to use, modify, and redistribute. No attribution required.`
   —— 上架的技能一律按 **MIT-0（MIT No Attribution）** 授权：可商用、可改、可再分发，**不要求署名**。
2. `ClawHub does not support paid skills, per-skill pricing, or paywalled releases.`
   —— **不支持付费技能、不支持单技能定价、不支持付费墙。**

所以那个勾选框的含义是：*同意把这一版按 MIT-0 放出去*。它**不是账户里的设置项，也不是一次性协议**，
而是**每发布一次就要勾一次**的表单字段 —— 这也是 CLI `clawhub publish` 永远报
`MIT-0 license terms must be accepted` 的原因：命令行没有这个字段，只能走网页表单。

⚠️ 两个后果要记住：
- 本仓库是 MIT（要求保留版权与许可声明），ClawHub 上是 MIT-0（不要求署名）—— 比 MIT 更宽松，
  等于默许他人去掉署名。能接受就勾。
- ClawHub **不能标价 $5**。要收费只能靠 API 侧的 x402 / 支付宝，不靠商店定价。

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
- **Short:** One colloquial sentence in, the best-matching visual style out — an art reference chart at your back.
- **Long:** "I want it to feel like…" is where art direction starts and where vocabulary runs out.
  feeling-search is the lookup table between a mood and the name of a style. Describe a mood in plain
  Chinese or English and get back the feeling words it hits plus the visual styles those words map to,
  each with a name, a one-line definition and the words that triggered it. Runs free on a local cached
  lexicon (works offline after the first pull); a paid cloud call is used only when nothing matches
  locally and you explicitly allow it.

### 中文区（腾讯 SkillHub / Cow Skill Hub / 讯飞 Astron / 扣子）

- **显示名：** 感觉检索
- **简介：** 用你的感觉检索美术风格 —— 一句口语进去，最匹配的视觉风格出来
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
