"""Three things the syllabus names, done for real: the parts of a URL, the padlock, and a cookie.

1. urllib splits a URL into protocol, domain, path (and the rest).
2. An HTTPS connection: the server proves its name with a certificate; we print who signed it
   and until when it is valid — the padlock in the address bar is this check passing.
3. The response headers carry Set-Cookie; the browser stores it and sends it back next time
   (github.com is used because it sets one of each kind on the first visit).

Run:  python3 internet-url-and-cookies.py
"""
import ssl, socket, http.client
from urllib.parse import urlsplit
url = "https://www.bilibili.com/video/BV1xx411c7mD?p=1#comments"
u = urlsplit(url)
print("URL      ", url)
print("protocol ", u.scheme, "   domain name", u.netloc, "   path (the file on the server)", u.path, "   query", u.query, "   fragment", u.fragment)
host = "example.com"
try:
    import certifi; ctx = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")   # macOS's bundle; the python.org build ships none
with socket.create_connection((host, 443), timeout=5) as raw, ctx.wrap_socket(raw, server_hostname=host) as tls:
    cert = tls.getpeercert()
    print(f"\nHTTPS to {host}: {tls.version()} with cipher {tls.cipher()[0]}")
    print("  certificate for:", dict(x[0] for x in cert["subject"])["commonName"], " issued by:", dict(x[0] for x in cert["issuer"])["organizationName"], " valid until:", cert["notAfter"])
c = http.client.HTTPSConnection("github.com", timeout=8, context=ctx)
c.request("GET", "/", headers={"User-Agent": "Mozilla/5.0"})
r = c.getresponse()
print(f"\nGET / from github.com -> HTTP {r.status}; the server set these cookies:")
for k, v in r.getheaders():
    if k.lower() == "set-cookie":
        name = v.split("=")[0]; attrs = [a.strip() for a in v.split(";")[1:]]
        kind = "persistent (has Expires/Max-Age)" if any(a.lower().startswith(("expires", "max-age")) for a in attrs) else "session (no expiry: dies with the browser)"
        print(f"  {name:20s} {kind}")
