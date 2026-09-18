---
chinese: "你是架构师，AI 是砌砖工 (nǐ shì jiàgòushī, AI shì qìzhuāngōng)"
prerequisites:
  - "[[Forward Reading and Problem Discovery]]"
  - "[[Chain of Thought]]"
  - "[[Learning as Verification]]"
leads_to: []
tags:
  - subject/methodology
  - subject/computer-science
  - domain/problem-solving
  - domain/software-engineering
  - level/life
  - level/university
  - type/methodology
  - type/meta
  - misconception/delegating-judgment
  - misconception/tests-prove-correctness
---

# You're the Architect, the AI is the Bricklayer 你是架构师，AI 是砌砖工

> You ask for a bill-splitting app. It arrives with rounded buttons, a cheerful animation and three payments of £3.33 for a £10 bill.
>
> The animation works. The money does not.

## Definition

### Formal

**Directing AI-assisted work** means maintaining a justified connection between a human need, a specification, an implementation and evidence that the implementation meets the need.

A **specification** states the required behaviour and its constraints. An **architecture** divides the system into parts and defines how they communicate. **Acceptance evidence** is something inspectable—a calculation, a test result, an observed interaction—that supports deciding the work is ready for its intended use.

These are different jobs. A program can implement its specification perfectly and still solve the wrong problem. Its parts can each work and still disagree about what a number means when they pass it between them.

**Delegating implementation does not delegate judgment.** Someone still has to own the connection all the way from need to evidence.

### Intuitive — responsibility, not a caste system

An architect does not personally place every brick. They must nevertheless understand what is carrying the load, where the openings are, and what would make the structure fail.

The analogy has a limit. A language model can propose the architecture, challenge requirements, write tests and spot errors; a human may do any of the implementation. The roles can move between participants. **“Architect” names responsibility for the whole**, rather than a claim that only humans can design or that implementation requires no thought.

If you accept a design because its author sounds confident, you have left that responsibility unfilled. If you can explain its constraints, compare alternatives and examine meaningful evidence, you are doing the work—even when someone else suggested every line.

### 中文锚点 (Chinese Anchor)

**你是架构师**，意思是你要对三件事负责：究竟要做什么，各部分为什么能配合，以及凭什么判断它做好了。实现可以交给 AI，判断却不会因此自动完成。

想想聚餐后的 AA 分账：10 元分给三个人，每个人都付 3.33 元，就少了一分钱。让 AI 写代码之前，先把规则说清楚：**总额一分不能少，每个人的份额最多相差一分，多出来的一分按事先约定的顺序分配。** 程序算错了，就沿着输入、计算、显示这条路径找出哪一步偏离了规则，再用自己独立算出的结果检验。这样，编程知识就成了你指挥和验收工作的工具。AI 也能提出设计和测试方案；架构师的职责是看懂并质疑其中的假设，判断现有证据是否足够。

### The family resemblance

| Habit you already know | What it becomes when directing a build |
|---|---|
| [[Forward Reading and Problem Discovery]]: read each fact for what it locks down | Read the user's situation for constraints; follow data through code you did not write |
| [[Chain of Thought]]: name the trigger that selects a tool | Justify each design choice by the requirement that makes it useful |
| [[Learning as Verification]]: choose a check capable of exposing a mistake | Define acceptance evidence before becoming attached to the implementation |

The new move is to **shape the work so that those checks are possible**. A separate calculation function is easier to inspect than arithmetic tangled into twelve button handlers. Architecture changes the cost of understanding and verification.

## Key Facts — the decisions behind the code

### 1. A wish leaves degrees of freedom

“Build a bill splitter” leaves unanswered questions:

- Equal shares, item-by-item shares, or shares weighted by appetite?
- One currency, or several?
- What happens to a remainder smaller than the smallest coin?
- Is it a calculator, a record of debts, or a service that moves money?
- Must the result survive closing the app? Must friends see the same result?

A model must do something with those gaps. Its choices may be reasonable and still differ from yours. The problem began before the first line of code.

A useful specification does not describe every pixel. It removes the ambiguities that would change the meaning of success. Other decisions can remain provisional and be tested with a small prototype.

### 2. An invariant gives you something to defend

An **invariant** is a property that must hold across the relevant cases or operations. For an equal split into whole pennies, conservation of the total is one:

$$\sum_{i=1}^{n} s_i=T.$$

Here $T$ is the total in pennies, $n$ the number of people, and $s_i$ person $i$'s share. Rounding each share independently does not guarantee this equation.

Invariants are stronger than screenshots. A screenshot shows one arrangement of pixels; the invariant applies when the bill changes, the group changes and the interface is redesigned.

But an invariant is only as appropriate as its assumptions. “Everybody pays the same” is impossible for £10 divided into three whole-penny payments. A designer has to resolve that conflict, not ask the programmer to conceal it.

### 3. Boundaries make disagreement visible

Separate three responsibilities:

| Part | Receives | Produces | Must preserve |
|---|---|---|---|
| Input conversion | Text such as `"10.00"` and a people count | Validated integer pennies and count | Exact amount; rejects unsupported input |
| Allocation | Integer total and positive integer count | Ordered list of integer shares | Total, count, fairness and agreed remainder policy |
| Display | Integer shares | Currency strings | `334` pennies is shown as `£3.34`, never `£334` |

The boundary between two parts is an **interface**: an agreement about what crosses it, in what form, and what it means.

This is [[Decouple and Recouple]] applied to responsibility. The calculator can be checked without a browser. A new colour scheme should not change who owes the extra penny. The parts remain connected through explicit agreements.

A boundary also creates a possible failure. A caller sending pounds to a function expecting pennies can produce a mathematically correct answer to the wrong question. Units belong in the interface, not merely in somebody's memory.

### 4. Evidence has a scope

A passing function test supports a claim about that function on those inputs. It does not show that the button calls it, that a saved bill reloads correctly, or that a person understands the result.

Keep claims as narrow as their evidence:

| Claim | Evidence that addresses it |
|---|---|
| “The allocation conserves the total.” | Argument about the algorithm, plus tests designed to expose violations |
| “Typing £10 and 3 people displays the agreed shares.” | Exercise the actual input-to-display path |
| “The bill survives reopening.” | Save, close, reopen, compare with the original |
| “People can use it.” | Watch someone complete the intended task without coaching |

[[Program Development Life Cycle and Testing]] gives the testing vocabulary. The supervisory skill is asking **which claim a test actually supports**.

## Worked Example — the missing penny

### Step 1 — read the situation forward

**Trigger → tool:** money is recorded in whole pennies → integer representation.

Our first version is a local calculator for one bill. It accepts a non-negative integer number of pennies and a positive integer number of people. The result follows the displayed participant order. It records amounts owed; it makes no payments and stores no history.

Those last choices keep the first slice understandable. Persistence and payment processing would introduce different requirements; they are not necessary to establish whether we can divide £10 correctly.

**Trigger → tool:** indivisible pennies → quotient and remainder, rather than independently rounded decimal shares.

The agreed contract is:

1. Return exactly $n$ shares, each a non-negative integer number of pennies.
2. Their sum is $T$.
3. The largest and smallest differ by at most one penny.
4. Give extra pennies to the earliest participants in the agreed order.
5. Reject inputs outside the stated domain, including fractional counts and negative totals.

Condition 4 is a **policy choice**, not a theorem about fairness. Rotating the order between meals might be fairer over time. That would require remembering previous meals; for a single-bill calculator, an explicit fixed order is a simpler agreement.

### Step 2 — settle one result before reading the code

**Tool: division with remainder.** The trigger is that exact equality of whole-penny shares is impossible when the total is not divisible by the count.

For £10 and three people:

$$1000=3\times333+1.$$

Everyone can receive 333 pennies; one penny remains. The first person receives it:

```python
expected = [334, 333, 333]
```

Write that expectation from the agreement. Do not obtain it by running the implementation being checked.

A second hand calculation, $2=3\times0+2$, gives `[1, 1, 0]`. This tiny case makes the remainder impossible to overlook.

### Step 3 — inspect a plausible implementation

```python
def split_bad(total_pence, people):
    return [round(total_pence / people)] * people

print(split_bad(1000, 3))  # [333, 333, 333]
```

**Tool: conservation check.** The total is fixed by the requirement, so add the outputs before admiring the interface.

The returned sum is 999. One penny vanished. For two pennies shared by three people, the same function returns `[1, 1, 1]`: it invents a penny instead.

This failure is deeper than floating-point precision. Even exact arithmetic followed by independent rounding cannot make three equal integer shares add to 1000. The **allocation policy** must account for the remainder.

**Tool: causal trace.** Feed `1000, 3` directly to the allocation function. If it already returns the wrong list, the display is not the cause of this failure. Trace the division, rounding and repetition; the remainder is discarded at rounding and never allocated.

A precise repair request is now possible:

> For input `(1000, 3)`, allocation returns `[333, 333, 333]`, whose sum is 999. The contract requires 1000 and assigns extra pennies in participant order. Replace independent rounding with quotient-and-remainder allocation. Preserve the function's units and return type, and include the two-penny case.

This request carries a reproducible failure, a violated rule and the intended boundary. “It looks wrong, try again” carries none of them.

### Step 4 — derive the repair

**Tool: the division algorithm.** For $T\geq0$ and integer $n>0$, there are unique integers $q,r$ such that

$$T=nq+r,\qquad 0\leq r<n.$$

Give everyone $q$ pennies, then one extra penny to each of the first $r$ people.

- **Count:** one share is created for each of the $n$ people.
- **Total:** $(n-r)q+r(q+1)=nq+r=T$.
- **Fairness:** each share is either $q$ or $q+1$, so the difference is at most one.
- **Order:** the extra penny goes exactly where the agreed policy says.

The proof explains the algorithm; the implementation still needs checking against that proof.

```python
def split_pence(total_pence, people):
    if type(total_pence) is not int or type(people) is not int:
        raise TypeError("Use integer pennies and an integer people count")
    if total_pence < 0 or people <= 0:
        raise ValueError("Total must be non-negative; people must be positive")
    quotient, remainder = divmod(total_pence, people)
    return [quotient + (1 if i < remainder else 0)
            for i in range(people)]
```

The exact type checks intentionally reject `True` and `False` as amounts or counts; Python otherwise treats booleans as a kind of integer. This function accepts plain Python integers, not every possible numeric object.

An equal split needs an output for each person, so creating this list takes time and space proportional to $n$. No database or clever search algorithm improves that requirement. **Choosing a simple design for a stated reason is architectural work.**

### Step 5 — make the check capable of refusing the work

**Trigger → tool:** the contract contains several independent promises → check each one, including its smallest revealing case.

```python
assert split_pence(1000, 3) == [334, 333, 333]
assert split_pence(2, 3) == [1, 1, 0]
assert split_pence(0, 3) == [0, 0, 0]
assert split_pence(1000, 1) == [1000]

for total in range(101):
    for people in range(1, 11):
        shares = split_pence(total, people)
        assert len(shares) == people
        assert all(type(s) is int and s >= 0 for s in shares)
        assert sum(shares) == total
        assert max(shares) - min(shares) <= 1
        assert shares == sorted(shares, reverse=True)
```

The final condition checks the agreed order: larger shares come first. Conservation and fairness alone would allow `[333, 333, 334]`, which breaks that policy.

This finite sweep checks 1,010 combinations. It does not exhaust all integers. The earlier argument explains the general rule; the sweep looks for implementation mistakes on a useful small range. Invalid inputs also need tests that confirm the promised exceptions.

Now deliberately run the same checks against `split_bad`. The checks should fail. This is a small **mutation test**: deliberately insert a fault and see whether the test notices. A test suite that welcomes the missing penny is giving you reassurance without defending your requirement.

The runnable companion `architect-bill-splitter.py` contains both versions, the checks, invalid-input cases and a second faulty version that allocates the remainder to the wrong end. Run it with Python 3; it reports which checks reject each fault.

### Step 6 — connect the real path

**Trigger → tool:** independently correct parts can disagree at a boundary → an integration test.

The function expects `1000`, while a person types `"10.00"`. Keep the currency conversion exact: parse the decimal text under a stated format, allowing at most two decimal places, and convert to integer pennies. Multiplying an arbitrary binary float by 100 and truncating it can lose a penny before the allocation even starts.

On the actual interface, enter £10.00 and three participants in a known order. Observe £3.34, £3.33 and £3.33 beside the correct names. Change the bill to £0.02; observe £0.01, £0.01 and £0.00. Try a rejected input and inspect the message. Change an input after a result is already on screen; verify that the result updates rather than remaining stale.

The allocation function and its tests are an implemented core. The interface path just described is a specification for the next slice, not evidence that a complete app has been built. **Naming that boundary honestly is part of the skill.**

## When the requirement changes — architecture earns its keep

A friend says, “I did not order dessert. Why am I paying a third of it?”

The program has not developed a bug. The equal-share assumption no longer matches the need.

**Trigger → tool:** different people participate in different purchases → represent each item with its amount and participant IDs, rather than patching the final display.

For each item, apply a stated allocation rule to its participants; then add each person's item shares. Require that the sum across people equals the sum across items. Decide separately whether a service charge is an item, a percentage, or already included. Decide how an item with no participants is handled.

The old equal-split function can remain a small component. The new design needs another layer to collect per-person totals and new tests for people who share some items but not others. The display consumes those totals. This is why the earlier boundaries mattered.

Ask the model for two candidate designs and their tradeoffs. Then ask what each makes awkward when a requirement changes. A design is understandable when you can predict the consequence of changing it, not merely repeat its description.

## How to practise — keep your judgment exercised

### Build a thin slice you can follow end to end

A **vertical slice** is one usable path through the necessary layers: one input, one calculation, one displayed result. It exposes misunderstandings sooner than separately generating an enormous backend and an enormous frontend and hoping they fit.

Keep each change small enough to inspect. Preserve a working version before changing a shared rule. After a change, run both the new check and the earlier checks: fixing itemised dessert must not break the one-person bill.

### Ask for evidence you can inspect

Useful requests include:

- “State the input units, output units and invalid-input behaviour.”
- “Which requirement selects this data structure?”
- “Give me the smallest input that exposes the reported fault.”
- “Show the exact test command and its actual result.”
- “Which parts of the claimed behaviour have not been exercised?”

A generated explanation is a claim about the work. Compare it with the actual code, outputs and observations. Asking the same model to agree with itself does not create independent evidence; a hand calculation grounded in the requirement contributes something different.

### Keep implementing enough to predict

Try writing one small function yourself, then compare approaches. Predict a result before running it. Change a requirement and predict which parts must change. Explain the failure without using the model's explanation as your script.

This is the practical reason to learn [[Programming Fundamentals]], algorithms and data structures even when code can be generated: they let you recognise what a design implies and construct a meaningful objection. You need not memorise every library to supervise work, but unfamiliarity with a crucial part is a reason to learn, simplify or get a qualified review.

Verification is not automatically easy. Deciding whether arbitrary software satisfies arbitrary intentions can be harder than writing a small replacement. Good boundaries, explicit assumptions and limited scope make *this* work more checkable; the difficulty has been managed, not abolished.

## Common Misconceptions

### “Architect means I describe the idea once and wait.”

A description starts the loop. Inspection may expose missing requirements; a prototype may show that the original need was misunderstood. **Fix:** stay with one small slice until you can trace why its output follows from its inputs.

### “All the tests pass, so it is correct.”

Tests can share the implementation's mistaken assumption. Three equal rounded shares will pass a test that expects three equal rounded shares. **Fix:** derive expected behaviour from the need; introduce a deliberate fault and confirm a relevant check rejects it.

### “More elaborate architecture means better engineering.”

A database, account system and network service introduce new obligations. Our single-bill allocation needs none of them. **Fix:** name the requirement each component serves, and the cost of omitting it. Add complexity when a real constraint earns it.

### “The AI made the decision, so the result is its responsibility.”

The user receives the system you accepted. The practical question remains whether somebody understands its assumptions and has evidence for its use. **Fix:** record important decisions with the reason and the check supporting them; unresolved questions stay visible.

## Connections

- **Parents:** [[Forward Reading and Problem Discovery]] supplies causal tracing; [[Chain of Thought]] supplies tool-selection triggers; [[Learning as Verification]] supplies checks that can refuse plausible work.
- **Engineering companion:** [[Program Development Life Cycle and Testing]] names the stages and testing methods used in the loop.
- **Design companion:** [[Decouple and Recouple]] explains why separating responsibilities can make parts easier to change and recombine.
- **Practical foundation:** [[Programming Fundamentals]] supplies the variables, selection, iteration and functions needed to read the allocation code.
- **Learning check:** [[The Feynman Technique]] — explain the remainder policy and rebuild the argument without reading the implementation.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\sum_{i=1}^{n}s_i=T$ | `\sum_{i=1}^{n}s_i=T` | Every penny is allocated |
| $T=nq+r$ | `T=nq+r` | Quotient-and-remainder decomposition |
| $0\leq r<n$ | `0\leq r<n` | Fewer remainder pennies than people |
