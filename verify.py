#!/usr/bin/env python3
"""校验 BIP39 助记词(多语言) / BIP39 mnemonic validator (multi-language).

用法 / Usage:
    python3 verify.py                        # 校验 README*.md 里全部语言的助记词
    python3 verify.py --lang zh-Hans          # 只校验简体中文(用于 -m)
    python3 verify.py -m "abandon abandon …"  # 校验任意一条(按 --lang 选词表)
    python3 verify.py --seed                 # 顺便输出 BIP39 种子
    python3 verify.py --list-languages

退出码 / Exit code: 0 = 全部通过, 1 = 有失败, 2 = 环境问题

扫描本目录所有 `README*.md`,每条助记词前用 `<!-- lang: xx -->` 标注语言,据此选词表分组。
仅依赖标准库。 / Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
BASE_URL = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039"

# 语言代码 -> (本地文件名, 远端文件名, 官方 SHA-256)
LANGS: dict[str, tuple[str, str, str]] = {
    "en": (
        "english.txt",
        "english.txt",
        "2f5eed53a4727b4bf8880d8f3f199efc90e58503646d9ff8eff3a2ed3b24dbda",
    ),
    "zh-Hans": (
        "chinese_simplified.txt",
        "chinese_simplified.txt",
        "5c5942792bd8340cb8b27cd592f1015edf56a8c5b26276ee18a482428e7c5726",
    ),
    "zh-Hant": (
        "chinese_traditional.txt",
        "chinese_traditional.txt",
        "417b26b3d8500a4ae3d59717d7011952db6fc2fb84b807f3f94ac734e89c1b5f",
    ),
}

VALID_LENGTHS = (12, 15, 18, 21, 24)
# 只认 LANGS 里真实存在的语言代码,这样文档正文里提到 `<!-- lang: xx -->` 之类的
# 举例文字不会被误当成标记 / only real language codes count as markers
LANG_MARKER = re.compile(
    r"<!--\s*lang:\s*(" + "|".join(re.escape(k) for k in sorted(LANGS, key=len, reverse=True)) + r")\s*-->"
)
CODE_BLOCK = re.compile(r"^```[^\n]*\n(.*?)^```", re.M | re.S)
PBKDF2_ROUNDS = 2048


class EnvError(Exception):
    pass


def mnemonic_re(lang: str) -> re.Pattern:
    """按语言构造助记词正则。中文词表每「词」是一个汉字,不用空格分隔。"""
    if lang == "en":
        return re.compile(r"^[a-z]+(?: [a-z]+){11,23}$")
    return re.compile(r"^[　-鿿]+$")


def ensure_wordlist(lang: str, download: bool = True) -> list[str]:
    local, remote, want_sha = LANGS[lang]
    path = HERE / local
    if not path.exists():
        if not download:
            raise EnvError(f"缺少词表 {local} / wordlist missing")
        print(f"下载词表 / downloading {local} …", file=sys.stderr)
        try:
            data = urllib.request.urlopen(f"{BASE_URL}/{remote}", timeout=30).read()
        except Exception as exc:  # noqa: BLE001
            raise EnvError(f"下载失败 / download failed: {exc}") from exc
        path.write_bytes(data)

    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != want_sha:
        raise EnvError(
            f"词表哈希不符 / wordlist hash mismatch ({local}):\n"
            f"  期望 expected: {want_sha}\n  实际 actual  : {digest}"
        )
    words = [ln.strip() for ln in raw.decode("utf-8").splitlines() if ln.strip()]
    if len(words) != 2048:
        raise EnvError(f"{local} 应为 2048 词,实际 {len(words)}")
    if len({w[:4] for w in words}) != 2048:
        raise EnvError(f"{local} 前 4 字符不唯一 / prefixes not unique")
    return words


def check(mnemonic: str, words: list[str], lang: str) -> tuple[bool, str, bytes, str]:
    """返回 (是否通过, 原因, 熵, 校验位)。中文助记词按字切分,英文按空格切分。"""
    ws = list(mnemonic) if lang != "en" else mnemonic.split()
    if len(ws) not in VALID_LENGTHS:
        return False, f"词数 {len(ws)} 非法 / invalid length", b"", ""
    known = set(words)
    unknown = [w for w in ws if w not in known]
    if unknown:
        return False, f"词不在词表 / not in wordlist: {unknown}", b"", ""

    bits = "".join(format(words.index(w), "011b") for w in ws)
    ent_bits = len(bits) * 32 // 33
    payload, checksum = bits[:ent_bits], bits[ent_bits:]
    entropy = bytes(int(payload[i : i + 8], 2) for i in range(0, len(payload), 8))
    digest = "".join(format(b, "08b") for b in hashlib.sha256(entropy).digest())
    if not digest.startswith(checksum):
        return (
            False,
            f"校验位不符 / checksum mismatch: got {checksum}, want {digest[:len(checksum)]}",
            entropy,
            checksum,
        )
    return True, "ok", entropy, checksum


def to_seed(mnemonic: str, passphrase: str = "") -> str:
    """BIP39 种子: PBKDF2-HMAC-SHA512, salt = 'mnemonic' + passphrase, 2048 轮。"""
    return hashlib.pbkdf2_hmac(
        "sha512",
        mnemonic.encode("utf-8"),
        ("mnemonic" + passphrase).encode("utf-8"),
        PBKDF2_ROUNDS,
    ).hex()


def harvest(md: str, wanted: set[str] | None) -> list[tuple[str, str]]:
    """从 README 里按 `<!-- lang: xx -->` 分组抽取助记词,返回 [(lang, mnemonic)]。"""
    out: list[tuple[str, str]] = []
    pos = 0
    current = "en"
    for m in LANG_MARKER.finditer(md):
        for block in CODE_BLOCK.findall(md[pos : m.start()]):
            for line in block.splitlines():
                line = line.strip()
                if line and mnemonic_re(current).match(line):
                    if wanted is None or current in wanted:
                        out.append((current, line))
        current = m.group(1)
        pos = m.end()
    for block in CODE_BLOCK.findall(md[pos:]):
        for line in block.splitlines():
            line = line.strip()
            if line and mnemonic_re(current).match(line):
                if wanted is None or current in wanted:
                    out.append((current, line))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description="校验 BIP39 助记词 / validate BIP39 mnemonics (multi-language)"
    )
    ap.add_argument("-m", "--mnemonic", help="要校验的助记词")
    ap.add_argument("-l", "--lang", default="en", choices=sorted(LANGS), help="-m 使用的词表语言")
    ap.add_argument("--seed", action="store_true", help="同时输出 BIP39 seed")
    ap.add_argument("--passphrase", default="", help="BIP39 passphrase(默认空)")
    ap.add_argument("--no-download", action="store_true", help="禁止联网下载词表")
    ap.add_argument("--list-languages", action="store_true")
    args = ap.parse_args()

    if args.list_languages:
        for k, (local, _r, sha) in LANGS.items():
            print(f"{k:9s} {local:26s} {sha}")
        return 0

    if args.mnemonic:
        wanted = {args.lang}
        try:
            words = ensure_wordlist(args.lang, download=not args.no_download)
        except EnvError as exc:
            print(f"环境错误 / env error: {exc}", file=sys.stderr)
            return 2
        print(f"词表 / wordlist : {LANGS[args.lang][0]}  (2048 words, SHA-256 verified)")
        ok, reason, ent, cs = check(args.mnemonic.strip(), words, args.lang)
        print(("OK   " if ok else "FAIL ") + args.mnemonic.strip())
        print(f"       {reason if not ok else f'entropy={ent.hex()} checksum={cs}'}")
        if args.seed and ok:
            print(f"       seed={to_seed(args.mnemonic.strip(), args.passphrase)}")
        return 0 if ok else 1

    readmes = sorted(HERE.glob("README*.md"))
    if not readmes:
        print("找不到 README*.md / no README*.md found", file=sys.stderr)
        return 2
    items: list[tuple[str, str, str]] = []
    for path in readmes:
        for lang, m in harvest(path.read_text(encoding="utf-8"), None):
            items.append((lang, m, path.name))
    if not items:
        print("README*.md 里没找到助记词 / no mnemonics found", file=sys.stderr)
        return 2

    loaded: dict[str, list[str]] = {}
    try:
        for lang in sorted({l for l, _m, _f in items}):
            loaded[lang] = ensure_wordlist(lang, download=not args.no_download)
    except EnvError as exc:
        print(f"环境错误 / env error: {exc}", file=sys.stderr)
        return 2

    for lang in sorted(loaded):
        print(f"词表 / wordlist : {LANGS[lang][0]}  (2048 words, SHA-256 verified)")

    passed = 0
    for lang, m, src in items:
        ok, reason, ent, cs = check(m, loaded[lang], lang)
        passed += ok
        print(("OK   " if ok else "FAIL ") + m + f"   [{src}]")
        print(f"       {f'entropy={ent.hex()} checksum={cs}' if ok else reason}")
        if args.seed and ok:
            print(f"       seed={to_seed(m, args.passphrase)}")

    print(f"\n{passed}/{len(items)} valid")
    return 0 if passed == len(items) else 1


if __name__ == "__main__":
    sys.exit(main())
