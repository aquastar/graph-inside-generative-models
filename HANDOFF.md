# Handoff: Is There a Graph Inside Generative Models?

## CURRENT STATE (2026-11-15, read this first, everything below "Fixed decisions" is older history)

### 1. What this is and who it is for
- Talk: "Is There a Graph Inside Generative Models? Evidence from Language and Music" by Zhiqian Chen (陈志谦), new assistant professor, RIT Department of Computer Science (joined Aug 2026).
- Event: RIT CS department internal talk, Thursday Nov 19 2026, one hour slot, about 50 minutes of talking and 10 of questions (his decision Nov 16). Audience: CS faculty from many areas (systems, theory, vision, NLP, HCI), not specialists in interpretability or music.
- Why he gives it: outreach. He is new, and wants colleagues to see one coherent research program and come to him as collaborators (knowledge graphs, NLP, vision, audio and hearing, AutoML, theory). So the talk must be clear to non specialists, interesting every minute, show presentation craft, and be honest: never overclaim, never show unfinished work as a result.
- Deck: Reveal.js built by Python, published on GitHub Pages: https://aquastar.github.io/graph-inside-generative-models/ . HEAD at handoff: 24a9a74. 32 main slides plus backup slides under the down arrow.

### 2. The story the talk must tell (the effect he wants)
- Throughline: we change and explain models with vectors (steering, editing, LoRA, fine tuning, probes, features). A vector says what we added, not where it went. The knowledge inside models has another shape: a graph. Reading that graph shows what a vector misses.
- Arc: (1) context, everyone uses vectors; (2) the graph possibility in text, in vision, in music, one slide each, so the audience sees the idea is general across modalities; (3) Part 1 language: mostly the field's related work (each surgery with its best result and its catch), then our own work in only three slides; (4) Part 2 music: why music (emotion, a designed signal can switch the brain, music as medicine), then creativity as a new edge between ideas leading to music genres and our 2017 FusionGAN, then music graphs from simple to inside the generator, then the listening brain as the outside judge; (5) close: the seven graphs seen today, and the open question for the room.
- Every new graph gets a small tag at the top of its slide ("graph N of 7, name"), so the talk is literally strung on graphs. The close slide lists all seven with small drawn icons.
- Tone: curious and concrete. Each slide makes one point, has one diagram that builds with at most four clicks, short labels, one takeaway line at the bottom. He dislikes clutter, repeated text, decorative motion and anything that reads machine made.

### 3. Current slide order (main slides, Nov 16 2026, 29 slides, about 50 minutes of talking in a one hour slot)
Opening: 1 cover. 2 change one fact and the next question goes wrong (Space Needle, graph 1). 3 every tool we use is a vector (matrix glyphs for steer, edit, LoRA, fine tune, a point cloud where one edit moves its neighbors). 4 inside vision models researchers already find graphs (Olah, Johnson figures, graph 2). 5 Für Elise tiny graph (graph 3). 6 two claims, also the entry to Part 1 (throughline said here and on the last slide only).
Part 1 language: 7 seven surgeries. 8 merging. 9 steering. 10 unlearning. 11 Hase. 12 three lessons (pruning named here, pruning slides are backup under 8). 13 CIKM 2026 published version, a missing path means a worse answer (Table 9). 14 delta graph (graph 4). 15 results.
Part 2 music: 16 knowledge beyond text. 17 emotion (Picard, Minsky, Meyer cards). 18 Nobel optogenetics, animated. 19 music as medicine, animated. 20 a new idea is a new edge (book covers, genre tree, FusionGAN), the long creativity slide is backup. 21 fold 88 keys (score drawn in SVG). 22 Occam 70.2% (86.8% richer nodes named, slide in backup). 23 longest memory copies (live vote). 24 music theory shape inside MusicGen (graph 5). 25 steering one way (graph 6). 26 IDyOM predicts the brain, Di Liberto Figure 1 (graph 7). 27 live EEG demo, embedded from aquastar.github.io/music-to-brain/eeg-demo, In progress (per note link not yet above an untrained model). 28 plan. 29 close: the cloud from slide 3 returns with its graph, seven graphs, "Is there a graph inside your model?".
Timing table: docs/speaker-guide-zh.md section 4.

### 4. How the code works
- `python3 src/build.py` writes index.html. Commit index.html with the sources.
- src/talk.py: new slides as SVG built with helpers (T text, R rect, C circle, L line, P path, F(i, ...) fragment, wrap, photo(), cover() for book covers, quote(), person()). `assemble()` at the end sets the order: `vision` list is the opening, `lang` is Part 1, `mus` is Part 2, `close`. `backup(x)` nests a slide under the previous main one. `bridge(x, line)` appends a spoken bridge to the speaker notes. `toch(x, '1')` sets the chapter.
- src/build.py: reuses slides from the old deck src/legacy/nn2n_index.html by index through `OLDS` (indices 3, 17, 18, 21, 22, 25, 29, 30, 33, 35, 38 to 40, 43, 45 to 51), applies the graph tags from `GTAGS`.
- src/style_v2.py: restyle pass and CSS (a Python f string, so CSS braces are doubled). `ref_separators` and `linkify` make the bottom reference line (one line, links, short "Author Year" labels when several).
- Images: figs/people (portraits he supplied), figs/books (covers he supplied), other figs/*.png are paper figures.
- Checking: serve the folder (python3 -m http.server), screenshot every slide with Playwright at 1280x660, open the screenshots of every slide you changed, check for overlap, clipped text, empty boxes, and that the reference line and graph tag show. Never push a slide you have not looked at.
- After each change: commit with a short message, push to main (Pages deploys from main).

### 5. His rules (firm, he has corrected each one before)
- Text: no em dashes, en dashes or semicolons anywhere, ranges use "to", American spelling. Talk to him in short Chinese, slides in English.
- Look: Tufte style, ET Book font family for all text, soft colors within the RIT palette, orange for language, purple for music, blue for vision. Diagrams must look polished (Transformer Circuits or TikZ quality).
- Human touch: real images next to our drawings, book covers, a paper's first page, photos of quoted people, real photos of experiments. A quoted person must have a photo or logo, never initials only. Getting images (his rule 2026-11-15): find and download them yourself from official or openly licensed sources, credit in the notes. Ask him only when the hosts are blocked. Wikimedia rate limits the cloud shell IP, nobelprize.org, distill.pub, arXiv and CVF open access work.
- Quotes: never invent a quote. If the exact wording cannot be verified, write a paraphrase in upright text without quote marks.
- Person cards: quote beside the photo, card only as tall as its content, no empty space, no tag chips.
- References: only at the bottom of the slide, never repeated inside cards, at most one line, clearly lighter than body text, every work linked.
- Status: no In progress or Planned labels on the close slide, and do not count unfinished work as a graph or a result. CIKM 2026 paper is published. Do not name the NIH R16. Do not use the ICLR submission title, say "co-authored work under review".
- Full rule set: his knowledge base aquastar/zhiqian-knowledge-base, folder claude/skills/presentation-craft (SKILL.md, visual-style.md, reference.md, template/style_v2.py). Add any new lesson he gives you there too.

### 6. What to do next, in order
1. Trim Part 1 related slides (8 to 14). They come from his older talk and are dense: merging and unlearning have small labels and long side boxes. Goal per slide: the field's key result in one picture and the catch in one line, readable from the back of a room, about 60 seconds each. Keep the old content's facts, cut the rest into speaker notes.
2. Time budget: aim for about 38 minutes of talking plus questions. Count about 70 to 80 seconds per main slide. If over, move to backup first: slide 23 genre tree (keep FusionGAN by folding it into slide 22 or 24), then slide 18 Gardner and Li. Ask him before cutting anything else.
3. Vision slide 4: ask him for screenshots of the curve detector circuit figure from Olah et al. "Zoom In" (Distill 2020) and one scene graph figure, then put them next to the drawn diagrams.
4. Nobel slide 20: three laureates (Deisseroth, Hegemann, Nagel) show initials, ask him for photos.
5. Speaker notes: after the reorder, bridges and notes may mention old slide numbers or slides that moved. Read every main slide's notes and fix the chain so each slide's bridge leads into the next one.
6. Update docs/speaker-guide-zh.md: section 4 timing table for the new 32 slides, page numbers in other sections.
7. Waiting on him: the KB CHANGELOG merge (branch kb-sync/2026-11-04-funnel-it5), the items marked "需要你" in the speaker guide, a timed rehearsal.

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
