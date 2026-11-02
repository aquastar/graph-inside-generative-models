"""Figures and markdown tables from results/*.json."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common import STYLES, LABELS, REP_NAMES, KMAX

INK, INK2, GRID, SURF = '#0b0b0b', '#52514e', '#e4e3df', '#fcfcfb'
BLUE, ORANGE, AQUA, YELLOW = '#2a78d6', '#eb6834', '#1baf7a', '#eda100'
plt.rcParams.update({'font.size': 10, 'axes.edgecolor': INK2, 'axes.labelcolor': INK, 'xtick.color': INK2,
                     'ytick.color': INK2, 'figure.facecolor': SURF, 'axes.facecolor': SURF, 'savefig.facecolor': SURF,
                     'axes.spines.top': False, 'axes.spines.right': False})
C = json.load(open('results/classification.json'))
M = C['methods']
G = json.load(open('results/generation_summary.json'))

# ---------- accuracy by order ----------
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True)
xs = ['0', '1', '2', '3', 'var']
for ax, rep in zip(axes, ['pc', 'int', 'pcdur']):
    ll = [M[f'{rep}|LL ' + (f'order {o}' if o != 'var' else f'variable (PPM C, max {KMAX})')] for o in xs]
    lr = [M[f'{rep}|LR order {o}'] for o in ('1', '2')]
    ax.errorbar(range(5), [m['acc_mean'] * 100 for m in ll], [m['acc_sd'] * 100 for m in ll], color=BLUE, lw=2,
                marker='o', ms=8, capsize=3, label='likelihood classifier')
    ax.errorbar([1, 2], [m['acc_mean'] * 100 for m in lr], [m['acc_sd'] * 100 for m in lr], color=ORANGE, lw=2,
                marker='s', ms=8, capsize=3, label='table features + logistic regression')
    ax.axhline(100 * max(C['counts'].values()) / sum(C['counts'].values()), color=INK2, lw=1, ls=':')
    ax.set_xticks(range(5), ['0', '1', '2', '3', f'variable\n(PPM C)'])
    ax.set_title(REP_NAMES[rep], color=INK, fontsize=11)
    ax.yaxis.grid(True, color=GRID)
    ax.set_axisbelow(True)
    ax.set_ylim(15, 95)
    ax.set_xlabel('Markov order')
axes[0].set_ylabel('5 fold accuracy (%)')
axes[0].text(4, 23, 'majority class', color=INK2, ha='right', fontsize=8)
axes[1].legend(frameon=False, loc='lower right', fontsize=9)
fig.suptitle('Style classification accuracy by Markov order (6 styles, 992 pieces, mean and sd over 5 folds)', color=INK)
fig.tight_layout()
fig.savefig('figures/accuracy_by_order.png', dpi=160)
plt.close(fig)

# ---------- confusion matrices ----------
picks = ['pc|LR order 1', 'pc|LR order 2', f'pc|LL variable (PPM C, max {KMAX})', f'pcdur|LL variable (PPM C, max {KMAX})']
titles = ['pitch class, order 1 table + LR', 'pitch class, order 2 table + LR',
          'pitch class, variable order likelihood', 'pitch class + duration, variable order likelihood']
fig, axes = plt.subplots(1, 4, figsize=(18, 4.9))
for ax, k, t in zip(axes, picks, titles):
    cm = np.array(M[k]['cm'], float)
    cmn = cm / cm.sum(1, keepdims=True)
    ax.imshow(cmn, cmap=matplotlib.colors.LinearSegmentedColormap.from_list('b', ['#fcfcfb', '#cde2fb', '#5598e7', '#184f95']), vmin=0, vmax=1)
    for i in range(6):
        for j in range(6):
            ax.text(j, i, f'{cmn[i, j]*100:.0f}', ha='center', va='center', fontsize=9,
                    color='white' if cmn[i, j] > 0.55 else INK)
    lab = [LABELS[s] for s in STYLES]
    ax.set_xticks(range(6), lab, rotation=40, ha='right')
    ax.set_yticks(range(6), lab if ax is axes[0] else [''] * 6)
    ax.set_title(f'{t}\nacc {M[k]["acc_mean"]*100:.1f}%', fontsize=10, color=INK)
    ax.set_xlabel('predicted')
    ax.spines[:].set_visible(False)
axes[0].set_ylabel('true style')
fig.suptitle('Confusion matrices, row normalized percent, pooled over the 5 held out folds', color=INK)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig('figures/confusion_matrices.png', dpi=160)
plt.close(fig)

# ---------- generation: style accuracy vs copying ----------
fig, ax = plt.subplots(figsize=(7.5, 5))
ocol = {'1': BLUE, '2': ORANGE, '3': AQUA, 'var': YELLOW}
mk = {'ancestral': 'o', 'temp 0.7': 'v', 'temp 1.3': '^', 'top k 3': 's', 'max copy L=6': 'D'}
S = G['summary']
for d in S[1:]:
    ax.scatter(d['longest_copy'], 100 * (d['style_acc'] + d['style_acc12']) / 2, s=70, c=ocol[d['order']],
               marker=mk[d['sampler']], edgecolors=SURF, linewidths=1.5, zorder=3)
r = S[0]
ax.scatter(r['longest_copy'], 100 * (r['style_acc'] + r['style_acc12']) / 2, s=140, c=INK, marker='*', zorder=3)
ax.annotate('real held out excerpts', (r['longest_copy'], 100 * (r['style_acc'] + r['style_acc12']) / 2),
            xytext=(6, -12), textcoords='offset points', fontsize=9, color=INK)
from matplotlib.lines import Line2D
h = [Line2D([], [], color=c, marker='o', ls='', ms=8, label=f'order {o}' if o != 'var' else 'variable order') for o, c in ocol.items()]
h += [Line2D([], [], color=INK2, marker=m, ls='', ms=8, label=s) for s, m in mk.items()]
ax.legend(handles=h, frameon=False, fontsize=8, loc='upper left', ncol=2)
ax.set_ylim(44, 72)
ax.set_xlabel('mean longest span copied verbatim from training (notes)')
ax.set_ylabel('style accuracy of generated melodies (%)\nmean of order 1 and order 1+2 judges')
ax.yaxis.grid(True, color=GRID)
ax.set_axisbelow(True)
ax.set_title('Generation: style fidelity vs copying (48 note melodies, 600 per cell)', color=INK, fontsize=11)
fig.tight_layout()
fig.savefig('figures/generation_style_vs_copy.png', dpi=160)
plt.close(fig)

# ---------- markdown tables ----------
L = []
L.append('| representation | method | order | accuracy % (mean ± sd) | macro F1 % (mean ± sd) |')
L.append('|---|---|---|---|---|')
for k, m in M.items():
    rep, name = k.split('|')
    fam = 'table features + LR' if m['family'] == 'LR' else 'likelihood classifier'
    o = m['order'] if m['order'] != 'var' else f'variable (PPM C, max {KMAX})'
    L.append(f"| {REP_NAMES[rep]} | {fam} | {o} | {m['acc_mean']*100:.1f} ± {m['acc_sd']*100:.1f} | {m['f1_mean']*100:.1f} ± {m['f1_sd']*100:.1f} |")
L.append('\nCONFUSED\n')
L.append('| method | top confused pairs (pieces misassigned in either direction, pooled over folds) |')
L.append('|---|---|')
for k in picks + ['int|LR order 2']:
    cm = np.array(M[k]['cm'])
    pairs = sorted(((cm[i, j] + cm[j, i], i, j) for i in range(6) for j in range(i + 1, 6)), reverse=True)[:3]
    L.append(f"| {k.replace('|', ', ')} | " + ', '.join(f'{LABELS[STYLES[i]]} and {LABELS[STYLES[j]]} ({n})' for n, i, j in pairs) + ' |')
L.append('\nGEN\n')
L.append('| order | sampler | style acc, order 1 judge % | style acc, order 1+2 judge % | longest copied span (notes) | 4 grams seen in training % | distinct 4 grams % | pairwise edit distance |')
L.append('|---|---|---|---|---|---|---|---|')
for d in S:
    o = d['order'] if d['order'] in ('real held out',) else ('variable (PPM C)' if d['order'] == 'var' else d['order'])
    L.append(f"| {o} | {d['sampler'] or 'n/a'} | {d['style_acc']*100:.1f} ± {d['style_acc_sd']*100:.1f} | {d['style_acc12']*100:.1f} ± {d['style_acc12_sd']*100:.1f} | {d['longest_copy']:.1f} | {d['seen4']*100:.1f} | {d['distinct4']*100:.1f} | {d['pair_edit']:.2f} |")
L.append('\nBYSTYLE\n')
L.append('| order | sampler | ' + ' | '.join(LABELS[s] for s in STYLES) + ' |')
L.append('|---|---|' + '---|' * 6)
for d in S:
    if d['sampler'] in ('', 'ancestral', G['best_sampler']):
        L.append(f"| {d['order']} | {d['sampler'] or 'n/a'} | " + ' | '.join(f"{d['style_acc_by_style'][s]*100:.0f}" for s in STYLES) + ' |')
L.append('\nSENS\n')
L.append('| Lidstone alpha | order 1 | order 2 | order 3 |')
L.append('|---|---|---|---|')
for a in ('0.01', '0.1', '1.0'):
    L.append(f'| {a} | ' + ' | '.join(f"{C['alpha_sensitivity_pc'][f'alpha={a}, order {k}']*100:.1f}" for k in (1, 2, 3)) + ' |')
open('results/tables.md', 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))
