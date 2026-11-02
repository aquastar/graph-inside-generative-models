"""How much do held out pieces overlap their training folds? (duplicate tunes, repeated
chorale melodies). Reports, per style, the share of pieces whose longest verbatim
pitch class span shared with the training fold is at least 16 notes or covers 80% of the piece."""
import json
import numpy as np
from common import *
P, y = load()
seqs = [rep_pc(p) for p in P]
out = {}
for s in STYLES:
    hits16, hits80, n = 0, 0, 0
    for tr, te in folds(y):
        sam = SAM([seqs[i] for i in tr if y[i] == s])
        for i in te:
            if y[i] != s: continue
            c = sam.longest_copy(seqs[i])
            n += 1
            hits16 += c >= 16
            hits80 += c >= 0.8 * len(seqs[i])
    out[s] = dict(n=n, span_ge_16=hits16, near_duplicate_80pct=hits80)
    print(s, out[s])
json.dump(out, open('results/leakage_check.json', 'w'), indent=1)
