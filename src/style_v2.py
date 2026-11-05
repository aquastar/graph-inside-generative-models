"""House style v2 (docs/style-spec.md): override CSS, self hosted fonts, and a recolor pass for generated slides."""
import re

BG = '#FBFAF7'; INK = '#1F1E1B'; INK2 = '#5F5D50'; LINE = '#7C878E'; AXIS = '#ACA39A'; RULE = '#D7D2CB'; GROUP = '#F1EDE7'
ACC = '#F76902'; ACC_T = '#C45200'; LANG = '#009CBD'; LANG_D = '#007A94'; MUS = '#7D55C7'; FAIL = '#DA291C'

FONTS = '''
@font-face{font-family:"et-book";src:url(figs/fonts/etbook-roman-lf.woff) format("woff");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"et-book";src:url(figs/fonts/etbook-bold-lf.woff) format("woff");font-weight:600 800;font-style:normal;font-display:swap}
@font-face{font-family:"et-book";src:url(figs/fonts/etbook-italic.woff) format("woff");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"et-book-osf";src:url(figs/fonts/etbook-roman-osf.woff) format("woff");font-weight:400;font-display:swap}
@font-face{font-family:"Source Sans 3";src:url(figs/fonts/SourceSans3-Upright.woff2) format("woff2");font-weight:200 900;font-style:normal;font-display:swap}
@font-face{font-family:"Source Sans 3";src:url(figs/fonts/SourceSans3-Italic.woff2) format("woff2");font-weight:200 900;font-style:italic;font-display:swap}
@font-face{font-family:"Source Code Pro";src:url(figs/fonts/SourceCodePro.woff2) format("woff2");font-weight:200 900;font-display:swap}
'''

SERIF = '"et-book","Palatino Linotype",Palatino,Georgia,serif'
# one family for everything (his choice, 2026-11-02). Source Sans 3 stays loaded as a fallback option.
SANS = SERIF
REF = '#4A483E'

CSS = FONTS + f'''
/* ===== style v2 overrides ===== */
:root{{--ink:{INK};--muted:{INK2};--accent:{ACC};--accent2:{INK2};--soft:{GROUP};--line:{RULE};--paper:{BG};
  --f-editing:{ACC_T};--f-stitch:{LANG_D};--f-merge:#4E6B5C;--f-prune:#8A6D1F;--f-steer:{MUS};--f-unlearn:#A3324F;--f-ft:#5F6B73}}
html,body,.reveal-viewport{{background:{BG} !important}}
.reveal{{font-family:{SANS};color:{INK}}}
.reveal .slides section{{font-size-adjust:.45}}
.reveal .slides section svg,.reveal .slides section h2,.reveal .slides section .ref,.reveal section.titlehero{{font-size-adjust:none}}
.reveal svg text:not([font-family]){{font-family:{SANS}}}
.reveal > .progress,.reveal .slide-number{{display:none !important}}
.reveal .controls{{display:none !important}}
/* headline: ET Book, left, no bar */
.reveal h2{{font-family:{SERIF} !important;font-size-adjust:none;font-weight:400 !important;font-size:40px !important;line-height:1.12;color:{INK} !important;
  background:none !important;padding:0 !important;margin:30px 1.1em 18px 1.1em !important;letter-spacing:0 !important}}
.reveal h2::after{{display:none !important}}
.reveal h1,.reveal h3{{font-family:{SERIF};font-size-adjust:none;font-weight:400}}
.reveal h3{{color:{INK2}}}
.reveal b{{font-weight:600}}
/* section marker instead of the tab rail */
#rail{{height:auto;padding:14px 0 0 68px;gap:0;background:none;font:400 18px/1 {SANS};font-size-adjust:none}}
#rail span{{display:none !important}}
#rail span.here{{display:block !important;flex:none;background:none !important;color:{INK2} !important;text-transform:uppercase;font-size:13px;letter-spacing:.14em;height:auto}}
#footer{{border-top:0 !important;background:none !important;font:400 14px/1.4em {SANS};color:{AXIS}}}
#footer{{justify-content:flex-start !important}} #footer #fpart{{display:none}}
/* status: small caps with an underline mark */
.reveal .status{{background:none !important;color:{INK2} !important;border:0 !important;border-radius:0 !important;padding:0 0 3px 0 !important;
  font:400 13px/1 {SANS} !important;text-transform:uppercase !important;letter-spacing:.14em !important;top:14px !important;right:44px !important}}
.reveal .status.published{{border-bottom:2px solid {LINE} !important}}
.reveal .status.review{{border-bottom:2px solid {AXIS} !important}}
.reveal .status.progress{{border-bottom:2px solid {ACC} !important;display:block !important;height:auto !important;width:auto !important;left:auto !important;bottom:auto !important;background:none !important}}
.reveal .status.open,.reveal .status.plan{{border-bottom:2px dashed {INK2} !important}}
/* sidenote citation */
.reveal .ref .rsep{{display:inline-block;width:1px;height:.85em;background:{AXIS};margin:0 .65em;vertical-align:-.1em}}
.reveal .ref{{font:400 13.5px/1.3 {SERIF} !important;color:{REF} !important;text-align:right !important;margin-left:auto !important;max-width:66% !important}}
/* no banners: takeaway is a quiet serif sentence */
.reveal .takeaway{{background:none !important;border:0 !important;padding:0 !important;font-family:{SERIF};font-size-adjust:none;font-size:27px;font-weight:400 !important;color:{INK}}}
.reveal .q,.reveal section>.tl{{font-family:{SERIF};font-size-adjust:none;font-weight:400 !important;color:{INK} !important;background:none !important;border:0 !important;padding:0 !important}}
.reveal .lead{{font-family:{SERIF};font-size-adjust:none;font-weight:400}}
.reveal .big{{font-family:{SERIF};font-size-adjust:none;font-weight:400;color:{INK};text-decoration:underline {ACC} 4px;text-underline-offset:10px}}
.reveal .tag,.reveal .crumb{{color:{INK2} !important;font-weight:400 !important;text-transform:uppercase !important;font-size:.42em !important;letter-spacing:.14em}}
.reveal .crumb b{{color:{INK} !important;font-weight:600}}
/* boxes: fill only, no rules, small radius */
.reveal .card,.reveal .grid2>div,.reveal .grid3>div,.reveal .icons>div,.reveal .chain>div,.reveal .tiles>div,.reveal .wbsteps>div,
.reveal .figrow .note,.reveal .mapexp,#tlinfo{{background:{GROUP} !important;border:0 !important;border-radius:3px}}
.reveal .card.warn,.reveal .note .one,.reveal .wbsteps>div.current-fragment{{background:#FDEBDD !important;border:0 !important}}
.reveal .grid2 .h,.reveal .grid3 .h,.reveal .legend b,.reveal .maplegend b,.reveal .mapexp b,.reveal .figrow .note b{{color:{INK} !important}}
.reveal .chain>div:not(:last-child)::after{{color:{AXIS}}}
.reveal .tiles .n{{font-family:{SERIF};font-size-adjust:none;font-weight:400}}
.reveal .note .key{{background:none !important;color:{INK} !important;border-bottom:3px solid {ACC};font-family:{SERIF};font-size-adjust:none;font-weight:400 !important}}
.reveal .pts li::before{{background:{AXIS} !important;transform:none !important;border-radius:50%;width:.4em;height:.4em;top:.5em}}
.reveal .steps b{{color:{INK} !important}}
.reveal .annot .lbl{{color:{INK} !important}}
.reveal .graphtag{{position:absolute;top:13px;left:50%;transform:translateX(-50%);z-index:4;font:400 13px/1.3 {SANS};color:{MUS};letter-spacing:.06em;white-space:nowrap;display:flex;align-items:center;gap:7px}}
.reveal .graphtag b{{font-weight:700;color:{INK}}}
.reveal .graphtag svg{{width:22px;height:14px;display:inline-block;margin:0}}
.reveal .lessontag{{top:14px !important;right:44px !important;background:none !important;border:0 !important;border-radius:0 !important;color:{INK2} !important;font:400 13px/1 {SANS} !important;text-transform:uppercase;letter-spacing:.14em}}
.reveal .ph{{border:1px dashed {AXIS};background:none}}
.reveal img.fig{{border:0 !important;border-bottom:1px solid {RULE} !important;background:none !important;padding:0 !important}}
.reveal table th{{border-bottom:1.5px solid {INK} !important}}
.reveal table tr:last-child td{{border-bottom:1.5px solid {INK} !important}}
.reveal .mu{{color:{MUS} !important}}
.reveal .lm{{color:{LANG_D} !important}}
.reveal .wb3d{{background:{GROUP} !important;border:0 !important}}
.reveal .wbl{{font-family:{SANS}}}
.reveal .wbl.hot{{background:{ACC};color:{INK}}}
.reveal .map text,.reveal .map .node text{{font-family:{SANS}}}
.reveal .map .node rect{{fill:{GROUP} !important;stroke:none !important}}
.reveal .map .node.here rect{{fill:#FAD6BA !important;stroke:none !important}}
.reveal .map .core rect{{fill:#E6E1DA !important;stroke:none !important}}
.reveal .map .core text{{fill:{INK} !important}}
/* vertical stacks for backup slides */
.reveal .slides>section.stack.present{{display:block !important;padding:0 !important}}
.reveal .slides>section.stack>section.present{{display:flex !important;flex-direction:column;padding-top:18px !important;padding-bottom:30px !important;height:100%;box-sizing:border-box}}
.reveal .slides>section.stack>section.present>h2{{order:-2}}
.reveal .slides>section.stack>section>*:not(h2){{margin-left:1.1em;margin-right:1.1em}}
.reveal .slides>section.stack>section{{margin:0 !important}}
/* cover */
.reveal section.titlehero h1{{font-family:{SERIF};font-size-adjust:none}}
.reveal section.titlehero .herofig{{right:-70px !important;width:600px !important}}
.reveal section.titlehero h1 .th-q{{font-weight:400 !important;color:{INK} !important;font-size:44px !important;letter-spacing:0 !important}}
.reveal section.titlehero h1 .th-graph{{font-weight:400 !important;font-size:168px !important;line-height:1 !important;letter-spacing:-.01em !important;margin:0 0 34px -8px !important}}
.reveal section.titlehero .th-kicker{{color:{INK2} !important;font-weight:400 !important;text-transform:uppercase !important;font-size:14px !important;letter-spacing:.16em !important}}
.reveal section.titlehero .th-rule{{height:3px !important;border-radius:0 !important}}
.reveal section.titlehero .th-sub{{font-family:{SERIF};font-size-adjust:none;color:{INK2} !important;font-size:30px !important}}
.reveal section.titlehero .th-sub .lm{{color:{LANG_D} !important;font-weight:400}}
.reveal section.titlehero .th-sub .mu{{color:{MUS} !important;font-weight:400}}
.reveal section.titlehero .th-author{{border-top:1px solid {RULE} !important;color:{INK2} !important}}
.reveal section.titlehero .th-author b{{color:{INK} !important;font-weight:600}}
.reveal section.titlehero .herofig text{{font-family:{SANS};font-weight:400}}
'''

CMAP = {
    '#111': INK, '#111111': INK, '#333': INK, '#333333': INK, '#1c2430': INK,
    '#4c5b66': INK2, '#5b6770': INK2, '#6f7c86': INK2, '#5b6b7c': INK2,
    '#8a969e': LINE, '#9aa6ae': AXIS, '#9aa7b0': AXIS, '#b3bbc1': AXIS, '#b8c0c6': AXIS, '#c9d0d5': '#C4BDB3', '#c3cbd1': '#C4BDB3',
    '#d3d7da': RULE, '#dfe3e6': '#E2DDD6', '#e3e7ea': '#E2DDD6', '#dfe6ec': '#E2DDD6', '#e6e9eb': '#E9E5DF',
    '#eef1f3': GROUP, '#eef0f2': GROUP, '#eef1f4': GROUP, '#f2f3f4': GROUP, '#f4f5f6': GROUP, '#f6f7f8': GROUP, '#fafbfb': GROUP, '#e6f0f4': GROUP, '#e9eef2': GROUP, '#eaf3ea': GROUP,
    '#c0392b': FAIL, '#fbeceb': '#F8D8D5', '#fdecea': '#F8D8D5',
    '#1f8a9a': MUS, '#38b2c4': '#9F82D8', '#4fa9b6': '#9677D2', '#86c6cf': '#B9A5E0', '#bfe1e5': '#DCD1EB', '#e6f5f7': '#EEE8F6',
    '#5a4fcf': MUS, '#8a5a9e': MUS, '#6b4e9b': MUS, '#eef0ff': '#EEE8F6',
    '#1f6f8b': LANG_D, '#b8442c': ACC_T, '#2e7d32': INK2, '#2f7d4f': '#4E6B5C', '#3f5f7f': '#5F6B73',
    '#fff1e6': '#FDEBDD', '#fff3ea': '#FDEBDD', '#fbd3b4': '#FAD6BA', '#ffd2ad': '#FAD6BA',
}
NEUTRAL_STROKES = {RULE.lower(), '#e2ddd6', '#e9e5df', '#c4bdb3', AXIS.lower(), LINE.lower(), INK2.lower(), INK.lower(), GROUP.lower()}
TINT = {ACC.lower(): '#FDEBDD', ACC_T.lower(): '#FDEBDD', FAIL.lower(): '#FBE1DE', MUS.lower(): '#EEE8F6', LANG_D.lower(): '#E0F1F5',
        LANG.lower(): '#E0F1F5', '#4e6b5c': GROUP, '#a3324f': '#F6E1E6', '#8a6d1f': '#F3ECDC', '#5f6b73': GROUP}
BANNER = {'#FDEBDD', '#FAD6BA', '#F1EDE7', '#EEE8F6', '#F8D8D5', '#FBE1DE', '#E0F1F5'}
WHITE = {'#fff', '#ffffff', 'white'}

HEX = re.compile(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b(?![0-9a-fA-F])')

def _map(m):
    h = m.group(0).lower()
    return CMAP.get(h, m.group(0))

def _attr(tag, name):
    m = re.search(rf'\s{name}="([^"]*)"', tag)
    return m.group(1) if m else None

def _set(tag, name, val):
    if re.search(rf'\s{name}="[^"]*"', tag):
        return re.sub(rf'(\s{name}=")[^"]*(")', lambda m: m.group(1) + str(val) + m.group(2), tag, count=1)
    return tag.replace('<rect', f'<rect {name}="{val}"', 1)

def _num(v, d=0.0):
    try: return float(v)
    except (TypeError, ValueError): return d

def _rect(m):
    tag = m.group(0)
    fill = (_attr(tag, 'fill') or '').lower(); stroke = (_attr(tag, 'stroke') or 'none').lower()
    sw = _num(_attr(tag, 'stroke-width'), 1.0); rx = _num(_attr(tag, 'rx')); h = _num(_attr(tag, 'height'), 999)
    dashed = 'stroke-dasharray' in tag
    w = _num(_attr(tag, 'width'), 0)
    if w <= 8 and h <= 130 and fill.upper() == ACC:
        return _set(tag, 'fill', 'none')
    if w >= 600 and h <= 80 and not dashed and (fill.upper() in BANNER or stroke.upper() in (ACC, ACC_T)):
        return _set(_set(tag, 'fill', 'none'), 'stroke', 'none')
    if rx > 4:
        tag = _set(tag, 'rx', 3 if h <= 70 else 4)
    if fill in ('none', 'transparent') or 'fill-opacity="0"' in tag:
        if sw > 2.5: tag = _set(tag, 'stroke-width', 2.5)
        return tag
    if dashed:
        tag = _set(tag, 'stroke-width', min(sw, 1.5))
        if fill in WHITE: tag = _set(tag, 'fill', BG)
        return tag
    if stroke not in ('none', '') and sw > 0:
        tint = None
        if fill in WHITE:
            tint = GROUP if stroke in NEUTRAL_STROKES else TINT.get(stroke, GROUP)
        if tint: tag = _set(tag, 'fill', tint)
        tag = _set(tag, 'stroke', 'none')
    elif fill in WHITE:
        pass
    return tag

def _text(m):
    tag = m.group(0)
    x = _num(_attr(tag, 'x'), 0); size0 = _num(_attr(tag, 'font-size'), 14)
    if _attr(tag, 'text-anchor') == 'middle' and 560 <= x <= 620 and size0 >= 15.5 and _attr(tag, 'font-weight') in ('600', '700', '800'):
        tag = re.sub(r'(\sfont-size=")[^"]*(")', lambda k: k.group(1) + f'{size0 * 1.3:.1f}' + k.group(2), tag, count=1)
        tag = re.sub(r'\sfont-weight="[^"]*"', ' font-weight="400"', tag)
        if (_attr(tag, 'fill') or '').lower() == ACC.lower():
            tag = re.sub(r'(\sfill=")[^"]*(")', lambda k: k.group(1) + ACC_T + k.group(2), tag, count=1)
        return tag.replace('<text', '<text font-family="et-book,Georgia,serif" style="font-size-adjust:none"', 1)
    f = (_attr(tag, 'fill') or '').lower()
    if f == ACC.lower():
        size = _num(_attr(tag, 'font-size'), 14)
        if size < 60:
            tag = re.sub(r'(\sfill=")[^"]*(")', lambda k: k.group(1) + ACC_T + k.group(2), tag, count=1)
    tag = re.sub(r'\sfont-weight="(700|800|900)"', ' font-weight="600"', tag)
    tag = re.sub(r'\sfont-weight="500"', ' font-weight="400"', tag)
    tag = tag.replace('font-family="Georgia,serif"', 'font-family="et-book,Georgia,serif" style="font-size-adjust:none"')
    tag = tag.replace('font-family="Fira Mono,monospace"', 'font-family="Source Code Pro,monospace"')
    tag = tag.replace('font-family="Fira Sans"', '')
    if _attr(tag, 'font-size') and 'Georgia' not in tag:
        tag = re.sub(r'(\sfont-size=")[^"]*(")', lambda k: k.group(1) + f'{grow(size0):g}' + k.group(2), tag, count=1)
    return tag

def grow(s):
    """ET Book has a small x height: lift small labels most, leave display sizes alone"""
    k = 1.2 if s <= 12.5 else 1.16 if s <= 14.5 else 1.1 if s <= 17.5 else 1.05 if s <= 22 else 1.0
    return round(s * k * 2) / 2

def _stroke(m):
    tag = m.group(0)
    sw = _num(_attr(tag, 'stroke-width'))
    if sw > 2.5:
        tag = re.sub(r'(\sstroke-width=")[^"]*(")', lambda k: k.group(1) + '2.5' + k.group(2), tag, count=1)
    return tag

def _circle(m):
    tag = m.group(0)
    if (_attr(tag, 'fill') or '').lower() in WHITE and (_attr(tag, 'stroke') or 'none') != 'none':
        tag = re.sub(r'(\sfill=")[^"]*(")', lambda k: k.group(1) + BG + k.group(2), tag, count=1)
    return tag

def _style_attr(m):
    st = m.group(1)
    st = st.replace('Fira Sans', 'et-book').replace('Fira Mono', 'Source Code Pro')
    st = re.sub(r'font:\s*700', 'font:600', st)
    st = re.sub(r'color:\s*#F76902', 'color:' + ACC_T, st, flags=re.I)
    st = re.sub(r'border-radius:\s*(1[0-9]|[2-9][0-9])px', 'border-radius:3px', st)
    return f'style="{st}"'

def restyle(sec, cover=False):
    sec = HEX.sub(_map, sec)
    sec = re.sub(r'style="([^"]*)"', _style_attr, sec)
    sec = re.sub(r'<text\b[^>]*>', _text, sec)
    sec = re.sub(r'<tspan\b[^>]*>', _text, sec)
    sec = re.sub(r'<circle\b[^>]*>', _circle, sec)
    if not cover:
        sec = re.sub(r'<rect\b[^>]*>', _rect, sec)
        sec = re.sub(r'<(line|path|polyline)\b[^>]*>', _stroke, sec)
    return sec


FIXUPS = [  # slide specific collisions after the ET Book size lift
    (r'(<text x="645" y="(?:382|398|414|430)" font-size=")15(")', r'\g<1>13.5\2'),
    (r'(<text x="196\.0" y="4[46][0-9.]*" font-size=")14\.5(")', r'\g<1>12.5\2'),
]

def fixups(sec):
    for a, b in FIXUPS:
        sec = re.sub(a, b, sec)
    return sec


SEP = '<span class="rsep" aria-hidden="true"></span>'

def ref_separators(sec):
    """split a reference line into works at '. ' after a year or a closing parenthesis, join with a thin rule"""
    def one(m):
        items = re.split(r'(?:(?<=\b(?:19|20)\d\d)|(?<=\b(?:19|20)\d\d[a-z])|(?<=\)))\.\s+', m.group(2))
        items = [i.strip().rstrip('.') for i in items if i.strip()]
        return m.group(1) + SEP.join(items) + m.group(3)
    return re.sub(r'(<div class="ref">)(.*?)(</div>)', one, sec, flags=re.S)
