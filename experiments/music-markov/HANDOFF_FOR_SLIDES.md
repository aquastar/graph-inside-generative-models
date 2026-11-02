# Handoff for the slides agent: Markov order experiments

Source: branch `experiments/music-markov`, folder `experiments/music-markov/`. Full tables in `results.md`. All numbers are 5 fold cross validation on 992 monophonic melodies from six music21 corpora (Bach chorale soprano 210, Palestrina 210, Monteverdi 49, Trecento 103, Essen folk 210, Ryan's Mammoth 210). Same folds for every method.

## Headline claims for slides

1. **The 70.9% result holds up.** Rebuilt from scratch, the 144 number first order table gets 70.2% ± 2.7 (reported 70.9%). Chance with six styles is 16.7%, majority class is 21.2%. The current slide text "baseline 20%" should read "chance 17%" or "majority class 21%".
2. **One more step of memory helps classification.** Order 2 tables (12x12x12) lift accuracy from 70.2% to 78.2%. With intervals instead of scale degrees: 74.8% to 81.4%.
3. **Beyond order 2, little gain.** Order 3 and variable order (PPM C, the IDyOM style model) give 72 to 73% as likelihood classifiers on scale degrees, within one sd of order 2 (71.8%).
4. **Variable order is the safest single choice.** It is never more than about one point below the best fixed order and is the top method overall when durations are included: 88.7%.
5. **What a node means matters more than how far back the graph looks.** Adding a duration bucket to each scale degree moves every method to 85 to 89%, a bigger jump than any change of order. (Caveat: partly notation conventions, see below.)
6. **Confusions are musically sensible.** Bach with Palestrina (vocal, stepwise), Essen folk with Ryan's fiddle tunes, Bach with Essen (simple diatonic tunes).
7. **For generation, higher order buys style by copying.** Plain sampling: order 1 melodies are recognized as their style 57% of the time, order 2 and variable order 64 to 66%. But variable order copies spans of 12 notes verbatim from training on average, and 99% of its 4 note patterns already exist in training. Order 1 copies about 8 notes.
8. **A copy limit keeps most of the gain.** Forbidding any verbatim span over 6 notes, order 2 still reaches 61% with 69% distinct 4 grams. Order 2 with this "max copy 6" sampler is the best balance and is used for all audio clips.
9. **Honest caveat for the talk.** Automatic style judges rate generated melodies above real held out excerpts (52%), so they measure typicality, not musical conviction. A listening test or LLM judge is the right next step (not run here).

## Key numbers

Classification accuracy, mean over 5 folds (%):

| node = | order 1 table + LR | order 2 table + LR | likelihood order 1 | order 2 | order 3 | variable order |
|---|---|---|---|---|---|---|
| scale degree | 70.2 | **78.2** | 62.6 | 71.8 | 72.3 | 73.3 |
| interval | 74.8 | **81.4** | 74.8 | 76.2 | 72.9 | 76.0 |
| degree + duration | 86.8 | 86.2 | 86.9 | 87.9 | 85.2 | **88.7** |

Generation, scale degrees, 600 melodies of 48 notes per cell (style accuracy is the mean of an order 1 and an order 1+2 judge):

| model | sampler | style accuracy % | longest copied span (notes) | 4 grams seen in training % | distinct 4 grams % |
|---|---|---|---|---|---|
| real held out excerpts | | 52 | 10.9 | 91 | 57 |
| order 1 | plain | 57 | 7.6 | 80 | 68 |
| order 2 | plain | 64 | 8.3 | 90 | 63 |
| order 3 | plain | 60 | 9.0 | 93 | 64 |
| variable order | plain | 65 | 12.1 | 99 | 58 |
| order 1 | max copy 6 | 54 | 6.0 | 79 | 71 |
| order 2 | max copy 6 | **61** | 6.0 | 87 | 69 |
| order 3 | max copy 6 | 57 | 6.0 | 88 | 73 |
| variable order | max copy 6 | 59 | 6.0 | 96 | 69 |

Other samplers (temperature 0.7, 1.3, top k 3) are in `results.md`. Low temperature and top k raise style scores only by repeating training material (top k 3 has 19 to 47% distinct 4 grams).

## Assets ready for slides

Figures (`experiments/music-markov/figures/`):
* `accuracy_by_order.png` three panels, accuracy vs order for each node type
* `confusion_matrices.png` four matrices (order 1 LR, order 2 LR, variable order, variable order with duration)
* `generation_style_vs_copy.png` style accuracy vs copied span, one point per order and sampler

Audio (`experiments/music-markov/audio/`), each 20 s, piano, `.wav` + `.mid` + `.json` note list `[[midi, dur_seconds], ...]`:
* `bach_real` (BWV 329 soprano, held out), `bach_order1`, `bach_order2`, `bach_order3`, `bach_ordervar`
* `essen_real` (held out folk tune), `essen_order1`, `essen_order2`, `essen_order3`, `essen_ordervar`
* All generated clips use the real melody's rhythm and key, so only the pitch order differs. Sampler max copy 6, one sample per order, fixed seed, no cherry picking.
* `experiments/music-markov/clips.json` bundles all ten note lists in the same shape as `src/clips.json`, ready for the browser player. Suggested slide: play real, then order 1, then order 2, then variable order.

## Caveats to keep in speaker notes

* Bach corpus repeats chorale tunes across harmonizations: 75 of 210 Bach melodies share a 16 note run with training. This flatters high order models on Bach a bit.
* Palestrina and Trecento editions use long note values, so the duration result partly reflects notation.
* LLM judge A/B was not run (no API key in that session). The existing slide claim "LLM judge 96 to 100% vs 60%" did not come from this run.
