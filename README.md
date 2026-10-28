# feeling-search · Agent Skill

**A commercial-grade art reference chart · the complete art-style encyclopedia · an AI prompt encyclopedia for visual styles.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776ab.svg)](https://www.python.org/)

> Turn a vague feeling into concrete visual style.

One colloquial sentence in, the visual style that fits best out — an **art reference chart** and
prompt encyclopedia behind every match, each style carrying its name, a one-line definition and
the words that triggered it.

This is not a toy style picker. It is a **working art-direction reference** you can put in front of a
real production: every style named and defined, mapped back from feeling words, so a brief like
"cold white light, empty convenience store, rain" lands on a concrete, defensible art direction instead
of five adjectives. Use it as an **art-style lookup table**, an **art-style prompt dictionary**
(Midjourney / Stable Diffusion / Flux), or a **style–word cross-reference** for concept art, game art
bibles and brand systems.

**中文说明见 [README.zh-CN.md](README.zh-CN.md).**

```
"Walking alone past a convenience store in the rain, cold white light"
   → words:  光 / 白 / 冷光 / 古寂 …
   → styles: ash-winter, gothic-stained-glass, ice-crystal-pale, karesansui …
```

## Why it exists

"I want it to feel like…" is where art direction starts and where vocabulary runs out.
This skill is the lookup table between a mood and the name of a style — useful for image-generation
prompts, concept art, game art direction, illustration, and brand visuals.

## Two routes

| Route | When | Network | Cost |
|---|---|---|---|
| Local lexicon | The sentence hits the cached word list (most cases) | No | Free |
| Cloud analyze | Nothing matched locally **and** `--allow-cloud` is set | Yes | 1 quota |

The order matters: **local first, then `--fuzzy` (still free), only then paid.**
The skill never presents a local result as a cloud one — `source` is always `local` or `cloud`.

> **Pricing status (2026-10-28): everything is free — no key, no quota token.** The upstream is
> free by default; paid 402 / x402 only turns on if the operator sets `FS_PAID=1`. Only rate limits
> apply (20/min per IP, 200 cloud calls per visitor per day). `FS_QUOTA` may stay unset.

## Quick start

```bash
SKILL_DIR="<path to>/skills/feeling-search"

python "$SKILL_DIR/scripts/fs_api.py" status
python "$SKILL_DIR/scripts/fs_api.py" analyze "a damp southern summer afternoon, an old fan turning"
python "$SKILL_DIR/scripts/fs_api.py" lookup 冷光
python "$SKILL_DIR/scripts/fs_api.py" style-words cyberpunk
```

Zero third-party dependencies, Python 3.8+, standard library only.
On Windows set `PYTHONIOENCODING=utf-8` if the console mangles Chinese.

## Commands

| Command | What it does | Billed |
|---|---|---|
| `status` | Quota / cache / reachability check | Free |
| `dict [--refresh] [--with-items]` | Pull or refresh the lexicon cache | Free |
| `analyze <text>` | One sentence → feeling words + visual styles | Free locally; 1 quota with `--allow-cloud` |
| `lookup <word>` | A word → its styles, co-occurring words, opposites | Free |
| `style-words <style-id>` | A style → the words attached to it | Free |
| `style <style-id>` | Style detail with images and credits | 1 quota |
| `images <id1,id2,…>` | Batch image fetch, max 5 | 1 quota |

Common flags: `--json` · `--offline` (cache only, never touches the network) · `--refresh` ·
`--words N` (1–12) · `--styles N` (1–30) · `--fuzzy` (match near-synonyms too, free).
Global flags work before or after the subcommand.

## Environment

| Variable | Required | Meaning |
|---|---|---|
| `FS_QUOTA` | No | Cloud quota token. **Free phase (2026-10-28 on): leave it empty — cloud calls still work.** Only needed if the operator turns billing on with `FS_PAID=1` |
| `FS_API_BASE` | No | Service endpoint, defaults to `https://xiximm.cloud` |
| `FS_CACHE_DIR` | No | Lexicon cache dir, defaults to `~/.cache/feeling-search` |
| `FS_CACHE_TTL` | No | Cache lifetime in seconds, defaults to 604800 (7 days) |

## Reading the output

- `words[].share` — how many styles use this word. **≤6 means it is a marker word** (style-specific)
- `styles[].score` — `Σ q² / √terms / ‖q‖`, plus 1.5 when the style name was named directly
- `styles[].matched` — which input words triggered this style; use it to explain the result
- `words[].gloss` is a **bag of near-synonyms and confusable words**, deliberately mixed
  (e.g. "warmth" carries "cold-desolation"). `--fuzzy` matches on it and can pull in opposites.

Image objects carry `thumb` / `full`, `kind` (`work` real CC0 work · `synthetic` AI illustration ·
`placeholder`), and `credit` / `license` / `source_url`. **Never cite `placeholder` as a style sample.**

## Layout

```
skills/feeling-search/
├── SKILL.md                      # what the agent reads
├── references/api-contract.md    # full HTTP API contract
└── scripts/fs_api.py             # zero-dependency client
```

The lexicon is **not** bundled — it is pulled once from the free `/v2/dictionary` endpoint and
cached locally, so the package stays a few kilobytes and the data stays current.

## Links

- Service & live demo: <https://xiximm.cloud>
- API contract: [`skills/feeling-search/references/api-contract.md`](skills/feeling-search/references/api-contract.md)

## License

MIT © 2026 xixi048
