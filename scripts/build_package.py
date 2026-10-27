#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构建「上传型渠道」用的技能包（Cow Skill Hub / 腾讯 SkillHub / 讯飞 Astron / machina.directory）。

与 build_wb.py 的区别：
- build_wb.py 产 WorkBuddy 开放平台专用包（注入 8 个必填 frontmatter 字段），走 dist/wb/
- 本脚本产**通用规范包**：SKILL.md 原样放在 zip 根，目录两层，不带任何注入字段

产物：
    dist/feeling-search-v<version>-skillroot.zip
    dist/feeling-search-v<version>-skillroot.zip.sha256
    dist/package-manifest-v<version>.json

用法：
    python scripts/build_package.py                # 版本取 SKILL.md frontmatter
    python scripts/build_package.py --version 1.0.3
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, "skills", "feeling-search")
OUT_DIR = os.path.join(ROOT, "dist")

# 包内允许的目录；其余（测试样本、备份、assets）一律不进包
INCLUDE_DIRS = ("references", "scripts")


def split_frontmatter(text: str):
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


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build(version: str) -> str:
    src = os.path.join(SKILL_DIR, "SKILL.md")
    with open(src, encoding="utf-8") as f:
        text = f.read()
    split_frontmatter(text)  # 只为校验 frontmatter 存在

    os.makedirs(OUT_DIR, exist_ok=True)
    out_zip = os.path.join(OUT_DIR, "feeling-search-v%s-skillroot.zip" % version)

    names = []
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("SKILL.md", text)
        names.append("SKILL.md")
        for sub in INCLUDE_DIRS:
            d = os.path.join(SKILL_DIR, sub)
            if not os.path.isdir(d):
                continue
            for fn in sorted(os.listdir(d)):
                p = os.path.join(d, fn)
                if os.path.isfile(p):
                    z.write(p, sub + "/" + fn)
                    names.append(sub + "/" + fn)

    size = os.path.getsize(out_zip)
    if size > 3 * 1024 * 1024:
        raise SystemExit("包超过 3MB 上限: %.2f MB" % (size / 1048576.0))

    digest = sha256_of(out_zip)
    with open(out_zip + ".sha256", "w", encoding="utf-8") as f:
        f.write("%s  %s\n" % (digest, os.path.basename(out_zip)))

    manifest = {
        "skill": "feeling-search",
        "version": version,
        "built_by": "scripts/build_package.py",
        "variants": {
            "skillroot": {
                "path": out_zip,
                "files": len(names),
                "sha256": digest,
                "note": "SKILL.md 位于 zip 根；适用于 Cow Skill Hub / machina.directory",
            },
            "flat": {
                "path": out_zip,
                "files": len(names),
                "sha256": digest,
                "note": "同 skillroot；若将来加入 assets/ 或 examples/，此形态仍保证不含测试样本与备份文件",
            },
            "repo": {
                "path": ROOT,
                "skill_relpath": "skills/feeling-search",
                "matches_standard_scan_path": True,
                "matched_pattern": "skills/{name}/",
                "note": "用于 skills.sh / skillstore.io 的仓库 URL 提交",
            },
        },
    }
    mpath = os.path.join(OUT_DIR, "package-manifest-v%s.json" % version)
    with open(mpath, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("OK ->", out_zip)
    print("   size: %.1f KB · files: %d" % (size / 1024.0, len(names)))
    print("   sha256:", digest)
    print("   files:", ", ".join(names))
    print("OK ->", mpath)
    return out_zip


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None)
    args = ap.parse_args()

    with open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8") as f:
        fm_lines, _ = split_frontmatter(f.read())

    version = args.version or detect_version(fm_lines)
    build(version)


if __name__ == "__main__":
    main()
