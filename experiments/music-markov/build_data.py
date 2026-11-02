"""Rebuild seqs_v2.json from music21 built in corpora.

Format: {style: [{"tonic": int, "mel": [[midi_pitch, onset, dur], ...], "src": str}]}
pitch -1 marks a rest, onset and dur are in quarter notes, tonic is the pitch class
of the tonic from music21 key analysis (Krumhansl Schmuckler) on the full score.
Multi voice pieces use the top part (soprano or cantus).
"""
import json, random, sys
from multiprocessing import Pool
from music21 import corpus, converter

CAP = 210
MIN_NOTES = 16
STYLES = ['bach', 'palestrina', 'monteverdi', 'trecento', 'essen', 'ryans']


def melody(score):
    part = score.parts[0] if score.parts else score
    part = part.stripTies()
    mel = []
    for n in part.flatten().notesAndRests:
        d = float(n.quarterLength)
        if d <= 0:
            continue  # grace notes
        if n.isRest:
            p = -1
        elif n.isChord:
            p = max(x.midi for x in n.pitches)
        else:
            p = n.pitch.midi
        on = float(n.offset)
        if p == -1 and mel and mel[-1][0] == -1:
            mel[-1][2] += d  # merge rests
            continue
        mel.append([p, on, d])
    # recompute onsets cumulatively (robust to measure offsets in flattened view)
    t = 0.0
    for m in mel:
        m[1] = round(t, 4)
        m[2] = round(m[2], 4)
        t += m[2]
    while mel and mel[0][0] == -1: mel.pop(0)
    while mel and mel[-1][0] == -1: mel.pop()
    return mel


def piece(score, src):
    mel = melody(score)
    if sum(1 for m in mel if m[0] >= 0) < MIN_NOTES:
        return None
    k = score.analyze('key')
    return {'tonic': int(k.tonic.pitchClass), 'mode': k.mode, 'mel': mel, 'src': src}


def load_path(arg):
    style, path = arg
    try:
        s = converter.parse(path)
        if hasattr(s, 'scores') and not hasattr(s, 'parts'):
            s = s.scores[0]
        return style, piece(s, str(path).split('corpus/')[-1])
    except Exception as e:
        return style, None


def essen_one(arg):
    path, i = arg
    try:
        sc = converter.parse(path).scores[i]
        return 'essen', piece(sc, f"{str(path).split('corpus/')[-1]}#{i}")
    except Exception:
        return 'essen', None


if __name__ == '__main__':
    rng = random.Random(0)
    jobs = []
    bach = [p for p in corpus.getComposer('bach') if str(p).endswith(('.mxl', '.xml'))]
    pools = {
        'bach': bach,
        'palestrina': list(corpus.getComposer('palestrina')),
        'monteverdi': [p for p in corpus.getComposer('monteverdi') if str(p).endswith('.mxl')],
        'trecento': list(corpus.getComposer('trecento')),
        'ryans': list(corpus.getComposer('ryansMammoth')),
    }
    with Pool() as pool:
        data = {s: [] for s in STYLES}
        for style, paths in pools.items():
            paths = sorted(paths, key=str)
            rng.shuffle(paths)
            # parse 30% extra so the cap survives parse failures and short pieces
            res = pool.map(load_path, [(style, p) for p in paths[:int(CAP * 1.3)]])
            data[style] = [r for _, r in res if r][:CAP]
            print(style, 'parsed', len(paths[:int(CAP * 1.3)]), 'kept', len(data[style]), flush=True)
        # Essen: 31 abc opus files, each with many tunes
        idx = []
        for p in sorted(corpus.getComposer('essenFolksong'), key=str):
            n = len(converter.parse(p).scores)
            idx += [(p, i) for i in range(n)]
        rng.shuffle(idx)
        res = pool.map(essen_one, idx[:int(CAP * 1.3)])
        data['essen'] = [r for _, r in res if r][:CAP]
        print('essen tunes', len(idx), 'kept', len(data['essen']), flush=True)
    counts = {s: len(v) for s, v in data.items()}
    print(counts, sum(counts.values()))
    json.dump(data, open('data/seqs_v2.json', 'w'))
    json.dump({'cap': CAP, 'min_notes': MIN_NOTES, 'counts': counts, 'total': sum(counts.values())},
              open('data/counts.json', 'w'), indent=1)
