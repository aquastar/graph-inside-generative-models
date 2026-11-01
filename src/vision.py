import math, random, re
from music import T, R, C, L, P, F, chip, defs, SVG, sec, mini_lattice, INK, MUT, ACC, AC2, MU, LINE, SOFT, MUL, ACL
import music

GRN = '#2f7d4f'

def tag(x, y, s, kind):
    col = {'done': GRN, 'part': ACC, 'plan': '#9aa6ae'}[kind]
    fill = {'done': '#eaf3ea', 'part': ACL, 'plan': '#fff'}[kind]
    w = len(s) * 7.2 + 20
    dash = 'stroke-dasharray="4 3"' if kind == 'plan' else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="11" fill="{fill}" stroke="{col}" stroke-width="1.5" {dash}/>' + T(x + w / 2, y + 15.5, s, 12.5, 700, col, 'middle')

def axis_icon(x, y, s=1.0, depth='done', time='part', label=True):
    """small depth by time grid used as a locator"""
    out = ''
    w, h = 150 * s, 100 * s
    out += L(x, y + h, x + w, y + h, INK, 1.5, 'marker-end="url(#axk)"') + L(x, y + h, x, y, INK, 1.5, 'marker-end="url(#axk)"')
    for i in range(5):
        for j in range(4):
            out += C(x + 18 * s + i * 28 * s, y + 12 * s + j * 24 * s, 3 * s, '#c9d0d5')
    dc = {'done': ACC, 'part': ACC, 'plan': '#c9d0d5'}[depth]
    tc = {'done': MU, 'part': MU, 'plan': '#c9d0d5'}[time]
    dd = '' if depth == 'done' else 'stroke-dasharray="4 3"'
    td = '' if time == 'done' else 'stroke-dasharray="4 3"'
    cx = x + 18 * s + 28 * s
    out += P(f'M{cx},{y+12*s} L{cx},{y+12*s+72*s}', dc, 3.5 * s, extra=dd)
    ry = y + 12 * s + 48 * s
    out += P(f'M{x+18*s},{ry} L{x+18*s+112*s},{ry}', tc, 3.5 * s, extra=td)
    if label:
        out += T(x - 8, y + h / 2, 'depth', 12 * s + 2, 700, ACC, 'end') + T(x + w / 2, y + h + 18 * s + 4, 'time', 12 * s + 2, 700, MU, 'middle')
    return out

def adefs(p):
    return defs(p) + '<defs><marker id="axk" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#111"/></marker></defs>'

V = []

# ---------------- V1: a vector says what we changed ----------------
g = adefs('v1')
bx = 90
names = ['block 1', 'block 2', 'block 3', 'block 4', 'block 5', 'block 6']
ys = [400 - k * 58 for k in range(6)]
for k, y in enumerate(ys):
    g += R(bx, y - 20, 170, 40, '#fff', '#9aa6ae', 1.5, 6) + T(bx + 85, y + 5, names[k], 14, 600, MUT, 'middle')
for k in range(5):
    g += L(bx + 85, ys[k] - 20, bx + 85, ys[k + 1] + 20, '#9aa6ae', 1.5)
g += R(bx, 30, 170, 40, SOFT, INK, 2, 6) + T(bx + 85, 55, 'output', 15, 700, INK, 'middle') + L(bx + 85, ys[5] - 20, bx + 85, 70, '#9aa6ae', 1.5)
f1 = P(f'M20,{ys[2]} L{bx-4},{ys[2]}', ACC, 4, extra='marker-end="url(#v1o)"') + T(20, ys[2] - 14, 'edit or', 13, 700, ACC) + T(20, ys[2] + 26, 'steering', 13, 700, ACC)
f1 += T(330, ys[2] + 5, 'what we changed', 16, 700, ACC)
g += F(1, f1)
f2 = ''.join(R(bx, ys[k] - 20, 170, 40, '#eef0f2', '#c9d0d5', 1.5, 6) + T(bx + 192, ys[k] + 8, '?', 22, 700, '#9aa6ae', 'middle') for k in (3, 4, 5))
f2 += T(330, ys[4] + 5, 'where it went: unknown', 16, 700, MUT)
g += F(2, f2)
paths = [(2, 3), (3, 5), (2, 4), (4, 5)]
f3 = ''
for a, b in paths:
    f3 += P(f'M{bx+150},{ys[a]} C{bx+215},{ys[a]} {bx+215},{ys[b]} {bx+150},{ys[b]}', ACC, 3)
f3 += P(f'M{bx+20},{ys[3]} C{bx-40},{ys[3]} {bx-40},{ys[5]} {bx+20},{ys[5]}', ACC, 3)
f3 += T(330, ys[5] + 5, 'it spreads along a graph', 16, 700, INK)
g += F(3, f3)
ex = R(640, 60, 510, 340, SOFT, LINE, 1, 10) + T(660, 92, 'Three places the vector story breaks', 17, 700, AC2)
rows = [('language', 'an edit passes its own test, a related fact breaks', ACC), ('language', 'steering works on average, flips on single inputs', ACC), ('music', 'removing a style works, adding one fails', MU)]
for i, (d, s, col) in enumerate(rows):
    y = 135 + i * 82
    ex += R(660, y, 90, 26, '#fff', col, 1.5, 13) + T(705, y + 18, d, 13, 700, col, 'middle') + T(765, y + 18, s, 14.5, 600, INK)
    ex += T(765, y + 42, ['SDM 2026, Hu 2025, Yang 2025', 'Tan 2024, Wollschläger 2025', 'our MusicGen study, under review'][i], 12.5, 400, MUT)
g += F(4, ex)
g += F(5, T(640, 450, 'Every control tool is a vector. Every side effect is a path.', 19, 700, ACC))
V.append(sec('A vector says what we changed, not where it went', SVG(g), ch='0',
             notes='Opening argument. Interventions are local, consequences are not. The question of the talk is whether a graph describes where the consequence goes better than the vector does.'))

# ---------------- V2: two axes ----------------
g = adefs('v2')
ox, oy = 120, 410
g += L(ox, oy, 760, oy, INK, 2, 'marker-end="url(#axk)"') + L(ox, oy, ox, 40, INK, 2, 'marker-end="url(#axk)"')
g += T(440, oy + 40, 'time: generation steps', 17, 700, MU, 'middle') + T(ox - 20, 225, 'depth: model blocks', 17, 700, ACC, 'middle', f'transform="rotate(-90 {ox-20} 225)"')
cols_x = [170 + i * 105 for i in range(6)]
rows_y = [370 - j * 75 for j in range(5)]
for x in cols_x:
    for y in rows_y:
        g += C(x, y, 9, '#fff', '#b8c0c6', 2)
dep = ''
cx = cols_x[2]
for j in range(4):
    dep += L(cx, rows_y[j] - 9, cx, rows_y[j + 1] + 9, ACC, 4)
for a, b in [(0, 2), (1, 3), (2, 4)]:
    dep += P(f'M{cx+9},{rows_y[a]} C{cx+45},{rows_y[a]} {cx+45},{rows_y[b]} {cx+9},{rows_y[b]}', ACC, 2.5)
dep += ''.join(C(cx, y, 10, ACC) for y in rows_y)
dep += R(800, 60, 350, 120, ACL, ACC, 1.5, 10) + T(820, 92, 'Depth: propagation', 18, 700, ACC) + T(820, 118, 'one moment, across blocks', 14.5, 400, INK) + T(820, 144, 'Language: does an edit stay local?', 14.5, 700, INK) + T(820, 166, 'Part 1', 13, 600, MUT)
g += F(1, dep)
tim = ''
ry = rows_y[2]
for i in range(5):
    tim += P(f'M{cols_x[i]+10},{ry} L{cols_x[i+1]-12},{ry}', MU, 4, extra='marker-end="url(#v2t)"')
tim += ''.join(C(x, ry, 10, MU) for x in cols_x)
tim += R(800, 200, 350, 120, MUL, MU, 1.5, 10) + T(820, 232, 'Time: reachability', 18, 700, MU) + T(820, 258, 'one layer, along a trajectory', 14.5, 400, INK) + T(820, 284, 'Music: can steering get there?', 14.5, 700, INK) + T(820, 306, 'Part 2', 13, 600, MUT)
g += F(2, tim)
whole = R(150, 50, 590, 345, 'none', INK, 2, 12, 'stroke-dasharray="8 6"') + R(800, 340, 350, 70, '#fff', INK, 2, 10) + T(820, 370, 'Both at once: any sequence generator', 15.5, 700, INK) + T(820, 394, 'Part 3: time series, video, dynamics', 14, 400, MUT)
g += F(3, whole)
V.append(sec('Two axes, two graph questions', SVG(g), ch='0',
             notes='The organizing frame. Language gives the depth case, music gives the time case, and every sequence generator has both.'))

# ---------------- V3: why a graph (network science lens) ----------------
g = adefs('v3')
hdr = T(70, 50, 'Network science concept', 15, 700, MUT) + T(470, 50, 'Question about a generative model', 15, 700, MUT) + T(930, 50, 'In this talk', 15, 700, MUT)
g += hdr + L(60, 62, 1120, 62, INK, 2)
rows = [('Diffusion and cascades', 'does an edit spread beyond its target?', 'Part 1, depth', ACC),
        ('Partial correlation networks', 'which blocks start working together after a change?', 'Part 1, delta graph', ACC),
        ('Communities and modularity', 'is a musical style a module of states?', 'Part 2, time', MU),
        ('Reachability and hitting time', 'can steering reach a style from here?', 'Part 2, time', MU),
        ('Resilience to edge removal', 'which surgery breaks the structure?', 'Part 3, model math', AC2),
        ('Markov state models', 'what are the slow states of a generator?', 'Part 3, dynamics', AC2)]
for i, (a, b, c, col) in enumerate(rows):
    y = 100 + i * 58
    blk = C(78, y - 5, 7, col) + T(96, y, a, 16, 700, INK) + T(470, y, b, 15.5, 400, INK) + R(930, y - 18, 170, 26, '#fff', col, 1.5, 13) + T(1015, y, c, 13, 700, col, 'middle') + L(60, y + 22, 1120, y + 22, LINE, 1)
    g += F(i + 1, blk) if i else blk
g += F(7, T(590, 470, 'Not new mathematics. Old network questions asked of a new object.', 18, 700, ACC, 'middle'))
V.append(sec('Why a graph: questions network science already knows how to ask', SVG(g), ch='0'))

# ---------------- V4: the program ----------------
g = adefs('v4')
boxes = [('Build', 'read a graph out of activations', 'cluster, correlate, count'),
         ('Test', 'does it predict an intervention?', 'better than a vector can'),
         ('Generalize', 'same questions, more generators', 'every surgery, every sequence')]
for i, (a, b, c) in enumerate(boxes):
    x = 40 + i * 380
    blk = R(x, 50, 340, 120, SOFT, AC2, 2, 10) + T(x + 170, 88, a, 24, 700, AC2, 'middle') + T(x + 170, 118, b, 15, 600, INK, 'middle') + T(x + 170, 142, c, 14, 400, MUT, 'middle')
    if i < 2:
        blk += P(f'M{x+342},110 L{x+376},110', AC2, 3, extra='marker-end="url(#v4a)"')
    g += F(i, blk) if i else blk
g += T(30, 222, 'depth', 16, 700, ACC) + T(30, 302, 'time', 16, 700, MU)
st = tag(60, 236, 'done: delta graph across blocks', 'done') + tag(440, 236, 'done: AUC 0.70 to 0.80, shape beats size', 'done') + tag(820, 236, 'planned: six model operations', 'plan')
st += tag(60, 316, 'part: data graph, model graph next', 'part') + tag(440, 316, 'part: one way steering, under review', 'part') + tag(820, 316, 'planned: time series, video', 'plan')
g += F(3, L(20, 200, 1160, 200, LINE, 1) + L(20, 280, 1160, 280, LINE, 1) + L(20, 360, 1160, 360, LINE, 1) + st)
g += F(4, R(160, 385, 860, 70, ACL, ACC, 1.5, 10) + T(590, 416, 'A graph earns its place only by predicting what a vector cannot.', 19, 700, ACC, 'middle') + T(590, 440, 'Otherwise it is just a drawing.', 15, 400, INK, 'middle'))
V.append(sec('The program: build, test, generalize', SVG(g), ch='0',
             notes='Green is done, orange is partial, dashed is planned. The rest of the talk walks this grid from top left to bottom right.'))

# ---------------- B1: bridge after language ----------------
g = adefs('b1')
g += axis_icon(90, 90, 2.0, 'done', 'plan')
g += T(240, 360, 'depth: done for one moment', 16, 700, ACC, 'middle') + T(240, 384, 'time: not touched yet', 16, 700, MUT, 'middle')
why = R(520, 60, 630, 330, SOFT, LINE, 1, 10) + T(545, 95, 'Why music is the right test for the time axis', 18, 700, MU)
items = [('No facts to check', 'a style has no right answer, only where the music goes'),
         ('Long trajectories', '30 seconds of audio is 1,500 generation steps at 50 Hz'),
         ('Steering is the control', 'no weight edit, every intervention acts along time'),
         ('Discrete outputs for free', 'audio tokens give a reference graph to compare against')]
for i, (a, b) in enumerate(items):
    y = 140 + i * 62
    why += F(i + 1, C(555, y - 5, 7, MU) + T(575, y, a, 16, 700, INK) + T(575, y + 22, b, 14, 400, MUT))
g += why
g += F(5, T(590, 450, 'Language gave the depth case. Music forces the time case.', 19, 700, INK, 'middle'))
BR1 = sec('From depth to time', SVG(g), ch='2', cls='divider')

# ---------------- B2: one intervention, both axes ----------------
g = adefs('b2')
ox, oy = 90, 420
g += L(ox, oy, 700, oy, INK, 2, 'marker-end="url(#axk)"') + L(ox, oy, ox, 50, INK, 2, 'marker-end="url(#axk)"')
g += T(400, oy + 34, 'time: MusicGen generation steps', 15, 700, MU, 'middle') + T(ox - 18, 235, 'depth: blocks', 15, 700, ACC, 'middle', f'transform="rotate(-90 {ox-18} 235)"')
cx_ = [140 + i * 100 for i in range(6)]; ry_ = [380 - j * 75 for j in range(5)]
for x in cx_:
    for y in ry_:
        g += C(x, y, 8, '#fff', '#b8c0c6', 2)
g += F(1, P(f'M{cx_[2]},{ry_[4]+40} L{cx_[2]},{ry_[2]-14}', ACC, 4, extra='marker-end="url(#b2o)"') + T(cx_[2] + 10, ry_[4] + 30, 'steer here', 14, 700, ACC))
dg = ''.join(L(cx_[2], ry_[j] - 8, cx_[2], ry_[j + 1] + 8, ACC, 4) for j in range(4)) + ''.join(C(cx_[2], y, 9, ACC) for y in ry_)
dg += R(760, 70, 390, 100, ACL, ACC, 1.5, 10) + T(780, 100, 'Depth: delta graph, steered vs not', 16, 700, ACC) + T(780, 124, 'the SDM 2026 recipe, run unchanged', 14, 400, INK) + T(780, 148, 'which blocks reorganize?', 14, 400, INK)
g += F(2, dg)
tg = ''.join(P(f'M{cx_[i]+9},{ry_[2]} L{cx_[i+1]-11},{ry_[2]}', MU, 4, extra='marker-end="url(#b2t)"') for i in range(2, 5)) + ''.join(C(x, ry_[2], 9, MU) for x in cx_[2:])
tg += R(760, 190, 390, 100, MUL, MU, 1.5, 10) + T(780, 220, 'Time: state graph after steering', 16, 700, MU) + T(780, 244, 'does the trajectory enter', 14, 400, INK) + T(780, 268, 'the target style\'s states?', 14, 400, INK)
g += F(3, tg)
g += F(4, R(760, 310, 390, 100, '#fff', INK, 2, 10) + T(780, 342, 'Do the two graphs agree?', 17, 700, INK) + T(780, 368, 'blocks that reorganize ↔ steps', 14, 400, INK) + T(780, 390, 'where the trajectory stalls', 14, 400, INK))
BR2 = sec('One intervention, both axes', SVG(g), ch='2', status='prog',
          notes='This experiment stitches the two halves together. It reuses the language pipeline on music without changes.')

# ---------------- Beyond section ----------------
B = []
g = adefs('f1')
ops = [('edit', 'done', 'SDM 2026'), ('fine-tune', 'plan', ''), ('merge', 'plan', ''), ('quantize', 'plan', ''), ('prune', 'plan', ''), ('distill', 'plan', '')]
for i, (n, k, s) in enumerate(ops):
    x = 50 + i * 185
    col = GRN if k == 'done' else '#9aa6ae'
    blk = R(x, 70, 165, 210, '#fff', col, 2, 10, '' if k == 'done' else 'stroke-dasharray="6 4"') + T(x + 82, 102, n, 18, 700, col, 'middle')
    for a in range(4):
        for b in range(4):
            v = (a * 7 + b * 3 + i) % 5
            blk += R(x + 22 + a * 30, 120 + b * 30, 26, 26, ACC if (k == 'done' and v > 2) else ('#e3e7ea' if v > 2 else '#f5f6f7'), 'none', 0, 3)
    blk += T(x + 82, 268, s if s else 'same recipe, not yet run', 13, 700 if s else 400, col, 'middle')
    g += F(1 if i else 0, blk) if i else blk
g += F(2, R(50, 310, 1080, 60, SOFT, LINE, 1, 10) + T(590, 346, 'Goal: predict the outcome of a model operation before running the benchmark', 18, 700, INK, 'middle'))
g += F(3, T(590, 420, 'If the recipe is operation agnostic, one detector screens every surgery.', 17, 700, ACC, 'middle') + T(590, 446, 'Not yet shown.', 15, 400, MUT, 'middle'))
B.append(sec('Depth, generalized: one delta graph for every surgery', SVG(g), ch='3', status='open'))

g = adefs('f2')
cols4 = [('MusicGen', 'audio tokens', 'token graph free', MU, True), ('Chronos', 'value bins, about 4,096', 'token graph free', MU, True), ('TimesFM, Moirai', 'continuous patches', 'cluster first', AC2, False), ('Video tokenizers', 'space time tokens', 'free but huge', AC2, True)]
for i, (n, s, f, col, free) in enumerate(cols4):
    x = 40 + i * 285
    blk = R(x, 60, 255, 170, '#fff', col, 2, 10) + T(x + 127, 95, n, 18, 700, col, 'middle') + T(x + 127, 125, 'states from:', 13, 400, MUT, 'middle') + T(x + 127, 147, s, 15, 600, INK, 'middle')
    blk += R(x + 40, 175, 175, 30, MUL if free else SOFT, col, 1.2, 15) + T(x + 127, 195, f, 13.5, 700, col, 'middle')
    g += F(i, blk) if i else blk
pipe = ''
for i, s in enumerate(['trajectory', 'states', 'transitions', 'graph']):
    x = 140 + i * 250
    pipe += R(x, 290, 170, 50, SOFT, AC2, 1.5, 25) + T(x + 85, 321, s, 16, 700, AC2, 'middle')
    if i < 3:
        pipe += P(f'M{x+172},315 L{x+246},315', AC2, 2.5, extra='marker-end="url(#f2a)"')
g += F(4, pipe + T(590, 390, 'the same read out for every model that emits a sequence', 16, 700, INK, 'middle'))
g += F(5, T(590, 445, 'Chronos is the closest cousin of MusicGen: the natural first transfer.', 17, 700, ACC, 'middle'))
B.append(sec('Time, generalized: a sequence generator is a dynamical system', SVG(g), ch='3', status='open',
             ref='Ansari et al., Chronos, TMLR 2024. Das et al., TimesFM, ICML 2024. Woo et al., Moirai, ICML 2024'))

g = adefs('f3')
cx, cy = 590, 245
g += C(cx, cy, 95, ACL, ACC, 3) + T(cx, cy - 10, 'state graph', 18, 700, ACC, 'middle') + T(cx, cy + 14, 'from a generator\'s', 14, 400, INK, 'middle') + T(cx, cy + 32, 'internal trajectory', 14, 400, INK, 'middle')
sats = [('Markov state models', 'lag time tests, slow states'), ('Symbolic dynamics', 'which partition keeps dynamics'), ('Koopman and DMD', 'steering as operator perturbation'),
        ('Hidden Markov models', 'states learned from tokens'), ('Recurrence and visibility graphs', 'series to network, on observations')]
for i, (a, b) in enumerate(sats):
    ang = -math.pi / 2 + i * 2 * math.pi / 5
    x, y = cx + 400 * math.cos(ang), cy + 180 * math.sin(ang)
    blk = L(cx + 95 * math.cos(ang), cy + 95 * math.sin(ang), x - 100 * math.cos(ang), y - 34 * math.sin(ang), AC2, 2)
    blk += R(x - 155, y - 32, 310, 62, SOFT, LINE, 1, 8) + T(x, y - 7, a, 16, 700, AC2, 'middle') + T(x, y + 16, b, 13.5, 400, INK, 'middle')
    g += F(i + 1, blk)
g += F(6, T(590, 468, 'Classic tools read observed series. We read the generator from inside.', 17, 700, INK, 'middle'))
B.append(sec('Old tools for new trajectories', SVG(g), ch='3',
             ref='Prinz et al., J. Chem. Phys. 2011. Lacasa et al., PNAS 2008. Marwan et al., 2009. Brunton et al., Koopman review, 2022'))

g = adefs('f4')
lanes = [('Months', 'planned', ACC, [('MusicGen state graph, controls, lag sweep', 'plan'), ('delta graph on MusicGen steering', 'plan'), ('one way steering paper', 'part')]),
         ('One year', 'planned', AC2, [('model math across six operations', 'plan'), ('Chronos: token graph vs activation graph', 'plan'), ('does guidance reshape the graph?', 'plan')]),
         ('Longer', 'speculative', '#9aa6ae', [('which discretization keeps reachability', 'plan'), ('one read out toolkit for sequence models', 'plan'), ('steering music for hearing loss', 'plan')])]
for i, (lab, st, col, its) in enumerate(lanes):
    x = 40 + i * 380
    blk = R(x, 50, 350, 320, '#fff', col, 2, 12, '' if i < 2 else 'stroke-dasharray="7 5"') + R(x, 50, 350, 56, col, col, 0, 12) + T(x + 20, 86, lab, 22, 700, '#fff') + T(x + 330, 86, st, 14, 600, '#fff', 'end')
    for j, (t_, k) in enumerate(its):
        y = 145 + j * 72
        blk += C(x + 26, y - 5, 8, GRN if k == 'done' else (ACC if k == 'part' else '#fff'), col, 2) + T(x + 42, y, t_, 13.5, 600, INK)
        if k == 'part':
            blk += T(x + 50, y + 22, 'under review', 13, 400, ACC)
    if i < 2:
        blk += P(f'M{x+352},210 L{x+376},210', AC2, 3, extra='marker-end="url(#f4a)"')
    g += F(i, blk) if i else blk
g += F(3, T(590, 440, 'Near term is an experiment. Long term is a hypothesis.', 19, 700, INK, 'middle'))
B.append(sec('Roadmap', SVG(g), ch='3'))

g = adefs('f5')
fal = ['delta graph features add nothing over change size on fine-tuning or merging',
       'MusicGen states show no community structure above shuffled labels at any lag',
       'steered trajectories reach target states as often as unsteered ones']
g += T(60, 60, 'Three numbers that would end this program', 19, 700, ACC)
for i, s in enumerate(fal):
    y = 110 + i * 62
    blk = C(80, y - 6, 18, ACC) + T(80, y + 1, str(i + 1), 16, 700, '#fff', 'middle') + T(112, y, s, 17, 600, INK)
    g += F(i + 1, blk)
g += F(4, L(60, 290, 1120, 290, LINE, 2) + T(60, 325, 'Not claimed today', 19, 700, AC2))
nc = ['a graph is the one true description', 'the delta graph traces causal paths (it detects)', 'a circuit level account of a music model', 'the data graph shown is inside the model']
for i, s in enumerate(nc):
    x = 60 + (i % 2) * 540; y = 365 + (i // 2) * 44
    g += F(5, T(x, y, '✗  ' + s, 16, 600, MUT))
B.append(sec('What would make me drop the graph', SVG(g), ch='3'))

# ---------------- Close ----------------
CL = []
g = adefs('c1')
ox, oy = 90, 400
g += L(ox, oy, 640, oy, INK, 2, 'marker-end="url(#axk)"') + L(ox, oy, ox, 50, INK, 2, 'marker-end="url(#axk)"')
g += T(370, oy + 34, 'time', 16, 700, MU, 'middle') + T(ox - 18, 225, 'depth', 16, 700, ACC, 'middle', f'transform="rotate(-90 {ox-18} 225)"')
cx_ = [140 + i * 95 for i in range(6)]; ry_ = [360 - j * 72 for j in range(5)]
for x in cx_:
    for y in ry_:
        g += C(x, y, 7, '#fff', '#c9d0d5', 2)
g += ''.join(L(cx_[1], ry_[j] - 7, cx_[1], ry_[j + 1] + 7, ACC, 4) for j in range(4)) + ''.join(C(cx_[1], y, 8, ACC) for y in ry_)
g += ''.join(P(f'M{cx_[i]+8},{ry_[1]} L{cx_[i+1]-10},{ry_[1]}', MU, 4, extra='marker-end="url(#c1t)"') for i in range(5)) + ''.join(C(x, ry_[1], 8, MU) for x in cx_)
g += R(700, 60, 450, 110, ACL, ACC, 1.5, 10) + T(720, 92, 'Depth, language', 18, 700, ACC) + T(720, 118, 'a delta graph catches edits that pass', 14.5, 400, INK) + T(720, 140, 'their own test but break other behavior', 14.5, 400, INK) + tag(980, 75, 'published', 'done')
g += F(1, R(700, 190, 450, 110, MUL, MU, 1.5, 10) + T(720, 222, 'Time, music', 18, 700, MU) + T(720, 248, 'styles look like islands, steering', 14.5, 400, INK) + T(720, 270, 'is one way, the in model graph is next', 14.5, 400, INK) + tag(980, 205, 'in progress', 'part'))
g += F(2, R(700, 320, 450, 80, '#fff', INK, 2, 10) + T(925, 352, 'Propagation and reachability:', 17, 700, INK, 'middle') + T(925, 378, 'classic graph questions, new object', 15, 400, MUT, 'middle'))
CL.append(sec('Two hidden graphs, one question', SVG(g), ch='4', cls='divider'))

g = adefs('c2')
cx, cy = 590, 245
g += C(cx, cy, 82, ACL, ACC, 3) + T(cx, cy - 6, 'hidden graphs', 17, 700, ACC, 'middle') + T(cx, cy + 16, 'in generative models', 15, 400, INK, 'middle')
areas = [('Knowledge graphs', 'edit a model like a database update?', 'Test'), ('NLP', 'which behaviors should an edit be tested on?', 'Build'),
         ('AutoML', 'score pruning and merging before full evaluation?', 'Generalize'), ('Theory', 'which discretization keeps reachability?', 'Generalize'),
         ('Systems and data', 'store activation graphs at scale?', 'Build'), ('Security', 'do malicious edits leave a graph fingerprint?', 'Test')]
for i, (a, q, stp) in enumerate(areas):
    ang = -math.pi / 2 + i * 2 * math.pi / 6
    x, y = cx + 390 * math.cos(ang), cy + 178 * math.sin(ang)
    blk = L(cx + 82 * math.cos(ang), cy + 82 * math.sin(ang), x - 70 * math.cos(ang), y - 34 * math.sin(ang), AC2, 2)
    blk += R(x - 170, y - 36, 340, 70, SOFT, LINE, 1, 8) + T(x - 155, y - 10, a, 16, 700, AC2) + T(x - 155, y + 16, q, 13.5, 400, INK)
    blk += R(x + 70, y - 28, 88, 22, '#fff', ACC, 1.2, 11) + T(x + 114, y - 12.5, stp, 12, 700, ACC, 'middle')
    g += F(i + 1, blk)
CL.append(sec('Where I would love your help', SVG(g), ch='4'))
CL.append(music.CLOSE[3].replace('data-ch="6"', 'data-ch="4"'))

# ---------------- Music, merged and new ----------------
MS = music.S
def rech(s, c):
    return re.sub(r'data-ch="[^"]*"', f'data-ch="{c}"', s, count=1)

# merged: Markov and score
g = adefs('mm')
nodes = {'C': (110, 230), 'D': (210, 140), 'E': (310, 230), 'G': (210, 320)}
for a, b in [('C', 'D'), ('D', 'E'), ('E', 'G'), ('G', 'C'), ('C', 'E')]:
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    g += L(x1, y1, x2, y2, '#9aa6ae', 2.5)
for n, (x, y) in nodes.items():
    g += C(x, y, 22, '#fff', AC2, 2.5) + T(x, y + 6, n, 17, 700, AC2, 'middle')
pd = 'M110,230 L210,140 L310,230 L210,320 Z'
g += f'<circle r="9" fill="{ACC}"><animateMotion dur="4s" repeatCount="indefinite" path="{pd}"/></circle>'
g += T(210, 70, 'The graph IS the generator', 18, 700, AC2, 'middle') + T(210, 380, '1957 Illiac Suite: Markov chains', 14, 600, INK, 'middle') + T(210, 402, '2003 Continuator: learn a player\'s style', 14, 400, INK, 'middle') + T(210, 424, '2011 Markov constraints: exact control', 14, 700, ACC, 'middle')
right = T(800, 70, 'The graph DESCRIBES the score', 18, 700, AC2, 'middle')
for k in range(5):
    right += L(500, 140 + k * 14, 700, 140 + k * 14, '#9aa6ae', 1)
nts = [(530, 196), (580, 182), (630, 168), (680, 182)]
right += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="7" fill="{INK}"/>' for x, y in nts)
right += P('M710,170 L760,170', ACC, 3, extra='marker-end="url(#mmo)"')
gx = [(800, 200), (860, 150), (920, 200), (980, 150), (1040, 210), (1100, 160)]
for a, b in [(0, 1), (1, 2), (2, 3), (1, 3), (3, 4), (4, 5), (3, 5)]:
    right += L(gx[a][0], gx[a][1], gx[b][0], gx[b][1], ACC, 2.5)
right += ''.join(C(x, y, 9, '#fff', ACC, 2.5) for x, y in gx)
right += T(800, 270, 'notes and bars become nodes for a GNN', 14, 400, MUT, 'middle')
wk = [('Jeong 2019', 'performance'), ('PopMNet 2020', 'melody'), ('Karystinaios 2022', 'cadences'), ('Polyphemus 2023', 'multitrack'), ('Lim 2024', 'pop songs'), ('SMUG-explain 2024', 'explanations')]
for i, (n, u) in enumerate(wk):
    x = 480 + (i % 3) * 225; y = 300 + (i // 3) * 58
    right += R(x, y, 210, 48, SOFT, LINE, 1, 8) + T(x + 105, y + 21, n, 13.5, 700, AC2, 'middle') + T(x + 105, y + 39, u, 12.5, 400, MUT, 'middle')
g += F(1, L(440, 50, 440, 430, LINE, 2) + right)
g += F(2, T(590, 465, 'Visible graph: exact control. Graph in the data: says nothing about the model.', 17, 700, ACC, 'middle'))
MERGE_MS = sec('Before neural generators: the graph was visible', SVG(g), ch='2',
               ref='Hiller and Isaacson 1959. Pachet, JNMR 2003. Pachet and Roy, Constraints 2011. Jeong et al., ICML 2019. Karystinaios and Widmer, ISMIR 2022. Cosenza et al., 2023. Lim, Liang, Zhang, 2024')

# MusicGen anatomy
g = adefs('an')
g += R(40, 180, 140, 64, '#fff', AC2, 2, 8) + T(110, 208, 'text', 15, 700, AC2, 'middle') + T(110, 228, 'T5 encoder', 13, 400, MUT, 'middle')
g += R(240, 90, 300, 250, '#fff', '#9aa6ae', 2, 10) + T(390, 125, 'transformer decoder', 17, 700, INK, 'middle') + T(390, 148, 'small 300M, medium 1.5B, large 3.3B', 13, 400, MUT, 'middle')
for k in range(5):
    g += R(270, 165 + k * 32, 240, 24, SOFT, LINE, 1, 4)
g += P('M180,212 C210,212 220,250 268,250', AC2, 2, extra='marker-end="url(#ana)" stroke-dasharray="5 4"') + T(200, 280, 'cross attention', 12.5, 600, AC2, 'middle')
for r in range(4):
    for c in range(6):
        g += R(600 + c * 28 + r * 28, 140 + r * 30, 24, 24, ['#1f8a9a', '#4fa9b6', '#86c6cf', '#bfe1e5'][r], 'none', 0, 3)
g += T(740, 120, 'tokens: 4 codebooks, 50 per second', 14, 700, MU, 'middle')
g += P('M540,215 L590,215', AC2, 2.5, extra='marker-end="url(#ana)"') + P('M760,330 C700,400 420,400 390,345', MU, 2.5, extra='marker-end="url(#ant)"') + T(580, 405, 'each step feeds the next', 13, 600, MU, 'middle')
facts = [('discrete tokens', 'a token graph for free'), ('coarse to fine codebooks', 'layered graph: style at which level?'), ('one step feeds the next', 'a trajectory is a path'),
         ('text enters every step', 'conditioning reweights all edges'), ('guidance: cond minus uncond', 'two graphs and a knob between them')]
fx = 880
for i, (a, b) in enumerate(facts):
    y = 70 + i * 74
    blk = R(fx, y, 285, 62, MUL if i != 4 else ACL, MU if i != 4 else ACC, 1.3, 8) + T(fx + 12, y + 24, a, 14, 700, INK) + T(fx + 12, y + 46, '→ ' + b, 13, 400, MU if i != 4 else ACC)
    g += F(i + 1, blk)
g += F(6, T(450, 460, 'Five facts, five graphs you can build and test.', 18, 700, ACC, 'middle'))
ANAT = sec('MusicGen anatomy: what invites a graph', SVG(g), ch='2',
           ref='Copet et al., Simple and Controllable Music Generation, NeurIPS 2023. Défossez et al., EnCodec, 2022',
           notes='Facts: 32 kHz audio, 50 Hz frames, 4 residual codebooks of 2048 entries with a delay interleaving pattern, T5 text conditioning through cross attention, classifier free guidance at inference. Delay interleaving means hidden states at one step mix four time offsets, so states must be aligned to the first codebook. At 50 Hz self transitions dominate, so the graph needs a lag sweep.')

# three vector tools
g = adefs('tt')
cols3 = [('Probe', 'is it encoded?', 'Wei et al. ISMIR 2024', 'tempo, notes, chords decodable, peaks mid depth'),
         ('Steer', 'can we push it?', '2025, Zhao et al. ICLR 2026', 'note accuracy 0.23 to 0.82, large push breaks audio'),
         ('Dictionary', 'which concepts exist?', 'Singh et al. 2025, Paek et al. 2025', 'sparse features, some unnamed by theory')]
for i, (a, q, cite, res) in enumerate(cols3):
    x = 40 + i * 380
    blk = R(x, 50, 350, 390, '#fff', LINE, 1.5, 10) + T(x + 175, 88, a, 22, 700, AC2, 'middle') + T(x + 175, 114, q, 15, 600, INK, 'middle')
    if i == 0:
        random.seed(2)
        for k in range(18):
            px, py = x + 60 + random.uniform(0, 230), 150 + random.uniform(0, 160)
            blk += C(px, py, 6, ACC if (py - 150) > (px - x - 60) * 0.7 else MU)
        blk += L(x + 50, 140, x + 300, 320, INK, 2.5, 'stroke-dasharray="7 5"')
    elif i == 1:
        blk += P(f'M{x+30},300 C{x+120},250 {x+220},280 {x+330},220 L{x+330},280 C{x+220},320 {x+120},330 {x+30},340 Z', 'none', 0, MUL)
        blk += C(x + 90, 315, 8, INK) + P(f'M{x+90},315 L{x+170},275', ACC, 3.5, extra='marker-end="url(#tto)"') + P(f'M{x+90},315 L{x+270},170', ACC, 3, extra='marker-end="url(#tto)" stroke-dasharray="8 5"')
        blk += T(x + 280, 165, 'cliff', 13, 700, ACC)
    else:
        for k in range(22):
            h = 110 if k in (3, 9, 15) else (80 if k == 19 else 3)
            blk += R(x + 40 + k * 12.5, 320 - h, 9, h, ACC if k in (3, 9, 15) else (MU if k == 19 else '#d3d7da'), 'none', 0, 2)
    blk += T(x + 175, 368, cite, 13, 700, AC2, 'middle') + T(x + 175, 392, res, 12.5, 400, INK, 'middle')
    g += F(i, blk) if i else blk
g += F(3, T(590, 470, 'Three tools, three questions, all at one layer and one moment.', 17, 700, ACC, 'middle'))
TOOLS = sec('Inside MusicGen today: three vector tools', SVG(g), ch='2',
            ref='Wei, Freeman, Donahue, Sun, ISMIR 2024. arXiv 2504.04479. Zhao et al., ICLR 2026. Singh, Cherep, Maes, arXiv 2505.18186. Paek et al., arXiv 2510.23802')

# next experiment with result matrix
g = adefs('nx')
steps = [('record', 'mid layer, every step'), ('discretize', '100 to 500 states'), ('connect', 'transitions, lag sweep'), ('test', 'communities, reachability')]
for i, (a, b) in enumerate(steps):
    x = 40 + i * 180
    g += R(x, 50, 160, 70, SOFT, AC2, 1.5, 10) + T(x + 80, 80, a, 16, 700, AC2, 'middle') + T(x + 80, 102, b, 12.5, 400, INK, 'middle')
    if i < 3:
        g += P(f'M{x+162},85 L{x+178},85', AC2, 2.5, extra='marker-end="url(#nxa)"')
g += T(780, 70, 'controls', 15, 700, MUT) + tag(780, 82, 'same graph on output tokens', 'plan') + tag(780, 110, 'shuffled style labels', 'plan') + tag(980, 110, 'loudness, position', 'plan')
mx, my = 330, 170
g += T(mx + 260, my - 6, 'steered trajectories reach target states?', 15, 700, INK, 'middle')
g += T(mx - 20, my + 140, 'styles form communities?', 15, 700, INK, 'middle', f'transform="rotate(-90 {mx-20} {my+140})"')
g += T(mx + 130, my + 22, 'yes', 14, 700, MUT, 'middle') + T(mx + 390, my + 22, 'no', 14, 700, MUT, 'middle')
g += T(mx + 10, my + 85, 'yes', 14, 700, MUT, 'end') + T(mx + 10, my + 205, 'no', 14, 700, MUT, 'end')
cells = [('islands, and steering can cross', 'graph explains success', GRN, '#eaf3ea'), ('islands, steering cannot enter', 'one way is a reachability fact', ACC, ACL),
         ('no islands, steering works', 'style is a direction after all', AC2, SOFT), ('no islands, steering fails', 'style lives in finer geometry', MU, MUL)]
for i, (a, b, col, fill) in enumerate(cells):
    x = mx + 20 + (i % 2) * 260; y = my + 35 + (i // 2) * 120
    g += F(i + 1, R(x, y, 250, 110, fill, col, 2, 10) + T(x + 125, y + 46, a, 14.5, 700, INK, 'middle') + T(x + 125, y + 72, b, 13.5, 400, col, 'middle'))
g += F(5, T(590, 470, 'Every cell is a result. None of them is a rescue.', 18, 700, INK, 'middle'))
NEXT = sec('Next: the graph inside MusicGen', SVG(g), ch='2', status='prog')

MUSIC = [rech(MS[0], '2'), rech(MS[1], '2'), MERGE_MS, rech(MS[4], '2'), ANAT, TOOLS, rech(MS[8], '2'), rech(MS[9], '2'), rech(MS[10], '2'), rech(MS[11], '2'), rech(MS[13], '2'), NEXT]
MUSIC[0] = MUSIC[0].replace('<section class="divider" data-ch="2">','<section data-ch="2">').replace('5. Music: where does a style live?', 'Graphs in music: four stages')

# ---------------- Part 1 divider ----------------
g = adefs('p1')
g += axis_icon(90, 110, 2.0, 'part', 'plan')
road = R(520, 60, 630, 340, SOFT, LINE, 1, 10) + T(545, 95, 'Part 1 in four steps', 18, 700, ACC)
its = [('A model is already many graphs', 'weights, co-activation, circuits'), ('Every surgery is an arrow', 'fine-tune, steer, edit: one kind of object'),
       ('The arrow passes its test', 'side effects hide outside the exam'), ('Our answer: a delta graph', 'how the blocks rewire after the change')]
for i, (a, b) in enumerate(its):
    y = 145 + i * 64
    road += F(i + 1, C(555, y - 5, 13, ACC) + T(555, y + 0, str(i + 1), 13, 700, '#fff', 'middle') + T(580, y, a, 16, 700, INK) + T(580, y + 22, b, 14, 400, MUT))
g += road + T(240, 380, 'one moment, across blocks', 16, 700, ACC, 'middle')
P1DIV = sec('Part 1. Depth: what an edit does inside a language model', SVG(g), ch='1', cls='divider')
