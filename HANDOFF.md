# Handoff: Is There a Graph Inside Generative Models?

RIT CS department internal talk (outreach). Title and abstract due Nov 19 2026. Live deck: https://aquastar.github.io/graph-inside-generative-models/

## Fixed decisions
- Title: Is There a Graph Inside Generative Models? Evidence from Language and Music
- Abstract: the Fable version (vectors record what we changed, not where it goes; LM delta graph detects silent edit failures; MusicGen remove works add fails; data transition graph suggests styles are disjoint regions; in model graph being tested; propagation and reachability). No overclaiming.
- Style: each slide one diagram with fragments, short labels, one takeaway. Original paper figures must be added on key slides, Claude's animations are supporting layers. Max 4 fragments, no decorative moving balls except the Für Elise animation.
- Never use dashes or semicolons in any text. American spelling.
- Status labels: Published, Under review, In progress, Planned/Open question.
- Do not name the NIH R16 on slides. Do not use the ICLR submission title. Say "co-authored work under review".

## Target structure (about 42 slides)
Vision 8: cover, a vector says what we changed, same machine two instruments (NEW), facts versus styles (NEW), two axes depth and time, three networks: the music, the model, the listener (NEW, brain as measuring instrument not modeled object), network science table (+ encoding row), program build test generalize (+ judge row).
LLM 11 (ratio LLM:music = 1:1.5): Part 1 divider, seven surgeries, refusal direction, steering per input critique, ROME causal tracing, localization is not editing (Hase), four receipts, delta graph method, results, shape beats size and limits, bridge to time (add "no ground truth: a style needs an outside judge").
Music 17: four stages divider (no moving ball), Für Elise learn (iframe figs/fe-chain.html), Für Elise compose, 144 numbers name the corpus 70.9% (six corpora, 1,000 pieces, confusion matrix from zhiqian.ai/music-markov), where the graph becomes a path (order 1: 10 nodes 89% revisits, order 3: 81 nodes 6%, LLM judge 96 to 100% vs 60%, AMI 0.16 to 0.32 at second order, variable order: which contexts earn their memory), 2017 ICDM genre fusion, before neural generators the graph was visible, MusicGen anatomy, three vector tools (+ SMITIN Koo 2025, Singh is ICLR 2026, Facchiano 2025 is arXiv 2504.04479), every tool is a vector, Music to brain 1 listener is a predictor (IDyOM, Di Liberto 2020 eLife), Music to brain 2 decoding (Bellier 2023 PLOS Biology, Denk 2023 Brain2Music, datasets OpenMIIR NMED-T NMED-H MUSIN-G DEAP), Music to brain 3 do model layers predict the brain (Schrimpf 2021, Caucheteux and King 2022, Goldstein 2022, Kell 2018, Tuckute 2023, Pepino 2025, Noguchi 2026), Music to brain 4 our plan: brain as judge (Planned), one way steering (Under review), pilot: attributes decodable, tempo dose response (In progress, needs his figures), next: graph inside MusicGen judged by a listener (2x2 matrix + brain column).
Beyond 3: one delta graph for every surgery, sequence generator is a dynamical system, what would make me drop the graph (+ layer EEG alignment no better than random init).
Close 3: two hidden graphs one judge, where I would love your help (+ audiology NTID, neuroscience), take home.
Closing line: "A graph inside a generator is a hypothesis about the model. A listener's brain is the only judge that did not write the exam."

## Closest prior work to the brain plan
Noguchi, Akama, Nakamura, Minamikawa, Polouliakh 2026 (Sony CSL), arXiv 2603.03190: NMED-T EEG (20 subjects, 10 songs, 128 ch). MusicGen-large output logits on the first codebook give surprisal and entropy, MuQ last layer gives acoustic tokens. These are teacher targets for masked pretraining of an EEG encoder, then 10-way song identification from 3 s EEG (accuracy 0.823 scratch to 0.887 ensemble). No internal layers, no steering, no style. Pepino 2025: 36 audio encoders vs fMRI, not generators. Yang 2026: audio LLMs vs EEG, speech stimuli. Brain2Music (Denk 2023): MusicLM components vs fMRI, no layerwise, no interventions.

## Files
- index.html is built by `python3 src/build.py`. It reads the old deck from ../aquastar/neural-networks-to-networks by default (clone it there, or set OLD_DECK to its path). No scratchpad paths remain.
- src/talk.py holds the new and reshaped slides and the final order. src/vision.py and src/music.py hold the reused drawings.
- build.py runs three checks on every slide: no animateMotion (moving balls are turned into static dots), at most 4 fragment steps (extra steps are pooled), and no em dash, en dash or semicolon in visible text.
- figs/fe-chain.html takes ?act=learn (learning only, loops) or ?act=compose (all arrows drawn, composing only). The two Für Elise body slides embed one act each, the cold open embeds the full loop. ?autoplay=1 makes it start when the deck loads it. A small script in the tail starts the animation when its slide opens and stops it when it closes. Click the animation for sound.
- thumbs/ is regenerated from headless Chrome screenshots. Reveal.js loads from cdnjs, which the cloud shell cannot reach, so screenshots use a local copy from npm.

## Status (Nov 1 2026)
Done: 42 slides in the target order (Vision 8, Language 11, Music 17, Beyond 3, Close 3). New slides: same machine two instruments, facts versus styles, three networks, two Für Elise slides, 144 numbers, where the graph becomes a path, music and the brain 1 to 4, pilot, shape beats size and where it stops (merged). Encoding row, judge row, outside judge line, SMITIN and corrected Singh and Facchiano citations, brain column on the next experiment slide, fourth falsifier, audiology and neuroscience in the help slide, closing line.

Original figures added: Denk 2023 Figure 1 and the encoding result (brain 2 and brain 3 slides), taken from the Brain2Music project page repo google-research/seanet.

## Opening (revised Nov 1 2026)
He did not want a trailer. "Trailer" was an analogy: say the exciting results early. Structure now: light cover with a large orange "Graph", then two preview slides, music first (live Für Elise graph plus three of our results) and language second (delta graph drawing, 11 vs 14 vs 17, one card on attribution graphs as other work), then the vision slides and Part 1. All slides use light backgrounds. 44 slides.
Presentation craft research: docs/presentation-craft.md. Apply next: assertion headlines, a findings forecast in the first five minutes, setup and payoff, end on contributions instead of "Thank you".

## Still to do
- Pilot slide: two dashed placeholders for his probe accuracy by layer and tempo dose response figures.
- Brain 1 slide: dashed placeholder for the Di Liberto 2020 figure.
- Paper figures still blocked: the cloud shell proxy answered 403 for arxiv.org, openreview.net, archives.ismir.net, elifesciences.org, journals.plos.org on Nov 1 2026 (also export.arxiv.org, ncbi, europepmc, huggingface, jsdelivr). Public GitHub clones work, which is how Brain2Music came in. Missing: Copet 2023 Fig 1 (anatomy slide), Wei 2024 layer probing (tools slide), Di Liberto 2020, Bellier 2023, Tuckute 2023 layer map, Hase 2023. Meng 2022 Fig 1 is already on the ROME slide. Fastest fix: download these PDFs locally and attach them, or check the domain allowlist again.
- Paywalled figures (Nature, Cell, Neuron, PNAS) may need the repo private before posting.
