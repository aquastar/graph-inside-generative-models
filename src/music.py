import math, random
INK = '#111'; MUT = '#5b6770'; ACC = '#F76902'; AC2 = '#4C5B66'; MU = '#1f8a9a'; LINE = '#d3d7da'; SOFT = '#f2f3f4'; MUL = '#e6f5f7'; ACL = '#fff1e6'

def T(x, y, s, size=14, w=400, fill=INK, a='start', extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}" {extra}>{s}</text>'

def R(x, y, w, h, fill='#fff', stroke=LINE, sw=1.5, rx=6, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def C(x, y, r, fill=INK, stroke='none', sw=1.5, extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def L(x1, y1, x2, y2, stroke=LINE, sw=1.5, extra=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def P(d, stroke=INK, sw=2, fill='none', extra=''):
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" {extra}/>'

def F(i, inner):
    return f'<g class="fragment" data-fragment-index="{i}">{inner}</g>'

def chip(x, y, s, fill=SOFT, color=AC2, size=13, w=None):
    w = w or (len(s) * size * 0.56 + 22)
    return R(x, y, w, 26, fill, LINE, 1, 13) + T(x + w / 2, y + 17.5, s, size, 600, color, 'middle')

def defs(pfx):
    out = '<defs>'
    for name, col in (('a', AC2), ('o', ACC), ('t', MU), ('k', INK), ('g', '#9aa6ae')):
        out += f'<marker id="{pfx}{name}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>'
    out += f'<radialGradient id="{pfx}gl"><stop offset="0" stop-color="{ACC}" stop-opacity=".5"/><stop offset="1" stop-color="{ACC}" stop-opacity="0"/></radialGradient>'
    out += f'<radialGradient id="{pfx}gt"><stop offset="0" stop-color="{MU}" stop-opacity=".45"/><stop offset="1" stop-color="{MU}" stop-opacity="0"/></radialGradient>'
    return out + '</defs>'

def SVG(inner, h=478):
    return f'<svg viewBox="0 0 1180 {h}" style="width:100%;max-width:1160px;height:auto;max-height:{h}px;display:block;margin:0 auto">{inner}</svg>'

def sec(title, svg, ch='5', status='', ref='', cls='', notes='', q='', take=''):
    st = {'pub': '<span class="status published">Published</span>', 'rev': '<span class="status review">Under review</span>', 'acc': '<span class="status published">Accepted, CIKM 2026</span>',
          'prog': '<span class="status progress">In progress</span>', 'open': '<span class="status open">Open question</span>'}.get(status, '')
    c = f' class="{cls}"' if cls else ''
    out = f'<section{c} data-ch="{ch}">\n  <h2>{title}</h2>{st}\n'
    if q: out += f'  <p class="q">{q}</p>\n'
    out += '  ' + svg + '\n'
    if take: out += f'  <div class="takeaway">{take}</div>\n'
    if ref: out += f'  <div class="ref">{ref}</div>\n'
    if notes: out += f'  <aside class="notes">{notes}</aside>\n'
    return out + '</section>'

def mini_lattice(x0, y0, cols=4, rows=4, dx=34, dy=26, col='#b8c0c6', op=.5):
    out = ''; pts = []
    for i in range(cols):
        for j in range(rows):
            pts.append((x0 + i * dx, y0 + j * dy))
    for i in range(cols - 1):
        for j in range(rows):
            for k in range(rows):
                out += L(x0 + i * dx, y0 + j * dy, x0 + (i + 1) * dx, y0 + k * dy, col, 1, f'stroke-opacity="{op*0.5}"')
    for (x, y) in pts:
        out += C(x, y, 4, '#fff', col, 1.5)
    return out

S = []

# ---------- M0 divider ----------
g = defs('m0')
xs = [150, 440, 730, 1020]
labels = [('1957', 'the graph IS', 'the generator'), ('2019', 'the graph describes', 'the score'), ('2023', 'the graph disappears', 'into a network'), ('now', 'read the graph', 'back out?')]
cols = [AC2, AC2, AC2, MU]
g += L(60, 370, 1120, 370, LINE, 3)
for i, (x, (yr, a, b)) in enumerate(zip(xs, labels)):
    inner = C(x, 370, 9, cols[i]) + T(x, 405, yr, 18, 700, cols[i], 'middle') + T(x, 432, a, 15, 600, INK, 'middle') + T(x, 452, b, 15, 400, MUT, 'middle')
    if i == 0:
        nodes = [(x - 60, 240), (x, 190), (x + 60, 240), (x, 290)]
        pic = ''.join(P(f'M{a[0]},{a[1]} L{b[0]},{b[1]}', AC2, 2) for a, b in [(nodes[0], nodes[1]), (nodes[1], nodes[2]), (nodes[2], nodes[3]), (nodes[3], nodes[0]), (nodes[0], nodes[2])])
        pic += ''.join(C(px, py, 11, '#fff', AC2, 2.5) for px, py in nodes)
        pic += ''.join(T(px, py + 5, n, 13, 700, AC2, 'middle') for (px, py), n in zip(nodes, 'CEGA'))
        pic += C(0, 0, 7, ACC, extra='') .replace('/>', f'><animateMotion dur="4s" repeatCount="indefinite" path="M{nodes[0][0]},{nodes[0][1]} L{nodes[1][0]},{nodes[1][1]} L{nodes[2][0]},{nodes[2][1]} L{nodes[3][0]},{nodes[3][1]} Z"/></circle>')
    elif i == 1:
        pic = ''.join(L(x - 90, 200 + k * 14, x + 90, 200 + k * 14, '#9aa6ae', 1) for k in range(5))
        notes = [(x - 65, 256), (x - 30, 242), (x + 5, 228), (x + 40, 242), (x + 75, 214)]
        pic += ''.join(P(f'M{a[0]},{a[1]} Q{(a[0]+b[0])/2},{min(a[1],b[1])-28} {b[0]},{b[1]}', ACC, 2, extra='stroke-dasharray="4 3"') for a, b in zip(notes, notes[1:]))
        pic += ''.join(f'<ellipse cx="{nx}" cy="{ny}" rx="8" ry="6" fill="{INK}"/>' for nx, ny in notes)
    elif i == 2:
        pic = mini_lattice(x - 80, 195, 5, 4, 40, 28)
    else:
        pic = mini_lattice(x - 80, 195, 5, 4, 40, 28)
        path = [(x - 80, 223), (x - 40, 251), (x, 223), (x + 40, 279), (x + 80, 251)]
        pic += P('M' + ' L'.join(f'{a},{b}' for a, b in path), MU, 3.5)
        pic += ''.join(C(a, b, 6, MU) for a, b in path)
        pic += T(x + 60, 195, '?', 34, 700, MU, 'middle')
    g += F(i + 1, pic + inner) if i else pic + inner
g += T(590, 40, 'Four stages of graphs in music generation', 20, 600, INK, 'middle')
S.append(sec('5. Music: where does a style live?', SVG(g), cls='divider',
             q='Language models store facts. Music models store styles.',
             ref='Hiller and Isaacson 1957. Pachet 2003. Pachet and Roy 2011. Jeong et al. 2019. Copet et al. 2023'))

# ---------- M1 2017 genre fusion ----------
g = defs('m1')
g += f'<ellipse cx="200" cy="230" rx="130" ry="110" fill="{ACL}" stroke="{ACC}" stroke-width="2"/>' + T(200, 140, 'Genre A', 18, 700, ACC, 'middle')
g += f'<ellipse cx="980" cy="230" rx="130" ry="110" fill="{MUL}" stroke="{MU}" stroke-width="2"/>' + T(980, 140, 'Genre B', 18, 700, MU, 'middle')
for k in range(9):
    random.seed(k)
    g += C(150 + random.uniform(0, 100), 190 + random.uniform(0, 90), 5, ACC, extra='opacity=".6"')
    g += C(930 + random.uniform(0, 100), 190 + random.uniform(0, 90), 5, MU, extra='opacity=".6"')
g += R(470, 120, 240, 60, '#fff', AC2, 2, 8) + T(590, 157, 'generator A to B', 16, 600, AC2, 'middle')
g += R(470, 280, 240, 60, '#fff', AC2, 2, 8) + T(590, 317, 'generator B to A', 16, 600, AC2, 'middle')
g += P('M330,200 C390,150 430,150 470,150', AC2, 2.5, extra='marker-end="url(#m1a)"') + P('M710,150 C760,150 800,170 850,200', AC2, 2.5, extra='marker-end="url(#m1a)"')
g += P('M850,265 C800,300 760,310 710,310', AC2, 2.5, extra='marker-end="url(#m1a)"') + P('M470,310 C430,310 390,300 330,265', AC2, 2.5, extra='marker-end="url(#m1a)"')
g += T(590, 225, 'dual learning: each checks the other', 14, 400, MUT, 'middle')
fus = f'<ellipse cx="590" cy="420" rx="120" ry="34" fill="url(#m1gl)" stroke="{ACC}" stroke-width="2" stroke-dasharray="6 4"/>' + T(590, 426, 'A and B fused', 17, 700, INK, 'middle')
g += F(1, fus + P('M590,340 L590,382', ACC, 2.5, extra='marker-end="url(#m1o)"'))
q = R(760, 395, 380, 56, '#fff', INK, 2, 8) + T(950, 420, 'But where does a style live', 16, 700, INK, 'middle') + T(950, 441, 'inside the generator?', 16, 700, INK, 'middle')
g += F(2, q + P('M760,420 C735,420 720,345 712,335', INK, 2, extra='marker-end="url(#m1k)" stroke-dasharray="5 4"'))
S.append(sec('Where I started: fusing two genres (2017)', SVG(g), status='pub',
             ref='Chen, Wu, Lu, Lerch, Lu, Learning to Fuse Music Genres with Generative Adversarial Dual Learning, ICDM 2017',
             notes='Trained a generator to blend genres. It could not tell us where a style lives inside the generator. Nine years later, the question flips.'))

# ---------- M2 Markov music ----------
g = defs('m2')
nodes = {'C': (180, 250), 'D': (320, 140), 'E': (470, 250), 'G': (320, 360), 'A': (610, 140), 'B': (610, 360)}
edges = [('C', 'D', .5), ('D', 'E', .7), ('E', 'G', .4), ('G', 'C', .6), ('C', 'E', .3), ('E', 'A', .5), ('A', 'B', .4), ('B', 'E', .5), ('G', 'B', .3), ('D', 'A', .2)]
for a, b, p in edges:
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    g += L(x1 + ux * 28, y1 + uy * 28, x2 - ux * 30, y2 - uy * 30, '#9aa6ae', 1 + p * 4, f'marker-end="url(#m2g)" id="e{a}{b}"')
    g += T((x1 + x2) / 2 + uy * 14, (y1 + y2) / 2 - ux * 14 + 5, f'{p:.1f}', 12, 600, MUT, 'middle')
for n, (x, y) in nodes.items():
    g += C(x, y, 26, '#fff', AC2, 2.5) + T(x, y + 7, n, 20, 700, AC2, 'middle')
walk = ['C', 'D', 'E', 'A', 'B', 'E', 'G', 'C']
pd = 'M' + ' L'.join(f'{nodes[n][0]},{nodes[n][1]}' for n in walk)
g += f'<circle r="11" fill="{ACC}"><animateMotion dur="7s" repeatCount="indefinite" path="{pd}"/></circle>'
g += T(395, 445, 'states are notes, edges are transition probabilities, a walk is a melody', 15, 400, MUT, 'middle')
right = R(770, 70, 380, 120, SOFT, LINE, 1, 8) + T(790, 100, '1957  Illiac Suite', 16, 700, AC2) + T(790, 124, 'Hiller and Isaacson draw notes', 14, 400, INK) + T(790, 144, 'from Markov chains', 14, 400, INK)
right += T(790, 172, 'first computer composed score', 13, 400, MUT)
g += right
c2 = R(770, 205, 380, 100, SOFT, LINE, 1, 8) + T(790, 235, '2003  The Continuator', 16, 700, AC2) + T(790, 259, 'Pachet learns a player\'s style live', 14, 400, INK) + T(790, 279, 'and continues the phrase', 14, 400, INK)
g += F(1, c2)
c3 = R(770, 320, 380, 120, ACL, ACC, 1.5, 8) + T(790, 350, '2011  Markov constraints', 16, 700, ACC) + T(790, 374, 'Pachet and Roy: force the walk to', 14, 400, INK) + T(790, 394, 'satisfy constraints, keep the style', 14, 400, INK) + T(790, 424, 'control = which states are reachable', 14, 700, ACC)
blockB = C(nodes['B'][0], nodes['B'][1], 34, 'none', ACC, 3, 'stroke-dasharray="5 4"') + T(nodes['B'][0] + 46, nodes['B'][1] + 5, 'end here', 13, 700, ACC)
g += F(2, c3 + blockB)
S.append(sec('When the graph was the generator', SVG(g),
             ref='Hiller and Isaacson, Experimental Music, 1959. Pachet, The Continuator, JNMR 2003. Pachet and Roy, Markov Constraints: Steerable Generation of Markov Sequences, Constraints 2011',
             notes='When the graph is visible, control is exact. You can ask which states are reachable and constrain the walk.'))

# ---------- M3 score as graph ----------
g = defs('m3')
sx, sy = 70, 120
for k in range(5):
    g += L(sx, sy + k * 16, sx + 460, sy + k * 16, '#9aa6ae', 1.2)
ns = [(110, 176), (180, 168), (250, 160), (250, 128), (330, 152), (400, 144), (470, 168)]
for i, (x, y) in enumerate(ns):
    g += f'<ellipse cx="{x}" cy="{y}" rx="10" ry="7.5" fill="{INK}"/>' + L(x + 9, y, x + 9, y - 46, INK, 2)
g += T(300, 92, 'a score', 16, 700, INK, 'middle')
gr = ''
gx = [(700, 170), (790, 130), (880, 100), (880, 190), (970, 140), (1060, 120), (1100, 200)]
pairs = [(0, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (4, 6)]
for a, b in pairs:
    gr += L(gx[a][0], gx[a][1], gx[b][0], gx[b][1], ACC, 2.5)
gr += ''.join(C(x, y, 11, '#fff', ACC, 2.5) for x, y in gx)
gr += T(900, 260, 'notes become nodes, onset, sequence and', 14, 400, MUT, 'middle') + T(900, 280, 'chord relations become edges', 14, 400, MUT, 'middle')
gr += P('M545,150 L650,150', ACC, 3, extra='marker-end="url(#m3o)"')
g += F(1, gr)
works = [('Jeong 2019', 'performance'), ('PopMNet 2020', 'melody'), ('Karystinaios 2022', 'cadences'), ('MELONS 2022', 'long melody'), ('Polyphemus 2023', 'multitrack'), ('Lim 2024', 'pop songs'), ('SMUG-explain 2024', 'explanations')]
wk = ''
x = 40
for i, (n, u) in enumerate(works):
    w = 150
    wk += R(x, 330, w, 64, SOFT, LINE, 1, 8) + T(x + w / 2, 356, n, 13.5, 700, AC2, 'middle') + T(x + w / 2, 378, u, 13, 400, MUT, 'middle')
    x += w + 8
g += F(2, wk + T(590, 440, 'The graph lives in the data. It tells us about the music, not about the model.', 17, 700, ACC, 'middle'))
S.append(sec('When the graph described the score', SVG(g),
             ref='Jeong et al., ICML 2019. Wu et al., 2020. Karystinaios and Widmer, ISMIR 2022. Zou et al., 2022. Cosenza et al., 2023. Lim, Liang, Zhang, 2024. Karystinaios et al., 2024'))

# ---------- M4 MusicGen ----------
g = defs('m4')
g += R(30, 190, 170, 70, '#fff', AC2, 2, 8) + T(115, 220, 'text prompt', 15, 700, AC2, 'middle') + T(115, 242, '"upbeat jazz piano"', 13, 400, MUT, 'middle')
g += P('M200,225 L250,225', AC2, 2.5, extra='marker-end="url(#m4a)"')
g += R(250, 190, 130, 70, '#fff', AC2, 2, 8) + T(315, 222, 'text', 15, 700, AC2, 'middle') + T(315, 242, 'encoder', 15, 700, AC2, 'middle')
g += P('M380,225 L430,225', AC2, 2.5, extra='marker-end="url(#m4a)"')
for k in range(8):
    g += R(430 + k * 6, 110 + k * 4, 200, 230 - k * 8, '#fff' if k < 7 else SOFT, '#9aa6ae', 1.2, 6)
g += T(560, 245, 'transformer', 16, 700, INK, 'middle') + T(560, 266, 'decoder', 16, 700, INK, 'middle')
g += P('M690,225 L740,225', AC2, 2.5, extra='marker-end="url(#m4a)"')
for r in range(4):
    for c in range(8):
        delay = c * 0.35 + r * 0.05
        g += f'<rect x="{745 + c * 26}" y="{170 + r * 26}" width="22" height="22" rx="3" fill="{AC2}" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{delay/4:.3f};{(delay+0.2)/4:.3f};0.92;1" dur="4s" repeatCount="indefinite"/></rect>'
g += T(848, 160, 'audio tokens, 4 codebooks', 14, 700, AC2, 'middle') + T(848, 290, 'discrete, one column per step', 13, 400, MUT, 'middle')
g += P('M960,225 L1000,225', AC2, 2.5, extra='marker-end="url(#m4a)"')
wave = 'M1005,225 ' + ' '.join(f'L{1005 + i * 4},{225 + 30 * math.sin(i * 0.9) * math.exp(-((i - 18) / 14) ** 2)}' for i in range(40))
g += P(wave, MU, 2.5)
hid = f'<rect x="420" y="96" width="290" height="268" rx="10" fill="url(#m4gt)" stroke="{MU}" stroke-width="3" stroke-dasharray="7 5"/>'
hid += T(565, 395, 'hidden activations: continuous, high dimensional', 16, 700, MU, 'middle') + T(565, 418, 'this is where a style must live', 15, 400, INK, 'middle')
g += F(1, hid)
g += F(2, T(590, 460, 'No explicit graph anywhere. Every tool so far reads vectors here.', 17, 700, ACC, 'middle'))
S.append(sec('Then the graph disappeared: MusicGen', SVG(g),
             ref='Copet et al., Simple and Controllable Music Generation, NeurIPS 2023. Défossez et al., High Fidelity Neural Audio Compression, 2022'))

# ---------- M5 probing ----------
g = defs('m5')
for k in range(6):
    y = 70 + k * 62
    g += R(60, y, 200, 46, '#fff' if k != 3 else MUL, '#9aa6ae' if k != 3 else MU, 1.5 if k != 3 else 2.5, 6) + T(160, y + 29, f'layer {6 - k}', 14, 600, MUT if k != 3 else MU, 'middle')
g += P('M260,279 L360,250', MU, 2.5, extra='marker-end="url(#m5t)"')
random.seed(3)
pts = ''
for i in range(26):
    x = random.uniform(400, 700); y = random.uniform(90, 400)
    side = (y - 90) > (x - 400) * 1.0 + 20
    pts += C(x, y, 7, ACC if side else MU, extra='opacity=".85"')
g += R(380, 70, 340, 350, '#fff', LINE, 1.5, 8) + pts
g += T(550, 445, 'activations at one layer', 14, 400, MUT, 'middle')
g += F(1, P('M400,110 L720,430', INK, 3, extra='stroke-dasharray="9 6"') + chip(560, 80, 'C major', ACL, ACC) + chip(400, 380, 'A minor', MUL, MU))
plot = R(780, 80, 360, 260, '#fff', LINE, 1.5, 8) + L(810, 310, 1120, 310, INK, 1.5) + L(810, 310, 810, 100, INK, 1.5)
curve = 'M815,290 C880,280 920,140 980,130 S1080,210 1115,250'
plot += P(curve, ACC, 3.5) + T(965, 335, 'layer', 13, 400, MUT, 'middle') + T(795, 205, 'decodable', 13, 400, MUT, 'middle', 'transform="rotate(-90 795 205)"')
plot += T(960, 108, 'schematic', 12, 600, MUT, 'middle')
g += F(2, plot + T(960, 375, 'Concepts peak in middle layers', 15, 700, INK, 'middle') + T(960, 398, 'tempo, notes, intervals, scales, chords', 14, 400, MUT, 'middle'))
g += F(3, T(960, 445, 'Readable is not controllable.', 17, 700, ACC, 'middle'))
S.append(sec('Inside, part 1: what can be read out?', SVG(g),
             ref='Castellon, Donahue, Liang, ISMIR 2021. Wei, Freeman, Donahue, Sun, Do Music Generation Models Encode Music Theory?, ISMIR 2024',
             notes='A linear probe separates concepts in one layer. Decodability depends on layer and model size, the smallest MusicGen often does best.'))

# ---------- M6 steering ----------
g = defs('m6')
band = 'M60,330 C250,250 450,300 650,220 S960,170 1120,150 L1120,250 C960,270 850,330 650,320 S250,360 60,420 Z'
g += P(band, 'none', 0, MUL) + T(1110, 140, 'where real music lives', 14, 700, MU, 'end')
x0, y0 = 300, 350
g += C(x0, y0, 10, INK) + T(x0, y0 + 32, 'current state', 14, 600, INK, 'middle')
step1 = P(f'M{x0},{y0} L{x0+140},{y0-80}', ACC, 4, extra='marker-end="url(#m6o)"') + C(x0 + 150, y0 - 86, 10, ACC) + T(x0 + 175, y0 - 70, 'small push: tempo up, still music', 14, 600, ACC)
g += F(1, step1)
step2 = P(f'M{x0},{y0} L{x0+420},{y0-260}', ACC, 4, extra='marker-end="url(#m6o)" stroke-dasharray="10 6"') + C(x0 + 430, y0 - 266, 10, '#fff', ACC, 3) + T(x0 + 450, y0 - 262, 'large push: off the music, audio breaks', 14, 600, ACC)
g += F(2, step2)
g += F(3, chip(60, 40, 'tempo and timbre, middle layers (2025)', SOFT, AC2) + chip(60, 76, 'notes and chords: accuracy 0.23 to 0.82 (ICLR 2026)', SOFT, AC2))
g += F(4, T(590, 465, 'One direction, one push. Strength is a knob with a cliff.', 17, 700, ACC, 'middle'))
S.append(sec('Inside, part 2: what can be pushed?', SVG(g),
             ref='Activation Patching for Interpretable Steering in Music Generation, arXiv 2504.04479. Zhao, Beaglehole, Berg-Kirkpatrick, McAuley, Novack, ICLR 2026',
             notes='Difference in means vectors control tempo and timbre, middle layers work best, large strength degrades audio. RFM probes steer notes and chords with prompt adherence nearly unchanged.'))

# ---------- M7 SAE ----------
g = defs('m7')
random.seed(7)
vals = [random.uniform(-1, 1) for _ in range(24)]
for i, v in enumerate(vals):
    g += R(60 + i * 14, 240 - max(v, 0) * 110, 10, abs(v) * 110, '#9aa6ae', 'none', 0, 2)
g += T(225, 390, 'one activation vector', 15, 700, INK, 'middle') + T(225, 412, 'dense, unreadable', 14, 400, MUT, 'middle')
g += P('M420,240 L520,240', AC2, 3, extra='marker-end="url(#m7a)"') + T(470, 225, 'SAE', 15, 700, AC2, 'middle')
feats = [('piano', ACC, .9), ('swing', ACC, .6), ('bright timbre', ACC, .5), ('no name yet', MU, .7)]
fe = ''
lit = {4: 0, 13: 1, 22: 2, 31: 3}
for i in range(40):
    x = 540 + i * 15
    if i in lit:
        n, col, h = feats[lit[i]]
        fe += R(x, 240 - h * 150, 11, h * 150, col, 'none', 0, 2) + T(x + 5, 255, n, 13, 700, col, 'end', f'transform="rotate(-40 {x+5} 255)"')
    else:
        fe += R(x, 236, 11, 4, '#d3d7da', 'none', 0, 1)
g += F(1, fe + T(840, 390, 'a few sparse features light up', 15, 700, INK, 'middle') + T(840, 412, 'some have no name in music theory', 14, 400, MU, 'middle'))
g += F(2, T(590, 460, 'A dictionary of musical directions. Still a list, not a map of how they connect.', 17, 700, ACC, 'middle'))
S.append(sec('Inside, part 3: what concepts exist?', SVG(g),
             ref='Singh, Cherep, Maes, Discovering and Steering Interpretable Concepts in Large Generative Music Models, arXiv 2505.18186. Paek, Zang, Yang, Leistikow, arXiv 2510.23802'))

# ---------- M8 every tool is a vector ----------
g = defs('m8')
tools = [('probe', 'is it encoded?'), ('steering vector', 'can we push it?'), ('sparse features', 'which concepts exist?')]
for i, (n, a) in enumerate(tools):
    x = 70 + i * 260
    g += R(x, 60, 230, 110, SOFT, LINE, 1, 8) + T(x + 115, 98, n, 17, 700, AC2, 'middle') + T(x + 115, 124, a, 14, 400, INK, 'middle')
    g += P(f'M{x+115},170 L{x+115},215', AC2, 2, extra='marker-end="url(#m8a)"')
g += R(70, 215, 750, 50, '#fff', AC2, 2, 8) + T(445, 247, 'all three look at one layer, one moment', 16, 700, AC2, 'middle')
seq = ''
for t in range(6):
    x = 120 + t * 130
    seq += C(x, 360, 18, '#fff', MU, 3) + T(x, 366, f't{t+1}', 13, 700, MU, 'middle')
    if t < 5:
        seq += P(f'M{x+20},360 L{x+108},360', '#9aa6ae', 2, extra='stroke-dasharray="5 5" marker-end="url(#m8g)"') + T(x + 65, 345, '?', 20, 700, ACC, 'middle')
seq += T(445, 420, 'missing: how states follow each other in time', 16, 700, ACC, 'middle')
g += F(1, seq)
llm = R(880, 60, 270, 205, ACL, ACC, 1.5, 8) + T(1015, 98, 'Language models', 17, 700, ACC, 'middle') + T(1015, 128, 'went from vectors', 14, 400, INK, 'middle') + T(1015, 148, 'to attribution graphs', 14, 400, INK, 'middle') + T(1015, 178, '(2025)', 13, 400, MUT, 'middle')
llm += mini_lattice(940, 195, 5, 2, 32, 26, ACC, .6)
g += F(2, llm + T(1015, 360, 'Music has not', 17, 700, MU, 'middle') + T(1015, 384, 'made that move yet', 17, 700, MU, 'middle'))
S.append(sec('Every tool so far is a vector', SVG(g),
             ref='Ameisen et al., Circuit Tracing: Revealing Computational Graphs in Language Models, Transformer Circuits 2025'))

# ---------- M9 reading a graph out ----------
g = defs('m9')
random.seed(11)
traj = []
centers = [(140, 180), (230, 300), (330, 160), (380, 320)]
for k in range(40):
    c = centers[(k // 3) % 4]
    traj.append((c[0] + random.uniform(-38, 38), c[1] + random.uniform(-32, 32), (k // 3) % 4))
tr = P('M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y, _ in traj), '#c9d0d5', 1.2)
g += tr + ''.join(C(x, y, 5, INK) for x, y, _ in traj)
g += T(260, 420, '1. activations, one per step', 15, 700, INK, 'middle')
pal = [ACC, MU, AC2, '#8a6d1f']
cl = ''.join(C(x, y, 6, pal[c]) for x, y, c in traj)
cl += ''.join(f'<ellipse cx="{c[0]}" cy="{c[1]}" rx="52" ry="46" fill="none" stroke="{pal[i]}" stroke-width="2" stroke-dasharray="5 4"/>' for i, c in enumerate(centers))
g += F(1, cl + T(260, 445, '2. cluster into states', 15, 700, INK, 'middle'))
gpos = [(720, 170), (850, 300), (980, 160), (1080, 310)]
ge = ''
for a, b, w in [(0, 1, 5), (1, 2, 5), (2, 3, 5), (3, 0, 4), (1, 0, 1.5), (2, 0, 1.5)]:
    (x1, y1), (x2, y2) = gpos[a], gpos[b]
    dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    off = 10 if a > b else -10
    ge += L(x1 + ux * 30 - uy * off, y1 + uy * 30 + ux * off, x2 - ux * 34 - uy * off, y2 - uy * 34 + ux * off, AC2, w, 'marker-end="url(#m9a)"')
ge += ''.join(C(x, y, 26, '#fff', pal[i], 3.5) for i, (x, y) in enumerate(gpos))
ge += P('M470,250 L620,250', ACC, 3, extra='marker-end="url(#m9o)"')
g += F(2, ge + T(900, 420, '3. count transitions: a directed graph', 15, 700, INK, 'middle'))
cites = chip(620, 40, 'Weiss et al. 2018: automata from RNNs') + chip(620, 74, 'Dong et al. 2020: probabilistic abstraction') + chip(620, 108, 'Markovian Circuit Tracing 2026: toy transformer', ACL, ACC)
g += F(3, cites + T(900, 460, 'Not yet done on a real music generator, to our knowledge.', 16, 700, ACC, 'middle'))
S.append(sec('Reading a graph out of a sequence model', SVG(g, 478),
             ref='Weiss, Goldberg, Yahav, ICML 2018. Dong et al., ASE 2020. Markovian Circuit Tracing for Transformer State Dynamics, arXiv 2605.20824 (preprint)'))

# ---------- M10 one way steering ----------
g = defs('m10')
def island(cx):
    return P(f'M{cx-150},300 C{cx-80},200 {cx+20},330 {cx+150},230', MU, 14, extra='stroke-linecap="round" stroke-opacity=".35"') + P(f'M{cx-150},300 C{cx-80},200 {cx+20},330 {cx+150},230', MU, 2.5)
g += R(40, 60, 530, 360, '#fff', LINE, 1.5, 8) + R(610, 60, 530, 360, '#fff', LINE, 1.5, 8)
g += T(305, 95, 'Remove a style', 19, 700, INK, 'middle') + T(875, 95, 'Add a style', 19, 700, INK, 'middle')
g += island(305) + island(875) + T(305, 360, 'a style: a thin set of trajectories', 14, 600, MU, 'middle') + T(875, 360, 'a style: a thin set of trajectories', 14, 600, MU, 'middle')
rm = f'<circle r="11" fill="{INK}"><animateMotion dur="3s" repeatCount="indefinite" path="M300,268 C300,220 300,180 300,140"/></circle>'
rm += P('M300,262 L300,150', ACC, 3, extra='marker-end="url(#m10o)"') + T(305, 400, '✓ leaves easily, still music', 17, 700, MU, 'middle')
g += F(1, rm)
ad = f'<circle r="11" fill="{INK}"><animateMotion dur="3s" repeatCount="indefinite" path="M800,150 C840,200 880,240 950,330"/></circle>'
ad += P('M800,150 L940,320', ACC, 3, extra='marker-end="url(#m10o)" stroke-dasharray="8 5"') + T(875, 400, '✗ the push misses the thin set', 17, 700, ACC, 'middle')
g += F(2, ad)
g += F(3, T(590, 460, 'Removing works. Adding fails. Tested on MusicGen small and medium.', 17, 700, INK, 'middle'))
S.append(sec('Our observation: steering a style is one way', SVG(g), status='rev',
             ref='Co-authored work under review', notes='Explanation: a style is not a direction but a thin set of trajectories. You can leave it easily, a push rarely lands on it.'))

# ---------- M11 Markov graph from data ----------
g = defs('m11')
random.seed(5)
comms = [((300, 230), ACC, 'style 1'), ((590, 200), MU, 'style 2'), ((880, 240), AC2, 'style 3')]
allp = []
for ci, ((cx, cy), col, nm) in enumerate(comms):
    ps = [(cx + 85 * math.cos(2 * math.pi * k / 7 + ci) * random.uniform(.5, 1), cy + 85 * math.sin(2 * math.pi * k / 7 + ci) * random.uniform(.5, 1)) for k in range(7)]
    allp.append(ps)
    ed = ''
    for i in range(7):
        for j in range(i + 1, 7):
            if random.random() < .55:
                ed += L(ps[i][0], ps[i][1], ps[j][0], ps[j][1], col, 1.8, 'stroke-opacity=".7"')
    nd = ''.join(C(x, y, 9, col) for x, y in ps)
    g += F(ci + 1, ed + nd + T(cx, cy + 140, nm, 16, 700, col, 'middle')) if ci else ed + nd + T(cx, cy + 140, nm, 16, 700, col, 'middle')
br = L(allp[0][1][0], allp[0][1][1], allp[1][4][0], allp[1][4][1], INK, 2, 'stroke-dasharray="5 4"') + L(allp[1][0][0], allp[1][0][1], allp[2][3][0], allp[2][3][1], INK, 2, 'stroke-dasharray="5 4"')
g += F(3, br + T(590, 420, 'dense inside a style, few edges between: styles look like islands', 17, 700, INK, 'middle'))
g += F(4, T(590, 455, 'Built from music data, not yet from inside the model', 15, 600, MUT, 'middle'))
S.append(sec('A graph over musical states, built from data', SVG(g), status='prog',
             notes='Nodes are musical states from the data, edges are transition frequencies. This suggests where to look. It does not yet show what the model does.'))

# ---------- M12 next experiment ----------
g = defs('m12')
steps = [('record', 'many clips per style,', 'middle layer, every step'), ('discretize', 'cluster activations', 'into a few hundred states'), ('connect', 'count transitions:', 'the hidden graph'), ('test', 'do styles form communities?', 'does steering reach them?')]
for i, (a, b, c) in enumerate(steps):
    x = 40 + i * 285
    blk = R(x, 90, 250, 150, SOFT if i < 3 else ACL, LINE if i < 3 else ACC, 1.5, 10) + C(x + 34, 124, 20, AC2 if i < 3 else ACC) + T(x + 34, 131, str(i + 1), 18, 700, '#fff', 'middle')
    blk += T(x + 64, 131, a, 19, 700, INK) + T(x + 20, 182, b, 14, 400, INK) + T(x + 20, 204, c, 14, 400, INK)
    if i < 3:
        blk += P(f'M{x+252},165 L{x+282},165', AC2, 2.5, extra='marker-end="url(#m12a)"')
    g += F(i, blk) if i else blk
ctr = chip(60, 300, 'control: same graph on output audio tokens') + chip(440, 300, 'control: shuffled style labels') + chip(720, 300, 'control: not just loudness or position')
g += F(4, ctr)
g += F(5, T(590, 400, 'If styles do not separate at this resolution, that is a result too:', 16, 700, INK, 'middle') + T(590, 426, 'style lives in finer geometry than clusters capture', 16, 400, MUT, 'middle'))
S.append(sec('Next: the graph inside MusicGen', SVG(g), status='prog'))

# ---------- M13 reachability ----------
g = defs('m13')
g += f'<ellipse cx="330" cy="240" rx="260" ry="170" fill="{SOFT}" stroke="{LINE}" stroke-width="2"/>' + T(330, 100, 'everything else', 18, 700, AC2, 'middle')
g += f'<ellipse cx="900" cy="240" rx="130" ry="85" fill="{MUL}" stroke="{MU}" stroke-width="3"/>' + T(900, 180, 'a style', 18, 700, MU, 'middle')
exits = ['M860,230 C760,150 600,150 460,180', 'M910,260 C780,360 600,360 420,300', 'M940,220 C820,90 560,80 300,150', 'M880,280 C740,420 420,420 260,320']
for k, d in enumerate(exits):
    g += P(d, AC2, 2, extra='marker-end="url(#m13a)" stroke-opacity=".6"')
    g += f'<circle r="8" fill="{MU}"><animateMotion dur="{2.2 + k*0.4:.1f}s" repeatCount="indefinite" path="{d}"/></circle>'
g += T(640, 60, 'many exits: removing a style is easy', 17, 700, AC2, 'middle')
ent = 'M380,240 C480,250 560,215 600,240 C640,265 700,250 760,236'
miss = f'<circle r="9" fill="{ACC}"><animateMotion dur="5s" repeatCount="indefinite" path="M300,250 C420,220 500,290 560,240 C620,200 650,300 700,280 C660,320 560,330 480,300 C400,270 330,280 300,250"/></circle>'
g += F(1, P(ent, ACC, 3, extra='stroke-dasharray="8 6" marker-end="url(#m13o)"') + miss + T(400, 445, 'few entrances: hard to find the way in', 17, 700, ACC, 'middle'))
g += F(2, R(840, 395, 320, 66, '#fff', INK, 2, 8) + T(1000, 423, 'time to enter >> time to leave', 17, 700, INK, 'middle') + T(1000, 445, 'a reachability fact, not a quirk', 14, 400, MUT, 'middle'))
S.append(sec('What a hidden graph would explain', SVG(g), status='open',
             notes='On a directed graph, the expected hitting time into an island from outside can be far larger than the time to leave it. If the graph inside MusicGen looks like this, one way steering follows.'))

# ================= closing =================
CL = []
g = defs('c1')
g += R(40, 50, 520, 330, '#fff', ACC, 2, 10) + T(300, 88, 'Language: across the model', 19, 700, ACC, 'middle')
g += mini_lattice(90, 130, 4, 4, 40, 34, '#b8c0c6') + T(150, 290, 'before', 13, 600, MUT, 'middle')
g += mini_lattice(330, 130, 4, 4, 40, 34, '#b8c0c6') + T(390, 290, 'after', 13, 600, MUT, 'middle')
g += P('M250,180 L300,180', ACC, 2.5, extra='marker-end="url(#c1o)"')
for (a, b), (c, d) in [((330, 130), (370, 198)), ((370, 198), (410, 164)), ((410, 164), (450, 232))]:
    g += L(a, b, c, d, ACC, 4)
g += T(300, 330, 'delta graph: catches edits that pass', 15, 600, INK, 'middle') + T(300, 352, 'their own test but break other behavior', 15, 600, INK, 'middle')
mus = R(620, 50, 520, 330, '#fff', MU, 2, 10) + T(880, 88, 'Music: across time', 19, 700, MU, 'middle')
for t in range(6):
    x = 680 + t * 80
    mus += C(x, 200 + (30 if t % 2 else -20), 16, '#fff', MU, 3)
    if t < 5:
        mus += P(f'M{x+16},{200 + (30 if t % 2 else -20)} L{x+64},{200 + (-20 if t % 2 else 30)}', MU, 2.5, extra='marker-end="url(#c1t)"')
mus += T(880, 330, 'state graph: can steering', 15, 600, INK, 'middle') + T(880, 352, 'reach a style from here?', 15, 600, INK, 'middle')
g += F(1, mus)
g += F(2, T(590, 440, 'Propagation and reachability: classic graph questions, new setting', 19, 700, INK, 'middle'))
CL.append(sec('6. Two hidden graphs, one question', SVG(g), ch='6', cls='divider'))

g = defs('c2')
items = ['a graph is the one true description', 'the delta graph traces causal paths (it detects)', 'a circuit level account of any music model', 'the data graph shown today is inside the model']
for i, s in enumerate(items):
    y = 80 + i * 72
    blk = C(80, y, 20, '#fff', ACC, 3) + T(80, y + 7, '✗', 20, 700, ACC, 'middle') + T(120, y + 7, s, 20, 600, INK)
    g += F(i, blk) if i else blk
g += F(4, R(60, 375, 1060, 70, ACL, ACC, 1.5, 8) + T(590, 418, 'Claimed: vectors leave questions that graph tools are built to answer', 19, 700, ACC, 'middle'))
CL.append(sec('What I am not claiming', SVG(g), ch='6'))

g = defs('c3')
cx, cy = 590, 240
g += C(cx, cy, 82, ACL, ACC, 3) + T(cx, cy - 6, 'hidden graphs', 17, 700, ACC, 'middle') + T(cx, cy + 16, 'in generative models', 15, 400, INK, 'middle')
areas = [('Knowledge graphs', 'edit a model like a database?'), ('NLP', 'which behaviors should an edit test?'), ('AutoML', 'score pruning and merging cheaply?'),
         ('Theory', 'discretize and keep reachability?'), ('Systems', 'store activation graphs at scale?'), ('Accessibility', 'steer music for hearing loss?')]
for i, (a, q) in enumerate(areas):
    ang = -math.pi / 2 + i * 2 * math.pi / 6
    x, y = cx + 390 * math.cos(ang), cy + 175 * math.sin(ang)
    blk = L(cx + 82 * math.cos(ang), cy + 82 * math.sin(ang), x - 60 * math.cos(ang), y - 30 * math.sin(ang), AC2, 2)
    blk += R(x - 150, y - 34, 300, 64, SOFT, LINE, 1, 8) + T(x, y - 8, a, 16, 700, AC2, 'middle') + T(x, y + 15, q, 14, 400, INK, 'middle')
    g += F(i + 1, blk)
CL.append(sec('Where I would love your help', SVG(g), ch='6'))

g = defs('c4')
pts3 = [('We steer and edit models with vectors.', 'Vectors say what we pushed, not where it went.', AC2),
        ('Language: a graph from activations', 'already catches failures that tests miss.', ACC),
        ('Music: styles look like islands.', 'A graph inside the generator is the next experiment.', MU)]
for i, (a, b, col) in enumerate(pts3):
    y = 70 + i * 120
    blk = C(90, y + 30, 30, col) + T(90, y + 40, str(i + 1), 26, 700, '#fff', 'middle') + T(150, y + 24, a, 22, 700, INK) + T(150, y + 54, b, 19, 400, MUT)
    g += F(i, blk) if i else blk
g += F(3, T(590, 440, 'Thank you. Questions, and collaborators, welcome.', 22, 600, AC2, 'middle'))
CL.append(sec('What to take home', SVG(g), ch='6'))

MUSIC = S
CLOSE = CL
