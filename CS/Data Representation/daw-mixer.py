#!/usr/bin/env python3
"""Load the lab's three WAV stems, process, automate, pan, sum and bounce.
Run after daw-lab.py; optional first argument is an output directory.
"""
from pathlib import Path
import importlib.util
import sys
import numpy as np

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('dsp', here / 'daw-lab.py')
dsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dsp)
out = Path(sys.argv[1]) if len(sys.argv) > 1 else here
out.mkdir(parents=True, exist_ok=True)
stems = []
for name in ['keys', 'bass', 'drums']:
    fs, audio = dsp.read_wav(here / f'daw-stem-{name}.wav')
    assert fs == dsp.FS and audio.ndim == 1
    stems.append(audio)
keys, bass, drums = stems
assert len(keys) == len(bass) == len(drums)
t = np.arange(len(keys)) / fs
b, a = dsp.peaking_eq(fs, 1200, .8, -9)
keys_eq = dsp.Biquad(b, a).process(keys)
keys_comp, _ = dsp.Compressor().process(keys_eq)
automation_db = np.interp(t, [0, 2, 6, 8], [-3, 0, 0, -12])
keys_comp *= dsp.db_gain(automation_db)
dry = dsp.pan(keys, -.3) + dsp.pan(bass, 0) + dsp.pan(drums, .25)
mix = dsp.pan(keys_comp, -.3) + dsp.pan(bass, 0) + dsp.pan(drums, .25)
wet = dsp.convolution(keys_comp, dsp.room_ir())
wet *= .25 * dsp.rms(keys_comp) / max(dsp.rms(wet), 1e-12)
mix = np.pad(mix, ((0, len(wet)-len(mix)), (0, 0))) + wet
dry = np.pad(dry, ((0, len(mix)-len(dry)), (0, 0)))
common_gain = min(1., .80 / max(np.max(abs(dry)), np.max(abs(mix))))
dsp.write_wav(out / 'daw-mix-dry.wav', dry * common_gain)
dsp.write_wav(out / 'daw-mix-wet.wav', mix * common_gain)
dsp.write_wav(out / 'daw-mix-ab.wav', dsp.pair(dry, mix) * common_gain)
converted = dsp.signal.resample_poly(mix * common_gain, 147, 160, axis=0)
dsp.write_wav(out / 'daw-mix-44100.wav', converted, fs=44100)
print(f'Bounced {len(mix)/fs:.3f} s, stereo, {fs} Hz PCM16; common gain {common_gain:.4f}')
