# 付费上架物料包 · feeling-search

> 用途：能收费的渠道逐个填好，登录取到账号后**直接粘贴**，不再二次构思。
> 更新：2026-10-27 · 对应 v1.0.2

---

## 0. 先看这一条：能不能收费取决于「形态」，不取决于渠道

感觉检索是**少数天生适合收费的形态**——它不是一个纯本地脚本，它背后有可调用的服务端点
（`https://xiximm.cloud/mcp`）。国内按次付费的两条主路（腾讯 SkillPay、扣子按次付费）
要求的正是「依赖后端、脱离后端无法独立使用」。这一点它天然满足。

所以本技能的 SKU 设计是：

| 形态 | 卖什么 | 在哪卖 | 定价 |
|---|---|---|---|
| **免费引流版** | 本地缓存词典，离线可用 | skillstore / skillsmd / awesome 榜 / GitHub | ¥0 |
| **按次调用版** | 后端检索服务，每次调用计费 | 扣子 Coze、腾讯 SkillPay、支付宝 SkillPay | ¥0.5–1 / 次 |
| **买断版** | 完整技能包 + 美术对照表完整档 | WorkBuddy 开放平台、skillbay.sh | ¥9.9–29 买断 |
| **月订版** | 持续更新 + 新风格扩充 | WorkBuddy 开放平台 | ¥9.9–19 / 月 |

> 本地档永远免费，收费只发生在**服务调用**与**完整档**上——这条必须写进 listing，
> 否则会被判「付费墙套壳」。

---

## 1. 优先级排序（按投入产出）

| 顺位 | 渠道 | 抽成（你拿） | 卡在哪 | 需要你做什么 |
|---|---|---|---|---|
| **1** | **WorkBuddy 开放平台** | **99%（内测 1%）** | 开发者认证 + 人脸识别 + 微信签约 | 扫码认证一次 |
| **2** | 扣子 Coze 技能商店 | 约 70% | 商户入驻 | 签协议 + 开收款 |
| 3 | 腾讯 SkillHub / SkillPay | 100%（暂 0 抽成） | 需改成 Pay Skill 形态 + 实名绑支付宝 | 登录 + 授权 |
| 4 | 支付宝 SkillPay | 平台规则 | 实名 + 签约 | 登录 + 签约 |
| 5 | MCP Market（卖 Agent Skills） | 自定 | seller 账号 | 登录 |
| 6 | SkillHQ | 80–85% | CLI + 账号 | `skillhq` 登录 |
| 7 | Agensi | 70% | 账号 | 登录 |
| 8 | skillbay.sh | 100%（0 抽成） | 邀请制 → Stripe | 等邀请邮件 |
| 9 | PromptBase | 80%（专属链接 100%） | seller 账号 | 登录 |
| 10 | Gumroad | 90%（Discover 70%） | 账号 | 登录 |

**共同点：定价动作全部发生在「账号 / 商户」层，不在「提交」层。**
匿名提交接口提交不了价格——所以顺序只能是：免费曝光先占位 → 账号到位 → 再挂价。

---

## 2. WorkBuddy 开放平台（第一优先）

### 2.1 三条硬约束（顺序不能倒）

1. **先有 1 个审核通过的免费技能，才能开收款账户。** 免费资产不支持转付费，
   所以正确姿势是：先发免费版过审 → 开收款 → 再单独发付费版。
2. **观察期只能发布 1 个付费资产**，首次产生订单后才能继续发布。
3. **付费方式（买断 / 月订）审核通过后不可更改。** 发布前想清楚。

### 2.2 上传规格

| 项 | 要求 | 本技能现状 |
|---|---|---|
| 格式 | 仅 `.zip` | ✅ `dist/wb/feeling-search-wb-1.0.2.zip` |
| 体积 | ≤ 3 MB | ✅ 14.6 KB |
| 目录层级 | 最多两层 | ✅ `SKILL.md` + `references/` + `scripts/` |
| SKILL.md 位置 | 包根 | ✅ |
| 头像 | 512×512、≤500 KB、JPG/PNG | ⏸ 待出图 |
| frontmatter | 8 个必填字段 | ✅ 见下 |

### 2.3 必须补齐的 8 个字段（这是最容易漏的一条）

通用 Skill 规范只要 `name` + `description`，**开放平台要 8 个**：

`name` · `display_name` · `display_name_en` · `description` ·
`description_zh` · `description_en` · `version` · `author`

用 `python scripts/build_wb.py` 打包，会在**不改源文件**的前提下注入缺的字段，
并自检 hyphen-case、尖括号、体积上限。**别手改 `skills/feeling-search/SKILL.md`**——
那会污染其他商店的上架物料。

### 2.4 可直接粘贴的展示字段

| 字段 | 值 |
|---|---|
| 技能名称 | `感觉检索 · 美术对照表` |
| 英文名 | `Feeling Search · Art Reference Chart` |
| 市场分类 | 内容创作 |
| 服务类目 | 设计辅助 / 图像生成 / 文案与创意 |
| 一句话简介 | 描述一句感觉，返回最匹配的视觉风格 |
| 版本号 | `1.0.2` |

**中文长简介（粘贴用）：**
> 输入一句口语化的感觉描述，比如「雨夜便利店的冷白灯光」「孤独但不想太暗」，
> 它会从一份中文美术对照表里检索出最匹配的视觉风格，并给出触发它的感受词、
> 一句话风格定义和参考图。用来做美术定调、AI 绘画提示词、概念设计方向锚点，
> 或者单纯回答「这种感觉在美术上到底叫什么」。
>
> 词库后续会持续扩充，所以不写死条数——你看到的是当前最新的对照表。

**英文长简介（粘贴用）：**
> Turn one colloquial sentence about a mood — "a rainy night outside a convenience
> store", "lonely but not too dark" — into the best-matching visual style from a
> Chinese art-reference lexicon. You get the style name, a one-line definition, the
> feeling words that triggered it, and reference images. Built for art direction,
> AI image prompt engineering, concept art and brand visuals.
>
> The lexicon keeps growing, so no counts are quoted here — what you get is always
> the current one.

**定价建议（首次上架别定高）：**
- 免费版先过审（必须）
- 付费版：**¥9.9 买断**试水，或 **¥9.9 / 月**（词库持续扩充，月订更合理）
- 官方示例价是 79 元买断，但市场里跑通的真实订单多在 19–29 元；
  **第一单的意义是验证有人愿意付，不是赚钱**

### 2.5 上架路径

```
open.workbuddy.cn → 注册/登录 → 开发者认证（个人：手机+邮箱+人脸）
→ 发布管理 → 技能 → 创建 → 上传 zip → 选分类/类目 → 提交审核
→ 审核通过（官方 7 工作日，实测常见 1–2 天）
→ 收入变现 → 开通收款账户（填资料 → 审核 → 微信扫码签约）
→ 回到技能 → 编辑 → 付费设置 → 选买断/月订 → 填价 → 勾原创声明 → 发布
```

---

## 3. 扣子 Coze（第二优先）

- 入口：`code.coze.cn/merchant-management` 先入驻商户
- 付费模式：**按次付费**（可低至 ¥0.5/次）/ 一次买断 / 免费
- 按次付费**只适用于通过 API 提供功能的技能**——感觉检索的 `xiximm.cloud` 正好符合
- 分成：约 70%（部分口径称 90%，以入驻后台为准）
- 在一个技能里可配置**多个付费接口，各自定价**：本地检索免费，云端精确检索 ¥0.5/次

**建议的计费切分：**

| 接口 | 价格 | 说明 |
|---|---|---|
| `local_lookup` | 免费 | 本地缓存命中的风格检索 |
| `cloud_lookup` | ¥0.5 / 次 | 本地没命中时的云端精确检索 |
| `style_detail` | ¥0.5 / 次 | 单风格完整档案（含参考图） |

---

## 4. 腾讯 SkillHub / SkillPay

- 入口：`skillhub.cn/skillpay`
- 抽成：平台**暂不收取技术服务费**（你拿 100%），支付宝/微信实时结算
- 硬门槛：必须是 **Pay Skill** —— 源文件依赖后端服务、脱离后端无法独立使用，
  调用链要改成「确认支付 → 返回支付触发标识 → 任务内继续执行」
- 感觉检索符合条件，但**需要把本地档和云端档拆成两个技能**
  （本地档免费上普通 Skill，云端档上 Pay Skill）

---

## 5. 支付宝 SkillPay

- 入口：`skillpay.alipay.com`
- 两种模式，交付方式不同：
  - **一次性付费** → 消费者拿到 Skill 明文
  - **周期付费** → 只提供当期使用权，不交付明文，不自动续费
- 已适配 WorkBuddy、Cursor、Codex、Claude Code
- ⚠️ 与 SkillHub 的 SkillPay **是两个不同入口**，别混

---

## 6. 海外付费渠道（英文文案）

| 渠道 | 抽成 | 上架方式 | 备注 |
|---|---|---|---|
| skillbay.sh | 0% | `POST /api/v1/sellers/{org}/listings` | 邀请制，Stripe 结算，$5 起 |
| SkillHQ | 20%/15% | CLI | Starter 80% / Pro 85%，有防盗版指纹 |
| Agensi | 30% | MCP 加载 | 一次购买 + 订阅 |
| MCP Market | 自定 | 网页 | 支持 GitHub 同步、版本发布 |
| PromptBase | 20%（专属链接 0%） | 网页 | 已在内容社区有受众时最优 |
| Gumroad | 10% + $0.50 | 网页 | 适合「技能包 + 教程 + 案例」组合 |

**英文一句话（所有海外渠道通用）：**
> One sentence about a feeling in, the best-matching visual style out — with the
> feeling words that triggered it and reference images.

---

## 7. 明确收不了钱的渠道（别浪费时间）

| 渠道 | 原因 |
|---|---|
| **ClawHub** | 官方明文：`does not support paid skills, per-skill pricing, or paywalled releases`，且强制 MIT-0（不要求署名） |
| skillstore.io | 只做免费收录 |
| skillsmd.dev | 只做免费收录 |
| buildwithclaude / awesome 榜 | 都要求免费开源 |
| Glama / mcp.so / Smithery | MCP 目录，只做收录 |

---

## 8. 回执留档

| 渠道 | 时间 | 回执 | 状态 |
|---|---|---|---|
| skillstore.io | 2026-10-27 | `0dd1668f-e82c-4144-a18f-f2d0c92f4d2b` | pending，ETA 5–10 分钟 |
| skillsmd.dev | 2026-10-27 | `eea63cc9-e656-4900-aa95-9c8c21102360` | Submission received |
| skillbay.sh | 2026-10-27 | HTTP 201 | 已提交待人工审核（付费版需邀请） |
| WorkBuddy 开放平台 | 2026-10-27 | 技能 `os_3782f91f36d4b688` | ✅ 已提交审核（免费版）。开收款前置：≥1 个技能过审 |
| WorkBuddy 连接器 | 2026-10-27 | `oc_5d13e5d566d17e7a` | ✅ 已提交审核（MCP，不参与收费） |
| 扣子 Coze | — | — | ⏸ 等商户入驻 |
