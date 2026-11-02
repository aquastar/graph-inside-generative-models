import random, math
random.seed(7)
W,H=760,600
cols=[70,190,310,430,550,670]
nodes=[]
for ci,x in enumerate(cols):
    n=7 if ci not in (0,5) else 5
    top=(H-(n-1)*66)/2
    for k in range(n):
        nodes.append((ci,x+random.uniform(-10,10),top+k*66+random.uniform(-8,8)))
bycol={}
for i,(c,x,y) in enumerate(nodes): bycol.setdefault(c,[]).append(i)
out=[]
# faint dense edges between adjacent columns
for c in range(5):
    for a in bycol[c]:
        for b in bycol[c+1]:
            out.append(f'<line x1="{nodes[a][1]:.1f}" y1="{nodes[a][2]:.1f}" x2="{nodes[b][1]:.1f}" y2="{nodes[b][2]:.1f}" stroke="#8a969e" stroke-opacity=".13" stroke-width="1"/>')
# hidden graph: two highlighted subgraphs (language orange, music teal)
def path(seq,color,w,start=0.0):
    s=[]
    for k,(a,b) in enumerate(zip(seq,seq[1:])):
        ln=math.hypot(nodes[b][1]-nodes[a][1], nodes[b][2]-nodes[a][2])
        s.append(f'<line class="hl" style="--len:{ln:.0f};--d:{start+k*0.35:.2f}s" x1="{nodes[a][1]:.1f}" y1="{nodes[a][2]:.1f}" x2="{nodes[b][1]:.1f}" y2="{nodes[b][2]:.1f}" stroke="{color}" stroke-opacity=".9" stroke-width="{w}" stroke-linecap="round"/>')
    return s
L=[bycol[0][1],bycol[1][2],bycol[2][1],bycol[3][2],bycol[4][3],bycol[5][2]]
L2=[bycol[1][2],bycol[2][3],bycol[3][2]]
L3=[bycol[2][1],bycol[3][1],bycol[4][3]]
M=[bycol[0][3],bycol[1][5],bycol[2][5],bycol[3][4],bycol[4][5],bycol[5][3]]
M2=[bycol[2][5],bycol[3][6],bycol[4][5]]
out+=path(L,"#F76902",3.5,0.2)+path(L2,"#F76902",3,0.55)+path(L3,"#F76902",3,0.9)
out+=path(M,"#38b2c4",3.5,0.4)+path(M2,"#38b2c4",3,1.1)
hot=set(L+L2+L3); cool=set(M+M2)
for i,(c,x,y) in enumerate(nodes):
    if i in hot:
        out.append(f'<circle class="hg" style="--d:{c*0.35+0.2:.2f}s" cx="{x:.1f}" cy="{y:.1f}" r="16" fill="url(#glowO)"/><circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="#F76902"/>')
    elif i in cool:
        out.append(f'<circle class="hg" style="--d:{c*0.35+0.4:.2f}s" cx="{x:.1f}" cy="{y:.1f}" r="16" fill="url(#glowT)"/><circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="#38b2c4"/>')
    else:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#1c2430" stroke="#6f7c86" stroke-width="1.5"/>')
# input glyphs: text token and music note at left
lx,ly=nodes[L[0]][1],nodes[L[0]][2]
mx,my=nodes[M[0]][1],nodes[M[0]][2]
out.append(f'<text x="{lx-30:.1f}" y="{ly+12:.1f}" font-size="42" font-family="Fira Sans" font-weight="700" fill="#F76902" text-anchor="end">Aa</text>')
out.append(f'<text x="{lx-30:.1f}" y="{ly+40:.1f}" font-size="22" font-family="Fira Sans" font-weight="600" fill="#F76902" text-anchor="end">language</text>')
out.append(f'<text x="{mx-30:.1f}" y="{my+16:.1f}" font-size="56" fill="#1f8a9a" text-anchor="end">&#9835;</text>')
out.append(f'<text x="{mx-30:.1f}" y="{my+44:.1f}" font-size="22" font-family="Fira Sans" font-weight="600" fill="#1f8a9a" text-anchor="end">music</text>')
svg=f'''<svg class="herofig" viewBox="-130 0 {W+130} {H}" aria-hidden="true"><defs><radialGradient id="glowO"><stop offset="0" stop-color="#F76902" stop-opacity=".5"/><stop offset="1" stop-color="#F76902" stop-opacity="0"/></radialGradient><radialGradient id="glowT"><stop offset="0" stop-color="#38b2c4" stop-opacity=".5"/><stop offset="1" stop-color="#38b2c4" stop-opacity="0"/></radialGradient></defs>{"".join(out)}</svg>'''
open('hero.svg','w').write(svg)
