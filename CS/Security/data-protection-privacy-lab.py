"""Data Protection and Privacy — five experiments you can run.

"We removed the names" is the most common privacy claim in the world, and it is usually
false.  Each experiment below takes one such claim and measures it.

1. uniqueness()      — how many people in a city are the ONLY person with their
                       (district, date of birth, sex)?  The quasi-identifier problem.
2. linkage_attack()  — a hospital publishes records with names removed; a public list
                       (a club roster, an electoral roll) has names and the same three
                       fields.  Join them.  Count the named diagnoses.
3. k_anonymity()     — generalise the quasi-identifiers (birth date -> year -> decade,
                       district -> region) until every record hides in a group of at
                       least k, and measure what the generalisation costs.
4. hashed_phones()   — "pseudonymised" phone numbers: SHA-256 of an 11-digit mobile
                       number, reversed by trying every number.
5. differencing()    — the averaging attack on a query interface, and the Laplace
                       mechanism (differential privacy) that defeats it, with the
                       accuracy price at each epsilon.

Run:  python3 data-protection-privacy-lab.py          (standard library + numpy, about 2 s)
All people are synthetic.
"""
import hashlib
import time
from collections import Counter

import numpy as np

rng = np.random.default_rng(2026)

# --------------------------------------------------------------------------------------
# A synthetic city
# --------------------------------------------------------------------------------------
N = 200_000
DISTRICTS = 40                      # postcode-like areas of unequal size
CONDITIONS = ["asthma", "diabetes", "depression", "hypertension", "HIV", "none", "none", "none"]


def make_city(n=N):
    weights = rng.dirichlet(np.ones(DISTRICTS) * 3)
    district = rng.choice(DISTRICTS, size=n, p=weights)
    age_days = rng.integers(0, 90 * 365, size=n)          # a birth date, as days before today
    sex = rng.integers(0, 2, size=n)
    condition = rng.choice(len(CONDITIONS), size=n)
    return district, age_days, sex, condition


def uniqueness(city):
    district, age_days, sex, _ = city
    year = age_days // 365
    combos = {
        "sex only":                               list(zip(sex)),
        "district":                               list(zip(district)),
        "district + sex":                         list(zip(district, sex)),
        "year of birth + sex":                    list(zip(year, sex)),
        "district + year of birth + sex":         list(zip(district, year, sex)),
        "date of birth + sex":                    list(zip(age_days, sex)),
        "district + date of birth":               list(zip(district, age_days)),
        "district + date of birth + sex":         list(zip(district, age_days, sex)),
    }
    out = {}
    for name, keys in combos.items():
        counts = Counter(keys)
        unique = sum(1 for k in keys if counts[k] == 1)
        out[name] = unique / len(keys)
        print(f"  {name:36s} {100*unique/len(keys):6.2f} % of people are unique")
    return out


def linkage_attack(city, sample=5000):
    district, age_days, sex, condition = city
    # the hospital's "anonymised" release: no names, but district, birth date, sex, diagnosis
    patients = rng.choice(N, size=20_000, replace=False)
    released = {}
    for i in patients:
        released.setdefault((district[i], age_days[i], sex[i]), []).append(CONDITIONS[condition[i]])
    # a public list with names: say, a marathon's published results
    public = rng.choice(N, size=sample, replace=False)
    named = wrong = 0
    in_hospital = set(patients.tolist())
    for i in public:
        key = (district[i], age_days[i], sex[i])
        if key in released and len(released[key]) == 1:
            if i in in_hospital:
                named += 1                  # a name now sits beside a diagnosis
            else:
                wrong += 1                  # a confident match to the wrong person
    on_list = sum(1 for i in public if i in in_hospital)
    print(f"  public list of {sample} named people; {on_list} of them are among the 20 000 patients")
    print(f"  re-identified with their diagnosis: {named}   ({100*named/on_list:.0f} % of the patients on the list)")
    print(f"  matched to a stranger's record:     {wrong}   (a false accusation is a harm too)")
    return named, wrong


def k_anonymity(city):
    district, age_days, sex, _ = city
    levels = [
        ("exact date, district",          district,        age_days,             sex),
        ("birth year, district",          district,        age_days // 365,      sex),
        ("birth year, region (8)",        district // 5,   age_days // 365,      sex),
        ("birth decade, region (8)",      district // 5,   age_days // 3650,     sex),
        ("birth decade, whole city",      district * 0,    age_days // 3650,     sex),
    ]
    for name, d, a, s in levels:
        counts = Counter(zip(d.tolist(), a.tolist(), s.tolist()))
        k = min(counts.values())
        at_risk = sum(c for c in counts.values() if c < 5) / N
        print(f"  {name:28s} smallest group k = {k:5d};  {100*at_risk:6.2f} % of people sit in a group of fewer than 5")


def hashed_phones():
    secret = "13881234567"                                   # a Chengdu-style mobile number (synthetic)
    token = hashlib.sha256(secret.encode()).hexdigest()
    # the attacker knows the carrier prefix and the city's number block: 1388 123 xxxx
    t0 = time.perf_counter()
    found = None
    for tail in range(10_000):
        guess = f"1388123{tail:04d}"
        if hashlib.sha256(guess.encode()).hexdigest() == token:
            found = guess
            break
    dt = time.perf_counter() - t0
    # speed test for the whole space
    t0 = time.perf_counter()
    for tail in range(200_000):
        hashlib.sha256(f"138{tail:08d}".encode()).hexdigest()
    rate = 200_000 / (time.perf_counter() - t0)
    print(f"  token {token[:16]}…  reversed to {found} in {dt*1000:.1f} ms (block known: 10 000 guesses)")
    print(f"  this laptop, one core, plain Python: {rate/1e6:.2f} million hashes a second")
    print(f"  every mobile number in China (~4.5e10 possible): {4.5e10/rate/3600:.1f} hours here; minutes on one GPU")
    print("  a salted hash with a SECRET salt, or a random token with a lookup table kept elsewhere, is not reversible this way")


def keyed_tokens():
    """The repair for experiment 4: a keyed hash (HMAC).  Without the key the attacker
    cannot even begin to guess; with the key destroyed, the tokens are orphans."""
    import hmac, secrets
    key = secrets.token_bytes(32)                             # kept by the controller, never released
    phones = ["13881234567", "13881234568", "13881234567"]
    tokens = [hmac.new(key, p.encode(), hashlib.sha256).hexdigest()[:16] for p in phones]
    print(f"  same number -> same token (records still link): {tokens[0] == tokens[2]}")
    print(f"  neighbouring numbers -> unrelated tokens:        {tokens[0]}  {tokens[1]}")
    guess = hashlib.sha256(b"13881234567").hexdigest()[:16]
    print(f"  attacker's plain SHA-256 of the right number:    {guess}  (matches: {guess == tokens[0]})")
    print("  this is pseudonymisation: whoever holds the key can still re-identify, so the law still treats it as personal data")


def differencing(city, epsilons=(0.1, 0.5, 1.0, 5.0), trials=2000):
    salaries = rng.lognormal(mean=9.2, sigma=0.5, size=5000).round(-2)   # one company, 5000 staff
    cap = 60_000.0                                                        # salaries clipped to [0, cap]
    salaries = np.minimum(salaries, cap)
    alice = 7
    total_all = salaries.sum()
    total_without = np.delete(salaries, alice).sum()
    print(f"  exact query 'total payroll' = {total_all:,.0f};  'total excluding employee #7' = {total_without:,.0f}")
    print(f"  difference = {total_all - total_without:,.0f}  = Alice's salary, exactly.  No record was ever 'accessed'.")
    for eps in epsilons:
        scale = cap / eps                                                 # sensitivity / epsilon
        noisy_a = total_all + rng.laplace(0, scale, trials)
        noisy_b = total_without + rng.laplace(0, scale, trials)
        guess = noisy_a - noisy_b
        err_attack = np.abs(guess - salaries[alice]).mean()
        err_query = np.abs(noisy_a - total_all).mean() / total_all
        print(f"  epsilon = {eps:4.1f}: attacker's error on Alice ±{err_attack:9,.0f}  |  honest analyst's error on the payroll {100*err_query:5.2f} %")
    print(f"  (Alice's true salary: {salaries[alice]:,.0f}.  Smaller epsilon = more privacy, less accuracy: a dial, not a switch.)")


if __name__ == "__main__":
    city = make_city()
    print(f"1. uniqueness in a synthetic city of {N:,}")
    uniqueness(city)
    print("\n2. the linkage attack")
    linkage_attack(city)
    print("\n3. k-anonymity by generalisation")
    k_anonymity(city)
    print("\n4. hashed phone numbers")
    hashed_phones()
    print("\n4b. the repair: keyed tokens")
    keyed_tokens()
    print("\n5. differencing, and differential privacy")
    differencing(city)
