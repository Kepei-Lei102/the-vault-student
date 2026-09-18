"""Runnable companion: You're the Architect, the AI is the Bricklayer.

No dependencies. Run with Python 3 (without -O, which disables assertions).
The two deliberately faulty implementations must be rejected.
"""


def split_bad(total_pence, people):
    return [round(total_pence / people)] * people


def split_pence(total_pence, people):
    if type(total_pence) is not int or type(people) is not int:
        raise TypeError("Use integer pennies and an integer people count")
    if total_pence < 0 or people <= 0:
        raise ValueError("Total must be non-negative; people must be positive")
    quotient, remainder = divmod(total_pence, people)
    return [quotient + (1 if i < remainder else 0)
            for i in range(people)]


def split_wrong_end(total_pence, people):
    return list(reversed(split_pence(total_pence, people)))


def check_contract(split):
    # Expectations derived independently from the stated policy.
    for args, expected in [((1000, 3), [334, 333, 333]),
                           ((2, 3), [1, 1, 0]),
                           ((0, 3), [0, 0, 0]),
                           ((1000, 1), [1000])]:
        assert split(*args) == expected, f"agreed example {args}"
    for total in range(101):
        for people in range(1, 11):
            shares = split(total, people)
            assert len(shares) == people
            assert all(type(s) is int and s >= 0 for s in shares)
            assert sum(shares) == total, "conservation"
            assert max(shares) - min(shares) <= 1, "fairness"
            assert shares == sorted(shares, reverse=True), "order"
    for args, exception in [((-1, 3), ValueError), ((10, 0), ValueError),
                            ((10, -1), ValueError), ((10.0, 3), TypeError),
                            ((10, 2.5), TypeError), ((True, 3), TypeError),
                            ((10, False), TypeError), (("10", 3), TypeError)]:
        try:
            split(*args)
        except exception:
            pass
        else:
            raise AssertionError(f"did not reject {args} with {exception.__name__}")


def main():
    if not __debug__:
        raise RuntimeError("Run without -O so the checks execute")
    check_contract(split_pence)
    print("PASS: four hand examples, 1,010 contract cases, eight invalid inputs")
    for faulty in (split_bad, split_wrong_end):
        try:
            check_contract(faulty)
        except AssertionError as failure:
            print(f"REJECTED {faulty.__name__}: {failure}")
        else:
            raise AssertionError(f"Tests accepted deliberate fault {faulty.__name__}")
    for args in ((1000, 3), (2, 3)):
        result = split_bad(*args)
        print(f"Rounding fault {args}: {result}, sum={sum(result)}")
    wrong_order = split_wrong_end(1000, 3)
    assert sum(wrong_order) == 1000
    assert max(wrong_order) - min(wrong_order) <= 1
    assert wrong_order != sorted(wrong_order, reverse=True)
    print("Wrong-end fault conserves money and passes fairness, but fails order")


if __name__ == "__main__":
    main()
