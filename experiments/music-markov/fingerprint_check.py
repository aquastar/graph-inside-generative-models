"""Sanity check: reimplementation of first-order-fingerprint.py from its description.

12 tonic relative scale degrees, row normalized 12x12 transition table (rests skipped),
multinomial logistic regression, StratifiedKFold(5, shuffle=True, random_state=0).
"""
import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = json.load(open('data/seqs_v2.json'))
X, y = [], []
for style, pieces in data.items():
    for p in pieces:
        d = [(m[0] - p['tonic']) % 12 for m in p['mel'] if m[0] >= 0]
        T = np.zeros((12, 12))
        for a, b in zip(d, d[1:]):
            T[a, b] += 1
        T = T / np.maximum(T.sum(1, keepdims=True), 1)
        X.append(T.ravel())
        y.append(style)
X, y = np.array(X), np.array(y)
cv = StratifiedKFold(5, shuffle=True, random_state=0)
for name, clf in [('plain LR', LogisticRegression(max_iter=5000)),
                  ('scaled LR', make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)))]:
    s = cross_val_score(clf, X, y, cv=cv)
    print(f'{name}: {s.mean()*100:.1f}% +/- {s.std()*100:.1f}  folds {np.round(s*100,1)}')
