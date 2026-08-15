---
chinese: 信息论 (xìnxī lùn)
prerequisites:
  - "[[Logarithms]]"
  - "[[Probability Basics]]"
  - "[[Combined Probability]]"
  - "[[Logic]]"
  - "[[Boltzmann's Tombstone]]"
  - "[[The Boolean-to-Silicon Bridge]]"
  - "[[A Fight With the Inevitable Errors]]"
leads_to:
  - "[[Compression]]"
  - "[[Kolmogorov Complexity]]"
  - "[[Cross-Entropy Loss]]"
  - "[[Error-Correcting Codes]]"
  - "[[Hashing]]"
  - "[[Turing at Bletchley]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/information-theory
  - domain/probability
  - domain/cryptography
  - level/university
  - level/beyond-syllabus
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/bit
  - notation/entropy
  - notation/cross-entropy
  - notation/KL-divergence
  - notation/mutual-information
  - notation/channel-capacity
  - misconception/information-equals-data
  - misconception/high-entropy-is-bad
  - misconception/compression-is-magic
  - misconception/encryption-and-compression-are-the-same
---

# Information Theory 信息论

## What this card teaches you

Given a probability distribution over events, this card teaches you to compute **how much information** a single event carries (its *surprise*, measured in **bits**) and **how much information on average** a draw from the distribution carries (its *entropy*). Then two further moves: that same entropy is the **mathematical floor** below which you cannot compress the source, and a noisy channel of bandwidth $B$ and signal-to-noise ratio $S/N$ has a **mathematical ceiling** above which reliable communication is impossible. The framework was invented in essentially one paper by Claude Elwood Shannon in 1948 — *A Mathematical Theory of Communication*, *Bell System Technical Journal* — and the entire modern world of compression (ZIP, MP3, JPEG, H.265), error correction (every WiFi packet, every QR code, every CD), cryptography (modern security analysis), and machine learning (the loss function of every large language model) runs on top of it.

The hunter's trace this card builds in you: **given any probabilistic process, ask "what's the entropy?" and you can immediately bound the data rate you'll need to encode it, the channel capacity you'll need to transmit it, and the loss function you'd train a model to predict it.** Once you internalise the trace, you start seeing Shannon's formula everywhere — and the recognition is correct, because it really is everywhere.

A note on residency: the biographical arc (Shannon 1916–2001, his 1937 master's thesis on relay-Boolean, his Bell Labs WWII cryptography work, the SIGSALY voice link to Churchill, Anthropic's choice to name **Claude** after him) lives in [[Stories/The Boolean-to-Silicon Bridge]]. *This* card carries the mathematics. The two cards are designed to be read in either order.

### 中文锚点

**信息论 (xìnxī lùn)** = 把「信息」从一个含糊的新闻词变成一个可以测量的物理量的数学理论。中心公式 $I(p) = -\log_2 p$ 比特：一件越罕见的事，发生时携带的信息越多；越确定的事，发生时携带的信息越少（极限是 $p = 1$ 时 $I = 0$ 比特，也就是「我早就知道了」）。

| English | 中文 | Symbol / formula |
|---|---|---|
| Bit | 比特 (bǐtè) | Unit of information; coined by John Tukey, popularised by Shannon |
| Information / surprise | 信息量 / 自信息 (zì xìnxī) | $I(p) = -\log_2 p$ |
| Entropy | 熵 (shāng) | $H(X) = -\sum_i p_i \log_2 p_i$ |
| Source coding | 信源编码 (xìnyuán biānmǎ) | Compression — bounded below by entropy |
| Channel capacity | 信道容量 (xìndào róngliàng) | $C = B \log_2(1 + S/N)$ |
| Perfect secrecy | 完美保密 / 信息论安全 (xìnxī lùn ānquán) | $H(\text{plaintext} \mid \text{ciphertext}) = H(\text{plaintext})$ |
| Cross-entropy | 交叉熵 (jiāochā shāng) | $-\sum_i p_i \log q_i$ — the loss function of modern LLMs |
| KL divergence | KL 散度 / 相对熵 (xiāngduì shāng) | $D_{\mathrm{KL}}(P \| Q) = \sum_i p_i \log(p_i / q_i)$ |
| Mutual information | 互信息 (hù xìnxī) | $I(X; Y) = H(X) - H(X \mid Y)$ |

中文物理课通常把熵当成一个热力学概念 ($S = k_B \ln W$, 玻尔兹曼公式)。但是 Shannon 在 1948 年发现：把概率分布当成「系统的微观态」，同一个 $-\sum p \log p$ 公式就成了**信息的不确定性度量**。这不是巧合 —— 热力学熵与信息熵是同一个数学对象在两种语言里的两个名字。冯·诺依曼据说就是因为这个数学等价性，建议 Shannon 沿用 "entropy" 一词：*「没有人真正知道熵是什么，所以在辩论里你永远占上风。」*

---

## The bit and the information formula

Shannon's first and most consequential move: **information is a function of probability, not of content**. Whether the event is "the coin came up heads" or "the President resigned today" or "the gene at locus 17 mutated," the *information content* depends only on how surprising the event was — i.e., on its probability.

The formula:

$$\boxed{\; I(p) \;=\; -\log_2 p \;\; \text{bits} \;}$$

Three reads of the same equation:

- **Rare events carry more information.** If $p = 1/2$, then $I = 1$ bit. If $p = 1/8$, then $I = 3$ bits. If $p = 1/1000$, then $I \approx 9.97$ bits. The rarer the event, the more bits its occurrence is worth.
- **Certainty carries zero information.** $I(1) = -\log_2 1 = 0$. If you were already sure something would happen, learning it happened tells you nothing. (This is why people who already know the joke don't laugh — zero bits of surprise.)
- **The unit "bit" is exactly one yes/no answer.** One bit = the information of an event with probability $1/2$. If a stranger flips a fair coin behind a curtain and tells you the outcome, you've received one bit. Two coin flips → 2 bits. A fair-die throw (six equiprobable outcomes) → $\log_2 6 \approx 2.585$ bits.

### Why this formula and not some other? The three axioms

Shannon didn't pull $-\log_2 p$ out of a hat. He showed it is the **unique** function (up to a positive constant — i.e., the base of the log) satisfying three natural requirements that any "information" measure ought to have.

Let $I : (0, 1] \to [0, \infty)$ be the proposed measure. Shannon's axioms:

1. **Monotone-decreasing in $p$.** Rarer events carry more information, more frequent events less. So $p < q \Rightarrow I(p) > I(q)$.
2. **Continuous in $p$.** A tiny change in probability should produce only a tiny change in information.
3. **Additive for independent events.** If $A$ and $B$ are independent ($P(A \cap B) = p \cdot q$), then $I(p \cdot q) = I(p) + I(q)$. The information from learning two independent things is the sum of the information from learning each separately.

The third axiom is the load-bearing one. It says **$I$ turns products into sums** — the defining property of the logarithm (the product law $\log(xy) = \log x + \log y$; see [[Logarithms]] §"Why the product law works — the proof" for the derivation from $b^x \cdot b^y = b^{x+y}$). Combined with monotonicity and continuity, the unique solution up to the base is $I(p) = -\log_b p$ for some $b > 1$. The minus sign comes from monotonicity (you want $I$ to increase as $p$ decreases). The choice $b = 2$ is convention, and it makes "one bit = one binary choice" the natural unit.

Other base choices give other names — $\log_e$ gives **nats** (used in physics and machine learning theory), $\log_{10}$ gives **bans** or **hartleys** (Alan Turing's WWII Bletchley Park unit, named for Ralph Hartley whose 1928 paper anticipated parts of Shannon's framework). All three are the *same* measure rescaled — $1$ nat $= \log_2 e \approx 1.443$ bits.

> [!info] The functional-equation derivation is its own thing
> Any continuous function $f : \mathbb{R}_{>0} \to \mathbb{R}$ satisfying $f(xy) = f(x) + f(y)$ for all positive $x, y$ is forced to be $f(t) = c \log t$ for some constant $c$. This is the **Cauchy functional equation** in disguise (substitute $u = \log x$, $v = \log y$ to convert it into additivity over the reals, then use continuity to rule out the pathological additive functions). So $-\log_2 p$ isn't a clever pick — it is the *only* pick compatible with the additivity axiom. [[Logarithms]] §"Why the product law works — the proof" derives the product law $\log(xy) = \log x + \log y$ from the index laws; the uniqueness statement above goes one step further (the product law plus continuity *forces* the function to be a log up to a constant) and is the link Shannon made: *information is exactly the unique function characterised by these three axioms*.

---

## Entropy — expected information of a distribution

A single event has information $-\log_2 p$. A **distribution** over events has *expected* information: the average bits-per-draw if you sampled from it repeatedly. This expectation is the **Shannon entropy**:

$$\boxed{\; H(X) \;=\; -\sum_i p_i \log_2 p_i \;\; \text{bits} \;}$$

where $X$ is a discrete random variable taking value $x_i$ with probability $p_i$. (Convention: $0 \log_2 0 = 0$, justified by $\lim_{p \to 0^+} p \log_2 p = 0$.)

Read this carefully: $H(X)$ is *the expected surprise of a draw from $X$'s distribution*. It's a property of the distribution, not of any particular outcome.

### Worked examples

**A fair coin.** Two outcomes, each $p = 1/2$. $H = -\tfrac{1}{2}\log_2 \tfrac{1}{2} - \tfrac{1}{2}\log_2 \tfrac{1}{2} = \tfrac{1}{2}(1) + \tfrac{1}{2}(1) = 1$ bit. *Makes sense: the result of a fair coin flip carries exactly one yes/no answer's worth of information.*

**A fair 8-sided die.** Eight outcomes, each $p = 1/8$. $H = -8 \cdot \tfrac{1}{8} \log_2 \tfrac{1}{8} = -\log_2 \tfrac{1}{8} = 3$ bits. *Three bits — exactly the number of binary digits needed to label the eight outcomes (000, 001, …, 111).*

**A biased coin.** $P(\text{heads}) = 0.9$, $P(\text{tails}) = 0.1$. $H = -0.9 \log_2 0.9 - 0.1 \log_2 0.1 \approx 0.9 (0.152) + 0.1 (3.322) \approx 0.469$ bits. *Less than 1 bit: the coin is nearly determined, so each flip carries less than full information.*

**A certain event.** $p = 1$. $H = -1 \log_2 1 = 0$ bits. *Zero — if you already know the outcome, the "draw" is informationless.*

**Maximum entropy.** For a distribution over $n$ outcomes, $H$ is maximised when *all* outcomes are equiprobable, $p_i = 1/n$, giving $H_{\max} = \log_2 n$. Any deviation from uniformity reduces the entropy. *Maximum entropy = maximum uncertainty = uniform distribution. This single sentence is the foundation of huge swathes of statistical inference, machine learning, and statistical physics.*

### The binary entropy function

For a binary random variable with $P(X = 1) = p$ and $P(X = 0) = 1 - p$, the entropy is the famous **binary entropy function**:

$$h(p) = -p \log_2 p - (1 - p) \log_2(1 - p).$$

![[information-theory-surprise-and-entropy.svg|800]]

The left panel shows the **surprise curve** $I(p) = -\log_2 p$ — diverging to infinity as $p \to 0$ (impossibly-rare events would carry impossibly-much information if they happened) and hitting zero at $p = 1$. The right panel shows **binary entropy** $h(p)$ — symmetric about $p = 1/2$ where it peaks at $h(1/2) = 1$ bit, zero at both endpoints where the coin is determined. **The peak at $1/2$ is the formal statement of "maximum uncertainty when both outcomes are equally likely."**

### Why is it called "entropy"?

The name was suggested by John von Neumann. The story goes (probably apocryphal but pedagogically perfect): Shannon asked von Neumann what to call his $-\sum p_i \log p_i$ quantity. Von Neumann replied: *"You should call it **entropy**, for two reasons. First, the same expression already appears in statistical mechanics, where it goes by that name. Second, nobody really knows what entropy is, so in a debate you'll always have the advantage."*

The connection isn't a metaphor. Boltzmann's thermodynamic entropy is

$$S = k_B \ln W$$

where $W$ is the number of microstates compatible with a given macrostate. If those microstates are *equally probable* (the postulate of equal a priori probabilities), then $W = 1/p$ for each microstate and $S = -k_B \ln p$ — Shannon's formula with a different unit ($k_B = 1.38 \times 10^{-23}$ J/K, the Boltzmann constant) and base ($e$ instead of $2$). **Thermodynamic entropy and Shannon entropy are the same mathematical object** — Boltzmann's formula is a special case of Shannon's, applied to the microstates of a physical system. The deeper consequence — that erasing one bit of information costs at least $k_B T \ln 2$ of dissipated heat — is **Landauer's principle**, treated in the beyond-syllabus section below.

---

## Source coding — entropy is the compression limit

Shannon's first landmark theorem (1948): **the entropy of a source is the minimum average number of bits per symbol needed to encode it.** You can compress down to $H(X)$ bits/symbol but not below.

The theorem in one sentence: for a source emitting symbols $x_i$ with probabilities $p_i$, any lossless code that encodes each symbol independently has average bits-per-symbol $\bar{L} \geq H(X)$. The bound is tight — there exist codes (Huffman codes, arithmetic codes) that get arbitrarily close.

**Why this is mathematics, not engineering.** ZIP doesn't have a clever algorithm hidden in it that someone could one day improve to break the entropy bound. *No* algorithm can break it, because the bound is information-theoretic. Engineering improvements only close the gap between practical codes and the Shannon limit; the limit itself is fixed by the source's probability distribution.

### Huffman codes — the constructive proof

Given a probability distribution, Huffman's algorithm (1952, then-MIT-grad-student David Huffman as a homework assignment from Robert Fano) constructs an optimal prefix code: take the two least-probable symbols, merge them into a meta-symbol whose probability is the sum, repeat until one symbol remains, then read off the tree as the codebook.

For the distribution $\{a: 0.5, b: 0.25, c: 0.125, d: 0.125\}$ (entropy $H = 1.75$ bits), Huffman gives codes $a \to 0$, $b \to 10$, $c \to 110$, $d \to 111$, with average length $\bar{L} = 0.5(1) + 0.25(2) + 0.125(3) + 0.125(3) = 1.75$ bits — *exactly the entropy*. This happens when all probabilities are negative powers of 2 (so $-\log_2 p_i$ is an integer). For general distributions, Huffman gets $\bar{L}$ within 1 bit of $H$; arithmetic coding closes the remaining gap.

### What gets compressed and what doesn't

Compression works on low-entropy data — sources where some symbols are more likely than others. English text is compressible because letters and word frequencies are highly non-uniform (Zipf's law); Huffman'ing it gives roughly 4.5 bits/character vs the 8 bits/character of naive ASCII. Natural images are compressible because adjacent pixels correlate. Music is compressible because the next sample is roughly the previous sample plus a small change.

**Already-encrypted data is incompressible** because a good cipher produces output indistinguishable from uniform random bits — *maximum entropy*. If you encrypt then ZIP, you save nothing (and may slightly inflate). This is a common practical confusion: people think they should encrypt and *then* compress for security and efficiency, but the right order is **compress first, encrypt second**. Compression reduces entropy by removing redundancy; encryption then re-randomises the compressed stream. *Order matters because entropy can be reduced (by removing structure) but can never be increased (by adding it back from nothing).*

The bound bites every codec you've ever used: ZIP, gzip, MP3, JPEG, FLAC, H.264, H.265, AV1. They differ in *how close* they get to the entropy of their respective sources, and in what they choose to model (audio has temporal correlation, images have spatial, video has both), but every single one of them is asymptotically bounded by Shannon.

> [!info] Lossless vs lossy compression
> The source coding theorem bounds *lossless* compression — the original data is exactly recoverable. **Lossy** compression (MP3, JPEG, H.265, AV1) is a different game: you allow some information to be *discarded* in exchange for much smaller output. The theoretical framework for this is **rate-distortion theory** (Shannon 1959): given a tolerance $D$ for distortion, the minimum bits-per-symbol needed to encode the source within that distortion is the rate-distortion function $R(D)$. Lossless compression is the special case $D = 0$. The vault may grow a [[Rate-Distortion Theory]] card eventually; for now, the takeaway is that lossy codecs throw away information humans don't perceive (sub-band audio that's masked by louder neighbours, JPEG's high-frequency DCT coefficients) and that the savings are huge — MP3 ≈ 10× over CD audio at "imperceptible" quality.

---

## Channel capacity — Shannon-Hartley

Shannon's second landmark theorem: **every noisy communication channel has a maximum reliable data rate, and that rate is mathematically determined by the channel's bandwidth and signal-to-noise ratio.**

For an additive-white-Gaussian-noise channel (the standard model for radio, copper, fibre, anything with thermal noise) of bandwidth $B$ hertz and signal-to-noise power ratio $S/N$:

$$\boxed{\; C \;=\; B \, \log_2\!\left(1 + \frac{S}{N}\right) \;\; \text{bits/second} \;}$$

**Below capacity** ($R < C$): there exist encoding schemes that drive the error rate as close to zero as you like. Reliable communication is possible.

**Above capacity** ($R > C$): there is no encoding that achieves bounded error rate. Errors are inevitable, no matter how cleverly you encode.

The shocking part is the dichotomy. You'd expect the error rate to scale smoothly with how aggressively you push the data rate — a little above capacity gives a few errors, a lot above gives a lot of errors. *That isn't what Shannon proved.* The error rate goes from "arbitrarily close to zero" to "bounded above zero by a fixed positive constant" the instant you cross capacity. There is no intermediate regime where you "just live with a small error rate"; there is a clean phase boundary.

### Reading the formula

- **$B$ (bandwidth) sets the upper bound on signalling rate.** Even with infinite signal-to-noise, you can't send faster than $B \log_2 \infty$ → you're still limited by bandwidth.
- **$S/N$ (signal-to-noise ratio) sets bits per use of the channel.** A noisier channel forces lower-density modulations (binary vs 256-QAM); more headroom over noise lets you pack more bits per symbol.
- **The trade-off is logarithmic.** Doubling $S/N$ adds *one* bit/Hz to capacity. Tenfold-improving $S/N$ adds $\log_2 10 \approx 3.32$ bits/Hz. The diminishing-returns shape is why "just add more power" is a losing strategy in network design — the gains compound logarithmically while the power cost compounds linearly.

### Examples of the bound in the wild

- **WiFi 6 (802.11ax)** in a 160 MHz channel with high $S/N$ achieves ~9.6 Gbps theoretical max. The number is set by $C = 160 \times 10^6 \times \log_2(1 + S/N)$.
- **A V.90 modem** on a 3400 Hz telephone line reached ~56 kbps because that's near $3400 \times \log_2(1 + S/N)$ with telephone-line noise. The "56K wall" was Shannon's wall.
- **5G New Radio** in a 100 MHz channel approaches multi-Gbps for the same reason WiFi does.
- **Submarine fibre-optic cables** carry tens of Tbps per fibre pair because optical signals have enormous bandwidth and good $S/N$, and modern coherent modulations approach the Shannon limit very closely.

Every single one of these is a Shannon-bounded number. Engineering improvements over the last fifty years have not raised the bound — they have raised *practical codes* closer to the bound. **Turbo codes** (Berrou et al. 1993, used in 3G/4G), **LDPC codes** (Gallager 1962, rediscovered 1995, used in WiFi 6, 5G data channel, DVB-S2), and **polar codes** (Arıkan 2008, used in 5G control channel) all hit within a fraction of a dB of capacity for realistic channels. We are essentially *at* Shannon's limit for the channels we use today.

### What sets bandwidth in the real world?

$B$ is set by physics (allowed RF spectrum, fibre transmission window, copper-pair bandwidth) and by regulation (ITU spectrum allocations, FCC licensing). $S/N$ is set by transmit power, antenna gain, distance, and the thermal-noise floor $k_B T B$ (the same $k_B$ that appears in Boltzmann's entropy). **You can buy more $B$ by getting wider spectrum allocation, and more $S/N$ by transmitting harder or moving closer.** Above the Shannon bound, no amount of engineering changes anything.

---

## Perfect secrecy — Shannon 1949

A year after the communication paper, Shannon published *Communication Theory of Secrecy Systems* (Bell System Technical Journal, 1949), which formalised cryptography in the same information-theoretic language. The key concept: a cipher achieves **perfect secrecy** when

$$H(\text{plaintext} \mid \text{ciphertext}) \;=\; H(\text{plaintext}).$$

In words: given the ciphertext, the receiver who knows the key learns the plaintext, but an eavesdropper who doesn't know the key learns *nothing* — their uncertainty about the plaintext after seeing the ciphertext is identical to their uncertainty before. The ciphertext leaks zero bits.

**Shannon proved that the only cipher achieving perfect secrecy is the one-time pad** (OTP):

1. The key is *truly random* (each bit independently uniform).
2. The key is *as long as the message*.
3. The key is *used exactly once*, then destroyed.

Encrypt with $c_i = m_i \oplus k_i$ (XOR each message bit with the corresponding key bit). Decrypt with $m_i = c_i \oplus k_i$ (XOR again — XOR is its own inverse). With those three conditions, the ciphertext distribution is uniform regardless of the plaintext distribution → perfect secrecy.

The catch is the conditions. Real systems can't satisfy them — you need a private channel as wide as the public channel to distribute the keys, defeating the point. *All* modern cryptography (AES, RSA, elliptic-curve, lattice-based post-quantum) is **computationally secure** rather than information-theoretically secure: a sufficiently powerful adversary could in principle break it, but the work required is believed to be infeasible. Shannon's 1949 theorem is the wall that computational cryptography routes around.

> [!tip] SIGSALY and the Turing-Shannon lunches at Bell Labs
> During WWII, Shannon worked at Bell Labs on **SIGSALY**, the encrypted voice link between Churchill and Roosevelt — the first system to digitise voice and apply a one-time pad on the digital stream, using vinyl records pressed with random noise as the "pad." Alan Turing visited Bell Labs in 1943, and the two had lunch regularly. **They couldn't discuss their actual work** — Turing's Bletchley Park decryption and Shannon's SIGSALY were both top-secret — so they talked about universal computation, abstract logic, and how a machine could be built that simulated any other machine. The intellectual lineage from those lunches to the modern computer is hard to overstate.
>
> The full narrative — including von Neumann naming the bit, Sheffer's stroke (NAND), the transistor in 1947, Intel in 1968, and Anthropic's choice of "Claude" in 2021 — lives in [[Stories/The Boolean-to-Silicon Bridge]]. Turing's side of it — Bletchley, the Bombe, and his **ban** unit of evidence (a base-10 cousin of the bit) — is in [[Stories/Turing at Bletchley]]. This card holds the equations.

---

## Shannon's formulas inside today's AI

This is where the "Claude is named after Shannon" claim becomes mathematically literal rather than merely ceremonial. Modern large language models — GPT, Claude, LLaMA, Gemini, all of them — are trained by minimising a Shannon quantity over enormous text corpora. Every gradient step, every parameter update, is in service of reducing a number defined by Shannon's 1948 framework.

### Cross-entropy loss

A language model assigns a probability distribution $q$ over the next token, given the context. The "truth" is the actual next token, with a one-hot distribution $p$ (probability 1 on the actual token, 0 elsewhere). The **cross-entropy loss** is

$$\mathcal{L}(p, q) \;=\; -\sum_i p_i \log q_i.$$

When $p$ is one-hot at token $t$, this reduces to $-\log q_t$ — *exactly* Shannon's information formula applied to the model's predicted probability of the correct token. Training the model = pushing $q_t$ closer to 1, i.e., reducing the "surprise" the model expresses on each true next token.

### Perplexity

The standard benchmark for language-model quality is

$$\text{PPL} \;=\; 2^{H(p, q)}$$

where $H(p, q)$ is the cross-entropy (in bits per token). Perplexity is "the effective branching factor" — a perplexity of 50 means the model is as uncertain about the next token as if it had to guess uniformly among 50 alternatives. Lower perplexity → closer to the Shannon compression bound on natural language → better predictions. State-of-the-art language models on standard test sets have perplexities in the single digits — *closer to the entropy of English text than anything we built before deep learning*.

### KL divergence

The **Kullback-Leibler divergence** measures how "far" one distribution is from another:

$$D_{\mathrm{KL}}(P \,\|\, Q) \;=\; \sum_i p_i \log \frac{p_i}{q_i} \;=\; H(p, q) - H(p).$$

It's the cross-entropy *above* the irreducible entropy of $p$ — the *excess* surprise from using the wrong distribution to encode events from the right one. $D_{\mathrm{KL}} \geq 0$ with equality iff $p = q$ (Gibbs' inequality). KL divergence appears in: variational autoencoders (the regularisation term), reinforcement learning from human feedback (the policy-distance constraint that keeps Claude-style models from drifting from their reference policy), Bayesian inference (the cost of approximating a posterior), and dozens of other places. **If you're optimising over distributions and you want a "how-different-are-they" measure, KL is almost always the first thing you reach for.**

### Mutual information

The **mutual information** between two random variables $X$ and $Y$ is

$$I(X; Y) \;=\; H(X) - H(X \mid Y) \;=\; H(Y) - H(Y \mid X).$$

In words: how much does learning $Y$ reduce your uncertainty about $X$? (Equivalently, by symmetry: how much does learning $X$ reduce your uncertainty about $Y$?) Mutual information is symmetric, non-negative, zero iff $X$ and $Y$ are independent.

In modern ML: **InfoMax representation learning** maximises mutual information between learned features and the input; **disentanglement objectives** want each latent factor to carry distinct information; **information bottleneck** theory (Tishby) describes deep-network training as a compression-then-prediction trade-off where the optimal representation maximises $I(\text{layer}; \text{output})$ while minimising $I(\text{layer}; \text{input})$. Recent interpretability research uses mutual information between attention heads and target concepts.

### The Claude/Anthropic connection — what this means concretely

Anthropic named their assistant **Claude** after **Claude Elwood Shannon** as an explicit homage. Once you've worked through this card's mathematics, the homage is not symbolic but literal: *the loss function used to train Claude, the metric used to evaluate Claude, the regularisation that keeps Claude on-policy during RLHF, and the information bottleneck describing what Claude's hidden layers represent are all Shannon quantities.* Training a language model at the modern scale is, mathematically, Shannon's 1948 framework run at billions-of-parameters scale on trillions of tokens of natural-language text.

The narrative arc from Sheffer's 1913 universality theorem through Shannon's 1937 thesis through 1948's information theory through 1947's transistor through 1971's Intel 4004 through 2017's transformer architecture through 2021's founding of Anthropic to today's frontier models lives in [[Stories/The Boolean-to-Silicon Bridge]]. The equations live here. The two are designed to be read together.

---

## The hunter's payoff — what this card teaches you to trace

Three causal traces this card equips you with:

1. **"How much information does this event carry?"** Given an event of probability $p$, compute $I(p) = -\log_2 p$ bits. A rare event carries a lot of information; a likely event carries little; a certain event carries none. *Reframes "surprising" and "informative" as the same word — measured in bits.*

2. **"What's the compression limit of this source?"** Given a distribution over the symbols of a source, compute $H = -\sum p_i \log_2 p_i$. That's the floor: no lossless code can do better on average. *Reframes data compression from "engineering with infinite headroom" to "engineering against a mathematical wall."*

3. **"What's the channel capacity for reliable communication?"** Given bandwidth $B$ and signal-to-noise ratio $S/N$, compute $C = B \log_2(1 + S/N)$. Above $C$, errors are unavoidable; below, reliable communication is possible with the right encoding. *Reframes "more power" and "wider channel" as two distinct trade-offs against the same Shannon wall.*

These three traces together let you read a probabilistic system end-to-end: how much information per symbol, how compressibly it can be stored, how reliably it can be transmitted, and (in the ML context) how well a probabilistic model is doing at predicting it. The traces transfer across domains in a way few other frameworks do — the same machinery analyses GPT's training, your phone's WiFi link, the JPEG photo you just took, and the lossy compression in your inner ear's nerve channel.

---

## Common misconceptions

### 1. "More information is better; high entropy is bad"

Backwards. Entropy measures *uncertainty about an outcome*, which equals *information in the eventual outcome*. High-entropy distributions (uniform, random) carry the most information per draw; low-entropy distributions (peaked, deterministic) carry the least. **An information-rich source IS a high-entropy source.** Random noise has *maximum* entropy and *maximum* information per bit — that's why already-encrypted data is incompressible.

**Fix:** ask "what would a fair coin do?" If the answer is "uniform distribution, maximum uncertainty, maximum bits per draw," then high entropy = high information = unavoidable in well-designed cryptography.

### 2. "Compression is somehow magic / a clever algorithm could always do better"

The source coding theorem proves there's a mathematical floor: entropy. **No algorithm can compress a source below its entropy on average.** ZIP, gzip, and friends are within a small factor of the entropy of English text and are improving slowly because there's not much room left. The "more clever code" intuition is misleading — the limit is set by information, not by ingenuity.

**Fix:** compute the entropy of a small example source (e.g., the distribution $\{a: 0.5, b: 0.25, c: 0.25\}$, entropy $H = 1.5$) and show that Huffman achieves it exactly.

### 3. "Compression and encryption are the same idea / they do the same thing to data"

They are opposites in a specific sense. **Compression reduces entropy** by exploiting structure (removing redundancy). **Encryption preserves entropy** while making the structure inaccessible to an eavesdropper (a good cipher's output looks uniformly random — *maximum* entropy). Compress first, encrypt second: compression has nothing left to do on encrypted data, so the order matters.

**Fix:** point at a ZIP file's hex dump (somewhat regular) vs an encrypted file's hex dump (looks like random noise). Then ask "which one would compress further?" — neither, the ZIP is already near-entropy and the encrypted file is at-entropy.

### 4. "Channel capacity is a soft engineering ceiling — push harder and you'll squeeze through"

Below capacity, error rate can be driven to zero. Above capacity, error rate is bounded above zero by a fixed positive constant *no matter what code you use*. The transition is sharp, not gradual. *"Push harder" doesn't work past the wall* because the wall is information-theoretic — there isn't a clever modulation scheme nobody has thought of yet.

**Fix:** point at the 56K modem era. The "56K wall" wasn't a Bell-Labs failure of imagination; it was Shannon's bound on a 3400 Hz telephone line. The same wall constrains every WiFi and 5G product today, just at higher numbers.

### 5. "Information is data is bits is bytes"

Subtly wrong. **Data** is the raw representation (bytes, characters); **information** is the entropy of the underlying probability distribution. An 800-MB encrypted file has more bits of *data* than an 80-MB text file, but if the text file is rich English prose the *information content* might be comparable. ZIP and gzip work by squeezing redundant-data files toward their information content.

**Fix:** introduce the slogan "data measures storage, entropy measures meaning" — pithy but accurate, helps students separate the two levels.

---

## Beyond syllabus

### Kolmogorov complexity — the algorithmic relative of entropy

Shannon's entropy is a property of a **probability distribution** — the expected information of a draw. **Kolmogorov complexity** $K(s)$ is a property of an *individual string* $s$ — the length of the shortest program (in some fixed universal language) that outputs $s$ and halts. The two concepts are deeply linked: for typical strings drawn from a distribution, $K(s) \approx -\log p(s)$ asymptotically.

Kolmogorov complexity is **uncomputable** (you cannot in general write a program that takes $s$ and returns $K(s)$ — this follows from the halting problem). But it captures something Shannon entropy can't: *algorithmic regularity*. The string `010101010101…` of length $n$ has high Shannon entropy if treated as samples from a $\{0, 1\}$ source with $p = 1/2$, but its Kolmogorov complexity is $O(\log n)$ because a tiny program ("print `01` $n/2$ times") generates it. Algorithmic information theory (Solomonoff, Kolmogorov, Chaitin in the 1960s) is the rigorous foundation for ideas like *"the simplest model that fits the data"* (Solomonoff induction, Minimum Description Length, the formal version of Occam's razor).

### Landauer's principle — information has a thermodynamic cost

Rolf Landauer (1961, at IBM): **erasing one bit of information in a physical computer requires dissipating at least $k_B T \ln 2 \approx 2.85 \times 10^{-21}$ J of heat** at temperature $T$. This isn't engineering inefficiency — it's a fundamental thermodynamic bound. The argument: erasing a bit reduces the entropy of the computational system by $k_B \ln 2$, so by the second law of thermodynamics that entropy must increase somewhere else (the environment) by at least that much, which means dissipating $k_B T \ln 2$ of heat.

Modern silicon computers dissipate ~$10^4$ times the Landauer limit per bit operation, so we're not yet at the wall. But the wall is real — confirmed experimentally in 2012 (Bérut et al., *Nature*). One consequence: **reversible computing** (operations that don't erase any information) could in principle run with arbitrarily little heat dissipation. Quantum computers, by their unitarity, are reversible at the gate level; classical reversible computing is a small research area. The conceptual point is that the bridge between information and physics is two-way — Shannon's $H = -\sum p \log p$ doesn't just *look* like Boltzmann's $S = k_B \ln W$, they are the *same* quantity in two unit systems, and erasing the information costs the same heat as erasing the thermodynamic disorder.

### Shannon's playful side — Theseus, juggling, the wearable computer

Shannon was that rare mathematician who was also a serious inventor and tinkerer:

- **Theseus (1950)** — mechanical mouse that "learned" to solve mazes using electromechanical relay logic. One of the first machines that adapted based on experience, fifteen years before the phrase "machine learning" was coined.
- **First chess program (1949)** — Shannon's paper *Programming a Computer for Playing Chess* gave the minimax-with-heuristic-evaluation template every chess engine used until deep learning arrived in the 2010s.
- **First wearable computer (1961)** — built with Ed Thorp (the same Ed Thorp who used card-counting to beat blackjack). A small analog device hidden in a shoe that predicted roulette outcomes from accelerometer readings in real time, used quietly in Vegas casinos.
- **Juggling theorem** — Shannon proved a relation between the number of balls, hand capacity, and average air time of a juggle. Rode a unicycle while juggling four balls in the Bell Labs hallways.

The complete narrative — including Shannon's role in SIGSALY, his lunches with Turing, and the lineage from his 1937 master's thesis to Anthropic — lives in [[Stories/The Boolean-to-Silicon Bridge]]. Soni and Goodman's biography *A Mind at Play* (2017) is the right level for further reading.

### Differential entropy — extending to continuous distributions

For a continuous random variable with density $f(x)$, the natural analogue is **differential entropy**:

$$h(X) = -\int f(x) \log f(x) \, dx.$$

This is *not* the limit of discrete entropy as bin widths shrink (that limit diverges to $\infty$) — it's the regular finite part after subtracting the diverging $\log(1/\Delta x)$ term. Differential entropy is invariant under translation but *not* under scaling, and can be negative (the differential entropy of a uniform distribution on $[0, 1/2]$ is $-1$ nat). For most working purposes — Gaussian channel capacity, ML continuous-variable models — differential entropy is the right tool, with these caveats noted.

---

## Exam Notes

Information theory is **not a named topic on any board the vault covers** — no 0478 or 9618 row, not in AP CSA/CSP's frameworks, and not a named statement in IB CS's published outline (A1.2 stops at binary/hex conversion and logic gates). Its fingerprints, however, are all over the examined material: [[Compression]] (0478 §1.3, 9618 §1.3) is bounded by this card's entropy floor, [[Sound Encoding]]'s bit-depth arithmetic is information-per-sample, and every "estimate the file size" calculation is counting bits this card defines. Treat it as the mathematical basement under the examined floors — enrichment for the student who asks *why* compression has a limit.

---

## Connections

- **Mathematical foundation:**
   - [[Logarithms]] — the functional equation $f(xy) = f(x) + f(y)$ that forces $-\log_b p$ to be the unique information measure (up to base). Includes a teaser §"Information theory — log as 'information content'" that this card cashes in full.
   - [[Probability Basics]] — a distribution is what entropy measures; this card needs the probability framework as input.
   - [[Combined Probability]] — independence ($p(a \cap b) = p(a) p(b)$) is what makes information additive ($I(p \cdot q) = I(p) + I(q)$).
   - [[Conditional Probability]] — $H(X \mid Y)$ in the mutual-information definition relies on conditional probabilities.
   - [[Logic]] — Boolean propositions are the discrete-variable case where the distribution is over $\{0, 1\}$.

- **Computer science siblings:**
   - [[Logic Gates]] — the physical implementation of Boolean logic; Shannon's 1937 thesis showed how to realise Boolean algebra in relays, the foundation of every chip.
   - [[Recursion]] — the third independent characterisation of computation alongside Boolean logic and information theory.

- **Cross-domain bridges:**
   - **Statistical physics** — Boltzmann's $S = k_B \ln W$ is Shannon's formula in $\ln$ units, applied to microstates. **Same maths, different sciences.** The link runs through Landauer's principle (above).
   - **Machine learning** — cross-entropy loss, perplexity, KL divergence, mutual information are direct Shannon quantities. Modern language models are Shannon's framework at scale.
   - **Cryptography** — the perfect-secrecy theorem and the one-time pad set the boundary between information-theoretic security and computational security. Every modern cipher (AES, RSA, post-quantum lattice schemes) is computationally secure rather than information-theoretically secure, working around Shannon's wall rather than over it.
   - **Communication engineering** — Shannon-Hartley caps every WiFi, 5G, fibre-optic, and submarine-cable throughput in current use. Modern codes (Turbo, LDPC, polar) approach the bound within fractions of a dB.

- **Story partner:**
   - [[Stories/The Boolean-to-Silicon Bridge]] — Sheffer 1913 (NAND universality) → Wittgenstein 1921 → Russell-Whitehead 1927 → Turing 1936 → Shannon 1937 (relay-Boolean thesis) → Shannon 1948 (this card's contents) → Shockley-Bardeen-Brattain 1947 (transistor) → Kilby-Noyce 1958–59 (integrated circuit) → Intel 4004 1971 → Anthropic 2021 (Claude). Dual-residency: the Stories card carries the dramatic arc, this card carries the equations.
   - [[Stories/Turing at Bletchley]] — Turing's wartime use of information as **weight of evidence** (the *ban* and *deciban*), his Banburismus method as secret Bayesian inference, and the Bell Labs lunches with Shannon — the human story behind the unit table above.
   - [[Stories/Boltzmann's Tombstone]] — where the formula came from. Boltzmann's $S = k_B \ln W$ (carved on his grave) is the *physics* original of which Shannon's $H = -\sum p\log p$ is the information-theoretic twin; the human drama of the atom wars, the death on the eve of vindication, and the twist that **Planck** — not Boltzmann — actually wrote the equation and named the constant *for him* (a tribute, the inverse of Stigler's Law). Dual-residency: that card carries the story, this one carries the maths.

- **Misconception traps cleared:** high entropy is **not** bad (it's just maximum information per draw); compression is **not** magic (it's bounded below by entropy); compression and encryption are **not** the same thing (one reduces entropy, the other preserves it); channel capacity is **not** a soft engineering ceiling (it's a sharp mathematical wall); data and information are **not** the same (one measures bytes, the other measures meaning).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $I(p) = -\log_2 p$ | `I(p) = -\log_2 p` | Self-information / surprise of an event of probability $p$, in bits |
| $H(X) = -\sum_i p_i \log_2 p_i$ | `H(X) = -\sum_i p_i \log_2 p_i` | Shannon entropy of a discrete distribution |
| $h(p) = -p \log_2 p - (1-p) \log_2 (1-p)$ | `h(p) = ...` | Binary entropy function; peaks at $h(1/2) = 1$ |
| $C = B \log_2(1 + S/N)$ | `C = B \log_2(1 + S/N)` | Shannon-Hartley channel capacity (bits/sec) |
| $H(X \mid Y)$ | `H(X \mid Y)` | Conditional entropy — uncertainty about $X$ after observing $Y$ |
| $I(X; Y) = H(X) - H(X\mid Y)$ | `I(X; Y) = H(X) - H(X \mid Y)` | Mutual information — symmetric in $X$ and $Y$ |
| $D_{\mathrm{KL}}(P \| Q) = \sum p_i \log(p_i / q_i)$ | `D_{\mathrm{KL}}(P \| Q) = ...` | KL divergence (relative entropy) |
| $\mathcal{L}(p, q) = -\sum_i p_i \log q_i$ | `\mathcal{L}(p, q) = -\sum_i p_i \log q_i` | Cross-entropy loss; equals $H(p) + D_{\mathrm{KL}}(p\|q)$ |
| $\text{PPL} = 2^{H}$ | `\text{PPL} = 2^{H}` | Perplexity — effective branching factor; LM benchmark |
| $S = k_B \ln W$ | `S = k_B \ln W` | Boltzmann entropy; Shannon's formula in nats applied to microstates |
| $K(s)$ | `K(s)` | Kolmogorov complexity; uncomputable in general |
