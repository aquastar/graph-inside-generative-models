# Slide style spec v2 (2026-11-02)

House style for Zhiqian Chen's academic talks. First used in "Is There a Graph Inside Generative Models?" (Reveal.js, inline SVG from Python, 16:9, figures on a 1180 wide viewBox). v1 was reviewed by a Fable research agent (contrast and colorblind simulation, font file inspection, Reveal.js source). This version merges that review.

Taste it encodes: Tufte typography, soft warm neutrals, the official RIT palette, diagrams in the manner of Transformer Circuits, TikZ level line quality. Avoids both the "AI generated" look (colored pill boxes, rainbow accents, centered bold takeaway on every slide) and the stereotyped Beamer look (Metropolis, Touying University, Fira Sans).

## 1. Principles
1. Ink carries information. No box, color or line without a meaning.
2. Warm neutrals do the work. One accent, RIT orange, marks "ours" or "the point of this slide", at most one orange item per slide.
3. One color, one meaning, fixed for the whole talk. Color never carries text by itself: text is ink, the color sits on a mark beside it.
4. Label directly on the figure. Legends only above four series.
5. The headline is a full sentence with the conclusion. No takeaway banner.
6. Glance test: the point of a slide registers in about three seconds (Duarte).

## 2. Palette (RIT brand portal values plus near neutrals)
Contrast ratios on bg #FBFAF7.
| Token | Hex | Contrast | Use |
|---|---|---|---|
| bg | #FBFAF7 | | background, deliberate warm tolerance on RIT white |
| ink | #1F1E1B | 16.0 | headlines, body, numbers |
| ink2 | #5F5D50 | 6.4 | labels, captions, ticks, sidenotes |
| line | #7C878E | 3.5 | RIT PMS 430, structural lines that carry meaning |
| axis | #ACA39A | 2.4 | RIT Warm Gray 5, axes, baselines, inactive nodes and edges |
| rule | #D7D2CB | 1.4 | RIT Warm Gray 1, optional gridlines only |
| group | #EFEBE5 | | group fill when whitespace is not enough |
| accent | #F76902 | 2.9 | RIT orange, marks only (strokes 2.5 px and up, fills, underline under the big number) |
| accent-tint | #FAD6BA | | fill for ours |
| lang | #009CBD | 3.1 | RIT teal, language domain marks, text only at 24 px and up |
| lang-tint | #BCE2E8 | | language fills |
| music | #7D55C7 | 5.0 | RIT purple, music domain marks and text |
| music-tint | #DCD1EB | | music fills |
| fail | #DA291C | 4.7 | RIT red, failure only, always with a dashed stroke or an x mark |
Rules: no green (it is invisible against orange for deuteranopes, success is the unmarked state). No gradients, no shadows. Tints are 25%, lighter tints vanish on projectors. Exception: the cover title word may be orange at display size (100 px and up). If a colored word is unavoidable elsewhere, use accent-text #C45200 (4.4, off brand, slides only).

## 3. Typography
Three families only.
- ET Book (Tufte's face, MIT license, self hosted). Two CSS families as in tufte-css: "et-book" (roman with lining figures, bold, display italic) and "et-book-osf" (roman with oldstyle figures, running text only). The free ET Book has no OpenType features and no small caps, so switch by family, never by font-feature-settings.
  Use: headline 40 px roman (not bold), body sentences 30 to 32 px, quotes, the one big number 40 px. Never below 24 px, never in ink2 below 24 px, italic only at 24 px and up.
- Source Sans 3 (SIL OFL): every label, tick, number in a chart, sidenote, section marker, status tag. 18 to 20 px, weight 400, ink2. Bold only for the one emphasized label. Lining tabular figures by default. Section markers and status tags in real small caps (font-variant-caps: all-small-caps), letter spacing 0.06em.
- Source Code Pro: code only, 20 px.
- Size ratio largest to smallest about 2.2 (Wilke: keep it near 2). Everything left aligned except the cover.

## 4. Lines, shapes, graphs
- Gridlines 1 px rule. Axes 1 px axis. Meaningful structure 1.5 px line or ink2. Emphasized path 2.5 px accent.
- Arrowheads: small filled triangles about 7 px long (TikZ stealth). Round joins.
- Boxes: no border. Group by whitespace first, group fill second, radius 3 px. No pills anywhere. Status (Published, Under review, In progress, Open question) is a small caps label in ink2 with a 2 px underline in a status color.
- Graph encoding, fixed for the talk: nodes 7 px radius, full domain color, no stroke (tints are too pale for nodes on a projector). The edited or active node is orange at 8 px. A wrong answer is a hollow node with a 2 px red ring, its label in ink and the expected answer below in ink2. Language nodes are circles, music nodes are rounded squares. Edge width by magnitude (sqrt scale, 0.5 to 3 px). Sign or failure by dashed vs solid. Direction by stealth head. Context edges at 5% ink. Layers as horizontal bands labeled at left in Source Sans (the Transformer Circuits layout).
- Ours: solid 2.5 px orange stroke or filled orange node plus the method name in small caps. Baselines gray, dashed when they are comparison methods.

## 5. Layout
- Margins 64 px left and right. 12 columns, about 80 px with 16 px gutters. Spacing scale 8, 16, 24, 32, 48, 64.
- Headline baseline at 88, content from 136, bottom safe line 600, sidenote baseline 632 (on a 1280 by 720 slide).
- Section marker top left in small caps (OVERVIEW, 1 LANGUAGE, 2 MUSIC, CLOSE). No progress bar.
- Headline at most two lines, about 70 characters, no terminal period, a question only if the slide answers it.
- Body text at most 25 words outside the headline, at most three bullets, bullets only for parallel items.
- Citation as one Tufte sidenote: bottom right, Source Sans 18 px ink2, author year venue, no DOI. No logos except cover and close.
- Photos of people: plain squares, radius 6 px, at most 160 px, no ring or shadow, on at most two slides. Name in Source Sans 18 px ink, credential in ink2. Screenshots get a 1 px rule under them, no shadow.

## 6. Charts
- Horizontal bars when labels are long. Value at the bar end in Source Sans, difference as +8 in ink2 beside it.
- Baselines in axis gray, ours in accent, partial variants in accent-tint. No frame, no vertical gridlines, at most one reference line.
- One number to remember: ET Book 40 px ink with a 3 px orange rule under it, plus one line in Source Sans saying what it measures and which direction is better.

## 7. Equations and code
- MathJax 4 with the mathjax-pagella font, pre-rendered to SVG at build time, sized 1 em to the ET Book text. Only the term being discussed gets the accent (as an underline mark).
- Code: at most 12 lines, no syntax rainbow, one highlighted line on accent-tint.

## 8. Production pipeline
1. Primary: one Python style module (tokens, T, R, L, P, node, edge, bar, sidenote helpers) used for every SVG, static or animated. Text stays as text with classes mapped to the page fonts. Every node and edge carries an id and data-id so fragments and Reveal auto-animate can address them. D3 or elkjs only when a layout needs it.
2. Secondary: TikZ for a static figure whose layout benefits from TikZ libraries. Route: DVI mode (dvilualatex with fontspec and ET Book, or latex with fbb), pgfsys-dvisvgm driver, dvisvgm --font-format=woff2 --exact-bbox --optimize, then strip embedded fonts and map to the page fonts. pdftocairo or dvisvgm --pdf turn text into outlines, acceptable only as a last resort for one figure.
3. Build gate: a script checks the tokens and every SVG text fill for contrast (text 4.5, meaningful graphics 3.0), simulates color vision deficiency on each figure, and fails on violations. Keep the existing checks (no em dash, en dash or semicolon in visible text, at most 4 fragment steps).

## 9. Motion
Fade only, 250 ms, at most four steps, each step one meaningful unit. Reveal auto-animate when the same figure returns (add fill, stroke and stroke-width to autoAnimateStyles if colors should morph).

## 10. Do not
Colored pill boxes for content, rainbow accents, per-section accent colors, centered bold takeaway banners, generic icons (check marks in circles, light bulbs), emoji, drop shadows, gradients, all caps headlines, Fira Sans, colored body text, two orange items on one slide.

## 11. Open
- Test the TikZ DVI route with ET Book end to end before relying on it.
- Check the warm white and the tints once on the real room projector.
- A dark venue variant (bg #1A1917, ink #EDEBE6, same roles) only if needed.

## References
- ET Book https://github.com/edwardtufte/et-book and Tufte CSS https://github.com/edwardtufte/tufte-css
- Transformer Circuits methods https://transformer-circuits.pub/2025/attribution-graphs/methods.html and frontend https://github.com/anthropics/attribution-graphs-frontend
- Wilke, Fundamentals of Data Visualization, color pitfalls https://clauswilke.com/dataviz/color-pitfalls and slides https://clauswilke.com/lectures/slides/effective-visualization-2025-04-02.html
- Prinzipien, Touying theme after Doumont https://github.com/Entze/prinzipien
- quarto-revealjs-clean https://github.com/grantmcdermott/quarto-revealjs-clean
- Duarte glance test https://www.duarte.com/resources/slide-glance-test/
- RIT brand colors https://www.rit.edu/brandportal/colors and typography https://www.rit.edu/brandportal/typography
- MathJax 4 fonts https://docs.mathjax.org/en/v4.1/output/fonts.html
