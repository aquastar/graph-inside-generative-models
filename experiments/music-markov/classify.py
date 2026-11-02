"""Part A: style classification by Markov order. Same 5 folds for every method."""
import json, time
import numpy as np
from scipy import sparse
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from common import *

P, y = load()
F = folds(y)
out = {'methods': {}, 'counts': {s: int((y == s).sum()) for s in STYLES}}


def table_features(seq, A, order):
    """Row normalized transition table of a given order, flattened (sparse)."""
    rows, vals = {}, {}
    for i in range(order, len(seq)):
        ctx = tuple(seq[i - order:i])
        rows.setdefault(ctx, np.zeros(A))[seq[i]] += 1
    idx, val = [], []
    for ctx, c in rows.items():
        base = 0
        for t in ctx:
            base = base * A + t
        c = c / c.sum()
        for j in np.nonzero(c)[0]:
            idx.append(base * A + j)
            val.append(c[j])
    return idx, val


def feat_matrix(seqs, A, order):
    data, ind, ptr = [], [], [0]
    for s in seqs:
        i, v = table_features(s, A, order)
        ind += i
        data += v
        ptr.append(len(ind))
    return sparse.csr_matrix((data, ind, ptr), shape=(len(seqs), A ** (order + 1)))


def record(name, preds, extra=None):
    accs = [accuracy_score(y[te], preds[te]) for _, te in F]
    f1s = [f1_score(y[te], preds[te], average='macro') for _, te in F]
    cm = confusion_matrix(y, preds, labels=STYLES)
    out['methods'][name] = dict(acc_mean=float(np.mean(accs)), acc_sd=float(np.std(accs)),
                                f1_mean=float(np.mean(f1s)), f1_sd=float(np.std(f1s)),
                                acc_folds=[float(a) for a in accs], cm=cm.tolist(), **(extra or {}))
    print(f'{name:40s} acc {np.mean(accs)*100:5.1f} +/- {np.std(accs)*100:4.1f}  macroF1 {np.mean(f1s)*100:5.1f}', flush=True)


for rep, (fn, A) in REPS.items():
    seqs = [fn(p) for p in P]
    # 1. fixed features + logistic regression
    feats = {o: feat_matrix(seqs, A, o) for o in (1, 2)}
    feats['1+2'] = sparse.hstack([feats[1], feats[2]]).tocsr()
    for o, X in feats.items():
        pred = np.empty(len(y), dtype=object)
        for tr, te in F:
            clf = LogisticRegression(max_iter=5000).fit(X[tr], y[tr])
            pred[te] = clf.predict(X[te])
        record(f'{rep}|LR order {o}', pred, dict(rep=rep, family='LR', order=str(o), n_features=int(X.shape[1])))
    # 2. likelihood classifiers
    configs = [('fixed', k, 0.1) for k in (0, 1, 2, 3)] + [('ppm', None, None)]
    for kind, k, alpha in configs:
        t0 = time.time()
        pred = np.empty(len(y), dtype=object)
        for tr, te in F:
            models = {s: Markov([seqs[i] for i in tr if y[i] == s], A, kind, k or 0, alpha or 0.1) for s in STYLES}
            for i in te:
                ll = [models[s].loglik_per_note(seqs[i]) for s in STYLES]
                pred[i] = STYLES[int(np.argmax(ll))]
        label = f'order {k}' if kind == 'fixed' else f'variable (PPM C, max {KMAX})'
        record(f'{rep}|LL {label}', pred, dict(rep=rep, family='LL', order=str(k) if k is not None else 'var'))

# smoothing sensitivity for fixed order likelihood classifiers, pitch class rep
seqs = [rep_pc(p) for p in P]
sens = {}
for alpha in (0.01, 0.1, 1.0):
    for k in (1, 2, 3):
        pred = np.empty(len(y), dtype=object)
        for tr, te in F:
            models = {s: Markov([seqs[i] for i in tr if y[i] == s], 12, 'fixed', k, alpha) for s in STYLES}
            for i in te:
                pred[i] = STYLES[int(np.argmax([models[s].loglik_per_note(seqs[i]) for s in STYLES]))]
        sens[f'alpha={alpha}, order {k}'] = float(np.mean([accuracy_score(y[te], pred[te]) for _, te in F]))
        print('sens', alpha, k, sens[f'alpha={alpha}, order {k}'], flush=True)
out['alpha_sensitivity_pc'] = sens
json.dump(out, open('results/classification.json', 'w'), indent=1)
