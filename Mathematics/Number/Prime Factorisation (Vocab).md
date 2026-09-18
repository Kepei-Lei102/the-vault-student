---
chinese: 质因数分解 (zhì yīnshù fēnjiě)
prerequisites:
  - "[[Factors and Multiples (Vocab)]]"
leads_to:
  - "[[Prime Numbers]]"
  - "[[Powers and Roots (Vocab)]]"
  - "[[Heptadecagon]]"
  - "[[Surds]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N4
  - syllabus/0580-E1-1
  - type/vocabulary
---

# Prime Factorisation 质因数分解

## Definition

**Prime factorisation** is writing a number as a product of its prime factors. Every integer greater than 1 has exactly one prime factorisation (ignoring the order of factors). This uniqueness is the **Fundamental Theorem of Arithmetic**.

$$360 = 2^3 \times 3^2 \times 5$$

### 中文锚点

24块饼干，可以先分成2盒、每盒12块，也可以先分成3盒、每盒8块。接着把12或8继续拆成几个相同的小组，把得到的数也这样往下拆，直到每个数都只能拆成1乘自己。两条路最后都会留下2、2、2、3。质因数分解找的不是哪种装盒方法最好，而是不管从哪里开始分，这个数背后总会露出的那几个乘法积木。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| prime (number) | 质数 / 素数 (zhìshù / sùshù) | Exactly two factors: 1 and itself. Smallest prime is 2 |
| composite (number) | 合数 (héshù) | More than two factors. 1 is neither prime nor composite |
| prime factor | 质因数 (zhì yīnshù) | A factor that is itself prime |
| product of primes | 质因数乘积 | The factorised form: $60 = 2^2 \times 3 \times 5$ |
| index form | 指数形式 (zhǐshù xíngshì) | Writing repeated primes as powers: $2 \times 2 \times 2 = 2^3$ |
| factor tree | 因数树 (yīnshù shù) | Visual method: split a number into two factors, repeat until all are prime |
| divisibility test | 整除判定 (zhěngchú pàndìng) | Quick checks: even → divisible by 2; digit sum divisible by 3 → divisible by 3 |

> [!tip] Exam method — Factor tree vs repeated division
> **Factor tree:** Split into any two factors, keep splitting until all leaves are prime. Flexible but can be messy.
> **Repeated division:** Divide by the smallest prime that works, write quotients in a column. Systematic and less error-prone. Both give the same answer.

## Exam Notes

### Cambridge 0580 — Core and Extended

**C1.1 and E1.1** both include expressing an integer as a product of prime factors and finding HCF/LCM. This is not Extended-only. Stop a factor tree only when every leaf is prime; repeated factors can be collected in index form. There is no fixed mark allocation attached to the topic.

**Original example — tool and trigger:** “product of prime factors” selects repeated division by primes. For $72$, divide by $2$ three times, leaving $9$; divide by $3$ twice, leaving $1$. Thus $72=2^3\times3^2$. Multiplying back checks the product; checking the bases are prime checks the requested form. The final $1$ is not a prime factor.

### OxfordAQA 9260

**N4, Core content** explicitly includes prime factorisation and product notation, with index form specified in its notes. HCF and LCM are also named. For two factorizations, HCF takes the smaller exponent of each shared prime; LCM takes the larger exponent of every prime present. An absent prime has exponent zero. These methods support the named outcomes; a proof of unique factorisation is enrichment.

### IB Mathematics — AA and AI

Both guides list primes, factors and multiples as **prior learning**, knowledge that questions may assume. Both mark greatest common factor and least common multiple **HL only** in their prior-learning lists. AA HL AHL1.15 includes Euclid’s proof of infinitely many primes. This does not establish a separately assessed prime-factorisation unit or a requirement to prove the Fundamental Theorem of Arithmetic. [AA guide, prior learning](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf) · [AI guide, prior learning](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf)

### Further courses — boundary

**Cambridge 0606, 9709 and 9231; Edexcel IAL; OxfordAQA 9660; AP Calculus AB/BC:** the inspected specifications do not list elementary prime factorisation as a new standalone syllabus topic. It remains useful arithmetic, especially behind simplification of surds. Algebraic polynomial factorisation is a different skill. Edexcel IAL P4's proof content includes the infinity of primes; that is not a requirement to prove unique prime factorisation. **A proof of the Fundamental Theorem of Arithmetic is not a named requirement in these specifications.** Prior arithmetic can still be used in questions: “not a separate topic” does not mean “forbidden to appear.”

## Connections

- **Prerequisite:** [[Factors and Multiples (Vocab)]] — what factors are
- **Leads to:** [[Prime Numbers]] — prime numbers and their multiplicative structure
- **Leads to:** [[Powers and Roots (Vocab)]] — index form used here
- **Used in:** [[Cardinality]] — HCF/LCM via Venn diagrams uses prime factorisation

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $2^3 \times 3^2 \times 5$ | `2^3 \times 3^2 \times 5` | Product of primes in index form |
