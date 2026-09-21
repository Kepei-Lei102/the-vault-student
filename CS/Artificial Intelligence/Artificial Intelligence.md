---
chinese: 人工智能 (réngōng zhìnéng)
prerequisites:
  - "[[Graphs]]"
  - "[[Ethics and Ownership]]"
  - "[[Differentiation]]"
  - "[[Probability Basics]]"
  - "[[Automated Systems and Robotics]]"
leads_to:
  - "[[The Turing Test]]"
  - "[[Compression Is Intelligence]]"
  - "[[Data Protection and Privacy]]"
  - "[[You Are a Reinforcement Learner]]"
  - "[[The Perceptron and Move 78]]"
  - "[[Privacy-Preserving Computation]]"
  - "[[Affective Computing]]"
tags:
  - subject/cs
  - domain/artificial-intelligence
  - domain/machine-learning
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/9618-18-1
  - syllabus/0478-6-3
  - syllabus/IB-CS-A4-1
  - syllabus/IB-CS-A4-3
  - misconception/expert-systems-learn
  - misconception/deep-means-wide
  - misconception/reinforcement-is-supervised
  - misconception/describe-the-app-not-the-ai
  - type/deep
---

# Artificial Intelligence 人工智能

> *There are two ways to make a machine behave as if it understood something. You can write down the rules. Or you can show it examples and let it find the rules itself. Everything the syllabus calls AI is one of those two, and the whole modern story is the second one overtaking the first.*

![[ai-manim.mp4]]

## Definition

### Formal

**Artificial intelligence (AI)** is the branch of computer science concerned with programs that simulate intelligent behaviour. Cambridge's IGCSE names its characteristics: an AI system holds a **collection of data** and **rules for using that data**, it can **reason** (draw conclusions from the data by the rules), and it may be able to **learn and adapt** (change its own data and rules from experience).

Two ways to build one are examined:

- An **expert system** captures human expertise as explicit rules. It has four components: a **knowledge base** (facts), a **rule base** (IF–THEN rules written by experts), an **inference engine** (the program that applies the rules to the facts to reach conclusions and to decide what to ask next), and an **interface** (how the user puts facts in and gets answers out). It does not learn.
- **Machine learning (ML)** is a program that automatically adapts its own processes or data from experience, so that its performance on a task improves without those improvements being programmed explicitly. Three categories: **supervised learning** (learns a mapping from example input–output pairs), **unsupervised learning** (finds patterns in data with no labels), and **reinforcement learning** (an agent learns by acting in an environment and receiving reward or punishment for the results).

An **artificial neural network (ANN)** is a machine-learning model built from many simple connected units arranged in layers, loosely modelled on the brain; each connection carries a **weight** that training adjusts. **Deep learning** is machine learning with neural networks that have **many hidden layers**, each extracting higher-level features from the last. **Back propagation of errors** is the algorithm that trains them: compare the network's outputs with the expected outputs, use calculus to find how the error changes with each weight, feed that error gradient backwards through the layers, adjust every weight to reduce it, and repeat. **Regression methods** are supervised learning that fits a mathematical function, a line or curve, mapping input variables to a numerical output, by minimising the difference between predicted and actual values.

**Graphs in AI:** a graph stores relationships between entities as vertices and edges, so an AI problem can be posed as a search on a graph (the shortest route on a map, by Dijkstra's algorithm or A\*), and a neural network is itself a weighted graph.

### Intuitive

Ordinary programming is rules in, answers out. Machine learning is answers in, rules out. A doctor's expert system is a very long flowchart written by doctors: it asks about your symptoms, follows the arrows, and names the illness. It is exactly as good as the doctors who wrote it and never gets better. A machine-learning system is shown ten thousand past patients with their diagnoses and finds its own arrows; it may be better than any doctor who trained it, and nobody can quite say what its arrows are. Training a neural network is turning a hundred thousand tiny dials until the answers come out right, where "which way to turn each dial" is what back propagation calculates. And "deep" means the dials are arranged in stages, so that later stages can work with what earlier ones have already found.

### 中文锚点

手机相册会自动把你家猫的照片归到一起，可是没有哪个程序员写过"什么是猫"：尖耳朵？有的猫耳朵是折的。四条腿？狗和桌子也有。靠人手写规则，很快就写不下去了。实际发生的是：程序先看了海量已经标好"是猫"或"不是猫"的照片。它一开始乱猜；每猜错一次，就把自己内部那一大堆数字朝"这次本可以少错一点"的方向微调一下；微调几百万次之后，这堆数字就变成了一个能认出猫的东西，虽然没人指得出哪一行代表"耳朵"。这就是机器学习：不是被告知规则，而是照着例子不断调整自己，直到错误变少。造智能程序的另一条路更老，叫专家系统：去请教人类专家，把知识写成一条条明确的"如果……那么……"规则，让程序照着推理。专家说得清楚的事它做得好，比如诊断故障、核对报税表；专家自己也说不清的事它就不行，而那正是机器学习接手的地方。专家系统每一步都能解释，却不会自己进步；学出来的模型越看越准，却常常解释不了自己。

---

## Part I — What "intelligent" means, in practice

Nobody has a definition of intelligence that survives contact with a philosopher ([[The Turing Test]] is the vault's card on that argument), so engineering does something more useful: it says what an intelligent *system* has and how it gets its rules. The three boards that teach this draw the same picture from different sides, and the picture is worth having whole.

**What the system has.** An AI system holds a **collection of data** about the world and the case in hand, and **rules for using that data**; it can **reason**, running the rules on the data to draw conclusions; and it may be able to **learn and adapt**, changing its own data or rules in the light of results. That is Cambridge's IGCSE list, and it is a fair checklist for any AI you meet: point at the data, point at the rules, ask whether it reasons, ask whether it changes.

**Where the rules come from.** This is the IB's way in, and the sharper of the two. Traditional programming takes *rules and data* and produces *answers*: you write the tax code as `if` statements, feed it a salary, and out comes the tax. Machine learning turns the arrow round: it takes *data and answers* and produces *the rules*, which you then run on new data. Show it ten thousand salaries with the tax that was paid, and it finds the tax code itself, or something that behaves like it. The IB frames the whole topic as the kinds of learning that do this (supervised, unsupervised, reinforcement), what each is used for, and what hardware each needs; the A-Level adds the machinery inside, neural networks and back propagation, and asks what graphs have to do with it.

The two designs, side by side, because the boards want both and the difference is the whole story of the field:

| | Expert system (rules written) | Machine learning (rules learned) |
|---|---|---|
| Where the rules come from | written by human experts | found in data and answers |
| Can it improve with use? | its fixed rules need human revision | through training or retraining; a deployed model does not necessarily learn from every use |
| Can it explain its answer? | yes, it can list the rules it fired | depends on the model: a decision tree can expose its decisions; a large neural network is harder to interpret |
| Fails when | a case its rules do not cover | the data was biased, sparse, or unlike the real world |
| Building it costs | interviewing experts and encoding their knowledge (slow) | collecting and labelling data, then compute |
| Examples | medical diagnosis, fault-finding, tax advice | spam filters, speech recognition, recommendations, image recognition |

Everything else on the card is how those two are built.

---

## Part II — Expert systems: the rules written down

![[ai-expert-system.svg|700]]

An expert system is the 1970s' answer, and it still runs in fault-finding help desks, tax software and some medical triage. The four components, in the words the mark scheme wants:

- **Knowledge base** — the facts: general facts about the domain and the facts of the present case ("engine cranks", "no spark at the plug").
- **Rule base** — IF–THEN rules written by human experts: *IF the engine cranks AND it does not start THEN the problem is fuel or spark.*
- **Inference engine** — the reasoning program. It searches the rule base for rules whose IF-part is satisfied by the facts, adds their conclusions to the knowledge base as new facts, and repeats until nothing new follows; when it needs a fact it does not have, it decides which question to ask the user next. This is **forward chaining**; running rules backwards from a hypothesis to see what facts would support it is **backward chaining**.
- **Interface** — the user answers questions and receives the conclusion, ideally with the chain of rules that produced it.

`ai-learning-demo.py` has one in twenty lines. Given the facts *engine cranks, no start, fuel gauge not empty, no spark at plug* and five rules about cars, the engine fires *engine cranks + no start → fuel or spark problem*, then *fuel or spark problem + gauge not empty + no spark → ignition fault*, and stops: diagnosis, ignition fault, with its reasoning printed. Give it a case its rules do not cover and it says nothing at all. It will never say anything a human did not write into it. That is its virtue, because every answer is auditable, and its limit, because the expert's knowledge has to be extracted by interview and typed in, rule by rule, and the world changes faster than the rule base.

---

## Part III — Machine learning: the rules learned

**Learning** in a program means one thing: there are numbers inside it, **parameters**, that are adjusted to make its errors smaller. Every method on this card is a way of choosing which numbers to adjust and in which direction.

### Regression: the first learner

![[ai-learning-curves.svg|900]]

Two hundred points scattered around a line. A program holds a slope $m$ and an intercept $c$, predicts $mx + c$, and measures its **loss**, the mean squared error between predictions and the data. [[Differentiation]] gives the direction: $\partial L/\partial m$ and $\partial L/\partial c$ say how the loss changes when each number moves, so step both a little *downhill*, and repeat. This is **gradient descent**, and it is the engine under everything that follows. The script starts at $m = c = 0$ and after two thousand steps has $m = 3.01$, $c = 1.90$ against the true $3$ and $2$, with a remaining error equal to the noise it was given. Nothing was solved in closed form; the line was *learned*. That is regression: supervised learning of a function, a line or a curve, from input variables to a numerical output, used for prediction and forecasting. The Cambridge scheme's words are "finds a mathematical function… best-fit line… calculus is used to find the error gradient… minimise the difference between predicted and actual".

### The three kinds

- **Supervised learning.** The data comes with the right answers: input–output pairs. Regression is supervised (the $y$ values are the labels); so is classification, where the labels are categories (spam or not, cat or dog). The learner's job is the *mapping*.
- **Unsupervised learning.** No labels. The learner has to find structure on its own: which points cluster together, which features vary together. The script's **k-means** is handed three hundred points and the number three, picks three centres, assigns every point to its nearest centre, moves each centre to the middle of its points, and repeats; after four iterations the centres sit at $(0.1, -0.2)$, $(4.8, 4.9)$, $(-0.2, 6.2)$ against the hidden truth of $(0,0)$, $(5,5)$, $(0,6)$, and every point is in the right group. It was never shown a label.
- **Reinforcement learning.** No labels either, but a **reward**: an **agent** takes actions in an environment, sees what happens, gets positive feedback for good outcomes and negative for bad, and adjusts so that similar situations produce better actions next time. The script's agent is dropped on a $5 \times 5$ grid with a goal worth $+10$, a pit worth $-10$ and a cost of $-1$ per step, knowing none of it; six hundred episodes of trial and error later it walks the eight-step route that skirts the pit. Games, robot control and the fine-tuning of language models are reinforcement problems.

![[ai-unsupervised-reinforcement.svg|700]]

> [!tip] The examiners' sentence for each
> Supervised: "enables learning by mapping an input to an output based on example input–output pairs." Unsupervised: "allows the process to discover patterns on its own that were previously undetected." Reinforcement: "learning in an interactive environment by trial and error using its own experiences", "feedback / rewards / punishment", "without any labelled data". Those are the June 2023 and June 2024 mark schemes' own words, and a matching question is the commonest shape.

---

## Part IV — The neuron, and why one is not enough

![[ai-neuron-network.svg|700]]

An **artificial neuron** takes inputs $x_1, x_2, \dots$, multiplies each by a weight $w_i$, adds a bias $b$, and passes the total through an **activation function** that transforms it (a sigmoid bounds its output; ReLU does not): $y = f(\sum w_i x_i + b)$. That is all. The weights are the parameters; learning is adjusting them.

What can one neuron learn? The sum $\sum w_i x_i + b = 0$ is a straight line (a plane, in more inputs), and the neuron says "yes" on one side and "no" on the other. So it can learn AND and OR, and it **cannot learn XOR**, whose yes-cases sit on opposite corners of a square with the no-cases between them: no single line separates them. The script trains one neuron on XOR for five thousand epochs and it sits at $0.5, 0.5, 0.5, 0.5$, having learned nothing, because there is nothing a line can do. Marvin Minsky and Seymour Papert proved this in 1969, and it helped stall neural-network research for fifteen years.

The cure is a **layer**. Put three neurons between the inputs and the output, each drawing its own line, and the output neuron combines *their* answers; three lines can fence off the two corners. The same script, with a **hidden layer** of three, reaches $0.01, 0.98, 0.98, 0.02$ and a loss of $0.0003$. That is an **artificial neural network**: an **input layer** (the data), one or more **hidden layers** (each neuron reading every output of the layer before), and an **output layer** (the answer), every connection carrying a weight. It is a weighted graph, which is one of the ways graphs serve AI.

---

## Part V — Back propagation: how the weights find out they are wrong

A network with a few hundred weights, a loss that measures how wrong its outputs are, and one question: which way should each weight move? Gradient descent wants $\partial L/\partial w$ for every $w$, and there are too many to nudge one at a time.

**Back propagation** is the chain rule of [[Differentiation]] organised so that all those derivatives cost about the same as one forward pass. The loss depends on the output; the output depends on the last layer's weights and on the previous layer's activations; those depend on the weights before, and so on back to the input. So compute the error at the output, multiply it backwards through each layer's weights and the slope of each activation, and at each layer you obtain the gradient with respect to that layer's weights on the way past. The error *propagates back*. Then every weight is adjusted a small step against its gradient, and the process repeats over the data, epoch after epoch, until the loss stops falling.

The script does it in eleven lines and then checks it the only honest way: nudge one weight by $10^{-6}$, watch the loss change, and compare that numerical derivative with what back propagation computed. They agree to $10^{-11}$. Back propagation is not a heuristic or a search; it is calculus, exact to rounding, and it is why the loss curve in Part III's figure falls the way it does.

> [!tip] The mark scheme's version, in order
> Initial outputs are **compared** with the expected outputs; **calculus** is used to find the **error gradient**; the results are **fed back** into the network; the **weightings** of each neuron are **adjusted** to reduce the difference; the process **repeats** until the results are accurate. Six marking points, four needed. Say *gradient* and say *repeat*.

---

## Part VI — Deep learning: why the layers stack

![[ai-deep-vs-shallow.svg|700]]

**Deep learning** is machine learning with neural networks of many hidden layers. The word *deep* is about depth, not size, and the reason for depth is **feature hierarchy**: the first layer learns simple features of the raw input (edges in an image, the slope of a curve), the next layer learns combinations of those (corners, a bend of a bend), the next learns combinations of *those*, and by the top the network is responding to concepts the designer never named. One wide layer has to draw every bend from scratch.

The script makes this measurable. Two spirals, wound three times round each other, six hundred training points, six hundred unseen test points. A network with **one hidden layer of 64** neurons and a network with **three hidden layers of 10** have almost the same number of adjustable numbers, 257 against 261, and the same eight thousand epochs of the same training. The wide one reaches $87.5\%$ on the unseen points and gives up on the outer turns; the deep one reaches $98.8\%$ and follows the spiral to its end. Same budget, arranged in stages.

The examiners add the other reasons the industry uses it: deep networks learn their own features from **raw, unstructured data** (pixels, sound samples, text) rather than needing a human to design the features; they **work well with very large data sets**, keeping on improving where shallower methods plateau; and they train by back propagation, which is why it took until the 2010s, when the data and the graphics hardware to run it on arrived at once. The story of that hardware is in [[Stories/You Never Expect the Change of Needs]]: the chips built to draw triangles for games turned out to be exactly what multiplying weight matrices needs.

---

## Part VII — Graphs in AI

The A-Level asks how **graphs** aid AI, and the answers come in three sizes.

- **A graph stores relationships.** Vertices for entities, edges for how they relate, weights for how strongly or how far: places and roads, people and friendships, words and their co-occurrence, symptoms and diseases. Much of what an AI "knows" is a graph.
- **A problem becomes a path.** Route-finding is the syllabus's example: the shortest route between two places is a search on a weighted graph, and [[Graphs]] works both algorithms the examiners name against real papers. **Dijkstra's algorithm** settles the nearest unsettled vertex and finds shortest paths when edge weights are **non-negative**. **A\*** prioritises the cost so far plus a **heuristic**, an estimate of the remaining cost. A useful heuristic can reduce exploration, but A* is not guaranteed to visit fewer vertices on every problem. An admissible heuristic never overestimates; for graph search, a consistent heuristic or correct reopening of improved paths is needed to preserve the shortest-path guarantee. Game trees, planning and puzzle solving are the same search wearing different clothes.
- **The network is a graph.** A neural network's layers of nodes and weighted connections are a directed weighted graph, and back propagation is a pass over that graph's edges in reverse.

---

## Where it is the working tool

- **Your phone unlocking on your face.** A deep network trained on millions of faces maps an image to a compact code; unlocking compares your code with the stored one. The examiners' report for June 2024 warns that candidates described the *authentication* and not the *AI*: the marks are for the learned mapping, the training data, the layers extracting features from pixels.
- **The spam folder.** Supervised classification on tens of millions of labelled messages; the filter adapts as spammers change tactics, which no rule base could keep up with. The Bayesian version is [[Conditional Probability]] doing the work.
- **AlphaGo, 2016.** Every item on this card in one system: a graph search over the game tree, deep networks estimating which positions are good and which moves are worth trying, trained first by supervised learning on human games and then by reinforcement learning against itself. It beat the world's best player at a game whose tree has more positions than there are atoms.
- **Navigation.** The half-second before the blue route appears is a graph the size of a continent and an A\*-family search across it.
- **Recommendation and search.** Ranking pages, films or products is a mapping learned from what people clicked, with the feedback loop the IGCSE's search-engine question describes: results that were not useful are recorded, and the ranking changes.
- **Medical imaging.** Deep networks reading X-rays and retinal scans match specialists on narrow tasks; the expert systems of the 1970s (MYCIN advised on blood infections) were the same ambition with hand-written rules.
- **Language models.** A very deep network trained by supervised learning to predict the next word over most of the written internet, then shaped by reinforcement learning from human feedback: supervised, deep and reinforcement learning stacked, on the largest data set there is.

---

## Worked examples — every tool named

### Example 1 — the matching question (Cambridge 9618, June 2023 Paper 31, Q2)

*(a) Draw one line from each machine learning category to its description.* — *Tool: the four definitions of Part III.* Supervised → "mapping an input to an output based on example input–output pairs". Unsupervised → "discover patterns on its own that were previously undetected". Reinforcement → "learning in an interactive environment by trial and error using its own experiences". Deep learning → "simulates the data-processing capabilities of the human brain to make decisions". The fifth description, "enables information related to errors produced by the neural network to be transmitted", is **back propagation**, the distractor. *(Four marks.)* *(b) Explain how a graph can aid AI.* — To find the optimal, shortest or most cost-effective route between two nodes, based on distance, cost or time. *(Two marks.)*

### Example 2 — the layers (Cambridge 9618, November 2021 Paper 31, Q9(a))

A diagram shows an input layer, three hidden layers and an output layer. *(i) State the reason for having multiple hidden layers.* — To enable deep learning; a more complex problem needs more layers; to improve accuracy. *(One mark.)* *(ii) Explain how artificial neural networks enable machine learning.* — *Tool: Parts IV and V in order.* ANNs replicate the way the brain works; **weights** are assigned to each connection between nodes; data enters at the input layer and is analysed at each hidden layer, where features are extracted; the training is **repeated many times** to reach optimum outputs; decisions are then made without being explicitly programmed; the output layer gives the result. *(Four marks from the list.)*

### Example 3 — deep learning in two marks (Cambridge 9618, November 2022 Paper 31, Q9(a))

*Describe what is meant by deep learning.* — Uses artificial neural networks with a **high number of hidden layers**, modelled on the brain; the layers progressively extract **higher-level features** from the raw input; it is a specialised form of machine learning. *(Two marks; the follow-up (b) wanted the reasons: it makes good use of unstructured data, and works well with large data sets.)*

### Example 4 — reinforcement learning (Cambridge 9618, June 2024 Paper 32, Q11)

*Explain what is meant by reinforcement learning in relation to AI.* — A machine-learning technique based on **feedback, rewards or punishment**; an **agent** learns to behave in an environment by performing actions and seeing the results; each good action earns positive feedback and each bad one negative; it learns automatically **without labelled data** or specific instructions, and uses the feedback to improve at similar tasks. *(Three marks from five points. Part III's gridworld is this paragraph run for six hundred episodes.)*

### Example 5 — back propagation (Cambridge 9618, November 2025 Paper 32, Q9(b))

*Describe the back propagation of errors method in machine learning.* — Initial outputs are **compared** with expected outputs; **weightings are adjusted** to minimise the difference; **calculus** is used to find the **error gradient** in the outputs; the results are **fed back** into the network; the weightings of each node are adjusted as a result; the process **repeats** until the results are more accurate. *(Four marks. The scheme's gradient check is Part V's.)*

### Example 6 — regression (Cambridge 9618, June 2026 Paper 33, Q9(a))

*Explain what is meant by regression methods in relation to machine learning.* — A **supervised** learning technique; it finds a **mathematical function** or a best-fit line or curve, using **calculus to find the error gradient**, that maps how independent variables influence a dependent variable; used for **forecasting** and prediction; trained to minimise the difference between predicted and actual values. *(Three marks. Part III's line, learned in two thousand steps.)*

### Example 7 — the subset, and A\* against Dijkstra (Cambridge 9618, June 2026 Paper 32, Q9)

*(a) State the subset of AI that makes use of an artificial neural network.* — **Deep learning**. The scheme adds a warning: "machine learning" is not accepted, because not all machine learning uses ANNs. *(b)(i) Compare the two search algorithms.* — A\* uses **heuristics** and does not necessarily pass through every node, and may miss the shortest path if the heuristic is inaccurate; Dijkstra's checks each vertex, finds the shortest path to all nodes, and always finds it. *(Three marks; the working of Dijkstra's on the given graph in (b)(ii) is the kind [[Graphs]] does step by step.)*

### Example 8 — the best question from the other Cambridge board: the diagnosis (Cambridge 0478, June 2025 Paper 12, Q5(a))

A hospital's expert system takes a patient's symptoms through an interface and outputs a diagnosis. *Describe how the expert system decides the diagnosis.* — *Tool: Part II's loop.* The **inference engine** decides which questions to ask, based on the answers so far; the symptoms entered are compared with the facts in the **knowledge base**; the inference engine then applies the **rule base** to those facts to reach the diagnosis. *(The scheme's five points name all three internal components and the loop; an answer that says "it looks up the symptoms" gets one.)* The same board's November 2024 paper gave the paragraph with blanks: an expert system is a type of *artificial* intelligence; symptoms go into the *interface*; the *inference engine* decides which questions to ask by linking the facts in the *knowledge base* to the *rule base*; the *inference engine* decides the diagnosis.

### Example 9 — the search engine (Cambridge 0478, March 2025 Paper 12, Q6)

*(a) One characteristic of AI is the ability to learn. Identify three others.* — Collection of data; rules for using the data; ability to reason; (ability to adapt). *(b) Explain how machine learning is used by the search engine.* — It **changes its own data or rules according to feedback or results**; when a result does not give a suitable response that is recorded, and next time the result is changed, to give more accurate or relevant results in future. *(Three marks each. Part I's checklist and Part III's definition of learning, verbatim.)*

---

## Hands-on

- **`ai-learning-demo.py`** — every method on the card from scratch in numpy: regression, the neuron that cannot learn XOR and the network that can, the gradient check, wide against deep, k-means, Q-learning, the expert system. Change `hidden` in `train_net`, or the pit's position, or add a rule to the car diagnoser, and watch the printed numbers move. Nothing here needs a library; the whole of Part V is eleven lines.
- **`ai-figures.py`** and **`ai-manim.py`** — the figures, and the two films: a network learning the spirals while its loss falls, and the agent's six hundred episodes.
- **Two experiments to run on the demo.** (1) Train the spiral nets for 800 epochs instead of 8000 and see both fail: learning needs time as well as depth. (2) Give k-means the wrong number of groups, $k = 2$ or $k = 5$, and see it obediently find them: unsupervised learning finds the structure you ask for, which is the danger of it.

---

## Common Misconceptions (Teaching Notes)

### 1. "An expert system learns from the cases it sees"
It does not. Its rules were written by people, and it applies them; a new case outside the rules gets no answer until a person adds a rule. "It can learn and adapt" is the characteristic that separates *machine learning* from the rest of AI, and the IGCSE examines the distinction directly.

### 2. "Deep means a lot of neurons"
Deep means a lot of **layers**. A single hidden layer with a thousand neurons is wide, not deep, and Part VI's experiment shows that with the same number of weights the deep arrangement wins because each layer builds on the last's features.

### 3. "Reinforcement learning is supervised learning with rewards as the labels"
There are no labels. A label says what the right answer *was*; a reward says only how well the last action *turned out*, often long after it, and the agent has to work out which of its actions deserved the credit. The scheme's phrase is "without any labelled data".

### 4. "Machine learning is just the answer to any AI question"
The June 2021 report complained of "generic statements about machine learning that were not applied to the context". If the question is about a board game, say what the states, actions and reward are for *that game*; if it is about a search engine, say what feedback it records.

### 5. "Describe the app, not the AI"
Asked how AI is used for face recognition, candidates described how face recognition unlocks the phone. The marks are for the *learning*: the training data, the network mapping pixels to features to an identity, the adjustment of weights. Describe what was learned and how.

### 6. "Back propagation is a kind of search"
It is calculus: the exact gradient of the loss with respect to every weight, computed by the chain rule. Say *gradient*, say *calculus*, say *fed back*, say *repeated*; those are the marking points.

### 7. "Deep learning is a different thing from machine learning"
It is a subset of it, and the 2026 scheme refuses "machine learning" as the answer to "which subset uses neural networks" because the containment runs the other way: all deep learning is machine learning; not all machine learning is deep.

---

## Exam Notes

### Cambridge 9618 (§18.1 Artificial Intelligence — Paper 3)

Four learning outcomes: how **graphs** aid AI (purpose and structure of a graph; A\* and Dijkstra's used for searches, with no requirement to write the algorithms); how **artificial neural networks** have helped machine learning; **deep learning, machine learning and reinforcement learning** and the reasons for using them, with the categories supervised and unsupervised; **back propagation of errors** and **regression methods**. Set every series since 2021 as a four-to-nine-mark Paper 3 question: a matching table, a "describe/explain" on one term (deep learning, reinforcement learning, ANNs, back propagation, regression), and a graph question that may hand you Dijkstra's to run. The schemes are lists of marking points and the answers above quote them; the examiners' standing complaints are the generic-ML-statement and the describe-the-app-not-the-AI errors. The graph algorithms themselves are worked in [[Graphs]]; AI's *applications and impact*, including bias, are §7.1 and live in [[Ethics and Ownership]].

### Cambridge 0478 (§6.3 Artificial intelligence — Paper 1)

Three outcomes: what AI is (a branch of computer science dealing with the simulation of intelligent behaviours); its **characteristics** (collection of data, rules for using it, ability to reason, and possibly the ability to learn and adapt); and the basic operation and components of AI systems, **limited to expert systems and machine learning**, with expert systems having a *knowledge base, rule base, inference engine and interface* and machine learning defined as a program that can *automatically adapt its own processes and/or data*. Two-to-five-mark questions: name the four components, describe the inference engine's role or how a diagnosis is reached, complete a paragraph with the component names, explain how a robot or search engine improves with machine learning. Part I's table and Part II's loop are the whole of it. §6.1 automated systems and §6.2 robotics are the same section's neighbours.

### IB Computer Science (A4 Machine learning — SL and HL)

A4.1 machine-learning fundamentals has two understandings: the **types of machine learning and their real-world applications** (supervised, unsupervised, reinforcement, deep learning), which Parts III–VI cover at the A-Level's depth and beyond, and the **hardware requirements** of the scenarios machine learning runs in (GPUs and accelerators for training, what inference needs on a phone), which this card only touches in Part VI's remark about graphics cards. The IB's framing of the topic, rules-from-data against rules-written, is Part I's. A4.3 (HL) goes further into specific models and their evaluation; A4.2 (HL) data preprocessing is not here. A4.4's ethical considerations are [[Ethics and Ownership]].

### Where it is *not* examined

- **AP Computer Science A** has no AI or machine-learning content; the Java course stops at algorithms and data structures.
- **OxfordAQA International GCSE Computer Science (9210)** has none either: its subject content runs algorithms, programming, data representation, computer systems, networks, cyber security, SQL and web design. **AQA A-level Computer Science (7517)** examines no AI in its written papers; the only place it appears is as a permitted topic for the practical project.
- **9618 §18.1 does not ask you to write** any graph, search or learning algorithm; the Paper 4 programming questions never touch it.

---

## Connections

- **Builds on:** [[Graphs]] — Dijkstra's and A\* worked on real papers; [[Ethics and Ownership]] — bias, the proxy that learns the historical decisions, and the economic and environmental cost of training; [[Differentiation]] — the gradient that every learner walks down; [[Probability Basics]] — the Bayesian spam filter and the reward's expectation.
- **Extends into:** [[The Turing Test]] — whether any of this counts as thinking; [[Compression Is Intelligence]] — prediction and compression as the same act, which is what a language model does; [[Data Protection and Privacy]] — the training data was somebody's.
- **Training without pooling the data:** [[Privacy-Preserving Computation]] — federated averaging, the record a single gradient gives away, and the secure aggregation that hides it.
- **A classifier pointed at people:** [[Affective Computing]] — what a model can and cannot infer about feelings from a face, a voice or a pulse, and why an accurate detector can give an inaccurate answer.
- **Sibling:** [[Sorting]] and [[Searching]] — the classical algorithms that AI search generalises; [[Information Theory]] — the entropy that a learning system reduces.
- **Leads to:** [[You Are a Reinforcement Learner]] — Part III's gridworld agent read as a self-portrait: you are someone else's environment, and a proxy-paid learner circles the checkpoints forever.
- **Story:** [[Stories/The Perceptron and Move 78]] — why these ideas exist in this order: the Navy's press conference, Minsky's theorem and the winters, back propagation's four inventors, two gaming cards, and AlphaGo as the marriage of search and learning.
- **Builds on:** [[Automated Systems and Robotics]] — the sensor → microprocessor → actuator ring that a learning robot is built on; nearly every 0478 robotics question ends by handing the robot machine learning, and the answer is Part III's definition applied to the scenario.

---

## Beyond Syllabus

### Universal approximation, and its small print
A network with one hidden layer and enough neurons can approximate any continuous function (Cybenko 1989, Hornik 1991). So depth is not *necessary* in principle; Part VI shows it is necessary in practice, because "enough neurons" for a wide net can be exponentially more than a deep net needs, and training has to find them.

### Overfitting, and why the script tested on unseen points
A network with enough weights can memorise its training data, scoring perfectly on it and badly on anything new. The only honest score is on data the network never saw, which is why the spiral accuracies are measured on a separate six hundred points; the gap between training and test error is the measure of memorisation, and every serious system holds data back to measure it.

### The perceptron and the winter
Frank Rosenblatt's perceptron (1958) was the single neuron of Part IV, built in hardware, and the *New York Times* reported it would one day "walk, talk, see, write". Minsky and Papert's 1969 book proved its XOR limit and funding for neural networks collapsed. Back propagation for multi-layer nets was rediscovered several times and made famous by Rumelhart, Hinton and Williams in 1986; the data and hardware to make it dominant arrived around 2012, when a deep network (AlexNet) halved the error on the ImageNet image-recognition contest.

### Transformers, in one paragraph
The language models of the 2020s are deep networks whose layers are **attention**: each word's representation is updated by a weighted mix of every other word's, with the weights themselves computed from the words. Trained by back propagation to predict the next token over trillions of words, they turn out to encode grammar, facts and some reasoning as side effects of prediction, which is [[Compression Is Intelligence]]'s thesis made industrial.

---

## LaTeX Reference

| Rendered | Source | Meaning |
|---|---|---|
| $y = f\!\left(\sum_i w_i x_i + b\right)$ | `y = f\!\left(\sum_i w_i x_i + b\right)` | one artificial neuron |
| $L = \dfrac{1}{n}\sum (\hat y - y)^2$ | `L = \dfrac{1}{n}\sum (\hat y - y)^2` | mean squared error, the loss |
| $w \leftarrow w - \eta\,\dfrac{\partial L}{\partial w}$ | `w \leftarrow w - \eta\,\dfrac{\partial L}{\partial w}` | gradient-descent update |
| $\delta^{(l)} = (W^{(l+1)})^{\mathsf T}\delta^{(l+1)} \odot f'(z^{(l)})$ | `\delta^{(l)} = (W^{(l+1)})^{\mathsf T}\delta^{(l+1)} \odot f'(z^{(l)})` | back propagation, one layer back |
| $Q(s,a) \leftarrow Q(s,a) + \alpha\,[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$ | `Q(s,a) \leftarrow Q(s,a) + \alpha\,[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]` | Q-learning update |
| $f = g + h$ | `f = g + h` | A\*'s ranking: cost so far plus heuristic |
