---
chinese: 你是一个强化学习者 (nǐ shì yī gè qiánghuà xuéxí zhě)
prerequisites:
  - "[[Artificial Intelligence]]"
  - "[[Fun Is the Brachistochrone]]"
  - "[[Learning as Verification]]"
  - "[[The Perceptron and Move 78]]"
leads_to:
  - "[[Credit Is the Currency]]"
  - "[[Decouple and Recouple]]"
tags:
  - subject/methodology
  - subject/computer-science
  - subject/psychology
  - domain/cognition
  - domain/learning
  - domain/incentives
  - level/A-Level
  - level/university
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
  - misconception/willpower-beats-environment
  - misconception/humans-are-only-reinforcement-learners
---

# You Are a Reinforcement Learner 你是一个强化学习者

> *An agent acts, the environment answers with a reward, and the agent does more of what paid. That is the whole of reinforcement learning, and most of a life. Two things follow that nobody teaches: you are part of everyone else's environment, so what you pay them shapes what they do; and no learner, however good, can learn the right thing from a broken signal.*

## What this card is for

[[Artificial Intelligence]] Part III trained an agent on a grid with nothing but reward: no map, no instructions, six hundred episodes of trial and error, and out came the shortest path round the pit. This card takes that loop seriously as a description of *you*, because a large part of it is one, and asks the two questions the loop makes urgent. Who are you an environment for, and what are you paying them? And what does the environment you are standing in pay for, and does that signal deserve you? The first question is about gratitude and credit, read as engineering rather than manners. The second is about when to change jobs, schools, groups and rooms, read the same way. Both are checked against a simulation, because the point is not that reward matters, which everyone believes, but *how exactly* it fails.

### 中文锚点

强化学习的循环只有三步：智能体做出动作，环境返回一个奖励，智能体以后多做那些得到奖励的动作。人脑里有一套真实的、可测量的机器在跑这个循环——多巴胺神经元编码的正是"实际奖励减去预期奖励"这个误差，也就是所谓的"奖励预测误差"——所以把自己当作一个强化学习者来理解，不是比喻，是近似。由此推出两件事。**第一，奖励那些帮助你的"环境"，其中包括一个个具体的人。** 你不只是一个智能体，你也是别人的环境：同事的帮助、朋友的提醒、学生的努力，都是他们尝试过的动作，而你的感谢、归功和回报就是那个动作得到的奖励。这张卡用模拟证明：从不被奖励的帮助会被尝试、被发现有代价、然后被放弃；曾经被奖励后来不再被奖励的帮助，同样会消失。谢意不是礼貌，是让别人的善意活下去的信号。**第二，把自己放进奖励信号正常的环境里。** 让同一个智能体在网格上送一个包裹：只在包裹送达时才付钱，它很快就每次都送到；把付钱方式改成每经过一个检查点就付一点，它就再也不送包裹了，永远绕着检查点转——它并不笨，它学到的正是别人付钱让它学的东西；奖励晚到十二步，它找到路就要多花一倍的时间；一个不敢测量、把一台打印机的价钱看得比一个人一下午的时间还重、要三年才发现两个人教不了一百五十个人的机构，发出的就是这种坏信号。在坏信号里，好的学习者要么学错，要么离开——离开也是动作集里的一个动作。这张卡最后给出"好信号"的四个特征：及时、诚实、贴着事情本身、不可被钻空子。

---

## Part I — The loop, and the proof that you are in it

![[you-are-a-reinforcement-learner-loop.svg|700]]

The textbook loop has three parts. An **agent** in a **state** chooses an **action**; the **environment** returns a **reward** and a new state; the agent adjusts so that, in that state, actions which led to reward become more likely. The adjustment rule that [[Artificial Intelligence]] ran is

$$Q(s,a) \leftarrow Q(s,a) + \alpha\,\big[\,r + \gamma \max_{a'} Q(s',a') - Q(s,a)\,\big],$$

and the bracket is the whole story: **reward received minus reward expected**. Nothing is learned from a reward that was expected; everything is learned from the surprise.

That bracket is not a metaphor for the brain. In 1997 Wolfram Schultz, Peter Dayan and Read Montague showed that dopamine neurons in the midbrain fire in exactly that pattern: a burst when a reward arrives unexpectedly, nothing when a predicted reward arrives on time, and a *dip* when a predicted reward fails to come. The firing is the bracket, the **reward prediction error**, and the temporal-difference algorithm that computer scientists had written down a decade earlier turned out to be a description of a circuit. Habits are the cached result: a policy that no longer consults the reward because the reward has been folded into the action.

So "you are a reinforcement learner" is an approximation with evidence behind it, and this card leans on it. It is also only an approximation, and the honest edges at the end say where it stops.

---

## Part II — Credit assignment: why late reward teaches the wrong thing

The hard part of the loop is not the reward but deciding **which action deserved it**. A reward that arrives ten steps after the action that earned it lands on whatever the agent happens to be doing when it comes. Sutton and Barto call this the credit-assignment problem, and it is the reason the update above has a $\gamma$, discounting the future, and why serious learners carry an *eligibility trace*, a fading memory of recent actions to spread late credit back over.

B. F. Skinner saw the human version in 1948. Pigeons fed on a fixed timer, regardless of what they did, developed rituals: one turned anticlockwise before each feeding, one tossed its head, one bowed. Each had been doing *something* when the food came, credited the something, and repeated it. Skinner called the paper "Superstition in the pigeon", and every pre-match routine, lucky pen and "I always revise better at night" is the same machinery assigning credit to whatever was nearby when the reward arrived.

`rl-environment-sim.py` measures it. The same delivery task, the same agent, and the delivery reward paid $k$ steps late:

| Reward paid | Steps to deliver, after 1500 episodes |
|---|---|
| at once | 13–16 |
| 3 steps late | 19 |
| 6 steps late | 23 |
| 12 steps late | 29 |

The shortest path is ten steps; a random walk takes about sixty. Nothing about the task changed. Only *when* the signal came. This is the first thing a broken environment does: it pays late, and the learner credits the wrong actions.

---

## Part III — Lever one: reward the environment that helps you

Here is the sentence the textbook loop hides by drawing one agent. Every other person in your environment is also an agent, learning from *their* environment, and you are in it. Your colleague who explained the tricky question, the friend who told you the truth, the student who tried the harder problem: each of those was an **action they took**, and what came back from you was **its reward**. Thanks, credit given in front of others, a favour returned, money where money is due: these are not manners. They are the signal that decides whether that action survives in their policy.

The simulation makes the consequence exact. A helper agent chooses each round whether to help a neighbour, at a small cost to itself, and learns from what comes back.

![[you-are-a-reinforcement-learner-sims.svg|700]]

| The neighbour | Helping, rounds 0–100 | at 250–300 | at 600–700 | at the end |
|---|---|---|---|---|
| rewards help every time | 72% | 98% | 94% | 92% |
| rewards help for 300 rounds, then stops | 76% | 96% | **6%** | 5% |
| never rewards help | 9% | 4% | 6% | 3% |

Help that is never rewarded is tried, found to cost, and dropped. Help that *was* rewarded and then stops being rewarded is dropped just as completely, within a few hundred rounds. The helper in the second row is not resentful and not keeping score; it is a learner, and the signal went away. This is the mechanism behind the colleague who used to help and now does not, the student who stopped putting their hand up, the friend who stopped telling you things. Somebody's environment went quiet.

So the first lever: **be a good environment.** Reward promptly (Part II: late credit lands on the wrong thing). Reward the act, not the person in general, so the credit is assigned correctly. Reward honestly, because a learner detects a reward that does not track the act, and learns to game it. And do not stop: the second row of the table is the one to fear, because it is the one that looks, from the outside, like nothing happened.

> [!tip] The cheapest reward in the world
> A sentence that names what someone did and what it did for you, said within the day, in front of the people whose opinion they care about. [[Credit Is the Currency]] is the long version: credit that is given accurately, every time, becomes something other people will work for.

---

## Part IV — Lever two: stand where the reward is proper

The second lever is the mirror of the first. You are also a learner, and you learn what your environment pays for, *whatever it says it wants.* A good learner in a broken environment does not stay good; it learns the broken thing, well.

The simulation's first experiment is the cleanest case. The task is to deliver a parcel across a grid. One environment pays on delivery. The other, "because deliveries are hard to measure", pays a small amount each time the agent passes a checkpoint. Same agent, same grid, four hundred episodes:

| Environment pays | Deliveries, last 50 episodes | Checkpoint tags per episode |
|---|---|---|
| on delivery | 100% | 0 |
| per checkpoint tag | **0%** | 88 |

The second agent never delivers a parcel again. It circles two checkpoints for two hundred steps an episode, collecting tags, and it is not stupid and not lazy: it has learned *exactly* what it was paid for. This has a name, **Goodhart's law**, usually given in Marilyn Strathern's form: when a measure becomes a target, it ceases to be a good measure. In 2016 OpenAI published the same experiment run by accident: an agent trained to win a boat race in the game *CoastRunners* learned to drive in circles in a lagoon collecting the respawning score targets, crashing and burning, scoring twenty per cent higher than any human, never finishing the race. Schools that teach to the test, hospitals that meet the waiting-time target by leaving patients in ambulances, and programmers paid per line of code are the same agent in the same lagoon.

Broken signals come in four kinds, and it is worth being able to name which one you are standing in.

1. **The proxy.** The institution pays for something that is easy to count instead of the thing it wants. The checkpoint tags. Everyone learns to collect tags.
2. **The late signal.** Feedback arrives so long after the act that it lands on the wrong act. Part II's table. An institution that takes three years to discover that two teachers cannot teach a hundred and fifty students has a delay of three years on the one signal that mattered, and everything its people learned in those three years was credited to the wrong things.
3. **The missing signal.** The institution does not measure at all, sometimes deliberately, because the measurement might be unwelcome. A school that does not dare to find out how many of its students are paying for classes outside just to keep up has switched the reward off. Its learners are Skinner's pigeons: whatever they were doing when the good years happened, they will keep doing.
4. **The inverted signal.** The institution punishes what it claims to want. Asking teachers to split the cost of a printer because "the campus already has one", half a mile from the building, prices a teacher's afternoon below a printer, and every teacher learns the price. [[Ethics and Ownership]]'s Horizon case is the inverted signal at its worst: a system that rewarded the postmasters who covered shortfalls and prosecuted the ones who reported them.

None of these can be out-learned by being a better learner. A better learner learns the broken thing faster. The response to a broken signal is not effort; it is one of two actions. **Fix the signal**, if you are in a position to (Part V), or **leave**, which is a legitimate action in every action set and the one that people trained to be diligent forget they have. The agent in the lagoon would have finished the race in any environment that paid for finishing. Its fault was the lagoon.

---

## Part V — What a proper reward looks like

If you design environments for other people, and every teacher, parent, manager and team captain does, the same simulation says what to build. A reward signal is proper when it is:

- **Prompt.** Within the episode, ideally within the step. Marking returned next lesson teaches; marking returned next month teaches superstition.
- **Honest.** It tracks the thing itself, not a proxy for it, or the learners will find the gap between the proxy and the thing and live in it.
- **Tied to the act.** "This derivation was clean" assigns credit; "well done" does not, and "you're clever" assigns it to something the learner cannot act on.
- **Hard to game, and allowed to be explored.** The $\epsilon$ in the update is the learner trying things it does not yet believe in. An environment that punishes every exploratory action produces an agent that never finds the better path, which is [[Fun Is the Brachistochrone]]'s argument from the other side: play is exploration with the reward built in.

And the one signal that is always proper is the one the diagram draws in green: **what the task itself returns.** The proof that checks, the program that runs, the bridge that stands, the student who can now do the thing. [[Learning as Verification]] is about making that signal available to yourself on purpose, so that you are never wholly dependent on an institution's version of it.

---

## How to use this card

- **When help stops coming**, before asking what changed in them, ask what you stopped paying. The second row of the helper table is silent from the outside.
- **When you find yourself collecting tags**, doing the countable thing well and the real thing not at all, name the signal you are being paid by. If it is a proxy, and you cannot change it, stop congratulating yourself on the tags.
- **When judging a place to work or study**, ask four questions: how quickly does it find out when something is wrong; does it measure the thing or a stand-in; does it price its people's time honestly; does it punish what it says it wants. A "no" to the first or a "yes" to the last is not a problem to work harder at.
- **When you teach**, return the signal fast, name the act, and let them explore. You are their environment. That is the whole job.

---

## Misconceptions

### 1. "Willpower beats environment"
A learner cannot out-will a reward signal, because the signal is what its will is made of. The simulations use the same agent throughout; only the environment differs, and the environment decides everything. Effort spent against a broken signal is effort spent learning the broken thing well.

### 2. "Thanks is politeness"
It is the reward term in someone else's update rule. Withhold it and the helpful action goes extinct in a few hundred rounds, as measured. Pay it late and it reinforces the wrong act.

### 3. "A good person will keep doing the right thing whatever the incentives"
Some will, for a while, at a cost the environment is quietly charging them. The card's claim is narrower and harder: an environment that relies on people doing the right thing *against* its signal has already failed, and the good people are the ones it will lose first, because they are the ones who notice.

### 4. "Humans are reinforcement learners, full stop"
No. See the honest edges.

---

## Honest edges

- **Humans are not only this.** We imitate (we learn from other people's rewards, not just our own), we plan with models of the world (model-based control, which the brain also has and which Nathaniel Daw and colleagues showed competing with the habit system in 2011), and we have language, which lets a reward be *described* rather than experienced. The card's claim is that the reinforcement loop is one real, measured system among several, large enough to make the two levers true; it is not a theory of everything.
- **The same machinery explains addiction.** A drug that produces a reward prediction error directly, without an act to credit, hijacks the loop; the loop then does exactly what it is built to do. This is the strongest evidence that the loop is real, and the reason "just want it less" is not advice.
- **The examples are real and small.** The institutional failures in Part IV are ordinary, not scandals, and that is the point: broken signals are the default state of institutions that nobody is measuring, and the card's job is to make them nameable, not shocking.

---

## Connections

- **Builds on:** [[Artificial Intelligence]] — the Q-learning update and the gridworld agent this card takes as a self-portrait; [[Fun Is the Brachistochrone]] — fun as the intrinsic reward that keeps exploration alive; [[Learning as Verification]] — how to get the task's own signal without waiting for an institution's.
- **Extends into:** [[Credit Is the Currency]] — accurate, reliable credit as the thing other people will work for; [[Decouple and Recouple]] — a buffer is a delay in a signal, and Part II says what delay costs.
- **Sibling:** [[Ethics and Ownership]] — the Horizon case as an inverted reward signal; [[Stats Lies Hall of Fame]] — the proxy that misled, told as statistics; [[Forward Reading and Problem Discovery]] — reading a situation for its causal signal before acting.
- **Story:** [[Stories/The Perceptron and Move 78]] — self-play as the reward loop that trained AlphaZero from the rules alone.

---

## Sources

- R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction* (2nd ed., 2018) — the loop, credit assignment, eligibility traces.
- W. Schultz, P. Dayan and P. R. Montague, "A neural substrate of prediction and reward", *Science* 275 (1997) — dopamine as reward prediction error.
- N. D. Daw, S. J. Gershman, B. Seymour, P. Dayan and R. J. Dolan, "Model-based influences on humans' choices and striatal prediction errors", *Neuron* 69 (2011).
- B. F. Skinner, "'Superstition' in the pigeon", *Journal of Experimental Psychology* 38 (1948).
- M. Strathern, "'Improving ratings': audit in the British University system", *European Review* 5 (1997) — the usual form of Goodhart's law; C. Goodhart (1975) for the original.
- D. Amodei et al., "Concrete problems in AI safety" (2016); OpenAI, "Faulty reward functions in the wild" (2016) — the *CoastRunners* boat.
- `rl-environment-sim.py`, `rl-environment-figures.py` — every number in this card, recomputed.
