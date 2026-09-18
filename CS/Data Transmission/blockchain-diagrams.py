"""Regenerate the two static schematic figures; no third-party dependencies."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
BLUE, PURPLE, GREEN, RED, AMBER = '#2563eb', '#7c3aed', '#059669', '#dc2626', '#f59e0b'


def text(x,y,label,size=17,anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="#888">{escape(label)}</text>'


def box(x,y,w,h,color):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" fill-opacity="0.10" stroke="{color}" stroke-width="2"/>'


def arrow(x1,y1,x2,y2,color=BLUE):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="2" marker-end="url(#arrow)"/>'


def save(name,height,parts,title):
    head=f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 760 {height}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#888" stroke-width="1.5"/></marker></defs><g font-family="Arial, sans-serif">'
    (ROOT/name).write_text(head+''.join(parts)+'</g></svg>\n')


p=[text(380,30,'Changing a record changes what later blocks refer to',21),
   text(195,70,'Original history',19),text(565,70,'Edited copy',19)]
for col,x in enumerate([30,400]):
    for i in range(3):
        y=92+i*157
        color=BLUE if not col else (RED if i==0 else AMBER)
        p += [box(x,y,330,108,color),text(x+165,y+27,f'Block {i+1}',18)]
        if i==0:
            p += [text(x+165,y+56,'Alice pays Bob '+('7' if not col else '6')),
                  text(x+165,y+84,'hash = h1' if not col else "new hash = h1′")]
        else:
            p += [text(x+165,y+56,f'previous hash = h{i}'),
                  text(x+165,y+84,f'hash = h{i+1}' if not col else ('link fails: h1 ≠ h1′' if i==1 else 'repair above → changes here'))]
        if i<2:p.append(arrow(x+165,y+113,x+165,y+150,color))
p += [text(380,562,'Repairing every later hash can make a local copy consistent.',18),
      text(380,590,'It cannot make the network accept that history.',18)]
save('blockchain-links.svg',614,p,'Original and edited hash-linked histories')

p=[text(380,32,'A payment: authorise → validate → propose → agree',21)]
steps=[('1  Wallet signs and broadcasts','Payment data + authorisation; private key stays private',BLUE),
       ('2  Peers validate','Check signature, available funds and no repeated spend',PURPLE),
       ('3  A producer proposes a block','Batch records + timestamp + previous-block hash',AMBER),
       ('4  Nodes validate and apply consensus rules','Accept a history; update ledger copies as it propagates',GREEN)]
for i,(title,body,color) in enumerate(steps):
    y=60+i*123
    p += [box(35,y,690,91,color),text(380,y+32,title,20),text(380,y+64,body,17)]
    if i<3:p.append(arrow(380,y+95,380,y+119,color))
p += [text(380,551,'A valid signature is not a guarantee of funds, freshness or finality.',17)]
save('blockchain-payment.svg',576,p,'Payment through signature, validation, block proposal and agreement')
