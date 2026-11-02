"""Part C: 15 to 20 second clips for slides (Bach chorales and Essen folk songs).

Real clip: a held out melody from fold 0 (first test piece of the style that reaches 15 s).
Generated clips: models trained on the fold 0 training pieces of that style, sampler chosen
by the pre specified rule in generate.py (results/generation_summary.json). Generated
scale degrees are placed in the real melody's key, nearest octave to the previous note,
kept inside the real melody's range, and played with the real melody's rhythm, so the only
difference between clips is the pitch sequence. One sample per order, fixed seed, no cherry picking.
Rests are merged into the preceding note so the JSON is a plain [[midi, dur_seconds], ...] list.
"""
import json, os, subprocess
import numpy as np
import pretty_midi
from scipy.io import wavfile
from common import *
from generate import sample, ORDERS

SEC_PER_QUARTER = {'bach': 60 / 72, 'essen': 60 / 100}
SF2 = '/usr/share/sounds/sf2/FluidR3_GM.sf2'
OUT = os.path.join(HERE, 'audio')


def rhythm(p, spq):
    """Real melody as [[midi, dur_s]], rests merged into the previous note, cut to 15 to 20 s."""
    ev = []
    for m in p['mel']:
        if m[0] < 0:
            if ev: ev[-1][1] += m[2] * spq
        else:
            ev.append([m[0], m[2] * spq])
    out, t = [], 0.0
    for e in ev:
        if t + e[1] > 20: break
        out.append([e[0], round(e[1], 4)])
        t += e[1]
    return out if t >= 15 else None


def place(degrees, tonic, first, lo, hi):
    out, prev = [], first
    for d in degrees:
        pc = (tonic + d) % 12
        cands = [m for m in range(lo - 2, hi + 3) if m % 12 == pc]
        prev = min(cands, key=lambda m: (abs(m - prev), m))
        out.append(prev)
    return out


def render(name, notes, program):
    pm = pretty_midi.PrettyMIDI()
    inst = pretty_midi.Instrument(program=program)
    t = 0.0
    for m, d in notes:
        inst.notes.append(pretty_midi.Note(velocity=88, pitch=int(m), start=t, end=t + d * 0.97))
        t += d
    pm.instruments.append(inst)
    mid = os.path.join(OUT, name + '.mid')
    wav = os.path.join(OUT, name + '.wav')
    pm.write(mid)
    if os.path.exists(SF2):
        subprocess.run(['fluidsynth', '-ni', '-g', '0.8', '-F', wav, '-r', '22050', SF2, mid],
                       check=True, capture_output=True)
        sr, a = wavfile.read(wav)  # fold to mono to keep files small
        a = a.mean(1) if a.ndim == 2 else a.astype(float)
        wavfile.write(wav, sr, (a / max(1, np.abs(a).max()) * 0.9 * 32767).astype(np.int16))
        synth = 'fluidsynth, FluidR3 GM acoustic grand piano'
    else:
        a = pm.synthesize(fs=22050)
        wavfile.write(wav, 22050, (a / np.abs(a).max() * 0.8 * 32767).astype(np.int16))
        synth = 'pretty_midi sine synthesis'
    json.dump(notes, open(os.path.join(OUT, name + '.json'), 'w'))
    return synth, round(t, 2)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    P, y = load()
    tr, te = folds(y)[0]
    best = json.load(open(os.path.join(HERE, 'results', 'generation_summary.json')))['best_sampler']
    manifest = {'sampler': best, 'clips': {}}
    rng = np.random.default_rng(2026)
    for s in ('bach', 'essen'):
        spq = SEC_PER_QUARTER[s]
        real_p = next(P[i] for i in te if y[i] == s and P[i]['mode'] == 'major' and rhythm(P[i], spq))
        real = rhythm(real_p, spq)
        pitches = [m for m, _ in real]
        lo, hi = min(pitches), max(pitches)
        tonic = real_p['tonic']
        trs = [rep_pc(P[i]) for i in tr if y[i] == s]
        sam = SAM(trs)
        synth, dur = render(f'{s}_real', real, 0)
        manifest['clips'][f'{s}_real'] = dict(style=s, kind='real held out melody', src=real_p['src'],
                                              n_notes=len(real), seconds=dur)
        for oname, kind, k in ORDERS:
            model = Markov(trs, 12, kind, k or 0)
            deg = sample(model, sam, best, len(real), rng)
            notes = [[m, d] for m, (_, d) in zip(place(deg, tonic, pitches[0], lo, hi), real)]
            name = f'{s}_order{oname}'
            _, dur = render(name, notes, 0)
            manifest['clips'][name] = dict(style=s, kind=f'generated, order {oname}, sampler {best}',
                                           longest_copy=sam.longest_copy(deg), n_notes=len(notes), seconds=dur)
        manifest['synth'] = synth
        print(s, real_p['src'], len(real))
    json.dump(manifest, open(os.path.join(OUT, 'clips_manifest.json'), 'w'), indent=1)
    # one bundle for the slide player, same shape as src/clips.json
    bundle = {n: json.load(open(os.path.join(OUT, n + '.json'))) for n in manifest['clips']}
    json.dump(bundle, open(os.path.join(HERE, 'clips.json'), 'w'))
    print(json.dumps(manifest, indent=1))
