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
            notes='Five single numbers: max edge change 0.589, mean 0.572, total 0.575, top 5 node share 0.564, top 1 node share 0.521. Trained on 200 facts and tested on 500 unseen ones, the AUC holds at 0.840 to 0.862 (the slide boxes are the wiki_recent run, 0.853 to 0.904). Only 2 of the 50 riskiest flip when rerun. Labels depend on which 12 held out prompts define failure. Scale: 7B and 8B models, three editors, two benchmark families.')

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
conf = [[64, 10, 1, 18, 3, 4], [12, 70, 0, 4, 12, 1], [10, 6, 53, 24, 0, 6], [17, 5, 1, 70, 3, 4], [3, 10, 0, 2, 83, 2], [4, 4, 0, 22, 4, 66]]  # 992 melodies, LR order 1, row normalized
g = adefs('cm')
pipe = [('one piece', 'monophonic melody'), ('12 by 12 table', 'scale degree transitions'), ('144 numbers', 'no theory beyond the key'), ('logistic regression', 'names the corpus')]
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
g += F(2, R(820, 70, 330, 120, ACL, ACC, 1.5, 10) + T(985, 128, '70.2%', 44, 700, ACC, 'middle') + T(985, 166, 'five fold accuracy, chance 17%', 14, 600, INK, 'middle'))
g += F(3, R(820, 210, 330, 150, '#fff', LINE, 1.5, 10) + T(840, 240, 'Confusions make musical sense', 15, 700, AC2) + T(840, 268, 'Bach and Palestrina swap about 17%', 13.5, 400, INK) + T(840, 292, 'folk and fiddle swap 10 to 12%', 13.5, 400, INK) + T(840, 316, 'Monteverdi and fiddle: never', 13.5, 400, INK) + T(840, 344, 'row normalized, percent', 12, 400, MUT))
g += F(4, T(590, 465, 'A first order graph already carries a style. 144 numbers name the corpus.', 18, 700, INK, 'middle'))
CORPUS = sec('144 numbers name the corpus', SVG(g), ch='2', status='prog',
             ref='992 melodies, six public corpora (Bach chorales, Essen, Monteverdi, Palestrina, Ryan\'s Mammoth Collection, Trecento), parsed with music21, five fold cross validation. zhiqian.ai/music-markov',
             notes='Chance with six styles is 17%, majority class 21%. Counting the 12 notes without order gives 41.9%, so the graph adds 28 points. Rebuilt from scratch in Nov 2026: 70.2% plus or minus 2.7. No tuning, the number is what the script prints on a first run. The script is public on the site.')

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
res = [('70.2%', '144 numbers per piece name its tradition', 'six corpora, 992 melodies, chance 17%', ACC, 'in progress', 'part'),
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
RED = '#c0392b'
g = adefs('mr')
def clip(x, y, label, sub, col, fill):
    return R(x, y, 210, 70, fill, col, 2, 12) + T(x + 105, y + 31, label, 17, 700, col, 'middle') + T(x + 105, y + 54, sub, 13, 400, INK, 'middle')
g += T(40, 40, 'Remove a style', 19, 700, INK)
g += clip(40, 60, 'a jazz clip', 'MusicGen, jazz prompt', MU, MUL)
g += F(1, P('M254,95 L380,95', ACC, 3.5, extra='marker-end="url(#mro)"') + T(317, 82, 'minus the', 13, 700, ACC, 'middle') + T(317, 120, 'jazz direction', 13, 700, ACC, 'middle')
          + clip(386, 60, 'not jazz any more', 'and still sounds like music', GRN, '#eaf3ea') + C(626, 95, 18, GRN) + P('M617,95 L624,103 L637,87', '#fff', 3.5))
g += T(40, 220, 'Add a style', 19, 700, INK)
g += clip(40, 240, 'a classical clip', 'MusicGen, classical prompt', AC2, SOFT)
g += F(2, P('M254,275 L380,275', ACC, 3.5, extra='marker-end="url(#mro)"') + T(317, 262, 'plus the same', 13, 700, ACC, 'middle') + T(317, 300, 'jazz direction', 13, 700, ACC, 'middle')
          + clip(386, 240, 'still not jazz', 'the push barely registers', RED, '#fdecea'))
g += F(3, P('M600,275 L700,275', ACC, 4.5, extra='marker-end="url(#mro)" stroke-dasharray="8 5"') + T(650, 262, 'push harder', 13, 700, ACC, 'middle')
          + clip(706, 240, 'noise', 'it breaks before it turns jazz', RED, '#fdecea'))
isl = R(760, 40, 390, 170, '#fff', LINE, 1.5, 12) + T(955, 66, 'One picture that would explain it', 15, 700, AC2, 'middle') + T(955, 86, 'our hypothesis, being tested', 12.5, 400, MUT, 'middle')
isl += f'<ellipse cx="955" cy="140" rx="70" ry="38" fill="{MUL}" stroke="{MU}" stroke-width="2.5"/>' + T(955, 146, 'jazz', 15, 700, MU, 'middle')
for ang in (-0.45, 0.35, 2.8, 3.6):
    x1, y1 = 955 + 70 * math.cos(ang), 140 + 38 * math.sin(ang)
    x2, y2 = 955 + 150 * math.cos(ang), 140 + 62 * math.sin(ang)
    isl += P(f'M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}', GRN, 2, extra='marker-end="url(#mra)"')
isl += P('M790,190 C850,175 880,170 893,160', RED, 2, extra='stroke-dasharray="5 4"') + T(786, 182, 'rare way in', 12.5, 600, RED, 'end') + T(955, 200, 'many ways out, few ways in', 13.5, 700, INK, 'middle')
g += F(4, isl + T(590, 380, 'Leaving a style is easy. Entering one is not.', 22, 700, INK, 'middle') + T(590, 414, 'A vector cannot explain that. Reachability on a graph could.', 18, 700, ACC, 'middle'))
MUSRES = sec('Steering leaves a style easily but rarely enters one', SVG(g), ch='0', status='rev',
             ref='Co-authored work under review, MusicGen small and medium. Jazz and classical are an illustration of the two arms',
             notes='Same vector tool as the refusal direction, now in a music generator. Removing a style works and keeps the music coherent. Adding the same direction to music without that style does not make it acquire the style, and a bigger push breaks the audio first. Replace this drawing with real clips and numbers from the paper when available.')

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
          ('Music: a tiny graph already carries a style, and the listener\'s brain is the judge we will use for a generator.', 'in progress', 'part', MU)]

# ---- every surgery is stored as a vector (concrete) ----
g = adefs('vc')
cols4 = [('Steer', 'h ← h + α r', 'add a direction to the', 'activations at run time', 'refusal direction, Arditi et al. 2024'),
         ('Edit', 'W ← W + u vᵀ', 'add a rank one matrix', 'to one layer', 'ROME, Meng et al. 2022'),
         ('LoRA', 'W ← W + B A', 'add a low rank matrix', 'to many layers', 'LoRA, Hu et al. 2022'),
         ('Fine tune', 'θ ← θ + τ', 'add a task vector', 'to all weights', 'task arithmetic, Ilharco et al. 2023')]
for k, (a, eq, d1, d2, cite) in enumerate(cols4):
    x = 30 + k * 283
    blk = R(x, 30, 265, 230, '#fff', LINE, 1.5, 12) + T(x + 132, 70, a, 22, 700, AC2, 'middle')
    blk += R(x + 20, 92, 225, 58, ACL, ACC, 1.5, 10) + T(x + 132, 130, eq, 23, 700, ACC, 'middle', extra='font-family="Fira Mono,monospace"')
    blk += T(x + 132, 182, d1, 14.5, 600, INK, 'middle') + T(x + 132, 202, d2, 14.5, 600, INK, 'middle') + T(x + 132, 238, cite, 12.5, 400, MUT, 'middle')
    g += F(k, blk) if k else blk
g += F(4, R(30, 285, 1120, 100, SOFT, LINE, 1, 12) + T(590, 323, 'Each one tells you exactly what was added.', 22, 700, INK, 'middle') + T(590, 362, 'None tells you which other facts, behaviors or styles moved with it.', 22, 700, ACC, 'middle')
          + T(590, 420, 'Our own test: single numbers about the change barely beat chance (AUC 0.52 to 0.59).', 16, 600, MUT, 'middle')
          + T(590, 456, 'Its shape, the delta graph, lifts editor and model alone from 0.703 to 0.797.', 19, 700, INK, 'middle'))
VECTOR = sec('Every surgery is stored as a vector', SVG(g), ch='0',
             ref='Arditi et al., NeurIPS 2024. Meng et al., NeurIPS 2022. Hu et al., LoRA, ICLR 2022. Ilharco et al., ICLR 2023. Benbrahim et al., SDM 2026, Table 5.1 and Table F.1',
             notes='Four surgeries, four one line formulas a CS audience can read. ROME is a rank one LoRA on one layer, which links knowledge editing to something most of the room has used. The point is not the math, it is that each operation is a single added object, and that object carries no information about its side effects.')

# ---- demo: a tiny graph is enough to represent a piece ----
g = adefs('dm2')
g += f'<foreignObject x="20" y="10" width="740" height="410"><div xmlns="http://www.w3.org/1999/xhtml" style="width:740px;height:410px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1.5px #d3d7da,0 10px 30px rgba(17,17,17,.10)"><iframe class="fe-frame" data-src="figs/fe-chain.html?autoplay=1" title="Für Elise Markov chain" style="width:740px;height:410px;border:0;background:#fff"></iframe></div></foreignObject>'
g += T(790, 34, 'Graphs in music, in this talk', 15, 600, MUT)
MENU = [('1', 'Note to note graph', '144 numbers name the tradition', '70.2%, chance 17%', False),
        ('2', 'Richer nodes', 'note plus its length', '86.8%', False),
        ('3', "The listener's graph", 'its surprise tracks the brain', 'IDyOM, EEG', False),
        ('4', 'A graph inside MusicGen', 'read from the generator itself', 'next step', True)]
for k, (num, name, line, val, plan) in enumerate(MENU):
    y = 50 + k * 92
    row = R(790, y, 370, 80, SOFT, 'none', 0, 3)
    row += (C(818, y + 40, 13, '#fff', MU, 1.5, 'stroke-dasharray="4 3"') + T(818, y + 45, num, 14, 600, MU, 'middle')) if plan else (C(818, y + 40, 13, MU) + T(818, y + 45, num, 14, 600, '#fff', 'middle'))
    row += T(846, y + 34, name, 18, 600, INK) + T(846, y + 58, line, 14, 400, MUT) + T(1148, y + 34, val, 15, 600, MU if not plan else MUT, 'end')
    g += F(k + 1, row) if k else row
g += T(590, 466, 'A tiny graph already captures a style. Part 2 covers this list.', 20, 700, INK, 'middle')
DEMO2 = sec('A tiny graph is enough to represent a piece of music', SVG(g), ch='0', status='prog',
            ref='Opening of Beethoven, Für Elise, animation from zhiqian.ai, click for sound. Five fold cross validation, zhiqian.ai/music-markov',
            notes='Let the ball learn the opening, then compose. Then the point: this little graph is not a toy. The same 144 numbers per piece, fed to a plain classifier, name the tradition of a piece it has never seen 70.2% of the time across 992 melodies in six corpora, against 41.9% for note counts without order.')

# ---- trailer: the delta graph drawn ----
def _dg(ox, oy, edges, mode, lab):
    """4 layers x (attention, MLP). edges: (a, b, w). mode before/after: gray by weight, delta: + orange solid, - dashed"""
    pos = {}
    for L_ in range(4):
        pos[f'{L_+1}a'] = (ox, oy + (3 - L_) * 62)
        pos[f'{L_+1}m'] = (ox + 86, oy + (3 - L_) * 62)
    o = ''
    for a_, b_, w in edges:
        (x1, y1), (x2, y2) = pos[a_], pos[b_]
        long_ = abs(int(a_[0]) - int(b_[0])) > 1
        bend = (-46 if x1 == x2 == ox else 46) if long_ else 0
        sw = 0.6 + 2.6 * abs(w) ** 0.5
        if mode == 'delta':
            col = ACC if w > 0 else AC2
            dash = '' if w > 0 else 'stroke-dasharray="5 4"'
        else:
            col, dash = AC2, f'stroke-opacity="{0.35 + 0.6 * w:.2f}"'
        mx, my = (x1 + x2) / 2 + bend, (y1 + y2) / 2
        o += P(f'M{x1},{y1} Q{mx},{my} {x2},{y2}', col, round(sw, 2), extra=dash + ' stroke-linecap="round"')
    for k_, (x, y) in pos.items():
        o += C(x, y, 9, '#009CBD' if k_.endswith('a') else '#5F6B73')
    o += T(ox + 43, oy + 230, lab, 15, 600, INK, 'middle')
    return o

BEFORE = [('1a', '1m', .8), ('1m', '2a', .6), ('2a', '2m', .7), ('2m', '3a', .55), ('3a', '3m', .7), ('3m', '4a', .5), ('4a', '4m', .6), ('1a', '3a', .3), ('2m', '4m', .3)]
AFTER = [('1a', '1m', .8), ('1m', '2a', .6), ('2a', '2m', .7), ('2m', '3a', .12), ('3a', '3m', .7), ('3m', '4a', .85), ('4a', '4m', .6), ('1a', '3a', .3), ('2m', '4m', .3), ('1m', '4a', .7)]
DELTA = [('1m', '4a', .7), ('3m', '4a', .35), ('2m', '3a', -.43)]
g = adefs('dtg')
g += T(30, 26, 'A real edit from the paper. Every exam says: passed.', 16, 600, MUT)
g += '<image href="figs/delta_construction_real.png" x="20" y="36" width="600" height="233"/>'
g += T(100, 286, 'before the edit', 14, 600, INK, 'middle') + T(275, 286, 'after the edit', 14, 600, INK, 'middle') + T(450, 286, 'after minus before', 14, 600, ACC_T if False else '#C45200', 'middle')
# the same delta read as a graph: blocks by layer, edges where they started moving together
dg = T(30, 324, 'The same difference, drawn as a graph', 15, 600, MUT)
xs = [60 + i * 36 for i in range(16)]
for i, x in enumerate(xs):
    if i < 15:
        dg += L(x, 362, xs[i + 1], 362, '#D7D2CB', 1) + L(x, 410, xs[i + 1], 410, '#D7D2CB', 1)
    dg += L(x, 362, x, 410, '#D7D2CB', 1)
hot = [(5, 'a', 7, 'm', 3.0), (6, 'a', 8, 'a', 2.4), (6, 'm', 8, 'm', 2.4), (5, 'm', 7, 'a', 1.8), (7, 'a', 9, 'm', 1.6), (6, 'a', 7, 'm', 2.2)]
for i, ti, j, tj, w in hot:
    y1 = 362 if ti == 'a' else 410; y2 = 362 if tj == 'a' else 410
    mx = (xs[i] + xs[j]) / 2; my = min(y1, y2) - 34 if y1 == y2 == 362 else (max(y1, y2) + 34 if y1 == y2 else (y1 + y2) / 2)
    dg += P(f'M{xs[i]},{y1} Q{mx},{my} {xs[j]},{y2}', ACC, w, extra='stroke-linecap="round" stroke-opacity=".9"')
for i, x in enumerate(xs):
    act = 5 <= i <= 9
    dg += C(x, 362, 6.5, '#009CBD' if act else '#BCE2E8') + C(x, 410, 6.5, '#5F6B73' if act else '#C9C4BD')
dg += T(36, 366, 'attn', 12, 400, MUT, 'end') + T(36, 414, 'MLP', 12, 400, MUT, 'end') + T(xs[7], 448, 'the edit rewired blocks around layer 7', 13.5, 600, '#C45200', 'middle')
dg += T(xs[0], 448, 'layer 0', 12, 400, MUT, 'middle') + T(xs[15], 448, 'layer L', 12, 400, MUT, 'middle')
g += F(1, dg)
res = T(700, 60, 'Check only 20 of 100 edits. Bad edits found:', 15, 600, MUT)
for k, (who, n_, col) in enumerate([('at random', 11, '#ACA39A'), ('by editor and model', 14, '#ACA39A'), ('by the delta graph', 17, ACC)]):
    y = 84 + k * 62
    res += T(700, y + 16, who, 16, 600 if col == ACC else 400, INK) + R(700, y + 24, n_ * 22, 22, col, 'none', 0, 2) + T(710 + n_ * 22, y + 41, str(n_), 17, 600, INK)
res += T(700, 300, 'Top 20% by risk: 86% truly fail.', 18, 600, INK) + T(700, 326, 'The other 80%: 49%.', 16, 400, MUT)
res += T(700, 380, 'The exam saw no change.', 20, 600, INK) + T(700, 410, 'The graph saw the rewiring.', 20, 600, '#C45200')
g += F(2, res)
DELTA_T = sec('Our delta graph: rank edits by how the inside rewired', SVG(g), ch='0', status='pub',
              ref='Benbrahim, Goghrod, Rashme, Ji, Fu, Zhang, Chen. Delta-Graph Signatures, SDM 2026, Figure 1.1 (b). Node link drawing is our rendering of the same difference',
              notes='A real edit from the paper. Record every attention and MLP block on 12 probe prompts before and after the edit, connect blocks that move together, subtract. The edit passed every exam, yet the difference shows a knot of new connections around layer 7. Below, the same difference drawn as a graph. Rank edits by that picture: with the same budget of 20 checks, the delta graph finds 17 bad edits, the editor and model alone 14, random 11. Part 1 explains how the graph is built.')

# ---- trailer: music is steered with vectors too ----
def _si_dir(x):
    return C(x + 60, 150, 5, MU) + P(f'M{x+60},150 L{x+200},112', MU, 2.5, extra='marker-end="url(#mstt)" stroke-linecap="round"') + T(x + 206, 108, '+ jazz', 12, 400, MUT)

def _si_heads(x):
    o = ''
    for i in range(7):
        hx = x + 40 + i * 28; on = i in (2, 5)
        o += R(hx, 128, 20, 20, MU if on else '#fff', 'none', 0, 2) + (P(f'M{hx+10},124 L{hx+10},108', MU, 2, extra='marker-end="url(#mstt)"') if on else '')
    return o

def _si_concept(x):
    import random as _rr
    r = _rr.Random(7); o = ''
    for _ in range(9):
        o += C(x + 60 + r.gauss(0, 10), 145 + r.gauss(0, 7), 3.2, '#ACA39A')
        o += C(x + 190 + r.gauss(0, 10), 118 + r.gauss(0, 7), 3.2, MU)
    return o + P(f'M{x+76},140 L{x+172},122', AC2, 2, extra='marker-end="url(#msta)" stroke-dasharray="5 3"')

def _si_feature(x):
    o = ''
    hs = [10, 18, 8, 14, 6, 12, 9, 16, 7]
    for i, h in enumerate(hs):
        bx = x + 40 + i * 20; hh = 44 if i == 4 else h
        o += R(bx, 160 - hh, 13, hh, MU if i == 4 else '#C9C4BD', 'none', 0, 1)
    return o + P(f'M{x+126},112 L{x+126},100', MU, 2, extra='marker-end="url(#mstt)"')

STEER_ICON = [_si_dir, _si_heads, _si_concept, _si_feature]

g = adefs('mst')
g += T(30, 26, 'How people steer MusicGen today', 16, 600, MUT)
cards = [('Add a direction', 'genre or instrument', 'activation steering', 'Facchiano et al. 2025'),
         ('Nudge attention heads', 'chosen by a probe', 'inference time intervention', 'SMITIN, Koo et al. 2025'),
         ('Learn a concept direction', 'then push along it', 'recursive feature machines', 'Zhao et al., ICLR 2026'),
         ('Turn up one feature', 'from a sparse dictionary', 'sparse autoencoders', 'Singh, Cherep, Maes, ICLR 2026')]
for k, (a1, a2, kind, cite) in enumerate(cards):
    x = 30 + k * 283
    blk = R(x, 42, 265, 170, SOFT, 'none', 0, 3)
    blk += STEER_ICON[k](x)
    blk += T(x + 22, 76, a1, 18, 600, INK) + T(x + 22, 98, a2, 14, 400, MUT) + T(x + 22, 178, kind, 14, 600, MU) + T(x + 22, 198, cite, 12.5, 400, MUT)
    g += blk
# ours, one way
o = R(30, 236, 1120, 186, '#EEE8F6', 'none', 0, 3) + T(52, 266, 'Ours, under review: for the styles we tested, the same kind of vector works only one way', 17, 600, INK)
o += R(60, 290, 200, 46, '#fff', 'none', 0, 3) + T(160, 319, 'a jazz clip', 16, 600, MU, 'middle') + P('M262,313 L420,313', ACC, 2.5, extra='marker-end="url(#msto)"') + T(341, 303, 'minus jazz', 13, 400, MUT, 'middle')
o += R(424, 290, 210, 46, '#fff', 'none', 0, 3) + T(529, 319, 'not jazz any more', 16, 600, INK, 'middle') + T(660, 320, 'leaving: easy', 16, 600, '#C45200')
o += R(60, 346, 200, 46, '#fff', 'none', 0, 3) + T(160, 375, 'a classical clip', 16, 600, INK, 'middle') + P('M262,369 L420,369', AC2, 2, extra='marker-end="url(#msta)" stroke-dasharray="6 4"') + T(341, 359, 'plus jazz', 13, 400, MUT, 'middle')
o += R(424, 346, 210, 46, '#FBE1DE', 'none', 0, 3) + T(529, 375, 'still not jazz', 16, 600, '#DA291C', 'middle') + T(660, 376, 'entering: hard', 16, 600, '#DA291C')
isl = '<ellipse cx="960" cy="318" rx="52" ry="32" fill="#DCD1EB"/>' + T(960, 323, 'jazz', 15, 600, MU, 'middle')
import math as _mm
for k in range(7):
    a = -_mm.pi * 0.85 + k * _mm.pi * 1.7 / 6
    x1, y1 = 960 + 52 * _mm.cos(a), 318 + 32 * _mm.sin(a); x2, y2 = 960 + 96 * _mm.cos(a), 318 + 56 * _mm.sin(a)
    isl += P(f'M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}', AC2, 1.5, extra='marker-end="url(#msta)"')
isl += P('M1100,266 Q1060,282 1010,298', '#DA291C', 1.5, extra='stroke-dasharray="4 4" marker-end="url(#msta)"') + T(1144, 256, 'rare way in', 12, 600, '#DA291C', 'end')
isl += T(960, 398, 'a graph view: many ways out, few ways in', 13, 600, INK, 'middle') + T(960, 414, 'our hypothesis, being tested', 12.5, 400, MUT, 'middle')
o += isl
g += F(1, o)
g += F(2, T(590, 452, 'A vector says what we pushed. It cannot say why the push lands only one way.', 19, 700, INK, 'middle'))
MSTEER = sec('Yet music generators are steered with vectors too', SVG(g), ch='0',
             ref='Facchiano et al., arXiv 2504.04479, 2025. Narashiman et al., arXiv 2506.10225, 2025. Koo et al., SMITIN, 2025. Zhao et al., ICLR 2026. Singh, Cherep, Maes, ICLR 2026. Co-authored work under review, MusicGen. Jazz and classical illustrate the two arms',
             notes='The music twin of the vector slide. The tiny graph just showed that a style has structure. Yet the way people steer MusicGen today is a direction or a feature added inside the model. Our own finding, still under review: removing a style with such a vector works, adding one does not. A vector cannot explain that. A graph can, if a style is an island with many ways out and few ways in. That picture is our hypothesis, and testing it is part of Part 2.')

# ---- trailer: knowledge is a graph, an edit must follow it ----
g = adefs('kgt')
def kn2(x, y, lab, col='#009CBD', up=True, fill=None):
    return C(x, y, 9, fill or col) + T(x, y - 18 if up else y + 30, lab, 16, 600, INK, 'middle')
def ke(x1, y1, x2, y2, lab, col=AC2, sw=1.6, dash='', m='kgta', lx=0, ly=-8):
    import math as _m
    d = _m.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    o = P(f'M{x1+ux*12:.1f},{y1+uy*12:.1f} L{x2-ux*13:.1f},{y2-uy*13:.1f}', col, sw, extra=f'marker-end="url(#{m})" ' + (f'stroke-dasharray="{dash}"' if dash else ''))
    return o + (T((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, lab, 12.5, 400, MUT, 'middle') if lab else '')
SN, SE, WA, US = (90, 170), (300, 170), (520, 170), (740, 170)
WF, OL, DO = (90, 64), (520, 64), (740, 276)
ET, PA, FR, EU = (300, 380), (520, 380), (740, 380), (740, 460)
base = ke(*SN, *SE, 'located in') + ke(*SE, *WA, 'city in') + ke(*WA, *US, 'state of') + ke(*SN, *WF, 'built for', lx=34, ly=4) + ke(*WA, *OL, 'capital', lx=-32, ly=4) + ke(*US, *DO, 'currency', lx=-36, ly=4)
base += ke(*ET, *PA, 'located in', col='#ACA39A') + ke(*PA, *FR, 'city in', col='#ACA39A') + ke(*FR, *EU, '', col='#ACA39A') + T(770, 444, 'currency', 12.5, 400, MUT)
base += kn2(*SN, 'Space Needle') + kn2(*SE, 'Seattle') + kn2(*WA, 'Washington State', up=False) + kn2(*US, 'United States') + kn2(*WF, "1962 World's Fair") + kn2(*OL, 'Olympia') + kn2(*DO, 'dollar', up=False)
base += kn2(*ET, 'Eiffel Tower', '#ACA39A') + kn2(*PA, 'Paris', '#ACA39A') + kn2(*FR, 'France', '#ACA39A') + C(*EU, 9, '#ACA39A') + T(EU[0] - 18, EU[1] + 5, 'euro', 16, 600, INK, 'end')
intro = (f'<foreignObject x="860" y="52" width="290" height="330"><div xmlns="http://www.w3.org/1999/xhtml" style="width:290px;height:330px;overflow:hidden;border-radius:3px;background:#F1EDE7">'
         f'<img src="figs/space-needle.jpg" alt="The Space Needle in Seattle" style="width:290px;height:330px;object-fit:cover;max-width:none;max-height:none;margin:0;border:0;box-shadow:none"/></div></foreignObject>')
intro += R(860, 318, 290, 64, '#FBFAF7', 'none', 0, 0, 'fill-opacity=".9"')
intro += T(876, 342, 'The Space Needle, Seattle', 17, 600, INK) + T(876, 364, "built for the 1962 World's Fair, 184 m tall", 13.5, 400, MUT)
g += intro
g += F(1, base + T(30, 470, 'What the model knows, drawn as a knowledge graph', 16, 600, MUT))
ed = ke(*SN, PA[0], PA[1], '', col=ACC, sw=2.8, m='kgto') + T(250, 290, 'the edit:', 14, 600, '#C45200', 'end') + T(250, 310, 'located in Paris', 14, 600, '#C45200', 'end')
ed += P(f'M{SN[0]+10},{SN[1]} L{SE[0]-12},{SE[1]}', '#DA291C', 2.2, extra='stroke-dasharray="2 5" stroke-linecap="round"')
g += F(2, ed)
q = R(860, 52, 290, 330, SOFT, 'none', 0, 3) + T(880, 82, 'Ask one step further', 15, 600, MUT)
for k, (qq, said, should) in enumerate([('Which country is it in?', 'United States', 'France'), ('Which state is it in?', 'Washington', 'none: Paris has no state'), ('What currency is used there?', 'dollar', 'euro')]):
    y = 112 + k * 92
    q += T(880, y, qq, 16, 600, INK) + T(880, y + 24, 'edited model: ' + said, 14.5, 600, '#DA291C') + T(880, y + 46, 'should be: ' + should, 14.5, 400, MUT)
g += F(3, q)
g += F(4, T(1005, 430, 'Change one edge, and every', 17, 600, INK, 'middle') + T(1005, 454, 'path through it must change.', 17, 600, INK, 'middle'))
KGT = sec('Knowledge is a graph, and an edit has to follow it', SVG(g), ch='0',
          ref='Cohen et al., Evaluating the Ripple Effects of Knowledge Editing in Language Models, TACL 2024. Zhong et al., MQuAKE, EMNLP 2023. Space Needle answers are an illustration of the failure type',
          notes='Open on the photo: a landmark everyone knows, in Seattle, built for the 1962 World\'s Fair. Click: this is what a model knows about it, drawn as a knowledge graph. Facts link to other facts. The Space Needle is in Seattle, Seattle is in Washington, Washington is in the United States. Suppose an editor moves the Space Needle to Paris and changes only that one edge. Now every question one step further is wrong: the model still says United States, still says Washington, still says dollar. This is the ripple effect, measured by RippleEdits and MQuAKE. The knowledge has a graph. The question for the talk: does the model have one inside?')

# ---- Part 1 opener: multi-hop questions fall off a cliff, and the graph says why (our CIKM 2026 paper) ----
g = adefs('cgt')
g += T(30, 26, 'A clinical record, drawn as a knowledge graph', 16, 600, MUT)
PT, AD, AL, SY = (80, 150), (290, 150), (480, 90), (480, 230)
g += P(f'M{PT[0]+12},{PT[1]} L{AD[0]-13},{AD[1]}', AC2, 1.8, extra='marker-end="url(#cgta)"') + T(185, 140, 'admitted', 13, 400, MUT, 'middle')
g += P(f'M{AD[0]+11},{AD[1]-6} L{SY[0]-12},{SY[1]-4}', AC2, 1.8, extra='marker-end="url(#cgta)"') + T(366, 222, 'symptom', 13, 400, MUT, 'middle')
g += P(f'M{AD[0]+11},{AD[1]-6} L{AL[0]-12},{AL[1]+4}', '#DA291C', 1.8, extra='stroke-dasharray="5 5"') + T(352, 70, 'allergy edge', 13, 400, '#DA291C', 'middle') + T(352, 86, 'never recorded', 13, 400, '#DA291C', 'middle')
for (x, y), lab in ((PT, 'Patient'), (AD, 'Admission'), (AL, 'Allergy'), (SY, 'chest pain')):
    g += C(x, y, 9, '#009CBD') + T(x, y + 30, lab, 16, 600, INK, 'middle')
g += T(30, 300, '1 hop: why was this patient admitted?', 15.5, 600, INK) + T(30, 324, '2 hops: what allergy does the patient admitted', 15.5, 600, INK) + T(30, 346, 'for chest pain have?', 15.5, 600, INK)
g += T(30, 386, 'Our test: does the question map into the record?', 16, 600, '#C45200') + T(30, 410, 'No path in the graph, no correct answer, for any model.', 16, 600, '#C45200')
# slope chart, MIMIC-III exact match, 9 models
X1, X2, Y0, YS = 680, 940, 400, 4.0
H = [('Kimi-K2.5', 76.7, 9.1), ('GPT-OSS-120B', 76.0, 6.0), ('DeepSeek-V4-Pro', 76.0, 7.0), ('GLM-5.1', 76.0, 9.0), ('Gemma4-31B', 76.0, 6.0),
     ('Nemotron-3-Super', 76.0, 8.0), ('Qwen3.5', 59.0, 7.0), ('Llama3.2-3B', 76.0, 12.0), ('Mistral-7B', 75.0, 12.0)]
ch = T(600, 26, 'Exact match on MIMIC-III, 9 models from 3B to 1.6T parameters', 15, 600, MUT)
ch += L(X1, 70, X1, Y0, '#D7D2CB', 1) + L(X2, 70, X2, Y0, '#D7D2CB', 1) + T(X1, Y0 + 24, '1 hop', 15, 600, INK, 'middle') + T(X2, Y0 + 24, '2 hops', 15, 600, INK, 'middle')
for name, a, b in H:
    ch += P(f'M{X1},{Y0 - a * YS:.1f} L{X2},{Y0 - b * YS:.1f}', '#7C878E', 1.6, extra='stroke-opacity=".75"') + C(X1, round(Y0 - a * YS, 1), 4, '#5F5D50') + C(X2, round(Y0 - b * YS, 1), 4, '#5F5D50')
ch += T(X1 - 14, Y0 - 76 * YS + 5, 'about 76%', 16, 600, INK, 'end') + T(X1 - 14, Y0 - 59 * YS + 5, '59%', 14, 400, MUT, 'end')
ch += T(X2 + 14, Y0 - 9 * YS + 5, '6 to 12%', 16, 600, INK) + T(860, 118, 'a cliff of', 16, 600, '#C45200', 'middle') + T(860, 138, 'about 50 to 70 points', 16, 600, '#C45200', 'middle')
g += F(1, ch)
rep = R(1000, 86, 180, 262, SOFT, 'none', 0, 3) + T(1016, 114, 'The graph splits', 15, 600, INK) + T(1016, 134, 'the failures', 15, 600, INK)
rep += T(1016, 170, 'missing edges:', 14, 600, '#C45200') + T(1016, 190, 'fix the graph. On', 14, 400, INK) + T(1016, 210, 'CORAL, 51 edges cut', 14, 400, INK) + T(1016, 230, 'misses 8.2% to 0%', 14, 600, INK)
rep += T(1016, 270, 'On MIMIC-III only 1.3%', 14, 600, INK) + T(1016, 290, 'of 2 hop questions have', 14, 400, INK) + T(1016, 310, 'no path: the cliff is', 14, 400, INK) + T(1016, 330, 'the models\' reasoning', 14, 400, INK)
g += F(2, rep)
g += F(3, T(590, 466, 'A graph tells which questions cannot be answered, before any model tries.', 19, 700, INK, 'middle'))
CGT = sec('Two hops break every model. The graph says why', SVG(g), ch='1', status='acc',
          ref='Ours, Diagnosing Multi-Hop KG Question Answering Failures: A Typed Homomorphism Framework with Clinical Repair, CIKM 2026, Table 4 and Table 6. MIMIC-III, CORAL from PhysioNet',
          notes='Our CIKM 2026 paper, the knowledge graph from the opening made concrete. On clinical records kept behind a data use agreement, seven of nine models reach about 76 percent at one hop and fall to 6 to 12 percent at two hops, from 3B up to a 1.6T mixture of experts. Part of that cliff is not the model at all: if the record never stored the edge, no model can answer. The paper turns that into a theorem and a test that runs before retrieval. On CORAL, adding 51 missing edges removes every structural miss, 8.2 percent to zero. What remains is the model reasoning gap. On MIMIC-III, only 3 of 239 two hop questions (1.3 percent) have no path, so almost all of that cliff is the models reasoning, not the record.')

# ---- backup under the CIKM slide: the four classes ----
g = T(40, 40, 'The "no path" side of slide 9, checked in this order. Each question gets exactly one label.', 14, 600, MUT)
cls4 = [('1', 'Out of scope', 'more hops than the graph is certified for', 'no change to the graph, the workload asks too much'),
        ('2', 'Entity failure', 'a needed entity type has no instances at all', 'fix how the graph is populated'),
        ('3', 'Relation failure', 'a needed relation type is not in the schema', 'fix the schema'),
        ('4', 'Composition failure', 'types exist, but this patient\'s path is missing', 'repair that edge')]
for k, (n_, name, why, fix) in enumerate(cls4):
    y = 64 + k * 74
    g += R(40, y, 1100, 62, SOFT, 'none', 0, 6) + T(70, y + 38, n_, 22, 700, '#C45200', 'middle') + T(100, y + 27, name, 17, 700, INK) + T(100, y + 49, why, 14.5, 400, INK) + T(1120, y + 38, fix, 14.5, 600, '#C45200', 'end')
g += T(590, 392, 'None of the four applies: a path exists, so a wrong answer is the model\'s own reasoning.', 17, 700, INK, 'middle')
g += T(590, 420, 'Typed homomorphism: read the question as a small typed graph. It must map into the record, types and edges preserved.', 14.5, 400, MUT, 'middle')
g += T(590, 446, 'MIMIC-III: 3 of 239 two hop questions land in the four classes. CORAL: 8.2%, and repairing 51 edges brings it to 0%.', 14.5, 400, MUT, 'middle')
CGT4 = sec('Four ways a question can be impossible before any model tries', SVG(g), ch='1', status='acc',
           ref='Ours, CIKM 2026, Definition 8 (priority ordered failure classes), Theorem 1 and Table 6',
           notes='Only if asked. The four classes refine the missing edge box on slide 9. The order matters: each question gets the first label that applies. Entity and relation failures are design errors in the graph, composition failure is a documentation gap fixed by adding the edge, out of scope means the questions ask for more hops than we can certify, so nothing in the graph changes.')

# ---- forecast, two claims ----
g = adefs('fc2')
g += T(590, 60, THROUGH_A, 32, 700, INK, 'middle') + T(590, 104, THROUGH_B, 32, 700, ACC, 'middle')
for k, (a, st, kk, col) in enumerate(CLAIMS):
    y = 140 + k * 100
    g += F(k + 1, C(80, y + 30, 24, col) + T(80, y + 38, str(k + 1), 20, 700, '#fff', 'middle') + wrap(122, y + 24, a, 19, 600, INK, width=80, lh=26) + tag(122, y + 64, st, kk))
mods = [('Text', 'today, Part 1', ACC, ACL, True), ('Music', 'today, Part 2', MU, MUL, True), ('Equations', 'proofs, physics', '#5a4fcf', '#fff', False),
        ('Code', 'programs', AC2, '#fff', False), ('Images', 'vision', AC2, '#fff', False), ('Space', '3D, maps', AC2, '#fff', False),
        ('Motion', 'bodies, robots', AC2, '#fff', False), ('Molecules', 'proteins, DNA', AC2, '#fff', False)]
strip = T(30, 360, 'Kinds of knowledge a generative model holds', 14, 700, MUT)
for k, (a, b, col, fill, solid) in enumerate(mods):
    x = 30 + k * 141
    strip += R(x, 372, 130, 62, fill, col, 2 if solid else 1.5, 12, '' if solid else 'stroke-dasharray="6 5" opacity=".75"')
    strip += T(x + 65, 399, a, 16, 700, col, 'middle', '' if solid else 'opacity=".8"') + T(x + 65, 420, b, 12, 400, INK if solid else MUT, 'middle')
g += F(3, strip + T(590, 462, 'Two kinds today. Many more, and none is a substitute for another.', 17, 700, INK, 'middle'))
g += T(590, 136, 'A graph inside a model: nodes are its parts or states, edges are how they move together or follow each other.', 15, 600, MUT, 'middle')
g += F(1, T(840, 166, 'nodes: parts of the network', 15, 600, '#C45200') + T(840, 188, 'edges: parts that fire together', 15, 600, '#C45200'))
g += F(2, T(840, 266, 'nodes: notes, or states of a generator', 15, 600, MU) + T(840, 288, 'edges: what follows what', 15, 600, MU))
FORECAST2 = sec('Two claims for the rest of this talk', SVG(g), ch='0',
                notes='The dashed tiles are the point of the vision: knowledge comes in many forms, and text is only one of them. Today covers text and music. Language is published and the result is solid. Music is in progress: the data side has numbers, the generator side is being tested, and the brain is the judge.')

# ---- part dividers, plain ----
def divider(title, line, ch):
    g = T(590, 170, THROUGH_A, 30, 700, INK, 'middle') + T(590, 215, THROUGH_B, 30, 700, ACC, 'middle') + T(590, 300, line, 22, 600, AC2, 'middle')
    return sec(title, SVG(g, 420), ch=ch, cls='divider')
DIV1 = divider('Part 1. Language models', 'First, the graph outside the model. Then, the graph inside.', '1')
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

# ---- last slide: the kinds of knowledge this talk did not cover ----
def _gi(kind, x, y, col):
    """tiny graph that each kind of knowledge already carries"""
    o = ''
    def n(px, py, r=4.5, f='#fff'): return C(px, py, r, f, col, 1.4)
    if kind == 'eq':      # proof steps depend on earlier steps
        P_ = [(x, y - 26), (x - 22, y - 4), (x + 22, y - 4), (x, y + 22)]
        for a_, b_ in ((0, 1), (0, 2), (1, 3), (2, 3)): o += L(*P_[a_], *P_[b_], col, 1.2)
        o += ''.join(n(*q) for q in P_[:3]) + n(*P_[3], 5.5, col)
    elif kind == 'code':  # functions call functions
        P_ = [(x - 24, y - 20), (x + 24, y - 20), (x, y + 2), (x - 24, y + 24), (x + 24, y + 24)]
        for a_, b_ in ((0, 2), (1, 2), (2, 3), (2, 4), (0, 3)): o += L(*P_[a_], *P_[b_], col, 1.2)
        o += ''.join(P(f'M{qx-7},{qy-5} h14 v10 h-14 Z', col, 1.4, '#F1EDE7') for qx, qy in P_)
    elif kind == 'img':   # objects relate in a scene
        P_ = [(x - 26, y + 14), (x, y - 20), (x + 26, y + 14)]
        for a_, b_ in ((0, 1), (1, 2), (0, 2)): o += L(*P_[a_], *P_[b_], col, 1.2)
        o += P(f'M{P_[1][0]-8},{P_[1][1]-8} h16 v16 h-16 Z', col, 1.4, '#F1EDE7') + n(*P_[0], 6) + P(f'M{P_[2][0]-7},{P_[2][1]+6} L{P_[2][0]},{P_[2][1]-7} L{P_[2][0]+7},{P_[2][1]+6} Z', col, 1.4, '#fff')
    elif kind == 'space': # places connect into maps
        for i in range(3):
            for j in range(3):
                px, py = x - 24 + i * 24, y - 22 + j * 22
                if i < 2 and not (i == 1 and j == 0): o += L(px, py, px + 24, py, col, 1.2)
                if j < 2 and not (i == 2 and j == 1): o += L(px, py, px, py + 22, col, 1.2)
        o += ''.join(n(x - 24 + i * 24, y - 22 + j * 22, 3.6) for i in range(3) for j in range(3))
    elif kind == 'motion':  # joints chain into a skeleton
        J = {'h': (x, y - 28), 'n': (x, y - 14), 'p': (x, y + 8), 'la': (x - 18, y), 'ra': (x + 18, y - 6), 'll': (x - 12, y + 28), 'rl': (x + 14, y + 28)}
        for a_, b_ in (('h', 'n'), ('n', 'p'), ('n', 'la'), ('n', 'ra'), ('p', 'll'), ('p', 'rl')): o += L(*J[a_], *J[b_], col, 1.2)
        o += ''.join(n(*q, 3.8) for q in J.values())
    elif kind == 'mol':   # atoms bond into a molecule
        import math as _m
        H = [(x + 20 * _m.cos(_m.pi / 6 + k * _m.pi / 3), y + 20 * _m.sin(_m.pi / 6 + k * _m.pi / 3)) for k in range(6)]
        for k in range(6): o += L(*H[k], *H[(k + 1) % 6], col, 1.2)
        o += L(H[0][0] + 1, H[0][1], H[0][0] + 16, H[0][1] + 9, col, 1.2) + n(H[0][0] + 18, H[0][1] + 10, 4)
        o += ''.join(n(*q, 3.8) for q in H)
    return o

g = adefs('tk2')
g += T(40, 30, 'Covered today', 15, 600, MUT)
g += R(40, 44, 360, 52, '#FDEBDD', 'none', 0, 3) + T(58, 76, 'Text', 19, 600, '#C45200') + T(118, 76, 'Part 1: facts inside a language model', 13.5, 400, INK)
g += R(416, 44, 360, 52, '#EEE8F6', 'none', 0, 3) + T(434, 76, 'Music', 19, 600, MU) + T(512, 76, 'Part 2: style, expectation, the brain', 13.5, 400, INK)
g += T(40, 140, 'Not covered, and each already carries a graph', 15, 600, MUT)
KINDS = [('eq', 'Equations', 'each step rests on earlier ones'), ('code', 'Code', 'functions call other functions'),
         ('img', 'Images', 'objects relate in a scene'), ('space', 'Space', 'places connect into a map'),
         ('motion', 'Motion', 'joints chain into a skeleton'), ('mol', 'Molecules', 'atoms bond into a molecule')]
for k, (kind, name, line) in enumerate(KINDS):
    cx, cy = 40 + (k % 3) * 372, 156 + (k // 3) * 150
    g += R(cx, cy, 356, 134, SOFT, 'none', 0, 3) + _gi(kind, cx + 62, cy + 67, AC2)
    g += T(cx + 124, cy + 58, name, 21, 600, INK) + T(cx + 124, cy + 86, line, 14, 400, MUT)
TAKEAWAY = sec('Language and music are two of many places a graph may hide', SVG(g), ch='4',
               notes='One sentence before the map, no more: in language the graph inside is published and ranks risky edits, it does not repair them, in music it is in progress and the judge is planned. Then the map. No conclusion slide, just the map of what is left. Text and music were today. Equations, code, images, space, motion and molecules each already have a natural graph, and each has its own generative models. Every one of these is a place where the same question can be asked, and where someone in this department may already have the data or the expertise.')

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

# ======================= ROUND 5 (Nov 2 2026): music part rebuilt from the survey =======================
import json as _json, os as _os
CLIPS = _json.load(open(_os.path.join(_os.path.dirname(__file__), 'clips.json')))  # includes experiments/music-markov clips

def playbtn(x, y, w, clip, label, col):
    au = f' data-audio="figs/audio/{clip}.mp3"' if _os.path.exists(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), 'figs', 'audio', clip + '.mp3')) else ''
    return (f'<foreignObject x="{x}" y="{y}" width="{w}" height="44"><div xmlns="http://www.w3.org/1999/xhtml">'
            f'<button class="playclip" data-clip="{clip}"{au} style="width:{w}px;height:40px;border-radius:20px;border:2px solid {col};background:#fff;color:{col};font:700 15px Fira Sans,sans-serif;cursor:pointer">&#9654; {label}</button></div></foreignObject>')

CLIP_JSON = '<script type="application/json" id="clipdata">' + _json.dumps(CLIPS) + '</script>'


def _arc(x1, y1, x2, y2, col, bend=14, m='h1a', sw=1.5, extra=''):
    import math
    dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    sx, sy, ex, ey = x1 + ux * 10, y1 + uy * 10, x2 - ux * 11, y2 - uy * 11
    mx, my = (sx + ex) / 2 - uy * bend, (sy + ey) / 2 + ux * bend
    return P(f'M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}', col, sw, extra=f'marker-end="url(#{m})" ' + extra)

def _nd(x, y, lab, col, fill='#fff', r=9):
    return C(x, y, r, fill, col, 1.5) + T(x, y + 4, lab, 11, 600, col if fill == '#fff' else '#fff', 'middle')

def icon_chain(x, col):
    """1957: one chain, the next note depends only on this note"""
    A, B, Cc = (x - 50, 160), (x, 102), (x + 50, 160)
    o = _arc(*A, *B, col) + _arc(*B, *Cc, col) + _arc(*Cc, *A, col) + _arc(*B, *A, col) + _arc(*Cc, *B, col)
    o += P(f'M{x+58},{152} C{x+86},{132} {x+86},{186} {x+59},{167}', col, 1.5, extra='marker-end="url(#h1a)"')
    o += _nd(*A, 'C', col) + _nd(*B, 'E', col) + _nd(*Cc, 'G', col)
    return o, 'one chain over notes'

def icon_views(x, col):
    """1995: several small chains, one per view of the music, vote on the next note"""
    o = ''
    for j, lab in enumerate(['pitch', 'rhythm', 'interval']):
        y = 104 + j * 30
        o += T(x - 70, y + 4, lab, 11.5, 400, MUT, 'end')
        for i in range(3):
            o += C(x - 58 + i * 26, y, 5, '#fff', col, 1.5)
            if i < 2: o += L(x - 52 + i * 26, y, x - 38 + i * 26, y, col, 1.2)
        o += P(f'M{x+10},{y} L{x+44},{134}', col, 1.2, extra='stroke-opacity=".7"')
    o += C(x + 56, 134, 10, col, 'none') + T(x + 56, 138, '?', 12, 600, '#fff', 'middle')
    return o, 'three chains vote on the next note'

def icon_tree(x, col):
    """2003: a context tree, deeper branches remember more of the phrase"""
    root = (x - 62, 140); l1 = [(x - 20, 112), (x - 20, 168)]; l2 = [(x + 22, 96), (x + 22, 128), (x + 22, 158)]; l3 = [(x + 62, 116)]
    o = ''.join(L(*root, *p_, col, 1.2) for p_ in l1)
    o += L(*l1[0], *l2[0], col, 1.2) + L(*l1[0], *l2[1], col, 1.2) + L(*l1[1], *l2[2], col, 1.2)
    o += P(f'M{root[0]},{root[1]} L{l1[0][0]},{l1[0][1]} L{l2[1][0]},{l2[1][1]} L{l3[0][0]},{l3[0][1]}', col, 3, extra='stroke-linecap="round" stroke-linejoin="round"')
    o += ''.join(C(*p_, 5, '#fff', col, 1.5) for p_ in [root] + l1 + l2) + C(*l3[0], 6, col, 'none')
    return o, 'longest matching context continues'

def icon_expect(x, col):
    """2005 on: from this note, each possible next note gets a probability, a rare one is a surprise"""
    E = (x - 58, 140)
    o = ''
    for (y, lab, w, bar) in ((106, 'C', 3.2, 52), (140, 'G', 1.8, 30), (174, 'B', 0.8, 10)):
        o += _arc(*E, x - 4, y, col, bend=0, m='h1t', sw=w)
        o += _nd(x + 6, y, lab, col)
        o += R(x + 22, y - 5, bar, 10, col, 'none', 0, 2, f'fill-opacity="{0.4 + bar / 90:.2f}"')
    o += _nd(*E, 'E', col, col)
    o += T(x + 40, 178, 'surprise', 12, 600, ACC, 'start')
    return o, 'probability of each next note'

HICON = [icon_chain, icon_views, icon_tree, icon_expect]

# ---- M1: the oldest music model is a graph ----
g = adefs('h1')
g += L(60, 250, 1120, 250, LINE, 3)
hist = [('1957', 'Hiller and Isaacson', 'A Markov chain writes a movement', 'of a string quartet, the Illiac Suite.', AC2),
        ('1995', 'Conklin and Witten', 'Several small chains predict Bach', 'better than one big chain.', AC2),
        ('2003', 'Pachet, Continuator', 'A variable order chain improvises', 'back in the player\'s own style.', AC2),
        ('2005 on', 'Pearce, IDyOM', 'The same kind of graph predicts', 'what listeners expect next.', MU)]
for k, (yr, who, a, b, col) in enumerate(hist):
    x = 160 + k * 285
    blk = C(x, 250, 11, col) + T(x, 222, yr, 22, 700, col, 'middle') + R(x - 130, 280, 260, 130, '#fff', col, 1.5, 10)
    blk += T(x, 312, who, 16, 700, INK, 'middle') + T(x, 344, a, 14, 400, INK, 'middle') + T(x, 366, b, 14, 400, INK, 'middle')
    ic, cap = HICON[k](x, col)
    blk += f'<g transform="translate({x},124) scale(1.4) translate({-x},-140)">{ic}</g>' + T(x, 198, cap, 13, 400, MUT, 'middle')
    g += F(k, blk) if k else blk
g += F(4, T(590, 462, 'In music the graph is not a metaphor. It was the first generator.', 20, 700, INK, 'middle'))
HIST = sec('Part 2. The oldest music model is a graph', SVG(g), ch='2', cls='divider',
           ref='Hiller and Isaacson, Experimental Music, 1959. Conklin and Witten, JNMR 1995. Pachet, The Continuator, JNMR 2003. Pearce, IDyOM, 2005 and 2018',
           notes='Four stops, one sentence each. The point: music had explicit graphs long before neural generators. The last card, IDyOM, comes back in the brain section: the same kind of graph predicts what listeners expect.')

# ---- M2: fold 88 keys into 12 degrees ----
g = adefs('fd')
wk = 14
for k in range(wk):
    x = 40 + k * 34
    g += R(x, 60, 32, 120, '#fff', '#9aa6ae', 1.2, 3)
blk_pos = [0, 1, 3, 4, 5, 7, 8, 10, 11, 12]
for k in blk_pos:
    x = 40 + k * 34 + 22
    g += R(x, 60, 22, 74, INK, 'none', 0, 2)
g += T(278, 44, 'a piano: 88 keys, the same 12 notes repeating', 15, 700, INK, 'middle')
g += T(278, 205, 'E4 and E5 are the same note an octave apart', 14, 400, MUT, 'middle')
cx, cy, r = 278, 345, 95
names = ['0 tonic', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
ring = ''
for d_ in range(12):
    a = -math.pi / 2 + d_ * 2 * math.pi / 12
    x, y = cx + r * math.cos(a), cy + r * math.sin(a)
    ring += C(round(x), round(y), 15 if d_ else 19, ACC if d_ == 0 else '#fff', ACC, 2.5) + T(round(x), round(y) + 5, str(d_), 13, 700, '#fff' if d_ == 0 else ACC, 'middle')
ring += P('M278,212 L278,224', ACC, 2.5, extra='marker-end="url(#fdo)"') + T(420, 250, 'fold every octave together,', 14, 700, ACC) + T(420, 270, 'count from the piece\'s own key', 14, 700, ACC) + T(cx, 470, '12 scale degrees: 0 is the home note', 14, 700, ACC, 'middle')
g += F(1, ring)
fe = {(0, 2): 2, (0, 3): 2, (0, 7): 1, (2, 0): 1, (2, 3): 1, (2, 5): 2, (2, 7): 2, (3, 0): 2, (3, 2): 1, (3, 7): 3, (5, 3): 2, (6, 7): 4, (7, 0): 2, (7, 2): 2, (7, 3): 1, (7, 6): 4, (7, 7): 1, (7, 11): 1, (11, 2): 1}
rs = {i_: sum(v for (a_, b_), v in fe.items() if a_ == i_) for i_ in range(12)}
tb = T(800, 44, 'Für Elise as a 12 by 12 table', 15, 700, INK, 'middle') + T(800, 64, 'row: this note, column: the next note', 13, 400, MUT, 'middle')
cs_ = 24
for a_ in range(12):
    for b_ in range(12):
        v = fe.get((a_, b_), 0) / rs[a_] if rs[a_] else 0
        tb += R(656 + b_ * cs_, 80 + a_ * cs_, cs_ - 2, cs_ - 2, f'rgba(247,105,2,{0.2 + 0.8 * v:.2f})' if v else SOFT, 'none', 0, 2)
tb += T(800, 386, '12 x 12 = 144 numbers. Rhythm and register are dropped.', 14, 700, ACC, 'middle')
g += F(2, tb)
g += F(3, playbtn(640, 410, 230, 'fe_orig', 'Für Elise, the opening', AC2) + playbtn(890, 410, 260, 'fe_graph', 'a tune drawn from the table', ACC))
FOLD = sec('Fold 88 keys into 12 scale degrees, and a melody becomes 144 numbers', SVG(g), ch='2',
           ref='Scale degrees are counted from each piece\'s key (its tonic). The overview animation used real pitches, the classifier uses these 12 degrees',
           notes='For non musicians: the 12 notes repeat across the piano, and a melody in C and the same melody in G should look the same, so we fold octaves and count from the home note of the key. Each row of the table says where the melody goes next from that note. Play the two buttons: the second tune uses only the 144 numbers. It sounds like the right material with the wrong sentences. That is the next slides.')

# ---- M5: when graphs help ----
g = adefs('gh')
g += T(300, 40, 'Helps: edges carry what a sequence throws away', 17, 700, GRN, 'middle')
segs = [('A', 40, 150, ACC), ('B', 150, 270, MU), ('A', 270, 380, ACC), ('B', 380, 500, MU), ('C', 500, 560, AC2)]
for lab, x1, x2, col in segs:
    g += R(x1, 200, x2 - x1 - 4, 40, col, 'none', 0, 4, 'opacity=".85"') + T((x1 + x2) / 2, 226, lab, 16, 700, '#fff', 'middle')
for x1, x2 in [(95, 325), (210, 440), (100, 330)]:
    g += P(f'M{x1},196 C{x1},110 {x2},110 {x2},196', INK, 2, extra='stroke-dasharray="5 4"')
g += T(300, 92, 'beats are nodes, repeated passages are linked', 13.5, 600, MUT, 'middle')
g += T(300, 270, 'verse and chorus fall out of the graph', 14, 700, INK, 'middle') + T(300, 292, 'McFee and Ellis, ISMIR 2014', 12.5, 400, MUT, 'middle')
right = T(880, 40, 'Does not help by itself', 17, 700, RED, 'middle')
rows = [('Cadence detection, Bach', 'hand features 0.80, graph net 0.73 to 0.80'), ('Composer from Tonnetz paths', 'graph 0.49 vs a random forest 0.76, style task 0.84'), ('Note networks', 'power laws and small worlds, no task solved')]
for k, (a_, b_) in enumerate(rows):
    y = 80 + k * 72
    right += R(640, y, 500, 60, SOFT, LINE, 1, 8) + T(660, y + 26, a_, 15, 700, INK) + T(660, y + 48, b_, 13.5, 400, INK)
right += T(880, 312, 'Karystinaios and Widmer 2022. Karystinaios et al. 2020. Liu, Tse, Small 2010', 12.5, 400, MUT, 'middle')
g += F(1, right)
g += F(2, R(90, 340, 1000, 80, ACL, ACC, 1.5, 10) + T(590, 372, 'A graph earns its place only when its edges carry', 20, 700, INK, 'middle') + T(590, 402, 'what the sequence or the vector throws away.', 20, 700, ACC, 'middle'))
WHEN = sec('In music, graphs help only when the edges carry new information', SVG(g), ch='2',
           ref='McFee and Ellis, Analyzing Song Structure with Spectral Clustering, ISMIR 2014. Karystinaios and Widmer, Cadence Detection using GNNs, ISMIR 2022. Karystinaios et al., Tonnetz trajectories, JIM 2020. Liu, Tse, Small, Physica A 2010',
           notes='Honest survey. The clear win is song structure: a graph linking beats that sound alike, far apart in time, cuts a song into verse and chorus, something a left to right sequence model does not see. The counterexamples: graph neural nets on scores only tie hand features, Tonnetz trajectories alone classify worse than metadata, and note networks with pretty degree distributions never solved a task.')

# ---- M6: MusicGen in plain words ----
g = adefs('mg')
g += R(40, 50, 170, 110, '#fff', AC2, 2, 8) + T(125, 74, 'sound', 16, 700, AC2, 'middle') + T(125, 150, '32,000 samples per sec', 12, 400, MUT, 'middle')
g += P('M58,110 ' + ' '.join(f'L{58 + k * 6},{110 + (16 if k % 2 else -16) * (0.4 + 0.6 * abs(math.sin(k)))}' for k in range(1, 24)), AC2, 1.5)
g += P('M212,100 L262,100', AC2, 2.5, extra='marker-end="url(#mga)"') + T(237, 88, 'EnCodec', 12, 700, AC2, 'middle')
for r_ in range(4):
    for c_ in range(8):
        g += R(272 + c_ * 30 + r_ * 30, 60 + r_ * 26, 26, 22, ['#1f8a9a', '#4fa9b6', '#86c6cf', '#bfe1e5'][r_], 'none', 0, 3)
        if r_ == 0 and c_ < 4:
            g += T(285 + c_ * 30, 76, ['812', '33', '1907', '5'][c_], 9.5, 700, '#fff', 'middle')
g += T(470, 50, 'every 20 ms of sound becomes 4 integers', 14, 700, MU, 'middle')
g += F(1, R(700, 50, 260, 120, ACL, ACC, 2, 10) + T(830, 90, 'one Transformer', 18, 700, ACC, 'middle') + T(830, 116, 'predicts the next tokens,', 14, 400, INK, 'middle') + T(830, 138, 'like GPT predicts the next word', 14, 400, INK, 'middle')
          + P('M612,110 L696,110', ACC, 2.5, extra='marker-end="url(#mgo)"') + R(990, 80, 160, 60, '#fff', AC2, 1.5, 8) + T(1070, 106, 'text prompt', 14, 700, AC2, 'middle') + T(1070, 126, '"upbeat jazz"', 13, 400, MUT, 'middle') + P('M988,110 L962,110', AC2, 2, extra='marker-end="url(#mga)"'))
pts3 = [('No music theory is built in.', 'Notes, keys and styles are not in the design.'), ('A key or a style inside it must emerge.', 'If there is a graph inside, training put it there.'), ('Open weights, three sizes.', 'small 300M, medium 1.5B, large 3.3B parameters.')]
for k, (a_, b_) in enumerate(pts3):
    y = 220 + k * 70
    g += F(2 if k < 2 else 3, C(70, y - 6, 9, MU) + T(92, y, a_, 18, 700, INK) + T(92, y + 26, b_, 15, 400, MUT))
g += F(4, T(590, 464, 'MusicGen is GPT for audio tokens. Any graph inside it would have to emerge.', 19, 700, INK, 'middle'))
MGEN = sec('MusicGen is a next token predictor for sound', SVG(g), ch='2',
           ref='Copet et al., Simple and Controllable Music Generation, NeurIPS 2023. Demo: ai.honu.io/papers/musicgen. Live: huggingface.co/spaces/facebook/MusicGen',
           notes='MusicGen never sees a waveform. EnCodec compresses every 20 ms into four integers from four codebooks of 2,048 entries, 50 steps per second. The four rows are staggered by one step, so all four are predicted together. A single Transformer, conditioned on a text prompt, predicts the next tokens. Consider playing a 10 second sample from the demo page here.')

# ---- M7: probing, then shapes (helix, circle of fifths) ----
import math as _pm
g = adefs('pb')
g += T(40, 24, 'MusicGen is a GPT over audio tokens, 4 integers per 20 ms, with no music theory built in (down arrow).', 14, 600, MUT)
# column 1: a probe reads it
c1 = T(220, 60, 'A tiny classifier on a frozen layer', 15, 700, INK, 'middle') + T(220, 80, 'reads music theory', 15, 700, INK, 'middle')
bars = [('Jukebox', 0.984, AC2), ('MusicGen small', 0.950, ACC), ('MusicGen medium', 0.914, '#f6a46a'), ('MusicGen large', 0.929, '#f6a46a'), ('hand chroma', 0.878, GRY), ('raw tokens', 0.701, '#c9d0d5')]
for k_, (a_, v, col) in enumerate(bars):
    y = 98 + k_ * 32
    c1 += T(160, y + 16, a_, 13, 700 if 'small' in a_ else 500, INK, 'end') + R(168, y, (v - 0.6) * 420, 22, col, 'none', 0, 3) + T(168 + (v - 0.6) * 420 + 6, y + 16, f'{v:.2f}', 12.5, 700, INK)
c1 += T(220, 312, 'average probe accuracy, axis from 0.6', 12.5, 400, MUT, 'middle') + T(220, 334, 'the smallest MusicGen reads best', 13.5, 600, INK, 'middle')
g += F(1, c1)
# column 2: pitch on a helix
c2 = T(600, 60, 'Pitch sits on a helix', 15, 700, INK, 'middle') + T(600, 80, 'one turn per octave', 13.5, 400, MUT, 'middle')
pts = []
hx = lambda t: (600 + 86 * _pm.sin(2 * _pm.pi * t / 12), 266 - t * 6.6 + 26 * _pm.cos(2 * _pm.pi * t / 12))
for n in range(25):
    pts.append(hx(n) + (n,))
for q in range(96):
    t1, t2 = q / 4, (q + 1) / 4
    (x1, y1), (x2, y2) = hx(t1), hx(t2)
    c2 += P(f'M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}', MU, 2, extra='' if _pm.cos(2 * _pm.pi * (t1 + 0.125) / 12) > 0 else 'opacity=".3"')
for x, y, n in pts:
    front = _pm.cos(2 * _pm.pi * n / 12) > -0.01
    c2 += C(x, y, 6.5 if n % 12 == 0 else 3.6, ACC if n % 12 == 0 else MU, extra='' if front else 'opacity=".3"')
c2 += P(f'M{pts[0][0]:.0f},{pts[0][1]:.0f} L{pts[24][0]:.0f},{pts[24][1]:.0f}', ACC, 1.6, extra='stroke-dasharray="4 4"')
c2 += T(pts[0][0] + 12, pts[0][1] + 5, 'C3', 12.5, 700, '#C45200') + T(pts[12][0] + 12, pts[12][1] + 5, 'C4', 12.5, 700, '#C45200') + T(pts[24][0] + 12, pts[24][1] + 5, 'C5', 12.5, 700, '#C45200')
c2 += T(600, 312, 'shown: one turn per octave, clean guitar: two', 12.5, 400, MUT, 'middle') + T(600, 334, 'Jukebox and MusicGen large, Jul 2026', 13.5, 600, INK, 'middle')
g += F(2, c2)
# column 3: keys on the circle of fifths
c3 = T(980, 60, 'Keys sit on the circle of fifths', 15, 700, INK, 'middle') + T(980, 80, 'clearest in the deepest layers', 13.5, 400, MUT, 'middle')
names = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']
xy = [(980 + 84 * _pm.sin(2 * _pm.pi * q / 12), 192 - 84 * _pm.cos(2 * _pm.pi * q / 12)) for q in range(12)]
for q in range(12):
    a, b = xy[q], xy[(q + 1) % 12]
    c3 += P(f'M{a[0]:.0f},{a[1]:.0f} L{b[0]:.0f},{b[1]:.0f}', LINE, 1.4)
for q, (x, y) in enumerate(xy):
    c3 += C(x, y, 13, '#fff', ACC if q == 0 else MU, 1.6) + T(x, y + 4.5, names[q], 11.5, 700, '#C45200' if q == 0 else MU, 'middle')
c3 += T(980, 312, 'a key probe, scored by transposing', 12.5, 400, MUT, 'middle') + T(980, 334, 'MERT and MusicGen, ISMIR 2026', 13.5, 600, INK, 'middle')
g += F(3, c3)
g += F(4, T(590, 392, 'Each shape is a graph we already know: the semitone chain wound by the octave, and a 12 node cycle.', 17, 700, INK, 'middle')
          + T(590, 426, 'Both are snapshots of single states. Still missing: a graph of how one state follows the next.', 18, 700, ACC, 'middle'))
PROBE = sec('Inside a music generator, music theory has a shape', SVG(g), ch='2',
            ref='Wei, Freeman, Donahue, Sun, ISMIR 2024, Table 2. Do Music Foundation Models Embed Pitch in Helical Structure?, arXiv 2607.29086, 2026. Kanatas, Kong, Alonso-Jim&eacute;nez, Serra, Bogdanov, What Makes a Good Layer?, ISMIR 2026',
            notes='Three steps, one click each. First, a probe reads music theory (Wei et al.). Second, a July 2026 preprint feeds 36 single notes, C3 to B5, to Jukebox and MusicGen large, projects each layer to 3D and fits a helix: both form one, clearer in deeper layers, Jukebox mean helicality 2.28 and MusicGen 1.16 against 0.37 for random points, and the shape depends on the instrument, a Hammond organ winds once per octave, a clean electric guitar twice. Third, Kanatas et al. at ISMIR 2026 study 12 music models including MusicGen small, medium and large: a key probe projected on the circle of fifths stays consistent under transposition, and tonal tasks peak in the deepest layers. Our reading, not theirs: a helix is the semitone chain wound by the octave, the circle of fifths is a 12 node cycle, so these are graphs too, but graphs of where a single state sits. Neither paper reads how one state follows the next, and that transition graph is what our plan builds. Then bridge to steering: and to change the music, people still push a vector. Details of the probe study: Wei et al. built SynTheory, synthetic clips where one concept changes at a time: tempo, time signature, notes, intervals, scales, chords, chord progressions. They froze the generators and trained tiny classifiers on each layer. Concepts are linearly readable. Plain chroma features tie the models on static notes and lose on progressions. Castellon et al. found Jukebox layers beat tag trained representations by about 30 percent, most on key detection. Bridge: a probe tells us what is stored, not how the states move. That is the graph question.')

# ---- B1: language models already met the brain ----
g = adefs('lb')
g += R(60, 60, 220, 300, SOFT, AC2, 1.5, 12) + T(170, 95, 'language model', 16, 700, AC2, 'middle')
for k in range(5):
    g += R(90, 115 + k * 46, 160, 34, '#fff', '#9aa6ae', 1.2, 5) + T(170, 137 + k * 46, f'layer {5 - k}', 12.5, 600, MUT, 'middle')
g += R(400, 60, 220, 300, MUL, MU, 1.5, 12) + T(510, 95, 'listener\'s brain', 16, 700, MU, 'middle')
for k, lab in enumerate(['higher areas', '', 'language areas', '', 'auditory cortex']):
    g += R(430, 115 + k * 46, 160, 34, '#fff', MU, 1.2, 5) + T(510, 137 + k * 46, lab, 12.5, 600, MU, 'middle')
g += F(1, ''.join(P(f'M252,{132 + k * 46} L426,{132 + k * 46}', ACC, 2, extra='stroke-dasharray="6 4" marker-end="url(#lbo)"') for k in (0, 2, 4)) + T(340, 380, 'predict brain activity from model activity', 14, 700, ACC, 'middle'))
works = [('Schrimpf et al. 2021', 'The better a model predicts the next word, the better it predicts the brain.'),
         ('Goldstein et al. 2022', 'The brain predicts the next word before it arrives, then measures its surprise.'),
         ('Kell et al. 2018', 'In audio networks, middle layers match early auditory cortex, deep layers later areas.'),
         ('Tuckute et al. 2024', 'Sentences chosen by a model can drive or quiet the brain\'s language network.')]
for k, (a_, b_) in enumerate(works):
    y = 60 + k * 82
    g += F(2 if k < 2 else 3, R(670, y, 480, 72, '#fff', LINE, 1.5, 8) + T(688, y + 26, a_, 15, 700, AC2) + wrap(688, y + 50, b_, 13.5, 400, INK, width=62, lh=18))
g += F(4, T(590, 466, 'Brains and models are both next event predictors, so one can be a yardstick for the other.', 18, 700, INK, 'middle'))
BRL = sec('Predict the next word well, and you predict the brain', SVG(g), ch='2',
          ref='Schrimpf et al., PNAS 2021. Caucheteux and King, Communications Biology 2022. Goldstein et al., Nature Neuroscience 2022. Kell et al., Neuron 2018. Tuckute et al., Nature Human Behaviour 2024',
          notes='The unifying theme of the brain section. A model and a brain can be compared without any theory of language or music: fit a map from model activity to brain activity and test it on new stimuli. In language this works, and models that predict the next word better also predict the brain better. Caucheteux and King found the same with 102 people in fMRI and MEG.')

# ---- B2: a graph predicts the listening brain (IDyOM) ----
g = adefs('id')
g += T(260, 44, 'a melody, note by note', 15, 700, AC2, 'middle')
nts = [(90, 135), (150, 115), (210, 145), (270, 105), (330, 130), (390, 90)]
g += ''.join(L(60, 80 + k * 14, 430, 80 + k * 14, GRY, 1) for k in range(5)) + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="7.5" fill="{INK}"/>' for x, y in nts)
idy = R(500, 50, 300, 130, ACL, ACC, 2, 10) + T(650, 82, 'IDyOM: a note transition graph', 16, 700, ACC, 'middle') + T(650, 108, 'with several memory lengths,', 14, 400, INK, 'middle') + T(650, 130, 'learned from thousands of melodies', 14, 400, INK, 'middle') + T(650, 160, 'the cousin of our 12 node graph', 13, 700, ACC, 'middle')
idy += P('M436,115 L496,115', AC2, 2.5, extra='marker-end="url(#ida)"')
g += F(1, idy)
hs = [0.3, 0.5, 0.95, 0.35, 0.7, 1.0]
sur = T(990, 44, 'how surprising is each note?', 15, 700, ACC, 'middle') + ''.join(R(880 + k * 38, 170 - 100 * h, 28, 100 * h, ACC, 'none', 0, 3) for k, h in enumerate(hs)) + L(870, 172, 1110, 172, INK, 1.5) + P('M804,115 L866,115', AC2, 2.5, extra='marker-end="url(#ida)"')
g += F(2, sur)
eeg = R(60, 220, 1090, 150, MUL, MU, 2, 10) + T(80, 252, 'EEG while 20 people listen to Bach', 16, 700, MU)
ons = [110 + k * 100 for k in range(6)]
def _erp(x):
    v = 0
    for t0, h in zip(ons, hs):
        v += 6 * math.exp(-((x - t0 - 14) / 9) ** 2) - 34 * h * math.exp(-((x - t0 - 42) / 15) ** 2)
    return 318 - v
eeg += ''.join(L(t0, 270, t0, 356, '#C9C4BD', 1, 'stroke-dasharray="3 3"') + C(t0, 270, 4, INK) for t0 in ons)
eeg += P('M80,318 ' + ' '.join(f'L{x},{_erp(x):.1f}' for x in range(83, 700, 3)), MU, 2, extra='stroke-linejoin="round"')
eeg += T(110, 290, 'note', 11.5, 400, MUT, 'middle') + T(ons[5] + 42, 362, 'big surprise, big response', 12.5, 600, MU, 'middle')
eeg += T(740, 290, 'Surprise explains the brain response', 16, 700, INK) + T(740, 316, 'beyond the sound itself, within 350 ms', 15, 400, INK) + T(740, 340, 'after each note, in 16 of 20 listeners.', 15, 400, INK)
g += F(3, eeg)
g += F(4, T(590, 420, 'A graph of note transitions is something the listening brain is measurably tracking.', 19, 700, INK, 'middle') + T(590, 452, 'So the brain can judge a graph.', 18, 700, ACC, 'middle'))
BRI = sec('A note transition graph predicts the listening brain', SVG(g), ch='2',
          ref='Pearce, IDyOM, 2005 and 2018. Di Liberto et al., Cortical encoding of melodic expectations in human temporal cortex, eLife 2020',
          notes='This is where graphs and brains meet. IDyOM is a variable order Markov model, the grown up version of our 12 node graph. It assigns every note a surprise value. Di Liberto and colleagues show that this surprise explains EEG responses beyond acoustic features, strongest within the first 350 ms, in 16 of 20 participants, with a large effect (d about 1.6). ECoG locates it near auditory cortex.')

# ---- B3: rebuild ----
g = adefs('rb')
g += img(40, 40, 700, 112, 'figs/denk2023_fig1.png') + T(390, 172, 'Brain2Music: fMRI to a music embedding to a generator', 13, 600, MUT, 'middle')
inv = R(40, 200, 340, 190, SOFT, LINE, 1, 10) + T(60, 232, 'Through the skull', 17, 700, AC2) + T(60, 262, '29 patients, 2,668 electrodes', 14, 400, INK) + T(60, 286, 'on auditory cortex, during surgery.', 14, 400, INK) + T(60, 318, 'A Pink Floyd song is rebuilt', 14, 700, INK) + T(60, 342, 'from brain activity alone.', 14, 700, INK) + T(60, 372, 'Bellier et al., PLOS Biology 2023', 12.5, 400, MUT)
g += F(1, inv)
non = R(400, 200, 340, 190, MUL, MU, 1.5, 10) + T(420, 232, 'Without surgery', 17, 700, MU) + T(420, 262, 'fMRI of 5 listeners, mapped to', 14, 400, INK) + T(420, 286, 'a music embedding, then to MusicLM.', 14, 400, INK) + T(420, 318, 'Genre, instruments and mood', 14, 700, INK) + T(420, 342, 'of the clip come back.', 14, 700, INK) + T(420, 372, 'Denk et al., Nature Communications 2025', 12.5, 400, MUT)
g += F(2, non)
g += F(3, R(780, 40, 370, 350, '#fff', LINE, 1.5, 12) + T(965, 80, 'Listen', 20, 700, ACC, 'middle') + T(965, 112, 'original and rebuilt clips:', 14, 400, INK, 'middle')
          + T(965, 160, 'Brain2Music samples', 15, 700, MU, 'middle') + T(965, 184, 'google-research.github.io/seanet/brain2music', 11.5, 400, MUT, 'middle')
          + T(965, 240, 'Pink Floyd reconstruction', 15, 700, AC2, 'middle') + T(965, 264, 'supporting audio S1 to S3 of', 12.5, 400, MUT, 'middle') + T(965, 284, 'doi.org/10.1371/journal.pbio.3002176', 11.5, 400, MUT, 'middle'))
g += F(4, T(590, 440, 'The brain keeps enough of the music to rebuild it, so it is a rich enough instrument to judge a style.', 17, 700, INK, 'middle'))
BRR = sec('The brain keeps enough of the music to rebuild it', SVG(g), ch='2',
          ref='Bellier et al., Music can be reconstructed from human auditory cortex activity using nonlinear decoding models, PLOS Biology 2023. Denk et al., Nature Communications 2025 (Brain2Music)',
          notes='Two experiments, one message. Bellier: epilepsy patients with electrodes on the brain listened to Another Brick in the Wall, and a nonlinear decoder rebuilt a recognizable song (r squared 0.43 versus 0.33 for a linear one). Denk: no surgery, fMRI mapped into the embedding space of a music model, then MusicLM generates music that matches genre, instruments and mood. Play one rebuilt clip if the room has sound. Open EEG music datasets for our own work: OpenMIIR, NMED-T, NMED-H, MUSIN-G.')

# ---- B4: music generators meet the brain only from the outside ----
g = adefs('mo')
cards = [('Audio models in general', 'Pepino et al. 2025', '36 audio models: the better a model is at its tasks, the more brain like it is.'),
         ('A music generator\'s output', 'Noguchi et al. 2026', 'MusicGen\'s next token surprise helps identify which song a person hears from EEG: 0.823 to 0.887.'),
         ('A music model\'s embeddings', 'Denk et al. 2025', 'Embeddings map onto auditory cortex, but the low to high hierarchy is weaker than in vision.')]
for k, (a_, who, b_) in enumerate(cards):
    y = 40 + k * 108
    g += F(k, R(40, y, 700, 94, '#fff', LINE, 1.5, 10) + T(60, y + 30, a_, 17, 700, AC2) + T(720, y + 30, who, 13, 600, MUT, 'end') + wrap(60, y + 58, b_, 14.5, 400, INK, width=88, lh=20)) if k else R(40, y, 700, 94, '#fff', LINE, 1.5, 10) + T(60, y + 30, a_, 17, 700, AC2) + T(720, y + 30, who, 13, 600, MUT, 'end') + wrap(60, y + 58, b_, 14.5, 400, INK, width=88, lh=20)
g += F(3, R(780, 40, 370, 310, ACL, ACC, 2, 12) + T(965, 84, 'Missing', 22, 700, ACC, 'middle') + T(965, 126, 'Nobody has read a graph', 16, 700, INK, 'middle') + T(965, 150, 'from inside a music generator', 16, 700, INK, 'middle') + T(965, 174, 'and asked the brain', 16, 700, INK, 'middle') + T(965, 198, 'whether it is real.', 16, 700, INK, 'middle')
          + T(965, 250, 'The outside: outputs, embeddings.', 14, 400, MUT, 'middle') + T(965, 274, 'The inside: how states connect.', 14, 700, ACC, 'middle'))
g += F(4, T(590, 420, 'Music generators meet the brain through outputs, embeddings and layers, never as a graph.', 19, 700, INK, 'middle'))
BRG = sec('Music generators meet the brain, but never as a graph', SVG(g), ch='2',
          ref='Pepino et al., arXiv 2511.16849, 2025. Noguchi et al., arXiv 2603.03190, 2026. Denk et al., Nature Communications 2025. Mischler et al., Nature Communications 2025',
          notes='Same yardstick as language, applied to audio and music. Three lines of work on the cards look at what comes out of a model or at whole embeddings. A fourth goes inside: Mischler, Mesgarani and colleagues (Nature Communications, Oct 2025) fit the 13 layers of a symbolic music transformer (Musicautobot) to EEG from 10 pianists and 10 non musicians and to intracranial recordings, deeper layers predict better and musicians use longer context. None of them reads a graph of how states follow each other. Noguchi is the closest: it uses MusicGen large output probabilities, not internal layers, no steering and no style. The gap is the inside.')

# ---- plan ----
g = adefs('pn')
g += T(40, 30, 'So far the brain has met music generators through outputs, embeddings and layer activations. Missing: a graph of how states follow each other.', 15, 600, MUT)
steps = [('1', 'Generate', 'clips of each style with MusicGen, keep the middle layer state at every step', AC2),
         ('2', 'Read a graph', 'cluster the states, count transitions: a graph from inside the model', ACC),
         ('3', 'Play to listeners', 'record EEG while people listen to the same clips', MU)]
for k, (n_, a_, b_, col) in enumerate(steps):
    x = 40 + k * 380
    blk = R(x, 50, 350, 150, '#fff', col, 2, 12) + C(x + 36, 92, 20, col) + T(x + 36, 99, n_, 18, 700, '#fff', 'middle') + T(x + 68, 99, a_, 19, 700, col) + wrap(x + 24, 140, b_, 14.5, 400, INK, width=40, lh=20)
    if k < 2:
        blk += P(f'M{x+352},125 L{x+376},125', AC2, 3, extra='marker-end="url(#pna)"')
    g += F(k, blk) if k else blk
cmp_ = R(40, 230, 1110, 140, SOFT, LINE, 1, 12) + T(590, 264, 'Which explains the brain best?', 19, 700, INK, 'middle')
for k, (a_, col) in enumerate([('surprise from IDyOM, a graph from scores', AC2), ('surprise from the graph read inside MusicGen', ACC), ('surprise from MusicGen\'s own output', MU)]):
    cmp_ += R(70 + k * 360, 290, 340, 56, '#fff', col, 1.8, 28) + T(240 + k * 360, 324, a_, 14, 700, col, 'middle')
g += F(3, cmp_)
g += F(4, T(590, 416, 'If the graph inside the generator explains the listener as well as the generator itself,', 17, 700, INK, 'middle') + T(590, 446, 'the graph is real. If not, it is our drawing, not the model\'s.', 17, 700, ACC, 'middle'))
PLAN = secx('Our plan: a graph from inside MusicGen, judged by the brain', SVG(g), ch='2', status='plan',
            ref='So far (down arrow): Pepino et al. 2025, Noguchi et al. 2026, Denk et al. 2025, Mischler et al., Nature Communications 2025',
            notes='One question replaces the earlier four outcome matrix. Three sources of surprise for the same clips, one yardstick. The scores graph (IDyOM) is the baseline from music cognition, MusicGen output surprisal is what Noguchi used, and the graph from inside MusicGen is ours. The steering asymmetry shown after the probing slide is the follow up: once the graph is validated, ask whether steering can reach a style on it.')

# ======================= ROUND 6 (Nov 2 2026): knowledge beyond text, emotion =======================
def photo(cx, cy, r, fname, initials, col):
    d = 2 * r
    return (f'<foreignObject x="{cx-r}" y="{cy-r}" width="{d}" height="{d}"><div xmlns="http://www.w3.org/1999/xhtml" '
            f'style="position:relative;width:{d}px;height:{d}px;border-radius:10px;overflow:hidden;background:#f2f3f4">'
            f'<span style="position:absolute;left:0;top:0;width:{d}px;height:{d}px;display:flex;align-items:center;justify-content:center;font-family:Fira Sans,sans-serif;font-weight:700;font-size:{int(r*0.7)}px;line-height:1;color:{col}">{initials}</span>'
            f'<img src="figs/people/{fname}" alt="" onerror="this.remove()" style="position:absolute;left:0;top:0;width:{d}px;height:{d}px;max-width:none;max-height:none;margin:0;padding:0;border:0;box-shadow:none;border-radius:10px;object-fit:cover"/></div></foreignObject>')

def qline(x, y, segs, size, a='start'):
    out = f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{a}" fill="{INK}" font-style="italic">'
    for t_, hl in segs:
        out += f'<tspan font-weight="{700 if hl else 400}" fill="{ACC if hl else INK}" font-style="{"normal" if hl else "italic"}">{t_}</tspan>'
    return out + '</text>'

def qcard(x, y, w, h, fname, ini, lines, who, src, col, size=16):
    out = R(x, y, w, h, '#fff', LINE, 1.5, 14) + R(x, y, 6, h, col, 'none', 0, 3)
    out += T(x + 22, y + 52, '“', 64, 700, col, 'start', 'opacity=".35" font-family="Georgia,serif"')
    for k, segs in enumerate(lines):
        out += qline(x + 62, y + 34 + k * (size + 7), segs, size)
    yb = y + h - 22
    px = x + w - 80 if fname else x + w - 20
    out += (photo(x + w - 44, yb - 10, 28, fname, ini, col) if fname else '') + T(px, yb - 8, who, 14, 700, INK, 'end') + T(px, yb + 10, src, 12, 400, MUT, 'end')
    return out

g = adefs('bt')
def mlist(x, y, w, who, when, fname, ini, items, hi, col):
    tx = x + 86 if fname else x + 24
    out = R(x, y, w, 300, '#fff', LINE, 1.5, 12) + (photo(x + 44, y + 44, 28, fname, ini, col) if fname else '') + T(tx, y + 40, who, 16, 700, INK) + T(tx, y + 62, when, 13, 400, MUT)
    for k, (it, h) in enumerate(zip(items, hi)):
        yy = y + 104 + k * 27
        if h:
            out += R(x + 18, yy - 18, w - 36, 25, {'L': ACL, 'E': '#eef0ff', 'M': MUL}[h], 'none', 0, 12)
        out += T(x + 32, yy, it, 14.5, 700 if h else 400, {'L': ACC, 'E': '#5a4fcf', 'M': MU}.get(h, INK) if h else INK)
    return out
g += mlist(30, 30, 270, 'Howard Gardner', 'Frames of Mind, 1983', 'howard-gardner.jpg', 'HG',
           ['linguistic', 'logical mathematical', 'musical', 'spatial', 'bodily kinesthetic', 'interpersonal', 'intrapersonal'], ['L', 'E', 'M', '', '', '', ''], AC2)
g += F(1, mlist(320, 30, 270, 'Fei-Fei Li', 'interview, 2026', None, 'FL',
           ['language', 'perceptual', 'spatial', 'bodily', 'emotional'], ['L', '', '', '', 'M'], AC2))
rows = [('Language', 'facts in text: Part 1', ACC, ACL), ('Equations', 'open direction: see the sketch', '#5a4fcf', '#eef0ff'), ('Music and emotion', 'Part 2', MU, MUL)]
mp = ''
for k, (a_, b_, col, fill) in enumerate(rows):
    y = 30 + k * 62
    mp += R(620, y, 530, 50, fill, col, 1.5, 25) + T(642, y + 32, a_, 17, 700, col) + T(830, y + 32, b_, 15, 400, INK)
g += F(2, mp)
sk = R(620, 222, 530, 128, '#fff', '#5a4fcf', 1.5, 12) + T(640, 246, 'Inside a language model, 36 + 59 is a graph of two paths', 13.5, 700, '#5a4fcf')
sk += R(640, 286, 70, 34, SOFT, '#9aa6ae', 1.2, 17) + T(675, 308, '36 + 59', 13, 700, INK, 'middle')
sk += P('M712,296 C760,276 800,276 846,292', '#5a4fcf', 2.2, extra='marker-end="url(#bta)"') + T(780, 270, 'rough size: about 92', 12, 600, '#5a4fcf', 'middle')
sk += P('M712,312 C760,332 800,332 846,316', '#5a4fcf', 2.2, extra='marker-end="url(#bta)"') + T(780, 344, 'last digit: 6 + 9 ends in 5', 12, 600, '#5a4fcf', 'middle')
sk += R(850, 286, 70, 34, '#eef0ff', '#5a4fcf', 1.5, 17) + T(885, 308, '95', 15, 700, '#5a4fcf', 'middle') + T(1030, 300, 'redrawn after', 12, 400, MUT, 'middle') + T(1030, 316, 'Lindsey et al. 2025', 12, 600, MUT, 'middle')
g += F(3, sk)
g += F(4, qcard(30, 358, 1120, 84, 'fei-fei-li.jpg', 'FL', [[('Spatial intelligence represents the ', False), ('frontier beyond language', True), ('.', False)]], 'Fei-Fei Li', 'From Words to Worlds, Substack essay, 2025', AC2, 19)
          + T(590, 462, 'Equations and music are knowledge beyond text. They may need graphs even more than text does.', 18, 700, INK, 'middle'))
BEYOND = sec('Knowledge is not only text', SVG(g), ch='0',
             ref='Gardner, Frames of Mind, 1983. Fei-Fei Li, Silicon Valley Girl podcast, 2026 (five intelligences, Chinese transcript), and From Words to Worlds, Substack essay, 2025. Lindsey et al., On the Biology of a Large Language Model, Transformer Circuits 2025',
             notes='Photos: Wikimedia Commons, see each file page for author and license. Why language and music, and why not only text. Gardner listed musical intelligence and logical mathematical intelligence as their own kinds of intelligence, separate from language. Fei-Fei Li lists language, perceptual, spatial, bodily and emotional intelligence. This talk covers language and music, equations are the next step: in Claude, addition already runs as a small graph of two parallel paths. Photos: drop licensed images into figs/people with the file names in figs/people/README.md.')

g = adefs('em')
g += T(40, 40, 'Machines need emotion', 17, 700, AC2)
g += qcard(30, 54, 540, 130, 'rosalind-picard.jpg', 'RP', [[('we give computers the ability to ', False)], [('recognize, express, and in some cases,', True)], [("'have' emotions", True)]], 'Rosalind Picard', 'Affective Computing, MIT Press 1997', AC2, 16)
g += qcard(30, 196, 540, 130, 'marvin-minsky.jpg', 'MM', [[('Each of our major ', False), ('emotional states', True)], [('results from turning certain ', False), ('resources on', True)], [('while turning certain others off.', False)]], 'Marvin Minsky', 'The Emotion Machine, 2006', AC2, 16)
chain = [('music', MU), ('expectation', ACC), ('emotion', '#5a4fcf'), ('brain response', MU)]
ch_ = T(870, 40, 'Music moves us through expectation', 17, 700, MU, 'middle')
for k, (a_, col) in enumerate(chain):
    x = 612 + k * 136
    ch_ += R(x, 56, 116, 40, '#fff', col, 2, 20) + T(x + 58, 82, a_, 14, 700, col, 'middle')
    if k < 3:
        ch_ += P(f'M{x+118},76 L{x+134},76', AC2, 2.5, extra='marker-end="url(#ema)"')
g += F(1, ch_)
g += F(2, qcard(600, 110, 550, 150, None, 'LM', [[('affect is aroused when an ', False), ('expectation', True), (',', False)], [('a tendency to respond, activated by the music,', False)], [('is ', False), ('temporarily inhibited or permanently blocked', True)]], 'Leonard Meyer', 'Emotion and Meaning in Music, 1956, p. 31', ACC, 16))
ev = [('Salimpoor et al. 2011', 'dopamine at peak musical pleasure, and just before'), ('Koelsch 2014', 'engages core emotion areas: amygdala, hippocampus')]
for k, (a_, b_) in enumerate(ev):
    y = 274 + k * 56
    g += F(3, R(600, y, 550, 48, MUL, MU, 1.2, 10) + T(618, y + 30, a_, 14, 700, INK) + T(780, y + 30, b_, 13.5, 400, INK))
g += F(3, R(30, 340, 540, 92, ACL, ACC, 1.5, 12) + T(50, 368, 'The link to this talk', 15.5, 700, ACC) + T(50, 394, 'Expectation is what a note transition graph computes.', 14, 400, INK) + T(50, 416, 'Meyer 1956, Huron 2006, IDyOM: the same idea, made computable.', 14, 400, INK))
g += F(4, T(590, 466, 'Music is one of the most measurable routes to emotion, so it is where a brain can judge a model.', 18, 700, INK, 'middle'))
EMOTION = sec('Music is where emotion can be measured', SVG(g), ch='0',
              ref='Picard, Affective Computing, MIT Press 1997, introduction. Minsky, The Emotion Machine, 2006. Meyer, Emotion and Meaning in Music, 1956, p. 31, as quoted in Margulis 2005. Huron, Sweet Anticipation, 2006. Salimpoor et al., Nature Neuroscience 2011. Koelsch, Nature Reviews Neuroscience 2014',
              notes='Photos: Wikimedia Commons, see each file page for author and license. Why music, beyond being a second domain. Emotion is one of the intelligences beyond language, and music is one of the most reliable ways to evoke it in a lab, with a response we can measure in the brain. The bridge is expectation: music moves us partly by playing with what we expect next, and a transition graph is exactly a model of what comes next. Check exact wording of the five citations before the talk, they were added from memory.')

# ======================= ROUND 7 (Nov 2 2026): Markov order results =======================
def hbars(x0, y0, rows, scale, maxv, lw=300, bh=34, gap=14):
    out = ''
    for k, (lab, v, col, note, bold) in enumerate(rows):
        y = y0 + k * (bh + gap)
        out += T(x0 + lw - 12, y + bh / 2 + 6, lab, 15, 700 if bold else 500, ACC if bold else INK, 'end')
        out += R(x0 + lw, y, v / maxv * scale, bh, col, 'none', 0, 4)
        out += T(x0 + lw + v / maxv * scale + 10, y + bh / 2 + 6, f'{v:g}%', 16, 700, INK) + T(x0 + lw + v / maxv * scale + 72, y + bh / 2 + 6, note, 14, 700, ACC if bold else MUT)
    return out

g = adefs('ro')
g += T(40, 40, 'Which tradition is this melody from? 992 melodies, six traditions, five fold cross validation', 14, 600, MUT)
rowsA = [('chance', 16.7, '#d3d7da', '', False), ('12 note counts, no order', 41.9, '#d3d7da', '', False), ('graph, 1 note of memory', 70.2, GRY, '+28 over counts', False), ('graph, 2 notes of memory', 78.2, '#f6a46a', '+8 points', False),
         ('graph, memory as needed', 73.3, '#f6a46a', '+3 points', False)]
g += hbars(40, 56, rowsA, 640, 100, bh=28, gap=10)
rowsB = [('note plus length, 1 note of memory', 86.8, '#ef7d33', '+17 points', False), ('note plus length, 2 notes of memory', 86.2, '#ef7d33', 'no gain from memory', False), ('note plus length, memory as needed', 88.7, ACC, '+19 points', True)]
g += F(1, L(40, 256, 1150, 256, LINE, 1.5) + hbars(40, 268, rowsB, 640, 100, bh=28, gap=10))
g += F(2, R(160, 386, 860, 44, ACL, ACC, 1.5, 10) + T(590, 415, 'A richer node buys more than a longer memory.', 19, 700, INK, 'middle'))
g += F(3, T(590, 462, 'For a graph, what a node means matters more than how far back it looks.', 17, 700, ACC, 'middle'))
RICHER = sec('Richer nodes beat longer memory', SVG(g), ch='2', status='prog',
             ref='Our experiments, Nov 2026: 992 melodies from six music21 corpora, same five folds for every method. Points are differences from the 1 note graph (70.2%). "Memory as needed" is a variable order model, the IDyOM style',
             notes='With richer nodes, a second note of memory adds nothing (86.8 to 86.2), which is the fair comparison. First the baseline everyone asks for: counting the 12 notes without any order gets 41.9 percent, so the order, the graph, adds 28 points. Three lessons. One more note of memory helps, 70 to 78. Letting the graph decide how much memory each context needs is not better for notes alone (73.3, below 2 notes at 78.2), it wins only with richer nodes (88.7). But giving each node one more attribute, how long the note lasts, jumps to 87 to 89, more than any change of order. Caveats: Bach repeats chorale tunes across harmonizations, which flatters long memory, and Palestrina and Trecento editions use long note values, so part of the duration gain reflects notation.')

g = adefs('gc')
g += T(40, 40, 'Generate 600 melodies per setting, then ask a style classifier and a copy checker', 14, 600, MUT)
cols_ = [('1 note', 57, 7.6, GRY), ('2 notes', 64, 8.3, '#f6a46a'), ('memory as needed', 65, 12.1, ACC)]
g += T(300, 82, 'recognized as its style', 16, 700, INK, 'middle') + T(880, 82, 'longest span copied from training', 16, 700, INK, 'middle')
for k, (lab, st, cp, col) in enumerate(cols_):
    x = 110 + k * 130
    g += R(x, 260 - st * 1.6, 90, st * 1.6, col, 'none', 0, 4) + T(x + 45, 252 - st * 1.6, f'{st}%', 16, 700, INK, 'middle') + T(x + 45, 282, lab, 13.5, 600, INK, 'middle')
g += L(90, 260, 500, 260, INK, 1.5)
cp_ = ''
for k, (lab, st, cp, col) in enumerate(cols_):
    x = 690 + k * 130
    cp_ += R(x, 260 - cp * 9, 90, cp * 9, col, 'none', 0, 4) + T(x + 45, 252 - cp * 9, f'{cp} notes', 15, 700, INK, 'middle') + T(x + 45, 282, lab, 13.5, 600, INK, 'middle')
cp_ += L(670, 260, 1080, 260, INK, 1.5) + L(670, 260 - 10.9 * 9, 1080, 260 - 10.9 * 9, '#c0392b', 1.5, 'stroke-dasharray="6 4"') + T(672, 260 - 10.9 * 9 - 6, 'real melodies: 10.9', 12.5, 700, '#c0392b')
g += F(1, cp_)
pb = T(40, 334, 'Vote: which one is the real Bach? Same rhythm and key, only the order of pitches changes', 14, 700, MUT)
pb += playbtn(40, 344, 250, 'bach_order2', 'melody A', AC2) + playbtn(300, 344, 250, 'bach_real', 'melody B', AC2)
g += F(2, pb)
g += F(3, T(610, 372, 'B is the real Bach. A came from the 2 note graph,', 15, 600, '#C45200') + T(610, 392, 'and under that 6 note copy limit it still scores 61% (64% free).', 15, 600, '#C45200')
          + T(590, 450, 'The useful graph remembers a little and copies nothing long.', 18, 700, ACC, 'middle'))
COPY = sec('The longest memory sounds most like the style, because it copies', SVG(g), ch='2', status='prog',
           ref='Our experiments, Nov 2026. Clips: order 2 and the other settings sampled with a 6 note copy limit, one sample each, fixed seed, no cherry picking. Real Bach melody: BWV 329 soprano, held out',
           notes='Live vote first (the folk clips are in the repo if asked): play melody A, then B, and ask for hands, which one is the real Bach. Then reveal. This is a pilot of the listening test, either result is honest data. Generation tells the other half. Plain sampling with more memory is recognized as its style more often, 57 to 65, but the variable order model copies 12 note stretches verbatim and 99 percent of its 4 note patterns already exist in training. A 6 note copy limit keeps most of the gain. Honest caveat: these automatic judges rate generated melodies above real held out ones (52 percent), so they measure typicality, not musical conviction. A listening test is the next step. The LLM judge numbers on the memory order slide come from the website, not from this run.')

# ======================= ROUND 8 (Nov 2 2026): slides 9 and 10 on one template =======================
PURP = '#5a4fcf'

def steps(active):
    out = ''
    for k, lab in enumerate(['Knowledge beyond text', 'Why music: emotion']):
        x = 30 + k * 300
        on = (k == active)
        out += R(x, 6, 280, 30, ACC if on else '#fff', ACC if on else LINE, 1.5, 15) + C(x + 18, 21, 10, '#fff' if on else SOFT) + T(x + 18, 25.5, str(k + 1), 12, 700, ACC if on else MUT, 'middle')
        out += T(x + 36, 26, lab, 14, 700, '#fff' if on else MUT)
        if k == 0:
            out += P('M314,21 L326,21', LINE, 2, extra='marker-end="url(#pea)"')
    return out

def person(x, y, w, h, fname, ini, name, title_lines, col):
    """photo 96 px on the left, name and credential beside it, content starts at y + 132"""
    out = R(x, y, w, h, '#fff', LINE, 1.5, 14)
    out += photo(x + 66, y + 66, 48, fname, ini, col)
    out += T(x + 132, y + 50, name, 20, 700, INK)
    for k, tl in enumerate(title_lines):
        out += T(x + 132, y + 74 + k * 19, tl, 13.5, 600, AC2)
    return out

def chips(x, y, items, maxw):
    out = ''; cx = x; cy = y
    for it, hl in items:
        w = len(it) * 7.3 + 22
        if cx + w > x + maxw:
            cx = x; cy += 30
        col = {'L': ACC, 'E': PURP, 'M': MU}.get(hl, '#9aa6ae'); fill = {'L': ACL, 'E': '#eef0ff', 'M': MUL}.get(hl, '#fff')
        out += R(cx, cy, w, 24, fill, col, 1.5, 12) + T(cx + w / 2, cy + 16.5, it, 12.5, 700 if hl else 500, col if hl else MUT, 'middle')
        cx += w + 8
    return out

def quote(x, y, lines, size=15.5, lh=22):
    out = T(x - 4, y + 18, '“', 44, 700, ACC, 'end', 'opacity=".45" font-family="Georgia,serif"')
    for k, segs in enumerate(lines):
        out += qline(x + 8, y + k * lh, segs, size)
    return out

# ---- slide 9 ----
g = adefs('pe')
g += steps(0)
c1 = person(30, 50, 545, 282, 'howard-gardner.jpg', 'HG', 'Howard Gardner', ['Harvard psychologist, theory of multiple intelligences'], AC2)
c1 += chips(52, 182, [('linguistic', 'L'), ('logical mathematical', 'E'), ('musical', 'M'), ('spatial', ''), ('bodily', ''), ('interpersonal', ''), ('intrapersonal', '')], 490)
c1 += T(52, 268, 'Intelligence is plural. Each kind has its own', 15.5, 600, INK) + T(52, 290, 'brain systems and its own symbols, so one', 15.5, 600, INK) + T(52, 312, 'kind cannot stand in for another.', 15.5, 600, INK)
c1 += T(555, 318, 'Frames of Mind, 1983', 12.5, 400, MUT, 'end')
g += c1
c2 = person(605, 50, 545, 282, 'fei-fei-li.jpg', 'FL', 'Fei-Fei Li', ['Stanford professor, creator of ImageNet,', 'cofounder of World Labs'], AC2)
c2 += chips(627, 182, [('linguistic', 'L'), ('spatial', ''), ('emotional, still missing', 'M')], 490)
c2 += quote(645, 236, [[('Spatial intelligence is', False)], [("AI's next frontier", True), ('.', False)]], 18, 26)
c2 += T(1130, 318, "From Words to Worlds, essay, 2025. Lenny's Podcast, Nov 2025", 12.5, 400, MUT, 'end')
g += F(1, c2)
band = T(30, 356, 'What this talk covers', 14, 700, MUT)
tiles = [('Text', 'Part 1: facts inside a language model', ACC, ACL, ''), ('Equations', 'not today: 36 + 59 runs as two paths inside a model', PURP, '#fff', 'stroke-dasharray="7 5"'), ('Music and emotion', 'Part 2: style, expectation, the brain', MU, MUL, '')]
for k, (a_, b_, col, fill, dash) in enumerate(tiles):
    x = 30 + k * 377
    band += R(x, 366, 360, 60, fill, col, 2, 14, dash) + T(x + 18, 390, a_, 17, 700, col) + T(x + 18, 413, b_, 13, 400, INK)
g += F(2, band)
g += F(3, T(590, 466, 'Equations and music are knowledge beyond text. They may need graphs even more than text does.', 17, 700, INK, 'middle'))
BEYOND2 = sec('Knowledge is not only text', SVG(g), ch='0',
              ref='Gardner, Frames of Mind, 1983. Fei-Fei Li, From Words to Worlds: Spatial Intelligence is AI\'s Next Frontier, Substack essay, Nov 2025, and Lenny\'s Podcast, Nov 2025. Lindsey et al., On the Biology of a Large Language Model, 2025. Photos: Wikimedia Commons',
              notes='Step 1 of 2. A psychologist and an AI leader say the same thing from two sides: intelligence and knowledge come in several kinds, and language is only one. Gardner counts musical and logical mathematical intelligence as their own kinds. Fei-Fei Li names linguistic and spatial intelligence and says emotional intelligence is still missing in AI, and calls space the frontier beyond language. This talk covers text and music. Equations are next: inside Claude, 36 + 59 runs as two parallel paths, one for the rough size and one for the last digit (Lindsey et al. 2025).')

# ---- slide 10 ----
g = adefs('pe')
g += steps(1)
w3 = 365
c1 = person(30, 50, w3, 282, 'rosalind-picard.jpg', 'RP', 'Rosalind Picard', ['MIT Media Lab, founder of', 'affective computing'], AC2)
c1 += quote(62, 186, [[('we give computers the ability', False)], [('to ', False), ('recognize, express,', True)], [('and in some cases,', False)], [("'have' emotions", True)]], 15.5, 23)
c1 += T(375, 320, 'Affective Computing, MIT Press, 1997', 12, 400, MUT, 'end')
g += c1
c2 = person(407, 50, w3, 282, 'marvin-minsky.jpg', 'MM', 'Marvin Minsky', ['MIT, cofounder of the AI Lab,', 'Turing Award 1969'], AC2)
c2 += quote(439, 186, [[('Each of our major', False)], [('emotional states', True), (' results', False)], [('from turning certain', False)], [('resources on', True), (' while turning', False)], [('certain others off.', False)]], 15.5, 22)
c2 += T(752, 320, 'The Emotion Machine, 2006', 12, 400, MUT, 'end')
g += F(1, c2)
c3 = person(785, 50, w3, 282, 'leonard-meyer.jpg', 'LM', 'Leonard Meyer', ['Music theorist, University of', 'Chicago and Penn'], MU)
c3 += quote(817, 186, [[('affect is aroused when an', False)], [('expectation', True), (', a tendency to', False)], [('respond, is ', False), ('temporarily', True)], [('inhibited or permanently', True)], [('blocked', True)]], 15.5, 22)
c3 += T(1130, 320, 'Emotion and Meaning in Music, 1956, p. 31', 12, 400, MUT, 'end')
g += F(2, c3)
band = T(30, 356, 'Why this matters for a graph', 14, 700, MUT)
chain = [('music', 'a melody unfolds', MU, MUL), ('expectation', 'what comes next? a transition graph', ACC, ACL), ('emotion', 'dopamine at the peak, Salimpoor 2011', PURP, '#eef0ff'), ('brain response', 'measured in EEG, Di Liberto 2020', MU, MUL)]
for k, (a_, b_, col, fill) in enumerate(chain):
    x = 30 + k * 283
    band += R(x, 366, 262, 60, fill, col, 2, 14) + T(x + 16, 390, a_, 16.5, 700, col) + T(x + 16, 413, b_, 12.5, 400, INK)
    if k < 3:
        band += P(f'M{x+264},396 L{x+281},396', AC2, 2.5, extra='marker-end="url(#pea)"')
g += F(3, band)
g += F(4, T(590, 466, 'Music is one of the most measurable routes to emotion, so it is where a brain can judge a model.', 17, 700, INK, 'middle'))
EMOTION2 = sec('Music is where emotion can be measured', SVG(g), ch='0',
               ref='Picard, Affective Computing, MIT Press 1997, introduction. Minsky, The Emotion Machine, 2006. Meyer, Emotion and Meaning in Music, 1956, p. 31, via Margulis 2005. Huron, Sweet Anticipation, 2006. Salimpoor et al., Nature Neuroscience 2011. Koelsch, Nature Reviews Neuroscience 2014. Photos: Wikimedia Commons',
               notes='Step 2 of 2. Two AI pioneers say machines need emotion. A music theorist explains where musical emotion comes from: expectation that is held back or broken. Expectation is exactly what a note transition graph computes, and its effect is measurable in the brain. That is why music is the place where a brain can judge whether a model has a graph inside.')

# ======================= ASSEMBLY =======================
# ---- loop it1: results slide that pays off the trailer bars (P15, P10) ----
g = adefs('r20')
g += T(40, 34, '100 edits, all with perfect scores, 56 of them secretly bad. Check only 20. Bad edits found:', 16, 600, MUT)
def _bar20(k, who, n_, rate, col, bold=False):
    y = 66 + k * 72
    return T(40, y + 18, who, 18, 600 if bold else 400, INK) + R(40, y + 28, n_ * 30, 26, col, 'none', 0, 2) + T(52 + n_ * 30, y + 48, str(n_), 20, 600, INK) + T(110 + n_ * 30, y + 48, f'{rate}% of checks bad', 14, 400, MUT)
g += _bar20(0, 'at random', 11, 56, '#ACA39A') + _bar20(1, 'by editor and model', 14, 70, '#ACA39A')
g += F(1, _bar20(2, 'by the delta graph', 17, 86, ACC, True))
box = ''
for k, (big, a, b) in enumerate([('0.703 to 0.797', 'ranking quality (AUC), editor and model only,', 'then with the delta graph'), ('0.853 to 0.904', 'second dataset (wiki_recent), 500 real', 'Wikipedia facts, the same pattern')]):
    x = 40 + k * 560
    box += R(x, 300, 540, 96, SOFT, 'none', 0, 3) + T(x + 20, 346, big, 30, 400, INK, extra='font-family="et-book,Georgia,serif" style="font-size-adjust:none"') + T(x + 250, 336, a, 14, 400, MUT) + T(x + 250, 358, b, 14, 400, MUT)
g += F(2, box)
g += F(3, T(590, 452, 'Next: is it the size of the change, or its shape?', 19, 700, INK, 'middle'))
RES20 = sec('Results: same checking budget, more bad edits caught', SVG(g), ch='1', status='pub',
            ref='Benbrahim et al., SDM 2026, Tables 5.1 to 5.5. Counts are the expected bad edits among 20 checks at the reported rates',
            notes='The same three bars as the trailer, now with the method behind them. Do not ask the room to guess, they saw 17 at minute 3. Say instead: these are the bars from the start of the talk, now you know what the orange one measures. Then click to 17. The rates are what the paper reports: 56 percent at random, 70 by editor and model, 86 with the delta graph. Ranking quality goes from 0.703 to 0.797, and on a second dataset of real Wikipedia facts from 0.853 to 0.904.')

# ---- loop it1: one slide for the vector evidence (P03) ----
import random as _r3
g = adefs('vv')
g += T(40, 34, 'Refusal in 13 chat models', 16, 600, MUT)
g += T(40, 92, 'normal model', 16, 400, INK) + R(240, 74, 260, 26, AC2, 'none', 0, 2) + T(510, 92, 'refuses', 15, 400, MUT)
g += T(40, 150, 'one direction removed', 16, 600, '#C45200') + R(240, 132, 14, 26, ACC, 'none', 0, 2) + T(264, 150, 'almost never refuses', 15, 600, '#C45200')
g += T(40, 196, 'difference of means at one layer, removed everywhere', 13.5, 400, MUT)
sc = T(620, 34, 'One steering vector, applied to single inputs', 16, 600, MUT)
_r3.seed(3)
for v in [_r3.gauss(1.2, 1.6) for _ in range(46)]:
    x = 880 + v * 52; y = 150 - _r3.uniform(0, 80)
    sc += C(round(x), round(y), 5, ACC if v > 0 else AC2, extra='opacity=".8"')
sc += L(620, 170, 1150, 170, INK, 1.5) + L(880, 60, 880, 176, '#DA291C', 1.5, 'stroke-dasharray="5 4"') + T(880, 194, '0: no effect', 13, 600, '#DA291C', 'middle')
sc += P(f'M{880+1.2*52},56 L{880+1.2*52},170', ACC, 2.5) + T(880 + 1.2 * 52 + 8, 66, 'average: it works', 14, 600, '#C45200')
sc += T(620, 194, 'moved the opposite way', 13, 400, MUT) + T(1150, 194, 'moved as intended', 13, 400, MUT, 'end')
g += F(1, sc)
g += F(2, R(40, 250, 1110, 110, SOFT, 'none', 0, 3) + T(590, 296, 'A vector works on average and fails on many single inputs.', 21, 400, INK, 'middle', extra='font-family="et-book,Georgia,serif" style="font-size-adjust:none"') + T(590, 330, 'Our reading: a detector cannot be the vector we added. It has to look at what the vector did to the rest of the network.', 15, 600, '#C45200', 'middle'))
VEC2 = sec('A vector switches a behavior on average, and fails on many single inputs', SVG(g), ch='1',
           ref='Arditi et al., Refusal in Language Models Is Mediated by a Single Direction, NeurIPS 2024, Figure 1 (redrawn). Tan et al., Analysing the Generalisation and Reliability of Steering Vectors, NeurIPS 2024 (schematic)',
           notes='Two results side by side. Arditi: in 13 chat models, one direction found by a difference of means at one layer controls refusal, remove it and the model stops refusing. Tan: the same kind of vector, applied input by input, sends a large share of inputs the opposite way, on many datasets close to half. The bridge is our reading, not their claim: if the vector itself is unreliable per input, the signal for a bad change has to come from what the change did to the rest of the network.')

def backup(sec_html):
    """a backup slide: stacked under the slide before it (down arrow), not counted in the main run"""
    sec_html = re.sub(r'<section( class="([^"]*)")?', lambda m: '<section class="backup ' + (m.group(2) or '') + '"', sec_html, count=1)
    if 'class="status' in sec_html:
        return re.sub(r'(<span class="status [^"]*">)', r'\1Backup, ', sec_html, count=1)
    return sec_html.replace('</h2>', '</h2><span class="status plan">Backup</span>', 1)

_fb = lambda sec_, line: sec_.replace('<aside class="notes">', '<aside class="notes">If sound fails: ' + line + ' ', 1)
DEMO2 = _fb(DEMO2, 'skip the click, point at the arrows, and say the ball walks the graph, one move per note.')
FOLD = _fb(FOLD, 'say what the second clip would show: the right notes in the wrong sentences, it sounds like Für Elise in pieces.')
COPY = _fb(COPY, 'skip the vote. Say B is the real Bach, A comes from the 2 note graph, and that the vote is a pilot of the listening test. Move on.')

def assemble(cover, old):
    """old: the reused slides from the earlier deck, keyed by their old index"""
    def bridge(sec_, line):
        return sec_.replace('</aside>', ' Bridge out: ' + line + '</aside>', 1) if '</aside>' in sec_ else sec_.replace('</section>', '  <aside class="notes">Bridge out: ' + line + '</aside>\n</section>', 1)
    surg = retitle(old[3].replace(' The map next.', '').replace('>CEO of Apple is<', '>Space Needle is in<').replace('>Steve Jobs<', '>Seattle<').replace('>Tim Cook<', '>Paris<'), 'A released model is not left alone. Seven kinds of surgery.')
    story = retitle(old[43], 'After release, every change is checked by an exam that only reads answers')
    story = re.sub(r'\s*<p class="q"[^>]*>.*?</p>', '', story, count=1, flags=re.S)
    story = story.replace('  <aside class="notes">', '  <div class="ref">Receipts (down arrow): Yang 2025, editing. Hu 2025, unlearning. Hammoud 2024, merging. Shrestha 2026, pruning</div>\n  <aside class="notes">', 1)
    story = story.replace('Everything else is detail on it.', 'Everything else is detail on it. If asked for evidence, press down for the four receipts. Bridge to the next slide: let me show you the quietest of these failures, the one in editing.')
    receipts = (old[45].replace('38.5% when it writes freely', '38.5% under realistic evaluation (WILD)')
                .replace('on harmless general text and the original comes back word for word', 'on related Wikipedia text and the original comes back word for word')
                .replace('A safe chemistry expert averaged with an unsafe math expert passes every capability benchmark and inherits the unsafe behavior', 'Merging domain experts also merges their misalignment: the merged model inherits unsafe behavior')
                .replace('A quarter of the layers removed and repaired: classification keeps 80 to 90%, math and code generation drop hard and do not come back', 'Layers removed and repaired: classification recovers up to 90%, generation and arithmetic stay broken'))
    delta_paper = retitle(old[47], 'Our delta graph: rank edits by how the inside rewired').replace('class="divider" ', '', 1)
    toch = lambda sec_, c: re.sub(r'data-ch="[^"]*"', f'data-ch="{c}"', sec_, count=1)
    vector = retitle(VECTOR, 'Every change to a model is stored as a vector')
    # trailer: the problem, the thesis, one best result per domain, the two claims
    vector = retitle(vector, 'Yet every change to a model is applied as a vector')
    # per domain: the structure is a graph, our graph sees the problem, yet the field uses vectors
    vision = [cover, KGT, DELTA_T, vector, DEMO2, MSTEER, FORECAST2]
    rome = old[33]
    a = rome.find('<div class="note"'); e = rome.find('  <div class="ref">')
    rome = rome[:a] + '<div class="note" style="font-size:.62em"><div class="key">The finding</div><p class="one" style="font-size:1.25em">A fact sits in two places. Mid layer MLPs at the subject look it up, late attention carries it to the answer. Editing a fact means changing the first place.</p></div>\n  </div>\n' + rome[e:]
    rome = retitle(rome, 'A fact lives in mid layer MLPs and moves out by attention')
    d46 = old[46].replace('3. Before minus after', '3. After minus before').replace('running example from slide 45: the Space Needle edit', 'running example: the Space Needle edit').replace(' (slide 2).', '.')
    rome = retitle(rome, 'If not the vector, look where the fact lives')
    abl = old[50].replace('on 500 unseen facts, AUC 0.840 to 0.862.', 'trained on 200 facts, tested on 500 new ones, AUC 0.840 to 0.862.').replace('Same probes, same before/after difference, scored different ways (AUC on the 1,761 benchmark-perfect edits)', 'Same probes, same difference, scored different ways. Appendix run, Table F.1, so 0.705 and 0.798 here').replace('Also holds: on 500 unseen facts', 'Also holds when trained on 200 facts and tested on 500 unseen ones')
    for pat in (r'<text[^>]*>Table F\.1\.[^<]*</text>', r'<text[^>]*>total change 0\.575[^<]*</text>', r'<text[^>]*>best 0\.589: max edge change</text>'):
        abl = re.sub(pat, '', abl)
    abl = re.sub(r'(<aside class="notes">)(.*?)(</aside>)', lambda m: m.group(1) + m.group(2) + ' The five single numbers from Table F.1: max edge change 0.589, total change 0.575, top 5 node share 0.564, top 1 node share 0.521. The main text reports 0.703 and 0.797 for the same experiment, Table F.1 gives 0.705 and 0.798.' + m.group(3), abl, count=1, flags=re.S) if '<aside class="notes">' in abl else notes(abl, 'The five single numbers from Table F.1: max edge change 0.589, total change 0.575, top 5 node share 0.564, top 1 node share 0.521.')
    _l = old[51]; _a = _l.find('<rect x="596" y="0" width="287" height="382"'); _b = _l.find('</g><g class="fragment" data-fragment-index="2">')
    lim_main = _l[:_a] + '<text x="915" y="150" font-size="17" font-weight="700" fill="#1F1E1B" text-anchor="middle">Two more under the down arrow:</text><text x="915" y="182" font-size="15" fill="#5F5D50" text-anchor="middle">checking 20% catches about a third of all bad edits</text><text x="915" y="208" font-size="15" fill="#5F5D50" text-anchor="middle">and on CounterFact there is nothing to catch</text>' + _l[_b:]
    lim_main = lim_main.replace('</section>', '  <aside class="notes">Two limits on screen, two more under the down arrow if asked. Say the Llama one plainly: when almost every passing edit fails, there is little left to rank.</aside>\n</section>', 1) if '<aside' not in lim_main else lim_main
    vec2_b = bridge(VEC2, 'If not the vector, look where the fact lives. Causal tracing (Meng et al.) finds a fact in mid layer MLPs at the subject, the figure is under the down arrow on the next slide. The next slide shows why that is still not where editing works.')
    d46_q = bridge(d46, 'Nearest 2026 cousin, if asked: Circuit-Diff (Friedman and Song, arXiv 2609.23892, Sep 2026) also compares attribution graphs before and after a factual edit, but to label features, not to rank which edits went wrong. If asked how a partial correlation over 64 blocks is estimated from 12 prompts: it is not well posed alone, ridge with one fixed lambda shapes the graph, which is why the paper leans on held out evidence. Hard question to expect: is the delta graph real, or an artifact of the 12 probe prompts? Three answers from the paper. The probe prompts are disjoint from the prompts that define failure. Trained on 200 facts and tested on 500 new ones, the AUC holds at 0.840 to 0.862. Rerun the 50 riskiest edits from scratch and only 2 of 50 flip.')
    silent_b = bridge(toch(SILENT, '1'), 'And the usual fix, a vector, is unreliable too: it switches a behavior on average but sends many single inputs the wrong way (Tan et al., under the down arrow). So instead of the vector, look where the fact lives, which the next slide does.')
    lang = [DIV1, CGT, backup(CGT4), toch(story, '1'), backup(toch(surg, '1')), backup(toch(receipts, '1')), silent_b, backup(vec2_b), old[35].replace('The first crack: where a fact lives is not where editing works', 'Where a fact lives is not where editing works').replace('(numbers illustrative)', '(numbers illustrative. Causal tracing: corrupt the input, restore one layer)').replace('Each grey dot is one fact. Hase 2023: correlation about zero (minus 0.13).', 'Schematic, each grey dot one fact. Hase 2023 measured a correlation of about zero (minus 0.13).').replace('Guo 2025, slide 31', 'Guo 2025').replace('So an edit can land where the knowledge is not, and its side effects can land where nobody looks.', 'Mechanism still matters: choosing where to change by it makes forgetting stick (Guo 2025).').replace('But choosing where to change by mechanism makes forgetting stick (Guo 2025).', 'So instead of asking where a fact lives, we read what the edit did to the connections.'), backup(rome), d46_q, backup(old[48]), RES20, abl, bridge(lim_main, 'That is the graph inside a language model, published, with its limits. The title says generative models, plural. Text is one kind of knowledge a model holds, and the next part asks whether the same question survives in knowledge that is not words.'), backup(retitle(old[51], 'Limits, all four, with the numbers'))]
    four = retitle(FOUR, 'Music generation went from a visible graph to a hidden one')
    four = re.sub(r'\s*<p class="q">.*?</p>', '', four, count=1, flags=re.S)
    tools = retitle(TOOLS, 'Every tool inside MusicGen reads one layer at one moment').replace('Three tools, three questions, all at one layer and one moment.', 'Language models moved on to attribution graphs. Music has not.')
    b1 = retitle(BRAIN1, 'Listeners\' brains track a Markov model\'s surprise, note by note')
    b1 = b1.replace(ph(60, 230, 400, 140, 'Original figure: Di Liberto et al. 2020', 'eLife, to add when the site is reachable'),
                    R(60, 230, 400, 140, ACL, ACC, 1.5, 10) + T(80, 270, 'The listener model is a graph', 17, 700, ACC) + T(80, 300, 'IDyOM counts transitions between notes', 14.5, 400, INK) + T(80, 324, 'with several context lengths, like the', 14.5, 400, INK) + T(80, 348, 'tiny graph from the opening.', 14.5, 400, INK))
    b2 = retitle(BRAIN2, 'The brain carries enough of the music to rebuild it').replace('Denk et al., Brain2Music, arXiv 2307.11078, 2023.', 'Denk et al., Text to music generation models capture musical semantic representations in the human brain, Nature Communications 2025 (Brain2Music).')
    corpus = retitle(CORPUS, 'Occam\'s razor: the simplest graph already names the tradition')
    path = retitle(PATH, 'Too little memory gives a graph without syntax, too much gives a path').replace('An 89 note Bach chorale at first and third order.', 'An 89 note Bach chorale at first and third order. LLM judge result from zhiqian.ai/music-markov')
    beyond2 = retitle(toch(BEYOND2, '2'), 'Part 2. Knowledge is not only text')
    hist = retitle(HIST, 'The oldest music model is a graph')
    bri = retitle(BRI, 'A note transition graph predicts the listening brain')
    lang[1] = bridge(lang[1], 'That was the graph outside the model, a record we can draw. The harder case is a change made inside the model, where nobody drew the graph.')
    musres_b = bridge(toch(MUSRES, '2'), 'So inside MusicGen, steering is lopsided, and a vector cannot say why. To test any graph we draw inside, we need a judge outside the model. In music that judge exists: a listener\'s brain.')
    emo_b = bridge(toch(EMOTION2, '2'), 'If emotion lives in expectation, the first question is what a listener expects. The oldest answer is a graph: in 1957 a Markov chain already wrote a string quartet, and IDyOM, the listener model we meet later, is its descendant (history under the down arrow).')
    copy_b = bridge(COPY, 'Before we go inside a generator, one honest line from the literature: in music, graphs win only when the edges carry something the sequence throws away, and often they do not (survey under the down arrow). The one place nobody has looked for such edges is inside the generator itself.')
    corpus_b = bridge(corpus, 'How much memory should the graph have? One note gives the right vocabulary with the wrong syntax, three notes memorize the piece (the picture is under the down arrow on the next slide).')
    mus = [beyond2, emo_b, backup(hist), FOLD, corpus_b, RICHER, backup(path), copy_b, backup(WHEN), PROBE, backup(MGEN), musres_b, bri, backup(BRL), backup(BRR), PLAN, backup(BRG)]
    beyond = []
    close = [TAKEAWAY.replace('</section>', CLIP_JSON + '</section>')]
    parts = {'vision': vision, 'language': lang, 'music': mus, 'beyond': beyond, 'close': close}
    return parts
