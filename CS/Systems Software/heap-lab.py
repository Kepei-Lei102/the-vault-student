"""heap-lab.py — an allocator, a garbage collector, and Python's own heap, measured.

Run:  python3 heap-lab.py       (standard library only; writes heap-lab.json)

Part A builds a first-fit allocator over a bytearray arena, with headers and a
free list, and shows fragmentation: after allocating and freeing, the arena has
more free bytes than a request needs and still cannot satisfy it, until
neighbouring free blocks are coalesced.
Part B builds reference counting and a mark-and-sweep collector over a small
object graph and shows the case reference counting cannot handle: a cycle.
Part C watches Python's real heap with tracemalloc, sys.getrefcount and gc:
a leak through a global list, and a cycle that only the collector frees.
"""
import gc, json, os, sys, time, tracemalloc

HERE = os.path.dirname(os.path.abspath(__file__))
R = {}

# ───────────────────── Part A: a first-fit allocator ─────────────────────
class Arena:
    """A heap in miniature. Each block: 4-byte header (size, high bit = free) then payload."""
    HDR = 4
    def __init__(self, size):
        self.mem = bytearray(size); self.size = size
        self._write(0, size - self.HDR, free=True)            # one big free block
    def _write(self, off, n, free):
        v = n | (1 << 31 if free else 0); self.mem[off:off + 4] = v.to_bytes(4, "little")
    def _read(self, off):
        v = int.from_bytes(self.mem[off:off + 4], "little"); return v & 0x7FFFFFFF, bool(v >> 31)
    def blocks(self):
        off = 0
        while off < self.size:
            n, free = self._read(off); yield off, n, free; off += self.HDR + n
    def malloc(self, n):
        n = (n + 7) & ~7                                       # round up to 8 bytes, like real allocators
        for off, size, free in self.blocks():                  # first fit: walk the list, take the first that fits
            if free and size >= n:
                rest = size - n
                if rest > self.HDR + 8:                        # split: the remainder becomes a new free block
                    self._write(off, n, False); self._write(off + self.HDR + n, rest - self.HDR, True)
                else:
                    self._write(off, size, False)
                return off + self.HDR                          # the "pointer": an offset into the arena
        raise MemoryError("no free block of %d bytes" % n)
    def free(self, ptr):
        off = ptr - self.HDR; n, was_free = self._read(off)
        assert not was_free, "double free at %d" % ptr
        self._write(off, n, True)
    def coalesce(self):
        """Merge adjacent free blocks: the step that turns scattered gaps back into room."""
        merged = 0; off = 0
        while off < self.size:
            n, free = self._read(off); nxt = off + self.HDR + n
            if free and nxt < self.size:
                n2, free2 = self._read(nxt)
                if free2:
                    self._write(off, n + self.HDR + n2, True); merged += 1; continue
            off = nxt
        return merged
    def stats(self):
        free_bytes = sum(n for _, n, f in self.blocks() if f); largest = max((n for _, n, f in self.blocks() if f), default=0)
        return {"free_bytes": free_bytes, "largest_free": largest, "blocks": sum(1 for _ in self.blocks())}
    def picture(self, cols=64):
        """One character per (size/cols) bytes: # used, . free, | header."""
        out = []; per = self.size / cols
        for off, n, free in self.blocks():
            span = max(1, round((n + self.HDR) / per)); out.append(("." if free else "#") * span)
        return "".join(out)[:cols]

def part_a():
    arena = Arena(4096); ptrs = [arena.malloc(120) for _ in range(32)]    # 32 blocks of 124 incl. header = 3968 B; 124 B left
    pic_full = arena.picture()
    for p in ptrs[::2]: arena.free(p)                                        # free every other block
    s = arena.stats(); pic_frag = arena.picture()
    try:
        arena.malloc(400); big_ok = True
    except MemoryError:
        big_ok = False
    for p in ptrs[1::2]: arena.free(p)                                       # now free the rest: all gaps, still separate
    s2 = arena.stats(); pic_freed = arena.picture()
    try:
        arena.malloc(400); big_ok2 = True
    except MemoryError:
        big_ok2 = False
    merged = arena.coalesce(); s3 = arena.stats(); pic_merged = arena.picture()
    big_ok3 = arena.malloc(400) is not None
    R["allocator"] = {"after_alternate_free": s, "malloc_400_ok": big_ok, "after_all_free": s2, "malloc_400_ok_after_all_free": big_ok2,
                      "merged_blocks": merged, "after_coalesce": s3, "malloc_400_ok_after_coalesce": big_ok3,
                      "pictures": {"full": pic_full, "fragmented": pic_frag, "all_freed_uncoalesced": pic_freed, "coalesced": pic_merged}}
    print("A. allocator (4096-byte arena, 32 blocks of 120 bytes, then free every other one):")
    print("   full        ", pic_full); print("   fragmented  ", pic_frag)
    print("   free %d bytes, largest free block %d: malloc(400) %s" % (s["free_bytes"], s["largest_free"], "succeeds" if big_ok else "FAILS"))
    print("   free the rest, without coalescing: free %d bytes, largest %d: malloc(400) %s" % (s2["free_bytes"], s2["largest_free"], "succeeds" if big_ok2 else "FAILS"))
    print("   coalesce: %d merges -> largest free block %d: malloc(400) %s" % (merged, s3["largest_free"], "succeeds" if big_ok3 else "FAILS"))
    print("   coalesced   ", pic_merged, "\n")

# ───────────────────── Part B: reference counting versus mark-and-sweep ─────────────────────
class Obj:
    def __init__(self, name): self.name, self.refs, self.rc, self.marked = name, [], 0, False
    def __repr__(self): return self.name

def link(a, b): a.refs.append(b); b.rc += 1
def unlink(a, b): a.refs.remove(b); b.rc -= 1

def refcount_free(obj, freed):
    """When a count hits zero, free the object and decrement everything it pointed to."""
    if obj.rc == 0 and obj not in freed:
        freed.append(obj)
        for child in obj.refs: child.rc -= 1; refcount_free(child, freed)

def mark_sweep(roots, heap):
    for o in heap: o.marked = False
    stack = list(roots); order = []
    while stack:                                          # mark: everything reachable from a root
        o = stack.pop()
        if not o.marked:
            o.marked = True; order.append(o.name); stack.extend(o.refs)
    swept = [o for o in heap if not o.marked]            # sweep: everything else is garbage
    return order, swept

def part_b():
    heap = [Obj(n) for n in "ABCDEF"]; A, B, C, D, E, F = heap
    root = Obj("root"); link(root, A); link(A, B); link(B, C); link(A, D); link(D, E); link(E, D); link(root, F)
    # drop the two references the program holds: A→D (so the D↔E cycle is orphaned) and root→F
    unlink(A, D); freed = []; refcount_free(D, freed)
    unlink(root, F); refcount_free(F, freed)
    rc_view = {o.name: o.rc for o in heap}
    order, swept = mark_sweep([root], heap)
    R["gc"] = {"refcounts_after_unlink": rc_view, "freed_by_refcount": [o.name for o in freed], "mark_order": order, "swept_by_mark_sweep": [o.name for o in swept]}
    print("B. object graph root->A->B->C, A->D<->E, root->F; then drop A->D and root->F:")
    print("   reference counts now:", rc_view, "-> refcount frees", [o.name for o in freed], "(D and E hold each other at 1)")
    print("   mark from root reaches", order, "-> sweep frees", [o.name for o in swept], "\n")

# ───────────────────── Part C: Python's real heap ─────────────────────
def part_c():
    x = [1, 2, 3]; y = x
    rc = sys.getrefcount(x)                                 # the argument itself adds one
    print("C. Python: sys.getrefcount([1,2,3] bound to x and y) =", rc, "(x, y, and the call's own argument)")
    tracemalloc.start(); keep = []
    s0 = tracemalloc.take_snapshot()
    for i in range(20000): keep.append("row %d" % i)        # a "cache" that is never trimmed: the classic Python leak
    s1 = tracemalloc.take_snapshot(); grew = sum(st.size_diff for st in s1.compare_to(s0, "lineno"))
    print("   20 000 strings appended to a global list and never removed: +%.1f MB still reachable" % (grew / 1e6))
    gc.disable(); gc.collect()
    class Node: pass
    def make_cycle():
        a, b = Node(), Node(); a.other, b.other = b, a       # a<->b: each keeps the other's count at 1
    before = len(gc.get_objects())
    for _ in range(10000): make_cycle()
    after_no_gc = len(gc.get_objects()) - before
    collected = gc.collect(); gc.enable()
    after_gc = max(0, len(gc.get_objects()) - before)
    print("   10 000 two-object cycles created and dropped with the collector off: %d objects still alive" % after_no_gc)
    print("   gc.collect() reports %d unreachable objects freed; alive afterwards: %d" % (collected, after_gc))
    t0 = time.perf_counter()
    for _ in range(300000): _ = [0] * 8
    per = (time.perf_counter() - t0) / 300000 * 1e9
    print("   allocating and dropping an 8-element list: %.0f ns each (a malloc, a refcount to zero, a free)\n" % per)
    R["python"] = {"refcount_x_y": rc, "leak_mb": round(grew / 1e6, 2), "cycle_objects_alive_without_gc": after_no_gc, "gc_collected": collected, "alive_after_gc": after_gc, "list_alloc_ns": round(per)}
    tracemalloc.stop()

if __name__ == "__main__":
    part_a(); part_b(); part_c()
    json.dump(R, open(os.path.join(HERE, "heap-lab.json"), "w"), indent=1); print("saved heap-lab.json")
