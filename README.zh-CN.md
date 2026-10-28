# 感觉检索 · Agent Skill

**商业级美术对照表 · 美术风格大全 · 美术风格 AI 提示词大全。**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776ab.svg)](https://www.python.org/)

> 用你的感觉检索美术风格。

一句口语进去，最匹配的视觉风格出来 —— 背后是一份**美术对照表**，每条风格带名称、
一句话定义，以及它命中了输入里的哪些词。

这不是一个玩具级画风选择器，而是能直接放进商业项目的**美术定调工具**：
命名风格条条带定义，由感受词反查而来。一句「雨天、冷白灯光、空便利店」
不再只换来五个形容词，而是落到一个说得清、立得住的美术方向。可当**美术风格对照表**用、
当**美术风格 AI 提示词词典**用（Midjourney / Stable Diffusion / Flux），
也可以当**风格–词汇交叉索引**，接进概念设计、游戏美术设定集与品牌视觉规范。

**English: [README.md](README.md).**

```
"下雨天一个人走在便利店门口，冷白灯光"
   → 感受词：光 / 白 / 冷光 / 古寂 …
   → 视觉风格：灰烬寒冬、哥特彩色玻璃、冰晶冷白、枯山水 …
```

## 解决什么问题

「我想要那种……的感觉」是美术方向的起点，也是词汇量断掉的地方。
这个技能就是**感觉与风格名之间的查表器**：给图像生成找风格词、给概念设计定方向锚点、
给游戏美术定调、给插画和品牌视觉找参考。

## 两条路径

| 路径 | 触发条件 | 联网 | 花钱 |
|---|---|---|---|
| 本地词典档 | 句子能命中词表（大多数情况） | 否 | 否 |
| 云端 analyze | 本地一个词都没命中，且显式 `--allow-cloud` | 是 | 1 次额度 |

顺序是硬的：**先本地，再 `--fuzzy`（仍然免费），最后才考虑付费。**
本地结果绝不会被标成云端结果 —— `source` 只有 `local` / `cloud` 两个值。

> **计费状态（2026-10-28）：全部免费，不用 token。** 上游默认免费，只有运营端显式设 `FS_PAID=1`
> 才会恢复 402 / x402。只限量：每 IP 20 次/分钟、云端 analyze 每访客每天 200 次。
> `FS_QUOTA` 可以不设，本 skill 无需改动。

## 快速开始

```bash
SKILL_DIR="<路径>/skills/feeling-search"

python "$SKILL_DIR/scripts/fs_api.py" status
python "$SKILL_DIR/scripts/fs_api.py" analyze "潮湿的南方夏天午后，老旧风扇在转"
python "$SKILL_DIR/scripts/fs_api.py" lookup 冷光
python "$SKILL_DIR/scripts/fs_api.py" style-words cyberpunk
```

零第三方依赖，Python 3.8+，只用标准库。Windows 控制台中文乱码时先设 `PYTHONIOENCODING=utf-8`。

## 子命令

| 命令 | 作用 | 计费 |
|---|---|---|
| `status` | 额度 / 缓存 / 连通性体检 | 免费 |
| `dict [--refresh] [--with-items]` | 拉取或刷新词表缓存 | 免费 |
| `analyze <文本>` | 一句描述 → 感受词 + 风格 | 本地免费；`--allow-cloud` 时 1 次额度 |
| `lookup <词>` | 一个词 → 落点风格、共现词、对立词 | 免费 |
| `style-words <风格id>` | 一个风格 → 挂了哪些词 | 免费 |
| `style <风格id>` | 风格详情含图与出处 | 1 次额度 |
| `images <id1,id2,…>` | 批量取图，最多 5 个 | 1 次额度 |

通用参数：`--json` · `--offline`（只读缓存，绝不联网）· `--refresh` ·
`--words N`（1–12）· `--styles N`（1–30）· `--fuzzy`（连近义词一起匹配，免费）。
全局参数写在子命令前或后都行。

## 环境变量

| 变量 | 必填 | 说明 |
|---|---|---|
| `FS_QUOTA` | 否 | 云端额度 token。**免费期（2026-10-28 起）留空即可，云端照样能调**；只有运营端打开 `FS_PAID=1` 时才需要 |
| `FS_API_BASE` | 否 | 服务端点，默认 `https://xiximm.cloud` |
| `FS_CACHE_DIR` | 否 | 词表缓存目录，默认 `~/.cache/feeling-search` |
| `FS_CACHE_TTL` | 否 | 缓存有效期秒数，默认 604800（7 天） |

## 怎么读结果

- `words[].share` —— 这个词被几个风格使用，**≤6 是标识词**（风格专属），越大越泛
- `styles[].score` —— `Σ q² / √词条数 / 向量模长`，风格名被直接说出时额外 +1.5
- `styles[].matched` —— 这个风格命中了输入里的哪些词，用来解释结果
- `words[].gloss` 是**近义词 + 易混词混合的词袋**（「温暖」的串里带「冷寂」）。
  `--fuzzy` 会拿它做匹配，因此可能带进反义词 —— 看到不对路就去掉 `--fuzzy`

图片对象带 `thumb` / `full` 两个尺寸、`kind`（`work` 有出处的真作品 · `synthetic` AI 示意图 ·
`placeholder` 占位）与 `credit` / `license` / `source_url`。
**`placeholder` 不要当风格样本引用。**

## 目录结构

```
skills/feeling-search/
├── SKILL.md                      # 给模型读的正文
├── references/api-contract.md    # 线上 API 完整契约
└── scripts/fs_api.py             # 零依赖客户端
```

词表**不随包分发**：首次运行时从免费的 `/v2/dictionary` 拉到本地缓存，
所以包体只有几 KB，数据也始终是最新的。

## 相关链接

- 线上站点：<https://xiximm.cloud>
- API 契约：[`skills/feeling-search/references/api-contract.md`](skills/feeling-search/references/api-contract.md)

## 许可

MIT © 2026 xixi048
