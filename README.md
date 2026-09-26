# awesome-bip39

**Meaningful BIP39 mnemonics** — all 35 of them. Every one reads as an actual sentence, and every one
is fully **valid**: all 12 words come from the official BIP39 wordlist, and the 4-bit SHA-256 checksum
embedded in the word indices is consistent with the entropy. Any standard BIP39 implementation will
import them.

The list covers both official wordlists that fit this task:

| Wordlist | Words | Characters per "word" | So 12 words = |
|---|---|---|---|
| `english.txt` | 2048 | 3–8 letters | 12 English words |
| `chinese_simplified.txt` | 2048 | **1 character** | **12 Chinese characters** |

> **[中文译本](README.zh-CN.md)**(`README.zh-CN.md`)

`chinese_traditional.txt` has the same shape (2048 single characters), but this repository does not
cover Traditional Chinese mnemonics yet.

---

## ⚠️ Security Warning

Every mnemonic in this file is publicly known and readable by anyone. They exist for learning,
testing, and demonstrating the BIP39 wordlist and checksum mechanics. **Never** use them to create or
restore a wallet that holds real funds.

---

## Quick Check

```bash
python3 verify.py                 # validates all 70 listings (35 mnemonics, each in both files)
python3 verify.py --seed          # also prints the BIP39 seed (PBKDF2-HMAC-SHA512, 2048 rounds)
python3 verify.py -m "your twelve words here …"                   # validate one, English wordlist
python3 verify.py --lang zh-Hans -m "努力向上才能令人生都精彩"   # validate one, Simplified Chinese
python3 selftest.py               # regression-test verify.py against the official Trezor vectors
```

`verify.py` is standard-library only. It downloads the official wordlists when they are missing,
confirms each one by SHA-256, then checks word membership and the checksum bits. Exit code 0 means
everything passed, so it is CI-friendly. It scans every `README*.md` in this directory and picks the
wordlist per mnemonic based on the `lang: en` / `lang: zh-Hans` markers, so each language is checked
against its own wordlist.

`selftest.py` regression-tests `verify.py` against the 24 official Trezor vectors (12/18/24-word
lengths), covering checksum validation, entropy recovery and seed derivation.

## Files

| File | Purpose |
|---|---|
| `README.md` | This file, in English. All 35 mnemonics. |
| `README.zh-CN.md` | 中文译本,内容与本文件相同 |
| `verify.py` | The multi-language validator |
| `selftest.py` | Official-vector regression test |
| `english.txt` | Auto-downloaded wordlist, verified by SHA-256 |
| `chinese_simplified.txt` | Simplified Chinese wordlist |
| `chinese_traditional.txt` | Traditional Chinese wordlist |
| `vectors.json` | Auto-downloaded official vectors |

---

## Wordlist Source

| | |
|---|---|
| Files | [`english.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) · [`chinese_simplified.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt) · [`chinese_traditional.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt) |
| Repo | `github.com/bitcoin/bips`, directory `bip-0039/` |
| Count | 2048 per wordlist |
| SHA-256 | `english.txt` `2f5eed53…b24dbda`<br>`chinese_simplified.txt` `5c594279…7c5726`<br>`chinese_traditional.txt` `417b26b3…c1b5f` |

---

## The Mnemonics

### Part 1 — English (19)

<!-- lang: en -->

#### 1. Motivational

```
climb above all silent worry then shine like you have never before
```

> Climb above every silent worry, and shine as though you never had before.

entropy `2b001019e43fddc0717c0dff2d36540a` · checksum `0001`

#### 2. Departure

```
climb wild mountain cross wide river then float across vast ocean alone
```

> Climb wild mountains, cross wide rivers, then float across the vast ocean alone.

entropy `2b1f62421a0fab75b80ac9025e366383` · checksum `0111`

#### 3. The Elder

```
old wise person teach lesson about life that you will never forget
```

> An old wise person teaches a lesson about life that you will never forget.

entropy `9a1f8e8d6f480600e056ffff3f66542d` · checksum `1010`

> **Note** — the subject and verb do not agree (`person teach`, not `person teaches`). The wordlist
> has no third-person singular `-s` form of a verb; only nouns take `-s`, so verbs must stay bare.

#### 4. Falling and Rising

```
when you fall you cry alone then you stand strong soon again
```

> When you fall you cry alone, then you soon stand strong again.

entropy `fa3fe548ff93520df80ff9e49ae73d02` · checksum `0101`

> **Note** — **this one really is awkward; do not use it as a model.** The ideal wording is
> `when you fall you cry alone then you stand strong once again`, but its checksum does not match
> (entropy `fa3fe548ff93520df80ff9e49ae66a02`, actual checksum `0100`, while the words carry `0101`).
> `once` was swapped for `soon` to make the sentence validate, which is why it now reads as "you
> stand back up very quickly".

#### 5. Quiet Night

```
calm soft night flame glow slow sweet sleep where you will dream
```

> A calm, soft night; the flame glows; slow sweet sleep where you will dream.

entropy `2099ca562c263d9876ee59fa5fe7eca1` · checksum `0100`

#### 6. Voyage

```
silver moon light above calm ocean where dream boat sail home alone
```

> Silver moonlight above the calm ocean, where a dream boat sails home alone.

entropy `c8d1f20600420931fe921418d7c5b403` · checksum `0111`

#### 7. Friendship

```
good sister that stay near you when other people leave you alone
```

> A good sister stays near you when other people leave you alone.

entropy `6479337fea7939fe7e8ce8a2cfdffc83` · checksum `0111`

#### 8. Time

```
time will teach you lesson that also very old age can tell
```

> Time will teach you a lesson that even very old age can tell.

entropy `e25f677a7f9807bfc1d7979a009883ef` · checksum `0110`

#### 9. Perseverance

```
hard work can turn you brave when you never say you quit
```

> Hard work can turn you brave, as long as you never say "quit".

entropy `693fb083f56ff236be8ff99517fffcd7` · checksum `1110`

#### 10. Patience

```
one small water drop over long year must wear away old stone
```

> One small drop of water, over a long year, must wear away even old stone.

entropy `9ab98fdf21b9df07bfbc90f8620e686b` · checksum `0010`

#### 11. Kindness

```
one kind word can turn one more angry heart into warm smile
```

> One kind word can turn one more angry heart into a warm smile.

entropy `9aaf53f5907ead3563f0476a4ebbdce6` · checksum `0101`

#### 12. Wisdom

```
one old man can tell young boy story that you never forget
```

> An old man can tell a young boy a story that he will never forget.

entropy `9ab3421b107dedfe86aeb4dfffe6542d` · checksum `1010`

#### 13. Hope

```
one long night will become short when you have one good dream
```

> One long night becomes short once you have one good dream.

entropy `9ab07a567d913f8dbe8ff969b35591a1` · checksum `0100`

#### 14. Loyalty

```
one true friend will stay near you until nothing else can stay
```

> One true friend stays near you until nothing else can stay.

entropy `9abd2973fd9d4f273fcfd7196c90483ea` · checksum `0111`

#### 15. Warmth

```
one warm smile can make one very sad young face bright again
```

> One warm smile can make one very sad young face bright again.

entropy `9abee732907869357cbdedff4a307002` · checksum `0101`

#### 16. Composure

```
one calm heart will wait long time until one warm autumn day
```

> One calm heart will wait a long time, right up to one warm autumn day.

entropy `9aa411a97d9f6707b897719abee43e9c` · checksum `0000`

#### 17. Growth

```
one long road can make you strong also kind also very wise
```

> One long road can make you strong, also kind, also very wise.

entropy `9ab07aeb907869fe75c83a7a80ebcbfe` · checksum `0011`

> **Note** — `and` and `to` are both missing from the English wordlist, so the three adjectives can
> only be chained by repeating `also`. An earlier draft ended `... also very brave old`, which
> checksummed but read badly; `wise` was the replacement that kept the sentence intact.

#### 18. Learning

```
young mind can learn much more when you hold one great book
```

> A young mind can learn much more when you hold one great book.

entropy `ff519c83bf69111fbe8ff96c9355988c` · checksum `1100`

#### 19. Morning

```
morning light come over green hill then one young girl will sing
```

> Morning light comes over the green hill, then one young girl will sing.

entropy `8ff030b84ef664d7780cd5ff4c4bece4` · checksum `1010`

### Part 2 — Chinese Simplified (16)

<!-- lang: zh-Hans -->

> Every "word" in `chinese_simplified.txt` is a **single character**, so 12 words is 12 characters —
> that is, a whole sentence. The checksum mechanics are identical to English.

#### 1. 励志 / Inspirational

```
努力向上才能令人生都精彩
```

> Strive upward, and only then can life be made wonderful.

entropy `7f01244d80d2b20ad4e808030164db43` · checksum `0001`

> **Note** — only this phrasing, 令人生都精彩, matches the checksum. The smoother 让人生更精彩
> ("make life even better") does not.

#### 2. 进步 / Progress

```
每天总进步一点点就会成功
```

> Improve a little every day, and you will succeed.

entropy `28e1d0638422d60043006003c08810a7` · checksum `0100`

> **Note** — 每天多进步一点点 ("improve a bit more each day") fails the checksum, so 多 had to be
> replaced by 总.

#### 3. 勇气 / Courage

```
真正勇猛的人敢于面对一切
```

> The truly brave dare to face anything.

entropy `28622e785f50000220501c0640800093` · checksum `0111`

> **Note** — the intended wording was 真正**勇敢**的人…, but the checksum only accepts 勇猛.

#### 4. 家庭 / Family

```
一家人平静就是最大的幸福
```

> A family at peace is the greatest happiness.

entropy `00211c0407c6f0078010b0016002b436` · checksum `1100`

> **Note** — the intended wording was 一家人**平安**就是最大的幸福 ("when a family is safe and sound…"),
> but that fails. Changing 安 to 静 at position 3 is the only edit that works.

#### 5. 友情 / Friendship

```
好朋友是人间最宝贵之礼品
```

> A good friend is the most precious gift in this world.

entropy `0cf4b1660020102045848068e106b70c` · checksum `1001`

> **Note** — 人生最宝贵的礼物 ("life's most precious gift") does not match; the 人间…之礼品
> wording does.

#### 6. 时间 / Time

```
时间会证实你的努力有意义
```

> Time will show that your effort was meaningful.

entropy `0282041112d0ac238003f80920185307` · checksum `1010`

> **Note** — 时间会证明… does not match; the only difference is 明 → 实.

#### 7. 追梦 / Dreams

```
有心的人走遍天下都会发光
```

> Whoever keeps their heart travels the world and shines.

entropy `00c2300000829701c3a02c0b20881290` · checksum `0111`

> **Note** — the intended wording was 有梦的人… ("those who dream…"), but the checksum only accepts
> 有心.

#### 8. 坚持 / Perseverance

```
坚持努力的人定会获得成功
```

> Those who persist and work hard will succeed.

entropy `4be605fc0490000201b8226480f410a7` · checksum `0100`

> **Note** — 终会获得 ("will eventually get") does not match; 定会获得 does.

#### 9. 读书 / Study

```
学书会让你的世界更加宽广
```

> Studying books widens your world.

entropy `072610112a611c0008d17326815dc016` · checksum `1101`

> **Note** — 读书会让… ("reading will make…") does not match; 学书 works.

#### 10. 春天 / Spring

```
春回来了万物生长一片生机
```

> Spring has returned; all things grow with vigour.

entropy `4de3f40a80528c1500c0d10027500c05` · checksum `1101`

> **Note** — 春回大地万物复苏生机勃勃 is far smoother, but its checksum does not match. This is the
> only readable result the search turned up.

#### 11. 识人 / Judging Character

```
路远知马力年久才见真人心
```

> A long road tests a horse's strength; long years reveal a true heart.

entropy `1b28847015d0920997e1591c850c0408` · checksum `1100`

> **Note** — 遥 is not in the wordlist, so only 远 is available. The proverb 路遥知马力,日久见人心
> is therefore one character short.

#### 12. 善良 / Kindness

```
善良的人福气总是不会太坏
```

> A kind person is never short of good fortune.

entropy `65aaa4000086d826463802008088da28` · checksum `0101`

#### 13. 付出 / Effort

```
所有的努力付出必将有回报
```

> Every effort and contribution will be rewarded.

entropy `076018003f80932380e8fa1c40187e95` · checksum `0000`

#### 14. 强大 / Strength

```
真正的强大是内心更加安定
```

> Real strength is a calmer heart.

entropy `28622c000f30160084488c26815c9f03` · checksum `0111`

#### 15. 信念 / Inner Light

```
心里有光的人的确从不迷路
```

> Someone who carries light inside truly never loses their way.

entropy `11812803107000020001580c2013148d` · checksum `1001`

#### 16. 陪伴 / Company

```
陪伴都是最长情的告白礼物
```

> Companionship is the longest-lasting confession, and a gift in itself.

entropy `eab8842c8021603445700042a4e6b705` · checksum `0100`

> **Note** — 就是 ("is exactly") fails the checksum here, so the plainer 都是 had to be used. The
> trailing 礼物 is likewise not a free choice: 陪伴是最长情的告白 alone is 11 characters, one short
> of the 12 a BIP39 Chinese mnemonic requires.

---

## Why the English Sentences Sound Awkward

The BIP39 wordlist was not designed for prose. There are three hard constraints:

1. **Words are 3–8 characters**, 2048 in total, uniquely encoded by their first 4 characters — so
   `there` and `theme` cannot both exist.
2. **Common function words are deliberately excluded.** All of the following are absent:

   | Absent | Available instead |
   |---|---|
   | `the` `and` `to` `be` `is` `of` `it` `my` `your` | no articles at all; only `one` `all` `any` `own` |
   | `with` `up` `down` `far` `as` | `over` `under` `above` `below` `into` `upon` `near` `close` |
   | `not` `no` `but` `so` `or` `if` | `never` `only` `just` `also` `because` `once` `since` `until` |
   | `rise` `fear` `doubt` `silence` `dark` `data` `beat` `burn` | `fall` `worry` `gloom` `silent` `alone` `crash` `error` `glow` |
   | third-person singular verb `-s` | verbs are bare: `person teach` |

3. **Evocative words are scarce.** `amber`, `emerge`, `youth`, `gospel`, `wisdom` occupy a handful of
   the 2048 slots between them.

The result is telegraphic, translated-sounding clauses rather than natural English. Items 1, 2, 5, 6
and most of 7–19 read reasonably well; items 3, 4 and 17 have visible grammatical flaws, flagged
in place.

## Why Chinese Is Easier

The Chinese wordlist has none of those constraints, because every "word" is a single character:

- All the common function words are present — `的` `一` `是` `在` `不` `了` `有` `和` `人` `这` `中` — and
  they sit at the very front of the list.
- So genuinely grammatical, natural-sounding 12-character sentences are possible, with no
  translated-sounding indirection.
- The trade-off is that 2048 slots are heavily padded with single-character function words, so
  sentence-like orderings are a small fraction of the combination space.

It is not freely writable either: some characters are simply missing from the 2048, for example
`己` `懈` `遥` `盎` `暖`. That is why 遥 in the proverb 路遥知马力,日久见人心 had to become 远,
leaving the sentence one character short.

---

## Where the Entropy Came From

**Honest disclosure:**

- The words were chosen by hand. A script only checked word membership and the 4 checksum bits; it
  never took part in writing the sentences.
- The entropy is *derived from* the word order, not random. These 35 mnemonics cover 35 points out
  of 2048¹² possible combinations per wordlist, and carry **no cryptographic randomness**.
- A hand-picked 12-word set has only a **1 in 16** chance of carrying a correct checksum. Many of
  these were found by trying synonyms until one fit — `doubt` → `worry`, `peak` → `mountain`,
  `once` → `soon`, 勇敢 → 勇猛, 明 → 实, 安 → 静. Their wording was therefore chosen *by* the
  checksum bits, not the other way round.
- This is most visible in the Chinese items: nearly every one carries a visible scar where a smoother
  phrasing failed the checksum. Each is noted under the sentence.
- For **cryptographically random** mnemonics, generate entropy with `secrets` / `os.urandom` and run
  it through BIP39. Do not pick words out of a wordlist.

---

## References

- This repository: <https://github.com/lizzzhh/awesome-bip39>
- **[中文译本](README.zh-CN.md)**(`README.zh-CN.md`)
- BIP-39 specification: <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>
- English wordlist: <https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt>
- Simplified Chinese wordlist: <https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt>
- Traditional Chinese wordlist: <https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt>
- Official Trezor test vectors: <https://github.com/trezor/python-mnemonic/blob/master/vectors.json>
  (note: no longer in the `bitcoin/bips` repo — `bip-0039/vectors.json` returns 404)

⚠️ Never use anything in this file for real funds.
