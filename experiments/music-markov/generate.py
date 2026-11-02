"""Part B: generation by Markov order and sampler, pitch class (tonic relative) tokens.

For each of the 5 folds and each style, models are trained on that fold's training pieces
only. Every (order, sampler) cell draws N_PER_FOLD melodies of GEN_LEN notes per style per fold.
"""
import json, itertools
import numpy as np
from sklearn.linear_model import LogisticRegression
from common import *

GEN_LEN, N_PER_FOLD, L_COPY = 48, 20, 6
ORDERS = [('1', 'fixed', 1), ('2', 'fixed', 2), ('3', 'fixed', 3), ('var', 'ppm', None)]
SAMPLERS = ['ancestral', 'temp 0.7', 'temp 1.3', 'top k 3', 'max copy L=6']


def table1(seq):
    T = np.zeros((12, 12))
    for a, b in zip(seq, seq[1:]):
        T[a, b] += 1
    return (T / np.maximum(T.sum(1, keepdims=True), 1)).ravel()


def table12(seq):
    """Order 1 table plus order 2 table (12x12x12, row normalized per context)."""
    T = np.zeros((144, 12))
    for a, b, c in zip(seq, seq[1:], seq[2:]):
        T[a * 12 + b, c] += 1
    return np.concatenate([table1(seq), (T / np.maximum(T.sum(1, keepdims=True), 1)).ravel()])


def adjust(p, sampler):
    if sampler == 'temp 0.7':
        p = p ** (1 / 0.7)
    elif sampler == 'temp 1.3':
        p = p ** (1 / 1.3)
    elif sampler == 'top k 3':
        q = np.zeros_like(p)
        top = np.argsort(p)[-3:]
        q[top] = p[top]
        p = q
    return p / p.sum()


def sample(model, sam, sampler, n, rng):
    h, out, st = model.pad([]), [], (0, 0)
    for _ in range(n):
        p = adjust(model.dist(h), sampler)
        if sampler.startswith('max copy'):
            nxt = [sam.step(st, x) for x in range(12)]
            ok = np.array([s[1] <= L_COPY for s in nxt], float)
            if (p * ok).sum() > 0:
                p = p * ok / (p * ok).sum()
            else:  # every option would exceed L: take the least copying one
                lens = np.array([s[1] for s in nxt])
                p = (lens == lens.min()) * 1.0
                p /= p.sum()
        x = int(rng.choice(12, p=p))
        st = sam.step(st, x)
        h.append(x)
        out.append(x)
    return out


def ngrams(s, n):
    return [tuple(s[i:i + n]) for i in range(len(s) - n + 1)]


def edit(a, b):
    d = np.arange(len(b) + 1)
    for i, x in enumerate(a, 1):
        prev, d[0] = d[0], i
        for j, z in enumerate(b, 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (x != z))
            prev = cur
    return d[-1] / max(len(a), len(b))


def metrics(gens, style, clfs, sam, train4):
    clf, clf2 = clfs
    pred = clf.predict(np.array([table1(g) for g in gens]))
    pred2 = clf2.predict(np.array([table12(g) for g in gens]))
    four = [ngrams(g, 4) for g in gens]
    allfour = list(itertools.chain(*four))
    pairs = list(itertools.combinations(range(len(gens)), 2))
    return dict(style_acc=float(np.mean(pred == style)), style_acc12=float(np.mean(pred2 == style)),
                longest_copy=float(np.mean([sam.longest_copy(g) for g in gens])),
                seen4=float(np.mean([np.mean([t in train4 for t in f]) for f in four])),
                distinct4=len(set(allfour)) / len(allfour),
                pair_edit=float(np.mean([edit(gens[i], gens[j]) for i, j in pairs])))


if __name__ == '__main__':
    P, y = load()
    seqs = [rep_pc(p) for p in P]
    rng = np.random.default_rng(0)
    rows = []   # one row per fold x style x cell
    for f, (tr, te) in enumerate(folds(y)):
        clf = (LogisticRegression(max_iter=5000).fit(np.array([table1(seqs[i]) for i in tr]), y[tr]),
               LogisticRegression(max_iter=5000).fit(np.array([table12(seqs[i]) for i in tr]), y[tr]))
        for s in STYLES:
            trs = [seqs[i] for i in tr if y[i] == s]
            sam = SAM(trs)
            train4 = set(itertools.chain(*[ngrams(t, 4) for t in trs]))
            # reference: real held out excerpts of the same length
            real = [seqs[i][:GEN_LEN] for i in te if y[i] == s and len(seqs[i]) >= GEN_LEN]
            real = [real[j] for j in rng.permutation(len(real))[:N_PER_FOLD]]
            rows.append(dict(fold=f, style=s, order='real held out', sampler='', **metrics(real, s, clf, sam, train4)))
            for oname, kind, k in ORDERS:
                model = Markov(trs, 12, kind, k or 0)
                for smp in SAMPLERS:
                    gens = [sample(model, sam, smp, GEN_LEN, rng) for _ in range(N_PER_FOLD)]
                    rows.append(dict(fold=f, style=s, order=oname, sampler=smp, **metrics(gens, s, clf, sam, train4)))
            print('fold', f, s, flush=True)
    json.dump(rows, open('results/generation_rows.json', 'w'))

    # summary: mean over styles within fold, then mean and sd over folds
    keys = ['style_acc', 'style_acc12', 'longest_copy', 'seen4', 'distinct4', 'pair_edit']
    cells = [('real held out', '')] + [(o, s) for o, _, _ in ORDERS for s in SAMPLERS]
    summ = []
    for o, s in cells:
        r = [x for x in rows if x['order'] == o and x['sampler'] == s]
        d = dict(order=o, sampler=s)
        for k in keys:
            per_fold = [np.mean([x[k] for x in r if x['fold'] == f]) for f in range(5)]
            d[k] = float(np.mean(per_fold))
            d[k + '_sd'] = float(np.std(per_fold))
        d['style_acc_by_style'] = {st: float(np.mean([x['style_acc'] for x in r if x['style'] == st])) for st in STYLES}
        summ.append(d)
    # pre specified rule for the audio sampler: among samplers whose mean longest copied span
    # stays at or below the real held out reference for every order, take the one with the
    # highest style accuracy averaged over orders and both judges.
    ref = summ[0]['longest_copy']
    score = {}
    for smp in SAMPLERS:
        r = [d for d in summ if d['sampler'] == smp]
        if all(d['longest_copy'] <= ref for d in r):
            score[smp] = float(np.mean([(d['style_acc'] + d['style_acc12']) / 2 for d in r]))
    best = max(score, key=score.get)
    json.dump(dict(summary=summ, eligible_sampler_scores=score, best_sampler=best,
                   gen_len=GEN_LEN, n_per_fold_per_style=N_PER_FOLD, L=L_COPY),
              open('results/generation_summary.json', 'w'), indent=1)
    print('best sampler', best, score)
    for d in summ:
        print(f"{d['order']:14s} {d['sampler']:13s} acc {d['style_acc']*100:5.1f} acc12 {d['style_acc12']*100:5.1f}  copy {d['longest_copy']:5.1f}  seen4 {d['seen4']*100:5.1f}  distinct4 {d['distinct4']*100:5.1f}  edit {d['pair_edit']:.2f}")
