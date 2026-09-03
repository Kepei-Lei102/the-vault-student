# The Vault — Mathematics Directory

> **219 cards** — 214 topic cards across 14 domains, plus 5 formula-sheet references at the folder root. Last landed: [[Eigenvalues and Eigenvectors]] (2026-08-20).
> One line per card: what it teaches and, where settled, which syllabus rows it closes. Open the card for the derivations and the graph of what to read first.

**Reading the domains.** Folders are decorative; this index and each card's frontmatter are the map. *(Vocab)* cards are short definition-first entries; the rest are deep cards. Board codes: 0580 = Cambridge IGCSE, 0606 = Cambridge Additional Maths, 9709 = Cambridge A Level (P1–P6), 9231 = Cambridge Further (FP1, FP2, FM, FS), 9260 = OxAQA IGCSE, IB, AP.

See also: [[Physics/Directory|Physics]] · [[CS/Directory|Computer Science]] · [[Stories/Directory|Stories]] · [[Meta/Directory|Meta]].

---

## Foundations / Set Theory (12)

1. **[[Set]]** — definition, roster vs description, finite and infinite sets.
2. **[[Element]]** — membership ($\in$ / $\notin$), testing elements.
3. **[[Empty Set]]** — $\varnothing$, why it exists, common traps.
4. **[[Universal Set]]** — $\xi$, choosing an appropriate universal set.
5. **[[Subset]]** — $\subseteq$ vs $\subset$, proper subsets, $2^n$ subsets.
6. **[[Cardinality]]** — $n(A)$, counting elements, infinite cardinalities.
7. **[[Union]]** — $A \cup B$, "or" in set language.
8. **[[Intersection]]** — $A \cap B$, "and" in set language.
9. **[[Complement]]** — $A'$, everything not in $A$.
10. **[[Set Operations]]** — combined operations, De Morgan's laws, distributive laws.
11. **[[Set-Builder Notation]]** — $\{x : \text{condition}\}$, reading and writing it.
12. **[[Venn Diagram]]** — 2-set and 3-set diagrams, shading regions, inclusion–exclusion.

## Foundations / Notation (1)

1. **[[Greek Letters (Vocab)]]** — the borrowed alphabet: why $\Sigma$ is Sum and $\mu$ is Mean, capitals as operations, and the collisions that bite ($\sigma$, $\mu$, $\lambda$).

## Foundations / Logic (2)

1. **[[Logic]]** — propositions, connectives ($\lnot, \land, \lor, \Rightarrow, \Leftrightarrow$), quantifiers, negation rules, proof structures.
2. **[[Proof by Induction]]** — the two-pillar machine for claims about every $n$: pattern seduction shattered (Moser's circle), the domino argument made exact, Cambridge's four examples worked. *9231 FP1 §1.7*

---

## Functions (3)

1. **[[Function]]** — $f(x)$ notation, domain, range, input/output, the vertical line test.
2. **[[Composite Function]]** — $fg(x) = f(g(x))$, order matters, $f^2(x)$.
3. **[[Inverse Function]]** — $f^{-1}(x)$, swap-and-rearrange, reflection in $y = x$.

## Combinatorics (3)

1. **[[Factorial Notation]]** — $n!$, the recursive definition, why $0! = 1$.
2. **[[Permutations and Combinations]]** — $^nP_r$, $^nC_r$, order matters vs doesn't.
3. **[[Counting Problems]]** — strategies: complement, block, gap, digit constraints.

## Probability (15)

1. **[[Probability Basics]]** — sample space, $P(A)$, theoretical vs experimental.
2. **[[Combined Probability]]** — AND/OR rules, tree diagrams, with/without replacement.
3. **[[Conditional Probability]]** — $P(A \mid B)$, Venn diagrams, two-way tables.
4. **[[Relative and Expected Frequency]]** — long-run proportion, expected frequency $= n \times P$.
5. **[[Discrete Random Variables]]** — the distribution table, $E(X)$ and $\mathrm{Var}(X)$ with their rules, the binomial and the geometric with its memoryless property.
6. **[[Normal Distribution]]** — the bell curve: standardising, the $z$-table discipline, percentage points, the binomial → normal approximation with continuity correction.
7. **[[Poisson Distribution]]** — counts of arrivals in a window: the $B(n, \lambda/n)$ limit, mean = variance, rescaling $\lambda$, and the clustering illusion. *9709 P6 §6.1*
8. **[[Linear Combinations of Random Variables]]** — $E$ rides any linear recipe, $\mathrm{Var}$ picks up squared coefficients and demands independence; $\mathrm{Var}(\bar X) = \sigma^2/n$ as the engine of statistics.
9. **[[Continuous Random Variables]]** — probability becomes area: the pdf, $E$ and $\mathrm{Var}$ as centre of mass and moment of inertia, the cdf as odometer, uniform and exponential.
10. **[[Sampling and Estimation]]** — the mathematics of the spoonful: $\bar X$ as a random variable, the standard error and $\sqrt n$ economics, the CLT, the unbiased $s^2$.
11. **[[Hypothesis Tests]]** — the courtroom for claims: $H_0$ presumed innocent, the five-step ritual, binomial/Poisson/normal engines, Type I and II errors.
12. **[[t-Tests]]** — the ritual when $\sigma$ is unknown and $n$ is small: one-sample, paired and pooled two-sample $t$, each run on the real Paper 4 question it exists for. *9231 FS*
13. **[[Chi-Squared Tests]]** — a whole shape on trial: Pearson's statistic, goodness of fit with the degrees-of-freedom rule, and independence in contingency tables. *9231 FS*
14. **[[Non-Parametric Tests]]** — trust the order when the shape can't be trusted: sign test, Wilcoxon signed-rank, Wilcoxon rank-sum, with the MF19 tables built by hand. *9231 FS*
15. **[[Probability Generating Functions]]** — a distribution packed into one expression: sums, means and independent sums become $t = 1$, differentiate, multiply. *9231 FS*

## Statistics (8)

1. **[[Classifying Data]]** — qualitative vs quantitative, discrete vs continuous, primary vs secondary.
2. **[[Averages and Spread]]** — mean, median, mode, range, IQR, standard deviation.
3. **[[Statistical Charts]]** — bar charts, pie charts, frequency polygons, stem-and-leaf.
4. **[[Scatter Diagrams]]** — correlation, line of best fit, interpolation vs extrapolation.
5. **[[Cumulative Frequency]]** — cumulative frequency curves, reading medians and quartiles.
6. **[[Histograms]]** — frequency density, unequal class widths, area = frequency.
7. **[[Box Plots]]** — five-number summary, IQR, outliers, comparing distributions.
8. **[[Interpreting Data]]** — command words, comparison vocabulary, inference phrasing.

## Linear Algebra (8)

1. **[[Matrix]]** — order, notation, addition, scalar multiplication, matrix multiplication.
2. **[[Identity Matrix]]** — $I$, properties, $AI = IA = A$.
3. **[[Matrix Transformations]]** — reflection, rotation, enlargement as $2 \times 2$ matrices.
4. **[[Combination of Transformations]]** — matrix products for combined transformations.
5. **[[Determinants and Inverses]]** — det as area with a sign; singular = collapse = no undo; $2 \times 2$ and $3 \times 3$ inverses; $(AB)^{-1} = B^{-1}A^{-1}$.
6. **[[Invariant Points and Lines]]** — pins vs rails: lines of invariant points via $(M - I)\mathbf{p} = \mathbf{0}$, invariant lines via the gradient quadratic; the eigenvector preview.
7. **[[Eigenvalues and Eigenvectors]]** — the rails grown up: $\det(A - \lambda I) = 0$, diagonalisation for powers, Cayley–Hamilton both ways, power iteration → PageRank. *9231 FP2 §2.2*
8. **[[Linear Systems in 3D]]** — three equations = three planes: the determinant sorts unique from not, elimination sorts consistent from not; the census of configurations. *9231 FP2 §2.2*

## Calculus (31)

1. **[[Limit]]** — intuitive limit, left/right limits, limits at infinity.
2. **[[Differentiation]]** — first principles, $dy/dx$, gradient of a curve at a point.
3. **[[Power Rule]]** — $\frac{d}{dx}x^n = nx^{n-1}$, proved via the binomial expansion.
4. **[[Product Rule]]** — $(uv)' = u'v + uv'$ from first principles by the add-subtract trick; the Leibniz rectangle; the quotient rule as a corollary.
5. **[[Chain Rule]]** — $\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$: rates compose; the first-principles proof; why it is the same attention move as the product rule.
6. **[[Quotient Rule]]** — a corollary of product + chain on $u \cdot v^{-1}$; the chant explained as the principle pre-sorted; $(\tan x)' = \sec^2 x$ derived.
7. **[[Implicit Differentiation]]** — 隐函数求导: treat $y$ as $y(x)$, every term in $y$ gains a chain-rule factor; circle, folium of Descartes, $(\arcsin x)'$ derived.
8. **[[Parametric Differentiation]]** — $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$, and the second-derivative trap as the central jewel; circle, ellipse, cycloid.
9. **[[Stationary Points]]** — $f'(x) = 0$, maxima, minima, points of inflection.
10. **[[Tangents and Normals]]** — tangent and normal equations, $m_1 m_2 = -1$, linear approximation.
11. **[[Integration]]** — the reverse of differentiation: power rule, linear-inside rule, standard integrals, the FTC, area and volume of revolution.
12. **[[Integration by Substitution]]** — the chain rule in reverse; the five-step procedure; change of limits; the $f'/f$ pattern; trig substitutions.
13. **[[Integration by Parts]]** — the product rule in reverse; LIATE as the principle sorted; the self-referential $e^x \sin x$; the tabular method; reduction formulae.
14. **[[Standard Integrals]]** — 标准积分: the master table read from the differentiation rules backwards, the $\ln \lvert x \rvert$ subtlety, the inverse-trig family and its board asymmetry.
15. **[[Differentiation Rules]]** — the elementary-function derivatives, each with its proof: trig by the sum formula, $a^x$ by rewrite, $\ln$ and inverse trig by attacking the defining equation.
16. **[[Fundamental Theorem of Calculus]]** — 牛顿–莱布尼茨公式: FTC1 (every continuous function has an antiderivative) proved via the MVT for integrals; FTC2 in three lines; why "fundamental".
17. **[[Mean Value Theorem]]** — 中值定理: Rolle as the horizontal-chord lemma, Lagrange by the tilt trick, the MVT for integrals; monotonicity and the constant-difference lemma.
18. **[[L'Hôpital's Rule]]** — 洛必达法则: the seven indeterminate forms with conversion recipes; the Cauchy-MVT proof; the circular-application trap on $\sin h / h$.
19. **[[Properties of Definite Integrals]]** — the seven AP-required properties, each with a one-line Riemann-sum proof; average value of a function.
20. **[[Kinematics Calculus]]** — motion in 1D as the chain $s \to v \to a$ and back with initial conditions; the distance-vs-displacement trap; SUVAT as the constant-$a$ corollary.
21. **[[Optimisation]]** — the six-step framework; the second-derivative test with its Taylor intuition; the closed-interval method; box, cylinder and fence worked.
22. **[[Connected Rates of Change]]** — the chain rule applied to time: balloon, sliding ladder, water in a cone; the small-increment approximation as the root of error propagation.
23. **[[Numerical Methods]]** — bisection, fixed-point iteration and Newton–Raphson as one family; convergence when $\lvert g'(\alpha) \rvert < 1$; why NR converges quadratically.
24. **[[Differential Equations]]** — first-order ODEs: separable, the logistic equation via partial fractions, first-order linear by the integrating factor.
25. **[[Maclaurin Series]]** — Taylor from "match every derivative", Maclaurin as Taylor at zero; the six named expansions everything else derives from; convergence.
26. **[[Second-Order Differential Equations]]** — $ay'' + by' + cy = f(x)$: the eigenfunction key turns calculus into the auxiliary quadratic; the three-case table; particular integrals.
27. **[[Hyperbolic Functions]]** — the even and odd halves of $e^x$: definitions, identities from $e^x e^{-x} = 1$, the sector-area parameter, inverses as logarithms. *9231 FP2*
28. **[[Squeeze Theorem]]** — 夹逼定理: trap $f$ between two functions sharing a limit; the honest proof of $\sin x / x \to 1$ that L'Hôpital cannot give.
29. **[[Reduction Formulae]]** — don't integrate $\sin^{50}$: one integration by parts builds a machine that eats two powers at a time; the hinted-derivative protocol. *9231 FP2*
30. **[[Arc Length and Surfaces of Revolution]]** — the odometer written in calculus: $ds$ by Pythagoras on the sliver, three costumes, surfaces as $2\pi y\,ds$ with the frustum honesty. *9231 FP2*
31. **[[Bounding Sums with Integrals]]** — staircase vs ramp: trap a sum between two integrals (the harmonic sum vs $\ln$) or an integral between two sums; $\ln(n!)$ → the $n \log n$ sorting bound. *9231 FP2*

## Algebra (47)

1. **[[Algebraic Proof]]** — direct proof, counterexample, exhaustion; number representations; "show that" technique.
2. **[[Binomial Theorem]]** — $(a+b)^n$, Pascal's triangle 杨辉三角, the general term, the term independent of $x$.
3. **[[Completing the Square]]** — al-Khwarizmi's geometric construction, the quadratic formula derived, vertex form, exact roots via surds.
4. **[[Algebraic Expressions (Vocab)]]** — expression vs equation vs formula vs identity; term, coefficient, substitution.
5. **[[Collecting Like Terms (Vocab)]]** — like terms, simplify, combining coefficients.
6. **[[Expanding Brackets (Vocab)]]** — the distributive law, single and double brackets, FOIL, difference of two squares.
7. **[[Factorising (Vocab)]]** — common factor, difference of two squares, quadratic trinomial, the cross method, "fully factorised".
8. **[[Cartesian Coordinates (Vocab)]]** — origin, axes, quadrants, ordered pairs, Descartes.
9. **[[Linear Graphs (Vocab)]]** — $y = mx + c$, intercepts, plot vs sketch.
10. **[[Gradient (Vocab)]]** — rise over run, $\Delta y / \Delta x$, sign and direction; the foundation of the derivative.
11. **[[Equation of a Straight Line (Vocab)]]** — three forms, parallel and perpendicular conditions, finding equations.
12. **[[Quadratic Equations]]** — three solution methods (factorise, complete the square, formula), the discriminant, Vieta's formulas, word problems.
13. **[[Simultaneous Equations (Vocab)]]** — elimination, substitution, linear and non-linear, point of intersection.
14. **[[Linear Inequalities (Vocab)]]** — solve, number line, open/closed circle, the sign-flip rule, double inequalities.
15. **[[Graphical Inequalities (Vocab)]]** — boundary lines (dashed/solid), test a point, shade the region, feasible region.
16. **[[Changing the Subject (Vocab)]]** — rearrange, isolate, factor out when the target appears twice.
17. **[[Sketching Curves (Vocab)]]** — sketch vs plot; key features (roots, intercepts, turning points, asymptotes); standard shapes.
18. **[[Exponential Graphs (Vocab)]]** — $y = a \cdot b^x$, the asymptote, growth vs decay, the exponential-vs-polynomial trap, $y = e^x$.
19. **[[Remainder and Factor Theorems]]** — dividing by $(x - a)$ leaves $f(a)$; factor iff $f(a) = 0$; cubic factorisation as detective work; the rational root theorem.
20. **[[Linear Equations (Vocab)]]** — the balance method, the standard forms, degenerate cases (no solution, infinitely many).
21. **[[Indices in Algebra (Vocab)]]** — the five index laws on terms with coefficients and several variables; negative and fractional indices.
22. **[[Algebraic Fractions (Vocab)]]** — factorise-then-cancel, common denominator via LCM, multiply and divide, clearing fractions.
23. **[[Fractional Equations (Vocab)]]** — the unknown in a denominator: clear via LCM, solve, then the extraneous-root check.
24. **[[Arithmetic and Geometric Progressions]]** — $u_n$ and $S_n$ for both with Gauss and telescoping derivations; sum to infinity when $\lvert r \rvert < 1$; Zeno resolved.
25. **[[Sequences]]** — term-to-term vs position-to-term; the difference method with its $a = d_k/k!$ proof; the exponential fingerprint; special sequences.
26. **[[Graphs of Functions]]** — the six parent graphs; the $y = af(b(x - c)) + d$ framework, with "inside is backwards" proved point by point.
27. **[[Length and Midpoint (Vocab)]]** — the distance formula as Pythagoras in coordinates; midpoint as the component-wise average. *0580 E3.4*
28. **[[Parallel Lines (Vocab)]]** — $m_1 = m_2$; the vertical-lines edge case; why unequal gradients force one intersection. *0580 E3.6*
29. **[[Perpendicular Lines (Vocab)]]** — $m_1 m_2 = -1$ from a $90°$ rotation of direction vectors; perpendicular bisector worked. *0580 E3.7*
30. **[[Modulus Function]]** — $\lvert x \rvert$ two ways; seven properties; $y = \lvert f(x) \rvert$ vs $y = f(\lvert x \rvert)$; the squaring trick that extends to inequalities. *0606 §1.4, §4.1–4.2*
31. **[[Discriminant]]** — $b^2 - 4ac$ from completing the square; the three cases as parabola geometry; line–curve tangency; range-of-coefficient problems. *0606 §2.3*
32. **[[Linearisation]]** — take logs to turn $y = Ax^n$ and $y = Ab^x$ into straight lines; read $A$, $n$, $b$ off the graph; which axes straighten the data. *0606 §7.4*
33. **[[Travel Graphs (Vocab)]]** — distance–time and speed–time graphs: gradient as speed or acceleration, area as distance; the horizontal-line trap. *0580 E2.9*
34. **[[Area Under a Graph (Vocab)]]** — the trapezium rule; over- vs under-estimate read off concavity. *0580 E2.9*
35. **[[Cubic Graphs]]** — the factored-form sketching recipe and four canonical shapes; the modulus of a cubic; cubic inequalities by sign chart. *0606 §4.4–4.5*
36. **[[Quadratic Inequalities]]** — between vs outside the roots keyed by the sign of $a$; the discriminant-driven case split; "always positive" range-of-$k$ problems.
37. **[[Substitution Equations]]** — spot the disguised quadratic via $u = g(x)$: biquadratic, fractional-power, exponential, trig and log cases; the 2:1 ratio test.
38. **[[Polynomial Division]]** — $P = DQ + R$ with $\deg R < \deg D$ for any divisor; synthetic division as the linear shortcut; proper vs improper as the gateway to partial fractions.
39. **[[Partial Fractions]]** — the inverse of "combine over a common denominator": distinct linear, repeated linear, irreducible quadratic; Heaviside's cover-up.
40. **[[Complex Numbers]]** — $z = a + bi$: Cartesian and polar forms, the Argand diagram, modulus and argument, conjugates, the conjugate-root theorem, loci.
41. **[[Euler's Formula and De Moivre's Theorem]]** — $e^{i\theta} = \cos\theta + i\sin\theta$ with three independent proofs; De Moivre by induction; multiple angles and roots of unity.
42. **[[De Moivre at Work]]** — the exam kit: multiple angles with the division twists, powers flattened via $z \pm 1/z$, and the $C + iS$ method with three engines. *9231 FP2 §2.5*
43. **[[Binomial Series]]** — $(1 + x)^n$ for any real $n$ with $\lvert x \rvert < 1$; the generalised coefficient; convergence by the ratio test; expansions in use.
44. **[[Group Theory]]** — a group is the algebra of symmetry: the four axioms as "reversible actions you can compose"; $\mathbb{Z}_n$, permutations, Lagrange's theorem. 💎
45. **[[Symmetric Functions of Roots]]** — the relations built, not quoted, from $a(x - \alpha)(x - \beta)\cdots$; only symmetric functions are reachable from the coefficients. *9231 FP1 §1.1*
46. **[[Summation of Series]]** — a series has no sum, a sequence of partial sums has a limit: the method of differences proved, standard results, convergence. *9231 FP1 §1.3*
47. **[[Rational Functions and Graphs]]** — the forbidden band found by the discriminant method; oblique asymptotes; curves *do* cross their horizontal asymptotes. *9231 FP1 §1.2*

## Problem Solving (1)

1. **[[Exam Command Words (Vocab)]]** — official Cambridge definitions: sketch vs plot, state vs describe vs explain, show that vs prove vs verify; per-board differences.

## Geometry (36)

1. **[[Pythagoras Theorem]]** — $a^2 + b^2 = c^2$ with three proofs (赵爽弦图, rearrangement, similar triangles); triples; the converse; the 3D extension.
2. **[[Angle Properties (Vocab)]]** — acute/obtuse/reflex, complementary/supplementary, vertically opposite, angles on a line and at a point.
3. **[[Angles in Parallel Lines (Vocab)]]** — corresponding, alternate, co-interior; the transversal; F/Z/C shapes.
4. **[[Polygon Angles (Vocab)]]** — interior sum $(n - 2) \times 180°$, exterior sum $360°$, regular polygons.
5. **[[Circle Vocabulary (Vocab)]]** — radius, diameter, chord, arc, sector, segment, tangent, secant.
6. **[[Circle Theorems I]]** — angle at centre = twice at circumference, angle in a semicircle, same segment, cyclic quadrilateral; full proofs.
7. **[[Circle Theorems II]]** — tangent ⊥ radius, equal tangents, perpendicular from centre bisects chord, alternate segment; full proofs.
8. **[[Triangles (Vocab)]]** — classification by sides and angles; the exterior angle theorem.
9. **[[Congruence]]** — SSS, SAS, ASA/AAS, RHS with proofs; why AAA and SSA fail.
10. **[[Similarity]]** — AA/SSS/SAS with proofs; the $k$, $k^2$, $k^3$ scale-factor laws; the square–cube law in biology.
11. **[[Quadrilaterals (Vocab)]]** — the family tree from trapezium to square; diagonal properties.
12. **[[Transformations (Vocab)]]** — translation, reflection, rotation, enlargement; the "describe fully" checklist; negative scale factors.
13. **[[Symmetry (Vocab)]]** — line symmetry and rotational symmetry, the order of rotational symmetry, the symmetries of the standard shapes.
14. **[[Bearings (Vocab)]]** — three figures, clockwise from North; "the bearing of B from A"; back bearings.
15. **[[Geometrical Proof]]** — the anatomy of a geometrical proof; the toolkit of citable theorems; angle chase, congruence, similarity, circle chains.
16. **[[Vectors]]** — notation (column, $\vec{AB}$, $\mathbf{p}$), addition, subtraction, scalar multiplication; the geometric picture.
17. **[[Vector Geometry]]** — position vectors, the master identity $\vec{AB} = \mathbf{b} - \mathbf{a}$, parallel and collinear tests, the section formula, the three-step proof strategy.
18. **[[Magnitude of a Vector (Vocab)]]** — $\lvert \mathbf{a} \rvert = \sqrt{a_1^2 + a_2^2}$ as Pythagoras; unit vectors; the length of $\vec{AB}$.
19. **[[Circles Arcs and Sectors (Vocab)]]** — circumference and area, arc length and sector area as fractions of the whole, segment area, leave $\pi$ exact.
20. **[[Area and Perimeter (Vocab)]]** — the standard plane shapes; slanted side ≠ height; perimeter as the walk around the edge.
21. **[[Compound Shapes (Vocab)]]** — split or subtract: pick the strategy with fewer pieces; the shared-edge trap for perimeter.
22. **[[Units of Measure (Vocab)]]** — metric length, mass, capacity and area/volume conversions ($\times 100$ becomes $\times 10^4$ for area); tonne vs ton.
23. **[[Scale Drawings (Vocab)]]** — map scales as ratios with both sides in the same unit; real distance ↔ drawn distance; areas scale by the square.
24. **[[Nets (Vocab)]]** — unfolding solids: the cube's eleven nets, the cylinder's rectangle, the cone's sector; surface area from the net.
25. **[[Geometrical Constructions (Vocab)]]** — ruler-and-compass: perpendicular bisector, angle bisector, perpendiculars, $60°$; *why* each works (rhombus and kite symmetry).
26. **[[Loci (Vocab)]]** — a locus as a set, not a path; the four standard loci; combining them into shaded regions.
27. **[[Heptadecagon]]** — Gauss's constructible 17-gon at nineteen; the Fermat-prime classification; Richmond's construction animated. 💎
28. **[[Coordinate Geometry of the Circle]]** — $(x - a)^2 + (y - b)^2 = r^2$ from the locus; the general form; tangents; line–circle intersection via the discriminant; two circles. *0606 §8*
29. **[[Geometrical Terms (Vocab)]]** — point, line, ray, segment, plane; the polygon family; parallel and perpendicular; faces, edges, vertices and Euler's $V - E + F = 2$.
30. **[[Solids (Vocab)]]** — prisms, pyramids, cylinder, cone, sphere, hemisphere, frustum; "cylinder = circular prism"; nets and cross-sections.
31. **[[Surface Area and Volume (Vocab)]]** — the formula reference: prisms ($\times h$), pyramids ($\times \tfrac13 h$), sphere, cone, frustum; slant height; composite solids.
32. **[[3D Vectors and the Scalar Product]]** — $\mathbf{i}, \mathbf{j}, \mathbf{k}$ components, magnitude by Pythagoras twice, and $\mathbf{a}\cdot\mathbf{b} = \lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\cos\theta$ as the law of cosines in disguise. *9709 P3 §3.7*
33. **[[Vector Equations of Lines]]** — $\mathbf{r} = \mathbf{a} + t\mathbf{d}$; parallel, intersecting or skew — the 3D-only case; the consistency check; distance from a point. *9709 P3 §3.7*
34. **[[Cross Product]]** — the vector product perpendicular to both inputs with magnitude = parallelogram area; the determinant formula; built as the dot product's mirror. *9231 FP1*
35. **[[Planes in 3D]]** — point → line → plane, each anchor + span; the three costumes converted both ways; the normal as flagpole; distances and angles, every tool named. *9231 FP1*
36. **[[Polar Coordinates]]** — a polar sketch is an ordinary $r$–$\theta$ graph read while turning; tangents at the pole; the sector-area integral $\tfrac12 \int r^2\,d\theta$. *9231 FP1 §1.6*

## Trigonometry (9)

1. **[[Trigonometric Ratios]]** — SOH-CAH-TOA from similarity; exact values from the two special triangles; $\sin^2 + \cos^2 = 1$; elevation and depression.
2. **[[Exact Trigonometric Values]]** — the $30°/45°/60°$ table derived from the two triangles and extended round the unit circle; when exact beats decimal.
3. **[[3D Trigonometry]]** — the angle between a line and a plane is at the foot *in* the plane; diagonals of cuboids, pyramids and wedges by right-angled triangles in sequence.
4. **[[Trigonometric Functions]]** — three views (ratio, unit circle, wave); the CAST diagram; symmetry; $y = a\sin(b\theta + c) + d$.
5. **[[Sine and Cosine Rules]]** — proofs via the perpendicular; the cosine rule as extended Pythagoras; area $= \tfrac12 ab\sin C$; the ambiguous case.
6. **[[Radians]]** — arc over radius; $\pi \leftrightarrow 180°$; $s = r\theta$, $A = \tfrac12 r^2\theta$; why calculus demands radians; small-angle approximations.
7. **[[Trigonometric Identities]]** — the Pythagorean trio three ways; reciprocal, quotient, co-function; sum, difference and double angle; four proof tactics. *0606 §10.4, §10.6*
8. **[[Trigonometric Equations]]** — reduce to one trig of one argument; the second solution per period from CAST; four families; the $R\sin(x + \alpha)$ form. *0606 §10.5*
9. **[[Trigonometric Graphs]]** — the three parent graphs and the transformations of $y = a\sin(bx) + c$; reading $a, b, c$ off a given graph; tan's asymptotes. *0606 §10.2–10.3*

## Number (38)

1. **[[Upper and Lower Bounds]]** — error intervals, combining bounds in calculations, truncation vs rounding.
2. **[[Laws of Indices]]** — seven laws with *why* proofs; zero, negative and fractional indices; index equations.
3. **[[Surds]]** — simplification, rationalising denominators, the proof that $\sqrt 2$ is irrational.
4. **[[Four Operations (Vocab)]]** — sum, difference, product, quotient; fractions; reciprocal.
5. **[[Inverse Operations (Vocab)]]** — inverse, undo, cancellation, self-inverse.
6. **[[Order of Operations (Vocab)]]** — BIDMAS/BODMAS/PEMDAS, precedence, evaluate.
7. **[[Number Sets (Vocab)]]** — natural, integer, rational, irrational and real numbers, and how they nest.
8. **[[Factors and Multiples (Vocab)]]** — factor, multiple, HCF, LCM, divisible.
9. **[[Prime Factorisation (Vocab)]]** — product of primes, index form, factor trees.
10. **[[Powers and Roots (Vocab)]]** — base, index, squared, cubed, square and cube roots.
11. **[[Fractions (Vocab)]]** — numerator, denominator, proper/improper, equivalent, reciprocal.
12. **[[Decimals (Vocab)]]** — place value after the point; decimal places vs significant figures; the four operations on decimals.
13. **[[Recurring Decimals (Vocab)]]** — the dot notation; converting $0.\overline{3}$ and friends to fractions by the shift-and-subtract method.
14. **[[Reciprocals (Vocab)]]** — $1/x$; why $0$ has none; reciprocals of fractions and decimals.
15. **[[Ordering and Inequalities Notation (Vocab)]]** — arranging mixed fractions, decimals and negatives; $<, \le, >, \ge$ read both ways.
16. **[[Percentages (Vocab)]]** — conversions between fractions, decimals and percentages; "$X\%$ of $Y$" as an operator; percentages above 100.
17. **[[Percentage Calculations (Vocab)]]** — increase and decrease via multipliers, chained changes, percentage change, reverse percentages.
18. **[[Simple and Compound Interest (Vocab)]]** — principal, rate, term; simple vs compound; $P(1 + r/100)^n$; the bridge to exponential growth.
19. **[[Exponential Growth and Decay]]** — discrete compounding → the continuous limit $Pe^{rt}$; half-life and doubling time; Newton's cooling; $dy/dt = ky$.
20. **[[Euler's Number]]** — $e \approx 2.71828$: the 250-year history, three equivalent definitions, the irrationality proof, $e$ in probability and Euler's identity.
21. **[[Financial Literacy (Life)]]** — off-syllabus life card: 利率/年化, APR vs APY, 等额本息 vs 等额本金, exchange rates and inflation, the four legal deceptions.
22. **[[Additional Financial Literacy — US (Life)]]** — FICO, FDIC, healthcare vocabulary, 401(k)/IRA/HSA/529, W-2/1099, mortgages, credit from zero.
23. **[[Additional Financial Literacy — UK (Life)]]** — FSCS, the ISA ecosystem, auto-enrolment pensions, PAYE and tax codes, student loans as a graduate tax, the NHS.
24. **[[Additional Financial Literacy — Australia (Life)]]** — superannuation, HECS-HELP, franking credits, Medicare, offset-account mortgages, student visas.
25. **[[Ratio (Vocab)]]** — part-to-part vs part-to-whole, simplest form, $1 : n$, dividing in a ratio by the unitary method, three-part ratios.
26. **[[Proportion (Vocab)]]** — a proportion is two equal ratios: direct proportion (scale up a recipe), inverse proportion (more workers, less time), splitting in a ratio.
27. **[[Direct and Inverse Proportion (Vocab)]]** — $\propto$; $y = kx$, $y = k/x$, $y = kx^n$; find $k$ then answer.
28. **[[Rates (Vocab)]]** — quantity per unit of another: speed, density, pressure, flow, exchange rates; the rate triangle as the principle sorted.
29. **[[Average Speed (Vocab)]]** — total distance over total time, never the mean of the speeds; the 60-out-40-back trap.
30. **[[Time Calculations (Vocab)]]** — 12- and 24-hour clocks, durations across midnight, $2.5$ hours is not $2$ h $50$ min, timetables and time zones.
31. **[[Standard Form (Vocab)]]** — scientific notation, mantissa, order of magnitude.
32. **[[Rounding (Vocab)]]** — decimal places, significant figures, truncation.
33. **[[Estimation (Vocab)]]** — round every number to one significant figure, then calculate; checking an answer's size before trusting a calculator.
34. **[[Calculator Skills (Vocab)]]** — the DEG/RAD mode killer, fraction and surd display, brackets and negatives, memory, checking by estimate.
35. **[[Casio fx-991 Reference]]** — the exam calculator, key by key: modes, fractions, tables, equation solving, statistics; set the angle mode first.
36. **[[TI-84 CE Reference]]** — the graphing calculator for AP and IB: graphing, tables, solvers, statistics; it doesn't simplify surds.
37. **[[Logarithms]]** — $\log_b x = y \iff b^y = x$; the three laws proved from the index laws; change of base; $\ln$ and calculus; log scales, Napier, Shannon.
38. **[[Exponential Function]]** — $y = e^x$ as a function: the exp laws, $(e^x)' = e^x$ from the power series, $b^x = e^{x\ln b}$, disguised-quadratic exponential equations.

---

## Formula-sheet references (5)

What each board gives you on exam day and what you must carry in your head.

- **[[MF19 Reference (9709)]]** — the Cambridge MF19 booklet for Papers 1, 3, 4, 5 and 6: given vs memorise.
- **[[MF19 Reference (9231)]]** — the same booklet's Further pages: what Paper 1 gets, what Paper 4 gets (the four statistical tables), and what is absent booklet-wide.
- **[[AP Calculus Reference]]** — no formula sheet on exam day: the ~70-item memorise list across AB and BC.
- **[[Edexcel IAL Reference]]** — the Pearson booklet, less generous than MF19, more generous than AP; the cumulative-inheritance rule.
- **[[OxAQA 9660 Reference]]** — the most generous booklet of any international A Level board: a 15–20-item memorise list.

---

## How this directory stays honest

- **One line per card.** The hook says what the card teaches; the card carries everything else. If a line wants a second sentence, the second sentence belongs in the card.
- **Counts match the disk.** Each domain's number is the `.md` count in its folder and the total at the top is their sum; the linter checks both, and flags any line that has grown past a paragraph.
- **The landing story lives elsewhere.** What each card closed, and why it was built when it was, is recorded in the maintainer trackers at close-out — never here.
