# Reviewer notes — feeling-search v1.1.2

Paste-ready text for store review forms (English for global stores, 中文 for CN stores).

## English (skillstore.io / skillsmd.dev / skillbay.sh / buildwithclaude)

**feeling-search** turns one colloquial sentence into art-direction vocabulary: the feeling words it
hits plus the visual styles those words map to (name, one-line definition, parent style, triggering
words, reference images). It is an art-style reference chart / prompt dictionary for
Midjourney, Stable Diffusion and Flux, useful for concept art, game art direction and brand visuals.

What changed in 1.1.2 (previously listed: 1.0.2)

- Billing is off by default: the cloud `analyze` endpoint is now free and rate-limited instead of
  metered, so no quota token is needed. The local lexicon path is unchanged.
- Internal quota helper builds its request URL with `urlencode` instead of string concatenation
  (a scanner previously flagged the concatenation pattern as a hardcoded credential — it never was).
- Marketplace/preview metadata synced to the current free-mode wording.

Safety

- Zero third-party dependencies — Python 3.8+ standard library only.
- No `eval` / `exec` / `subprocess` / dynamic import.
- Only disk write: a lexicon cache inside the user's own cache dir (`~/.cache/feeling-search/`).
- `--offline` disables network access entirely.
- The cloud call happens only when the local lexicon returns zero matches **and** the caller passes
  `--allow-cloud`; the response marks its own `source` as `local` or `cloud` and never disguises a
  local result as a cloud one.

Package

- 3 files: `SKILL.md`, `references/api-contract.md`, `scripts/fs_api.py` — 18 KB.
- Contains no datasets and no images; the lexicon is pulled at runtime and cached locally.

Verified usage (before/after)

Without the skill, model output for *“下雨天一个人走在便利店门口，冷白灯光”* is a generic list of
mood adjectives. With it, the run returns ranked styles with definitions:
`代尔夫特画派 0.25 / 灰烬寒冬 0.22 / 风格派 0.22`, each with the words that triggered it — directly
usable as prompt words.

## 中文（腾讯 SkillHub / 讯飞 Astron / Cow Skill Hub）

**感觉检索 v1.1.2 · 商业级美术对照表 / 美术风格大全 / 美术风格 AI 提示词大全**

一句口语化的感觉描述进去，最匹配的视觉风格出来：给出命中的感受词，以及这些词映射到的视觉
风格（中文名、英文名、一句话定义、父风格、命中词、参考图）。可直接当美术风格词典与
Midjourney / Stable Diffusion / Flux 提示词库使用。

本版变化（上一版 1.0.2）

- 云端 `analyze` 改为默认免费 + 限量（每 IP 20 次/分钟，每访客每天 200 次），不再需要额度 token；
  本地词典档逻辑不变，仍可 `--offline` 完全断网。
- 额度辅助命令改用 `urlencode` 构造请求地址（原写法被扫描器误判为硬编码凭证）。
- 插件市场元数据同步到免费口径。

安全说明

- 零第三方依赖，仅用 Python 标准库，无 `eval` / `exec` / `subprocess` / 动态 import。
- 唯一磁盘写入是用户自己缓存目录下的词表文件（`~/.cache/feeling-search/`）。
- 云端调用需同时满足「本地零命中」+ 调用方显式 `--allow-cloud`；`source` 字段只有 `local` / `cloud`，不会把本地结果伪装成云端结果。
- 包内 3 个文件、18 KB，不含数据集与图片。
