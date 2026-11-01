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
- index.html built by src/build.py from the old deck repo aquastar/neural-networks-to-networks plus src/music.py and src/vision.py. Scratch paths inside build.py point to the old session scratchpad, fix paths before rerunning.
- figs/fe-chain.html: standalone Für Elise animation from aquastar/zhiqian-ai (src/pages/index.astro), plays when the parent posts 'fe-play', click for sound. Not yet embedded in a slide.

## Blocked
Original paper figures: shell could not reach arxiv.org, openreview.net, archives.ismir.net, elifesciences.org, journals.plos.org in the old session. User added domains in settings, expected to work in a new session. Priority figures: Copet 2023 Fig 1, Wei 2024 layer probing, Di Liberto 2020, Bellier 2023, Denk 2023 Fig 1, Tuckute 2023 layer map, Meng 2022 Fig 1, Hase 2023, plus his own steering and pilot figures.
Public repo: paywalled figures (Nature, Cell, Neuron, PNAS) may need the repo private before posting.
