#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构建 WorkBuddy 开放平台专用的技能包。

为什么单独出这个包：开放平台对 SKILL.md frontmatter 有 8 个必填字段
（name / display_name / display_name_en / description / description_zh /
description_en / version / author），而通用 Skill 规范只要 name + description。
直接在源文件里堆字段会污染其他商店的上架物料，所以这里只在打包时注入。

用法：
    python scripts/build_wb.py                # 用 SKILL.md 里的版本号
    python scripts/build_wb.py --version 1.0.3
产物：
    dist/wb/feeling-search-wb-<version>.zip   # SKILL.md 在包根，目录两层
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, "skills", "feeling-search")
OUT_DIR = os.path.join(ROOT, "dist", "wb")

# 开放平台 8 个必填字段里，通用规范没有的 5 个
DISPLAY_NAME = "感觉检索 · 美术对照表"
DISPLAY_NAME_EN = "Feeling Search · Art Reference Chart"

DESCRIPTION_ZH = (
    "输入一句口语化的感觉描述（如「雨夜便利店的冷白灯光」），"
    "检索出最匹配的视觉风格，并给出触发它的感受词、风格定义与参考图。"
    "适合美术定调、AI 绘画提示词、概念设计与品牌视觉。"
)
DESCRIPTION_EN = (
    "Turn one colloquial sentence about a mood into the best-matching visual style, "
    "with the feeling words that triggered it, a one-line definition and reference images. "
    "Use for art direction, AI image prompts, concept art and brand visuals."
)

EXAMPLES_ZH = [
    "帮我找一种适合「雨夜便利店冷白灯光」的画风",
    "这种感觉在美术上叫什么：孤独、安静、街头霓虹",
    "给一个赛博朋克但不要太吵的方案，要湿冷、克制",
]
EXAMPLES_EN = [
    "Find an art style for a rainy night outside a convenience store",
    "What is the art term for lonely, quiet, neon-lit streets",
    "A cyberpunk look that is wet and restrained, not loud",
]

REQUIRED = [
    "name",
    "display_name",
    "display_name_en",
    "description",
    "description_zh",
    "description_en",
    "version",
    "author",
]


def yaml_str(s: str) -> str:
    """单行字符串加双引号并转义，避免冒号/引号破坏 YAML。"""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def split_frontmatter(text: str):
    """返回 (frontmatter 行列表, 正文)。frontmatter 不含首尾 --- 分隔符。"""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if not m:
        raise SystemExit("SKILL.md 不是以 --- frontmatter 开头")
    return m.group(1).splitlines(), m.group(2)


def detect_version(fm_lines) -> str:
    for line in fm_lines:
        m = re.match(r"^\s+version:\s*[\"']?([^\"'\s]+)[\"']?\s*$", line)
        if m:
            return m.group(1)
    raise SystemExit("frontmatter 里没找到 version")


def existing_keys(fm_lines) -> set:
    return {line.split(":", 1)[0].strip() for line in fm_lines if re.match(r"^[A-Za-z_-]+:", line)}


def build(version: str) -> str:
    src = os.path.join(SKILL_DIR, "SKILL.md")
    with open(src, encoding="utf-8") as f:
        text = f.read()

    fm_lines, body = split_frontmatter(text)
    have = existing_keys(fm_lines)

    inject = []
    if "display_name" not in have:
        inject.append("display_name: " + yaml_str(DISPLAY_NAME))
    if "display_name_en" not in have:
        inject.append("display_name_en: " + yaml_str(DISPLAY_NAME_EN))
    if "description_zh" not in have:
        inject.append("description_zh: " + yaml_str(DESCRIPTION_ZH))
        inject.append("description_en: " + yaml_str(DESCRIPTION_EN))
    if "version" not in have:
        inject.append("version: " + yaml_str(version))
    if "author" not in have:
        inject.append("author: " + yaml_str("xixi048"))

    # 选填但强烈建议：详情页的「试试这样用」
    if "examples_zh" not in have:
        inject.append("examples_zh:")
        inject += ["  - " + yaml_str(s) for s in EXAMPLES_ZH]
    if "examples_en" not in have:
        inject.append("examples_en:")
        inject += ["  - " + yaml_str(s) for s in EXAMPLES_EN]

    # 插在 license 之前（若没有 license 就追加到末尾），保持 name/description 打头
    out_fm = list(fm_lines)
    try:
        idx = next(i for i, l in enumerate(out_fm) if l.startswith("license:"))
    except StopIteration:
        idx = len(out_fm)
    out_fm[idx:idx] = inject

    new_text = "---\n" + "\n".join(out_fm) + "\n---\n" + body

    # 自检：8 个必填字段齐、name 为 hyphen-case、frontmatter 无尖括号
    keys = existing_keys(out_fm)
    missing = [k for k in REQUIRED if k not in keys]
    if missing:
        raise SystemExit("仍缺必填字段: " + ", ".join(missing))
    name_val = next(l.split(":", 1)[1].strip() for l in out_fm if l.startswith("name:"))
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name_val):
        raise SystemExit("name 不是 hyphen-case: " + name_val)
    if re.search(r"[<>]", "\n".join(out_fm)):
        raise SystemExit("frontmatter 含尖括号，会被驳回")

    os.makedirs(OUT_DIR, exist_ok=True)
    out_zip = os.path.join(OUT_DIR, "feeling-search-wb-%s.zip" % version)

    # 目录两层：SKILL.md + references/ + scripts/ 下的文件
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("SKILL.md", new_text)
        for sub in ("references", "scripts", "templates"):
            d = os.path.join(SKILL_DIR, sub)
            if not os.path.isdir(d):
                continue
            for fn in sorted(os.listdir(d)):
                p = os.path.join(d, fn)
                if os.path.isfile(p):
                    z.write(p, sub + "/" + fn)

    size = os.path.getsize(out_zip)
    if size > 3 * 1024 * 1024:
        raise SystemExit("包超过 3MB 上限: %.2f MB" % (size / 1048576.0))

    print("OK ->", out_zip)
    print("   size: %.1f KB (上限 3MB)" % (size / 1024.0))
    print("   version:", version)
    print("   fields:", ", ".join(REQUIRED))
    return out_zip


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None)
    args = ap.parse_args()

    if args.version:
        version = args.version
    else:
        with open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8") as f:
            fm, _ = split_frontmatter(f.read())
        version = detect_version(fm)

    build(version)


if __name__ == "__main__":
    main()
