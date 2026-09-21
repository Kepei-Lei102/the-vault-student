"""Affective Computing — seven experiments you can run.

A machine never measures a feeling.  It measures a signal (a face, a voice, some text, a sweaty palm) and
INFERS.  Each experiment below takes one link of that chain and measures how much it can carry.
The people and signals are synthetic models, stated as such; the arithmetic is real.

1. voices()            — synthesises four short "utterances" (calm, sad, angry, joyful) as WAV files, extracts
                         pitch and loudness from the audio, and classifies.  Arousal is easy to hear;
                         anger and joy are nearly indistinguishable from prosody.
2. text()              — a lexicon sentiment scorer on forty sentences: fine on plain statements, poor on
                         negation and sarcasm.
3. skin()              — skin conductance: a slow drift plus a sharp response after each arousing event.
                         The events are found from the signal; whether each was delight or dread is not in it.
4. smile_is_not_joy()  — Bayes: a detector that finds SMILES with 99 % accuracy, asked about HAPPINESS.
5. who_gets_misread()  — a classifier trained on one group's faces, applied to a group whose resting
                         face differs slightly: whose neutral expression gets called angry?
6. screening()         — a 95 %-accurate "about to be violent" detector pointed at 10 000 employees.
7. what_leaves_the_device() — a minute of video against a minute of derived numbers.

Run:  python3 affective-computing-lab.py      (numpy + standard library; writes four WAV files beside this script)
"""
import os
import wave

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(1995)
RATE = 22_050

# typical prosody, after the patterns reported by Scherer and others: (mean pitch Hz, pitch range Hz, syllables per second, loudness)
PROSODY = {"calm": (120, 15, 3.5, 0.35), "sad": (105, 8, 2.6, 0.22), "angry": (175, 60, 5.2, 0.85), "joyful": (185, 70, 5.0, 0.75)}
AROUSAL = {"calm": 0, "sad": 0, "angry": 1, "joyful": 1}
VALENCE = {"calm": 1, "sad": 0, "angry": 0, "joyful": 1}


# ------------------------------------------------------------------ 1. voice
def utterance(f0, f_range, rate, loud, seconds=2.4, jitter=0.0):
    """A hummed 'sentence': syllable-shaped loudness, a pitch contour that rises and falls, five harmonics."""
    t = np.arange(int(seconds * RATE)) / RATE
    f0 = f0 * (1 + jitter * rng.normal()); f_range = max(2.0, f_range * (1 + jitter * rng.normal())); rate = rate * (1 + jitter * rng.normal()); loud = np.clip(loud * (1 + jitter * rng.normal()), 0.05, 0.95)
    contour = f0 + f_range * (0.6 * np.sin(2 * np.pi * 0.45 * t + 0.4) + 0.4 * np.sin(2 * np.pi * rate / 2 * t))
    phase = 2 * np.pi * np.cumsum(contour) / RATE
    voice = sum(a * np.sin(k * phase) for k, a in ((1, 1.0), (2, 0.55), (3, 0.35), (4, 0.2), (5, 0.12)))
    syllables = 0.5 * (1 - np.cos(2 * np.pi * rate * t)) ** 1.5
    fade = np.minimum(1, np.minimum(t, seconds - t) / 0.05)
    y = voice / np.abs(voice).max() * syllables * fade * loud
    return y


def features(y):
    """Pitch by autocorrelation on voiced frames, plus loudness and syllable rate: what a prosody model sees."""
    frame, hop = 1024, 512
    pitches, energies = [], []
    for i in range(0, len(y) - frame, hop):
        w = y[i:i + frame] * np.hanning(frame); e = float(np.sqrt((w * w).mean())); energies.append(e)
        if e < 0.02:
            continue
        ac = np.correlate(w, w, "full")[frame - 1:]
        lo, hi = RATE // 400, RATE // 70
        lag = lo + int(np.argmax(ac[lo:hi])); pitches.append(RATE / lag)
    en = np.array(energies); env = en - en.mean()
    crossings = np.sum((env[:-1] < 0) & (env[1:] >= 0)) / (len(y) / RATE)
    return np.array([np.mean(pitches), np.std(pitches), en.mean() * 10, crossings])


def voices(n_per_class=60):
    for name, p in PROSODY.items():
        y = utterance(*p)
        with wave.open(os.path.join(HERE, f"affective-voice-{name}.wav"), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes((y * 32767).astype(np.int16).tobytes())
        f = features(y)
        print(f"  wrote affective-voice-{name}.wav   measured pitch {f[0]:5.0f} Hz, pitch spread {f[1]:4.0f} Hz, loudness {f[2]:.2f}, syllables/s {f[3]:.1f}")
    X, lab = [], []
    for name, p in PROSODY.items():
        for _ in range(n_per_class):
            X.append(features(utterance(*p, seconds=1.6, jitter=0.16))); lab.append(name)
    X = np.array(X); lab = np.array(lab); names = list(PROSODY)
    idx = rng.permutation(len(X)); tr, te = idx[: len(X) * 2 // 3], idx[len(X) * 2 // 3:]
    mu, sd = X[tr].mean(0), X[tr].std(0); Z = (X - mu) / sd
    cents = {n: Z[tr][lab[tr] == n].mean(0) for n in names}                          # nearest-centroid classifier
    pred = np.array([min(names, key=lambda n: np.linalg.norm(z - cents[n])) for z in Z[te]])
    conf = np.array([[np.sum((lab[te] == a) & (pred == b)) for b in names] for a in names])
    print("  confusion matrix (rows: what was spoken; columns: what the classifier said)   " + "  ".join(f"{n:>6s}" for n in names))
    for n, row in zip(names, conf):
        print(f"    {n:>6s}  " + "  ".join(f"{v:6d}" for v in row))
    acc = np.trace(conf) / conf.sum()
    ar = np.mean([AROUSAL[a] == AROUSAL[b] for a, b in zip(lab[te], pred)]); va = np.mean([VALENCE[a] == VALENCE[b] for a, b in zip(lab[te], pred)])
    print(f"  four-way accuracy {100*acc:.0f} %;  excited-or-not {100*ar:.0f} %;  pleasant-or-not {100*va:.0f} %")
    print("  the voice carries AROUSAL.  Whether the excitement is rage or delight is mostly not in the pitch and loudness.")
    return names, conf


# ------------------------------------------------------------------ 2. text
LEXICON = {"love": 2, "great": 2, "wonderful": 2, "happy": 2, "brilliant": 2, "perfect": 2, "thanks": 1, "good": 1, "enjoyed": 2, "best": 2, "fantastic": 2, "pleased": 1,
           "hate": -2, "awful": -2, "terrible": -2, "sad": -2, "angry": -2, "worst": -2, "boring": -1, "broken": -1, "failed": -2, "annoying": -2, "useless": -2, "disappointed": -2}
SENTENCES = [  # (text, true polarity, kind)
    ("I love this phone", 1, "plain"), ("The food was wonderful", 1, "plain"), ("What a great lesson", 1, "plain"), ("I am so happy today", 1, "plain"),
    ("The film was brilliant", 1, "plain"), ("Thanks, that was perfect", 1, "plain"), ("We enjoyed every minute", 1, "plain"), ("Best holiday ever", 1, "plain"),
    ("The service was fantastic", 1, "plain"), ("I am pleased with the result", 1, "plain"),
    ("I hate waiting", -1, "plain"), ("The hotel was awful", -1, "plain"), ("A terrible idea", -1, "plain"), ("I feel sad about it", -1, "plain"),
    ("He was angry with me", -1, "plain"), ("The worst meal of my life", -1, "plain"), ("The lecture was boring", -1, "plain"), ("My screen is broken", -1, "plain"),
    ("The update failed again", -1, "plain"), ("This app is useless", -1, "plain"),
    ("I do not love this phone", -1, "negation"), ("The food was not good", -1, "negation"), ("It was never boring", 1, "negation"), ("I am not happy", -1, "negation"),
    ("Not the worst I have seen", 1, "negation"), ("I can't say I enjoyed it", -1, "negation"), ("Nothing was broken", 1, "negation"), ("It was hardly perfect", -1, "negation"),
    ("He is not angry any more", 1, "negation"), ("It didn't fail this time", 1, "negation"),
    ("Oh great, another Monday test", -1, "sarcasm"), ("Wonderful, my train is cancelled", -1, "sarcasm"), ("I just love being ignored", -1, "sarcasm"), ("Perfect, it crashed again", -1, "sarcasm"),
    ("Thanks for nothing", -1, "sarcasm"), ("Brilliant, now it won't turn on", -1, "sarcasm"), ("Yeah, best customer service ever, two hours on hold", -1, "sarcasm"),
    ("So happy to work all weekend", -1, "sarcasm"), ("Fantastic, more homework", -1, "sarcasm"), ("Good luck getting a refund", -1, "sarcasm"),
]


NEGATORS = {"not", "never", "no", "nothing", "hardly", "can't", "didn't", "don't", "won't", "isn't"}


def score(text, handle_negation=False):
    words = [w.strip(",.!?").lower() for w in text.split()]
    total, flip = 0, 0
    for w in words:
        if handle_negation and w in NEGATORS:
            flip = 4                                          # a negator reverses sentiment words in the next few positions
            continue
        v = LEXICON.get(w, 0)
        total += -v if flip and v else v
        flip = max(0, flip - 1)
    return total


def text():
    out = {}
    for label, neg in (("word list only", False), ("word list + a negation rule", True)):
        print(f"  {label}")
        for kind in ("plain", "negation", "sarcasm"):
            rows = [(t, y) for t, y, k in SENTENCES if k == kind]
            right = sum((score(t, neg) > 0) == (y > 0) for t, y in rows)
            out[(label, kind)] = right / len(rows)
            print(f"    {kind:9s} {right:2d} of {len(rows)} correct")
    for t in ("Oh great, another Monday test", "It was never boring"):
        print(f"    '{t}'  scores {score(t):+d} by words alone, {score(t, True):+d} with the negation rule")
    print("  a rule repairs negation.  Nothing in the sentence repairs sarcasm: that needs to know what Mondays and tests are like.")
    return out


# ------------------------------------------------------------------ 3. skin conductance
def skin(seconds=120, fs=10):
    t = np.arange(0, seconds, 1 / fs)
    events = [(18, "a friend jumps out: fright"), (47, "a message: you won the prize"), (83, "called on in class"), (104, "the goal in extra time")]
    tonic = 4.0 + 0.004 * t + 0.15 * np.sin(2 * np.pi * t / 90)
    phasic = np.zeros_like(t)
    for t0, _ in events:
        u = np.clip(t - t0 - 1.5, 0, None)                                   # the response starts 1-2 s after the event
        phasic += 0.9 * (np.exp(-u / 4.0) - np.exp(-u / 0.7)) * (u > 0)
    x = tonic + phasic + rng.normal(0, 0.01, len(t))
    smooth = np.convolve(x, np.ones(5) / 5, "same"); slope = np.gradient(smooth, 1 / fs)
    found, last = [], -99
    for i in range(len(t)):
        if t[i] > 3 and slope[i] > 0.12 and t[i] - last > 8:                  # ignore the filter's start-up edge
            found.append(t[i]); last = t[i]
    print(f"  true events at {[e for e, _ in events]} s;  responses detected at {[round(float(f), 1) for f in found]} s")
    print("  two were delight and two were dread.  The four responses have the same shape: the palm reports HOW MUCH, never WHICH.")
    return t, x, events, found


# ------------------------------------------------------------------ 4. expression is not feeling
def smile_is_not_joy(p_happy=0.30, p_smile_if_happy=0.70, p_smile_if_not=0.30, detector=0.99):
    # illustrative rates: people smile when happy most but not all of the time, and smile for many other reasons
    p_flag_if_happy = p_smile_if_happy * detector + (1 - p_smile_if_happy) * (1 - detector)
    p_flag_if_not = p_smile_if_not * detector + (1 - p_smile_if_not) * (1 - detector)
    p_flag = p_happy * p_flag_if_happy + (1 - p_happy) * p_flag_if_not
    post = p_happy * p_flag_if_happy / p_flag
    acc = p_happy * p_flag_if_happy + (1 - p_happy) * (1 - p_flag_if_not)
    print(f"  the detector finds smiles with {100*detector:.0f} % accuracy")
    print(f"  P(happy | it says 'smiling') = {100*post:.0f} %;   used as a happiness detector its accuracy is {100*acc:.0f} %")
    print(f"  always answering 'not happy' would score {100*(1-p_happy):.0f} %.  The error is not in the camera; it is in the step from face to feeling.")
    return post, acc


# ------------------------------------------------------------------ 5. who gets misread
def faces(n, brow_rest, angry_rate=0.2):
    """Two facial measurements: brow lowering and lip-corner pull.  Anger lowers the brow by about 1 unit."""
    angry = rng.random(n) < angry_rate
    brow = brow_rest + 1.0 * angry + rng.normal(0, 0.35, n)
    lips = 0.0 - 0.3 * angry + rng.normal(0, 0.35, n)
    return np.column_stack([brow, lips]), angry


def who_gets_misread(n=20_000):
    Xa, ya = faces(n, brow_rest=0.0)                       # group A: the training data
    w = np.zeros(3)
    Xb_ = np.column_stack([Xa, np.ones(n)])
    for _ in range(400):                                   # logistic regression by gradient descent
        w -= 0.5 * Xb_.T @ (1 / (1 + np.exp(-Xb_ @ w)) - ya) / n
    out = {}
    for name, rest in (("group A (the training data)", 0.0), ("group B (resting brow sits 0.4 lower)", 0.4)):
        X, y = faces(n, brow_rest=rest)
        pred = (np.column_stack([X, np.ones(n)]) @ w) > 0
        fp = np.mean(pred[~y]); acc = np.mean(pred == y)
        out[name] = (acc, fp)
        print(f"  {name:40s} accuracy {100*acc:.1f} %;  calm faces labelled ANGRY: {100*fp:.1f} %")
    a, b = list(out.values())
    print(f"  the same software calls a calm face angry {b[1]/a[1]:.1f} times as often in group B.  Nothing about B's feelings differs: only the face at rest.")
    return out


# ------------------------------------------------------------------ 6. screening
def screening(people=10_000, prevalence=0.001, sensitivity=0.95, specificity=0.95):
    true = people * prevalence
    tp = true * sensitivity; fp = (people - true) * (1 - specificity)
    print(f"  {people} employees, {true:.0f} of whom are really about to be violent; the detector is {100*sensitivity:.0f} % right both ways")
    print(f"  it flags {tp + fp:.0f} people: {tp:.1f} correctly and {fp:.0f} wrongly.  A flag is right {100*tp/(tp+fp):.1f} % of the time.")
    return tp, fp


# ------------------------------------------------------------------ 7. data minimisation
def what_leaves_the_device():
    video = 60 * 2.5e6 / 8                                   # one minute of 720p video at a modest 2.5 Mbit/s
    derived = 60 * 2 * 4                                     # one (valence, arousal) pair per second, 4-byte floats
    print(f"  one minute of face video: {video/1e6:.0f} MB.  One minute of derived valence and arousal: {derived} bytes.  Ratio {video/derived:,.0f} : 1")
    print("  inferring on the device and sending only the derived numbers (or a federated model update under secure aggregation)")
    print("  removes the face from the server entirely.  It does not make the inference any more true.")


if __name__ == "__main__":
    for i, f in enumerate((voices, text, skin, smile_is_not_joy, who_gets_misread, screening, what_leaves_the_device), 1):
        print(f"\n{i}. {f.__name__.replace('_', ' ')}"); f()
