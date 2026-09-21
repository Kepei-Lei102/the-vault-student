"""Run the Prime Numbers examples and boundary checks. Standard library only."""
from math import isqrt, prod, gcd, factorial

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def sieve(limit):
    if limit < 2:
        return []
    survives = [True] * (limit + 1)
    survives[0] = survives[1] = False
    for p in range(2, isqrt(limit) + 1):
        if survives[p]:
            for multiple in range(p * p, limit + 1, p):
                survives[multiple] = False
    return [n for n in range(2, limit + 1) if survives[n]]

def factor(n):
    if n < 1:
        raise ValueError('factor expects a positive integer')
    factors=[]
    d=2
    while d*d<=n:
        while n%d==0:
            factors.append(d);n//=d
        d+=1
    if n>1:factors.append(n)
    return factors

def bezout(a,b):
    old_r,r=a,b; old_s,s=1,0;old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s,old_t

def verify():
    for bound in [-3,0,1,2,3,4,9,25,49,100,997,10000]:
        assert sieve(bound)==[n for n in range(2,bound+1) if is_prime(n)]
    assert sieve(100)[-1]==97 and len(sieve(100))==25
    assert len(sieve(1_000_000))==78498
    for n in range(1,2000):
        fs=factor(n)
        assert prod(fs)==n and all(is_prime(p) for p in fs)
    for a in range(1,40):
        for b in range(1,40):
            d,x,y=bezout(a,b)
            assert d==gcd(a,b)==a*x+b*y
    for p in sieve(100):
        assert all((a*pow(a,-1,p))%p==1 for a in range(1,p))
    for m in range(2,10):
        assert all(not is_prime(factorial(m+1)+j) for j in range(2,m+2))
    assert factor(30031)==[59,509]
    assert all(30031%p==1 for p in [2,3,5,7,11,13])
    assert factor(540)==[2,2,3,3,3,5]
    assert isqrt(540*15)**2==540*15
    assert all(isqrt(540*m)**2!=540*m for m in range(1,15))
    assert [5,7,11]==sieve(11)[2:] and sum([5,7,11])%5!=0
    # Verify the precise code displayed in Markdown, independently of this module.
    from pathlib import Path
    s=Path(__file__).with_name('Prime Numbers.md').read_text()
    block=s.split('```python\n',1)[1].split('```',1)[0]
    namespace={};exec(compile(block,'Prime Numbers.md','exec'),namespace)
    assert namespace['sieve'](10000)==sieve(10000)
    print('PASS: displayed code; independent sieve/trial comparison; factors; Bezout; inverses; gaps; changed bounds.')
    print('Primes through 100:',sieve(100))
    print('30031 factors:',factor(30031),' | 540 × 15 =',540*15)
    print('Inverses mod 7:',{a:pow(a,-1,7) for a in range(1,7)})

if __name__=='__main__':verify()
