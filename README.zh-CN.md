# awesome-bip39

**有语义的 BIP39 助记词** —— 共 35 句。每一句都读得通,而且**通过完整校验**:12 个词全部来自官方
BIP39 词表,词索引里内嵌的 4 bit SHA-256 校验位与熵一致。任何标准 BIP39 实现都能正常导入。

本列表同时覆盖两套适合这件事的官方词表:

| 词表 | 词数 | 每「词」字数 | 所以 12 词 = |
|---|---|---|---|
| `chinese_simplified.txt` | 2048 | **1 个汉字** | **12 个汉字** |
| `english.txt` | 2048 | 3–8 字母 | 12 个英文单词 |

> **[The English version](README.md)**(`README.md`)

`chinese_traditional.txt` 形态相同(2048 个单字),但本仓库暂未收录繁体助记词。

---

## ⚠️ 安全警告

本文件里的所有助记词都已公开,任何人都能读到。它们仅供学习、测试、演示 BIP39 词表与校验机制之用。
**绝对不要**用它们创建或恢复任何持有真实资产的钱包。

---

## 快速验证

```bash
python3 verify.py                 # 校验全部 70 处(35 句,每句在两个文件里各出现一次)
python3 verify.py --seed          # 顺便输出 BIP39 种子 (PBKDF2-HMAC-SHA512, 2048 轮)
python3 verify.py --lang zh-Hans -m "努力向上才能令人生都精彩"   # 校验任意一条(简体)
python3 verify.py -m "your twelve words here …"                   # 校验任意一条(英文)
python3 selftest.py               # 用官方 Trezor 测试向量回归 verify.py 本身
```

`verify.py` 只依赖标准库。它会在缺失时自动下载官方词表,用 SHA-256 确认词表是原版,然后逐条检查
「词是否在词表内」和「校验位是否正确」。**全部通过时退出码为 0**,可用于 CI。它会扫描本目录下所有
`README*.md`,并按 `lang: en` / `lang: zh-Hans` 标记为每条助记词选择对应词表,因此两种语言各自
用各自的词表校验。

`selftest.py` 拿官方 24 条测试向量(含 12/18/24 词三种长度)回归验证 `verify.py` 的 checksum、
entropy 反推、seed 推导三项。

## 文件

| 文件 | 说明 |
|---|---|
| `README.md` | The English version, same content as this file |
| `README.zh-CN.md` | 本文件,中文版 |
| `verify.py` | 校验工具(多语言) |
| `selftest.py` | 官方向量回归测试 |
| `chinese_simplified.txt` | 简体词表 |
| `chinese_traditional.txt` | 繁体词表 |
| `english.txt` | 自动下载的词表,经 SHA-256 校验 |
| `vectors.json` | 自动下载的官方向量 |

---

## 词表来源

| | |
|---|---|
| 文件 | [`chinese_simplified.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt) · [`chinese_traditional.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt) · [`english.txt`](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) |
| 仓库 | `github.com/bitcoin/bips`,目录 `bip-0039/` |
| 词数 | 每个词表 2048 |
| SHA-256 | `chinese_simplified.txt` `5c594279…7c5726`<br>`chinese_traditional.txt` `417b26b3…c1b5f`<br>`english.txt` `2f5eed53…b24dbda` |

---

## 助记词

### 第一部分 —— 英文(19 句)

<!-- lang: en -->

#### 1. 励志 / Motivational

```
climb above all silent worry then shine like you have never before
```

> 爬过所有沉默的忧虑,像从未有过那样闪耀。

熵 `2b001019e43fddc0717c0dff2d36540a` · 校验位 `0001`

#### 2. 远行 / Departure

```
climb wild mountain cross wide river then float across vast ocean alone
```

> 攀野山,渡宽河,独自漂过浩瀚海洋。

熵 `2b1f62421a0fab75b80ac9025e366383` · 校验位 `0111`

#### 3. 长者教诲 / The Elder

```
old wise person teach lesson about life that you will never forget
```

> 睿智的长者教诲人生的功课,永志不忘。

熵 `9a1f8e8d6f480600e056ffff3f66542d` · 校验位 `1010`

> **注意** —— 英文主谓不一致(`person teach` 而非 `person teaches`)。因为词表里没有第三人称单数
> 动词的 `-s` 形式(只有名词复数带 `-s`),动词一律只能用原形。

#### 4. 跌倒与起身 / Falling and Rising

```
when you fall you cry alone then you stand strong soon again
```

> 跌倒时独自哭泣,很快又坚强地站起来。

熵 `fa3fe548ff93520df80ff9e49ae73d02` · 校验位 `0101`

> **注意** —— **这一句英文是别扭的,别当范例。** 理想版本是
> `when you fall you cry alone then you stand strong once again`,但它的校验位对不上
> (熵 `fa3fe548ff93520df80ff9e49ae66a02`,实测校验位 `0100`,而词里带的是 `0101`)。
> 为了让整句通过校验,`once` 被换成了 `soon`,意思因此变成「很快就站起来」。

#### 5. 静夜 / Quiet Night

```
calm soft night flame glow slow sweet sleep where you will dream
```

> 静谧柔和的夜,火焰泛着微光,缓慢而甜美的睡眠——你将在其中做梦。

熵 `2099ca562c263d9876ee59fa5fe7eca1` · 校验位 `0100`

#### 6. 航程 / Voyage

```
silver moon light above calm ocean where dream boat sail home alone
```

> 银色月光落在平静的海面上,梦中的小船独自归航。

熵 `c8d1f20600420931fe921418d7c5b403` · 校验位 `0111`

#### 7. 友情 / Friendship

```
good sister that stay near you when other people leave you alone
```

> 别人都离开你的时候,好姐姐仍留在你身边。

熵 `6479337fea7939fe7e8ce8a2cfdffc83` · 校验位 `0111`

#### 8. 时间 / Time

```
time will teach you lesson that also very old age can tell
```

> 时间会教你一些只有苍老才能讲述的功课。

熵 `e25f677a7f9807bfc1d7979a009883ef` · 校验位 `0110`

#### 9. 坚持

```
hard work can turn you brave when you never say you quit
```

> 只要你从不说放弃,努力就能让你变得勇敢。

熵 `693fb083f56ff236be8ff99517fffcd7` · 校验位 `1110`

#### 10. 耐心

```
one small water drop over long year must wear away old stone
```

> 一年的功夫,再小的一滴水也能滴穿老石。

熵 `9ab98fdf21b9df07bfbc90f8620e686b` · 校验位 `0010`

#### 11. 善意

```
one kind word can turn one more angry heart into warm smile
```

> 一句善意的话,能把另一颗愤怒的心变成温暖的微笑。

熵 `9aaf53f5907ead3563f0476a4ebbdce6` · 校验位 `0101`

#### 12. 智慧

```
one old man can tell young boy story that you never forget
```

> 一位老人能讲一个让男孩永远忘不掉的故事。

熵 `9ab3421b107dedfe86aeb4dfffe6542d` · 校验位 `1010`

#### 13. 希望

```
one long night will become short when you have one good dream
```

> 只要有一个好梦,再长的夜也会变短。

熵 `9ab07a567d913f8dbe8ff969b35591a1` · 校验位 `0100`

#### 14. 忠诚

```
one true friend will stay near you until nothing else can stay
```

> 一个真朋友会留在你身边,直到别的一切都留不住。

熵 `9abd2973fd9d4f273fcfd7196c90483ea` · 校验位 `0111`

#### 15. 温暖

```
one warm smile can make one very sad young face bright again
```

> 一个温暖的微笑,能让一张悲伤的年轻面孔重新明亮起来。

熵 `9abee732907869357cbdedff4a307002` · 校验位 `0101`

#### 16. 沉静

```
one calm heart will wait long time until one warm autumn day
```

> 一颗沉静的心,会一直等到某个温暖的秋日。

熵 `9aa411a97d9f6707b897719abee43e9c` · 校验位 `0000`

#### 17. 成长

```
one long road can make you strong also kind also very wise
```

> 一段长路,能让你强壮,也能让你善良、让你睿智。

熵 `9ab07aeb907869fe75c83a7a80ebcbfe` · 校验位 `0011`

> **Note** —— 英文词表里没有 `and` 也没有 `to`,所以三个形容词只能靠重复 `also` 串起来。早期草稿
> 结尾是 `... also very brave old`,校验能过但读起来别扭,最后换成 `wise` 才把句子保住。

#### 18. 学习

```
young mind can learn much more when you hold one great book
```

> 手里捧着一本好书,年轻的心能学到更多。

熵 `ff519c83bf69111fbe8ff96c9355988c` · 校验位 `1100`

#### 19. 清晨

```
morning light come over green hill then one young girl will sing
```

> 晨光越过绿色山丘,于是有一个年轻姑娘开始歌唱。

熵 `8ff030b84ef664d7780cd5ff4c4bece4` · 校验位 `1010`

### 第二部分 —— 简体中文(16 句)

<!-- lang: zh-Hans -->

> `chinese_simplified.txt` 里每个「词」就是**一个汉字**,所以 12 词就是 12 个字,写下来是一句完整
> 的话。校验机制与英文完全相同。

#### 1. 励志

```
努力向上才能令人生都精彩
```

> 努力向上,才能令人生都精彩。

熵 `7f01244d80d2b20ad4e808030164db43` · 校验位 `0001`

> **注意** —— 只有「令人生都精彩」这一版能对上校验位;更顺的「让人生更精彩」对不上。

#### 2. 进步

```
每天总进步一点点就会成功
```

> 每天总进步一点点,就会成功。

熵 `28e1d0638422d60043006003c08810a7` · 校验位 `0100`

> **注意** —— 「每天多进步一点点」对不上校验位,只能把「多」换成「总」。

#### 3. 勇气

```
真正勇猛的人敢于面对一切
```

> 真正勇猛的人,敢于面对一切。

熵 `28622e785f50000220501c0640800093` · 校验位 `0111`

> **注意** —— 原意想写「真正**勇敢**的人…」,但校验位只认「勇猛」。

#### 4. 家庭

```
一家人平静就是最大的幸福
```

> 一家人平静,就是最大的幸福。

熵 `00211c0407c6f0078010b0016002b436` · 校验位 `1100`

> **注意** —— 原想写「一家人**平安**就是最大的幸福」,但对不上;只差第 3 字「安」改成「静」
> 才成立。

#### 5. 友情

```
好朋友是人间最宝贵之礼品
```

> 好朋友是人间最宝贵之礼品。

熵 `0cf4b1660020102045848068e106b70c` · 校验位 `1001`

> **注意** —— 「人生最宝贵的礼物」对不上;「人间…之礼品」这版成立。

#### 6. 时间

```
时间会证实你的努力有意义
```

> 时间会证实,你的努力有意义。

熵 `0282041112d0ac238003f80920185307` · 校验位 `1010`

> **注意** —— 「时间会证明…」对不上,只差「明」改成「实」。

#### 7. 追梦

```
有心的人走遍天下都会发光
```

> 有心的人,走遍天下都会发光。

熵 `00c2300000829701c3a02c0b20881290` · 校验位 `0111`

> **注意** —— 原想写「有梦的人…」,校验位只认「有心」。

#### 8. 坚持

```
坚持努力的人定会获得成功
```

> 坚持努力的人,定会获得成功。

熵 `4be605fc0490000201b8226480f410a7` · 校验位 `0100`

> **注意** —— 「终会获得」对不上,「定会获得」成立。

#### 9. 读书

```
学书会让你的世界更加宽广
```

> 学书会让你的世界更加宽广。

熵 `072610112a611c0008d17326815dc016` · 校验位 `1101`

> **注意** —— 「读书会让…」对不上,「学书」这版成立。

#### 10. 春天

```
春回来了万物生长一片生机
```

> 春回来了,万物生长,一片生机。

熵 `4de3f40a80528c1500c0d10027500c05` · 校验位 `1101`

> **注意** —— 「春回大地万物复苏生机勃勃」太顺了但校验位对不上,这版是搜索结果里唯一读得通的。

#### 11. 识人

```
路远知马力年久才见真人心
```

> 路远知马力,年久才见真人心。

熵 `1b28847015d0920997e1591c850c0408` · 校验位 `1100`

> **注意** —— 「遥」不在词表,只能用「远」。「路遥知马力,日久见人心」因此少了一字。

#### 12. 善良

```
善良的人福气总是不会太坏
```

> 善良的人,福气总不会太坏。

熵 `65aaa4000086d826463802008088da28` · 校验位 `0101`

#### 13. 付出

```
所有的努力付出必将有回报
```

> 所有的努力与付出,必将有回报。

熵 `076018003f80932380e8fa1c40187e95` · 校验位 `0000`

#### 14. 强大

```
真正的强大是内心更加安定
```

> 真正的强大,是内心更加安定。

熵 `28622c000f30160084488c26815c9f03` · 校验位 `0111`

#### 15. 信念

```
心里有光的人的确从不迷路
```

> 心里有光的人,的确从不迷路。

熵 `11812803107000020001580c2013148d` · 校验位 `1001`

#### 16. 陪伴

```
陪伴都是最长情的告白礼物
```

> 陪伴,是最长情的告白礼物。

熵 `eab8842c8021603445700042a4e6b705` · 校验位 `0100`

> **注意** —— 这里用「都是」而不是更顺的「就是」,因为「就是」校验不过。结尾的「礼物」也不是随手
> 加的:「陪伴是最长情的告白」只有 11 个字,比 BIP39 中文助记词要求的 12 个字少一个。

---

## 为什么英文句子读起来别扭

BIP39 词表不是为写句子设计的,有三条硬性限制:

1. **词长限定 3–8 字符**,共 2048 词,按 4 字符前缀唯一编码 —— 所以 `there` 和 `theme` 不可能
   同时存在。
2. **刻意剔除了大量高频虚词**。下面这些常见英文词**全部不在词表里**:

   | 不在词表 | 词表里的替代 |
   |---|---|
   | `the` `and` `to` `be` `is` `of` `it` `my` `your` | 没有冠词,只能用 `one` `all` `any` `own` |
   | `with` `up` `down` `far` `as` | `over` `under` `above` `below` `into` `upon` `near` `close` |
   | `not` `no` `but` `so` `or` `if` | `never` `only` `just` `also` `because` `once` `since` `until` |
   | `rise` `fear` `doubt` `silence` `dark` `data` `beat` `burn` | `fall` `worry` `gloom` `silent` `alone` `crash` `error` `glow` |
   | 第三人称单数动词 `-s` | 动词只有原形,只能写 `person teach` |

3. **有画面感的词很少**:`amber` `emerge` `youth` `gospel` `wisdom` 这类只占 2048 格中的极少数。

所以英文能写出来的只能是「动词 + 名词 + 连接词」的**意译式短句**,像诗而不像标准英文。
第 1、2、5、6 句和第 7–19 句大多读起来自然;第 3、4、17 句有明确语法瑕疵,已在各条下方标注。

## 为什么中文好写多了

中文词表**没有**上面这些限制,因为每个「词」就是一个汉字:

- 常用虚词全都在 —— `的` `一` `是` `在` `不` `了` `有` `和` `人` `这` `中` —— 而且它们排在词表
  最前面。
- 所以能写出**语法完整、读起来自然**的 12 字中文句子,不用像英文那样意译。
- 代价是 2048 个格子里塞了大量单字虚词,组合空间里真正「像句子」的排列占比很低。

但中文也不是 freely 可写:有些字不在 2048 格子里,例如 `己` `懈` `遥` `盎` `暖`。
这正是「路遥知马力,日久见人心」里的「遥」只能改成「远」、句子因此少一字的原因。

---

## 这些熵不是随机的

**诚实说明:**

- 词是人挑的,脚本只负责**查词是否在词表内**和**比对 4 个校验位**,没有参与造句。
- 熵是从词序**反推**得到的。这 35 句只覆盖各自词表的 2048¹² 个组合中的 35 个,**不具备密码学
  随机性**。
- 手挑 12 个词天然带上正确校验位的概率只有 **1/16**。多数句子是靠同义词替换反复试出来的 ——
  `doubt` → `worry`、`peak` → `mountain`、`once` → `soon`,中文则如 `勇敢` → `勇猛`、`明` → `实`、
  `安` → `静`。所以它们的措辞是被校验位「挑」过的,而不是先有完美句子再对上。
- 中文句子里这一点尤其明显:几乎每句都留着一处「本该更顺、但校验位对不上」的痕迹,已在各条
  下方注明。
- 想要**密码学随机**的助记词,应该用 `secrets` / `os.urandom` 生成熵再套 BIP39,不要从词库里挑词。

---

## 相关链接

- 本仓库:<https://github.com/lizzzhh/awesome-bip39>
- **[The English version](README.md)**(`README.md`)
- BIP-39 规范:<https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>
- 简体词表:<https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt>
- 繁体词表:<https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt>
- 英文词表:<https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt>
- 官方 Trezor 测试向量:<https://github.com/trezor/python-mnemonic/blob/master/vectors.json>
  (注意:已不在 `bitcoin/bips` 仓库里,`bip-0039/vectors.json` 会返回 404)

⚠️ 本文件中的助记词不要用于真实资产。
