"""tech-stack-lab.py — a whole web stack in one file, then measured.

Standard library only. Run:  python3 tech-stack-lab.py
It starts a real HTTP server on a random local port with three layers —
a page (frontend), a JSON API (application), a SQLite table behind a cache
(data) — then acts as the clients: it restarts the server to show what a
script forgets and a system keeps, times each layer, loads it with 1, 4 and
16 concurrent clients, writes from 16 threads at once, and sends a broken
request to see that a system answers instead of crashing.
Results go to tech-stack-lab.json for tech-stack-figures.py.
"""
import json, os, sqlite3, statistics, threading, time, urllib.request, urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tech-stack-lab.sqlite")

# ───────────────────────── data layer ─────────────────────────
class Store:
    """The database: the only layer whose memory survives a restart."""
    def __init__(self, path):
        self.path = path
        with self._conn() as c:
            c.execute("PRAGMA journal_mode=WAL")
            c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT NOT NULL, score INTEGER NOT NULL, ts REAL NOT NULL)")
    def _conn(self):
        return sqlite3.connect(self.path, timeout=5)      # timeout: wait for the lock, don't fail
    def add(self, name, score):
        with self._conn() as c:
            c.execute("INSERT INTO scores (name, score, ts) VALUES (?, ?, ?)", (name, score, time.time()))
    def top(self, n=10):
        with self._conn() as c:
            return [dict(name=r[0], score=r[1]) for r in c.execute("SELECT name, score FROM scores ORDER BY score DESC, id LIMIT ?", (n,))]
    def count(self):
        with self._conn() as c:
            return c.execute("SELECT COUNT(*) FROM scores").fetchone()[0]

class Cache:
    """A dictionary with an expiry: the layer that makes reads cheap and stale."""
    def __init__(self, ttl):
        self.ttl, self.data, self.lock = ttl, {}, threading.Lock()
    def get(self, key, compute):
        with self.lock:
            hit = self.data.get(key)
            if hit and hit[0] > time.time():
                return hit[1], True
        value = compute()
        with self.lock:
            self.data[key] = (time.time() + self.ttl, value)
        return value, False
    def clear(self):
        with self.lock:
            self.data.clear()

# ───────────────────────── presentation layer ─────────────────────────
PAGE = """<!doctype html><meta charset=utf-8><title>Scores</title>
<h1>Top scores</h1><ol id=list></ol>
<form id=f><input name=name placeholder=name required> <input name=score type=number required> <button>Add</button></form>
<script>
async function load(){ const r = await fetch('/api/top'); const rows = await r.json();
  list.innerHTML = rows.map(x => `<li>${x.name}: ${x.score}</li>`).join(''); }
f.onsubmit = async e => { e.preventDefault(); const d = Object.fromEntries(new FormData(f));
  await fetch('/api/scores', {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify(d)}); load(); };
load();
</script>"""

# ───────────────────────── application layer ─────────────────────────
def make_handler(store, cache, state):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"                       # keep-alive: one TCP connection, many requests
        def log_message(self, fmt, *args):                  # the access log, kept in memory for the report
            state["log"].append("%s %s" % (self.command, self.path))
        def send(self, code, body, ctype="application/json"):
            data = body.encode() if isinstance(body, str) else json.dumps(body).encode()
            self.send_response(code); self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
        def do_GET(self):
            state["served"] += 1                             # a counter in the process: a script's memory
            if self.path == "/":
                return self.send(200, PAGE, "text/html; charset=utf-8")
            if self.path == "/api/health":
                return self.send(200, {"ok": True, "served": state["served"]})
            if self.path == "/api/top":
                rows, hit = cache.get("top", store.top)
                return self.send(200, {"rows": rows, "cache": "hit" if hit else "miss"})
            if self.path == "/api/top/nocache":
                return self.send(200, {"rows": store.top(), "cache": "bypassed"})
            self.send(404, {"error": "no such route"})
        def do_POST(self):
            state["served"] += 1
            if self.path != "/api/scores":
                return self.send(404, {"error": "no such route"})
            try:
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
                name, score = str(body["name"])[:40], int(body["score"])
            except (ValueError, KeyError, TypeError) as e:   # validation: the boundary where the outside world is untrusted
                return self.send(400, {"error": "bad request: %s" % e.__class__.__name__})
            store.add(name, score); cache.clear()
            self.send(201, {"ok": True})
    return Handler

class StackServer(ThreadingHTTPServer):
    request_queue_size = 256      # the listen backlog: the default of 5 drops connections under load (see the card)
    daemon_threads = True

class Server:
    """One process listening on one port. Stop it and everything in `state` is gone."""
    def __init__(self, store):
        self.state = {"served": 0, "log": []}
        self.httpd = StackServer(("127.0.0.1", 0), make_handler(store, Cache(ttl=2.0), self.state))
        self.port = self.httpd.server_address[1]
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
    def stop(self):
        self.httpd.shutdown(); self.httpd.server_close()

# ───────────────────────── clients ─────────────────────────
def get(port, path):
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d%s" % (port, path), timeout=5) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())

def post(port, path, obj, raw=None):
    data = raw if raw is not None else json.dumps(obj).encode()
    req = urllib.request.Request("http://127.0.0.1:%d%s" % (port, path), data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())

def timed(fn, n):
    ts = []
    for _ in range(n):
        t = time.perf_counter(); fn(); ts.append((time.perf_counter() - t) * 1000)
    ts.sort()
    return {"p50_ms": round(statistics.median(ts), 3), "p99_ms": round(ts[int(0.99 * (n - 1))], 3), "n": n}

def load(port, threads, per_thread, path="/api/top"):
    errors = [0]; kinds = {}
    def worker():
        for _ in range(per_thread):
            try: get(port, path)
            except Exception as e:
                errors[0] += 1; kinds[e.__class__.__name__] = kinds.get(e.__class__.__name__, 0) + 1
    ths = [threading.Thread(target=worker) for _ in range(threads)]
    t = time.perf_counter()
    for th in ths: th.start()
    for th in ths: th.join()
    dt = time.perf_counter() - t
    return {"threads": threads, "requests": threads * per_thread, "seconds": round(dt, 3), "req_per_s": round(threads * per_thread / dt), "errors": errors[0], "error_kinds": kinds}

# ───────────────────────── the experiments ─────────────────────────
def main():
    for f in (DB, DB + "-wal", DB + "-shm"):
        if os.path.exists(f): os.remove(f)
    store = Store(DB); results = {}
    srv = Server(store); p = srv.port
    print("server up on port %d — open http://127.0.0.1:%d/ in a browser while this runs" % (p, p))

    # 1. script vs system: what a restart forgets
    for name, score in [("ada", 90), ("alan", 85), ("grace", 95)]:
        post(p, "/api/scores", {"name": name, "score": score})
    for _ in range(5): get(p, "/api/top")
    before = get(p, "/api/health")[1]["served"]
    srv.stop(); srv = Server(store); p = srv.port           # the process dies; the port changes; the database stays
    after = get(p, "/api/health")[1]["served"]
    rows = get(p, "/api/top")[1]["rows"]
    results["restart"] = {"served_before": before, "served_after_restart": after, "db_rows_after_restart": store.count(), "top": rows}
    print("\n1. restart: the process counter went %d → %d; the database still holds %d rows, top = %s" % (before, after, store.count(), [r["name"] for r in rows]))

    # 2. the cost of each layer
    results["latency"] = {
        "health (no database)": timed(lambda: get(p, "/api/health"), 300),
        "top, database every time": timed(lambda: get(p, "/api/top/nocache"), 300),
        "top, through the cache": timed(lambda: get(p, "/api/top"), 300),
    }
    print("\n2. latency per layer (ms):")
    for k, v in results["latency"].items(): print("   %-28s p50 %6.3f  p99 %6.3f" % (k, v["p50_ms"], v["p99_ms"]))

    # 3. concurrency: reads
    results["load"] = [load(p, t, 200) for t in (1, 4, 16)]
    print("\n3. concurrent readers:")
    for r in results["load"]: print("   %2d clients: %4d req in %.2fs = %5d req/s, errors %d %s" % (r["threads"], r["requests"], r["seconds"], r["req_per_s"], r["errors"], r["error_kinds"] or ""))

    # 4. concurrency: writes from 16 threads at once, every one must land
    n0 = store.count(); errs = [0]
    def writer(i):
        for j in range(50):
            try:
                code, _ = post(p, "/api/scores", {"name": "t%d" % i, "score": j})
                if code != 201: errs[0] += 1
            except Exception:
                errs[0] += 1
    ths = [threading.Thread(target=writer, args=(i,)) for i in range(16)]
    t = time.perf_counter()
    for th in ths: th.start()
    for th in ths: th.join()
    dt = time.perf_counter() - t
    results["writes"] = {"attempted": 800, "landed": store.count() - n0, "errors": errs[0], "seconds": round(dt, 3)}
    print("\n4. 16 writers × 50 POSTs: %d attempted, %d landed, %d errors, %.2fs" % (800, store.count() - n0, errs[0], dt))

    # 5. a bad request is a response, not a crash
    bad = [post(p, "/api/scores", None, raw=b"this is not json")[0],
           post(p, "/api/scores", {"name": "x"})[0],
           post(p, "/api/scores", {"name": "x", "score": "lots"})[0],
           get(p, "/api/nothing")[0]]
    alive = get(p, "/api/health")[0]
    results["bad_requests"] = {"status_codes": bad, "server_alive_after": alive == 200}
    print("\n5. bad requests answered with %s; server still alive: %s" % (bad, alive == 200))
    results["log_sample"] = srv.state["log"][:6]
    print("\n   access log (first lines): %s" % results["log_sample"])

    srv.stop()
    for f in (DB, DB + "-wal", DB + "-shm"):
        if os.path.exists(f): os.remove(f)
    with open(os.path.join(os.path.dirname(DB), "tech-stack-lab.json"), "w") as f:
        json.dump(results, f, indent=1)
    print("\nsaved tech-stack-lab.json")

if __name__ == "__main__":
    main()
