"""Finite checks of the natural-pair construction. The card supplies the proof."""
from itertools import product

def equal(x,y):
    a,b=x;c,d=y
    return a+d==b+c

def add(x,y): return x[0]+y[0],x[1]+y[1]
def opposite(x): return x[1],x[0]
def multiply(x,y):
    a,b=x;c,d=y
    return a*c+b*d,a*d+b*c

def leq(x,y): return x[0]+y[1]<=x[1]+y[0]
def value(x): return x[0]-x[1]  # Independent oracle: Python's own integers.
def pad(x,t): return x[0]+t,x[1]+t

def main():
    pairs=list(product(range(6),repeat=2));checks=0
    for x,y in product(pairs,repeat=2):
        assert equal(x,y)==(value(x)==value(y))
        assert leq(x,y)==(value(x)<=value(y))
        assert value(add(x,y))==value(x)+value(y)
        assert value(multiply(x,y))==value(x)*value(y)
        for t in (0,1,100):
            assert equal(add(pad(x,t),y),add(x,y))
            assert equal(multiply(pad(x,t),y),multiply(x,y))
            assert equal(multiply(x,pad(y,t)),multiply(x,y))
        assert equal(add(x,opposite(x)),(0,0))
        checks+=14
    small=list(product(range(3),repeat=2))
    for x,y,z in product(small,repeat=3):
        assert equal(multiply(multiply(x,y),z),multiply(x,multiply(y,z)))
        assert equal(multiply(x,add(y,z)),add(multiply(x,y),multiply(x,z)))
        checks+=2
    decode=lambda word:word if word<128 else word-256
    for word in range(256):
        expected=decode(word)+1
        if expected==128:expected=-128
        assert decode((word+1)%256)==expected
    assert 127+1==128 and (10**100+1)-10**100==1
    assert -7//3==-3 and -7%3==2 and -7==(-7//3)*3+(-7%3)
    print(f'PASS: {checks} pair/ring assertions; all 256 byte increments; Python integer contrast.')
if __name__=='__main__':main()
