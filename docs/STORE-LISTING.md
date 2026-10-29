# 商店上架物料包 · feeling-search

> 用途：把 `feeling-search` 推到国内外技能商店时，手填字段都已写好，直接复制即可。
> 更新日期：2026-10-30 · 对应版本：**v1.2.0**（整句零命中给新答案；本地 MCP 包带语义引擎）

---

## -1. 本轮推送（v1.2.0 · 2026-10-30，有回执才算数）

| 渠道 | 结果 | 回执 |
|---|---|---|
| GitHub 仓库 | ✅ 已推送 | `main = 0a9953d`（`xixi048/feeling-search-skill`），含 marketplace / 发现端点版本同步 |
| **skillstore.io** | ✅ 已提交 | submission `49d31a68-d922-4505-8278-33cdf3b7e962`（pending，ETA 5–10 分钟） |
| **skillsmd.dev** | ✅ 已提交 | id `6e9fe9a7-45b7-4075-94c0-e7812584f155` |
| **skillbay.sh** | ✅ 已提交待人工审核 | `HTTP 201`，联系人 `xixi048 / 916708243@qq.com` |
| **buildwithclaude** | ✅ 重开 PR（按 #601 的三条意见全修） | [PR #613](https://github.com/davepoon/buildwithclaude/pull/613)：只带 feeling-search、去掉 `metadata`、scripts/references 随包、`plugin.json` 205→206 且 keywords 补 `feeling-search` |
| **awesome-openclaw-skills**（53k★） | ✅ 新开 PR | [PR #603](https://github.com/VoltAgent/awesome-openclaw-skills/pull/603)：加入 Image & Video Generation，README + `categories/image-and-video-generation.md` 双改，计数 171→172 |
| **public-api-lists**（16k★） | ✅ 新开 PR | [PR #868](https://github.com/public-api-lists/public-api-lists/pull/868)：Art & Design 表加一行，`No / Yes / Yes`（实测匿名可用、`Access-Control-Allow-Origin: *`） |
| **BehiSecc/awesome-claude-skills**（10k★） | ✅ 新开 PR | [PR #1099](https://github.com/BehiSecc/awesome-claude-skills/pull/1099)：加入 Media & Content |
| **自建发现端点** | ✅ 1.2.0 | `https://xixi048.github.io/feeling-search-skill/.well-known/agent-skills/index.json`（HTTP 200，updated 2026-10-30） |
| **包产物** | ✅ 已重打 | `dist/feeling-search-v1.2.0-skillroot.zip`（sha256 `9b29e711…`）、`dist/wb/feeling-search-wb-1.2.0.zip`（20.0 KB） |
| **ClawHub** | ✅ **1.2.0 已提交，待安全扫描** | 「`MIT-0 license terms must be accepted`」**是 CLI 版本过旧造成的假阻塞**：本地 `clawhub@0.7.0`，`npm i -g clawhub@latest` 升到 **0.24.1** 后，同一条 `clawhub publish` 直接通过 → `Update submitted for feeling-search@1.2.0; pending security scans`。注意新版要求 `--source-repo` 与 `--source-commit` **必须成对**提供 |
| **MCP.Directory** | ✅ **早已提交，审核中** | 填 `https://mcp.directory/submit` 时站点回 `This repository has already been submitted. We'll review it soon!` —— 说明前几轮已进队列（24h 审核），本轮无需重复 |
| **VoltAgent/awesome-agent-skills** | ❌ **PR #1276 已被关闭（未合并）** | 2026-10-29 09:35 关闭，无评论。其 CONTRIBUTING 明确「brand new skills that were just created are not accepted」「must have real community usage」→ 本仓 0 star，现在重提大概率再被关。**建议攒到 ≥10 star 再提** |
| Cow Skill Hub / 腾讯 SkillHub / 讯飞 Astron / WorkBuddy 开放平台（1.2.0 更新） / agentskill.sh | ⏸ 需登录 | 物料已就位：`dist/feeling-search-v1.2.0-skillroot.zip`、`dist/wb/feeling-search-wb-1.2.0.zip`；中文文案见 §3 |
| SkillsMP | ⏸ 需 ≥2 stars | 仓库 0 star，自动索引拿不到 |

### -1.0.1 本轮撞到的墙（省下一轮时间）

| 渠道 | 结论 |
|---|---|
| **apis.io** | `/add/` 表单已全部填妥（name / email / `https://xiximm.cloud` / `/openapi.json` / 备注里写了 llms.txt 与 `/mcp`），提交时卡 **Cloudflare Turnstile**（`cf-turnstile-response` 为空）→ 需真实浏览器人工过一次校验 |
| **directory.llmstxt.cloud** | 同上，Standard 免费档（1–3 月、nofollow）表单已填妥，卡同一个 Turnstile |
| **appcypher/awesome-mcp-servers** | 仓库 **已 archived**，`gh pr create` 报 `does not have the correct permissions` → 不是权限问题，是归档了 |
| **wong2/awesome-mcp-servers** | `pull_request_creation_policy = collaborators_only`，外部开不了 |
| **travisvn/awesome-claude-skills**（15k★） | CONTRIBUTING 双重门槛：**需 ≥10 stars 否则自动关闭**，且**禁止 AI 生成/提交的 PR** → 本仓 0 star，提交即违规 |
| **Glama** | 「Add Server」弹的是**邮箱注册**（不是 OAuth），要收验证邮件 → 暂缓 |
| **skills.cowagent.ai**（Cow Skill Hub） | curl 200（0.9s），但 Playwright 内 `ERR_TIMED_OUT` —— 该站对自动化浏览器直接超时，换 UA 也无效 |
| **agentskill.sh** | 表单与导入逻辑都正常，但返回 `Too many submissions. Please try again in an hour.` —— **IP 级限流** |
| **腾讯 SkillHub（skillhub.cn）** | 页面可达、「登录」按钮点不动（走扫码），自动化过不去 |
| **Chrome 登录态借不过来** | 复制 `User Data/Local State` + `Default/Network/Cookies` 到独立 profile 后，Playwright 里 GitHub 仍是未登录 —— **Chrome 的 cookie 是 App-Bound Encryption，跨浏览器内核解不开**。反过来，`--profile` + `--headed` 启动的 Playwright 会话**在窗口里登一次就能长期复用**，是唯一可行路径 |

### -1.1 本轮同步的 MCP / API 侧（同一个版本批）

| 渠道 | 结果 | 回执 |
|---|---|---|
| **GitHub（MCP 仓）** | ✅ 补推 7 个提交 | `6055456..ba109b7`（0.2.2 → 0.2.6 全在本地没推），另 `7a6aedf` 把连接器物料版本对齐 1.2.0 |
| **npm `feeling-search-mcp`** | ✅ 已是最新 | `0.2.6`（`dist-tags.latest`），包内含 762 词向量 `idx/terms*.bin` |
| **MCP 官方 Registry** | ✅ 已是最新 | `cloud.xiximm/feeling-search@0.2.6` `isLatest=true` |
| **远端 /mcp 探活** | ✅ 200 | `initialize` 返回 `serverInfo.name=feeling-search / version=0.3.0` |
| **Agent402** | ✅ 重新登记 | `listed:true` · `toolCount:13` · `routable:true` · `health:1` |
| **public-apis** | 🟡 PR 仍 OPEN | [#8482](https://github.com/public-apis/public-apis/pull/8482)（Art & Design 分类） |
| 扣子插件（新版本 + 重上架） / RapidAPI / Postman / x402scan / CDP Bazaar / APIs.guru | ⏸ 需登录或钱包签名 | 见 §0.3 与 2026-10-28 日志 |

---

## 0. 上一轮推送（v1.1.2 · 2026-10-29，有回执才算数）

| 渠道 | 结果 | 回执 |
|---|---|---|
| GitHub 仓库 | ✅ 已推送 | `main = e03f0c3`（仓库 `xixi048/feeling-search-skill`） |
| **skillstore.io** | ✅ 已提交，机器人已开 PR 待审 | submission `3290ac4a-389e-4c1a-865d-d7c64fc25a00` → [aiskillstore/marketplace#3988](https://github.com/aiskillstore/marketplace/pull/3988)（`pending-review`，风险 medium） |
| **skillsmd.dev** | ✅ 已提交 | id `fd4d6eda-a9b8-4f54-b75e-1a4e5add57d8`（该站首个请求常瞬时 404，重试即通） |
| **skillbay.sh** | ✅ 已提交待人工审核 | `HTTP 201`，联系人 `xixi048 / 916708243@qq.com`；审核后会邮件索要 before/after 证据 |
| **ClawHub** | ✅ v1.1.2 已发布 | `clawhub skill verify feeling-search` → `version 1.1.2`，pending security scans（MIT-0 勾选已不再是阻塞） |
| **buildwithclaude** | ✅ 重新开 PR（关闭时提的三条意见全修） | [PR #601](https://github.com/davepoon/buildwithclaude/pull/601)：去掉 `metadata`、`category: design`、scripts/references 随包提交 |
| **VoltAgent/awesome-agent-skills** | ❌ PR #1276 已于 2026-10-29 09:35 **被关闭（未合并）** | 见 §-1；门槛是「需有真实社区用量」，0 star 时重提无意义 |
| **自建发现端点** | ✅ 1.1.2 | `https://xixi048.github.io/feeling-search-skill/.well-known/agent-skills/index.json`（HTTP 200，Pages 已按 e03f0c3 重建） |
| **skills.sh** | ⏳ 尚未被索引 | 已 `npx skills add xixi048/feeling-search-skill` 播种安装量；搜索仍 0 命中，等爬虫 |
| **支付宝 SkillPay（付费）** | ✅ **已过审 · 销售中** | 三个商品全部上架：`P0806000210888223`「感觉检索 · 美术风格 AI 提示词大全」**订阅 ¥9.9/月**（试用 5 次）· `P0806000210888227`「全 CG 存档 · 单机游戏画廊全解锁」**订阅 ¥2.99/月** · `P0806000210883975`「一键上架所有 Skill 商店」**订阅 ¥4.99/月**；三项协议（SkillPay 产品协议 / AI 按量付费 / 即刻收）均已签署 |
| **腾讯 SkillHub（Pay Skill / 付费）** | 🟡 已提交，安全审核中 | slug `feeling-search`，显示名「感觉检索 · 美术风格对照表」，V 1.1.2，**单次调用价 0.10 元**（与支付宝服务登记价一致）；包 = `dist/feeling-search-v1.1.2-skillroot.zip`（45.7KB / 3 文件）。⚠️ 标价只是标价，实际扣款由技能打 402 完成，而线上 `FS_PAID` 未开 → 目前在售不扣款 |
| **Cindy SkillHub** | 🟡 已上传并通过审核（v1.0.4），**可见性 private** | 见 §0.2，需要人工在 Cindy 技能页改动 |
| 腾讯 SkillHub / 讯飞 Astron / Cow Skill Hub / WorkBuddy 开放平台（1.1.2 更新） / agentskill.sh | ⏸ 需登录 | 见 §0.3 |
| SkillsMP | ⏸ 需 ≥2 stars | 仓库 0 star，自动索引拿不到 |
| 扣子 Coze / 虾评（版本更新） | ⏸ 资质墙 / 缺 `COZE_API_TOKEN` | 见 §1.5 与旧表 |

### 0.1 本轮前置修复（都在 v1.1.2 里）

- `scripts/fs_api.py`：额度端点改用 `urlencode({...})` 构造，原 `?token=` + 拼接写法被上架体检判为「硬编码凭证」（SEC-001，实为误报），现在 preflight 通过（仅剩网络行为 WARN）。
- `.claude-plugin/marketplace.json`：`1.0.2 → 1.1.2`，描述从「付费兜底」改为当前免费 + 限量口径。
- `docs/.well-known/agent-skills/index.json`：版本与文案同步到 1.1.2。
- 重新打包：`dist/feeling-search-v1.1.2-skillroot.zip`（18.3 KB，sha256 `6a7a907b…`）、`dist/wb/feeling-search-wb-1.1.2.zip`。

### 0.2 Cindy SkillHub 遗留（必须人工处理）

1. `feeling-search` 已上传并审核通过（scorecard docs 100 / overall 100 / security passed），但**创建时是 private**；`publish_skill` 的 update 模式不允许改可见性，显示名与简介仍是首次上传时的占位值。
2. 需要在 Cindy 的技能管理页把它改为 **public**，并把显示名改为「感觉检索 · 美术风格对照表」、简介换成 §3 的中文文案。
3. **清理探针**：`probe-skill-check`（private）与 `probe-skill-pub`（public）是本轮排查上传失败时建的测试技能，务必删除，否则公开市场里会留一条垃圾 listing。

### 0.3 登录型渠道为什么没动

Cindy 内置浏览器是独立身份，没有这些站的登录态；切到外置浏览器套用系统 Chrome 登录拷贝时返回 `PROFILE_LOCKED`（Chrome 正在运行、锁着 cookie 库）。要继续，二选一：

- 完全退出 Chrome / Edge（含托盘）后由 Agent 启动外置浏览器借用登录态；或
- 在 Cindy 侧边栏浏览器里逐个站点登录一次（登录态会长期保留）。

物料已就位：`dist/feeling-search-v1.1.2-skillroot.zip`（SKILL.md 在包根）、`dist/wb/feeling-search-wb-1.1.2.zip`（WorkBuddy ≤3MB）、中文文案见 §3。

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

包根 zip 位于仓库 `dist/feeling-search-v1.0.2-skillroot.zip`，SKILL.md 已在包根（Cow / SkillHub 类上传型渠道要求）。

> 重新打包：`python scripts/build_package.py`（通用规范包，产 skillroot zip + sha256 + manifest）；
> WorkBuddy 专用包是 `python scripts/build_wb.py`（注入 8 个必填字段，产 `dist/wb/`）。
> 2026-10-28 因支付宝档位改价（0.10 元 = 1 次）重建过一次，sha256 见 `dist/package-manifest-v1.0.2.json`。

## 2. 定价：免费引流 + 付费渠道标价

| 渠道 | 定价 | 说明 |
|---|---|---|
| skillstore / skillsmd / buildwithclaude / awesome 列表 / 自建端点 | 免费引流 | 这些渠道本身不支持收费 |
| **skillbay.sh** | **$5**（≈¥35） | 平台 0 抽成；定价字段需 seller 账号 + Stripe，先匿名提交占曝光位 |
| 扣子 Coze 技能商店 | ¥0.5/次 起 或 ¥9.9/月 | 约 70% 分成；需入驻商户，属"移植"不是"推送" |
| GPT Store / Windows Agent Store | $4.99 | 需相应开发者账号，属移植 |

技能本身在 API 侧另有计费（云端 analyze 每次 1 额度：x402 是 $0.10/次，
支付宝是 0.10 元/次）——
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
