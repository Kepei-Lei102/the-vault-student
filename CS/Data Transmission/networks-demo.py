"""The network, actually touched. Four short experiments, all on your own machine.
(1) A TCP conversation on the loopback interface: a server and a client in one process, so you can see the
    connect / send / receive / close sequence that every web page rides on.
(2) The same with UDP: no connection, no guarantee, one datagram — the games-and-video protocol.
(3) An HTTP request by hand: what a browser actually sends, and the headers that come back.
(4) The four layers, made visible: the sizes a message grows to as each layer wraps it.
Run: python3 networks-demo.py"""
import socket, threading, time

print("== (1) TCP on the loopback: reliable, ordered, connection first ==")
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM); srv.bind(("127.0.0.1", 0)); srv.listen(1); port = srv.getsockname()[1]
def serve():
    conn, addr = srv.accept()
    data = conn.recv(1024); print(f"  server: got {data!r} from {addr}"); conn.sendall(b"ACK: " + data.upper()); conn.close()
t = threading.Thread(target=serve); t.start()
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM); cli.connect(("127.0.0.1", port))    # the three-way handshake happens here
cli.sendall(b"hello, network"); reply = cli.recv(1024); print(f"  client: reply {reply!r}"); cli.close(); t.join(); srv.close()

print("\n== (2) UDP: fire and forget ==")
usrv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); usrv.bind(("127.0.0.1", 0)); uport = usrv.getsockname()[1]
ucli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); ucli.sendto(b"frame 1", ("127.0.0.1", uport)); ucli.sendto(b"frame 2", ("127.0.0.1", uport))
for _ in range(2):
    d, a = usrv.recvfrom(1024); print(f"  datagram {d!r} — no connection was made, no acknowledgement will be sent")
usrv.close(); ucli.close()

print("\n== (3) HTTP by hand ==")
s = socket.create_connection(("example.com", 80), timeout=8)
req = b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"; print("  sent:"); print("    " + req.decode().replace("\r\n", "\\r\\n\n    ").rstrip())
t0 = time.time(); s.sendall(req); resp = b""
while True:
    chunk = s.recv(4096)
    if not chunk: break
    resp += chunk
print(f"  first byte after {1000*(time.time()-t0):.0f} ms; {len(resp)} bytes back. The headers:")
for line in resp.split(b"\r\n\r\n")[0].decode(errors="replace").splitlines()[:6]: print("    " + line)
s.close()

print("\n== (4) what each layer adds to a 100-byte message ==")
payload = 100
tcp = 20; ip = 20; eth = 14 + 4   # typical header sizes: TCP 20, IPv4 20, Ethernet 14 + 4-byte frame check
print(f"  application: {payload} bytes of your text")
print(f"  transport  : + {tcp}-byte TCP header (ports, sequence number, checksum)   = {payload+tcp}")
print(f"  internet   : + {ip}-byte IP header (source and destination addresses, TTL) = {payload+tcp+ip}")
print(f"  link       : + {eth}-byte Ethernet frame (MAC addresses, type, CRC)         = {payload+tcp+ip+eth}")
print(f"  on the wire, {payload} bytes of meaning travel as {payload+tcp+ip+eth}: {100*(tcp+ip+eth)/(payload+tcp+ip+eth):.0f} % of the frame is addressing and checking")
