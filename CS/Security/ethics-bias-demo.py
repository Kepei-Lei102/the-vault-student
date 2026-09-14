"""
ethics-bias-demo.py — "we removed the protected column, so the model is fair" — tested.

Companion to [[Ethics and Ownership]].

A synthetic hiring data set is generated with a KNOWN story built in:
  * every applicant has a true ability score (what a fair hire should track);
  * applicants belong to one of two groups, A or B;
  * the HISTORICAL hiring decisions used as training labels were biased —
    group B applicants were hired less often at the same ability;
  * a "postcode" feature is correlated with group (the proxy — in the real
    world, redlining made postcode a proxy for race in the USA for decades).

Then a logistic-regression classifier (written from scratch in numpy, no
library) is trained three ways and audited by the selection rate per group
at equal ability:
  1. with the group column          — learns the bias directly;
  2. WITHOUT the group column       — learns it anyway, through the postcode;
  3. without group AND postcode     — the bias mostly goes, at a cost in
                                      accuracy against the (biased) labels;
  4. with all columns but trained on FAIR labels (hire by ability alone) — the
     proxy is harmless when the labels are clean: the problem was the data.

Draws ethics-bias-proxy.svg.   Run:  python3 ethics-bias-demo.py
"""
from __future__ import annotations

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GREY = "#888"
rng = np.random.default_rng(20260914)


# ----------------------------------------------------------------------------
# 1. The world: ability, group, proxy, and two kinds of label
# ----------------------------------------------------------------------------
def make_world(n=20000):
    group = rng.integers(0, 2, n)                          # 0 = A, 1 = B
    ability = rng.normal(0, 1, n)                          # same distribution in both groups
    postcode = 0.85 * group + rng.normal(0, 0.6, n)        # proxy: correlated with group, not with ability
    score = ability + rng.normal(0, 0.5, n)                # a noisy test score the recruiter sees
    # historical hiring: ability counted, but group B was penalised by 1.2 units
    hist_logit = 1.6 * ability - 1.2 * group
    hired_hist = rng.random(n) < 1 / (1 + np.exp(-hist_logit))
    fair_logit = 1.6 * ability
    hired_fair = rng.random(n) < 1 / (1 + np.exp(-fair_logit))
    return group, ability, postcode, score, hired_hist.astype(float), hired_fair.astype(float)


# ----------------------------------------------------------------------------
# 2. Logistic regression from scratch (gradient descent)
# ----------------------------------------------------------------------------
def train(X, y, steps=3000, lr=0.5):
    X = np.c_[np.ones(len(X)), X]
    w = np.zeros(X.shape[1])
    for _ in range(steps):
        p = 1 / (1 + np.exp(-X @ w))
        w -= lr * X.T @ (p - y) / len(y)
    return w


def predict(X, w):
    return 1 / (1 + np.exp(-(np.c_[np.ones(len(X)), X] @ w)))


# ----------------------------------------------------------------------------
# 3. The audit: selection rate by group, at EQUAL ability
# ----------------------------------------------------------------------------
def audit(p, group, ability, thresh=0.5):
    """Hire if p > thresh. Compare groups within a narrow band of true ability."""
    band = np.abs(ability - 0.3) < 0.15                    # applicants of the same, above-average ability
    hire = p > thresh
    rate_a = hire[band & (group == 0)].mean()
    rate_b = hire[band & (group == 1)].mean()
    return rate_a, rate_b


def main():
    group, ability, postcode, score, y_hist, y_fair = make_world()
    corr = np.corrcoef(postcode, group)[0, 1]
    print(f"proxy check: corr(postcode, group) = {corr:.2f};  corr(postcode, ability) = {np.corrcoef(postcode, ability)[0,1]:.2f}")
    print(f"historical labels: hired {y_hist[group==0].mean():.0%} of group A, {y_hist[group==1].mean():.0%} of group B (same ability distribution)\n")

    experiments = [
        ("1  score + postcode + GROUP,   biased labels", np.c_[score, postcode, group], y_hist),
        ("2  score + postcode,           biased labels", np.c_[score, postcode], y_hist),
        ("3  score only,                 biased labels", np.c_[score], y_hist),
        ("4  score + postcode + group,   FAIR labels", np.c_[score, postcode, group], y_fair),
    ]
    print(f"{'model':<46} {'hire rate A':>11} {'hire rate B':>11} {'gap':>7}   (same true ability)")
    rows = []
    for name, X, y in experiments:
        w = train(X, y)
        p = predict(X, w)
        ra, rb = audit(p, group, ability)
        rows.append((name, ra, rb))
        print(f"{name:<46} {ra:>11.0%} {rb:>11.0%} {ra-rb:>+7.0%}")
    _, (n1, a1, b1), (n2, a2, b2), (n3, a3, b3), (n4, a4, b4) = [None] + rows
    assert a1 - b1 > 0.15, "model 1 should reproduce the historical bias"
    assert a2 - b2 > 0.10, "model 2 should still be biased through the proxy"
    assert abs(a3 - b3) < 0.06, "model 3 should be roughly fair"
    assert abs(a4 - b4) < 0.06, "model 4: clean labels make the proxy harmless"
    print("\nremoving the protected column removed", f"{(a1-b1)-(a2-b2):.0%} of the gap; the postcode carried the rest.")
    print("removing the proxy too closed it; so did keeping every column and fixing the LABELS.")
    print("the bias was in the historical decisions, and a model trained on them learns to repeat them.")

    # figure
    fig, ax = plt.subplots(figsize=(8.6, 4.2), dpi=100); fig.patch.set_alpha(0); ax.set_facecolor("none")
    labels = ["1  all columns,\nbiased labels", "2  group removed,\nbiased labels", "3  proxy removed too,\nbiased labels", "4  all columns,\nfair labels"]
    x = np.arange(4); wd = 0.36
    ax.bar(x - wd / 2, [r[1] * 100 for r in rows], wd, color="#2563eb", alpha=0.7, label="group A")
    ax.bar(x + wd / 2, [r[2] * 100 for r in rows], wd, color="#dc2626", alpha=0.7, label="group B")
    for i, r in enumerate(rows):
        ax.text(i, max(r[1], r[2]) * 100 + 2, f"gap {r[1]-r[2]:+.0%}", ha="center", color=GREY, fontsize=9)
    ax.set_xticks(x); ax.set_xticklabels(labels, color=GREY, fontsize=8.5)
    ax.set_ylabel("hire rate at equal ability (%)", color=GREY); ax.set_ylim(0, 100)
    ax.set_title("Deleting the protected column does not delete the bias: the postcode carries it", color=GREY, fontsize=10)
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY); ax.grid(True, axis="y", color=GREY, alpha=0.2)
    leg = ax.legend(frameon=False, fontsize=9)
    for t in leg.get_texts(): t.set_color(GREY)
    fig.tight_layout(); fig.savefig("ethics-bias-proxy.svg", format="svg", transparent=True)
    print("wrote ethics-bias-proxy.svg")


if __name__ == "__main__":
    main()
