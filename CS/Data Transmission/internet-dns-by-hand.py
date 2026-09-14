"""A DNS lookup with no library: build the 12-byte header and the question by hand, send
it over UDP to a public resolver, and read the IP address out of the answer bytes.

This is what happens in the first few milliseconds after you type a URL: the browser asks
a resolver "what is the IPv4 address of this name?", and the reply is a small binary record.

Run:  python3 internet-dns-by-hand.py [name]      (default: example.com)
"""
import socket, struct, sys, time

def build_query(name, qid=0x1234):
    header = struct.pack("!HHHHHH", qid, 0x0100, 1, 0, 0, 0)   # id, flags (recursion desired), 1 question
    qname = b"".join(bytes([len(p)]) + p.encode() for p in name.split(".")) + b"\x00"
    return header + qname + struct.pack("!HH", 1, 1)               # type A, class IN

def skip_name(data, i):
    while True:
        n = data[i]
        if n == 0: return i + 1
        if n & 0xC0 == 0xC0: return i + 2                         # compression pointer
        i += 1 + n

def parse(data):
    qid, flags, qd, an, ns, ar = struct.unpack("!HHHHHH", data[:12])
    i = 12
    for _ in range(qd): i = skip_name(data, i) + 4
    answers = []
    for _ in range(an):
        i = skip_name(data, i)
        rtype, rclass, ttl, rdlen = struct.unpack("!HHIH", data[i:i+10]); i += 10
        rdata = data[i:i+rdlen]; i += rdlen
        if rtype == 1: answers.append(("A", ".".join(map(str, rdata)), ttl))
        elif rtype == 5: answers.append(("CNAME", "(alias)", ttl))
    return flags, answers

name = sys.argv[1] if len(sys.argv) > 1 else "example.com"
resolver = ("223.5.5.5", 53)       # AliDNS, a public resolver reachable from Chengdu; 8.8.8.8 is Google's
q = build_query(name)
print(f"question: {name}  ({len(q)} bytes on the wire)  ->  resolver {resolver[0]}:53 over UDP")
print("bytes:   ", q.hex(" "))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.settimeout(3)
for attempt, res in enumerate([resolver, ("8.8.8.8", 53), ("114.114.114.114", 53)]):   # UDP has no delivery guarantee: if one resolver stays silent, ask another
    try:
        t0 = time.perf_counter(); s.sendto(q, res); data, _ = s.recvfrom(512); dt = (time.perf_counter() - t0) * 1000
        resolver = res; break
    except socket.timeout:
        print(f"  no reply from {res[0]} within 3 s (UDP packets can be lost — that is why there is a retry)")
flags, answers = parse(data)
print(f"answer:   {len(data)} bytes back in {dt:.1f} ms; flags {flags:#06x} (bit 15 set = this is a response)")
for rtype, addr, ttl in answers:
    print(f"  {rtype:5s} {addr:16s} TTL {ttl} s  (cache it for that long, then ask again)")
