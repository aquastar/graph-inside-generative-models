"""Final assembly for the talk: new slides, reshaped slides, and the 42 slide order.

Vision 8, Language 11, Music 17 (four on music and the brain), Beyond 3, Close 3.
Reuses the drawing helpers and slides built in music.py and vision.py.
"""
import math, re
from music import T, R, C, L, P, F, chip, defs, SVG, sec, mini_lattice, INK, MUT, ACC, AC2, MU, LINE, SOFT, MUL, ACL
import music
import vision as VZ
from vision import adefs, tag, axis_icon, GRN

GRY = '#9aa6ae'

def img(x, y, w, h, src, extra=''):
    return f'<image href="{src}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" {extra}/>'

def ph(x, y, w, h, a, b=''):
    out = R(x, y, w, h, '#fafbfb', '#b8c0c6', 2, 8, 'stroke-dasharray="8 6"') + T(x + w / 2, y + h / 2 - (6 if b else -5), a, 15, 700, MUT, 'middle')
    if b:
        out += T(x + w / 2, y + h / 2 + 18, b, 13, 400, MUT, 'middle')
    return out

def wrap(x, y, s, size=14, w=400, fill=INK, a='start', width=40, lh=None):
    lh = lh or size * 1.35
    words, lines, cur = s.split(), [], ''
    for wd in words:
        if len(cur) + len(wd) + 1 > width and cur:
            lines.append(cur); cur = wd
        else:
            cur = (cur + ' ' + wd).strip()
    lines.append(cur)
    return ''.join(T(x, y + i * lh, ln, size, w, fill, a) for i, ln in enumerate(lines))

def secx(title, svg, ch, status='', ref='', notes='', cls=''):
    """sec() plus a Planned status label"""
    if status == 'plan':
        s = sec(title, svg, ch=ch, ref=ref, notes=notes, cls=cls)
        return s.replace('</h2>', '</h2><span class="status plan">Planned</span>', 1)
    return sec(title, svg, ch=ch, status=status, ref=ref, notes=notes, cls=cls)

# ======================= VISION =======================

# ---- same machine, two instruments ----
g = adefs('sm')
def stack(x, col, top, bot, tok):
    out = R(x, 130, 300, 210, '#fff', col, 2, 10)
    for k in range(5):
        out += R(x + 30, 150 + k * 36, 240, 26, SOFT, LINE, 1, 4)
    out += T(x + 150, 368, 'transformer, next token', 15, 700, col, 'middle')
    out += T(x + 150, 70, top, 17, 700, INK, 'middle') + P(f'M{x+150},80 L{x+150},126', col, 2.5, extra=f'marker-end="url(#sm{"o" if col == ACC else "t"})"')
    out += R(x + 40, 395, 220, 34, ACL if col == ACC else MUL, col, 1.5, 17) + T(x + 150, 418, tok, 15, 700, col, 'middle')
    return out
g += stack(60, ACC, '"The CEO of Apple is"', '', 'word tokens')
g += F(1, stack(820, MU, '"upbeat jazz with piano"', '', 'audio tokens, 50 per second'))
mid = R(430, 150, 320, 170, SOFT, AC2, 2, 10) + T(590, 186, 'Same tools apply', 18, 700, AC2, 'middle')
for i, s in enumerate(['edit weights', 'steer activations', 'probe a layer', 'read a graph?']):
    mid += T(590, 218 + i * 26, s, 15, 700 if i == 3 else 400, ACC if i == 3 else INK, 'middle')
mid += P('M428,235 L366,235', AC2, 2.5, extra='marker-end="url(#sma)"') + P('M752,235 L814,235', AC2, 2.5, extra='marker-end="url(#sma)"')
g += F(2, mid)
g += F(3, T(590, 470, 'One architecture, two kinds of knowledge: facts and styles.', 19, 700, INK, 'middle'))
SAME = sec('Same machine, two instruments', SVG(g), ch='0',
           ref='Language: GPT style decoders. Music: Copet et al., MusicGen, NeurIPS 2023',
           notes='A language model and MusicGen are the same kind of object: a decoder only transformer that predicts the next discrete token. Anything we do to one, editing, steering, probing, we can do to the other. That is why one graph method can be tested on both.')

# ---- facts versus styles ----
g = adefs('fs')
g += T(330, 50, 'A fact', 22, 700, ACC, 'middle') + T(850, 50, 'A style', 22, 700, MU, 'middle')
rows = [('unit', 'one triple: Apple, CEO, Cook', 'a whole piece, minutes long'),
        ('where it acts', 'depth: one moment, many blocks', 'time: one layer, many steps'),
        ('how we change it', 'edit the weights', 'steer the activations'),
        ('what fails', 'passes its test, breaks a neighbor', 'removing works, adding fails'),
        ('who checks', 'a benchmark with an answer key', 'no answer key: an outside judge')]
for i, (k, a, b) in enumerate(rows):
    y = 100 + i * 66
    blk = T(60, y + 22, k, 15, 700, MUT) + R(200, y, 400, 46, ACL, ACC, 1.2, 8) + T(400, y + 29, a, 15.5, 600, INK, 'middle')
    blk += R(650, y, 400, 46, MUL, MU, 1.2, 8) + T(850, y + 29, b, 15.5, 600, INK, 'middle')
    g += F({0: 0, 1: 1, 2: 1, 3: 2, 4: 3}[i], blk) if i else blk
g += F(4, T(590, 460, 'A fact has an answer key. A style needs a judge that did not write the exam.', 18, 700, INK, 'middle'))
FACTS = sec('Facts versus styles', SVG(g), ch='0',
            notes='Five contrasts. The last row sets up the brain part: a style has no ground truth, so we need a measurement that is independent of the model and of us.')

# ---- three networks ----
g = adefs('tn')
pan = [(50, 'The music', 'states and transitions in scores', 'measured from data', AC2), (440, 'The model', 'states inside the generator', 'the hypothesis we test', ACC), (830, 'The listener', 'brain responses to the audio', 'the measuring instrument', MU)]
def panel(x0, a, b, c, col, i):
    x = x0 - 10
    out = R(x0, 60, 300, 290, '#fff', col, 2, 12) + T(x0 + 150, 98, a, 21, 700, col, 'middle')
    if i == 0:
        pts = [(x + 90, 190), (x + 160, 150), (x + 230, 190), (x + 200, 260), (x + 120, 260)]
        for p1, p2 in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)]:
            out += L(*pts[p1], *pts[p2], GRY, 2)
        out += ''.join(C(px, py, 10, '#fff', AC2, 2.5) for px, py in pts)
    elif i == 1:
        out += mini_lattice(x + 90, 150, 5, 4, 36, 34, '#b8c0c6')
        out += P(f'M{x+90},150 L{x+126},218 L{x+162},184 L{x+198},252 L{x+234},218', ACC, 3.5)
    else:
        out += f'<path d="M{x+90},250 C{x+70},170 {x+150},130 {x+200},150 C{x+260},150 {x+270},220 {x+230},250 Z" fill="{MUL}" stroke="{MU}" stroke-width="2.5"/>'
        out += P(f'M{x+80},300 ' + ' '.join(f'L{x+80+k*12},{300 + (12 if k % 2 else -12) * (1 if k % 3 else .4)}' for k in range(1, 15)), MU, 2)
    out += T(x0 + 150, 330, b, 14, 600, INK, 'middle')
    return out + T(x0 + 150, 375, c, 15, 700, col, 'middle')
g += panel(*pan[0][:5], 0)
g += F(1, panel(*pan[1][:5], 1) + P('M354,200 L436,200', AC2, 2.5, extra='marker-end="url(#tna)"') + T(395, 188, 'trained on', 13, 600, MUT, 'middle'))
g += F(2, panel(*pan[2][:5], 2) + P('M744,200 L826,200', AC2, 2.5, extra='marker-end="url(#tna)"') + T(785, 188, 'heard by', 13, 600, MUT, 'middle'))
g += F(3, R(150, 405, 880, 60, ACL, ACC, 1.5, 10) + T(590, 433, 'We do not model the brain. We use it to judge the graph we read out of the model.', 17, 700, INK, 'middle') + T(590, 455, 'does the model graph predict what listeners track, better than the data graph or a vector?', 14, 400, MUT, 'middle'))
THREE = sec('Three networks: the music, the model, the listener', SVG(g), ch='0',
            notes='Keep the roles straight. The music graph is measured from data. The model graph is the hypothesis. The listener is an instrument, not a modeling target. This is what makes a style testable without an answer key.')

# ---- network science table, with the encoding row ----
g = adefs('v3')
g += T(70, 40, 'Network science concept', 15, 700, MUT) + T(470, 40, 'Question about a generative model', 15, 700, MUT) + T(930, 40, 'In this talk', 15, 700, MUT) + L(60, 52, 1120, 52, INK, 2)
rows = [('Diffusion and cascades', 'does an edit spread beyond its target?', 'Part 1, depth', ACC),
        ('Partial correlation networks', 'which blocks start working together after a change?', 'Part 1, delta graph', ACC),
        ('Communities and modularity', 'is a musical style a module of states?', 'Part 2, time', MU),
        ('Reachability and hitting time', 'can steering reach a style from here?', 'Part 2, time', MU),
        ('Encoding models', 'do model states predict brain responses?', 'Part 2, judge', MU),
        ('Resilience to edge removal', 'which surgery breaks the structure?', 'Part 3, model math', AC2),
        ('Markov state models', 'what are the slow states of a generator?', 'Part 3, dynamics', AC2)]
grp = [0, 0, 1, 1, 2, 3, 3]
for i, (a, b, c, col) in enumerate(rows):
    y = 88 + i * 50
    blk = C(78, y - 5, 7, col) + T(96, y, a, 16, 700, INK) + T(470, y, b, 15.5, 400, INK) + R(930, y - 18, 170, 26, '#fff', col, 1.5, 13) + T(1015, y, c, 13, 700, col, 'middle') + L(60, y + 20, 1120, y + 20, LINE, 1)
    g += F(grp[i], blk) if grp[i] else blk
g += F(4, T(590, 460, 'Not new mathematics. Old network questions asked of a new object.', 18, 700, ACC, 'middle'))
NETSCI = sec('Why a graph: questions network science already knows how to ask', SVG(g), ch='0')

# ---- the program, with the judge row ----
g = adefs('v4')
boxes = [('Build', 'read a graph out of activations', 'cluster, correlate, count'),
         ('Test', 'does it predict an intervention?', 'better than a vector can'),
         ('Generalize', 'same questions, more generators', 'every surgery, every sequence')]
top = ''
for i, (a, b, c) in enumerate(boxes):
    x = 40 + i * 380
    top += R(x, 30, 340, 110, SOFT, AC2, 2, 10) + T(x + 170, 66, a, 24, 700, AC2, 'middle') + T(x + 170, 96, b, 15, 600, INK, 'middle') + T(x + 170, 120, c, 14, 400, MUT, 'middle')
    if i < 2:
        top += P(f'M{x+342},85 L{x+376},85', AC2, 3, extra='marker-end="url(#v4a)"')
g += top
g += F(1, T(30, 186, 'depth', 16, 700, ACC) + L(20, 160, 1160, 160, LINE, 1) + tag(110, 172, 'done: delta graph across blocks', 'done') + tag(470, 172, 'done: AUC 0.70 to 0.80, shape beats size', 'done') + tag(840, 172, 'planned: six model operations', 'plan'))
g += F(2, T(30, 250, 'time', 16, 700, MU) + L(20, 224, 1160, 224, LINE, 1) + tag(110, 236, 'part: data graph, model graph next', 'part') + tag(470, 236, 'part: one way steering, under review', 'part') + tag(840, 236, 'planned: time series, video', 'plan'))
g += F(3, T(30, 314, 'judge', 16, 700, INK) + L(20, 288, 1160, 288, LINE, 1) + L(20, 352, 1160, 352, LINE, 1) + tag(110, 300, 'part: steering pilot, tempo dose', 'part') + tag(470, 300, 'planned: listener EEG per layer', 'plan') + tag(840, 300, 'planned: brain as judge of graphs', 'plan'))
g += F(4, R(160, 380, 860, 70, ACL, ACC, 1.5, 10) + T(590, 411, 'A graph earns its place only by predicting what a vector cannot.', 19, 700, ACC, 'middle') + T(590, 435, 'For a style, the prediction is checked by a listener.', 15, 400, INK, 'middle'))
PROGRAM = sec('The program: build, test, generalize', SVG(g), ch='0',
              notes='Green is done, orange is partial, dashed is planned. The new third row is the judge: an outside measurement for the cases with no answer key.')

# ======================= LANGUAGE =======================
OLD_SHAPE_LIMITS = None  # built below

g = adefs('sl')
g += T(30, 34, 'Same probes, same before and after difference, scored differently', 15, 700, INK) + T(30, 56, 'AUC on 1,761 edits that pass the benchmark', 13, 400, MUT)
bars = [('single numbers, no graph', 0.555, '0.52 to 0.59', '#c9d0d5'), ('editor and model only', 0.705, '0.705', AC2), ('plus best single number', 0.752, '0.752', GRY), ('plus full delta graph', 0.798, '0.798', ACC)]
x0, x1 = 250, 640
sc = lambda v: x0 + (v - 0.5) / 0.35 * (x1 - x0)
for i, (lab, v, s, col) in enumerate(bars):
    y = 82 + i * 52
    blk = T(x0 - 10, y + 20, lab, 14, 700 if i == 3 else 600, ACC if i == 3 else INK, 'end') + R(x0, y + 2, sc(v) - x0, 28, col, 'none', 0, 3) + T(sc(v) + 8, y + 22, s, 14, 700, INK)
    g += F(1, blk) if i == 3 else blk
g += L(x0, 76, x0, 296, '#c0392b', 2, 'stroke-dasharray="5 4"') + T(x0, 314, '0.5 chance', 12, 700, '#c0392b', 'middle')
g += F(1, R(30, 334, 620, 60, ACL, ACC, 1.5, 8) + T(340, 360, 'Not how much the inside changed,', 16, 700, ACC, 'middle') + T(340, 382, 'but how the connections rearranged.', 16, 700, ACC, 'middle'))
lim = [('Strong on Qwen, weaker on Llama', 'AUC 0.847 vs 0.677. On Llama almost every passing edit fails, so little is left to separate.'),
       ('Cheaper, not more accurate', 'Reading outputs scores 0.984 but costs a generation per edit. Triage the riskiest 20% first.'),
       ('Catches about a third', 'Checking 20% finds about 300 of 987 bad edits. The value is in what to check first.'),
       ('Nothing to catch on CounterFact', 'Those edits fail or succeed deeply. A scope boundary, not a counterexample.')]
for i, (a, b) in enumerate(lim):
    y = 30 + i * 92
    blk = R(700, y, 450, 80, SOFT, LINE, 1, 8) + T(716, y + 26, a, 15.5, 700, AC2) + wrap(716, y + 49, b, 13, 400, INK, width=62, lh=18)
    g += F(2 if i < 2 else 3, blk)
g += F(4, T(590, 460, 'A graph signal that a single number cannot give, with honest limits.', 18, 700, INK, 'middle'))
SHAPE = sec('Shape beats size, and where it stops', SVG(g), ch='1', status='pub',
            ref='Benbrahim et al., SDM 2026, Table F.1, Tables 5.1, 5.2 and 5.5, Sections 5.2 to 5.6',
            notes='Five single numbers: max edge change 0.589, mean 0.572, total 0.575, top 5 node share 0.564, top 1 node share 0.521. On 500 unseen facts the AUC holds at 0.840 to 0.862. Only 2 of the 50 riskiest flip when rerun. Labels depend on which 12 held out prompts define failure. Scale: 7B and 8B models, three editors, two benchmark families.')

# ---- bridge to time, with the outside judge ----
g = adefs('b1')
g += axis_icon(90, 90, 2.0, 'done', 'plan')
g += T(240, 360, 'depth: done for one moment', 16, 700, ACC, 'middle') + T(240, 384, 'time: not touched yet', 16, 700, MUT, 'middle')
why = R(520, 60, 630, 330, SOFT, LINE, 1, 10) + T(545, 95, 'Why music is the right test for the time axis', 18, 700, MU)
items = [('Long trajectories', '30 seconds of audio is 1,500 generation steps at 50 Hz'),
         ('Steering is the control', 'no weight edit, every intervention acts along time'),
         ('Discrete outputs for free', 'audio tokens give a reference graph to compare against'),
         ('No ground truth', 'a style has no answer key, it needs an outside judge')]
for i, (a, b) in enumerate(items):
    y = 140 + i * 62
    why += F(i + 1, C(555, y - 5, 7, ACC if i == 3 else MU) + T(575, y, a, 16, 700, ACC if i == 3 else INK) + T(575, y + 22, b, 14, 400, MUT))
g += why
g += F(4, T(590, 450, 'Language gave the depth case. Music forces the time case, and a judge.', 19, 700, INK, 'middle'))
BRIDGE = sec('From depth to time', SVG(g), ch='2', cls='divider')

# ======================= MUSIC =======================

def rech(s, c):
    return re.sub(r'data-ch="[^"]*"', f'data-ch="{c}"', s, count=1)

FOUR = VZ.MUSIC[0]  # four stages, moving ball removed by the global pass in build.py

def fe(act, title, side, take, notes):
    g = adefs('fe' + act[0])
    g += f'<foreignObject x="20" y="10" width="760" height="420"><div xmlns="http://www.w3.org/1999/xhtml" style="width:760px;height:420px"><iframe class="fe-frame" data-src="figs/fe-chain.html?act={act}&amp;autoplay=1" title="Für Elise Markov chain, {act}" style="width:760px;height:420px;border:0;background:#fff" loading="lazy"></iframe></div></foreignObject>'
    for i, (a, b) in enumerate(side):
        y = 50 + i * 120
        g += F(i + 1, R(810, y, 350, 100, MUL if i < 2 else ACL, MU if i < 2 else ACC, 1.5, 10) + T(830, y + 32, a, 17, 700, MU if i < 2 else ACC) + wrap(830, y + 58, b, 14, 400, INK, width=42, lh=19))
    g += F(4, T(590, 465, take, 18, 700, INK, 'middle'))
    return sec(title, SVG(g), ch='2', ref='Opening of Beethoven, Für Elise. Animation from zhiqian.ai, click it for sound', notes=notes)

FE_LEARN = fe('learn', 'A melody is a walk on a graph',
              [('Nodes are notes', 'nine pitches in the opening, placed by pitch'), ('Every move draws an arrow', 'a repeated move makes the arrow thicker'), ('Learning is counting', 'arrow weights become transition probabilities')],
              'Learning a first order Markov chain means counting the walks.',
              'Let the ball run once through the opening. Point at E5 and D#5: the trill makes that pair of arrows the thickest. Nothing here is neural. The graph is the whole model.')
FE_COMPOSE = fe('compose', 'The graph composes',
                [('A spinner at every note', 'wedges are the outgoing probabilities'), ('The needle picks the next note', 'one random step on the graph'), ('Every choice is visible', 'so every choice can be steered')],
                'When the graph is the generator, control is a graph question.',
                'The chain now writes a tune Beethoven never wrote. Right notes, wrong syntax: we come back to that on the next slides. Click the animation for sound.')

# ---- 144 numbers name the corpus ----
styles = ['Bach chorale', 'Essen folk song', 'Monteverdi', 'Palestrina', "Ryan's fiddle", 'Trecento']
conf = [[66, 9, 2, 20, 2, 2], [16, 62, 2, 4, 13, 4], [1, 4, 80, 11, 0, 3], [20, 4, 0, 71, 2, 3], [4, 8, 0, 2, 82, 2], [5, 4, 0, 19, 5, 67]]
g = adefs('cm')
pipe = [('one piece', 'monophonic melody'), ('12 by 12 table', 'scale degree transitions'), ('144 numbers', 'no music theory'), ('logistic regression', 'names the corpus')]
for i, (a, b) in enumerate(pipe):
    y = 40 + i * 92
    g += R(30, y, 230, 64, SOFT, AC2, 1.5, 10) + T(145, y + 28, a, 16, 700, AC2, 'middle') + T(145, y + 50, b, 13, 400, MUT, 'middle')
    if i < 3:
        g += P(f'M145,{y+66} L145,{y+88}', AC2, 2.5, extra='marker-end="url(#cma)"')
mx, my, cs = 470, 64, 50
cm = T(mx + 3 * cs, my - 40, 'predicted corpus', 13, 700, MUT, 'middle') + T(mx - 150, my + 3 * cs + 4, 'true', 13, 700, MUT, 'middle')
for i, s in enumerate(styles):
    cm += T(mx - 10, my + i * cs + 30, s, 13, 600, INK, 'end')
    cm += T(mx + i * cs + 25, my - 10, s.split()[0][:7], 11.5, 600, MUT, 'middle')
    for j in range(6):
        v = conf[i][j]
        fill = ACC if i == j else ('#fbd3b4' if v >= 10 else '#f4f5f6')
        cm += R(mx + j * cs, my + i * cs, cs - 3, cs - 3, fill, 'none', 0, 3) + T(mx + j * cs + 23, my + i * cs + 30, str(v), 14, 700, '#fff' if i == j else INK, 'middle')
g += F(1, cm)
g += F(2, R(820, 70, 330, 120, ACL, ACC, 1.5, 10) + T(985, 128, '70.9%', 44, 700, ACC, 'middle') + T(985, 166, 'five fold accuracy, baseline 20%', 14, 600, INK, 'middle'))
g += F(3, R(820, 210, 330, 150, '#fff', LINE, 1.5, 10) + T(840, 240, 'Confusions make musical sense', 15, 700, AC2) + T(840, 268, 'Bach and Palestrina swap about 20%', 13.5, 400, INK) + T(840, 292, 'folk and fiddle swap 13 to 16%', 13.5, 400, INK) + T(840, 316, 'Monteverdi and fiddle: never', 13.5, 400, INK) + T(840, 344, 'row normalized, percent', 12, 400, MUT))
g += F(4, T(590, 465, 'A first order graph already carries a style. 144 numbers name the corpus.', 18, 700, INK, 'middle'))
CORPUS = sec('144 numbers name the corpus', SVG(g), ch='2', status='prog',
             ref='1,000 pieces, six public corpora (Bach chorales, Essen, Monteverdi, Palestrina, Ryan\'s Mammoth Collection, Trecento), parsed with music21. zhiqian.ai/music-markov',
             notes='Majority class baseline 20%. No tuning, the number is what the script prints on a first run. The script is public on the site.')

# ---- where the graph becomes a path ----
g = adefs('gp')
def walk(cx, cy, n, r, rev, col):
    pts = [(cx + r * math.cos(2 * math.pi * k / n - math.pi / 2), cy + r * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    return pts
p1 = walk(210, 200, 10, 95, 0, AC2)
o1 = ''
seq = [0, 3, 1, 3, 0, 5, 2, 7, 3, 0, 4, 8, 1, 6, 9, 3, 0, 2, 5, 3]
for a, b in zip(seq, seq[1:]):
    o1 += L(*p1[a], *p1[b], AC2, 2.5, 'stroke-opacity=".45"')
o1 += ''.join(C(x, y, 11, '#fff', AC2, 2.5) for x, y in p1)
o1 += T(210, 70, 'first order', 18, 700, AC2, 'middle') + T(210, 330, '10 nodes, 89% revisits', 15, 700, INK, 'middle') + T(210, 352, 'a graph with loops', 14, 400, MUT, 'middle')
g += o1
o3 = ''
xs = [470 + k * 26 for k in range(14)]
ys = [200 + 60 * math.sin(k * 1.3) for k in range(14)]
o3 += P('M' + ' L'.join(f'{x},{y}' for x, y in zip(xs, ys)), ACC, 2.5)
o3 += ''.join(C(x, y, 7, '#fff', ACC, 2) for x, y in zip(xs, ys)) + T(800, 205, '...', 26, 700, ACC)
o3 += T(640, 70, 'third order', 18, 700, ACC, 'middle') + T(640, 330, '81 nodes, 6% revisits', 15, 700, INK, 'middle') + T(640, 352, 'a path: the piece memorized', 14, 400, MUT, 'middle')
g += F(1, o3)
lim = R(870, 50, 290, 135, SOFT, LINE, 1, 10) + T(886, 78, 'Limit of order one', 16, 700, AC2) + wrap(886, 102, 'An LLM judge picks the real excerpt over a first order one 96 to 100% of the time, 60% on real vs real.', 13, 400, INK, width=40, lh=18)
g += F(2, lim + T(886, 178, 'right vocabulary, wrong syntax', 13, 700, ACC))
mem = R(870, 200, 290, 160, MUL, MU, 1.5, 10) + T(886, 228, 'Second order helps', 16, 700, MU) + wrap(886, 252, 'Community detection recovers key regions: AMI 0.16 to 0.32, about zero at first order.', 13, 400, INK, width=40, lh=18)
g += F(3, mem + T(886, 330, 'open: which contexts earn memory?', 13, 700, MU) + T(886, 350, 'information vs idiom', 12.5, 400, MUT))
g += F(4, R(130, 395, 920, 58, ACL, ACC, 1.5, 10) + T(590, 431, 'Too little memory: a graph without syntax. Too much: a path. Variable order is the question.', 16.5, 700, INK, 'middle'))
PATH = sec('Where the graph becomes a path', SVG(g), ch='2', status='prog',
           ref='An 89 note Bach chorale at first and third order. AMI: adjusted mutual information between communities and key regions',
           notes='Variable order graphs: promote a context to longer memory where the longer context disagrees with the shorter one, that is information, versus where both are confident, that is idiom.')

# ---- three vector tools, updated citations ----
TOOLS = VZ.TOOLS.replace('2025, Zhao et al. ICLR 2026', 'Facchiano 2025, SMITIN 2025, Zhao ICLR 2026').replace('Singh et al. 2025, Paek et al. 2025', 'Singh et al. ICLR 2026, Paek et al. 2025')
TOOLS = TOOLS.replace('arXiv 2504.04479. Zhao et al., ICLR 2026. Singh, Cherep, Maes, arXiv 2505.18186.',
                      'Facchiano et al., arXiv 2504.04479, 2025. Koo et al., SMITIN, 2025. Zhao et al., ICLR 2026. Singh, Cherep, Maes, ICLR 2026.')
assert 'SMITIN, 2025' in TOOLS and 'Singh et al. ICLR 2026' in TOOLS

# ---- music to brain 1: the listener is a predictor ----
g = adefs('br1')
notes_ = [(80, 140), (140, 120), (200, 150), (260, 110), (320, 135), (380, 95)]
st = ''.join(L(60, 90 + k * 14, 420, 90 + k * 14, GRY, 1) for k in range(5))
st += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="7.5" fill="{INK}"/>' for x, y in notes_)
st += T(240, 60, 'a melody, note by note', 15, 700, AC2, 'middle')
g += st
mdl = R(500, 70, 280, 110, ACL, ACC, 2, 10) + T(640, 102, 'IDyOM', 19, 700, ACC, 'middle') + T(640, 128, 'variable order Markov model', 14, 600, INK, 'middle') + T(640, 150, 'of melodic expectation', 14, 400, INK, 'middle')
mdl += P('M425,125 L496,125', AC2, 2.5, extra='marker-end="url(#br1a)"')
g += F(1, mdl)
heights = [0.3, 0.5, 0.9, 0.4, 0.7, 1.0]
sur = T(970, 60, 'surprisal per note', 15, 700, ACC, 'middle') + ''.join(R(870 + i * 34, 170 - 90 * h, 24, 90 * h, ACC, 'none', 0, 3) for i, h in enumerate(heights)) + L(860, 172, 1080, 172, INK, 1.5)
sur += P('M784,125 L854,125', AC2, 2.5, extra='marker-end="url(#br1a)"')
g += F(2, sur)
eeg = R(500, 230, 580, 140, MUL, MU, 2, 10) + T(520, 262, 'EEG while people listen', 16, 700, MU)
eeg += P('M520,320 ' + ' '.join(f'L{520 + k * 9},{320 + 20 * math.sin(k * 0.9) * (1.6 if k % 9 == 4 else 0.6)}' for k in range(1, 60)), MU, 2)
eeg += T(520, 360, 'cortical responses track surprisal, more strongly in musicians', 14, 600, INK)
eeg += P('M970,178 C990,200 990,210 980,226', MU, 2.5, extra='marker-end="url(#br1t)"')
g += F(3, eeg)
g += ph(60, 230, 400, 140, 'Original figure: Di Liberto et al. 2020', 'eLife, to add when the site is reachable')
g += F(4, T(590, 455, 'A model of expectation that is itself a graph, measured in the brain.', 19, 700, INK, 'middle'))
BRAIN1 = sec('Music and the brain 1: the listener is a predictor', SVG(g), ch='2',
             ref='Pearce, The Construction and Evaluation of Statistical Models of Melodic Structure, 2005. Di Liberto et al., Cortical encoding of melodic expectations in human temporal cortex, eLife 2020',
             notes='IDyOM learns variable order Markov statistics of melody and outputs a surprisal for every note. Di Liberto and colleagues show EEG tracks that surprisal beyond acoustic envelope features. This is the bridge: listeners already behave like the graphs in the previous slides.')

# ---- music and the brain 2: decoding ----
g = adefs('br2')
g += img(40, 40, 1100, 176, 'figs/denk2023_fig1.png') + T(590, 236, 'Brain2Music: fMRI to a music embedding to MusicLM (Denk et al. 2023, Figure 1)', 13, 600, MUT, 'middle')
bel = R(40, 260, 520, 120, SOFT, LINE, 1, 10) + T(60, 290, 'Bellier et al. 2023, PLOS Biology', 16, 700, AC2) + wrap(60, 316, 'Intracranial recordings from 29 patients reconstruct a recognizable Pink Floyd song. Right superior temporal gyrus matters most for rhythm.', 13.5, 400, INK, width=66, lh=19)
g += F(1, bel)
ds = R(600, 260, 540, 120, MUL, MU, 1.5, 10) + T(620, 290, 'Open EEG music datasets', 16, 700, MU)
for i, (a, b) in enumerate([('OpenMIIR', 'perception and imagination'), ('NMED-T', 'tempo, 20 people, 10 songs'), ('NMED-H', 'Hindi pop'), ('MUSIN-G', '20 genres'), ('DEAP', 'emotion, music videos')]):
    x = 620 + (i % 2) * 260; y = 318 + (i // 2) * 22
    ds += T(x, y, a, 13.5, 700, INK) + T(x + 82, y, b, 13, 400, MUT)
g += F(2, ds)
g += F(3, T(590, 440, 'The brain carries enough of the music to rebuild it.', 19, 700, INK, 'middle'))
g += F(4, T(590, 468, 'So it can serve as a measuring instrument for a generator.', 16, 600, MU, 'middle'))
BRAIN2 = sec('Music and the brain 2: decoding music from the brain', SVG(g), ch='2',
             ref='Denk et al., Brain2Music, arXiv 2307.11078, 2023. Bellier et al., PLOS Biology 2023. Stober et al., OpenMIIR, 2015. Losorelli et al., NMED-T, ISMIR 2017. Koelstra et al., DEAP, 2012',
             notes='Figure from the Brain2Music project page. Bellier original figure still to add.')

# ---- music and the brain 3: do model layers predict the brain? ----
g = adefs('br3')
g += img(30, 30, 640, 178, 'figs/denk2023_encoding.png') + T(350, 226, 'Music embeddings predict auditory cortex (Denk et al. 2023)', 13, 600, MUT, 'middle')
lay = R(30, 248, 640, 150, SOFT, LINE, 1, 10) + T(50, 276, 'The layer question', 16, 700, AC2)
for k in range(6):
    lay += R(60 + k * 46, 362 - 10, 38, 22, '#fff', GRY, 1.5, 4)
pk = [0.25, 0.45, 0.75, 0.85, 0.6, 0.4]
lay += P('M' + ' L'.join(f'{79 + k * 46},{340 - 50 * v}' for k, v in enumerate(pk)), ACC, 3)
lay += T(60, 390, 'layers', 12, 600, MUT) + T(360, 300, 'language and speech models:', 13.5, 600, INK) + T(360, 320, 'the middle layers predict best', 13.5, 700, ACC)
g += F(1, lay)
wk = [('Language', 'Schrimpf 2021, Caucheteux and King 2022, Goldstein 2022, Tuckute 2023'), ('Audio', 'Kell 2018, Pepino 2025: 36 audio encoders vs fMRI'),
      ('Music generator', 'Noguchi 2026: MusicGen surprisal as an EEG teacher, final outputs only')]
for i, (a, b) in enumerate(wk):
    y = 40 + i * 98
    g += F(2, R(700, y, 450, 84, '#fff', LINE, 1.5, 8) + T(716, y + 28, a, 16, 700, AC2) + wrap(716, y + 52, b, 13, 400, INK, width=58, lh=18))
g += F(3, R(700, 336, 450, 62, ACL, ACC, 1.5, 8) + T(716, 362, 'Missing: a music generator, layer by layer,', 14.5, 700, ACC) + T(716, 384, 'under intervention', 14.5, 700, ACC))
g += F(4, T(590, 455, 'Encoding models give a yardstick. Nobody has held it to the inside of a music generator.', 17, 700, INK, 'middle'))
BRAIN3 = sec('Music and the brain 3: do model layers predict the brain?', SVG(g), ch='2',
             ref='Schrimpf et al., PNAS 2021. Caucheteux and King, Comm. Biology 2022. Goldstein et al., Nat. Neurosci. 2022. Kell et al., Neuron 2018. Tuckute et al., Nat. Hum. Behav. 2024. Pepino et al., 2025. Noguchi et al., arXiv 2603.03190, 2026',
             notes='Closest prior work: Noguchi et al. use MusicGen large output logits for surprisal and entropy as teacher targets to pretrain an EEG encoder on NMED-T, then identify the song from 3 seconds of EEG. No internal layers, no steering, no style. Brain2Music uses MusicLM components without layerwise analysis or interventions. The layer curve is schematic.')

# ---- music and the brain 4: our plan ----
g = adefs('br4')
flow = [('steer MusicGen', 'add or remove a style', ACC), ('audio', 'steered and unsteered', AC2), ('listener EEG', 'NMED-T style protocol', MU), ('encoding model', 'per layer, per graph state', AC2)]
for i, (a, b, col) in enumerate(flow):
    x = 40 + i * 285
    blk = R(x, 50, 250, 80, '#fff', col, 2, 10) + T(x + 125, 84, a, 17, 700, col, 'middle') + T(x + 125, 108, b, 13.5, 400, MUT, 'middle')
    if i < 3:
        blk += P(f'M{x+252},90 L{x+282},90', AC2, 2.5, extra='marker-end="url(#br4a)"')
    g += F(1, blk) if i else blk
qs = [('Does a steered style land in the brain?', 'Steered audio should evoke the response that real music of that style evokes.'),
      ('Do graph states beat vectors?', 'Graph states should predict EEG better than the steering vector or the data graph.'),
      ('Do trained layers beat random ones?', 'If a randomly initialized MusicGen aligns as well, the alignment is not about music.')]
for i, (a, b) in enumerate(qs):
    y = 170 + i * 86
    g += F(i + 2 if i < 2 else 3, C(70, y + 22, 18, MU) + T(70, y + 29, str(i + 1), 16, 700, '#fff', 'middle') + T(105, y + 20, a, 17, 700, INK) + T(105, y + 44, b, 14, 400, MUT))
g += F(4, T(590, 465, 'A style has no answer key. The listener is a judge that did not write the exam.', 18, 700, ACC, 'middle'))
BRAIN4 = secx('Music and the brain 4: the brain as judge', SVG(g), ch='2', status='plan',
              notes='We do not build a model of the brain. EEG is the measurement that is independent of the model and of us. The random initialization control is also the third falsifier on the drop the graph slide.')

# ---- pilot ----
g = adefs('pl')
g += ph(40, 40, 530, 300, 'Pilot figure: probe accuracy by layer', 'tempo, key, instrument decodable from MusicGen')
g += F(1, ph(610, 40, 530, 300, 'Pilot figure: tempo dose response', 'steering strength vs measured BPM'))
g += F(2, R(40, 365, 530, 60, MUL, MU, 1.5, 8) + T(305, 401, 'Readable: attributes are decodable at middle layers', 15.5, 700, MU, 'middle'))
g += F(3, R(610, 365, 530, 60, ACL, ACC, 1.5, 8) + T(875, 401, 'Pushable: tempo moves with steering strength', 15.5, 700, ACC, 'middle'))
g += F(4, T(590, 465, 'A vector can read and push. Where the push lands is the graph question.', 18, 700, INK, 'middle'))
PILOT = sec('Pilot: readable and pushable', SVG(g), ch='2', status='prog',
            notes='Placeholders: insert the pilot probe and tempo dose response figures here.')

# ---- next: the graph inside MusicGen, judged by a listener ----
g = adefs('nx')
steps = [('record', 'mid layer, every step'), ('discretize', '100 to 500 states'), ('connect', 'transitions, lag sweep'), ('test', 'communities, reachability')]
for i, (a, b) in enumerate(steps):
    x = 40 + i * 180
    g += R(x, 40, 160, 70, SOFT, AC2, 1.5, 10) + T(x + 80, 70, a, 16, 700, AC2, 'middle') + T(x + 80, 92, b, 12.5, 400, INK, 'middle')
    if i < 3:
        g += P(f'M{x+162},75 L{x+178},75', AC2, 2.5, extra='marker-end="url(#nxa)"')
g += T(780, 60, 'controls', 15, 700, MUT) + tag(780, 72, 'same graph on output tokens', 'plan') + tag(780, 100, 'shuffled style labels', 'plan') + tag(980, 100, 'loudness, position', 'plan')
mx, my = 150, 150
g += T(mx + 260, my, 'steered trajectories reach target states?', 14.5, 700, INK, 'middle')
g += T(mx - 22, my + 140, 'styles form communities?', 14.5, 700, INK, 'middle', f'transform="rotate(-90 {mx-22} {my+140})"')
g += T(mx + 145, my + 22, 'yes', 13.5, 700, MUT, 'middle') + T(mx + 405, my + 22, 'no', 13.5, 700, MUT, 'middle')
g += T(mx + 10, my + 85, 'yes', 13.5, 700, MUT, 'end') + T(mx + 10, my + 205, 'no', 13.5, 700, MUT, 'end')
cells = [('islands, steering can cross', 'graph explains success', GRN, '#eaf3ea'), ('islands, steering cannot enter', 'one way is a reachability fact', ACC, ACL),
         ('no islands, steering works', 'style is a direction after all', AC2, SOFT), ('no islands, steering fails', 'style lives in finer geometry', MU, MUL)]
for i, (a, b, col, fill) in enumerate(cells):
    x = mx + 20 + (i % 2) * 260; y = my + 35 + (i // 2) * 120
    g += F(1 if i < 2 else 2, R(x, y, 250, 110, fill, col, 2, 10) + T(x + 125, y + 46, a, 14, 700, INK, 'middle') + T(x + 125, y + 72, b, 13, 400, col, 'middle'))
bc = T(960, my + 22, 'listener check', 14.5, 700, MU, 'middle')
for i, s in enumerate([('EEG separates the', 'same communities?'), ('EEG separates styles', 'the graph misses?')]):
    y = my + 35 + i * 120
    bc += R(840, y, 240, 110, '#fff', MU, 2, 10, 'stroke-dasharray="6 4"') + T(960, y + 46, s[0], 14, 700, INK, 'middle') + T(960, y + 70, s[1], 14, 700, INK, 'middle')
    bc += P(f'M{mx+544},{y+55} L836,{y+55}', MU, 2, extra='marker-end="url(#nxt)" stroke-dasharray="5 4"')
g += F(3, bc)
g += F(4, T(590, 470, 'Every cell is a result. The listener decides which one we are in.', 18, 700, INK, 'middle'))
NEXT = sec('Next: the graph inside MusicGen, judged by a listener', SVG(g), ch='2', status='prog')

# ======================= BEYOND =======================
g = adefs('f5')
fal = ['delta graph features add nothing over change size on fine tuning or merging',
       'MusicGen states show no community structure above shuffled labels at any lag',
       'steered trajectories reach target states as often as unsteered ones',
       'layer by layer EEG alignment is no better than a randomly initialized MusicGen']
g += T(60, 50, 'Four numbers that would end this program', 19, 700, ACC)
for i, s in enumerate(fal):
    y = 96 + i * 56
    g += F(1 if i < 2 else 2, C(80, y - 6, 18, ACC) + T(80, y + 1, str(i + 1), 16, 700, '#fff', 'middle') + T(112, y, s, 17, 600, INK))
g += F(3, L(60, 320, 1120, 320, LINE, 2) + T(60, 355, 'Not claimed today', 19, 700, AC2))
nc = ['a graph is the one true description', 'the delta graph traces causal paths (it detects)', 'a circuit level account of a music model', 'the data graph shown is inside the model']
g += F(4, ''.join(T(60 + (i % 2) * 540, 395 + (i // 2) * 44, '✗  ' + s, 16, 600, MUT) for i, s in enumerate(nc)))
DROP = sec('What would make me drop the graph', SVG(g), ch='3')

# ======================= CLOSE =======================
g = adefs('c1')
lanes = [(60, 'Depth, language', ACC, ACL, 'a delta graph catches edits that pass', 'their own test but break other behavior', ('published', 'done')),
         (430, 'Time, music', MU, MUL, 'styles look like islands, steering is', 'one way, the in model graph is next', ('in progress', 'part')),
         (800, 'The judge', AC2, SOFT, 'a listener\'s brain checks the graph', 'where no answer key exists', ('planned', 'plan'))]
for i, (x, a, col, fill, b1, b2, (tg, k)) in enumerate(lanes):
    blk = R(x, 60, 320, 230, fill, col, 2, 12) + T(x + 20, 98, a, 20, 700, col) + T(x + 20, 140, b1, 14.5, 400, INK) + T(x + 20, 164, b2, 14.5, 400, INK) + tag(x + 20, 240, tg, k)
    g += F(i, blk) if i else blk
g += F(3, R(160, 330, 860, 80, '#fff', INK, 2, 10) + T(590, 364, 'Propagation and reachability:', 18, 700, INK, 'middle') + T(590, 390, 'classic graph questions, asked of a new object', 15, 400, MUT, 'middle'))
TWO = sec('Two hidden graphs, one judge', SVG(g), ch='4', cls='divider')

g = adefs('c2')
g += C(590, 240, 80, ACL, ACC, 3) + T(590, 234, 'hidden graphs', 17, 700, ACC, 'middle') + T(590, 256, 'in generative models', 14, 400, INK, 'middle')
areas = [('Knowledge graphs', 'edit a model like a database?'), ('NLP', 'which behaviors should an edit test?'), ('AutoML', 'score pruning and merging cheaply?'), ('Theory', 'discretize and keep reachability?'),
         ('Audiology, NTID', 'steer music for hearing loss?'), ('Neuroscience', 'EEG protocols for a style judge?'), ('Systems and data', 'store activation graphs at scale?'), ('Security', 'do malicious edits leave a fingerprint?')]
for i, (a, q) in enumerate(areas):
    left = i < 4
    x = 40 if left else 820; y = 40 + (i % 4) * 104
    blk = R(x, y, 320, 84, SOFT, LINE, 1, 8) + T(x + 18, y + 32, a, 16.5, 700, MU if i in (4, 5) else AC2) + T(x + 18, y + 58, q, 14, 400, INK)
    ax = x + 320 if left else x
    blk += L(ax, y + 42, 590 + (-80 if left else 80) * 0.9, 240 + (y + 42 - 240) * 0.3, AC2, 1.5)
    g += F(1 if left else (2 if i in (4, 5) else 3), blk)
g += F(4, T(590, 465, 'Teal: new partners the music and brain work needs.', 16, 600, MU, 'middle'))
HELP = sec('Where I would love your help', SVG(g), ch='4')

g = adefs('c4')
pts3 = [('We steer and edit models with vectors.', 'Vectors say what we pushed, not where it went.', AC2),
        ('Language: a graph from activations', 'already catches failures that tests miss.', ACC),
        ('Music: a first order graph carries a style.', 'Whether a graph inside the generator explains steering is next.', MU)]
for i, (a, b, col) in enumerate(pts3):
    y = 40 + i * 100
    blk = C(90, y + 30, 28, col) + T(90, y + 39, str(i + 1), 24, 700, '#fff', 'middle') + T(145, y + 24, a, 21, 700, INK) + T(145, y + 52, b, 18, 400, MUT)
    g += F(i, blk) if i else blk
g += F(3, R(70, 340, 1040, 86, ACL, ACC, 1.5, 10) + T(590, 374, 'A graph inside a generator is a hypothesis about the model.', 20, 700, INK, 'middle') + T(590, 406, 'A listener\'s brain is the only judge that did not write the exam.', 20, 700, ACC, 'middle'))
g += F(4, T(590, 466, 'Thank you. Questions, and collaborators, welcome.', 19, 600, AC2, 'middle'))
TAKE = sec('What to take home', SVG(g), ch='4')

# ======================= PREVIEWS =======================
# Right after the cover: the best results first, one slide per domain, each with a graph.

def chipx(x, y, s, col):
    w = len(s) * 7.4 + 22
    return R(x, y, w, 24, '#fff', col, 1.5, 12) + T(x + w / 2, y + 16.5, s, 12.5, 700, col, 'middle')

g = adefs('pm')
g += f'<foreignObject x="10" y="20" width="640" height="340"><div xmlns="http://www.w3.org/1999/xhtml" style="width:640px;height:340px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1.5px #d3d7da,0 10px 30px rgba(17,17,17,.10)"><iframe class="fe-frame" data-src="figs/fe-chain.html?autoplay=1" title="Für Elise Markov chain" style="width:640px;height:340px;border:0;background:#fff"></iframe></div></foreignObject>'
g += T(330, 388, 'Für Elise as a graph: it learns the melody, then composes', 15, 700, MU, 'middle')
res = [('70.9%', '144 numbers per piece name its tradition', 'six corpora, 1,000 pieces, baseline 20%', ACC, 'in progress', 'part'),
       ('one way', 'steering MusicGen removes a style, cannot add one', 'a reachability question on a hidden graph', ACC, 'under review', 'part'),
       ('89% to 6%', 'revisits fall as memory grows: a graph becomes a path', 'the useful graph lives in between', ACC, 'in progress', 'part')]
for i, (big, a, b, col, st, k) in enumerate(res):
    y = 20 + i * 116
    blk = R(690, y, 470, 104, SOFT, LINE, 1, 10) + T(710, y + 46, big, 32, 700, col) + T(710, y + 72, a, 14.5, 700, INK) + T(710, y + 92, b, 13, 400, MUT)
    blk += chipx(1150 - (len(st) * 7.4 + 22) - 10, y + 12, st, ACC)
    g += F(i + 1, blk)
g += F(4, T(590, 455, 'Our work: a graph explains a style, and may explain why steering is one way.', 18, 700, INK, 'middle'))
PREV_MUSIC = sec('Music: the generator can be a graph, and the graph carries a style', SVG(g), ch='0',
                 ref='Our work. Corpus result: zhiqian.ai/music-markov. Steering: co-authored work under review, MusicGen small and medium',
                 notes='Preview one of two. Let the animation run. Then the three numbers, one sentence each. Do not explain methods here, every number comes back later in Part 2.')

g = adefs('pl')
cx0 = [70 + k * 92 for k in range(6)]
lay = [(x, 170) for x in cx0]
up = [(x + 46, 90) for x in cx0[:5]]
dn = [(x + 46, 250) for x in cx0[:5]]
nodes = lay + up + dn
edges = [(i, i + 1) for i in range(5)] + [(i, 6 + i) for i in range(5)] + [(6 + i, i + 1) for i in range(5)] + [(i, 11 + i) for i in range(5)] + [(11 + i, i + 1) for i in range(5)]
hot = {(1, 7), (7, 2), (1, 12), (12, 2), (1, 2)}
g += T(300, 34, 'blocks of the model, before and after one edit', 14, 700, AC2, 'middle')
for a, b in edges:
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    g += L(x1, y1, x2, y2, '#c9d0d5', 2)
rew = ''
for a, b in edges:
    if (a, b) in hot:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        rew += L(x1, y1, x2, y2, '#c0392b', 5, 'stroke-linecap="round"')
rew += P(f'M{nodes[7][0]},{nodes[7][1]} C{nodes[7][0]+120},40 {nodes[9][0]},40 {nodes[9][0]},{nodes[9][1]}', '#c0392b', 3, extra='stroke-dasharray="7 5"')
g += ''.join(C(x, y, 11, '#fff', AC2, 2.5) for x, y in nodes)
g += F(1, rew + ''.join(C(*nodes[k], 11, '#fde3dd', '#c0392b', 3) for k in (1, 2, 7, 12)) + T(300, 310, 'red: connections the edit rewired', 14, 700, '#c0392b', 'middle'))
bars = [('check 20 at random', 11, '#c9d0d5'), ('pick by editor and model', 14, GRY), ('pick by our delta graph', 17, ACC)]
blk = T(640, 34, '100 edits pass every test, 56 are secretly broken', 15, 700, INK) + T(640, 56, 'broken edits found with 20 checks', 13, 400, MUT)
for i, (a, v, col) in enumerate(bars):
    y = 82 + i * 54
    blk += T(640, y + 18, a, 14, 700 if i == 2 else 600, ACC if i == 2 else INK) + R(840, y, v * 14, 28, col, 'none', 0, 3) + T(848 + v * 14, y + 20, str(v), 16, 700, ACC if i == 2 else INK)
g += F(2, blk + chipx(640, 248, 'published, SDM 2026', GRN))
oth = R(640, 300, 520, 110, SOFT, LINE, 1, 10) + T(658, 328, 'Others see graphs too', 15.5, 700, AC2)
oth += T(658, 354, 'Attribution graphs trace how one prompt flows', 14, 400, INK) + T(658, 374, 'through a model, feature by feature.', 14, 400, INK) + T(658, 398, 'Ameisen et al., Circuit Tracing, 2025', 12.5, 600, MUT)
g += F(3, oth)
g += F(4, T(590, 466, 'A graph read from inside the model catches edits that pass their own test.', 18, 700, INK, 'middle'))
PREV_LLM = sec('Language models: a graph inside catches what tests miss', SVG(g), ch='0',
               ref='Benbrahim et al., SDM 2026, Figure 1(b) and Tables 5.1 to 5.5. Ameisen et al., Circuit Tracing: Revealing Computational Graphs in Language Models, Transformer Circuits 2025',
               notes='Preview two of two. The drawing is schematic. The paper figure comes later on the method slide. Then the result. Then one line on attribution graphs so the audience knows we are not alone, and that ours looks at an edit rather than a single prompt.')

# ======================= AUDIT REVISION (Nov 1 2026) =======================
# Opening: problem before answers. Throughline: Vectors say what we changed. Only a graph can say where it went.

def retitle(sec_html, new):
    return re.sub(r'<h2>.*?</h2>', f'<h2>{new}</h2>', sec_html, count=1, flags=re.S)

def notes(sec_html, n):
    if '<aside class="notes">' in sec_html:
        return re.sub(r'<aside class="notes">.*?</aside>', f'<aside class="notes">{n}</aside>', sec_html, count=1, flags=re.S)
    return sec_html.replace('</section>', f'  <aside class="notes">{n}</aside>\n</section>')

THROUGH_A, THROUGH_B = 'Vectors say what we changed.', 'Only a graph can say where it went.'

# ---- 3: the exam said pass, and a side effect hid ----
g = adefs('rc')
cards = [('Editing', 'A corrected fact scores 96.8% when the test feeds the start of the answer, 38.5% when the model writes freely.', 'Yang et al. 2025'),
         ('Unlearning', 'A "forgotten" Harry Potter comes back word for word after light fine tuning on harmless text.', 'Hu et al. 2025'),
         ('Merging', 'A safe chemistry expert averaged with an unsafe math expert passes every capability test and inherits the unsafe behavior.', 'Hammoud et al. 2024')]
for i, (a, b, c) in enumerate(cards):
    x = 40 + i * 380
    blk = R(x, 40, 350, 270, '#fff', LINE, 1.5, 12) + R(x, 40, 350, 8, ACC, 'none', 0, 4) + T(x + 24, 92, a, 24, 700, INK)
    blk += R(x + 24, 110, 118, 28, '#eaf3ea', GRN, 1.5, 14) + T(x + 83, 129, 'exam: pass', 14, 700, GRN, 'middle')
    blk += wrap(x + 24, 172, b, 16, 400, INK, width=36, lh=23) + T(x + 24, 292, c, 13, 600, MUT)
    g += F(i, blk) if i else blk
g += F(3, R(150, 345, 880, 80, ACL, ACC, 1.5, 10) + T(590, 377, 'Three different operations, one shape:', 18, 700, INK, 'middle') + T(590, 405, 'the test passed, a side effect hid, and only a costlier test found it.', 17, 400, INK, 'middle'))
g += F(4, T(590, 466, 'So where did the change actually go?', 21, 700, ACC, 'middle'))
RECEIPTS = sec('The exam said pass, and a side effect hid', SVG(g), ch='0',
               ref='Yang et al. 2025. Hu et al., ICLR 2025. Hammoud et al. 2024',
               notes='Everyone in the room has used a model that went through this. Three surgeries, three different labs, the same pattern. End on the question: where did the change go? That question is the talk.')

# ---- 5: the demo, as the world we want back ----
g = adefs('dm')
g += f'<foreignObject x="20" y="10" width="760" height="420"><div xmlns="http://www.w3.org/1999/xhtml" style="width:760px;height:420px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1.5px #d3d7da,0 10px 30px rgba(17,17,17,.10)"><iframe class="fe-frame" data-src="figs/fe-chain.html?autoplay=1" title="Für Elise Markov chain" style="width:760px;height:420px;border:0;background:#fff"></iframe></div></foreignObject>'
side = [('1957 onward', 'Markov chains composed music: notes are nodes, moves are arrows'), ('Every choice is visible', 'the spinner at each note shows exactly where the tune can go'), ('So control is exact', 'want a style? ask which notes are reachable from here')]
for i, (a, b) in enumerate(side):
    y = 40 + i * 120
    g += F(i + 1, R(810, y, 350, 100, MUL if i < 2 else ACL, MU if i < 2 else ACC, 1.5, 10) + T(830, y + 32, a, 17, 700, MU if i < 2 else ACC) + wrap(830, y + 58, b, 14, 400, INK, width=42, lh=19))
g += F(4, T(590, 466, 'Today\'s generators are far better, and the graph is gone.', 19, 700, INK, 'middle'))
DEMO = sec('When the generator is a graph, every choice is visible and can be steered', SVG(g), ch='0',
           ref='Opening of Beethoven, Für Elise. Animation from zhiqian.ai, click it for sound',
           notes='The one demo of the talk. Let the ball learn the opening, then let it compose. Click for sound. This is the "what could be" side: a generator whose graph we can see. The last line turns it into the question of the talk.')

# ---- 6: throughline and forecast ----
g = adefs('fc')
g += T(590, 70, THROUGH_A, 34, 700, INK, 'middle') + T(590, 118, THROUGH_B, 34, 700, ACC, 'middle')
finds = [('In language models, a graph of what rewired after an edit catches failures every benchmark passed.', 'published', 'done', ACC),
         ('In music, the simplest graph already carries a style, and steering can leave a style but not enter one.', 'in progress, under review', 'part', MU),
         ('A style has no answer key, so a listener\'s brain will judge the graph inside a music generator.', 'planned', 'plan', AC2)]
for i, (a, st, k, col) in enumerate(finds):
    y = 170 + i * 92
    blk = C(70, y + 28, 22, col) + T(70, y + 36, str(i + 1), 20, 700, '#fff', 'middle') + wrap(110, y + 22, a, 18, 600, INK, width=78, lh=25) + tag(1180 - 40 - (len(st) * 7.2 + 20), y + 8, st, k)
    g += F(i + 1, blk)
g += F(4, T(590, 466, 'Forty minutes, three claims. You can check each one as we go.', 18, 700, MUT, 'middle'))
FORECAST = sec('Today\'s generators hide the graph. Can we read it back out?', SVG(g), ch='0',
               notes='The forecast. Say the throughline slowly. Then the three claims, with their honest status. By minute 20 they will be able to pick 17 bad edits out of 20.')

# ---- 7: language result, random first ----
g = adefs('lr')
g += T(30, 40, '100 edits, all with perfect benchmark scores.', 19, 700, INK) + T(30, 70, '56 are secretly broken. You may check only 20.', 19, 700, ACC)
bars = [('check 20 at random', 11, '#c9d0d5'), ('pick by editor and model', 14, GRY), ('pick by what rewired inside', 17, ACC)]
for i, (a, v, col) in enumerate(bars):
    y = 120 + i * 82
    blk = T(30, y + 30, a, 17, 700 if i == 2 else 600, ACC if i == 2 else INK)
    for j in range(20):
        bx = 330 + j * 34
        blk += R(bx, y + 4, 28, 40, (ACC if i == 2 else '#c0503a') if j < v else '#eef0f2', 'none', 0, 4)
        if j < v:
            blk += P(f'M{bx+8},{y+16} L{bx+20},{y+32} M{bx+20},{y+16} L{bx+8},{y+32}', '#fff', 2.5, extra='stroke-linecap="round"')
    blk += T(1040, y + 36, str(v), 34, 700, ACC if i == 2 else INK)
    g += F(i + 1, blk) if i else blk
g += T(1080, 104, 'broken found', 13, 600, MUT, 'middle')
g += F(3, R(30, 380, 1120, 56, ACL, ACC, 1.5, 10) + T(590, 414, 'Same budget, half again as many broken edits caught, read only from how the inside rewired.', 17, 700, INK, 'middle'))
g += F(4, tag(30, 450, 'published, SDM 2026', 'done') + T(240, 466, 'How the graph is built: Part 1', 14, 600, MUT))
LANGRES = sec('Reading the rewiring finds 17 of 20 bad edits', SVG(g), ch='0', status='pub',
              ref='Benbrahim et al., SDM 2026, Tables 5.1 to 5.5. Counts rounded from the paper\'s rates (56%, 70%, 86%)',
              notes='Pause after the random row and ask: how would you pick the 20? Then the editor row, then ours. Do not explain the method yet, Part 1 does.')

# ---- 8: music result ----
g = adefs('mr')
def island2(cx):
    return P(f'M{cx-150},300 C{cx-80},200 {cx+20},330 {cx+150},230', MU, 14, extra='stroke-linecap="round" stroke-opacity=".35"') + P(f'M{cx-150},300 C{cx-80},200 {cx+20},330 {cx+150},230', MU, 2.5)
g += R(40, 40, 520, 360, '#fff', LINE, 1.5, 10) + R(620, 40, 520, 360, '#fff', LINE, 1.5, 10)
g += T(300, 80, 'Remove a style', 20, 700, INK, 'middle') + T(880, 80, 'Add a style', 20, 700, INK, 'middle')
g += island2(300) + island2(880) + T(300, 345, 'a style: a thin set of musical paths', 14, 600, MU, 'middle') + T(880, 345, 'a style: a thin set of musical paths', 14, 600, MU, 'middle')
g += F(1, C(300, 262, 10, INK) + P('M300,256 L300,140', ACC, 3.5, extra='marker-end="url(#mro)"') + T(300, 385, 'leaves easily, still music', 17, 700, MU, 'middle'))
g += F(2, C(800, 135, 10, INK) + P('M806,142 L930,312', ACC, 3.5, extra='marker-end="url(#mro)" stroke-dasharray="9 6"') + T(880, 385, 'the push misses the thin set', 17, 700, ACC, 'middle'))
g += F(3, R(380, 412, 420, 44, MUL, MU, 1.5, 22) + T(590, 440, 'and 144 note transitions name a tradition 71% of the time', 14.5, 700, MU, 'middle'))
g += F(4, T(590, 476, 'Many exits, almost no entrances: that sounds like a fact about a graph.', 17, 700, INK, 'middle'))
MUSRES = sec('Steering leaves a style easily but cannot enter one', SVG(g), ch='0', status='rev',
             ref='Co-authored work under review, MusicGen small and medium. Corpus result: zhiqian.ai/music-markov, in progress',
             notes='Same vector tool, now in MusicGen. This picture comes back in Part 2 as the payoff. Keep it to two sentences here.')

# ---- map slides ----
def mapx(title, depth, time, line, ch, take, n=''):
    g = adefs('mp' + ch)
    g += axis_icon(110, 70, 2.3, depth, time)
    g += T(600, 160, THROUGH_A, 30, 700, INK) + T(600, 205, THROUGH_B, 30, 700, ACC)
    g += F(1, T(600, 270, line, 21, 600, MU if time != 'plan' and depth == 'plan' else (ACC if depth != 'plan' else AC2)))
    g += F(2, T(600, 330, take, 17, 400, MUT))
    return sec(title, SVG(g), ch=ch, cls='divider', notes=n)

MAP_L = mapx('Part 1. Where does an edit go, across depth?', 'part', 'plan', 'Part 1: across the blocks of a language model', '1',
             'One moment in time, many blocks deep.', 'Landmark. The map lights the depth axis.')
MAP_B = mapx('Part 3. Where it went, for any sequence generator', 'done', 'part', 'Part 3: any model that emits a sequence', '3',
             'Both axes at once.', 'Landmark before the beyond section.')
BREATH = sec('Across depth, where an edit went is readable', SVG(T(590, 200, 'Across depth,', 40, 700, INK, 'middle') + T(590, 260, 'where an edit went is readable.', 40, 700, ACC, 'middle') + F(1, T(590, 340, 'Now the harder axis: time, where a style has no answer key.', 20, 400, MUT, 'middle')), 420), ch='1',
             notes='Breathing slide after the dense Part 1 results.')

# ---- part 2 opener: facts versus styles, as the bridge ----
P2 = retitle(FACTS, 'Part 2. A style has no answer key, it needs a judge').replace('data-ch="0"', 'data-ch="2"', 1).replace('<section data-ch="2">', '<section class="divider" data-ch="2">', 1)

# ---- close ----
g = adefs('tk')
for i, (a, st, k, col) in enumerate(finds):
    y = 40 + i * 100
    blk = C(70, y + 30, 26, col) + T(70, y + 39, str(i + 1), 22, 700, '#fff', 'middle') + wrap(115, y + 24, a, 20, 600, INK, width=72, lh=27) + tag(115, y + 62, st, k)
    g += F(i, blk) if i else blk
g += F(3, R(70, 345, 1040, 90, ACL, ACC, 1.5, 10) + T(590, 381, 'A graph inside a generator is a hypothesis about the model.', 20, 700, INK, 'middle') + T(590, 414, 'A listener\'s brain is the only judge that did not write the exam.', 20, 700, ACC, 'middle'))
TAKE2 = sec('Vectors say what we changed, and a graph can say where it went', SVG(g), ch='4',
            notes='The three claims again, now proven, in progress and planned. Then the closing line. Move straight to the ask.')

hero = open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'hero.svg')).read().replace('fill="#1c2430"', 'fill="#ffffff"').replace('stroke-opacity=".13"', 'stroke-opacity=".28"')
hero = hero.replace('class="herofig"', 'x="390" y="70" width="400" height="315"', 1)
g = adefs('ak') + hero
asks = [('Audiology, NTID', 'listeners with hearing loss as judges'), ('Neuroscience, EEG', 'a fair EEG protocol for a style judge'),
        ('Anyone who edits or merges models', 'your operations are our test cases')]
for i, (a, b) in enumerate(asks):
    x = 40 + i * 380
    g += F(i + 1, R(x, 380, 350, 80, SOFT, MU if i < 2 else ACC, 1.5, 10) + T(x + 18, 410, a, 16.5, 700, MU if i < 2 else ACC) + T(x + 18, 438, b, 13.5, 400, INK))
g += T(590, 40, 'Is there a graph inside generative models?', 22, 700, INK, 'middle') + T(590, 66, 'In language, yes, and it predicts failures. In music, we are testing it. Help us find out.', 15.5, 600, ACC, 'middle')
ASK = sec('Where I would love your help', SVG(g, 478), ch='4',
          notes='End here and stay on this slide for questions. The cover graph is back, now with an answer. Three concrete asks. Do not say thank you as the last line.')

# ======================= ROUND 3 (Nov 1 2026, late) =======================
# Two claims only (language, music with the brain), matching the subtitle.
CLAIMS = [('Language: a graph of how a model rewires after an edit catches failures that every benchmark passed.', 'published', 'done', ACC),
          ('Music: a tiny graph already carries a style, and the listener\'s brain can judge whether a generator has one inside.', 'in progress', 'part', MU)]

# ---- every surgery is stored as a vector (concrete) ----
g = adefs('vc')
cols3 = [('Steer', 'h  ←  h + α r', 'add a direction to the activations', 'refusal direction, Arditi et al. 2024'),
         ('Edit', 'W  ←  W + u vᵀ', 'add a rank one matrix to one layer', 'ROME, Meng et al. 2022'),
         ('Fine tune', 'θ  ←  θ + τ', 'add a task vector to all weights', 'task arithmetic, Ilharco et al. 2023')]
for k, (a, eq, d1, cite) in enumerate(cols3):
    x = 40 + k * 380
    blk = R(x, 30, 350, 230, '#fff', LINE, 1.5, 12) + T(x + 175, 72, a, 24, 700, AC2, 'middle')
    blk += R(x + 30, 95, 290, 64, ACL, ACC, 1.5, 10) + T(x + 175, 137, eq, 28, 700, ACC, 'middle', extra='font-family="Fira Mono,monospace"')
    blk += T(x + 175, 196, d1, 15, 600, INK, 'middle') + T(x + 175, 232, cite, 13, 400, MUT, 'middle')
    g += F(k, blk) if k else blk
g += F(3, R(40, 290, 1110, 110, SOFT, LINE, 1, 12) + T(595, 330, 'Each one tells you exactly what was added.', 22, 700, INK, 'middle') + T(595, 372, 'None tells you which other facts, behaviors or styles moved with it.', 22, 700, ACC, 'middle'))
g += F(4, T(595, 455, 'Beyond vectors: read how the parts connect, and follow the change.', 19, 700, INK, 'middle'))
VECTOR = sec('Every surgery is stored as a vector', SVG(g), ch='0',
             ref='Arditi et al., NeurIPS 2024. Meng et al., NeurIPS 2022. Ilharco et al., ICLR 2023',
             notes='Three surgeries, three one line formulas a CS audience can read. The point is not the math, it is that each operation is a single added object, and that object carries no information about its side effects.')

# ---- demo: a tiny graph is enough to represent a piece ----
g = adefs('dm2')
g += f'<foreignObject x="20" y="10" width="740" height="410"><div xmlns="http://www.w3.org/1999/xhtml" style="width:740px;height:410px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1.5px #d3d7da,0 10px 30px rgba(17,17,17,.10)"><iframe class="fe-frame" data-src="figs/fe-chain.html?autoplay=1" title="Für Elise Markov chain" style="width:740px;height:410px;border:0;background:#fff"></iframe></div></foreignObject>'
g += F(1, R(790, 20, 370, 120, MUL, MU, 1.5, 12) + T(810, 58, 'A whole piece in 144 numbers', 19, 700, MU) + T(810, 88, 'which note follows which,', 15, 400, INK) + T(810, 110, 'a 12 by 12 table, no music theory', 15, 400, INK))
g += F(2, R(790, 160, 370, 160, ACL, ACC, 1.5, 12) + T(975, 230, '70.9%', 56, 700, ACC, 'middle') + T(975, 262, 'of unseen pieces placed in', 15, 600, INK, 'middle') + T(975, 284, 'the right tradition (chance 20%)', 15, 600, INK, 'middle'))
g += F(3, R(790, 340, 370, 80, '#fff', LINE, 1.5, 12) + T(810, 372, '1,000 pieces, six traditions', 15.5, 700, INK) + T(810, 398, 'Bach to Palestrina to fiddle tunes', 14, 400, MUT))
g += F(4, T(590, 466, 'A tiny graph already captures a style.', 20, 700, INK, 'middle'))
DEMO2 = sec('A tiny graph is enough to represent a piece of music', SVG(g), ch='0', status='prog',
            ref='Opening of Beethoven, Für Elise, animation from zhiqian.ai, click for sound. Five fold cross validation, zhiqian.ai/music-markov',
            notes='Let the ball learn the opening, then compose. Then the point: this little graph is not a toy. The same 144 numbers per piece, fed to a plain classifier, name the tradition of a piece it has never seen 70.9% of the time across 1,000 pieces in six corpora.')

# ---- forecast, two claims ----
g = adefs('fc2')
g += T(590, 70, THROUGH_A, 34, 700, INK, 'middle') + T(590, 118, THROUGH_B, 34, 700, ACC, 'middle')
for k, (a, st, kk, col) in enumerate(CLAIMS):
    y = 180 + k * 120
    g += F(k + 1, C(80, y + 32, 26, col) + T(80, y + 41, str(k + 1), 22, 700, '#fff', 'middle') + wrap(125, y + 26, a, 21, 600, INK, width=72, lh=29) + tag(125, y + 70, st, kk))
g += F(3, T(590, 460, 'Two settings, one question: where did the change go?', 19, 700, MUT, 'middle'))
FORECAST2 = sec('Two claims for the next forty minutes', SVG(g), ch='0',
                notes='Language is published and the result is solid. Music is in progress: the data side has numbers, the generator side is being tested, and the brain is the judge.')

# ---- part dividers, plain ----
def divider(title, line, ch):
    g = T(590, 170, THROUGH_A, 30, 700, INK, 'middle') + T(590, 215, THROUGH_B, 30, 700, ACC, 'middle') + T(590, 300, line, 22, 600, AC2, 'middle')
    return sec(title, SVG(g, 420), ch=ch, cls='divider')
DIV1 = divider('Part 1. Language models', 'Where does an edit go inside a language model?', '1')
DIV3 = divider('Part 3. Beyond language and music', 'Every model operation, every sequence generator', '3')

# ---- refusal, redrawn ----
g = adefs('rf')
g += T(300, 40, 'A chat model asked something harmful', 17, 700, INK, 'middle')
bars = [('normal model', 0.95, AC2), ('one direction removed', 0.05, ACC)]
for k, (lab, v, col) in enumerate(bars):
    y = 90 + k * 110
    g += T(40, y + 30, lab, 17, 700, col) + R(250, y, 300 * v + 4, 46, col, 'none', 0, 4) + T(250 + 300 * v + 16, y + 31, 'refuses' if k == 0 else 'almost never refuses', 16, 700, col)
g += T(300, 330, 'schematic, the pattern holds in all 13 chat models tested', 13, 400, MUT, 'middle')
g += F(1, R(720, 60, 430, 250, SOFT, LINE, 1, 12) + T(745, 100, 'How it is found', 18, 700, AC2) + T(745, 140, 'average the activations on harmful', 15, 400, INK) + T(745, 164, 'requests, minus harmless ones,', 15, 400, INK) + T(745, 188, 'at one layer: one arrow.', 15, 400, INK) + T(745, 236, 'Remove that arrow everywhere:', 15, 700, ACC) + T(745, 260, 'the model stops refusing.', 15, 700, ACC))
g += F(2, T(590, 420, 'One vector switches a whole behavior off.', 22, 700, INK, 'middle'))
REFUSAL = sec('One direction switches refusal off across 13 chat models', SVG(g), ch='1',
              ref='Arditi et al., Refusal in Language Models Is Mediated by a Single Direction, NeurIPS 2024, Figure 1 (redrawn)',
              notes='Our own drawing of Arditi et al. Figure 1. Their figure shows 13 models, each with refusal near 1 before and near 0 after directional ablation.')

g = adefs('sv')
import random as _r
_r.seed(3)
pts = [_r.gauss(1.2, 1.6) for _ in range(60)]
g += L(120, 300, 1060, 300, INK, 2) + L(590, 90, 590, 310, '#c0392b', 2, 'stroke-dasharray="6 5"') + T(590, 330, '0: no effect', 13, 700, '#c0392b', 'middle')
for v in pts:
    x = 590 + v * 85; y = 230 - _r.uniform(0, 110)
    g += C(round(x), round(y), 6, ACC if v > 0 else AC2, extra='opacity=".8"')
g += T(1060, 325, 'moved the intended way', 14, 700, ACC, 'end') + T(120, 325, 'moved the opposite way', 14, 700, AC2)
g += F(1, P(f'M{590+1.2*85},80 L{590+1.2*85},300', ACC, 4) + T(590 + 1.2 * 85 + 10, 92, 'average: it works', 17, 700, ACC))
g += F(2, R(130, 360, 920, 60, SOFT, LINE, 1, 10) + T(590, 397, 'Same vector, single inputs: many move the opposite way.', 19, 700, INK, 'middle'))
CRITIQUE = sec('The same steering vector fails on many single inputs', SVG(g), ch='1',
               ref='Tan et al., Analysing the Generalisation and Reliability of Steering Vectors, NeurIPS 2024, Figure 1 (schematic redraw)',
               notes='Schematic redraw of Tan et al.: each dot is one input. The average effect is positive, but a large share of inputs move against the steering. A vector is reliable on average, not per input.')

# ---- take away only ----
g = adefs('tk2')
g += T(590, 60, THROUGH_A, 32, 700, INK, 'middle') + T(590, 104, THROUGH_B, 32, 700, ACC, 'middle')
for k, (a, st, kk, col) in enumerate(CLAIMS):
    y = 160 + k * 110
    g += F(k + 1, C(80, y + 32, 26, col) + T(80, y + 41, str(k + 1), 22, 700, '#fff', 'middle') + wrap(125, y + 26, a, 21, 600, INK, width=72, lh=29) + tag(125, y + 70, st, kk))
g += F(3, T(590, 430, 'A graph inside a generator is a hypothesis about the model.', 20, 700, INK, 'middle') + T(590, 462, 'A listener\'s brain is the only judge that did not write the exam.', 20, 700, ACC, 'middle'))
TAKEAWAY = sec('Take away', SVG(g), ch='4')

# ======================= ROUND 4 (Nov 2 2026): Space Needle anchor =======================
RED = '#c0392b'

def redtag(x, y, s_):
    w = len(s_) * 7.2 + 20
    return R(x, y, w, 22, '#fdecea', RED, 1.5, 11) + T(x + w / 2, y + 15.5, s_, 12.5, 700, RED, 'middle')

# ---- silent failure: the edit is a shortcut, the old fact is still inside ----
g = adefs('sf')
g += R(30, 210, 116, 42, SOFT, INK, 2, 21) + T(88, 237, 'Space Needle', 15, 700, INK, 'middle')
lay = [(190, 231), (280, 231), (370, 231), (460, 231)]
g += P(f'M146,231 L{lay[0][0]-9},231', AC2, 4)
for k in range(3):
    g += P(f'M{lay[k][0]+9},231 L{lay[k+1][0]-9},231', AC2, 4)
g += ''.join(C(x, y, 9, '#fff', AC2, 3) + T(x, y - 18, f'layer {k+1}', 12, 600, MUT, 'middle') for k, (x, y) in enumerate(lay))
g += P('M469,231 L496,231 L536,174', AC2, 4, extra='marker-end="url(#sfa)"') + R(512, 128, 104, 40, '#fff', AC2, 2, 20) + T(564, 154, 'Seattle', 16, 700, AC2, 'middle')
g += T(320, 110, 'what the model learned in training', 14, 600, MUT, 'middle')
ed = P('M280,240 C300,330 420,340 506,335', ACC, 4.5, extra='marker-end="url(#sfo)"') + R(506, 315, 96, 40, ACL, ACC, 2, 20) + T(554, 341, 'Paris', 16, 700, ACC, 'middle')
ed += T(370, 378, 'the edit: a new shortcut', 15, 700, ACC, 'middle')
c1 = R(640, 40, 510, 100, '#fff', LINE, 1.5, 10) + T(660, 70, 'The test prompt', 13, 700, MUT) + T(660, 98, 'The Space Needle is in ___', 17, 600, INK) + T(660, 126, 'Paris', 17, 700, ACC) + tag(720, 111, 'exam: pass', 'done')
g += F(1, ed + c1)
c2 = R(640, 155, 510, 120, '#fff', LINE, 1.5, 10) + T(660, 185, 'A slightly different prompt', 13, 700, MUT) + T(660, 212, 'Is the Space Needle in Seattle?', 16, 400, MUT) + T(660, 238, 'The Space Needle is in ___', 17, 600, INK) + T(660, 264, 'Seattle', 17, 700, RED) + redtag(740, 249, 'old fact returns')
c2 += T(320, 165, 'old path: still intact', 14, 700, AC2, 'middle')
g += F(2, c2)
ev = R(640, 290, 510, 140, SOFT, LINE, 1, 10) + T(660, 316, 'Measured, not hypothetical', 14.5, 700, AC2)
ev += wrap(660, 340, 'Xie et al., ACL 2025: crafted prompts bring the original answer back, and specific attention heads still carry it.', 13, 400, INK, width=72, lh=18)
ev += wrap(660, 385, 'Zhang et al., ICLR 2025: after editing Microsoft\'s founder to Steve Jobs, ROME answers "Steve Jobs" to "Which college did the founder of Microsoft attend?" 41% of the time, 0.27% before.', 13, 400, INK, width=72, lh=18)
g += F(3, ev)
g += F(4, T(590, 470, 'The old fact was never removed. The edit added a shortcut around it.', 19, 700, INK, 'middle'))
SILENT = sec('A silent failure: the edit passes, and the old fact is still inside', SVG(g), ch='0',
             ref='Xie et al., Revealing the Deceptiveness of Knowledge Editing, ACL 2025. Zhang et al., Uncovering Overfitting in Large Language Model Editing, ICLR 2025. Space Needle example is an illustration',
             notes='Running example for the whole language part: the Space Needle edited from Seattle to Paris. The test prompt passes. A prompt that mentions Seattle first brings the old answer back. Xie et al. show this with real edits (their example: US president) and find attention heads that still carry the original fact. Zhang et al. show the shortcut from the other side: the edit target leaks into unrelated questions.')

# ---- knowledge graph ripple ----
g = adefs('kg')
def kn(x, y, label, col, fill='#fff', w=150):
    return R(x - w / 2, y - 22, w, 44, fill, col, 2, 22) + T(x, y + 6, label, 16, 700, col, 'middle')
SN, SE, US, PA, FR = (130, 245), (420, 120), (750, 120), (420, 370), (750, 370)
base = P('M205,232 L345,138', AC2, 3, extra='marker-end="url(#kga)"') + T(306, 210, 'located in', 13, 600, AC2, 'start')
base += P('M495,120 L673,120', AC2, 3, extra='marker-end="url(#kga)"') + T(585, 108, 'country', 13, 600, AC2, 'middle')
base += P('M495,370 L673,370', '#9aa6ae', 2.5, extra='marker-end="url(#kgg)" stroke-dasharray="7 5"') + T(585, 358, 'country', 13, 600, '#9aa6ae', 'middle')
base += kn(*SN, 'Space Needle', INK, SOFT) + kn(*SE, 'Seattle', AC2) + kn(*US, 'United States', AC2, '#fff', 170) + kn(*PA, 'Paris', '#9aa6ae') + kn(*FR, 'France', '#9aa6ae')
g += T(450, 40, 'What the model knows, drawn as a knowledge graph', 15, 700, INK, 'middle') + base
f1 = P('M268,177 L290,199 M290,177 L268,199', RED, 4, extra='stroke-linecap="round"')
f1 += P('M205,258 L345,352', ACC, 4, extra='marker-end="url(#kgo)"') + T(235, 330, 'edited: located in', 13.5, 700, ACC, 'middle') + kn(*PA, 'Paris', ACC, ACL)
g += F(1, f1)
q = R(870, 40, 290, 150, '#fff', LINE, 1.5, 12) + T(890, 72, 'Ask one step further', 14, 700, MUT) + T(890, 102, 'Which country is the', 17, 600, INK) + T(890, 126, 'Space Needle in?', 17, 600, INK) + T(890, 162, 'should be: France', 16, 700, ACC)
q += P('M495,370 L673,370', ACC, 4, extra='marker-end="url(#kgo)" stroke-dasharray="7 5"') + kn(*FR, 'France', ACC, ACL)
g += F(2, q)
a = R(870, 205, 290, 70, '#fdecea', RED, 2, 12) + T(890, 235, 'edited model says', 14, 600, RED) + T(890, 262, 'United States', 19, 700, RED)
a += P('M495,120 L673,120', RED, 6, extra='stroke-opacity=".35" stroke-linecap="round"')
g += F(3, a)
ev = R(870, 290, 290, 140, SOFT, LINE, 1, 12) + wrap(888, 316, 'RippleEdits and MQuAKE test exactly this. Editors such as ROME and MEMIT change the edited fact but rarely carry the change to facts that depend on it.', 13, 400, INK, width=38, lh=18)
g += F(4, ev + T(450, 466, 'Change one edge, and its neighbors do not move.', 20, 700, INK, 'middle'))
RIPPLE = sec('Edit one fact in a knowledge graph, and the facts around it do not follow', SVG(g), ch='0',
             ref='Cohen et al., Evaluating the Ripple Effects of Knowledge Editing in Language Models, TACL 2024. Zhong et al., MQuAKE, EMNLP 2023. Space Needle example is an illustration of the failure type',
             notes='Same Space Needle edit. One edge changes from Seattle to Paris. A question one hop away, which country, should now say France, but the model still walks the old path through Seattle and says United States. This is the knowledge graph view of the problem, and it is exactly what a graph inside the model should be able to see.')

# ======================= ASSEMBLY =======================
def assemble(cover, old):
    """old: the reused slides from the earlier deck, keyed by their old index"""
    surg = retitle(old[3].replace(' The map next.', '').replace('>CEO of Apple is<', '>Space Needle is in<').replace('>Steve Jobs<', '>Seattle<').replace('>Tim Cook<', '>Paris<'), 'A released model is not left alone. Seven kinds of surgery.')
    story = old[43]
    receipts = old[45]
    delta_paper = retitle(old[47], 'Our delta graph: rank edits by how the inside rewired').replace('class="divider" ', '', 1)
    vision = [cover, surg, story, SILENT, RIPPLE, receipts, VECTOR, delta_paper, DEMO2, MUSRES, FORECAST2]
    rome = old[33]
    a = rome.find('<div class="note"'); e = rome.find('  <div class="ref">')
    rome = rome[:a] + '<div class="note" style="font-size:.62em"><div class="key">The finding</div><p class="one" style="font-size:1.25em">A fact sits in two places. Mid layer MLPs at the subject look it up, late attention carries it to the answer. Editing a fact means changing the first place.</p></div>\n  </div>\n' + rome[e:]
    rome = retitle(rome, 'A fact lives in mid layer MLPs and moves out by attention')
    d46 = old[46].replace('running example from slide 45: the Space Needle edit', 'running example: the Space Needle edit').replace(' (slide 2).', '.')
    lang = [DIV1, REFUSAL, CRITIQUE, rome, old[35].replace('Guo 2025, slide 31', 'Guo 2025'), d46, old[48], old[49], old[50], old[51]]
    four = retitle(FOUR, 'Music generation went from a visible graph to a hidden one')
    four = re.sub(r'\s*<p class="q">.*?</p>', '', four, count=1, flags=re.S)
    tools = retitle(TOOLS, 'Every tool inside MusicGen reads one layer at one moment').replace('Three tools, three questions, all at one layer and one moment.', 'Language models moved on to attribution graphs. Music has not.')
    b1 = retitle(BRAIN1, 'Listeners\' brains track a Markov model\'s surprise, note by note')
    b1 = b1.replace(ph(60, 230, 400, 140, 'Original figure: Di Liberto et al. 2020', 'eLife, to add when the site is reachable'),
                    R(60, 230, 400, 140, ACL, ACC, 1.5, 10) + T(80, 270, 'The listener model is a graph', 17, 700, ACC) + T(80, 300, 'IDyOM counts transitions between notes', 14.5, 400, INK) + T(80, 324, 'with several context lengths, like the', 14.5, 400, INK) + T(80, 348, 'tiny graph from the opening.', 14.5, 400, INK))
    b2 = retitle(BRAIN2, 'The brain carries enough of the music to rebuild it').replace('Denk et al., Brain2Music, arXiv 2307.11078, 2023.', 'Denk et al., Text to music generation models capture musical semantic representations in the human brain, Nature Communications 2025 (Brain2Music).')
    mus = [retitle(CORPUS, 'Occam\'s razor: the simplest graph already names the tradition').replace('data-ch="2"', 'data-ch="2" class="divider"', 1),
           retitle(PATH, 'Too little memory gives a graph without syntax, too much gives a path'),
           four, retitle(VZ.ANAT, 'MusicGen emits tokens step by step: a graph almost for free'), tools, b1, b2,
           retitle(BRAIN3, 'Layers predict the brain for language, not yet for music'),
           retitle(BRAIN4, 'A steered style must land in the listener\'s brain, or it did not land'),
           retitle(NEXT, 'Four outcomes, and the listener decides which one')]
    beyond = [VZ.B[0].replace('Not yet shown.', ''), DROP]
    close = [TAKEAWAY]
    parts = {'vision': vision, 'language': lang, 'music': mus, 'beyond': beyond, 'close': close}
    return parts
