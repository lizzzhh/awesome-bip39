# awesome-bip39

**有语义的 BIP39 助记词** —— 每一句都读得通,而且**通过完整校验**(12 个词全部来自官方词表,
内嵌的 4 bit SHA-256 校验位与熵一致),可以被任何标准 BIP39 实现正常导入。

**Meaningful BIP39 mnemonics** — every one reads as an actual sentence *and* is fully **valid**
(all 12 words in the official wordlist, 4-bit SHA-256 checksum consistent with the entropy), so any
standard BIP39 implementation will import it.

支持英文与简体中文两套官方词表 / Covers both the English and Chinese Simplified official wordlists:

| | 词数 | 每「词」字数 | 12 词 = |
|---|---|---|---|
| `english.txt` | 2048 | 3–8 字母 | 12 个英文单词 |
| `chinese_simplified.txt` | 2048 | **1 个汉字** | **12 个汉字** |

中文词表全是单字,所以 12 词正好是 12 个汉字 —— 写中文句子反而比英文容易得多。

---

## ⚠️ 安全警告 / Security Warning

**中文**:本文件里的所有助记词都已公开,任何人都能读到。它们仅供学习、测试、演示 BIP39 词表与
校验机制之用。**绝对不要**用它们创建或恢复任何持有真实资产的钱包。

**English**:Every mnemonic here is publicly known. They are for learning, testing and demonstrating
the BIP39 wordlist and checksum mechanics only. **Never** use them to create or restore a wallet that
holds real funds.

---

## 快速验证 / Quick Check

```bash
python3 verify.py                 # 校验本文件里全部 19 句(8 英文 + 11 中文)
python3 verify.py --seed          # 顺便输出 BIP39 种子 (PBKDF2-HMAC-SHA512, 2048 轮)
python3 verify.py -m "your twelve words here …"          # 校验任意一条
python3 verify.py --lang zh-Hans -m "努力向上才能令人生都精彩"  # 指定词表语言
python3 selftest.py               # 用官方 Trezor 测试向量回归 verify.py 本身
```

`verify.py` 只依赖标准库。它会在缺失时自动下载官方词表,用 SHA-256 确认词表是原版,然后逐条检查
「词是否在词表内」和「校验位是否正确」。**全部通过时退出码为 0**,可用于 CI。

`selftest.py` 拿官方 24 条测试向量(含 12/18/24 词三种长度)回归验证 `verify.py` 的
checksum、entropy 反推、seed 推导三项,确认工具本身可信。

`verify.py` is standard-library only. It auto-downloads the official wordlist, confirms it by
SHA-256, then checks word membership and the checksum bits. Exit code 0 means everything passed,
so it is CI-friendly. `selftest.py` regression-tests `verify.py` against the 24 official Trezor
vectors (12/18/24-word lengths) — checksum, entropy recovery, and seed derivation.

## 文件 / Files

| 文件 / File | 说明 / Purpose |
|---|---|
| `README.md` | 本文件,含 8 句英文 + 11 句中文助记词 / this file: 8 English + 11 Chinese mnemonics |
| `verify.py` | 校验工具(多语言) / the multi-language validator |
| `selftest.py` | 官方向量回归 / official-vector regression test |
| `english.txt` | 自动下载的词表 / auto-downloaded wordlist (verified by SHA-256) |
| `chinese_simplified.txt` | 简体词表 / Simplified Chinese wordlist |
| `chinese_traditional.txt` | 繁体词表 / Traditional Chinese wordlist |
| `vectors.json` | 自动下载的官方向量 / auto-downloaded official vectors |

---

## 词表来源 / Wordlist Source

| | |
|---|---|
| 文件 / Files | [`english.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) · [`chinese_simplified.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt) · [`chinese_traditional.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt) |
| 来源 / Repo | `github.com/bitcoin/bips`,目录 `bip-0039/` |
| 词数 / Count | 每个词表 2048 |
| SHA-256 | `english.txt` `2f5eed53…b24dbda`<br>`chinese_simplified.txt` `5c594279…7c5726`<br>`chinese_traditional.txt` `417b26b3…c1b5f` |

---

## 助记词 / The Mnemonics

### 英文 / English

<!-- lang: en -->

#### 1. 励志 / Motivational

```
climb above all silent worry then shine like you have never before
```

> 爬过所有沉默的忧虑,像从未有过那样闪耀。
>
> *Climb above all silent worry, then shine like you have never before.*

熵 `2b001019e43fddc0717c0dff2d36540a` · 校验位 `0001`

---

#### 2. 远行 / Departure

```
climb wild mountain cross wide river then float across vast ocean alone
```

> 攀野山,渡宽河,独自漂过浩瀚海洋。
>
> *Climb wild mountains, cross wide rivers, then float across the vast ocean alone.*

熵 `2b1f62421a0fab75b80ac9025e366383` · 校验位 `0111`

---

#### 3. 长者教诲 / The Elder

```
old wise person teach lesson about life that you will never forget
```

> 睿智的长者教诲人生的功课,永志不忘。
>
> *An old wise person teaches a lesson about life that you will never forget.*

熵 `9a1f8e8d6f480600e056ffff3f66542d` · 校验位 `1010`

> **注意 / Note** — 英文主谓不一致(`person teach` 而非 `person teaches`)。因为词表里没有第三人称
> 单数动词的 `-s` 形式(只有名词复数带 `-s`),动词一律只能用原形。

---

#### 4. 跌倒与起身 / Falling and Rising

```
when you fall you cry alone then you stand strong soon again
```

> 跌倒时独自哭泣,很快又坚强地站起来。
>
> *When you fall you cry alone, then you soon stand strong again.*

熵 `fa3fe548ff93520df80ff9e49ae73d02` · 校验位 `0101`

> **注意 / Note** — **这一句英文是别扭的,别当范例。** 理想版本是
> `when you fall you cry alone then you stand strong once again`,但它的校验位对不上
> (熵 `fa3fe548ff93520df80ff9d49ae66a02`,实测校验位 `0100`,而词里带的是 `0101`)。
> 为了让整句通过校验,`once` 被换成了 `soon`,意思因此变成「很快就站起来」。

---

#### 5. 静夜 / Quiet Night

```
calm soft night flame glow slow sweet sleep where you will dream
```

> 静谧柔和的夜,火焰泛着微光,缓慢而甜美的睡眠——你将在其中做梦。
>
> *Calm soft night, flame glows, slow sweet sleep where you will dream.*

熵 `2099ca562c263d9876ee59fa5fe7eca1` · 校验位 `0100`

---

#### 6. 航程 / Voyage

```
silver moon light above calm ocean where dream boat sail home alone
```

> 银色月光落在平静的海面上,梦中的小船独自归航。
>
> *Silver moonlight above the calm ocean, where a dream boat sails home alone.*

熵 `c8d1f20600420931fe921418d7c5b403` · 校验位 `0111`

---

#### 7. 友情 / Friendship

```
good sister that stay near you when other people leave you alone
```

> 别人都离开你的时候,好姐姐仍留在你身边。
>
> *A good sister stays near you when other people leave you alone.*

熵 `6479337fea7939fe7e8ce8a2cfdffc83` · 校验位 `0111`

---

#### 8. 时间 / Time

```
time will teach you lesson that also very old age can tell
```

> 时间会教你一些只有苍老才能讲述的功课。
>
> *Time will teach you a lesson that even very old age can tell.*

熵 `e25f677a7f9807bfc1d7979a009883ef` · 校验位 `0110`

---

### 简体中文 / Chinese Simplified

<!-- lang: zh-Hans -->

> 词表 `chinese_simplified.txt` 里每个「词」就是**一个汉字**,所以 12 词 = 12 个字,写下来就是
> 一句完整的话。校验机制与英文完全相同。

> In the Chinese wordlist every "word" is a **single character**, so 12 words = 12 characters —
> a whole sentence. The checksum mechanics are identical to English.

#### 1. 励志

```
努力向上才能令人生都精彩
```

> 只有「令人生都精彩」这一版能对上校验位;更顺的「让人生更精彩」对不上。

熵 `7f01244d80d2b20ad4e808030164db43` · 校验位 `0001`

#### 2. 进步

```
每天总进步一点点就会成功
```

> 「每天多进步一点点」对不上校验位,只能把「多」换成「总」。

熵 `28e1d0638422d60043006003c08810a7` · 校验位 `0100`

#### 3. 勇气

```
真正勇猛的人敢于面对一切
```

> 原意想写「真正**勇敢**的人…」,但校验位只认「勇猛」。

熵 `28622e785f50000220501c0640800093` · 校验位 `0111`

#### 4. 家庭

```
一家人平静就是最大的幸福
```

> 原想写「一家人**平安**就是最大的幸福」,但校验位对不上;只差第 3 字「安」改成「静」即成立。

熵 `00211c0407c6f0078010b0016002b436` · 校验位 `1100`

#### 5. 友情

```
好朋友是人间最宝贵之礼品
```

> 「人生最宝贵的礼物」对不上;「人间…之礼品」这版成立。

熵 `0cf4b1660020102045848068e106b70c` · 校验位 `1001`

#### 6. 时间

```
时间会证实你的努力有意义
```

> 「时间会证明…」对不上,只差「明」改成「实」。

熵 `0282041112d0ac238003f80920185307` · 校验位 `1010`

#### 7. 追梦

```
有心的人走遍天下都会发光
```

> 原想写「有梦的人…」,校验位只认「有心」。

熵 `00c2300000829701c3a02c0b20881290` · 校验位 `0111`

#### 8. 坚持

```
坚持努力的人定会获得成功
```

> 「终会获得」对不上,「定会获得」成立。

熵 `4be605fc0490000201b8226480f410a7` · 校验位 `0100`

#### 9. 读书

```
学书会让你的世界更加宽广
```

> 「读书会让…」对不上,「学书」这版成立。

熵 `072610112a611c0008d17326815dc016` · 校验位 `1101`

#### 10. 春天

```
春回来了万物生长一片生机
```

> 「春回大地万物复苏生机勃勃」太顺了但校验位对不上,这版是搜索结果里唯一读得通的。

熵 `4de3f40a80528c1500c0d10027500c05` · 校验位 `1101`

#### 11. 识人

```
路远知马力年久才见真人心
```

> 「遥」不在词表,只能用「远」。「路遥知马力,日久见人心」因此少了一字。

熵 `1b28847015d0920997e1591c850c0408` · 校验位 `1100`

---

## 为什么句子读起来别扭 / Why the Sentences Sound Awkward

BIP39 词表不是为写句子设计的,有两条硬性限制:

1. **词长限定 3–8 字符**,共 2048 词,按 4 字符前缀唯一编码 —— 所以 `there` 和 `theme` 不可能同时存在。
2. **刻意剔除了大量高频虚词**。下面这些常见英文词**全部不在词表里**:

   | 不在词表 / Absent | 词表里的替代 / Available instead |
   |---|---|
   | `the` `and` `to` `be` `is` `of` `it` `my` `your` | 没有冠词,只能用 `one` `all` `any` `own` |
   | `with` `up` `down` `far` `as` | `over` `under` `above` `below` `into` `upon` `near` `close` |
   | `not` `no` `but` `so` `or` `if` | `never` `only` `just` `also` `because` `once` `since` `until` |
   | `rise` `fear` `doubt` `silence` `dark` `data` `beat` `burn` | `fall` `worry` `gloom` `silent` `alone` `crash` `error` `glow` |
   | 第三人称单数动词 `-s` | 动词只有原形,只能写 `person teach` |

3. **有画面感的词很少**:`amber` `emerge` `youth` `gospel` `wisdom` 这类只占 2048 格中的极少数。

所以英文能写出来的只能是「动词 + 名词 + 连接词」的**意译式短句**,像诗而不像标准英文。
上面 8 句英文里第 1、2、5、6 句读起来比较自然;第 3、4 句有明确语法瑕疵,已标注。

The wordlist was not designed for prose, so you get telegraphic translated-sounding clauses rather
than natural English. Items 3 and 4 have visible grammatical flaws, flagged above.

### 中文的情况不一样 / Chinese is different

中文词表**没有**上面这些限制,因为每个「词」就是一个汉字:

- 常用虚词全都在:`的` `一` `是` `在` `不` `了` `有` `和` `人` `这` `中` —— 而且它们排在词表最前面。
- 所以能写出**语法完整、读起来自然**的 12 字中文句子,不用像英文那样意译。
- 代价是 2048 个格子里塞了大量单字虚词,组合空间里真正「像句子」的排列占比很低。

但中文也不是 freely 可写:有些字不在 2048 格子里,例如 `己` `懈` `遥` `盎` `暖`。
比如「路遥知马力,日久见人心」里的「遥」就没有,只能改成「远」,句子因此缺一字。

The Chinese wordlist has no such limitations — every "word" is one character, and all the common
function words (`的` `一` `是` `在` `不` `了` `和` `人`) are present, sitting at the very front of the
list. So genuinely grammatical 12-character sentences are possible. The trade-off is that 2048 slots
are heavily padded with single-character function words, and some characters simply are missing
(`己` `懈` `遥` `盎`).

---

## 这些熵不是随机的 / Where the Entropy Came From

**诚实说明 / Honest disclosure:**

- 词是人挑的,脚本只负责**查词是否在词表内**和**比对 4 个校验位**,没有参与造句。
- 熵是从词序**反推**得到的。这 19 句只覆盖各自词表的 2048¹² 个组合中的 19 个,**不具备密码学随机性**。
- 手挑 12 个词天然带上正确校验位的概率只有 **1/16**。多数句子是靠同义词替换
  (例如英文 `doubt` → `worry`、`peak` → `mountain`;中文 `勇敢` → `勇猛`、`明` → `实`)反复试出来的,
  所以它们的措辞是被校验位「挑」过的,而不是先有完美句子再对上。
- 中文句子里这一点尤其明显:几乎每句都有一处「本该更顺、但校验位对不上」的痕迹,已在各条下方注明。
- 想要**密码学随机**的助记词,应该用 `secrets` / `os.urandom` 生成熵再套 BIP39,
  不要从词库里挑词。

The words were chosen by hand; a script only checked membership and the 4 checksum bits. The entropy
is derived from the word order, not random. A hand-picked 12-word set has only a 1/16 chance of
carrying a correct checksum, so several of these were found by trying synonyms until one fit.

---

## 相关链接 / References

- BIP-39 规范 / Specification: <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>
- 英文词表 / English wordlist: <https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt>
- 简体词表 / Simplified Chinese: <https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt>
- 繁体词表 / Traditional Chinese: <https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt>
- 官方测试向量 / Trezor test vectors: <https://github.com/trezor/python-mnemonic/blob/master/vectors.json>
  (注意:已不在 `bitcoin/bips` 仓库里,`bip-0039/vectors.json` 会返回 404 /
  note: no longer in `bitcoin/bips` — `bip-0039/vectors.json` returns 404)

⚠️ 本文件中的助记词不要用于真实资产。
⚠️ Never use anything in this file for real funds.
