"""Regenerate the heap layout schematic, with computed parent-child endpoints."""
from pathlib import Path
from math import hypot
P=Path(__file__).parent
points=[(350,70),(180,155),(520,155),(95,240),(265,240),(435,240),(605,240)]
values=[2,5,3,9,7,8,4]
s=['<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 700 420">',
   '<style>text{font-family:Arial,sans-serif;fill:#888;text-anchor:middle;font-size:20px}.small{font-size:15px}</style>']
s.append('<text x="350" y="25">Same keys, two views: a tree stored as an array</text>')
for i in range(1,7):
 x,y=points[(i-1)//2];u,v=points[i];d=hypot(u-x,v-y);dx=(u-x)*24/d;dy=(v-y)*24/d
 s.append(f'<line x1="{x+dx:.3f}" y1="{y+dy:.3f}" x2="{u-dx:.3f}" y2="{v-dy:.3f}" stroke="#888" stroke-width="2"/>')
for i,((x,y),v) in enumerate(zip(points,values)):
 s.extend([f'<circle cx="{x}" cy="{y}" r="24" fill="rgba(37,99,235,0.15)" stroke="#2563eb" stroke-width="2"/>',f'<text x="{x}" y="{y+7}">{v}</text>',f'<text class="small" x="{x+38}" y="{y+5}">i={i}</text>'])
for i,v in enumerate(values):
 x=82+i*89
 s.extend([f'<rect x="{x-32}" y="307" width="64" height="46" rx="5" fill="rgba(8,145,178,0.15)" stroke="#0891b2" stroke-width="2"/>',f'<text x="{x}" y="337">{v}</text>',f'<text class="small" x="{x}" y="377">i={i}</text>'])
s.append('<text x="350" y="408" class="small">Children of i: 2i + 1 and 2i + 2 • valid indices only • root has no parent</text></svg>')
(P/'heap-array-tree.svg').write_text('\n'.join(s)+'\n')
