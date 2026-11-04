import re, shutil, os
HERE = os.path.dirname(os.path.abspath(__file__))
NEW = os.path.dirname(HERE)
OLD = os.environ.get('OLD_DECK', os.path.join(os.path.dirname(NEW), 'aquastar', 'neural-networks-to-networks'))
s = open(os.environ.get('OLD_HTML', os.path.join(HERE, 'legacy', 'nn2n_index.html'))).read()  # pinned copy of the original old deck
head = s[:s.find('<body>') + len('<body>')]
head = head.replace('<title>From Networks to Neural Networks</title>', '<title>Is There a Graph Inside Generative Models?</title>')
EXTRA_CSS = '''
.reveal .status{position:absolute;top:48px;right:44px;z-index:5;font:600 13px/1 "Fira Sans",sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:6px 11px;border-radius:3px;color:#fff}
.reveal .status.published{background:#2f7d4f}
.reveal .status.review{background:#4C5B66}
.reveal .status.progress{background:#F76902}
.reveal .status.open,.reveal .status.plan{background:#fff;color:#111;border:2px dashed #111;padding:4px 9px}
.reveal .mu{color:#1f8a9a;font-weight:600}
.reveal .lm{color:#F76902;font-weight:600}
.reveal .ph{border:2px dashed var(--line);color:var(--muted);font-size:.55em;padding:1.2em;text-align:center;background:#fafbfb}
.reveal .grid2{display:grid;grid-template-columns:1fr 1fr;gap:.7em;text-align:left;font-size:.78em}
.reveal .grid2>div{background:var(--soft);padding:.5em .8em}
.reveal .grid2 .h,.reveal .grid3 .h{font-weight:600;color:var(--accent2);display:block;margin-bottom:.2em}
.reveal .grid3 .yr{font-size:.75em;color:var(--muted);display:block;margin-bottom:.15em}
.reveal .nc{font-size:.66em;line-height:1.45}
.reveal .nc li{margin:.35em 0}
.reveal section.titlehero .th-sub .mu{color:#38b2c4}
.reveal section.titlehero .th-sub .lm{color:#F76902}
.reveal section.titlehero .herofig{position:absolute;right:-10px;top:40px;width:640px;height:580px}
.reveal .herofig .hl{stroke-dasharray:var(--len);stroke-dashoffset:var(--len)}
.reveal section.present .herofig .hl{animation:herodraw 7s ease-in-out infinite;animation-delay:var(--d)}
@keyframes herodraw{0%{stroke-dashoffset:var(--len);opacity:.95}22%{stroke-dashoffset:0}88%{stroke-dashoffset:0;opacity:.95}100%{stroke-dashoffset:0;opacity:.15}}
.reveal .herofig .hg{transform-box:fill-box;transform-origin:center}
.reveal section.present .herofig .hg{animation:heropulse 3.5s ease-in-out infinite;animation-delay:var(--d)}
@keyframes heropulse{0%,100%{opacity:.35;transform:scale(.8)}50%{opacity:1;transform:scale(1.4)}}
@media (prefers-reduced-motion:reduce){.reveal .herofig .hl{stroke-dashoffset:0;animation:none !important}.reveal .herofig .hg{animation:none !important}}
.reveal section.titlehero .th-left{top:70px;width:640px}
.reveal section.titlehero h1{color:#111;font-weight:700;line-height:1}
.reveal section.titlehero h1 .th-q{display:block;font-size:46px;font-weight:600;color:#111;letter-spacing:-.01em}
.reveal section.titlehero h1 .th-graph{display:block;font-size:150px;font-weight:800;color:#F76902;letter-spacing:-.03em;line-height:.95;margin:6px 0 4px -6px}
.reveal section.titlehero .th-sub{color:#4C5B66;font-size:27px}
.reveal section.titlehero .th-sub .mu{color:#1f8a9a}
.reveal section.titlehero .th-author{position:static;margin-top:26px;color:#4C5B66;border-top:1px solid rgba(247,105,2,.6)}
.reveal section.titlehero .th-author b{color:#111}
'''
import sys as _sys; _sys.path.insert(0, HERE); import style_v2 as SV
head = head.replace('</style>', EXTRA_CSS + SV.CSS + '</style>', 1)
head = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^"]*">', '', head)
assert 'fonts.googleapis' not in head

body = s[s.find('<div class="slides">'):]
secs = re.findall(r'(<section[^>]*>.*?</section>)', body, re.S)

def ch(sec, new):
    return re.sub(r'data-ch="[^"]*"', f'data-ch="{new}"', sec, count=1)

def retitle(sec, old, new):
    assert old in sec, old
    return sec.replace(old, new, 1)

PUB = '<span class="status published">Published</span>'

old = []
for i in (2, 3, 17, 25, 26, 33, 35):
    old.append(ch(secs[i], '1'))
x = ch(secs[40], '1'); x = retitle(x, '4. Eight surgeries, three lessons', 'Eight surgeries, three lessons'); old.append(x)
for i in (45, 46):
    old.append(ch(secs[i], '1'))
for i in (48, 49, 50, 51):
    x = ch(secs[i], '1'); x = x.replace('</h2>', '</h2>' + PUB, 1); old.append(x)

hero = open(os.path.join(HERE, 'hero.svg')).read().replace('fill="#1c2430"', 'fill="#ffffff"').replace('stroke-opacity=".13"', 'stroke-opacity=".28"')
cover = f'''<section class="title titlehero full" data-ch="0" data-background-color="#FBFAF7">
  <div class="th-left">
    <span class="th-kicker">RIT Computer Science Talk</span>
    <h1><span class="th-q">Is There a</span><span class="th-graph">Graph</span><span class="th-q">Inside Generative Models?</span></h1>
    <div class="th-rule"></div>
    <p class="th-sub">Evidence from <span class="lm">Language</span> and <span class="mu">Music</span></p>
    <div class="th-author"><b>Zhiqian Chen</b><br>Department of Computer Science<br>Rochester Institute of Technology</div>
  </div>
  {hero}
  <aside class="notes">Orange paths: a language model. Teal paths: a music generator. The faint lattice is the network we can see. The question of the talk: is there a smaller graph hiding inside it?</aside>
</section>'''

M = []
M.append('''<section class="divider" data-ch="5">
  <h2>5. Music: where does a style live?</h2>
  <p class="q">Language models store facts. Music models store styles. Is there a graph behind a style?</p>
  <div class="chain">
    <div>1957 to 2011<span>The graph is the generator. Markov chains, visible states, exact control.</span></div>
    <div>2019 to 2024<span>The graph describes the score. Notes and bars become nodes for a GNN.</span></div>
    <div>2023 on<span>The graph disappears into a large neural generator. Only vectors remain.</span></div>
    <div>Now<span>Can we read a graph back out of the generator?</span></div>
  </div>
  <div class="takeaway">Same arc as language models: interpretability started with vectors and is moving toward graphs. Music has not made that move yet.</div>
  <div class="ref">Hiller and Isaacson 1957. Pachet 2003. Pachet and Roy 2011. Jeong et al. 2019. Copet et al. 2023.</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Where I started: fusing two genres</h2>''' + PUB + '''
  <div class="cols">
    <div>
      <div class="card"><b>Task.</b> Given two genres, generate music that belongs to both.</div>
      <div class="card"><b>Model.</b> Generative adversarial dual learning: two generators trained to translate between genres and check each other.</div>
      <div class="ph">Audio example from the 2017 paper (to add)</div>
    </div>
    <div>
      <div class="card warn"><b>What it showed.</b> A generator can be trained to blend styles.</div>
      <div class="card warn"><b>What it could not show.</b> Where a style lives inside the generator, or why some blends work and others do not.</div>
    </div>
  </div>
  <div class="takeaway">Nine years later the question flips: open a large pretrained generator and ask whether a style can be added at all.</div>
  <div class="ref">Chen, Wu, Lu, Lerch, Lu, Learning to Fuse Music Genres with Generative Adversarial Dual Learning, ICDM 2017</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>When the graph was the generator</h2>
  <span class="crumb">First appearance: <b>Markov music</b></span>
  <div class="grid3">
    <div><span class="yr">1957</span><span class="h">Illiac Suite</span>Hiller and Isaacson compose with a computer. One movement draws notes from Markov chains: states are notes, edges are transition probabilities.</div>
    <div><span class="yr">2003</span><span class="h">The Continuator</span>Pachet learns a variable order Markov model of a player's style in real time and continues the phrase in that style.</div>
    <div><span class="yr">2011</span><span class="h">Markov constraints</span>Pachet and Roy steer a Markov model so that generated sequences satisfy constraints exactly, without losing the style.</div>
  </div>
  <div class="takeaway">When the graph is visible, control is a graph question: which states can be reached from here, and by which paths.</div>
  <div class="ref">Hiller and Isaacson, Experimental Music, 1959. Pachet, The Continuator: Musical Interaction with Style, JNMR 2003. Pachet and Roy, Markov Constraints: Steerable Generation of Markov Sequences, Constraints 2011</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>When the graph described the score</h2>
  <span class="crumb">Second appearance: <b>symbolic music as graphs</b></span>
  <table>
    <tr><th>Work</th><th>What becomes a graph</th><th>Used for</th></tr>
    <tr><td>Jeong et al. 2019</td><td>Notes in a score</td><td>Expressive piano performance</td></tr>
    <tr><td>PopMNet 2020</td><td>Melody and chord structure</td><td>Pop melody generation</td></tr>
    <tr><td>Karystinaios and Widmer 2022</td><td>Notes and their relations</td><td>Cadence detection</td></tr>
    <tr><td>MELONS 2022</td><td>Relations between bars</td><td>Long melody generation</td></tr>
    <tr><td>Polyphemus 2023</td><td>Chord level graphs (GraphVAE)</td><td>Multitrack generation</td></tr>
    <tr><td>Lim, Liang, Zhang 2024</td><td>Bar and phrase graphs</td><td>Hierarchical pop generation</td></tr>
    <tr><td>SMUG-explain 2024</td><td>Score graph</td><td>Explaining GNN predictions on music</td></tr>
  </table>
  <div class="takeaway">Here the graph lives in the data. It tells us about the music, not about the model.</div>
  <div class="ref">Jeong et al., ICML 2019. Wu et al., 2020. Karystinaios and Widmer, ISMIR 2022. Zou et al., 2022. Cosenza et al., 2023. Lim, Liang, Zhang, arXiv 2409.08155. Karystinaios et al., 2024</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Then the graph disappeared: MusicGen</h2>
  <span class="crumb">Third stage: <b>one large network, no explicit graph</b></span>
  <div class="chain">
    <div>Text prompt<span>"upbeat jazz with piano"</span></div>
    <div>Text encoder<span>prompt becomes conditioning vectors</span></div>
    <div>Transformer decoder<span>predicts audio tokens one step at a time, dozens of layers</span></div>
    <div>Audio tokens<span>EnCodec codebooks, discrete</span></div>
    <div>Waveform<span>decoded back to sound</span></div>
  </div>
  <div class="grid2">
    <div><span class="h">What is discrete</span>The audio tokens. Each time step picks from a fixed codebook.</div>
    <div><span class="h">What is hidden</span>The activations between layers. Continuous, high dimensional, where style must be encoded.</div>
  </div>
  <div class="takeaway">Open model, open weights, sizes from small to large. The standard test bed for interpretability of music generation.</div>
  <div class="ref">Copet et al., Simple and Controllable Music Generation, NeurIPS 2023. Défossez et al., High Fidelity Neural Audio Compression (EnCodec), 2022</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Inside, part 1: what can be read out?</h2>
  <span class="crumb">Interpretability of music generators: <b>probing</b></span>
  <div class="cols">
    <div class="card"><b>Castellon, Donahue, Liang 2021.</b> Representations inside Jukebox, a generative model, work well as features for music information retrieval tasks. Generation pretraining learns musical structure.</div>
    <div class="card"><b>Wei, Freeman, Donahue, Sun 2024.</b> Probes decode tempo, notes, intervals, scales, chords and chord progressions from Jukebox and MusicGen. Decodability depends on layer and size, and the smallest MusicGen often does best.</div>
  </div>
  <div class="takeaway">Musical concepts are linearly readable from activations. Reading is not controlling.</div>
  <div class="ref">Castellon, Donahue, Liang, Codified Audio Language Modeling Learns Useful Representations for Music Information Retrieval, ISMIR 2021. Wei et al., Do Music Generation Models Encode Music Theory?, ISMIR 2024</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Inside, part 2: what can be pushed?</h2>
  <span class="crumb">Interpretability of music generators: <b>steering vectors</b></span>
  <div class="cols">
    <div class="card"><b>Activation steering, 2025.</b> Difference in means vectors added to MusicGen activations control tempo (fast or slow) and timbre (bright or dark). Middle layers work best. Moderate strength gives smooth control, large strength degrades the audio.</div>
    <div class="card"><b>Zhao et al., ICLR 2026.</b> Recursive Feature Machine probes find directions for notes and chords. Adding them during generation raises target note accuracy from 0.23 to 0.82 while prompt adherence barely changes.</div>
  </div>
  <div class="takeaway">Same tool as refusal steering in language models: one direction, one push. Strength is a knob with a cliff.</div>
  <div class="ref">Activation Patching for Interpretable Steering in Music Generation, arXiv 2504.04479. Zhao, Beaglehole, Berg-Kirkpatrick, McAuley, Novack, Steering Autoregressive Music Generation with Recursive Feature Machines, ICLR 2026</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Inside, part 3: what concepts exist?</h2>
  <span class="crumb">Interpretability of music generators: <b>sparse features</b></span>
  <div class="cols">
    <div class="card"><b>Singh, Cherep, Maes 2025.</b> Sparse autoencoders on a music transformer's activations. Many features match familiar musical concepts, some match consistent patterns music theory has no name for. The features can steer generation.</div>
    <div class="card"><b>Paek et al. 2025.</b> Sparse autoencoders on audio latent spaces, mapped to pitch, loudness and timbre. Used to watch these properties form during generation in a text to music diffusion model.</div>
  </div>
  <div class="takeaway">A dictionary of musical directions. Still a list, not a map of how they connect.</div>
  <div class="ref">Singh, Cherep, Maes, Discovering and Steering Interpretable Concepts in Large Generative Music Models, arXiv 2505.18186. Paek, Zang, Yang, Leistikow, Learning Interpretable Features in Audio Latent Spaces via Sparse Autoencoders, arXiv 2510.23802</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Every tool so far is a vector</h2>
  <table>
    <tr><th>Tool</th><th>Object</th><th>Answers</th><th>Does not answer</th></tr>
    <tr><td>Probe</td><td>A direction</td><td>Is this concept encoded at this layer?</td><td>How states follow each other in time</td></tr>
    <tr><td>Steering vector</td><td>A direction plus a strength</td><td>Can we push the output toward the concept?</td><td>Can the generation reach it from where it is?</td></tr>
    <tr><td>Sparse features</td><td>Many sparse directions</td><td>Which concepts exist?</td><td>How concepts connect along a piece</td></tr>
  </table>
  <div class="takeaway">Music interpretability today sits where language model interpretability sat before attribution graphs: rich vectors, no graph.</div>
  <div class="ref">Language model contrast: Ameisen et al., Circuit Tracing: Revealing Computational Graphs in Language Models, Transformer Circuits 2025</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Reading a graph out of a sequence model</h2>
  <span class="crumb">The method exists, <b>on small models</b></span>
  <div class="chain">
    <div>Activations<span>one vector per time step</span></div>
    <div>Cluster<span>nearby vectors become one state</span></div>
    <div>Count transitions<span>state i at step t, state j at step t+1</span></div>
    <div>Directed graph<span>states are nodes, transition rates are edges</span></div>
  </div>
  <div class="grid3">
    <div><span class="yr">2018</span><span class="h">Weiss, Goldberg, Yahav</span>Extract automata from recurrent networks with queries and counterexamples.</div>
    <div><span class="yr">2020</span><span class="h">Dong et al.</span>Abstract recurrent networks into probabilistic automata, choosing the level of abstraction adaptively.</div>
    <div><span class="yr">2026</span><span class="h">Markovian Circuit Tracing</span>Cluster transformer activations into states and estimate transitions. Tested on a two layer model trained on synthetic sequences, with partial recovery.</div>
  </div>
  <div class="takeaway">Done for small recurrent networks and a toy transformer. Not yet for a real music generator, to our knowledge.</div>
  <div class="ref">Weiss, Goldberg, Yahav, ICML 2018. Dong et al., Towards Interpreting Recurrent Neural Networks through Probabilistic Abstraction, ASE 2020. Markovian Circuit Tracing for Transformer State Dynamics, arXiv 2605.20824 (preprint)</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Our observation: steering a style is one way</h2><span class="status review">Under review</span>
  <div class="cols">
    <div class="card"><b>Remove a style.</b> Subtract the style direction from MusicGen activations. The style fades and the music stays coherent. <span class="mu">Works.</span></div>
    <div class="card warn"><b>Add a style.</b> Add the same direction to music without that style. The output does not acquire it, or breaks before it does. <span class="lm">Fails.</span></div>
  </div>
  <div class="ph">Figure: the two arms side by side on MusicGen small and medium (to add after review)</div>
  <div class="takeaway">Our explanation: a style is not a direction but a thin set of trajectories. You can leave it easily, but a push rarely lands on it.</div>
  <div class="ref">Co-authored work under review. Results on MusicGen small and medium.</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>A graph over musical states, built from data</h2><span class="status progress">In progress</span>
  <div class="cols">
    <div>
      <div class="card"><b>Nodes.</b> Musical states taken from the music itself.</div>
      <div class="card"><b>Edges.</b> How often one state follows another, a Markov graph.</div>
      <div class="card"><b>Early picture.</b> Each style occupies a region with few edges to other styles. Styles look like islands.</div>
    </div>
    <div class="ph">Figure: the state graph colored by style (to add)</div>
  </div>
  <div class="takeaway">Honest caveat: this graph lives in the data, not inside the generator. It suggests where to look, it does not show what the model does.</div>
</section>''')

M.append('''<section data-ch="5">
  <h2>Next: the graph inside MusicGen</h2><span class="status progress">In progress</span>
  <div class="cols">
    <div>
      <ol class="nc">
        <li><b>Record.</b> Generate many clips per style with MusicGen and keep the activations of a middle layer at every step.</li>
        <li><b>Discretize.</b> Cluster all activations into a few hundred states.</li>
        <li><b>Connect.</b> Count state to state transitions along each generation. That is the hidden graph.</li>
        <li><b>Test.</b> Do styles form communities? After steering, do trajectories reach the target style's states?</li>
      </ol>
    </div>
    <div>
      <div class="card"><b>Control 1.</b> The same graph on output audio tokens, which are already discrete.</div>
      <div class="card"><b>Control 2.</b> Shuffled style labels, so community structure is not an artifact.</div>
      <div class="card"><b>Control 3.</b> Check that clusters are not just loudness or position in the clip.</div>
    </div>
  </div>
  <div class="takeaway">If styles are not separable at this resolution, that is a result too: style would then live in finer geometry than clusters capture.</div>
</section>''')

GSVG = '''<svg viewBox="0 0 1180 335" style="width:100%;max-width:1100px;height:auto;display:block;margin:0 auto">
<defs><marker id="mo" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4C5B66"/></marker>
<marker id="mi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#F76902"/></marker></defs>
<ellipse cx="300" cy="165" rx="230" ry="135" fill="#f2f3f4" stroke="#d3d7da" stroke-width="2"/>
<text x="300" y="60" font-size="18" font-weight="600" fill="#4C5B66" text-anchor="middle">Everything else</text>
<ellipse cx="860" cy="165" rx="120" ry="80" fill="#e6f5f7" stroke="#1f8a9a" stroke-width="2.5"/>
<text x="860" y="110" font-size="18" font-weight="600" fill="#1f8a9a" text-anchor="middle">A style</text>
<g fill="#111">
<circle cx="200" cy="130" r="7"/><circle cx="270" cy="210" r="7"/><circle cx="350" cy="120" r="7"/><circle cx="420" cy="200" r="7"/><circle cx="160" cy="210" r="7"/><circle cx="460" cy="130" r="7"/>
</g>
<g fill="#1f8a9a"><circle cx="810" cy="160" r="7"/><circle cx="880" cy="140" r="7"/><circle cx="900" cy="200" r="7"/><circle cx="830" cy="210" r="7"/></g>
<g stroke="#4C5B66" stroke-width="2" fill="none" marker-end="url(#mo)">
<path d="M810,160 C700,90 560,100 470,125"/><path d="M880,140 C720,40 520,60 360,115"/><path d="M900,200 C760,280 560,260 430,205"/><path d="M830,210 C700,300 400,300 278,215"/></g>
<path d="M440,250 C600,300 720,290 805,225" stroke="#F76902" stroke-width="3" fill="none" stroke-dasharray="8 6" marker-end="url(#mi)"/>
<text x="640" y="22" font-size="16" font-weight="600" fill="#4C5B66" text-anchor="middle">many exits: removing a style is easy</text>
<text x="620" y="322" font-size="16" font-weight="600" fill="#F76902" text-anchor="middle">few entrances: adding a style is hard</text>
</svg>'''

M.append('''<section data-ch="5">
  <h2>What a hidden graph would explain</h2><span class="status open">Open question</span>
  ''' + GSVG + '''
  <div class="takeaway">On a directed graph, the expected time to reach an island from outside can be far larger than the time to leave it. If the graph inside MusicGen looks like this, one way steering is a reachability fact, not a quirk.</div>
</section>''')

C = []
C.append('''<section class="divider" data-ch="6">
  <h2>6. Two hidden graphs, one question</h2>
  <div class="grid2">
    <div><span class="h"><span class="lm">Language</span>: across the model's state</span>A graph built from activation differences before and after an edit. Its features detect edits that pass their own test but break related behavior.<br><span class="small">Published, SDM 2026</span></div>
    <div><span class="h"><span class="mu">Music</span>: across time</span>A graph over the states a generation passes through. The question is whether steering can reach a style from where the music is.<br><span class="small">Observation under review, graph in progress</span></div>
  </div>
  <div class="takeaway">Propagation and reachability, classic questions in graph theory and network science, in a new setting.</div>
</section>''')

C.append('''<section data-ch="6">
  <h2>What I am not claiming</h2>
  <ul class="nc" style="font-size:.8em">
    <li>Not that a graph is the one true description of a generative model.</li>
    <li>Not that the delta graph traces the causal path of an edit. It detects, it does not explain.</li>
    <li>Not a circuit level account of any music model.</li>
    <li>Not that the music graph shown today is inside the model. That graph is built from data, the in model graph is in progress.</li>
  </ul>
  <div class="takeaway">What I am claiming: the vector view leaves questions that graph tools are built to answer, and both domains now give us a concrete place to test that.</div>
</section>''')

C.append('''<section data-ch="6">
  <h2>Where I would love your help</h2>
  <div class="grid3">
    <div><span class="h">Knowledge graphs</span>Align the explicit graphs we curate with the implicit ones inside models. Can an edit be checked like a database update?</div>
    <div><span class="h">NLP</span>Which related behaviors should an edit be tested on, and across which languages?</div>
    <div><span class="h">AutoML</span>Pruning, merging and quantization are searched operations. Can a graph diagnostic score them before full evaluation?</div>
    <div><span class="h">Theory</span>What discretization of continuous trajectories preserves reachability? What can be guaranteed?</div>
    <div><span class="h">Systems and data</span>Storing and querying activation graphs at scale across many models and many edits.</div>
    <div><span class="h">Accessibility</span>If style can be steered reliably, music can be shaped for listeners with hearing loss.</div>
  </div>
</section>''')

C.append('''<section data-ch="6">
  <h2>What to take home</h2>
  <div class="card" style="font-size:.95em"><b>1.</b> We control generative models with vectors. Vectors say what we pushed, not where it went.</div>
  <div class="card" style="font-size:.95em"><b>2.</b> In language models, a graph built from activations already catches failures that tests miss.</div>
  <div class="card warn" style="font-size:.95em"><b>3.</b> In music, styles look like islands, and whether a graph inside the generator explains one way steering is the next experiment.</div>
  <p class="q" style="margin-top:1em">Thank you. Questions, and collaborators, welcome.</p>
</section>''')

tail = s[s.rfind('</section>') + len('</section>'):]
tail = re.sub(r"var CH=\[\[.*?\]\];", "var CH=[['0','Overview'],['1','1 Language'],['2','2 Music'],['4','Close']];", tail, flags=re.S)
tail = re.sub(r"var NAMES=\{[^}]*\};", "var NAMES={'0':'Overview','1':'Part 1. Language','2':'Part 2. Music','3':'Part 3. Beyond','4':'Close'};", tail)
tail = re.sub(r"var CHN=\{[^}]*\};", "var CHN={'0':'Overview','1':'Part 1. Language','2':'Part 2. Music','3':'Part 3. Beyond','4':'Close'};", tail)
assert "1 Language" in tail

import sys; sys.path.insert(0, HERE); import talk as TK
OLDS = {}
for i in (3, 33, 35, 43, 45, 47):
    OLDS[i] = ch(secs[i], '0' if i in (3, 43, 45, 47) else '1')
for i in (46, 48, 49, 50, 51):
    OLDS[i] = ch(secs[i], '1').replace('</h2>', '</h2>' + PUB, 1)
parts = TK.assemble(cover, OLDS)
allsecs = [x for k in ('vision', 'language', 'music', 'beyond', 'close') for x in parts[k]]

def no_motion(sec):
    """drop decorative moving balls: a circle animated along a path becomes a static circle at the path start"""
    def fix(m):
        attrs, path = m.group(1), m.group(2)
        x, y = re.match(r'M\s*([-\d.]+)[ ,]([-\d.]+)', path).groups()
        attrs = re.sub(r'\s(cx|cy)="[^"]*"', '', attrs)
        return f'<circle{attrs} cx="{x}" cy="{y}"/>'
    return re.sub(r'<circle([^>]*)><animateMotion[^>]*path="([^"]+)"[^>]*/></circle>', fix, sec)

def cap_fragments(sec, n=4):
    """at most n reveal steps per slide: number unindexed fragments in order, then pool the steps"""
    k = [0]
    def num(m):
        tag = m.group(0)
        if 'data-fragment-index' in tag:
            return tag
        k[0] += 1
        return tag.replace('class="', f'data-fragment-index="{100 + k[0]}" class="', 1)
    sec = re.sub(r'<[a-z]+[^>]*class="[^"]*\bfragment\b[^"]*"[^>]*>', num, sec)
    idx = sorted({int(v) for v in re.findall(r'data-fragment-index="(\d+)"', sec)})
    if len(idx) <= n:
        return sec
    remap = {v: 1 + (r * n) // len(idx) for r, v in enumerate(idx)}
    return re.sub(r'data-fragment-index="(\d+)"', lambda m: f'data-fragment-index="{remap[int(m.group(1))]}"', sec)

allsecs = [cap_fragments(no_motion(x)) for x in allsecs]
allsecs = [re.sub(r'\s*<div class="lessontag">[^<]*</div>', '', x) for x in allsecs]
allsecs = [SV.ref_separators(SV.fixups(SV.restyle(x, cover='titlehero' in x[:200]))) for x in allsecs]
# backup slides become vertical stacks under the slide before them, so the page counter and the ending stay on the main run
_stack = []
for x in allsecs:
    if 'class="backup' in x[:120] and _stack:
        _stack[-1].append(x)
    else:
        _stack.append([x])
def _wrap(group):
    if len(group) == 1:
        return group[0]
    chv = re.search(r'data-ch="([^"]*)"', group[0]).group(1)
    return f'<section data-ch="{chv}">\n' + '\n'.join(group) + '\n</section>'
allsecs = [_wrap(g_) for g_ in _stack]
for x in allsecs:
    assert 'animateMotion' not in x, x[:120]
    vis = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', x, flags=re.S)
    txt = ' '.join(re.findall(r'>([^<>]+)<', vis))
    txt = re.sub(r'&#?\w+;', ' ', txt)
    bad = [c for c in ('\u2014', '\u2013', ';') if c in txt]
    if bad:
        print('CONTEXT', [t[max(0, t.find(c) - 60):t.find(c) + 20] for c in bad for t in [txt]])
    assert not bad, (bad, re.search(r'<h2>(.*?)</h2>', x).group(1) if '<h2>' in x else x[:80])

FE_HOOK = """<script>
(function(){
  function frames(s){ return s ? Array.prototype.slice.call(s.querySelectorAll('iframe.fe-frame')) : []; }
  function play(f){ if(!f.getAttribute('src')){ f.addEventListener('load', function(){ f.contentWindow.postMessage('fe-play','*'); }, {once:true}); f.setAttribute('src', f.dataset.src); } else { f.contentWindow.postMessage('fe-play','*'); } }
  function stop(f){ if(f.contentWindow) f.contentWindow.postMessage('fe-stop','*'); }
  var tok = 0;
  function count(s){
    if(!s) return; var my = ++tok;
    Array.prototype.forEach.call(s.querySelectorAll('[data-count]'), function(el){
      var to = parseFloat(el.dataset.count), dec = parseInt(el.dataset.dec || '0', 10), suf = el.dataset.suffix || '';
      var delay = parseFloat(el.dataset.delay || '0') * 1000, dur = 1100, t0 = null;
      el.textContent = (0).toFixed(dec) + suf;
      function step(ts){ if(my !== tok) return; if(t0 === null) t0 = ts; var k = Math.min(1, (ts - t0) / dur); k = 1 - Math.pow(1 - k, 3); el.textContent = (to * k).toFixed(dec) + suf; if(k < 1) requestAnimationFrame(step); }
      setTimeout(function(){ if(my === tok) requestAnimationFrame(step); }, delay);
    });
  }
  var actx = null, cur = null;
  function label(b, playing){ if(!b.dataset.label) b.dataset.label = b.innerHTML.replace(/^\\s*(&#9654;|▶)\s*/, ''); b.innerHTML = (playing ? '&#10074;&#10074; ' : '&#9654; ') + b.dataset.label; b.classList.toggle('playing', playing); }
  function stopAll(){
    if(!cur) return; var c = cur; cur = null;
    if(c.audio){ c.audio.pause(); c.audio.currentTime = 0; }
    if(c.osc){ c.osc.forEach(function(o){ try{ o.stop(); }catch(e){} }); }
    if(c.timer) clearTimeout(c.timer);
    label(c.btn, false);
  }
  document.addEventListener('click', function(ev){
    var b = ev.target.closest && ev.target.closest('button.playclip'); if(!b) return;
    ev.stopPropagation();
    if(cur && cur.btn === b){ stopAll(); return; }
    stopAll();
    if (b.dataset.audio) {
      var au = document.getElementById('au_' + b.dataset.clip);
      if (!au) { au = new Audio(b.dataset.audio); au.id = 'au_' + b.dataset.clip; au.className = 'clipaudio'; document.body.appendChild(au); }
      au.currentTime = 0; au.play(); cur = {btn: b, audio: au}; label(b, true);
      au.onended = function(){ if(cur && cur.audio === au){ cur = null; label(b, false); } };
      return;
    }
    var data = JSON.parse(document.getElementById('clipdata').textContent)[b.dataset.clip];
    actx = actx || new (window.AudioContext || window.webkitAudioContext)(); actx.resume();
    var t0 = actx.currentTime + 0.05, t = t0, osc = [];
    data.forEach(function(n){
      var o = actx.createOscillator(), g = actx.createGain();
      o.type = 'triangle'; o.frequency.value = 440 * Math.pow(2, (n[0] - 69) / 12);
      g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.25, t + 0.015); g.gain.exponentialRampToValueAtTime(0.0001, t + Math.max(n[1], 0.12) * 0.95);
      o.connect(g); g.connect(actx.destination); o.start(t); o.stop(t + Math.max(n[1], 0.12)); t += n[1]; osc.push(o);
    });
    var me = {btn: b, osc: osc}; cur = me; label(b, true);
    me.timer = setTimeout(function(){ if(cur === me){ cur = null; label(b, false); } }, (t - t0) * 1000 + 200);
  }, true);
  Reveal.on('ready', function(e){ frames(e.currentSlide).forEach(play); count(e.currentSlide); });
  Reveal.on('slidechanged', function(e){ stopAll(); frames(e.previousSlide).forEach(stop); frames(e.currentSlide).forEach(play); count(e.currentSlide); });
  (function boot(){ if (Reveal.isReady && Reveal.isReady()) { var cs = Reveal.getCurrentSlide(); frames(cs).forEach(function(f){ if(!f.getAttribute('src')) play(f); }); count(cs); } else { setTimeout(boot, 150); } })();
})();
</script>
"""
tail = tail.replace('</body>', FE_HOOK + '</body>', 1)
tail = tail.replace("document.body.classList.toggle('on-title', i===0)", "document.body.classList.toggle('on-title', secs[i].classList.contains('full'))")
assert "contains('full')" in tail
assert 'fe-frame' in tail
html = head + '\n<div class="reveal"><div class="slides">\n\n' + '\n\n'.join(allsecs) + '\n' + tail
open(NEW + '/index.html', 'w').write(html)
os.makedirs(NEW + '/figs', exist_ok=True)
for f in set(re.findall(r'figs/[A-Za-z0-9_]+\.png', html)):
    if not os.path.exists(NEW + '/' + f):
        shutil.copy(OLD + '/' + f, NEW + '/' + f)
shutil.copy(OLD + '/deck.js', NEW + '/deck.js')
print('slides', len(allsecs), {k: len(v) for k, v in parts.items()})
