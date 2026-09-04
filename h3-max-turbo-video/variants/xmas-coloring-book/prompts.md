# Japan Coloring Book for Kids ― Holiday Sale 30% OFF（AI生成版プロンプト・実際の表紙を使う版）

元動画（H3 Max Turbo 告知）の **12カット構成・14.4秒・ペーパークラフト様式** をそのまま使い、
Amazon KDP で販売中の **Takeda Studio「Japan ○○ Coloring Book for Kids」シリーズ** の
クリスマスセール告知に差し替えたプロンプト一式です。画面に出る文字は **すべて英語** で、
**実際の本の表紙を参照画像として動画に登場させます。**

## シリーズの表紙から読み取った「ブランドのルール」

| 要素 | 表紙の実物 | 動画での扱い |
|---|---|---|
| タイトル | 赤い丸ゴシック「Japan」＋ 紺の太字「Tokyo / Kyoto / Food …」＋ 虹色「Coloring Book for Kids」 | エンドカードのロゴをこの3段組で再現 |
| リボン | 黄色いリボンに "Color My ○○ Memories" | CTAカードの黄色地に流用 |
| 3つの丸バッジ | 赤 "Ages 5-10"、紺 "30 Scenes"、緑 "Memory Prompts Inside" | カット5の小タグに緑バッジ、カット3のカードに "Ages 5–10" |
| タグライン | "Color it. Remember it. Keep it forever." | カット5「COLOR IT → REMEMBER IT」、エンドカードで全文 |
| 主人公 | 赤いニット帽・黄シャツ・緑オーバーオールの男の子（白うさぎを抱く）、ピンクのパーカーでツインテールの女の子 | 紙人形の主人公をこの2人にする（エルフ帽案は廃止） |
| 背景色 | クリーム地、桜の花びら、赤い鳥居 | 雪の紙 ＋ 桜の花びらと雪片を混ぜて舞わせる |

```
 元動画                        →  Japan Coloring Book 版
 ─────────────────────────────────────────────────────────
 クラフト紙（ベージュ）          →  クリーム色の紙 ＋ 桜の花びらと雪片
 コーラル / ブルー / ティール    →  表紙の赤 / 紺 / 黄 ＋ クリスマスの緑
 会社員の女性                    →  表紙の男の子（赤ニット帽・白うさぎ）＋ 女の子（ピンクのパーカー）
 AI UPDATE のメモ               →  「XMAS SALE」のギフトタグ
 スタンプ → 朗報！              →  金の星スタンプ → HOLIDAY SALE!
 H3 Max Turbo登場               →  JAPAN COLORING BOOK for Kids ＋ 実物の表紙6冊が扇状に広がる
 ストップウォッチ：速度2倍       →  大きなクレヨン：COLOR IT → REMEMBER IT（緑バッジ MEMORY PROMPTS INSIDE）
 ハサミ：コスト半分             →  ハサミで値札を切る：30% OFF
 2枚のフレーム：品質ほぼそのまま →  Kyoto と Tokyo の表紙2冊を掲げる：THE PERFECT GIFT
 くしゃくしゃ → ゴミ箱          →  本を重ねてギフト箱に → ツリーの下へ
 期間限定プロモーション         →  HOLIDAY SALE ON NOW / Get it on Amazon
 H3 MAX TURBO ロゴ              →  Japan / Coloring Book for Kids / by Takeda Studio / タグライン / Available on Amazon
```

---

## 0. 画面に出る英語テキスト一覧（先に確認）

| # | カット | 画面の文字 | 備考 |
|---|---|---|---|
| 1 | ギフトタグ | `XMAS SALE` | |
| 2 | 爆発吹き出し | `HOLIDAY SALE!` | |
| 3 | 登場カード | `JAPAN COLORING BOOK` ＋ 小さく `for Kids · Ages 5–10 · 6 Titles` | |
| 3 | 扇状の本 | 実物の表紙6冊（文字は表紙のまま） | 参照画像を渡す |
| 5 | 売り文句1 | `COLOR IT` → `REMEMBER IT` ＋ 緑バッジ `MEMORY PROMPTS INSIDE` | 表紙のタグラインと同じ言葉 |
| 7 | 値札タグ | `30% OFF` | |
| 7 | 期間カード | `Until Dec 25` | **仮置き。実際のセール期間に差し替え** |
| 8 | 売り文句3 | `THE PERFECT GIFT` | Kyoto と Tokyo の表紙を掲げる |
| 10 | CTAカード | `HOLIDAY SALE ON NOW` / `Get it on Amazon` | |
| 12 | エンドカード | `Japan` / `Coloring Book for Kids` / `by Takeda Studio` / `Color it. Remember it. Keep it forever.` / `Available on Amazon` ＋ 小タグ `30% OFF` | |

> **Amazon の表記について**：文字で "Available on Amazon" / "Get it on Amazon" と書くのは一般的な表現ですが、
> Amazon のロゴ（矢印のマーク）や "a" のアイコンは商標のため、動画内に描かせないでください。
> プロンプトにも「ロゴは使わず文字のみ」と明記してあります。

> **30% OFF の表記について**：KDP のペーパーバックはクーポン機能がないため、割引は期間中に
> 定価（List Price）を下げることで実現します。Kindle 版は KDP Select 登録なら Countdown Deal が使えます。
> 実際に値下げしていない期間に「30% OFF」の動画を流すと景品表示法・Amazon規約の両方に触れるので、
> 値下げ期間と動画の掲載期間を必ず合わせてください。

---

## 1. 表紙画像（参照画像）の準備

`covers/` フォルダに、いただいた PDF から切り出した表紙が入っています。

| ファイル | 中身 |
|---|---|
| `covers/tokyo-front.jpg` | Japan Tokyo Coloring Book for Kids（表1） |
| `covers/festivals-matsuri-front.jpg` | Japan Festivals & Matsuri Coloring Book for Kids（表1） |
| `covers/tokyo-wrap.jpg` / `covers/festivals-matsuri-wrap.jpg` | 裏表紙込みの全体 |

**残り4冊（Animals & Nature、Food、Kyoto、Sumo）は画像として貼っていただいただけなので、ファイルとしては
まだありません。** 生成するときは、その4冊の表紙も JPG か PDF で用意し、同じ `covers/` に入れてください。
6冊そろわない場合は、手元にある冊数だけ扇状に並べる指示に変えて構いません（プロンプトの "six" を冊数に直す）。

生成モデルへの渡し方：
- Seedance 2.x / Kling 3.0 / Higgsfield：参照画像（image reference）として表紙を添付し、プロンプトに
  「the real book covers provided as reference images, reproduced faithfully」と書いてあります。
- 表紙の文字は AI が崩しやすいので、生成後に必ず拡大して確認し、崩れていたら **そのカットだけ** 作り直します。
- どうしても表紙の文字が崩れる場合は、動画編集ソフトで表紙画像を上から貼る（合成する）のが確実です。
  カット3・8・12 は表紙が正面を向いて止まる時間があるので、合成しやすい設計にしてあります。

---

## 2. スタイル定義（すべてのプロンプトの先頭に付ける）

```
STYLE: Handcrafted paper-cutout stop-motion animation, 3D-rendered papercraft look, a Christmas
craft-corner mood that matches the look of the "Japan ... Coloring Book for Kids" series by
Takeda Studio. Every object is a flat piece of 1-2mm thick card stock with visible white paper
edges and a soft, short drop shadow. Background is a fixed sheet of cream textured paper (#FFF6D6)
with fine fiber grain, a gentle vignette, and a few small paper snowflakes and pink paper cherry
petals that drift down slowly through the whole video. Fixed camera, straight-on, slight top-down
tilt; only the paper objects move.
Palette taken from the book covers: title red #E03A2E, navy #1F3A8A, ribbon yellow #F6D33C,
sakura pink #F5A3B8, leaf green #4C9A3C, plus Christmas pine green #2F7A5A and gold #E9B94B.
Characters are the two kids from the covers, made as paper dolls with round paper pins at
shoulders, elbows and knees: a boy about six with a red knit beanie with a pom-pom, a yellow
t-shirt, green overalls and red sneakers, holding a small white paper bunny; and a girl about
seven with wavy orange-blonde pigtails, a pink hoodie and purple leggings. The boy stays on the
right side of the frame and interacts with every prop (catches, colors, cuts, stacks, raises
arms); the girl joins him only in the final CTA shot.
THE BOOKS: whenever a book appears, it is one of the real covers provided as reference images
(Japan Tokyo / Japan Kyoto / Japan Food / Japan Festivals & Matsuri / Japan Animals & Nature /
Sumo — all "Coloring Book for Kids"), reproduced faithfully as flat paper rectangles with a
white paper edge, portrait orientation, 4:5 proportion; do not invent new cover art or change
their text.
ALL ON-SCREEN TEXT IS IN ENGLISH, spelled exactly as written in the shot list. Headlines are heavy
rounded sans-serif capitals (like Nunito Black / Fredoka), cut from paper with thickness and
shadow, in navy or red; the word "Japan" in the end card is red rounded type like the covers, and
"Coloring Book for Kids" is set in rainbow letters like the covers. Text pops in with a bouncy
overshoot (scale 0 → 1.1 → 1.0) or unfolds like an accordion. Never draw the Amazon logo or smile
icon; "Amazon" appears as plain text only. No hard cuts: every transition is a paper gesture
(ribbon wipe, folding screen, stack into a gift box, page fold).
Aspect ratio 16:9 (1280x720), 24fps, 14.4 seconds. No narration; bright, playful sleigh-bell BGM
with paper foley (rustle, stamp, crayon scribble, snip, fold) on each beat.
```

---

## 3. フルプロンプト（14.4秒・1本用）

### SHOT-BY-SHOT EFFECTS TIMELINE

```
SHOT 1 (00:00.0–00:00.85) — Gift Tag Drop
• EFFECT: Object drop-in (gravity settle) + drifting petals and snowflakes + character slide-in
• A kraft-brown paper gift tag with a red string, reading "XMAS SALE" in navy capitals, flutters
  down from the top-left, rocks once and settles tilted approx -12°. Three small white paper
  snowflakes and two pink petals drift down behind it. The boy in the red beanie jogs in from the
  right edge with a bobbing walk, the white bunny tucked under one arm.
• Camera fixed, straight-on. Empty cream paper background.
• Tag lands at 0.4s; boy reaches center-right at 0.85s.
• Exits by the tag being covered by the star stamp in SHOT 2.

SHOT 2 (00:00.85–00:01.45) — Gold Star Stamp and Burst
• EFFECT: Impact slam (scale 1.6 → 1.0 with squash) + starburst reveal + paper confetti
• A gold paper star-shaped stamp slams down from above onto the tag. On impact a large red
  starburst speech bubble (sawtooth edge, 16 points, white paper edge) pops out behind it and the
  tag is replaced by the burst reading "HOLIDAY SALE!" in white heavy rounded capitals on red.
• Small red, green, gold and pink paper flecks fly outward and fall; the boy does a small jump
  and the bunny's ears flop.
• Slam lands at 1.0s; burst fully visible at 1.2s; hold to 1.45s.
• Exits by the burst flipping down and folding into a strip for SHOT 3.

SHOT 3 (00:01.45–00:02.95) — Series Title and the Six Real Covers Fan Out
• EFFECT: Accordion unfold (paper pleats opening) + fan stack (staggered rotation)
• A pleated strip of paper held by the boy unfolds left-to-right into a wide cream card: big line
  "JAPAN COLORING BOOK" in heavy navy rounded capitals with "JAPAN" in red, small line under it
  "for Kids · Ages 5–10 · 6 Titles" in navy.
• Behind and beside the card, the six real books slide out and fan into a stack like a hand of
  cards, each rotated 3-4° more than the last, front covers facing the camera and fully readable:
  Japan Tokyo, Japan Kyoto, Japan Food, Japan Festivals & Matsuri, Japan Animals & Nature, Sumo
  — exactly as in the reference images. The Tokyo cover ends on top.
• The boy pushes the stack with both hands, leaning into it; the covers hold still and readable
  for the last 0.5s of the shot.
• Unfold 1.45–1.85s; fan-out 1.85–2.3s; hold with a slight breathing wobble to 2.95s.
• Exits via the candy-cane ribbon wipe in SHOT 4.

SHOT 4 (00:02.95–00:03.30) — Candy-Cane Ribbon Wipe
• EFFECT: Wipe transition (paper ribbon) — 0.35 seconds
• The boy grabs the end of a wide paper ribbon striped red and white like a candy cane and pulls
  it across the whole frame from right to left; the ribbon covers the books and reveals an empty
  background.
• Motion blur on the ribbon, slight curl at its leading edge.

SHOT 5 (00:03.30–00:04.60) — Crayon: Color It, Remember It
• EFFECT: Prop entrance + crayon scribble fill + staggered text pop + badge pop
• A large paper line-art torii gate (like the one on the back covers) stands at center-left in
  navy outline. A giant red paper crayon rolls in from the left; the boy catches it and scribbles
  across the torii: it fills with red in three diagonal strokes, the top beam stays black.
• "COLOR IT" pops in above-left (scale overshoot), then "REMEMBER IT" pops in below it, larger,
  0.25s later. A round green paper badge reading "MEMORY PROMPTS INSIDE" in white capitals — the
  same badge as on the covers — pops in at the lower left with a bounce.
• Crayon enters 3.3–3.6s; scribble 3.6–4.1s; "COLOR IT" at 3.75s; "REMEMBER IT" at 4.0s; badge 4.2s.
• Exits by the torii and crayon sliding right off-frame while the red price sheet enters from the left.

SHOT 6 (00:04.60–00:05.65) — Scissors Cut the Price
• EFFECT: Prop entrance + path-following cut + piece separation
• A large red rectangle of paper (a price tag before it is shaped) slides in from the left with a
  dotted cut line across its middle and a faint crossed-out price on the lower half. Oversized
  grey paper scissors held by the boy open and close 4 times, moving right-to-left along the
  dotted line.
• The cut edge shows a zig-zag paper tear. This is the SIGNATURE VISUAL EFFECT of the middle
  section: literally cutting the price.
• Scissors start 4.9s, finish cut 5.55s.

SHOT 7 (00:05.65–00:06.75) — 30% OFF Tag
• EFFECT: Piece drop + shape morph + secondary card pop + character kick
• The lower half of the red paper falls away and tumbles; the remaining half snaps into a classic
  price-tag shape (pointed top with a hole and a gold string) reading "30% OFF" in white heavy
  rounded type, "30%" very large.
• A small white card pops in at the upper right reading "Until Dec 25" with a tiny paper holly leaf.
• The boy kicks the fallen scrap, which slides off-frame.
• Tag forms 5.65–5.9s; card pops 5.9s; kick 6.3–6.7s.
• Exits by the tag flipping backward and folding into the two books of SHOT 8.

SHOT 8 (00:06.75–00:08.85) — The Perfect Gift
• EFFECT: Folding-screen unfold (rotate on vertical hinge) + typewriter text + subtle wobble
• Two real books unfold like a folding screen, side by side, front covers to camera and fully
  readable: left, "Japan Kyoto Coloring Book for Kids"; right, "Japan Tokyo Coloring Book for
  Kids" — exactly as in the reference images, each a flat paper rectangle with a white edge and
  a soft shadow. A red paper ribbon bow sits on the top corner of the right book.
• The boy steadies the right book with one hand. The right book rocks gently (approx 3°).
• "THE PERFECT GIFT" types in below in heavy navy capitals, one letter every ~60ms, from 7.35s.
• Books open 6.75–7.3s; text 7.35–7.95s; hold, covers readable, to 8.85s.
• Exits as the boy grabs both books and stacks them.

SHOT 9 (00:08.85–00:10.20) — Stack into a Gift, Slide Under the Tree
• EFFECT: Stack morph (books stack and wrap into a box) + slide + settle wobble
• The two books stack in the boy's hands, red paper wraps around them and a gold paper bow pops
  on top: a small red gift box. A green paper Christmas tree with a gold star on top appears at
  the lower right, decorated with tiny pink paper petals.
• The box slides right along the floor, bumps once, and settles under the tree; the tree wobbles
  and the star spins half a turn. The boy steps out of frame to the right.
• Stack and wrap 8.85–9.1s; slide 9.3–10.0s; tree wobble 10.0–10.2s.
• Exits via the box lid popping open in SHOT 10.

SHOT 10 (00:10.20–00:12.10) — Sale CTA Card
• EFFECT: Unfold reveal + two-character pop-up + ribbon swirl (path draw)
• The gift box lid pops open and a sheet of ribbon-yellow paper (the same yellow as the cover
  ribbons) unfolds out of it and flattens into a rounded CTA card: small line "HOLIDAY SALE ON NOW"
  in red with a navy underline, big line "Get it on Amazon" in navy with a red underline (plain
  text, no Amazon logo). A red paper cup holding three crayons (red, green, blue) sits at the
  right of the card.
• The boy and the girl in the pink hoodie pop up from behind the card together, both with arms
  raised, with a small hop; the bunny pops up between them.
• A red ribbon curls around from the left and a green ribbon from the right, drawing themselves
  along their paths and settling with a slight sway. Petals and snowflakes drift past.
• Unfold 10.2–10.55s; kids pop 10.6s; ribbons 10.9–11.6s; hold to 12.1s.
• Exits by the page fold in SHOT 11.

SHOT 11 (00:12.10–00:12.40) — Page Fold Transition
• EFFECT: Fold transition (page turns over its vertical center) — 0.3 seconds
• The whole scene is a sheet of paper that folds over from the center, back-side showing plain
  cream paper, wiping everything away and revealing the end card.

SHOT 12 (00:12.40–00:14.40) — Series End Card
• EFFECT: Static hold (no effects)
• Plain cream paper background. Centered, slightly above the vertical middle, a paper lockup in
  the exact style of the book covers: "Japan" in big red rounded letters with a white outline,
  "Coloring Book for Kids" under it in rainbow-colored rounded letters, and below that a small
  yellow paper ribbon reading "Color it. Remember it. Keep it forever." in navy. Under the ribbon,
  "by Takeda Studio" in small navy capitals and a white paper strip "Available on Amazon" (plain
  text). A small red "30% OFF" paper tag hangs from the letter "n" of "Japan". To the right, the
  six real covers stand in a short neat row, small, tilted 5°, like books on a shelf. Two pink
  petals and one snowflake rest on the paper. Nothing moves for 2 seconds.
• Audio drops to silence at 13.0s.
```

### MASTER EFFECTS INVENTORY

```
1. Object drop-in / gravity settle — used 2x (Shots 1, 7) — gift tag and price scrap land and rock.
2. Drifting petals and snowflakes — used 4x (Shots 1, 9, 10, 12) — ambient motion, always slow.
3. Impact slam with squash — used 1x (Shot 2) — the gold star stamp; loudest beat of the opening.
4. Starburst reveal — used 1x (Shot 2) — the red "HOLIDAY SALE!" bubble.
5. Paper confetti / flecks — used 2x (Shots 2, 6) — red/green/gold/pink pieces scatter on impact and cut.
6. Accordion unfold — used 2x (Shots 3, 10) — pleated paper opens into a flat card.
7. Fan stack of real covers (staggered rotation) — used 1x (Shot 3) — the six books spread like a hand of cards.
8. Ribbon wipe — used 1x (Shot 4) — candy-cane striped ribbon transition.
9. Crayon scribble fill — used 1x (Shot 5) — the torii fills with red in three strokes.
10. Bouncy text / badge pop (scale overshoot) — used 6x (Shots 2, 5, 7, 10) — every headline and the badge.
11. Path-following cut — used 1x (Shot 6) — scissors along the dotted line. SIGNATURE.
12. Shape morph — used 2x (Shots 7, 9) — rectangle to tag; two books wrapped into a gift box.
13. Folding-screen unfold of real covers — used 1x (Shot 8) — Kyoto and Tokyo swing open.
14. Typewriter text — used 1x (Shot 8) — "THE PERFECT GIFT".
15. Idle wobble / breathing — used 3x (Shots 3, 8, 9) — held objects and the tree rock 2-3°.
16. Slide + settle — used 1x (Shot 9) — gift box slides under the tree.
17. Two-character pop-up — used 1x (Shot 10) — the boy, the girl and the bunny hop up behind the card.
18. Ribbon swirl (path draw) — used 1x (Shot 10) — red and green ribbons draw along curved paths.
19. Page fold transition — used 1x (Shot 11) — sheet folds over to reveal end card.
20. Static hold — used 1x (Shot 12) — series lockup, tagline, publisher, Amazon line, cover row, 30% OFF tag.
```

### EFFECTS DENSITY MAP

```
00:00–00:03 = HIGH DENSITY (drop-in, petals, slide-in, slam, starburst, confetti, accordion, cover fan — 8 effects in 3s)
00:03–00:06 = MEDIUM DENSITY (ribbon wipe, crayon fill, text pop x2, badge pop, path cut — 6 effects in 3s, evenly spaced)
00:06–00:09 = MEDIUM DENSITY (piece drop, shape morph, card pop, folding screen, typewriter, wobble — 6 effects in 3s)
00:09–00:12 = MEDIUM DENSITY (stack morph, slide, tree wobble, unfold, pop-up, ribbon swirl — 6 effects in 3s)
00:12–00:14.4 = LOW DENSITY (page fold, then a static end card — 1 effect in 2.4s)
```

### ENERGY ARC

```
Act 1 (0–3s) — Attention grab: three quick beats (tag drops, star stamp slams, six real covers
  fan out) each louder than the last. The covers themselves are the hook: a viewer who already
  knows the series recognizes it in under three seconds, and a new viewer sees six Japan-themed
  books at once.
Act 2 (3–10.2s) — Three benefits at a steady march: color it / remember it (the series tagline),
  30% off, the perfect gift (two real covers). Each beat uses the same grammar (prop enters →
  headline pops → boy reacts) for 1.1–2.1s. The scissors cutting the price is the signature
  moment; wrapping the books into a gift and sliding it under the tree is the release that says
  "buy it as a present".
Act 3 (10.2–14.4s) — Landing: the CTA card gets the most decoration (both kids, ribbons, crayons)
  then a single page fold drops everything to a silent end card that repeats the covers' own
  typography and tagline, so the video ends looking like the books do.
```

---

## 4. 分割プロンプト（4〜5秒ずつ3本に分けて生成する場合）

生成モデルが1回で14秒を作れない場合は、スタイル定義＋以下を1本ずつ生成します。
**各パートに表紙画像を参照として添付してください**（Part A：6冊、Part B：Kyoto と Tokyo、Part C：6冊）。

### Part A（0.0–4.6s）導入〜COLOR IT / REMEMBER IT

```
[STYLE 定義を貼る]
SEQUENCE (4.6s): A kraft paper gift tag reading "XMAS SALE" flutters down with paper snowflakes and
pink petals and lands tilted; the boy in the red beanie jogs in from the right holding his white
paper bunny. A gold paper star stamp slams onto the tag and a red sawtooth starburst reading
"HOLIDAY SALE!" bursts out with red, green, gold and pink paper flecks; the boy hops. The boy
unfolds a pleated strip into a wide cream card "JAPAN COLORING BOOK" ("JAPAN" in red) with a small
line "for Kids · Ages 5–10 · 6 Titles", and the six real books from the reference images (Japan
Tokyo, Japan Kyoto, Japan Food, Japan Festivals & Matsuri, Japan Animals & Nature, Sumo) fan out
beside it like a hand of cards, covers facing the camera and readable, Tokyo on top, as he pushes
the stack. He grabs a red-and-white candy-cane striped paper ribbon and pulls it across the frame
right-to-left, wiping to empty paper. A giant red paper crayon rolls in from the left; he
scribbles a navy line-art torii gate red in three strokes; "COLOR IT" then "REMEMBER IT" pop in
with a bounce, and a round green paper badge "MEMORY PROMPTS INSIDE" pops in at the lower left.
All text in English, spelled exactly; the covers are reproduced from the reference images, not
invented.
```

### Part B（4.6–10.2s）30% OFF〜THE PERFECT GIFT〜ツリーの下へ

```
[STYLE 定義を貼る]
SEQUENCE (5.6s): A red paper rectangle with a dotted line slides in from the left. The boy in the
red beanie cuts along the line with oversized grey paper scissors, four snips, right to left. The
lower half tumbles away; the remainder snaps into a price tag with a gold string reading "30% OFF"
in white, the "30%" very large. A small white card "Until Dec 25" with a paper holly leaf pops in
at the upper right; the boy kicks the scrap off-frame. The tag flips back and two real books unfold
like a folding screen, covers to camera and readable: left "Japan Kyoto Coloring Book for Kids",
right "Japan Tokyo Coloring Book for Kids", exactly as in the reference images, a red paper bow on
the corner of the right book. The right book rocks gently while "THE PERFECT GIFT" types in below
in heavy navy capitals. The boy stacks both books, red paper wraps around them and a gold bow pops
on top; he slides the gift box right until it settles under a green paper Christmas tree with a
gold star and tiny pink petals; the tree wobbles and the star spins; the boy walks off to the
right. All text in English.
```

### Part C（10.2–14.4s）CTA〜エンドカード

```
[STYLE 定義を貼る]
SEQUENCE (4.2s): The red gift box lid pops open and ribbon-yellow paper unfolds out of it into a
rounded card: small line "HOLIDAY SALE ON NOW" in red with a navy underline, big line
"Get it on Amazon" in navy with a red underline (plain text, no Amazon logo), a red paper cup
holding three crayons beside it. The boy in the red beanie and the girl in the pink hoodie pop up
together from behind the card with arms raised, the white bunny between them. A red ribbon curls
in from the left and a green ribbon from the right, drawing along their paths; petals and
snowflakes drift past. The whole scene folds over like a page turning on its vertical center,
revealing plain cream paper with a paper lockup in the style of the book covers: "Japan" in big
red rounded letters with a white outline, "Coloring Book for Kids" in rainbow rounded letters, a
small yellow ribbon "Color it. Remember it. Keep it forever." in navy, "by Takeda Studio" in small
navy capitals, a white strip "Available on Amazon", a small red "30% OFF" tag hanging from the
"n" of "Japan", and the six real covers standing in a small tilted row on the right like books on
a shelf. Hold completely still for 2 seconds. All text in English, spelled exactly as written.
```

---

## 5. BGM（音楽）の作り方

元動画はナレーションなし・BGM＋紙の効果音だけでした。この版も同じ設計にします。
**X（旧Twitter）ではタイムライン上で音が出ない状態から再生される**ので、メッセージは画面の文字で
完結させ、音は「音を出した人へのご褒美」と割り切るのが安全です。

### 3つの入手ルート

| ルート | 向いている人 | 費用 | 注意点 |
|---|---|---|---|
| A. AI音楽生成（Higgsfield generate_audio、Suno、Udio など） | 下のプロンプトを貼るだけで済ませたい | クレジット消費 | 生成物の商用利用可否を各サービスの規約で確認 |
| B. 動画生成モデルに音も作らせる（Seedance 2.5 / Kling 3.0 の音声付き生成） | 一発で済ませたい | 動画生成に含まれる | 3分割で作ると3本の曲がバラバラになるので、BGMは別で1本作って上から乗せる方が良い |
| C. ロイヤリティフリー音源（YouTube オーディオライブラリ、Pixabay Music、Epidemic Sound） | 確実に権利をクリアしたい | 無料〜月額 | "sleigh bells ukulele playful" で検索。**市販のクリスマス曲の音源は使わない**（Jingle Bells の旋律は著作権切れでも、録音物には権利がある） |

### AI音楽生成用プロンプト（14.4秒・BGM）

```
Playful Christmas jingle for a kids' product ad, 15 seconds, instrumental, no vocals.
Sleigh bells on every beat, bright ukulele strum, glockenspiel melody, soft pizzicato strings,
light hand claps, a hint of a Japanese pentatonic melody in the glockenspiel. Tempo 120 BPM,
key of C major, cheerful and warm, papercraft / stop-motion mood. Structure: 0-1s a single
sleigh-bell shake as a pickup; 1-10s a bouncy 4-bar loop; 10-12s a short rising build with a
whole-note chord; 12.5-13s one final bright chime with a short reverb tail; then silence.
Mix: bright, mono-compatible, no bass-heavy sub, loudness suitable for social media (-14 LUFS).
```

### 効果音（紙のフォーリー）の入れどころ

| 秒 | 音 | 何が起きているか |
|---|---|---|
| 0.4 | 紙がふわっと落ちる音 | ギフトタグが着地 |
| 1.0 | ドン（スタンプ） | 星スタンプが押される |
| 1.2 | ポン＋紙吹雪のサラサラ | HOLIDAY SALE! が弾ける |
| 1.5 / 1.9 | 紙がめくれる音（アコーディオン）＋ 本が滑る音 | タイトルカードと6冊が開く |
| 3.0 | シュッ | リボンワイプ |
| 3.6–4.1 | クレヨンでこする音 | 鳥居を塗る |
| 3.75 / 4.0 / 4.2 | ポン×3 | COLOR IT / REMEMBER IT / 緑バッジ |
| 4.9–5.55 | チョキチョキ×4 | ハサミで切る |
| 5.9 | ポン | Until Dec 25 |
| 6.8 / 7.0 | 紙が開く音×2 | Kyoto と Tokyo が開く |
| 7.35–7.95 | カタカタ（タイプ音） | THE PERFECT GIFT |
| 8.9 | 本を重ねる音＋紙を包む音 | ギフト箱になる |
| 10.0 | コトン＋シャラン | 箱がツリーの下に収まる・星が回る |
| 10.3 / 10.6 | パカッ＋ポン | 箱が開く・2人が飛び出す |
| 12.2 | パタン | ページ折り |
| 13.0 | 最後のチャイム → 無音 | エンドカード |

効果音は Pixabay や freesound.org で "paper rustle" "stamp" "scissors snip" "paper fold" を検索すれば揃います。
動画編集ソフト（CapCut、DaVinci Resolve など）で BGM を1本敷き、上の秒に効果音を置いてください。

---

## 6. X（旧Twitter）投稿のしかた

**できます。** X は動画付き投稿に対応していて、この動画の仕様（16:9・14.4秒・音なしでも伝わる）は X 向けにそのまま使えます。

| 項目 | 推奨 |
|---|---|
| 形式 | MP4（H.264 / AAC） |
| 画面 | 1280×720（16:9）。フィードで大きく見せたいなら 1080×1080（1:1）版も作ると良い |
| 尺 | 14.4秒（X の上限は 2分20秒なので余裕あり） |
| 容量 | 512MB 以下（この尺なら数MB） |
| 音 | 無音再生が前提。文字で完結しているのでOK |
| リンク | 投稿本文に Amazon の商品ページ（またはシリーズの著者ページ）URLを入れる。動画内にURLは入れない |

### 投稿文の例（英語）

```
🎄 Holiday Sale — 30% OFF until Dec 25!
Japan Coloring Book for Kids by Takeda Studio: Tokyo, Kyoto, Food, Festivals & Matsuri,
Animals & Nature, and Sumo. 30 scenes each, with memory prompts inside.
Color it. Remember it. Keep it forever.
Get it on Amazon 👉 [商品ページURL]
#coloringbook #kidsactivities #japan #christmasgift #KDP
```

### 投稿文の例（日本語・国内向けに出す場合）

```
🎄 クリスマスセール 12/25まで 30% OFF
こども向け英語版ぬりえ「Japan Coloring Book for Kids」（Takeda Studio）
東京・京都・日本の食べ物・お祭り・動物と自然・相撲の6冊。各30シーン、思い出を書き込むページつき。
Amazonで販売中 👉 [商品ページURL]
#ぬりえ #知育 #英語 #クリスマスプレゼント
```

**縦型（9:16）が必要な場合**：Instagram リール・TikTok・YouTube ショート向けには、スタイル定義の
`Aspect ratio 16:9 (1280x720)` を `Aspect ratio 9:16 (1080x1920)` に変えて生成し直してください。
主人公を右側ではなく下側に、文字を上側に置く指示に変える必要があるので、必要なら縦型プロンプトも作ります。

---

## 7. 参照画像の使い方（まとめ）

| 画像 | 役割 | 添えるひとこと |
|---|---|---|
| `covers/*.jpg`（6冊の表紙） | **本そのもの**。カット3・8・12で正面を向く | "Reproduce these covers faithfully; do not change their text or art." |
| `../../frames/05_2.50s.jpg` | 紙の質感・厚み・影の参照 | "Reference for paper texture and shadows only, not for colors or characters." |
| `../../frames/09_5.10s.jpg` | ハサミのカットの構図 | 同上 |
| `../../frames/16_11.40s.jpg` | CTAカードとリボンの構図 | 同上 |

Higgsfield で `generate_video` の `hf_mult_motion_control`（動きの転写）を使う場合は、元動画そのものを
driving video に指定し、表紙6枚を image として添付し、Part A〜C を各パートのテキストにすると、動きが元動画と揃います。

---

## 8. 日本語カット表（確認用）

| # | 時間 | 画面に出るもの | 動き |
|---|---|---|---|
| 1 | 0.00–0.55 | ギフトタグ「XMAS SALE」、花びらと雪片、赤ニット帽の男の子（白うさぎ） | タグがひらひら落ちて着地。男の子が右から登場 |
| 2 | 0.55–1.40 | 金の星スタンプ、赤い吹き出し「HOLIDAY SALE!」 | スタンプがドン → 吹き出しが弾ける。紙片が飛ぶ。男の子がジャンプ |
| 3 | 1.40–2.95 | カード「JAPAN COLORING BOOK / for Kids · Ages 5–10 · 6 Titles」、実物の表紙6冊 | アコーディオンで開く → 6冊が扇状に広がり、正面を向いて止まる |
| 4 | 2.95–3.30 | 赤白ストライプのリボン | 男の子が引っ張って右から左へワイプ |
| 5 | 3.30–4.60 | 巨大クレヨン、線画の鳥居、「COLOR IT」「REMEMBER IT」、緑バッジ「MEMORY PROMPTS INSIDE」 | 鳥居が赤く塗られる。文字が順にポン。バッジがポン |
| 6 | 4.60–5.65 | 赤い紙（点線入り）、大きなハサミ | 点線に沿ってジョキジョキ切る |
| 7 | 5.65–6.75 | 値札タグ「30% OFF」、小カード「Until Dec 25」 | 下半分が落ちて値札の形に。期間カードがポン |
| 8 | 6.75–8.85 | Kyoto と Tokyo の表紙2冊、「THE PERFECT GIFT」 | 屏風のように開いて正面を向く。右の本が揺れる。文字がタイプライター風 |
| 9 | 8.85–10.20 | 赤いギフト箱（本を包んだもの）、緑の紙のツリー | 2冊を重ねて包む。ツリーの下へ滑る。男の子退場 |
| 10 | 10.20–12.10 | 黄色いCTAカード「HOLIDAY SALE ON NOW / Get it on Amazon」、クレヨン立て、リボン、男の子と女の子 | 箱が開いてカードが広がる。2人が飛び出す。リボンが巻きつく |
| 11 | 12.10–12.40 | 紙のページ | 紙を折るように転換 |
| 12 | 12.40–14.40 | 「Japan / Coloring Book for Kids」ロゴ、タグライン、「by Takeda Studio」「Available on Amazon」、30% OFF タグ、表紙6冊の列 | 静止して終了 |
