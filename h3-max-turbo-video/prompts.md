# 再現用プロンプト（Seedance 2.0 / Higgsfield 向け）

`README.md` の解析結果を、AI動画生成に貼り付けられる形にしたものです。
まず**スタイル定義**を読み、次に**フルプロンプト（14秒・1本）**か**分割プロンプト（3本）**を使ってください。

---

## 0. 差し替え用テンプレート（日本語）

別の商品・別の文言で同じ動画を作るときは、この表を埋めてから下のプロンプトの `{ }` を置き換えます。

| 変数 | 元動画の値 | 説明 |
|---|---|---|
| `{PRODUCT}` | H3 Max Turbo | 商品名（カードとロゴに出る） |
| `{LOGO}` | H3 MAX TURBO | エンドカードのロゴ表記（大文字） |
| `{HOOK}` | 朗報！ | 冒頭の爆発吹き出しの一言 |
| `{ANNOUNCE}` | H3 Max Turbo登場 | 登場カードの文言 |
| `{BENEFIT1_LABEL}` / `{BENEFIT1_VALUE}` | 速度 / 2倍 | 売り文句1（小道具：ストップウォッチ） |
| `{BENEFIT2}` | コスト半分 | 売り文句2（小道具：ハサミと値札タグ） |
| `{PRICE_NOTE}` | 768p ｜ 1秒 ｜ $0.01 | 料金カードの表記 |
| `{BENEFIT3}` | 品質 ほぼそのまま | 売り文句3（小道具：2枚の風景フレーム） |
| `{CTA_SMALL}` / `{CTA_BIG}` | 期間限定プロモーション / 今すぐ試す | CTAカードの2行 |

---

## 1. スタイル定義（すべてのプロンプトの先頭に付ける）

```
STYLE: Handcrafted paper-cutout stop-motion animation, 3D-rendered papercraft look.
Every object is a flat piece of 1-2mm thick card stock with visible white paper edges
and a soft, short drop shadow. Background is a fixed sheet of cream kraft paper (#E9E4D2)
with fine fiber texture and a gentle vignette. Fixed camera, straight-on, slight top-down
tilt; only the paper objects move. Palette: coral #E8705A, blue #2F7FB8, teal #3BB1A8,
cream yellow #F4E6A6, ink navy #24243C, off-white card #F2EEE0.
Character: a paper-doll woman with black bob hair, coral jacket over a white top, blue
wide-leg trousers, cream shoes, round paper pins at shoulders, elbows and knees. She
stays on the right side of the frame and interacts with every prop (carries, pushes,
cuts, crumples, raises arms). Japanese text is heavy black gothic type (Noto Sans JP
Black), also cut from paper with thickness and shadow. Text pops in with a bouncy
overshoot (scale 0 → 1.1 → 1.0) or unfolds like an accordion. No hard cuts: every
transition is a paper gesture (ribbon wipe, folding screen, crumple, page fold).
Aspect ratio 7:4 (1260x720), 24fps, 14.4 seconds. No narration; upbeat playful
BGM with paper foley (rustle, stamp, snip, crumple) on each beat.
```

---

## 2. フルプロンプト（14.4秒・1本用）

### SHOT-BY-SHOT EFFECTS TIMELINE

```
SHOT 1 (00:00.0–00:00.85) — Paper Note Drop
• EFFECT: Object drop-in (gravity settle) + character slide-in
• A small white paper note reading "AI UPDATE" flutters down from the top-left, rocks
  once and settles slightly tilted (approx -12°). The paper-doll woman jogs in from the
  right edge with a bobbing walk cycle, arms swinging.
• Camera fixed, straight-on. Empty cream paper background.
• Note lands at 0.4s; character reaches center-right at 0.85s.
• Exits by the note being covered by the stamp in SHOT 2.

SHOT 2 (00:00.85–00:01.45) — Stamp and Burst
• EFFECT: Impact slam (scale 1.6 → 1.0 with squash) + starburst reveal + paper confetti
• A coral rubber stamp slams down from above onto the note. On impact, a large white
  starburst speech bubble (sawtooth edge, 16 points) pops out behind it and the note
  is replaced by the burst reading "朗報！" in heavy black type.
• Small paper flecks fly outward and fall; the character does a small jump on impact.
• Slam lands at 1.0s; burst fully visible at 1.2s; hold to 1.45s.
• Exits by the burst flipping down and folding into a strip for SHOT 3.

SHOT 3 (00:01.45–00:02.95) — Accordion Announcement Cards
• EFFECT: Accordion unfold (paper pleats opening) + fan stack (staggered rotation)
• A pleated strip of paper held by the character unfolds left-to-right into a wide white
  card reading "H3 Max Turbo登場" (two lines, heavy black gothic). 
• Behind it, 4-5 more cards with coral, teal and cream edges slide out and fan into a
  stack, each rotated 2-4° more than the last, like a hand of playing cards.
• The character pushes the stack with both hands, leaning into it.
• Unfold 1.45–1.85s; fan-out 1.85–2.3s; hold with a slight breathing wobble to 2.95s.
• Exits via the teal ribbon wipe in SHOT 4.

SHOT 4 (00:02.95–00:03.30) — Ribbon Wipe Transition
• EFFECT: Wipe transition (paper ribbon) — 0.35 seconds
• The character grabs the end of a wide teal paper ribbon and pulls it across the whole
  frame from right to left; the ribbon covers the cards and reveals an empty background.
• Motion blur on the ribbon, slight curl at its leading edge.

SHOT 5 (00:03.30–00:04.60) — Stopwatch, Speed x2
• EFFECT: Prop entrance + speed lines + staggered text pop + hand sweep
• A large dark-navy paper stopwatch rolls in from the left and the character catches
  it. Short horizontal speed lines streak to the left of the watch.
• "速度" pops in above-left (scale overshoot), then "2倍" pops in below it, larger,
  0.25s later. The coral second hand sweeps one full clockwise revolution.
• Watch enters 3.3–3.6s; "速度" at 3.75s; "2倍" at 4.0s; hand sweep 3.9–4.5s.
• Exits by the watch sliding right off-frame while the coral sheet enters from the left.

SHOT 6 (00:04.60–00:05.65) — Scissors Cut
• EFFECT: Prop entrance + path-following cut + piece separation
• A large coral rectangle of paper (a price tag before it is shaped) slides in from the
  left with a dotted cut line across its middle. Oversized grey paper scissors held by
  the character open and close 4 times, moving right-to-left along the dotted line.
• The cut edge shows a zig-zag paper tear. This is the SIGNATURE VISUAL EFFECT of the
  middle section.
• Scissors start 4.9s, finish cut 5.55s.

SHOT 7 (00:05.65–00:06.75) — Cost Half Tag
• EFFECT: Piece drop + shape morph + secondary card pop + character kick
• The lower half of the coral paper falls away and tumbles; the remaining half snaps
  into a classic price-tag shape (pointed top with a hole and string) reading "コスト半分".
• A small white card pops in at the upper right reading "768p | 1秒" over "$0.01".
• The character kicks the fallen scrap, which slides off-frame.
• Tag forms 5.65–5.9s; card pops 5.9s; kick 6.3–6.7s.
• Exits by the tag flipping backward and folding into the picture frames of SHOT 8.

SHOT 8 (00:06.75–00:08.85) — Quality Almost Unchanged
• EFFECT: Folding-screen unfold (rotate on vertical hinge) + typewriter text + subtle wobble
• Two dark-framed paper pictures unfold like a folding screen: left panel first, right
  panel swings open from its hinge. Both show the same paper landscape — a coral sun,
  blue hill, cream cloud, dark tree silhouette — the right one slightly cropped and
  shifted to imply "almost the same".
• The character steadies the right panel with one hand. The right panel rocks gently
  (approx 3°) back and forth.
• "品質 ほぼそのまま" types in below, one character every ~60ms, starting 7.35s.
• Frames open 6.75–7.3s; text 7.35–7.95s; hold to 8.85s.
• Exits as the character grabs the frames and crumples them.

SHOT 9 (00:08.85–00:10.20) — Crumple and Toss
• EFFECT: Crumple morph (paper collapses into a ball) + roll + physics knock-over
• The frames crumple in the character's hands into a wrinkled off-white paper ball.
  A coral paper waste bin with a lid appears at the lower right.
• The ball rolls right along the floor, bounces once, hits the bin, and the bin tips
  over. The character steps out of frame to the right.
• Crumple 8.85–9.1s; roll 9.3–10.0s; bin tips 10.0–10.2s.
• Exits via the paper unfolding out of the bin in SHOT 10.

SHOT 10 (00:10.20–00:12.10) — Promo CTA Card
• EFFECT: Unfold reveal + character pop-up + ribbon swirl (path draw)
• A sheet of cream-yellow paper unfolds out of the tipped bin and flattens into a
  rounded CTA card: small line "期間限定プロモーション" with a coral underline, big line
  "今すぐ試す" with a teal underline. A teal paper pen cup with a pencil sits at the
  right of the card.
• The character pops up from behind the card, both arms raised, with a small hop.
• A coral ribbon curls around from the left and a teal ribbon from the right, drawing
  themselves along their paths and settling with a slight sway.
• Unfold 10.2–10.55s; character pop 10.6s; ribbons 10.9–11.6s; hold to 12.1s.
• Exits by the page fold in SHOT 11.

SHOT 11 (00:12.10–00:12.40) — Page Fold Transition
• EFFECT: Fold transition (page turns over its vertical center) — 0.3 seconds
• The whole scene is a sheet of paper that folds over from the center, back-side
  showing plain cream, wiping everything away and revealing the end card.

SHOT 12 (00:12.40–00:14.40) — Logo End Card
• EFFECT: Static hold (no effects)
• Plain cream paper background. Heavy dark-navy sans-serif wordmark "H3 MAX TURBO"
  centered, slightly above the vertical middle. Nothing moves for 2 seconds.
• Audio drops to silence at 13.0s.
```

### MASTER EFFECTS INVENTORY

```
1. Object drop-in / gravity settle — used 2x (Shots 1, 7) — props land and rock once.
2. Impact slam with squash — used 1x (Shot 2) — the stamp; the loudest beat of the opening.
3. Starburst reveal — used 1x (Shot 2) — the "朗報！" bubble.
4. Paper confetti / flecks — used 2x (Shots 2, 6) — small pieces scatter on impact and cut.
5. Accordion unfold — used 2x (Shots 3, 10) — pleated paper opens into a flat card.
6. Fan stack (staggered rotation) — used 1x (Shot 3) — cards spread like a hand of cards.
7. Ribbon wipe — used 1x (Shot 4) — teal ribbon transition.
8. Speed lines — used 1x (Shot 5) — horizontal streaks behind the stopwatch.
9. Bouncy text pop (scale overshoot) — used 5x (Shots 2, 5, 7, 10) — every headline.
10. Hand sweep — used 1x (Shot 5) — stopwatch second hand rotates 360°.
11. Path-following cut — used 1x (Shot 6) — scissors along the dotted line. SIGNATURE.
12. Shape morph — used 2x (Shots 7, 9) — rectangle to tag; frames to crumpled ball.
13. Folding-screen unfold — used 1x (Shot 8) — hinged panels swing open.
14. Typewriter text — used 1x (Shot 8) — "品質 ほぼそのまま".
15. Idle wobble / breathing — used 3x (Shots 3, 8, 10) — held objects rock 2-3°.
16. Roll + knock-over physics — used 1x (Shot 9) — ball rolls and tips the bin.
17. Character pop-up — used 1x (Shot 10) — arms-raised hop from behind the card.
18. Ribbon swirl (path draw) — used 1x (Shot 10) — two ribbons draw along curved paths.
19. Page fold transition — used 1x (Shot 11) — sheet folds over to reveal end card.
20. Static hold — used 1x (Shot 12) — logo.
```

### EFFECTS DENSITY MAP

```
00:00–00:03 = HIGH DENSITY (drop-in, slide-in, slam, starburst, confetti, accordion, fan stack — 7 effects in 3s)
00:03–00:06 = MEDIUM DENSITY (ribbon wipe, speed lines, text pop x2, hand sweep, path cut — 6 effects in 3s, evenly spaced)
00:06–00:09 = MEDIUM DENSITY (piece drop, shape morph, card pop, folding screen, typewriter, wobble — 6 effects in 3s)
00:09–00:12 = MEDIUM DENSITY (crumple morph, roll, knock-over, unfold, pop-up, ribbon swirl — 6 effects in 3s)
00:12–00:14.4 = LOW DENSITY (page fold, then a static logo hold — 1 effect in 2.4s)
```

### ENERGY ARC

```
Act 1 (0–3s) — Attention grab: three quick beats (note drops, stamp slams, cards fan)
  each louder than the last. The character's jump on the stamp is the emotional peak.
Act 2 (3–10.2s) — Three benefits at a steady march: speed, cost, quality. Each beat
  uses the same grammar (prop enters → headline pops → character reacts) for 1.1–2.1s,
  so the viewer learns the rhythm and reads faster. The scissors cut is the signature
  moment; the crumple-and-toss is the release that clears the stage.
Act 3 (10.2–14.4s) — Landing: the CTA card gets the most decoration (ribbons, pop-up)
  then a single page fold drops everything to a silent logo. Two seconds of stillness
  lets the wordmark register.
```

---

## 3. 分割プロンプト（4〜5秒ずつ3本に分けて生成する場合）

生成モデルが1回で14秒を作れない場合は、スタイル定義＋以下のいずれかを1本ずつ生成します。各パートの末尾と次パートの先頭が同じ「紙の転換」で終わる／始まるようにしてあるので、つなぎ目が目立ちません。

### Part A（0.0–4.6s）導入〜速度2倍

```
[STYLE 定義を貼る]
SEQUENCE (4.6s): A white note reading "AI UPDATE" flutters down and lands tilted; the
paper-doll woman jogs in from the right. A coral rubber stamp slams onto it and a white
sawtooth starburst reading "朗報！" bursts out with paper flecks; she hops. She unfolds a
pleated strip into a wide white card "H3 Max Turbo登場", and coral/teal/cream-edged cards
fan out behind it as she pushes the stack. She grabs a teal ribbon and pulls it across the
frame right-to-left, wiping to empty paper. A navy paper stopwatch rolls in from the left
with speed lines; "速度" then "2倍" pop in with a bounce; the coral hand sweeps a full turn.
```

### Part B（4.6–10.2s）コスト半分〜品質〜片付け

```
[STYLE 定義を貼る]
SEQUENCE (5.6s): A coral paper rectangle with a dotted line slides in from the left. The
woman cuts along the line with oversized grey paper scissors, four snips, right to left.
The lower half tumbles away; the remainder snaps into a price tag with a string reading
"コスト半分". A small white card "768p | 1秒 $0.01" pops in at the upper right; she kicks
the scrap off-frame. The tag flips back and two dark-framed paper landscapes (coral sun,
blue hill, cream cloud, dark tree) unfold like a folding screen; the right panel rocks
gently while "品質 ほぼそのまま" types in below. She grabs both frames and crumples them
into a wrinkled paper ball, rolls it right into a coral waste bin, which tips over; she
walks off to the right.
```

### Part C（10.2–14.4s）CTA〜ロゴ

```
[STYLE 定義を貼る]
SEQUENCE (4.2s): Cream-yellow paper unfolds out of the tipped bin into a rounded card:
small line "期間限定プロモーション" with a coral underline, big line "今すぐ試す" with a
teal underline, a teal pen cup with a pencil beside it. The woman pops up from behind the
card with both arms raised. A coral ribbon curls in from the left and a teal ribbon from
the right, drawing along their paths. The whole scene folds over like a page turning on
its vertical center, revealing plain cream paper with a heavy navy wordmark "H3 MAX TURBO"
centered. Hold completely still for 2 seconds.
```

---

## 4. 参照画像の使い方

`frames/` の以下の3枚をスタイル参照として渡すと、色・質感・キャラクターが安定します。

| ファイル | 用途 |
|---|---|
| `frames/05_2.50s.jpg` | キャラクターとカードの質感（紙の厚み・影） |
| `frames/10_5.90s.jpg` | 主役色コーラルと極太ゴシック文字の見え方 |
| `frames/16_11.40s.jpg` | CTAカードとリボンの色構成 |

Higgsfield の場合：`generate_video` で `hf_mult_motion_control`（動きの転写）を使うなら、元動画そのものを driving video として渡し、上の Part A〜C を各パートのテキストにしてください。
