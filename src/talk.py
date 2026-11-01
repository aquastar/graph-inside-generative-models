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

# ======================= ASSEMBLY =======================
def assemble(cover, old):
    """old: the reused language slides from the earlier deck, keyed by their old index"""
    lang = [VZ.P1DIV, old[3], old[25], old[26], old[33], old[35], old[45], old[48], old[49], SHAPE, BRIDGE]
    vision = TRAILER + [cover.replace('class="title titlehero"', 'class="title titlehero full"', 1), VZ.V[0], SAME, FACTS, VZ.V[1], THREE, NETSCI, PROGRAM]
    mus = [FOUR, FE_LEARN, FE_COMPOSE, CORPUS, PATH, rech(VZ.MUSIC[1], '2'), VZ.MERGE_MS, VZ.ANAT, TOOLS, rech(VZ.MUSIC[6], '2'),
           BRAIN1, BRAIN2, BRAIN3, BRAIN4, rech(VZ.MUSIC[8], '2'), PILOT, NEXT]
    beyond = [VZ.B[0], VZ.B[1], DROP]
    close = [TWO, HELP, TAKE]
    parts = {'vision': vision, 'language': lang, 'music': mus, 'beyond': beyond, 'close': close}
    return parts


# ======================= TRAILER =======================
# Full bleed dark slides before the title. Entrance animations replay every time a
# slide opens: elements with class "a" rise in after --d, "dr" paths draw, "g" bars
# grow, "p" marks pop. Numbers with data-count count up (script in build.py).
TRAILER_CSS = '''
.reveal section.trailer,.reveal section.trailer *{font-family:"Fira Sans",sans-serif}
.reveal section.trailer{padding:0 !important;color:#e8edf0}
.reveal .slides>section.trailer.present{display:block !important}
.reveal section.trailer .tk{position:absolute;left:64px;top:44px;margin:0;font-size:15px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:#F76902;text-align:left}
.reveal section.trailer .hl{position:absolute;left:64px;top:74px;width:1150px;margin:0;font-size:44px;line-height:1.14;font-weight:600;color:#fff;text-align:left;letter-spacing:-.01em}
.reveal section.trailer .hl em{font-style:normal;color:#F76902}
.reveal section.trailer .hl i{font-style:normal;color:#38b2c4}
.reveal section.trailer .pay{position:absolute;left:64px;bottom:46px;width:1150px;margin:0;font-size:25px;line-height:1.3;color:#c9d2d8;text-align:left}
.reveal section.trailer .pay b{color:#fff;font-weight:600}
.reveal section.trailer .src{position:absolute;left:64px;bottom:16px;margin:0;font-size:13px;color:#7d8a93;text-align:left}
.reveal section.trailer .tag{position:absolute;right:56px;top:40px;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:6px 11px;border-radius:3px;color:#fff}
.reveal section.trailer .tag.pub{background:#2f7d4f}.reveal section.trailer .tag.rev{background:#4C5B66}.reveal section.trailer .tag.prog{background:#F76902}
.reveal section.trailer .stage{position:absolute;left:64px;width:1150px}
.reveal section.trailer .card{position:absolute;background:#fff;border-radius:14px;box-shadow:0 0 0 1px rgba(255,255,255,.08),0 30px 80px rgba(0,0,0,.55),0 0 120px rgba(247,105,2,.18);overflow:hidden}
@keyframes tr-rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes tr-fade{from{opacity:0}to{opacity:1}}
@keyframes tr-pop{0%{opacity:0;transform:scale(.3)}70%{opacity:1;transform:scale(1.18)}100%{opacity:1;transform:scale(1)}}
@keyframes tr-draw{to{stroke-dashoffset:0}}
@keyframes tr-grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.reveal section.trailer .a,.reveal section.trailer .p{opacity:0}
.reveal section.trailer.present .a{animation:tr-rise .8s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0s)}
.reveal section.trailer.present .a.f{animation-name:tr-fade}
.reveal section.trailer.present .p{animation:tr-pop .45s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0s);transform-box:fill-box;transform-origin:center}
.reveal section.trailer .dr{stroke-dasharray:var(--len,1200);stroke-dashoffset:var(--len,1200)}
.reveal section.trailer.present .dr{animation:tr-draw var(--t,1.2s) ease-in-out both;animation-delay:var(--d,0s)}
.reveal section.trailer .g{transform-box:fill-box;transform-origin:left center;transform:scaleX(0)}
.reveal section.trailer.present .g{animation:tr-grow 1s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0s)}
@media (prefers-reduced-motion:reduce){.reveal section.trailer .a,.reveal section.trailer .p{opacity:1;animation:none !important}.reveal section.trailer .dr{stroke-dashoffset:0;animation:none !important}.reveal section.trailer .g{transform:none;animation:none !important}}
'''

DARK_BG = 'data-background-gradient="radial-gradient(ellipse at 70% 40%,#1c2633 0%,#141a22 55%,#0d1117 100%)"'
WT, DM, TL = '#ffffff', '#8c9aa4', '#38b2c4'

def d(t):
    return f'style="--d:{t:.2f}s"'

def tsec(inner, notes='', tag=''):
    tg = {'pub': '<span class="tag pub a f" style="--d:.2s">Published</span>', 'rev': '<span class="tag rev a f" style="--d:.2s">Under review</span>',
          'prog': '<span class="tag prog a f" style="--d:.2s">In progress</span>'}.get(tag, '')
    n = f'\n  <aside class="notes">{notes}</aside>' if notes else ''
    return f'<section class="trailer full" data-ch="0" {DARK_BG}>\n  {tg}{inner}{n}\n</section>'

def tT(x, y, s, size, w=400, fill=WT, a='start', cls='', dd=None, extra=''):
    st = f' style="--d:{dd:.2f}s"' if dd is not None else ''
    c = f' class="{cls}"' if cls else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}"{c}{st} {extra}>{s}</text>'

# ---- T0 cold open: the Für Elise graph, learning then composing ----
TR0 = tsec('''<p class="tk a" style="--d:.1s">Beethoven, Für Elise, opening bars</p>
  <p class="hl a" style="--d:.3s">This generator is a graph. <i>Watch it learn, then compose.</i></p>
  <div class="card a" style="--d:.9s;left:170px;top:150px;width:940px;height:370px">
    <iframe class="fe-frame" data-src="figs/fe-chain.html?autoplay=1" title="Für Elise Markov chain" style="width:940px;height:370px;border:0;background:#fff"></iframe>
  </div>
  <p class="pay a" style="--d:2.4s;bottom:38px">Every move draws an arrow. Then the arrows write music Beethoven never wrote.</p>''',
  notes='Cold open. Say nothing for the first few seconds, let the ball walk the melody. Then: this is a complete generative model, and every decision it makes is a visible edge. Large neural generators have no such picture. The talk asks whether one is hiding inside them. Click the animation for sound.')

# ---- T1 language result: silent edit failures ----
rows = [('check 20 at random', 11, DM, '#5d6b75'), ('pick by editor and model', 14, DM, '#5d6b75'), ('pick by our delta graph', 17, '#F76902', '#F76902')]
g = ''
for r, (lab, k, lc, cc) in enumerate(rows):
    y = 30 + r * 92; t0 = 1.6 + r * 1.25
    g += tT(320, y + 30, lab, 22, 700 if r == 2 else 500, '#fff' if r == 2 else '#c9d2d8', 'end', 'a', t0 - .3)
    for j in range(20):
        x = 345 + j * 37
        bad = j < k
        fill = (cc if r == 2 else '#c0503a') if bad else '#2a3640'
        g += f'<rect class="p" style="--d:{t0 + j * .045:.2f}s" x="{x}" y="{y}" width="31" height="44" rx="4" fill="{fill}"/>'
        if bad:
            g += f'<path class="p" style="--d:{t0 + j * .045 + .05:.2f}s" d="M{x+9},{y+15} L{x+22},{y+29} M{x+22},{y+15} L{x+9},{y+29}" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    g += f'<text x="1100" y="{y + 36}" font-size="40" font-weight="700" fill="{lc if r < 2 else "#F76902"}" text-anchor="middle" class="a f" style="--d:{t0 + .9:.2f}s" data-count="{k}" data-delay="{t0 + .9:.2f}">0</text>'
g += tT(1146, 300, 'broken edits caught', 15, 600, DM, 'end', 'a f', 5.2)
TR1 = tsec(f'''<p class="tk a" style="--d:.1s">Language models: editing one fact</p>
  <p class="hl a" style="--d:.3s">100 edits. Every one passes its own test.<br><em>56 are secretly broken.</em></p>
  <svg class="stage" style="top:228px;height:320px" viewBox="0 0 1150 320">{g}</svg>
  <p class="pay a" style="--d:5.4s">Same budget of 20 checks, <b>half again as many broken edits caught</b>, read only from how the inside rewired.</p>
  <p class="src a f" style="--d:5.6s">Benbrahim et al., SDM 2026. Rates from the paper: 56%, 70%, 86% bad among the 20 checked.</p>''', tag='pub',
  notes='Result one, language. An edit can pass the benchmark and still break related facts. With the same checking budget, ranking by our delta graph finds about 17 broken edits where random checking finds about 11. The details come in Part 1.')

# ---- T2 music data graph: 144 numbers ----
fe_counts = {(0, 2): 2, (0, 3): 2, (0, 7): 1, (2, 0): 1, (2, 3): 1, (2, 5): 2, (2, 7): 2, (3, 0): 2, (3, 2): 1, (3, 7): 3, (5, 3): 2, (6, 7): 4, (7, 0): 2, (7, 2): 2, (7, 3): 1, (7, 6): 4, (7, 7): 1, (7, 11): 1, (11, 2): 1}
rowsum = {i: sum(v for (a, b), v in fe_counts.items() if a == i) for i in range(12)}
g = ''
cs, gx, gy = 25, 70, 20
for i in range(12):
    for j in range(12):
        v = fe_counts.get((i, j), 0) / rowsum[i] if rowsum[i] else 0
        fill = f'rgba(247,105,2,{0.25 + 0.75 * v:.2f})' if v else '#222c35'
        g += f'<rect class="p" style="--d:{0.9 + (i * 12 + j) * 0.011:.2f}s" x="{gx + j * cs}" y="{gy + i * cs}" width="{cs - 3}" height="{cs - 3}" rx="3" fill="{fill}"/>'
g += tT(gx + 6 * cs, gy + 12 * cs + 30, 'Für Elise as a 12 by 12 table', 16, 600, DM, 'middle', 'a f', 2.4)
g += f'<text x="720" y="140" font-size="120" font-weight="700" fill="#F76902" text-anchor="middle" class="a f" style="--d:3.0s" data-count="70.9" data-dec="1" data-suffix="%" data-delay="3.0">0%</text>'
g += tT(720, 186, 'of unseen pieces placed in the right tradition', 20, 500, '#c9d2d8', 'middle', 'a', 3.4)
g += tT(470, 250, 'guessing the biggest corpus', 16, 500, DM, 'start', 'a f', 4.0) + f'<rect class="g" style="--d:4.0s" x="470" y="262" width="{500 * .2:.0f}" height="22" rx="3" fill="#4C5B66"/>' + tT(470 + 500 * .2 + 10, 279, '20%', 16, 700, DM, 'start', 'a f', 4.6)
g += tT(470, 320, '144 numbers, plain logistic regression', 16, 600, WT, 'start', 'a f', 4.4) + f'<rect class="g" style="--d:4.4s" x="470" y="332" width="{500 * .709:.0f}" height="22" rx="3" fill="#F76902"/>' + tT(470 + 500 * .709 + 10, 349, '70.9%', 16, 700, '#F76902', 'start', 'a f', 5.0)
TR2 = tsec(f'''<p class="tk a" style="--d:.1s">Music: a graph read from the notes</p>
  <p class="hl a" style="--d:.3s">One melody becomes <em>144 numbers.</em> No music theory.</p>
  <svg class="stage" style="top:170px;height:380px" viewBox="0 0 1150 380">{g}</svg>
  <p class="pay a" style="--d:5.4s">A first order graph already carries a style: <b>1,000 pieces, six traditions</b>, Bach to fiddle tunes.</p>
  <p class="src a f" style="--d:5.6s">Five fold cross validation, majority baseline 20%. zhiqian.ai/music-markov</p>''', tag='prog',
  notes='Result two. The table is the real one for the Für Elise opening, rows are the current scale degree, columns the next. The same 144 numbers per piece, fed to a plain classifier, name the tradition of a piece it has never seen 70.9% of the time.')

# ---- T3 music model: one way steering ----
def isl(cx, cy, dd):
    pth = f'M{cx-150},{cy+20} C{cx-110},{cy-60} {cx-20},{cy-50} {cx+30},{cy-30} C{cx+110},{cy-5} {cx+160},{cy+30} {cx+120},{cy+60} C{cx+60},{cy+95} {cx-120},{cy+85} {cx-150},{cy+20} Z'
    return f'<path class="a f" style="--d:{dd:.2f}s" d="{pth}" fill="rgba(56,178,196,.16)" stroke="{TL}" stroke-width="3"/>' + tT(cx, cy + 30, 'a style', 18, 700, TL, 'middle', 'a f', dd)
g = isl(260, 190, 1.0) + isl(860, 190, 1.0)
g += tT(260, 30, 'remove a style', 24, 700, WT, 'middle', 'a', .9) + tT(860, 30, 'add a style', 24, 700, WT, 'middle', 'a', .9)
for k, (sx, sy, ex, ey) in enumerate([(230, 195, 110, 75), (265, 185, 280, 55), (300, 195, 440, 90)]):
    g += f'<path class="dr" style="--d:{1.8 + k * .35:.2f}s;--len:220" d="M{sx},{sy} L{ex},{ey}" stroke="#F76902" stroke-width="4" fill="none" stroke-linecap="round" marker-end="url(#trA)"/>'
g += ''.join(f'<circle class="p" style="--d:1.6s" cx="{x}" cy="{y}" r="6" fill="#F76902"/>' for x, y in [(230, 195), (265, 185), (300, 195)])
g += f'<circle class="p" style="--d:3.0s" cx="260" cy="350" r="26" fill="#2f7d4f"/>' + f'<path class="p" style="--d:3.1s" d="M247,350 L257,361 L275,340" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/>'
g += tT(300, 358, 'leaves easily, still music', 19, 600, WT, 'start', 'a', 3.1)
for k, (sx, sy, ex, ey) in enumerate([(640, 60, 750, 140), (1100, 50, 990, 140), (650, 330, 720, 270)]):
    g += f'<path class="dr" style="--d:{3.6 + k * .4:.2f}s;--len:200" d="M{sx},{sy} L{ex},{ey}" stroke="#F76902" stroke-width="4" fill="none" stroke-dasharray="10 8" stroke-linecap="round"/>'
    g += f'<path class="p" style="--d:{4.0 + k * .4:.2f}s" d="M{ex-9},{ey-9} L{ex+9},{ey+9} M{ex+9},{ey-9} L{ex-9},{ey+9}" stroke="#ff7a59" stroke-width="4" stroke-linecap="round"/>'
g += f'<circle class="p" style="--d:5.0s" cx="860" cy="350" r="26" fill="#c0503a"/>' + f'<path class="p" style="--d:5.1s" d="M850,340 L870,360 M870,340 L850,360" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
g += tT(900, 358, 'the push misses', 19, 600, WT, 'start', 'a', 5.1)
g = '<defs><marker id="trA" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#F76902"/></marker></defs>' + g + f'<line class="a f" style="--d:.9s" x1="560" y1="20" x2="560" y2="370" stroke="#2a3640" stroke-width="2"/>'
TR3 = tsec(f'''<p class="tk a" style="--d:.1s">Music: steering a neural generator</p>
  <p class="hl a" style="--d:.3s">Inside MusicGen, steering a style is <em>one way.</em></p>
  <svg class="stage" style="top:160px;height:380px" viewBox="0 0 1150 380">{g}</svg>
  <p class="pay a" style="--d:5.6s">Many exits, almost no entrances. <b>That sounds like a fact about a graph.</b></p>
  <p class="src a f" style="--d:5.8s">Co-authored work under review. MusicGen small and medium.</p>''', tag='rev',
  notes='Result three. Subtract a style direction and the style fades while the music stays coherent. Add the same direction and the output does not acquire the style. A vector cannot explain that asymmetry. Reachability on a directed graph can.')

# ---- T4 memory: graph or path ----
g = ''
pts = [(250 + 120 * math.cos(2 * math.pi * k / 10 - math.pi / 2), 190 + 120 * math.sin(2 * math.pi * k / 10 - math.pi / 2)) for k in range(10)]
walk1 = [0, 3, 1, 3, 0, 5, 2, 7, 3, 0, 4, 8, 1, 6, 9, 3, 0, 2, 5, 3, 7, 1, 4, 0]
pd = 'M' + ' L'.join(f'{pts[a][0]:.0f},{pts[a][1]:.0f}' for a in walk1)
g += f'<path class="dr" style="--d:1.2s;--t:3.2s;--len:6000" d="{pd}" stroke="#38b2c4" stroke-width="2.5" stroke-opacity=".75" fill="none"/>'
g += ''.join(f'<circle class="p" style="--d:{.8 + k * .05:.2f}s" cx="{x:.0f}" cy="{y:.0f}" r="12" fill="#141a22" stroke="#38b2c4" stroke-width="3"/>' for k, (x, y) in enumerate(pts))
g += tT(250, 30, 'first order', 24, 700, TL, 'middle', 'a', .9)
g += f'<text x="250" y="378" font-size="46" font-weight="700" fill="#38b2c4" text-anchor="middle" class="a f" style="--d:3.6s" data-count="89" data-suffix="%" data-delay="3.6">0%</text>'
g += tT(330, 370, 'of steps revisit a node', 16, 500, DM, 'start', 'a f', 3.8)
xs = [640 + k * 15 for k in range(32)]
ys = [190 + 95 * math.sin(k * 1.1) * (0.6 + 0.4 * math.cos(k * .37)) for k in range(32)]
pd2 = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in zip(xs, ys))
g += f'<path class="dr" style="--d:2.0s;--t:3s;--len:2400" d="{pd2}" stroke="#F76902" stroke-width="3" fill="none"/>'
g += ''.join(f'<circle class="p" style="--d:{2.0 + k * .09:.2f}s" cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#141a22" stroke="#F76902" stroke-width="2"/>' for k, (x, y) in enumerate(zip(xs, ys)))
g += tT(870, 30, 'third order', 24, 700, '#F76902', 'middle', 'a', 1.8)
g += f'<text x="760" y="378" font-size="46" font-weight="700" fill="#F76902" text-anchor="middle" class="a f" style="--d:5.0s" data-count="6" data-suffix="%" data-delay="5.0">0%</text>'
g += tT(820, 370, 'revisit: the piece memorized', 16, 500, DM, 'start', 'a f', 5.2)
g += f'<line class="a f" style="--d:.9s" x1="540" y1="20" x2="540" y2="380" stroke="#2a3640" stroke-width="2"/>'
TR4 = tsec(f'''<p class="tk a" style="--d:.1s">Music: how much memory makes a style</p>
  <p class="hl a" style="--d:.3s">Too little memory: a graph. Too much: <em>a path.</em></p>
  <svg class="stage" style="top:160px;height:390px" viewBox="0 0 1150 390">{g}</svg>
  <p class="pay a" style="--d:5.8s">Same Bach chorale, 10 nodes versus 81. <b>The graph worth finding lives in between.</b></p>
  <p class="src a f" style="--d:6.0s">An 89 note Bach chorale at first and third order. Drawings are schematic, numbers are measured.</p>''', tag='prog',
  notes='Result four. At first order the walk keeps returning to the same ten states, so it is a real graph, but an LLM judge can tell its output from Bach almost every time. At third order the piece becomes a path through 81 states and stops generalizing. Second order already recovers key regions. The open question is which contexts earn longer memory.')

TRAILER = [TR0, TR1, TR2, TR3, TR4]
