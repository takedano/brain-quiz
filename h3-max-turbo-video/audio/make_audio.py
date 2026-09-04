# -*- coding: utf-8 -*-
"""
BGM と効果音を自動で作って、動画に乗せるスクリプト。
外部の音源ファイルは一切使わず、すべてこのスクリプトが合成する（権利の心配なし）。

使い方:
  python3 make_audio.py                      # bgm.wav / sfx.wav / mix.wav を書き出す
  python3 make_audio.py --video in.mp4       # in.mp4 に音を乗せて in_with_audio.mp4 を作る
  python3 make_audio.py --video in.mp4 --bgm my_free_track.mp3   # BGM だけ手持ちのフリー素材に差し替える

必要なもの: numpy, imageio-ffmpeg（pip install numpy imageio-ffmpeg）
"""
import argparse, math, os, subprocess, wave
import numpy as np

SR = 44100
DUR = 14.4          # 元動画と同じ尺
BPM = 120
BEAT = 60 / BPM     # 0.5 秒

# ---------------------------------------------------------------- 基本部品
def t_axis(sec):
    return np.arange(int(SR * sec)) / SR

def env(n, a=0.005, d=0.15, s=0.0, r=0.05, sustain_len=0.0):
    """ADSR っぽい簡易エンベロープ"""
    a_n, d_n, r_n = int(a*SR), int(d*SR), int(r*SR)
    s_n = max(0, n - a_n - d_n - r_n)
    parts = [np.linspace(0, 1, a_n, endpoint=False),
             np.linspace(1, s, d_n, endpoint=False),
             np.full(s_n, s),
             np.linspace(s, 0, r_n)]
    e = np.concatenate(parts)[:n]
    if len(e) < n: e = np.pad(e, (0, n - len(e)))
    return e

def tone(freq, sec, kind="sine", harmonics=(1.0,)):
    t = t_axis(sec); out = np.zeros_like(t)
    for i, amp in enumerate(harmonics, start=1):
        out += amp * np.sin(2*np.pi*freq*i*t)
    return out / max(1e-9, sum(abs(a) for a in harmonics))

def noise(sec):
    return np.random.default_rng(int(sec*1e6) % 2**32).uniform(-1, 1, int(SR*sec))

def bandpass(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1/SR)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, n=len(x))

def place(buf, sound, at, gain=1.0):
    i = int(at * SR)
    if i >= len(buf): return
    seg = sound[:len(buf)-i]
    buf[i:i+len(seg)] += gain * seg

# ---------------------------------------------------------------- 楽器
def glock(freq, sec=0.6):
    x = tone(freq, sec, harmonics=(1.0, 0.0, 0.25, 0.0, 0.08)) * env(int(SR*sec), a=0.002, d=0.5, s=0.0, r=0.05)
    return x

def uke(freq, sec=0.35):
    x = tone(freq, sec, harmonics=(1.0, 0.6, 0.35, 0.2)) * env(int(SR*sec), a=0.003, d=0.3, s=0.0, r=0.03)
    return x

def sleigh(sec=0.18):
    x = bandpass(noise(sec), 5000, 11000) * env(int(SR*sec), a=0.002, d=0.15, s=0.0, r=0.02)
    return x

def clap(sec=0.12):
    x = bandpass(noise(sec), 1200, 4000) * env(int(SR*sec), a=0.001, d=0.1, s=0.0, r=0.01)
    return x

NOTE = {n: 440*2**((i-9)/12) for i, n in enumerate(["C4","C#4","D4","D#4","E4","F4","F#4","G4","G#4","A4","A#4","B4"])}
def f(name, octave_shift=0):
    return NOTE[name] * 2**octave_shift

# ---------------------------------------------------------------- BGM
def make_bgm():
    buf = np.zeros(int(SR*DUR))
    # 0-1s: ピックアップのそり鈴ひと振り
    for k in range(3): place(buf, sleigh(), 0.15 + k*0.09, 0.5)
    # 1-10s: 4小節ループ ×2 ＋ 12s まで
    # ウクレレのコード進行 C - G - Am - F（1小節=2秒、8分刻みでストラム）
    chords = [("C4","E4","G4"), ("G4","B4","D4"), ("A4","C4","E4"), ("F4","A4","C4")]
    t = 1.0
    bar = 0
    while t < 12.0 - 1e-6:
        ch = chords[bar % 4]
        for e in range(8):                       # 8分音符 ×8 = 1小節（2秒）
            at = t + e*BEAT/2
            if at >= 12.0: break
            g = 0.55 if e % 2 == 0 else 0.35
            for j, n in enumerate(ch):
                place(buf, uke(f(n, -1 if j == 0 else 0), 0.3), at + j*0.012, g*0.28)
        # そり鈴：各拍
        for b in range(4):
            place(buf, sleigh(), t + b*BEAT, 0.42 if b % 2 == 0 else 0.3)
        # 手拍子：2拍目・4拍目
        for b in (1, 3):
            place(buf, clap(), t + b*BEAT, 0.35)
        t += 2.0; bar += 1
    # 鉄琴のメロディ（ヨナ抜き音階でほんのり和風）: 各小節に4音
    melody = [["E4","G4","A4","C4+"], ["D4","B4","G4","D4"], ["C4+","A4","E4","G4"], ["A4","C4+","A4","G4"]]
    t = 1.0; bar = 0
    while t < 10.0 - 1e-6:
        for k, n in enumerate(melody[bar % 4]):
            name, up = (n[:-1], 1) if n.endswith("+") else (n, 0)
            place(buf, glock(f(name, up+1), 0.55), t + k*BEAT, 0.5)
        t += 2.0; bar += 1
    # 10-12s: 上昇ビルド
    for k, n in enumerate(["C4","E4","G4","C4","E4","G4","C4","E4"]):
        place(buf, glock(f(n, 1 + k//3), 0.4), 10.0 + k*0.22, 0.45)
    # 12s: 全音符コード（伸ばし）
    for j, n in enumerate(("C4","E4","G4","C4")):
        x = tone(f(n, 1 if j < 3 else 2), 1.2, harmonics=(1.0,0.4,0.2)) * env(int(SR*1.2), a=0.01, d=0.2, s=0.6, r=0.6)
        place(buf, x, 12.0, 0.22)
    # 12.6s: 最後のチャイム → 無音
    place(buf, glock(f("C4", 3), 1.4), 12.6, 0.6)
    place(buf, glock(f("G4", 2), 1.4), 12.62, 0.35)
    for k in range(3): place(buf, sleigh(), 12.6 + k*0.07, 0.4)
    buf[int(SR*13.6):] *= np.linspace(1, 0, len(buf) - int(SR*13.6))
    return buf

# ---------------------------------------------------------------- 効果音
def sfx_paper_fall(sec=0.5):
    return bandpass(noise(sec), 800, 4000) * env(int(SR*sec), a=0.05, d=0.3, s=0.2, r=0.15) * np.linspace(0.6, 1.0, int(SR*sec))

def sfx_stamp():
    sec = 0.25; t = t_axis(sec)
    thump = np.sin(2*np.pi*(90 - 60*t/sec)*t) * env(int(SR*sec), a=0.002, d=0.15, s=0.0, r=0.05)
    click = bandpass(noise(0.03), 2000, 6000) * env(int(SR*0.03), a=0.001, d=0.02, s=0, r=0.005)
    out = thump.copy(); out[:len(click)] += 0.5*click
    return out

def sfx_pop(pitch=1.0):
    sec = 0.12; t = t_axis(sec)
    x = np.sin(2*np.pi*(420*pitch + 380*pitch*np.exp(-t*40))*t) * env(int(SR*sec), a=0.002, d=0.1, s=0, r=0.01)
    return x

def sfx_confetti(sec=0.5):
    out = np.zeros(int(SR*sec))
    rng = np.random.default_rng(7)
    for _ in range(18):
        at = rng.uniform(0, sec-0.05); l = 0.04
        place(out, bandpass(noise(l), 1500, 7000) * env(int(SR*l), a=0.002, d=0.03, s=0, r=0.005), at, 0.5)
    return out

def sfx_accordion(sec=0.4):
    out = np.zeros(int(SR*sec))
    for k in range(6):
        l = 0.06
        place(out, bandpass(noise(l), 900, 3500) * env(int(SR*l), a=0.005, d=0.04, s=0, r=0.01), k*sec/6, 0.7)
    return out

def sfx_swoosh(sec=0.35):
    t = t_axis(sec)
    x = bandpass(noise(sec), 600, 5000) * np.sin(np.pi*t/sec)**2
    return x

def sfx_crayon(sec=0.5):
    out = np.zeros(int(SR*sec))
    for k in range(3):
        l = 0.14
        place(out, bandpass(noise(l), 300, 2500) * env(int(SR*l), a=0.02, d=0.1, s=0.3, r=0.02), k*0.16, 0.8)
    return out

def sfx_snip():
    l = 0.09; t = t_axis(l)
    a = bandpass(noise(l), 2500, 9000) * env(int(SR*l), a=0.001, d=0.05, s=0, r=0.01)
    b = np.sin(2*np.pi*3200*t) * env(int(SR*l), a=0.001, d=0.03, s=0, r=0.005) * 0.4
    return a + b

def sfx_type():
    l = 0.05
    return bandpass(noise(l), 2000, 7000) * env(int(SR*l), a=0.001, d=0.03, s=0, r=0.005)

def sfx_fold(sec=0.25):
    return bandpass(noise(sec), 500, 3000) * env(int(SR*sec), a=0.03, d=0.15, s=0.2, r=0.05)

def sfx_thud():
    sec = 0.2; t = t_axis(sec)
    return np.sin(2*np.pi*(140 - 80*t/sec)*t) * env(int(SR*sec), a=0.002, d=0.12, s=0, r=0.05)

def sfx_chime():
    return 0.7*glock(f("C4", 3), 1.4) + 0.4*glock(f("E4", 3), 1.4)

# 効果音の入れどころ（prompts.md の表と同じ秒数）
CUES = [
    (0.40, "paper_fall"), (1.00, "stamp"), (1.20, "pop"), (1.22, "confetti"),
    (1.50, "accordion"), (1.90, "accordion"), (3.00, "swoosh"),
    (3.60, "crayon"), (3.75, "pop"), (4.00, "pop_low"), (4.20, "pop_high"),
    (4.90, "snip"), (5.08, "snip"), (5.26, "snip"), (5.44, "snip"),
    (5.90, "pop_high"), (6.80, "accordion"), (7.00, "accordion"),
    (7.35, "type"), (7.41, "type"), (7.47, "type"), (7.53, "type"), (7.59, "type"), (7.65, "type"), (7.71, "type"), (7.77, "type"), (7.83, "type"), (7.89, "type"),
    (8.90, "fold"), (9.05, "fold"), (10.00, "thud"), (10.05, "sleigh"),
    (10.30, "fold"), (10.60, "pop"), (10.64, "pop_high"), (12.20, "fold"), (13.00, "chime"),
]
def make_sfx():
    buf = np.zeros(int(SR*DUR))
    bank = {
        "paper_fall": lambda: sfx_paper_fall(), "stamp": sfx_stamp, "pop": lambda: sfx_pop(1.0),
        "pop_low": lambda: sfx_pop(0.8), "pop_high": lambda: sfx_pop(1.3), "confetti": lambda: sfx_confetti(),
        "accordion": lambda: sfx_accordion(), "swoosh": lambda: sfx_swoosh(), "crayon": lambda: sfx_crayon(),
        "snip": sfx_snip, "type": sfx_type, "fold": lambda: sfx_fold(), "thud": sfx_thud,
        "sleigh": lambda: np.concatenate([sleigh(), sleigh(), sleigh()]), "chime": sfx_chime,
    }
    gains = {"stamp": 1.0, "thud": 0.9, "chime": 0.9, "snip": 0.7, "type": 0.35, "confetti": 0.5}
    for at, name in CUES:
        place(buf, bank[name](), at, gains.get(name, 0.7))
    return buf

# ---------------------------------------------------------------- 書き出し
def normalize(x, peak=0.89):
    m = np.max(np.abs(x)) or 1.0
    return x / m * peak

def write_wav(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())

def ffmpeg():
    try:
        import imageio_ffmpeg; return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", help="音を乗せたい動画（mp4）")
    ap.add_argument("--bgm", help="手持ちのフリー素材BGMを使う場合のファイル（mp3/wav）。省略時は合成する")
    ap.add_argument("--out", help="出力先ディレクトリ", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--bgm-gain", type=float, default=0.55)
    ap.add_argument("--sfx-gain", type=float, default=0.9)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    sfx = normalize(make_sfx())
    write_wav(os.path.join(a.out, "sfx.wav"), sfx)
    if a.bgm:
        # 手持ちのBGMを 14.4 秒にトリムして 13.0 秒からフェードアウト
        tmp = os.path.join(a.out, "bgm_trimmed.wav")
        subprocess.run([ffmpeg(), "-loglevel", "error", "-y", "-i", a.bgm, "-t", str(DUR), "-ac", "1", "-ar", str(SR),
                        "-af", "afade=t=out:st=12.6:d=0.8", tmp], check=True)
        with wave.open(tmp) as w:
            bgm = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32767
        bgm = np.pad(bgm, (0, max(0, len(sfx) - len(bgm))))[:len(sfx)]
    else:
        bgm = normalize(make_bgm())
        write_wav(os.path.join(a.out, "bgm.wav"), bgm)
    mix = normalize(a.bgm_gain * bgm + a.sfx_gain * sfx, 0.95)
    mix_path = os.path.join(a.out, "mix.wav")
    write_wav(mix_path, mix)
    print("wrote", mix_path)

    if a.video:
        base, _ = os.path.splitext(os.path.basename(a.video))
        outv = os.path.join(a.out, base + "_with_audio.mp4")
        subprocess.run([ffmpeg(), "-loglevel", "error", "-y", "-i", a.video, "-i", mix_path,
                        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", outv], check=True)
        print("wrote", outv)

if __name__ == "__main__":
    main()
