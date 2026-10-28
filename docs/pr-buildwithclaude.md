## Component Details

- **Type**: Skill (`plugins/all-skills/skills/feeling-search/`)
- **Category**: `design`
- **Purpose**: turn one colloquial sentence into art-direction vocabulary — the feeling words it hits
  plus the visual styles those words map to (name, one-line definition, parent style, triggering
  words, reference images). Positioned as a commercial-grade art reference chart / art-style prompt
  encyclopedia for Midjourney, Stable Diffusion and Flux.

## What's included

```
plugins/all-skills/skills/feeling-search/
├── SKILL.md
├── references/api-contract.md   endpoint contract (v2 API)
└── scripts/fs_api.py            zero-dependency client (stdlib only)
```

## Fixes from the closed #569

Thanks for the review — all three points addressed:

1. **`metadata` dropped.** Frontmatter now only uses `name`, `description`, `category`, `license`,
   which validates against `scripts/skill-schema.json` (`additionalProperties: false`).
2. **Scripts shipped.** `scripts/fs_api.py` and `references/api-contract.md` are in this PR next to
   `SKILL.md`, so every path the skill tells the agent to run exists in the submission.
3. **Valid category.** `category: design` (not `gaming`).

## Testing

- `python scripts/fs_api.py --help` runs on Python 3.8+ with no third-party packages.
- `python scripts/fs_api.py analyze "下雨天一个人走在便利店门口，冷白灯光"` →
  `代尔夫特画派 0.25 / 灰烬寒冬 0.22 / 风格派 0.22`, each with the matched words and a definition.
- `--offline` completes without network; the cloud call only fires when the local lexicon returns
  zero matches **and** the caller passes `--allow-cloud`.
- Only disk write: a lexicon cache under the user's own `~/.cache/feeling-search/`.

## Prompt

```
$feeling-search 我想让画面有那种雨天便利店门口冷白灯光的感觉
```
