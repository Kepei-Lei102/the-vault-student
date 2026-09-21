"""Regenerate the schematic; discrete idealised reception, not a radio simulation."""
from pathlib import Path
from html import escape
SCHEDULE = [1, 4, 2, 3, 1, 2, 4, 3]
def received(tx, rx, blocked):
    if len(tx) != len(rx):
        raise ValueError('Compare equal-length time windows')
    return sum(a == b and a not in blocked for a,b in zip(tx,rx))
def render():
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1000 460">','<style>text{font-family:Arial,sans-serif;fill:#888;font-size:19px}</style>']
    def text(x,y,t,size=19,anchor='middle'):
        s.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-size:{size}px">{escape(t)}</text>')
    text(500,32,'Same sequence is not enough: the timing must match',25)
    text(500,63,'Eight equal time slots; channel 2 is blocked throughout',18)
    text(20,113,'Time slot',18,'start')
    for i in range(8):text(275+78*i,113,str(i+1))
    scenarios=[('Fixed on channel 2',[2]*8,[2]*8),('Hopping together',SCHEDULE,SCHEDULE),('Receiver one slot late',SCHEDULE,SCHEDULE[-1:]+SCHEDULE[:-1])]
    for r,(label,tx,rx) in enumerate(scenarios):
        y=147+r*93
        text(20,y+14,label,18,'start');text(20,y+42,'send / listen',16,'start')
        for i,(a,b) in enumerate(zip(tx,rx)):
            col='#059669' if a==b and a!=2 else '#dc2626';x=244+i*78
            s.append(f'<rect x="{x}" y="{y-9}" width="62" height="57" rx="6" fill="{col}" fill-opacity="0.13" stroke="{col}" stroke-width="2"/>')
            text(x+31,y+15,f'{a} / {b}',18);text(x+31,y+37,'OK' if col=='#059669' else 'lost',13)
        text(939,y+22,f'{received(tx,rx,{2})} / 8',22)
    text(500,436,'Green = matching clear channel. Red = blocked channel or mismatched tuning.',17)
    s.append('</svg>');Path(__file__).with_suffix('.svg').write_text('\n'.join(s)+'\n')
if __name__=='__main__':
    assert received([2]*8,[2]*8,{2})==0
    assert received(SCHEDULE,SCHEDULE,{2})==6
    assert received(SCHEDULE,SCHEDULE,{1,2})==4
    assert received(SCHEDULE,SCHEDULE,set())==8
    assert received(SCHEDULE,SCHEDULE,SCHEDULE)==0
    assert received(SCHEDULE,SCHEDULE[-1:]+SCHEDULE[:-1],set())==0
    assert received([1,1,1],[1,1,1],set())==3  # a shifted constant schedule need not fail
    try:received([1],[],set())
    except ValueError:pass
    else:raise AssertionError('Unequal windows accepted')
    render();print('Eight meaningful reception checks passed; schematic regenerated.')
