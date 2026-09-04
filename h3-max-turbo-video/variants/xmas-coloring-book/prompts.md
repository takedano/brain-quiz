# Japan Coloring Book ― Holiday Sale 30% OFF（AI生成版プロンプト・英語テキスト版）

元動画（H3 Max Turbo 告知）の **12カット構成・14.4秒・ペーパークラフト様式** をそのまま使い、
Amazon KDP で販売中の子ども向け英語版ぬりえ **「Japan Coloring Book」（Takeda Studio）** の
クリスマスセール告知に差し替えたプロンプト一式です。画面に出る文字は **すべて英語** です。

```
 元動画                        →  Japan Coloring Book 版
 ─────────────────────────────────────────────────────────
 クラフト紙（ベージュ）          →  雪のような白い紙 ＋ 紙の雪片
 コーラル / ブルー / ティール    →  クリスマス赤 / モミの緑 / 金（＋ 藍色の線画）
 会社員の女性                    →  エルフ帽の子ども（紙人形）
 AI UPDATE のメモ               →  「XMAS SALE」のギフトタグ
 スタンプ → 朗報！              →  金の星スタンプ → HOLIDAY SALE!
 H3 Max Turbo登場               →  JAPAN COLORING BOOK / English Edition for Kids
                                   （富士山・寿司・だるま・鯉のぬりえページが扇状に）
 ストップウォッチ：速度2倍       →  大きなクレヨン：COLOR IT → LEARN IT（DARUMA）
 ハサミ：コスト半分             →  ハサミで値札を切る：30% OFF
 2枚のフレーム：品質ほぼそのまま →  線画→彩色の2ページ（MT. FUJI）：THE PERFECT GIFT
 くしゃくしゃ → ゴミ箱          →  折りたたんでギフト箱 → ツリーの下へ
 期間限定プロモーション         →  HOLIDAY SALE ON NOW / Get it on Amazon
 H3 MAX TURBO ロゴ              →  JAPAN COLORING BOOK / by Takeda Studio / Available on Amazon
```

---

## 0. 画面に出る英語テキスト一覧（先に確認）

| # | カット | 画面の文字 | 備考 |
|---|---|---|---|
| 1 | ギフトタグ | `XMAS SALE` | |
| 2 | 爆発吹き出し | `HOLIDAY SALE!` | |
| 3 | 登場カード | `JAPAN COLORING BOOK` ＋ 小さく `English Edition · for Kids` | ブランド名 |
| 3 | 扇状のページ | `MT. FUJI` `SUSHI` `DARUMA` `KOI` | 日本モチーフの線画 |
| 5 | 売り文句1 | `COLOR IT` → `LEARN IT` ＋ 単語タグ `DARUMA` | |
| 7 | 値札タグ | `30% OFF` | |
| 7 | 期間カード | `Until Dec 25` | **仮置き。実際のセール期間に差し替え** |
| 8 | 売り文句3 | `THE PERFECT GIFT` | |
| 10 | CTAカード | `HOLIDAY SALE ON NOW` / `Get it on Amazon` | |
| 12 | エンドカード | `JAPAN COLORING BOOK` / `by Takeda Studio` / `Available on Amazon` ＋ 小タグ `30% OFF` | |

> **Amazon の表記について**：文字で "Available on Amazon" / "Get it on Amazon" と書くのは一般的な表現ですが、
> Amazon のロゴ（矢印のマーク）や "a" のアイコンは商標のため、動画内に描かせないでください。
> プロンプトにも「ロゴは使わず文字のみ」と明記してあります。

> **30% OFF の表記について**：KDP のペーパーバックはクーポン機能がないため、割引は期間中に
> 定価（List Price）を下げることで実現します。Kindle 版は KDP Select 登録なら Countdown Deal が使えます。
> 実際に値下げしていない期間に「30% OFF」の動画を流すと景品表示法・Amazon規約の両方に触れるので、
> 値下げ期間と動画の掲載期間を必ず合わせてください。

---

## 1. スタイル定義（すべてのプロンプトの先頭に付ける）

```
STYLE: Handcrafted paper-cutout stop-motion animation, 3D-rendered papercraft look, Christmas
craft-corner mood with a light Japanese touch. Every object is a flat piece of 1-2mm thick card
stock with visible white paper edges and a soft, short drop shadow. Background is a fixed sheet of
snow-white textured paper (#F3EFE4) with fine fiber grain, a gentle vignette, and a few small paper
snowflakes that drift down slowly through the whole video. Fixed camera, straight-on, slight
top-down tilt; only the paper objects move. Palette: Christmas red #D9463F, pine green #2F7A5A,
gold #E9B94B, ice blue #8CC5E3, kraft brown #C9A97C, indigo navy #24243C, off-white card #FBF8F0.
Character: a paper-doll child about six years old, short brown hair, a green pointed elf hat with a
white pom-pom, a red knit sweater with one white snowflake, green trousers, yellow boots, round
paper pins at shoulders, elbows and knees. The child stays on the right side of the frame and
interacts with every prop (catches, colors, cuts, folds, raises arms), always cheerful.
Coloring-book pages are white paper with thick indigo line art of Japanese motifs (Mt. Fuji, sushi,
a daruma doll, a koi fish, a torii gate) and an English word in rounded capitals printed under
each picture.
ALL ON-SCREEN TEXT IS IN ENGLISH, spelled exactly as written in the shot list. Headlines are heavy
rounded sans-serif capitals (like Nunito Black / Fredoka), cut from paper with thickness and
shadow; word tags are rounded navy capitals. Text pops in with a bouncy overshoot
(scale 0 → 1.1 → 1.0) or unfolds like an accordion. Never draw the Amazon logo or smile icon;
"Amazon" appears as plain text only. No hard cuts: every transition is a paper gesture (ribbon
wipe, folding screen, fold into a gift box, page fold).
Aspect ratio 16:9 (1280x720), 24fps, 14.4 seconds. No narration; bright, playful sleigh-bell BGM
with paper foley (rustle, stamp, crayon scribble, snip, fold) on each beat.
```

---

## 2. フルプロンプト（14.4秒・1本用）

### SHOT-BY-SHOT EFFECTS TIMELINE

```
SHOT 1 (00:00.0–00:00.85) — Gift Tag Drop
• EFFECT: Object drop-in (gravity settle) + drifting paper snowflakes + character slide-in
• A kraft-brown paper gift tag with a red string, reading "XMAS SALE" in navy capitals, flutters
  down from the top-left, rocks once and settles tilted approx -12°. Three small white paper
  snowflakes drift down behind it. The elf-hat child jogs in from the right edge with a bobbing
  walk, arms swinging, boots tapping.
• Camera fixed, straight-on. Empty snow-white paper background.
• Tag lands at 0.4s; child reaches center-right at 0.85s.
• Exits by the tag being covered by the star stamp in SHOT 2.

SHOT 2 (00:00.85–00:01.45) — Gold Star Stamp and Burst
• EFFECT: Impact slam (scale 1.6 → 1.0 with squash) + starburst reveal + paper confetti
• A gold paper star-shaped stamp slams down from above onto the tag. On impact a large red
  starburst speech bubble (sawtooth edge, 16 points, white paper edge) pops out behind it and the
  tag is replaced by the burst reading "HOLIDAY SALE!" in white heavy rounded capitals on red.
• Small red, green and gold paper flecks fly outward and fall; the child does a small jump.
• Slam lands at 1.0s; burst fully visible at 1.2s; hold to 1.45s.
• Exits by the burst flipping down and folding into a strip for SHOT 3.

SHOT 3 (00:01.45–00:02.95) — Book Title and Pages Fan Out
• EFFECT: Accordion unfold (paper pleats opening) + fan stack (staggered rotation)
• A pleated strip of paper held by the child unfolds left-to-right into a wide white card: big
  line "JAPAN COLORING BOOK" in heavy navy rounded capitals, small line under it
  "English Edition · for Kids" in red.
• Behind it, 4 coloring-book pages slide out and fan into a stack, each rotated 2-4° more than the
  last: Mt. Fuji with "MT. FUJI", a sushi plate with "SUSHI", a daruma doll with "DARUMA", a koi
  fish with "KOI". Indigo line art only on white, each with a red or green paper edge.
• The child pushes the stack with both hands, leaning into it.
• Unfold 1.45–1.85s; fan-out 1.85–2.3s; hold with a slight breathing wobble to 2.95s.
• Exits via the candy-cane ribbon wipe in SHOT 4.

SHOT 4 (00:02.95–00:03.30) — Candy-Cane Ribbon Wipe
• EFFECT: Wipe transition (paper ribbon) — 0.35 seconds
• The child grabs the end of a wide paper ribbon striped red and white like a candy cane and pulls
  it across the whole frame from right to left; the ribbon covers the pages and reveals an empty
  background.
• Motion blur on the ribbon, slight curl at its leading edge.

SHOT 5 (00:03.30–00:04.60) — Crayon: Color It, Learn It
• EFFECT: Prop entrance + crayon scribble fill + staggered text pop + word-tag pop
• A large paper line-art daruma doll stands at center-left. A giant red paper crayon rolls in
  from the left; the child catches it and scribbles across the daruma: it fills with red in three
  diagonal strokes, its face stays white, two gold dots pop in as the eyes.
• "COLOR IT" pops in above-left (scale overshoot), then "LEARN IT" pops in below it, larger,
  0.25s later. A small white paper tag reading "DARUMA" in rounded navy capitals pops in under
  the doll with a bounce.
• Crayon enters 3.3–3.6s; scribble 3.6–4.1s; "COLOR IT" at 3.75s; "LEARN IT" at 4.0s; "DARUMA" 4.2s.
• Exits by the daruma and crayon sliding right off-frame while the red price sheet enters from the left.

SHOT 6 (00:04.60–00:05.65) — Scissors Cut the Price
• EFFECT: Prop entrance + path-following cut + piece separation
• A large red rectangle of paper (a price tag before it is shaped) slides in from the left with a
  dotted cut line across its middle and a faint crossed-out price on the lower half. Oversized
  grey paper scissors held by the child open and close 4 times, moving right-to-left along the
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
• The child kicks the fallen scrap, which slides off-frame.
• Tag forms 5.65–5.9s; card pops 5.9s; kick 6.3–6.7s.
• Exits by the tag flipping backward and folding into the two pages of SHOT 8.

SHOT 8 (00:06.75–00:08.85) — The Perfect Gift
• EFFECT: Folding-screen unfold (rotate on vertical hinge) + typewriter text + subtle wobble
• Two navy-framed coloring pages unfold like a folding screen: left panel first, right panel
  swings open from its hinge. Left page: Mt. Fuji in indigo line art with "MT. FUJI" under it.
  Right page: the same Mt. Fuji fully colored with crayon strokes (blue mountain, white snow cap,
  red rising sun, pink cherry blossoms), slightly shifted to show "before and after".
• The child steadies the right panel with one hand. The right panel rocks gently (approx 3°).
• "THE PERFECT GIFT" types in below in heavy navy capitals, one letter every ~60ms, starting 7.35s.
• Pages open 6.75–7.3s; text 7.35–7.95s; hold to 8.85s.
• Exits as the child grabs both pages and folds them.

SHOT 9 (00:08.85–00:10.20) — Fold into a Gift, Slide Under the Tree
• EFFECT: Fold morph (pages fold into a box) + slide + settle wobble
• The two pages fold in the child's hands into a small red paper gift box with a gold paper bow.
  A green paper Christmas tree with a gold star on top appears at the lower right.
• The box slides right along the floor, bumps once, and settles under the tree; the tree wobbles
  and the star spins half a turn. The child steps out of frame to the right.
• Fold 8.85–9.1s; slide 9.3–10.0s; tree wobble 10.0–10.2s.
• Exits via the box lid popping open in SHOT 10.

SHOT 10 (00:10.20–00:12.10) — Sale CTA Card
• EFFECT: Unfold reveal + character pop-up + ribbon swirl (path draw)
• The gift box lid pops open and a sheet of off-white paper unfolds out of it and flattens into
  a rounded CTA card: small line "HOLIDAY SALE ON NOW" with a red underline, big line
  "Get it on Amazon" with a green underline (plain text, no Amazon logo). A red paper cup holding
  three crayons (red, green, blue) sits at the right of the card.
• The child pops up from behind the card, both arms raised, with a small hop; the elf-hat pom-pom
  bounces.
• A red ribbon curls around from the left and a green ribbon from the right, drawing themselves
  along their paths and settling with a slight sway. Two more paper snowflakes drift past.
• Unfold 10.2–10.55s; child pop 10.6s; ribbons 10.9–11.6s; hold to 12.1s.
• Exits by the page fold in SHOT 11.

SHOT 11 (00:12.10–00:12.40) — Page Fold Transition
• EFFECT: Fold transition (page turns over its vertical center) — 0.3 seconds
• The whole scene is a sheet of paper that folds over from the center, back-side showing plain
  snow-white paper, wiping everything away and revealing the end card.

SHOT 12 (00:12.40–00:14.40) — Logo End Card
• EFFECT: Static hold (no effects)
• Plain snow-white paper background. Centered, slightly above the vertical middle: heavy navy
  rounded wordmark "JAPAN COLORING BOOK" on two lines, a thin red paper line under it, and
  "by Takeda Studio" in small navy capitals. Below that, a small white paper strip reading
  "Available on Amazon" (plain text). A small red "30% OFF" paper tag hangs from the last letter
  of the wordmark. One paper snowflake rests in a corner. Nothing moves for 2 seconds.
• Audio drops to silence at 13.0s.
```

### MASTER EFFECTS INVENTORY

```
1. Object drop-in / gravity settle — used 2x (Shots 1, 7) — gift tag and price scrap land and rock.
2. Drifting paper snowflakes — used 3x (Shots 1, 10, 12) — ambient Christmas motion, always slow.
3. Impact slam with squash — used 1x (Shot 2) — the gold star stamp; loudest beat of the opening.
4. Starburst reveal — used 1x (Shot 2) — the red "HOLIDAY SALE!" bubble.
5. Paper confetti / flecks — used 2x (Shots 2, 6) — red/green/gold pieces scatter on impact and cut.
6. Accordion unfold — used 2x (Shots 3, 10) — pleated paper opens into a flat card.
7. Fan stack (staggered rotation) — used 1x (Shot 3) — coloring pages spread like a hand of cards.
8. Ribbon wipe — used 1x (Shot 4) — candy-cane striped ribbon transition.
9. Crayon scribble fill — used 1x (Shot 5) — the daruma fills with red in three strokes.
10. Bouncy text pop (scale overshoot) — used 6x (Shots 2, 5, 7, 10) — every headline and the word tag.
11. Path-following cut — used 1x (Shot 6) — scissors along the dotted line. SIGNATURE.
12. Shape morph — used 2x (Shots 7, 9) — rectangle to tag; pages to gift box.
13. Folding-screen unfold — used 1x (Shot 8) — hinged pages swing open.
14. Typewriter text — used 1x (Shot 8) — "THE PERFECT GIFT".
15. Idle wobble / breathing — used 3x (Shots 3, 8, 9) — held objects and the tree rock 2-3°.
16. Slide + settle — used 1x (Shot 9) — gift box slides under the tree.
17. Character pop-up — used 1x (Shot 10) — arms-raised hop from behind the card.
18. Ribbon swirl (path draw) — used 1x (Shot 10) — red and green ribbons draw along curved paths.
19. Page fold transition — used 1x (Shot 11) — sheet folds over to reveal end card.
20. Static hold — used 1x (Shot 12) — wordmark, publisher line, Amazon line, hanging 30% OFF tag.
```

### EFFECTS DENSITY MAP

```
00:00–00:03 = HIGH DENSITY (drop-in, snowflakes, slide-in, slam, starburst, confetti, accordion, fan stack — 8 effects in 3s)
00:03–00:06 = MEDIUM DENSITY (ribbon wipe, crayon fill, text pop x3, path cut — 6 effects in 3s, evenly spaced)
00:06–00:09 = MEDIUM DENSITY (piece drop, shape morph, card pop, folding screen, typewriter, wobble — 6 effects in 3s)
00:09–00:12 = MEDIUM DENSITY (fold morph, slide, tree wobble, unfold, pop-up, ribbon swirl — 6 effects in 3s)
00:12–00:14.4 = LOW DENSITY (page fold, then a static end card — 1 effect in 2.4s)
```

### ENERGY ARC

```
Act 1 (0–3s) — Attention grab: three quick beats (tag drops, star stamp slams, pages fan) each
  louder than the last. The child's jump on the stamp is the emotional peak; snowflakes set the
  season and the Japanese line art sets the product in the first three seconds without narration.
Act 2 (3–10.2s) — Three benefits at a steady march: learn by coloring, 30% off, perfect gift.
  Each beat uses the same grammar (prop enters → headline pops → child reacts) for 1.1–2.1s.
  The scissors cutting the price is the signature moment; folding the pages into a gift and
  sliding it under the tree is the release that clears the stage and says "buy it as a present".
Act 3 (10.2–14.4s) — Landing: the CTA card gets the most decoration (ribbons, pop-up, crayons)
  then a single page fold drops everything to a silent end card carrying the brand, the publisher,
  where to buy, and the 30% OFF tag still hanging on it.
```

---

## 3. 分割プロンプト（4〜5秒ずつ3本に分けて生成する場合）

生成モデルが1回で14秒を作れない場合は、スタイル定義＋以下を1本ずつ生成します。
各パートの終わりと次の始まりが同じ「紙の転換」になっているので、つなぎ目が目立ちません。

### Part A（0.0–4.6s）導入〜COLOR IT / LEARN IT

```
[STYLE 定義を貼る]
SEQUENCE (4.6s): A kraft paper gift tag reading "XMAS SALE" flutters down with three paper
snowflakes and lands tilted; the elf-hat paper-doll child jogs in from the right. A gold paper star
stamp slams onto it and a red sawtooth starburst reading "HOLIDAY SALE!" bursts out with red, green
and gold paper flecks; the child hops. The child unfolds a pleated strip into a wide white card
"JAPAN COLORING BOOK" with a small red line "English Edition · for Kids", and four coloring-book
pages (indigo line art: MT. FUJI, SUSHI, DARUMA, KOI, each word printed under its picture) fan out
behind it as the child pushes the stack. The child grabs a red-and-white candy-cane striped paper
ribbon and pulls it across the frame right-to-left, wiping to empty paper. A giant red paper crayon
rolls in from the left; the child scribbles a line-art daruma doll red in three strokes, its face
stays white and two gold eye dots pop in; "COLOR IT" then "LEARN IT" pop in with a bounce, and a
small white tag "DARUMA" pops in under the doll. All text in English, no logos.
```

### Part B（4.6–10.2s）30% OFF〜THE PERFECT GIFT〜ツリーの下へ

```
[STYLE 定義を貼る]
SEQUENCE (5.6s): A red paper rectangle with a dotted line slides in from the left. The elf-hat
child cuts along the line with oversized grey paper scissors, four snips, right to left. The lower
half tumbles away; the remainder snaps into a price tag with a gold string reading "30% OFF" in
white, the "30%" very large. A small white card "Until Dec 25" with a paper holly leaf pops in at
the upper right; the child kicks the scrap off-frame. The tag flips back and two navy-framed
coloring pages unfold like a folding screen: left, Mt. Fuji in indigo line art with "MT. FUJI";
right, the same Mt. Fuji colored with crayon strokes (blue mountain, white snow, red sun, pink
blossoms). The right page rocks gently while "THE PERFECT GIFT" types in below in heavy navy
capitals. The child folds both pages into a small red gift box with a gold bow and slides it right
until it settles under a green paper Christmas tree with a gold star; the tree wobbles and the star
spins; the child walks off to the right. All text in English.
```

### Part C（10.2–14.4s）CTA〜エンドカード

```
[STYLE 定義を貼る]
SEQUENCE (4.2s): The red gift box lid pops open and off-white paper unfolds out of it into a
rounded card: small line "HOLIDAY SALE ON NOW" with a red underline, big line "Get it on Amazon"
with a green underline (plain text, no Amazon logo), a red paper cup holding three crayons beside
it. The elf-hat child pops up from behind the card with both arms raised, pom-pom bouncing. A red
ribbon curls in from the left and a green ribbon from the right, drawing along their paths; two
paper snowflakes drift past. The whole scene folds over like a page turning on its vertical
center, revealing plain snow-white paper with a heavy navy rounded wordmark "JAPAN COLORING BOOK"
on two lines, a thin red line, "by Takeda Studio" in small capitals, a small white strip
"Available on Amazon", and a small red "30% OFF" paper tag hanging from the wordmark. Hold
completely still for 2 seconds. All text in English, spelled exactly as written.
```

---

## 4. BGM（音楽）の作り方

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
light hand claps. Tempo 120 BPM, key of C major, cheerful and warm, papercraft / stop-motion
mood. Structure: 0-1s a single sleigh-bell shake as a pickup; 1-10s a bouncy 4-bar loop;
10-12s a short rising build with a whole-note chord; 12.5-13s one final bright chime with a
short reverb tail; then silence. Mix: bright, mono-compatible, no bass-heavy sub, loudness
suitable for social media (-14 LUFS).
```

### 効果音（紙のフォーリー）の入れどころ

| 秒 | 音 | 何が起きているか |
|---|---|---|
| 0.4 | 紙がふわっと落ちる音 | ギフトタグが着地 |
| 1.0 | ドン（スタンプ） | 星スタンプが押される |
| 1.2 | ポン＋紙吹雪のサラサラ | HOLIDAY SALE! が弾ける |
| 1.5 / 1.9 | 紙がめくれる音（アコーディオン） | タイトルカードとページが開く |
| 3.0 | シュッ | リボンワイプ |
| 3.6–4.1 | クレヨンでこする音 | だるまを塗る |
| 3.75 / 4.0 / 4.2 | ポン×3 | COLOR IT / LEARN IT / DARUMA |
| 4.9–5.55 | チョキチョキ×4 | ハサミで切る |
| 5.9 | ポン | Until Dec 25 |
| 6.8 / 7.0 | 紙が開く音×2 | 屏風のように開く |
| 7.35–7.95 | カタカタ（タイプ音） | THE PERFECT GIFT |
| 8.9 | 紙を折る音 | ギフト箱になる |
| 10.0 | コトン＋シャラン | 箱がツリーの下に収まる・星が回る |
| 10.3 / 10.6 | パカッ＋ポン | 箱が開く・子どもが飛び出す |
| 12.2 | パタン | ページ折り |
| 13.0 | 最後のチャイム → 無音 | エンドカード |

効果音は Pixabay や freesound.org で "paper rustle" "stamp" "scissors snip" "paper fold" を検索すれば揃います。
動画編集ソフト（CapCut、DaVinci Resolve など）で BGM を1本敷き、上の秒に効果音を置いてください。

---

## 5. X（旧Twitter）投稿のしかた

**できます。** X は動画付き投稿に対応していて、この動画の仕様（16:9・14.4秒・音なしでも伝わる）は X 向けにそのまま使えます。

| 項目 | 推奨 |
|---|---|
| 形式 | MP4（H.264 / AAC） |
| 画面 | 1280×720（16:9）。フィードで大きく見せたいなら 1080×1080（1:1）版も作ると良い |
| 尺 | 14.4秒（X の上限は 2分20秒なので余裕あり） |
| 容量 | 512MB 以下（この尺なら数MB） |
| 音 | 無音再生が前提。文字で完結しているのでOK |
| リンク | 投稿本文に Amazon の商品ページURLを入れる（動画内にURLは入れない。読めないため） |

### 投稿文の例（英語）

```
🎄 Holiday Sale — 30% OFF until Dec 25!
Japan Coloring Book (English Edition for Kids): color Mt. Fuji, sushi, daruma and koi,
and learn the words while you color. The perfect gift.
Get it on Amazon 👉 [商品ページURL]
#coloringbook #kidsactivities #japan #christmasgift #KDP
```

### 投稿文の例（日本語・国内向けに出す場合）

```
🎄 クリスマスセール 12/25まで 30% OFF
こども向け英語版ぬりえ「Japan Coloring Book」（Takeda Studio）
富士山・寿司・だるま・鯉をぬりながら英単語が身につきます。プレゼントにどうぞ。
Amazonで販売中 👉 [商品ページURL]
#ぬりえ #知育 #英語 #クリスマスプレゼント
```

**縦型（9:16）が必要な場合**：Instagram リール・TikTok・YouTube ショート向けには、スタイル定義の
`Aspect ratio 16:9 (1280x720)` を `Aspect ratio 9:16 (1080x1920)` に変えて生成し直してください。
主人公を右側ではなく下側に、文字を上側に置く指示に変える必要があるので、必要なら縦型プロンプトも作ります。

---

## 6. 参照画像の使い方

元動画のキーフレーム（`../../frames/`）は**動きと紙の質感の参照**として今回も有効です。色は違うので、
「構図と質感だけ参考にし、色と文字はプロンプトの指定に従う」と添えてください。

| ファイル | 用途 |
|---|---|
| `../../frames/05_2.50s.jpg` | キャラクターとカードの質感（紙の厚み・影） |
| `../../frames/09_5.10s.jpg` | ハサミで切るカットの構図 |
| `../../frames/16_11.40s.jpg` | CTAカードとリボンの構図 |

Higgsfield で `generate_video` の `hf_mult_motion_control`（動きの転写）を使う場合は、元動画そのものを
driving video に指定し、Part A〜C を各パートのテキストにすると、動きが元動画と揃います。

---

## 7. 日本語カット表（確認用）

| # | 時間 | 画面に出るもの | 動き |
|---|---|---|---|
| 1 | 0.00–0.55 | ギフトタグ「XMAS SALE」、雪片、エルフ帽の子ども | タグがひらひら落ちて着地。子どもが右から登場 |
| 2 | 0.55–1.40 | 金の星スタンプ、赤い吹き出し「HOLIDAY SALE!」 | スタンプがドン → 吹き出しが弾ける。紙片が飛ぶ。子どもがジャンプ |
| 3 | 1.40–2.95 | カード「JAPAN COLORING BOOK / English Edition · for Kids」、ぬりえページ4枚（富士山・寿司・だるま・鯉） | アコーディオンで開く → ページが扇状に広がる |
| 4 | 2.95–3.30 | 赤白ストライプのリボン | 子どもが引っ張って右から左へワイプ |
| 5 | 3.30–4.60 | 巨大クレヨン、線画のだるま、「COLOR IT」「LEARN IT」「DARUMA」 | だるまが赤く塗られる。文字が順にポン。単語タグがポン |
| 6 | 4.60–5.65 | 赤い紙（点線入り）、大きなハサミ | 点線に沿ってジョキジョキ切る |
| 7 | 5.65–6.75 | 値札タグ「30% OFF」、小カード「Until Dec 25」 | 下半分が落ちて値札の形に。期間カードがポン |
| 8 | 6.75–8.85 | 2枚のページ（線画／彩色の富士山）、「THE PERFECT GIFT」 | 屏風のように開く。右ページが揺れる。文字がタイプライター風 |
| 9 | 8.85–10.20 | 赤いギフト箱、緑の紙のツリー | ページを折ってギフト箱に。ツリーの下へ滑る。子ども退場 |
| 10 | 10.20–12.10 | CTAカード「HOLIDAY SALE ON NOW / Get it on Amazon」、クレヨン立て、赤と緑のリボン | 箱が開いてカードが広がる。子どもが飛び出す。リボンが巻きつく |
| 11 | 12.10–12.40 | 紙のページ | 紙を折るように転換 |
| 12 | 12.40–14.40 | 「JAPAN COLORING BOOK」「by Takeda Studio」「Available on Amazon」＋小タグ「30% OFF」 | 静止して終了 |
