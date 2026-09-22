"""Deterministic schematic SVGs; transparent, theme-safe Vault palette."""
from pathlib import Path
from html import escape
OUT=Path(__file__).parent
BLUE,PURPLE,GREEN,RED,AMBER='#2563eb','#7c3aed','#059669','#dc2626','#f59e0b'

def txt(x,y,s,size=18,anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="#888">{escape(s)}</text>'

def box(x,y,w,h,s,color=BLUE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="2"/>'+txt(x+w/2,y+h/2+6,s,18,'middle')

def save(name,w,h,body):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {w} {h}" font-family="Arial, sans-serif"><title>{name}</title>'+''.join(body)+'</svg>\n'
    (OUT/(name+'.svg')).write_text(s)

b=[txt(28,35,'Five layouts. Different promises.',29),txt(28,66,'Columns are drives; rows are stripes. Same letter = same stored data.',18)]
panels=[
(28,100,'RAID 0 · split',[['A','B','C','D'],['E','F','G','H']],'Four drives: 4C usable. No drive failure tolerated.'),
(560,100,'RAID 1 · copy',[['A','A'],['B','B']],'Two drives: C usable. Either one may fail.'),
(28,350,'RAID 5 · one parity',[['A','B','C','P0'],['D','E','P1','F'],['G','P2','H','I']],'Four drives: 3C usable. Any one may fail.'),
(560,350,'RAID 6 · two relations',[['A','B','P0','Q0'],['C','P1','Q1','D'],['P2','Q2','E','F']],'Four drives: 2C usable. Any two may fail.'),
(28,650,'RAID 10 · stripe over mirrored pairs',[['A','A','B','B'],['C','C','D','D']],'Four drives: 2C usable. One survivor needed in EACH pair.')]
for x,y,title,rows,caption in panels:
    b.append(txt(x,y,title,23))
    for d in range(len(rows[0])): b.append(txt(x+d*116+50,y+31,f'Drive {d}',16,'middle'))
    for r,row in enumerate(rows):
        for d,s in enumerate(row):
            c=PURPLE if s.startswith('P') else (GREEN if s.startswith('Q') else BLUE)
            b.append(box(x+d*116,y+45+r*46,100,36,s,c))
    b.append(txt(x,y+205,caption,17))
b.extend([txt(560,699,'RAID 10: the identity of the failures matters',20),txt(560,745,'Lose drives 0 + 2: one copy of A and B survives.',18),txt(560,783,'Lose drives 0 + 1: both copies of A disappear.',18),txt(560,826,'C = capacity of one equal-sized drive.',18),txt(560,858,'Metadata and file-system overhead omitted.',17)])
save('raid-layouts',1080,885,b)
b=[txt(30,37,'Why XOR can put a missing block back',28),txt(30,69,'One bit column at a time; no carries between columns.',18)]
rows=[('A','00111100',BLUE),('B (recovered)','10100101',GREEN),('C','01100110',BLUE),('P = A XOR B XOR C','11111111',PURPLE)]
for r,(label,bits,col) in enumerate(rows):
    y=104+r*48;b.append(txt(30,y+26,label,18))
    for j,bit in enumerate(bits):b.append(box(280+j*43,y,34,34,bit,col))
b.extend([txt(675,127,'B is missing.',23),txt(675,170,'A XOR C XOR P = B',23),txt(675,214,'10100101 is recovered.',20),txt(30,330,'WHY: A XOR A = 0, C XOR C = 0, and 0 XOR B = B.',21),txt(30,367,'Known location matters: one parity relation alone cannot locate an arbitrary corrupt block.',18)])
save('raid-xor-recovery',1040,394,b)
