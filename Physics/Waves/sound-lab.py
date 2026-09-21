"""Sound — the numbers behind the card, and five sounds to listen to.

1. speed_vs_temperature()  — why the syllabus says "330–350 m/s" and not one number.
2. speeds_in_media()       — v = sqrt(stiffness / density) for air, water and steel: why
                             sound is fastest in the densest of the three.
3. measure_speed()         — four school methods for the speed of sound in air, each
                             simulated 20 000 times with a human or electronic timing error.
4. thunder()               — the three-seconds-per-kilometre rule.
5. write_sounds()          — WAV files beside this script: the same note quiet and loud,
                             the note an octave up, the same note with a different timbre,
                             and a 15 kHz tone that many adults cannot hear.

Run:  python3 sound-lab.py        (numpy + the standard library)
"""
import os
import wave

import numpy as np

rng = np.random.default_rng(343)
HERE = os.path.dirname(os.path.abspath(__file__))


def speed_in_air(theta_c):
    """Ideal-gas result v = sqrt(gamma R T / M), written relative to 0 °C."""
    return 331.3 * np.sqrt(1 + theta_c / 273.15)


def speed_vs_temperature():
    for th in (-10, 0, 15, 20, 35):
        print(f"  {th:4d} °C: {speed_in_air(th):6.1f} m/s")
    print("  every ordinary day on Earth lands inside 325–352 m/s; pressure does not appear in the formula at all")


def speeds_in_media():
    media = [("air (20 °C)",  1.40 * 101_325, 1.204,  "gamma × pressure"),
             ("water",        2.2e9,          998.0,  "bulk modulus"),
             ("steel rod",    200e9,          7850.0, "Young modulus")]
    v_air = None
    for name, stiff, rho, kind in media:
        v = np.sqrt(stiff / rho)
        v_air = v_air or v
        print(f"  {name:12s} stiffness {stiff:9.3g} Pa ({kind}), density {rho:7.1f} kg/m³  ->  v = {v:6.0f} m/s  ({v/v_air:4.1f} × air)")
    print("  steel is 6500 × denser than air but 1.4 million × stiffer: the stiffness wins")


def measure_speed(trials=20_000, v_true=343.0, reaction=0.10):
    def report(name, v):
        print(f"  {name:58s} {v.mean():6.0f} ± {v.std():5.0f} m/s  ({100*v.std()/v_true:5.1f} %)")
    # (a) see the cymbals clash, hear the crash, one hand stopwatch.  The error is in the TIME,
    #     so report the time: dividing a distance by a time that may be near zero is meaningless.
    for d in (60.0, 500.0):
        t_true = d / v_true
        t = t_true + rng.normal(0, reaction, trials) - rng.normal(0, reaction, trials)
        print(f"  see-then-hear over {d:3.0f} m, hand stopwatch: time {t_true:5.3f} ± {t.std():.3f} s, "
              f"so the speed is uncertain by {100*t.std()/t_true:5.1f} %")
    # (b) clap in rhythm with your own echo, 50 m from a wall, time 20 claps
    d, n = 50.0, 20
    interval = 2 * d / v_true                      # clap, echo, clap, echo...: claps coincide with echoes
    total = 2 * n * interval / 2 + rng.normal(0, reaction, trials) - rng.normal(0, reaction, trials)
    rhythm_err = rng.normal(0, 0.01, trials) * n    # you drift a little off the beat
    report("clap in time with the echo, 50 m wall, 20 claps", 2 * d * n / (total + rhythm_err))
    # (c) two microphones 1.00 m apart, electronic timer reading to 0.1 ms, ruler to 2 mm
    d = 1.00 + rng.normal(0, 0.002, trials)
    t = 1.00 / v_true + rng.uniform(-0.00005, 0.00005, trials)
    report("two microphones 1.00 m apart, timer to 0.1 ms", d / t)
    # (d) the same, 3.00 m apart
    d = 3.00 + rng.normal(0, 0.002, trials)
    t = 3.00 / v_true + rng.uniform(-0.00005, 0.00005, trials)
    report("two microphones 3.00 m apart, timer to 0.1 ms", d / t)
    print(f"  (true value {v_true:.0f} m/s; a hand stopwatch is wrong by ~0.14 s whatever you time, so time something long)")


def thunder():
    v = speed_in_air(20)
    print(f"  sound needs {1000/v:.2f} s per kilometre: count the seconds after the flash and divide by three")
    print(f"  the light covered the same kilometre in {1000/3e8*1e6:.1f} microseconds, which is why the flash counts as 'now'")


def tone(freq, amp, seconds=0.9, rate=44_100, harmonics=None):
    t = np.arange(int(seconds * rate)) / rate
    if harmonics is None:
        y = np.sin(2 * np.pi * freq * t)
    else:
        y = sum(a * np.sin(2 * np.pi * freq * k * t) for k, a in harmonics)
        y = y / np.abs(y).max()
    fade = np.minimum(1, np.minimum(t, seconds - t) / 0.03)        # no click at the ends
    return (amp * y * fade * 32767).astype(np.int16), rate


def write_sounds():
    files = {
        "sound-a440-quiet.wav":   tone(440, 0.12),
        "sound-a440-loud.wav":    tone(440, 0.85),
        "sound-a880-octave.wav":  tone(880, 0.85),
        "sound-a440-reedy.wav":   tone(440, 0.85, harmonics=[(1, 1.0), (2, 0.6), (3, 0.5), (4, 0.35), (5, 0.25), (6, 0.15)]),
        "sound-15khz.wav":        tone(15_000, 0.5),
    }
    for name, (data, rate) in files.items():
        with wave.open(os.path.join(HERE, name), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(data.tobytes())
        print(f"  wrote {name:24s} {len(data)/rate:.1f} s, {os.path.getsize(os.path.join(HERE, name))/1024:.0f} KB")
    print("  quiet and loud: same frequency, amplitude × 7, so intensity × 50 (about 17 dB)")


if __name__ == "__main__":
    print("1. speed of sound in air against temperature")
    speed_vs_temperature()
    print("\n2. speed in three media")
    speeds_in_media()
    print("\n3. four ways to measure it")
    measure_speed()
    print("\n4. thunder")
    thunder()
    print("\n5. sounds to listen to")
    write_sounds()
