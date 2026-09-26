#!/usr/bin/env python3
"""用官方 Trezor 测试向量回归 verify.py / regression-test verify.py against official vectors.

用法 / Usage:
    python3 selftest.py            # 下载 vectors.json 并跑全部 24 条
    python3 selftest.py --no-download

检查三项 / checks three things per vector:
    1. checksum  —— verify.check() 是否判定为有效
    2. entropy   —— 反推出的熵是否等于向量里的 entropy
    3. seed      —— verify.to_seed(m, "TREZOR") 是否等于向量里的 seed

注意: trezor/python-mnemonic 的 vectors.json 里第 3 个字段是**带 "TREZOR" passphrase** 的 seed,
不是空 passphrase 的 seed。/ Note: field 3 is the seed WITH the "TREZOR" passphrase.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import verify  # noqa: E402

VECTORS_URL = (
    "https://raw.githubusercontent.com/trezor/python-mnemonic/master/vectors.json"
)
VECTORS_PATH = pathlib.Path(__file__).resolve().parent / "vectors.json"


def load_vectors(download: bool) -> list:
    if not VECTORS_PATH.exists():
        if not download:
            raise SystemExit("缺少 vectors.json / missing vectors.json")
        print("下载测试向量 / downloading vectors …", file=sys.stderr)
        VECTORS_PATH.write_bytes(urllib.request.urlopen(VECTORS_URL, timeout=30).read())
    return json.loads(VECTORS_PATH.read_text(encoding="utf-8"))["english"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-download", action="store_true")
    args = ap.parse_args()

    words = verify.ensure_wordlist("en", download=not args.no_download)
    vectors = load_vectors(download=not args.no_download)
    print(f"官方向量 / official vectors: {len(vectors)} 条\n")

    failures = []
    for ent_hex, mnemonic, seed_trezor, _xprv in vectors:
        ok, reason, ent, _cs = verify.check(mnemonic, words, "en")
        results = {
            "checksum": ok,
            "entropy": ent.hex() == ent_hex,
            "seed": verify.to_seed(mnemonic, "TREZOR") == seed_trezor,
        }
        if not all(results.values()):
            failures.append((mnemonic[:40], results, reason))

    for name in ("checksum", "entropy", "seed"):
        n = 0
        for ent_hex, mnemonic, seed_trezor, _ in vectors:
            ok, _r, ent, _c = verify.check(mnemonic, words, "en")
            n += {
                "checksum": ok,
                "entropy": ent.hex() == ent_hex,
                "seed": verify.to_seed(mnemonic, "TREZOR") == seed_trezor,
            }[name]
        print(f"  {name:9s} {n}/{len(vectors)}")

    if failures:
        print("\n失败 / failures:")
        for m, r, reason in failures:
            print(f"  {m}…  {r}  {reason}")
        return 1
    print(f"\n{len(vectors)}/{len(vectors)} 全部通过 / all passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
