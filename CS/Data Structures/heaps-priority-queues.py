"""An inspectable min-heap, a discrete-event queue, and executable checks.
Python 3.10+; standard library only. Run this file directly for all checks.
Keys must form a consistent total order; NaN and incomparable mixed types are excluded.
"""
from itertools import count, permutations
import heapq
import random


class MinHeap:
    def __init__(self, values=()):
        self.a = list(values)  # own the array; do not mutate the caller's list
        self.comparisons = 0
        for i in range(len(self.a) // 2 - 1, -1, -1):
            self._down(i)

    def __len__(self):
        return len(self.a)

    def _less(self, i, j):
        self.comparisons += 1
        return self.a[i] < self.a[j]

    def peek(self):
        if not self.a:
            raise IndexError('peek from empty heap')
        return self.a[0]

    def push(self, value):
        self.a.append(value)
        i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if not self._less(i, p):
                break
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p

    def _down(self, i):
        n = len(self.a)
        while 2 * i + 1 < n:
            child = 2 * i + 1
            if child + 1 < n and self._less(child + 1, child):
                child += 1
            if not self._less(child, i):
                break
            self.a[i], self.a[child] = self.a[child], self.a[i]
            i = child

    def pop(self):
        if not self.a:
            raise IndexError('pop from empty heap')
        answer = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            self._down(0)
        return answer

    def valid(self):
        return all(not self.a[i] < self.a[(i - 1) // 2]
                   for i in range(1, len(self.a)))


class EventQueue:
    """Unique event IDs; replacement invalidates the old version lazily.
    A new schedule gets a new tie ticket, including when rescheduling.
    Times are nonnegative integer simulation ticks; callbacks may schedule
    further events at the current time or later. No wall-clock sleeping.
    """
    def __init__(self):
        self.now = 0
        self.heap = []
        self.serial = count()
        self.live = {}

    def schedule(self, when, event_id, payload):
        if type(when) is not int or when < self.now:
            raise ValueError('time must be an integer at or after now')
        ticket = next(self.serial)
        self.live[event_id] = ticket
        heapq.heappush(self.heap, (when, ticket, event_id, payload))

    def cancel(self, event_id):
        return self.live.pop(event_id, None) is not None

    def pop(self):
        while self.heap:
            when, ticket, event_id, payload = heapq.heappop(self.heap)
            if self.live.get(event_id) != ticket:
                continue
            del self.live[event_id]
            self.now = when
            return when, event_id, payload
        raise IndexError('no live events')

    def compact(self):
        self.heap = [e for e in self.heap if self.live.get(e[2]) == e[1]]
        heapq.heapify(self.heap)


def demo():
    q = EventQueue()
    q.schedule(5, 'shield', 'shield expires')
    q.schedule(2, 'arrow', 'arrow hits')
    q.schedule(5, 'spawn', 'enemy spawns')
    q.schedule(1, 'arrow', 'arrow hits after speed boost')
    out = []
    while q.live:
        when, name, payload = q.pop()
        out.append((when, payload))
        if name == 'arrow':
            q.schedule(when + 1, 'spark', 'impact spark fades')
    return out


def verify():
    # Independent sorted-list/heapq oracles, including duplicate and negative keys.
    cases = [[], [0], [2, 2, 2], [-4, 0, -2, -4]]
    cases += [list(p) for n in range(8) for p in permutations(range(n))]
    for values in cases:
        h = MinHeap(values)
        assert h.valid()
        result = []
        while h:
            result.append(h.pop())
            assert h.valid()
        assert result == sorted(values)
    for seed in range(20):
        rng = random.Random(seed)
        h, oracle = MinHeap(), []
        for _ in range(2000):
            if not oracle or rng.random() < .6:
                x = rng.randrange(-100, 101)
                h.push(x)
                heapq.heappush(oracle, x)
            else:
                assert h.pop() == heapq.heappop(oracle)
            assert h.valid() and len(h) == len(oracle)
            if oracle:
                assert h.peek() == oracle[0]
    for method in ('peek', 'pop'):
        try:
            getattr(MinHeap(), method)()
        except IndexError:
            pass
        else:
            raise AssertionError('empty heap accepted')
    q = EventQueue()
    q.schedule(0, 'a', {})
    q.schedule(0, 'b', {})  # dictionaries never compared
    q.schedule(0, 'a', {'replacement': True})
    assert q.pop()[1] == 'b'
    assert q.pop()[1] == 'a'
    q.schedule(5, 'cancel', {})
    assert q.cancel('cancel') and not q.cancel('cancel')
    q.compact()
    assert q.heap == []
    q.schedule(10, 'later', {})
    q.pop()
    for bad in (9, 1.5, float('nan'), True):
        try:
            q.schedule(bad, 'bad', {})
        except ValueError:
            pass
        else:
            raise AssertionError('invalid time accepted')
    # Scheduler differential test against a separately sorted active-event map.
    for seed in range(10):
        rng = random.Random(seed)
        q, reference, ticket = EventQueue(), {}, 0
        for step in range(500):
            key = rng.randrange(12)
            action = rng.randrange(4)
            if action < 2:
                t = q.now + rng.randrange(20)
                q.schedule(t, key, step)
                reference[key] = (t, ticket, key, step)
                ticket += 1
            elif action == 2:
                q.cancel(key)
                reference.pop(key, None)
            elif reference:
                e = min(reference.values())
                assert q.pop() == (e[0], e[2], e[3])
                del reference[e[2]]
            if step % 37 == 0:
                q.compact()
        while reference:
            e = min(reference.values())
            assert q.pop() == (e[0], e[2], e[3])
            del reference[e[2]]
        try:
            q.pop()
        except IndexError:
            pass
        else:
            raise AssertionError('empty event queue accepted')
    assert demo() == [(1, 'arrow hits after speed boost'), (2, 'impact spark fades'),
                      (5, 'shield expires'), (5, 'enemy spawns')]
    print(f'PASS: {len(cases)} build/drain cases; 40,000 mixed heap operations; 5,000 scheduler operations.')
    print('Descending input: n / bottom-up comparisons / repeated-insert comparisons')
    for n in (31, 127, 511, 2047):
        values = list(range(n, 0, -1))
        bottom, insert = MinHeap(values), MinHeap()
        for x in values:
            insert.push(x)
        assert bottom.comparisons < 2 * n
        print(n, bottom.comparisons, insert.comparisons)
    print('Game event trace:', demo())


if __name__ == '__main__':
    verify()
