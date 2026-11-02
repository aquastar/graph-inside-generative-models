"""Shared data loading, representations, folds, Markov models and copy detection."""
import json, os
import numpy as np
from sklearn.model_selection import StratifiedKFold

HERE = os.path.dirname(os.path.abspath(__file__))
STYLES = ['bach', 'palestrina', 'monteverdi', 'trecento', 'essen', 'ryans']
LABELS = {'bach': 'Bach', 'palestrina': 'Palestrina', 'monteverdi': 'Monteverdi',
          'trecento': 'Trecento', 'essen': 'Essen folk', 'ryans': "Ryan's Mammoth"}
KMAX = 5            # max context for the variable order (PPM C) model
DUR_EDGES = [0.5, 1.0, 2.0, 4.0]   # quarter length buckets: <.5, <1, <2, <4, >=4


def load():
    data = json.load(open(os.path.join(HERE, 'data', 'seqs_v2.json')))
    pieces, y = [], []
    for s in STYLES:
        for p in data[s]:
            pieces.append(p)
            y.append(s)
    return pieces, np.array(y)


def folds(y):
    """The same 5 folds for every method."""
    cv = StratifiedKFold(5, shuffle=True, random_state=0)
    return list(cv.split(np.zeros(len(y)), y))


# ---------------- representations ----------------
def notes(p):
    return [m for m in p['mel'] if m[0] >= 0]


def rep_pc(p):
    return [(m[0] - p['tonic']) % 12 for m in notes(p)]


def rep_int(p):
    ps = [m[0] for m in notes(p)]
    return [int(np.clip(b - a, -12, 12)) + 12 for a, b in zip(ps, ps[1:])]


def dur_bucket(d):
    return int(np.searchsorted(DUR_EDGES, d, side='right'))


def rep_pcdur(p):
    return [((m[0] - p['tonic']) % 12) * 5 + dur_bucket(m[2]) for m in notes(p)]


REPS = {'pc': (rep_pc, 12), 'int': (rep_int, 25), 'pcdur': (rep_pcdur, 60)}
REP_NAMES = {'pc': 'pitch class (tonic relative)', 'int': 'interval', 'pcdur': 'pitch class + duration'}


# ---------------- Markov models ----------------
class Markov:
    """Counts for every order 0..KMAX on BOS padded sequences.

    kind='fixed', order k: Lidstone(alpha) estimate from the order k context. If that
    context was never seen in training it backs off to the longest seen shorter context.
    kind='ppm': interpolated PPM with escape method C over orders 0..KMAX, uniform base.
    """

    def __init__(self, seqs, A, kind='fixed', order=1, alpha=0.1, kmax=KMAX):
        self.A, self.kind, self.order, self.alpha = A, kind, order, alpha
        self.kmax = kmax if kind == 'ppm' else order
        self.BOS = A
        self.counts = [dict() for _ in range(self.kmax + 1)]
        for s in seqs:
            h = [self.BOS] * self.kmax + list(s)
            for i in range(self.kmax, len(h)):
                for k in range(self.kmax + 1):
                    ctx = tuple(h[i - k:i])
                    c = self.counts[k].get(ctx)
                    if c is None:
                        c = self.counts[k][ctx] = np.zeros(A)
                    c[h[i]] += 1
        self.cache = {}

    def pad(self, s):
        return [self.BOS] * self.kmax + list(s)

    def dist(self, hist):
        """hist: padded history (list). Returns the next symbol distribution."""
        ctx = tuple(hist[len(hist) - self.kmax:])
        v = self.cache.get(ctx)
        if v is not None:
            return v
        A = self.A
        if self.kind == 'ppm':
            v = np.full(A, 1.0 / A)
            for k in range(self.kmax + 1):
                c = self.counts[k].get(ctx[self.kmax - k:])
                if c is None:
                    break
                n, t = c.sum(), (c > 0).sum()
                v = (c + t * v) / (n + t)
        else:
            for k in range(self.order, -1, -1):
                c = self.counts[k].get(ctx[self.kmax - k:])
                if c is not None:
                    break
            v = (c + self.alpha) / (c.sum() + self.alpha * A)
        self.cache[ctx] = v
        return v

    def loglik_per_note(self, s):
        h = self.pad(s)
        lp = 0.0
        for i in range(self.kmax, len(h)):
            lp += np.log(self.dist(h[:i])[h[i]])
        return lp / max(1, len(s))


# ---------------- copy detection (suffix automaton over training sequences) ----------------
class SAM:
    def __init__(self, seqs):
        self.next, self.link, self.len = [{}], [-1], [0]
        last = 0
        for s in seqs:
            for x in list(s) + [-1]:   # -1 separates pieces, never generated
                last = self._extend(last, x)

    def _extend(self, last, x):
        cur = len(self.len)
        self.next.append({})
        self.link.append(-1)
        self.len.append(self.len[last] + 1)
        p = last
        while p != -1 and x not in self.next[p]:
            self.next[p][x] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][x]
            if self.len[p] + 1 == self.len[q]:
                self.link[cur] = q
            else:
                cl = len(self.len)
                self.next.append(dict(self.next[q]))
                self.link.append(self.link[q])
                self.len.append(self.len[p] + 1)
                while p != -1 and self.next[p].get(x) == q:
                    self.next[p][x] = cl
                    p = self.link[p]
                self.link[q] = self.link[cur] = cl
        return cur

    def step(self, state, x):
        """state = (node, matched length). Returns state after appending x."""
        v, l = state
        while v and x not in self.next[v]:
            v = self.link[v]
            l = self.len[v]
        if x in self.next[v]:
            return self.next[v][x], l + 1
        return 0, 0

    def longest_copy(self, s):
        st, best = (0, 0), 0
        for x in s:
            st = self.step(st, x)
            best = max(best, st[1])
        return best
