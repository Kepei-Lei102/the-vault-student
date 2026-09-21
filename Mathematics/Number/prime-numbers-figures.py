"""Two reproducible teaching schematics; no external assets."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parent
GREY='#888'
def svg(body,w=800,h=360):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {w} {h}"><style>text{{font-family:Arial,sans-serif;fill:#888}} .t{{font-size:22px;font-weight:600}} .b{{font-size:18px}} .s{{font-size:16px}}</style>{body}</svg>\n'
def text(x,y,s,cls='b'):
 return f'<text x="{x}" y="{y}" text-anchor="middle" class="{cls}">{escape(s)}</text>'
def box(x,y,w,h,color='#2563eb'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" fill-opacity=".12" stroke="{color}" stroke-width="2"/>'
def line(x1,y1,x2,y2):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#888" stroke-width="2"/>'
b=text(400,30,'A finite list cannot trap every prime','t')
b+=box(30,55,740,62)+text(400,94,'Proposed list: 2, 3, 5, 7, 11, 13')
b+=line(400,117,400,144)+box(30,145,740,62,'#7c3aed')+text(400,184,'Product + 1 = 30031. Every listed prime leaves remainder 1.')
b+=line(400,207,210,235)+line(400,207,590,235)
b+=box(40,236,340,70,'#059669')+text(210,265,'59 is a prime divisor')+text(210,290,'and was not on the list.','s')
b+=box(420,236,340,70,'#059669')+text(590,265,'509 is another prime divisor')+text(590,290,'and was not on the list.','s')
b+=text(400,340,'30031 is composite. The proof only needs a NEW prime factor.','s')
(ROOT/'prime-numbers-euclid.svg').write_text(svg(b))
b=text(400,30,'Different routes, identical prime ingredients','t')
# Explicit trees: endpoints stop at the circular node boundaries.
def tree(offset,coords,edges,labels,leaves):
 out=''
 from math import hypot
 for a,c in edges:
  x,y=coords[a];u,v=coords[c];dx,dy=u-x,v-y;d=hypot(dx,dy)
  out+=line(offset+x+23*dx/d,y+23*dy/d,offset+u-23*dx/d,v-23*dy/d)
 for i,(x,y) in enumerate(coords):
  color='#059669' if i in leaves else '#2563eb'
  out+=f'<circle cx="{offset+x}" cy="{y}" r="23" fill="{color}" fill-opacity=".12" stroke="{color}" stroke-width="2"/>'+text(offset+x,y+6,str(labels[i]))
 return out
coords=[(200,80),(110,150),(290,150),(55,225),(165,225),(235,225),(345,225)]
b+=tree(0,coords,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)],[60,6,10,2,3,2,5],{3,4,5,6})
coords2=[(200,80),(110,150),(290,150),(55,225),(165,225),(235,225),(345,225)]
b+=tree(400,coords2,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)],[60,4,15,2,2,3,5],{3,4,5,6})
b+=text(200,290,'60 = 6 × 10 = 2 × 3 × 2 × 5','s')+text(600,290,'60 = 4 × 15 = 2 × 2 × 3 × 5','s')
b+=text(400,340,'After reordering: 2, 2, 3, 5. Euclid’s lemma proves this agreement is inevitable.','s')
(ROOT/'prime-numbers-factor-trees.svg').write_text(svg(b))
