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

## Round 7 (Nov 2 2026): Markov order results
Experiments from branch experiments/music-markov added as two music slides after the memory order slide: "Richer nodes beat longer memory" (chance 16.7, order 1 70.2, order 2 78.2, variable 73.3, note plus length 86.8 and 88.7) and "More memory sounds more like the style, because it copies" (style 57, 64, 65 percent, longest copy 7.6, 8.3, 12.1 notes vs real 10.9, eight play buttons with the piano clips in figs/audio). "Baseline 20%" corrected to "chance 17%" everywhere. Figures from the experiment kept in figs/markov for reference. 38 slides.

## Round 6 (Nov 2 2026)
Two overview slides before the Für Elise demo: "Knowledge is not only text" (Gardner 1983 and Fei-Fei Li's five intelligences, equations as the open direction with a redrawn sketch of Lindsey et al. 2025 addition paths, her verified quote "Spatial intelligence represents the frontier beyond language") and "Music is where emotion can be measured" (Picard 1997, Minsky 2006, Salimpoor 2011, Koelsch 2014, Juslin and Västfjäll 2008, the last five citations from memory, check wording). Take away adds "Next: equations". People photos: circular slots that show initials until he adds licensed photos to figs/people (file names in figs/people/README.md). Claude does not download photos of real people. 36 slides.

## Round 5 (Nov 2 2026)
Music part rebuilt from a verified Fable survey (docs/music-graphs-survey-2026-11-02.md). 12 slides: oldest music model is a graph (Hiller, Conklin and Witten, Continuator, IDyOM), fold 88 keys into 12 scale degrees with two play buttons (Für Elise opening, a tune drawn from its table, WebAudio, clips in src/clips.json), Occam's razor classification, memory order, when graphs help (McFee and Ellis structure graph vs cadence GNN, Tonnetz, note networks), MusicGen in plain words, probing (Wei et al. ISMIR 2024 Table 2), brain story under one theme (brains and models are both next event predictors): language met the brain, IDyOM predicts EEG (Di Liberto 2020), the brain keeps enough to rebuild music (Bellier 2023, Denk 2025), music generators only from the outside (Pepino, Noguchi, Denk), our plan (three sources of surprise, one yardstick). Beyond section and the four outcome matrix removed. 34 slides.
Experiments for higher order classification and generation were handed to another conversation, results expected on branch experiments/music-markov (prompt in chat Nov 2 2026). Add their audio clips to the memory order slide when they arrive.

## Round 4 (Nov 2 2026)
Space Needle (Seattle to Paris) is the running example for the whole language part. Overview is now 11 slides, language first then music, to stop jumping between domains: cover, seven surgeries (Edited card uses Space Needle), whole field story, silent failure (edit is a shortcut, old fact still inside, Xie et al. ACL 2025, Zhang et al. ICLR 2025), knowledge graph ripple (which country is the Space Needle in, RippleEdits TACL 2024, MQuAKE EMNLP 2023), four receipts, every surgery is a vector, delta graph screen, Für Elise demo, one way steering, two claims forecast. 34 slides total.

## Structure, round 3 (Nov 1 2026, late night, after his slide by slide feedback)
32 slides. His rules from this round: do not cut in the introduction, cut later. Reuse his original slides from aquastar/neural-networks-to-networks where they exist, they are better than redraws. Others' paper figures must be glanceable, otherwise redraw with one conclusion. No duplicate slides. Final slide is the take away only.
- Overview 9: animated cover, seven surgeries (old 3, all seven), the whole field in one story (old 43), four receipts with original figures (old 45), every surgery is stored as a vector (steer, edit, fine tune formulas), Für Elise demo with the 70.9% result, two claims forecast (language, music with the brain), the delta graph screen (old 47), one way steering (placeholder until he supplies his own data, audio and visuals).
- Part 1 language 10: divider, refusal and steering critique redrawn as simple diagrams, ROME with one line conclusion, Hase (old 35), then old 46, 48, 49, 50, 51 unchanged.
- Part 2 music 10: Occam's razor opener (confusion matrix), memory order, four stages, MusicGen anatomy, vector tools, brain 1 to 4 (Brain2Music cited as Nature Communications 2025), four outcomes.
- Beyond 2, take away 1.
Abstract and title: see the chat. Title still "Is There a Graph Inside Generative Models?", "Beyond Vectors" prefix proposed, not confirmed.

## Still to do
- Pilot slide: two dashed placeholders for his probe accuracy by layer and tempo dose response figures.
- Brain 1 slide: dashed placeholder for the Di Liberto 2020 figure.
- Paper figures still blocked: the cloud shell proxy answered 403 for arxiv.org, openreview.net, archives.ismir.net, elifesciences.org, journals.plos.org on Nov 1 2026 (also export.arxiv.org, ncbi, europepmc, huggingface, jsdelivr). Public GitHub clones work, which is how Brain2Music came in. Missing: Copet 2023 Fig 1 (anatomy slide), Wei 2024 layer probing (tools slide), Di Liberto 2020, Bellier 2023, Tuckute 2023 layer map, Hase 2023. Meng 2022 Fig 1 is already on the ROME slide. Fastest fix: download these PDFs locally and attach them, or check the domain allowlist again.
- Paywalled figures (Nature, Cell, Neuron, PNAS) may need the repo private before posting.
