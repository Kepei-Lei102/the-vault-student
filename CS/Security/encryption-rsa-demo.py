"""Asymmetric encryption, actually run.
Part 1 — textbook RSA from scratch with small numbers (p = 61, q = 53), so every step is checkable by hand.
Part 2 — RSA with 2048-bit primes generated here by Miller–Rabin: encrypt, decrypt, sign, verify.
Part 3 — the real thing with the `cryptography` library: RSA-OAEP, PSS signatures, and the hybrid
          scheme every real protocol uses (RSA to move an AES key, AES-GCM to move the message).
Part 4 — Diffie–Hellman: two people agree a secret over a public channel.
Run:  python3 encryption-rsa-demo.py"""
import random, hashlib, time, math

# ---------- Part 1: RSA by hand ----------
p, q = 61, 53
n = p * q                      # 3233 — the public modulus
phi = (p - 1) * (q - 1)        # 3120 — Euler's totient, the secret behind the secret
e = 17                         # public exponent: any e with gcd(e, phi) = 1
d = pow(e, -1, phi)            # private exponent: e·d ≡ 1 (mod phi)  → 2753
assert (e * d) % phi == 1
print("== Part 1: textbook RSA ==")
print(f"p={p} q={q}  n={n}  phi={phi}  public=(e={e}, n={n})  private=(d={d}, n={n})")
m = 65                         # the message 'A' (ASCII 65)
c = pow(m, e, n)               # encrypt with the PUBLIC key
m2 = pow(c, d, n)              # decrypt with the PRIVATE key
print(f"message m={m} ('A')  ->  ciphertext c = {m}^{e} mod {n} = {c}  ->  {c}^{d} mod {n} = {m2}")
assert m2 == m
# a signature is the same trick run backwards
s = pow(m, d, n)               # sign with the PRIVATE key
print(f"signature s = {m}^{d} mod {n} = {s};  verify: {s}^{e} mod {n} = {pow(s, e, n)}  (equals m, so it was signed by the holder of d)")
# encrypt a whole word, letter by letter (insecure in practice — see the card — but it shows the mechanism)
word = "HI"
cipher = [pow(ord(ch), e, n) for ch in word]
plain = "".join(chr(pow(x, d, n)) for x in cipher)
print(f"'{word}' -> {cipher} -> '{plain}'")

# ---------- Part 2: RSA at real size, from scratch ----------
def is_probable_prime(n, rounds=40):
    if n < 2: return False
    for sp in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % sp == 0: return n == sp
    d, r = n - 1, 0
    while d % 2 == 0: d //= 2; r += 1
    for _ in range(rounds):                      # Miller–Rabin
        a = random.randrange(2, n - 1); x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def random_prime(bits):
    while True:
        cand = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_probable_prime(cand): return cand

print("\n== Part 2: 2048-bit RSA, generated here ==")
t0 = time.time(); P = random_prime(1024); Q = random_prime(1024); t1 = time.time()
N = P * Q; PHI = (P - 1) * (Q - 1); E = 65537; D = pow(E, -1, PHI)
print(f"two 1024-bit primes found in {t1 - t0:.1f} s; N has {N.bit_length()} bits, {len(str(N))} decimal digits")
msg = b"Meet at the Sublight Lounge at nine."
M = int.from_bytes(msg, "big"); assert M < N
C = pow(M, E, N); back = pow(C, D, N).to_bytes((N.bit_length() + 7) // 8, "big").lstrip(b"\x00")
print(f"encrypt with public (E, N): ciphertext starts {str(C)[:24]}...; decrypt with private D: {back!r}")
assert back == msg
h = int.from_bytes(hashlib.sha256(msg).digest(), "big")
sig = pow(h, D, N); print(f"sign SHA-256(msg) with D; verify with E: {pow(sig, E, N) == h}")
print(f"tamper one byte and verify again: {pow(sig, E, N) == int.from_bytes(hashlib.sha256(msg[:-1] + b'!').digest(), 'big')}")

# ---------- Part 3: the real thing ----------
print("\n== Part 3: cryptography library — RSA-OAEP, PSS, and hybrid AES-GCM ==")
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
alice_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
alice_public = alice_private.public_key()
pem = alice_public.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
print("Alice's public key, as she would publish it:\n" + pem.decode().splitlines()[0] + "\n" + pem.decode().splitlines()[1][:64] + "...")
# Bob encrypts TO Alice with Alice's PUBLIC key
ct = alice_public.encrypt(b"Bob -> Alice: only you can read this", padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
pt = alice_private.decrypt(ct, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
print(f"RSA-OAEP: {len(ct)}-byte ciphertext -> {pt!r}")
# Alice signs with her PRIVATE key; anyone verifies with her PUBLIC key
document = b"I, Alice, agree to pay Bob 100 credits."
signature = alice_private.sign(document, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
try:
    alice_public.verify(signature, document, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()); print("PSS signature verifies with Alice's public key: True")
    alice_public.verify(signature, document.replace(b"100", b"900"), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
except Exception as ex:
    print(f"altered document ('900 credits') -> verification raises {type(ex).__name__}")
# Hybrid: RSA moves a 256-bit AES key; AES-GCM moves the actual data (this is what TLS, PGP and Signal do)
aes_key = AESGCM.generate_key(bit_length=256); nonce = os.urandom(12)
big = ("The whole of a long message, or a 4 GB file, goes under AES; " * 2000).encode()
t0 = time.time(); body = AESGCM(aes_key).encrypt(nonce, big, None); t_aes = time.time() - t0
wrapped_key = alice_public.encrypt(aes_key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
key_back = alice_private.decrypt(wrapped_key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
assert AESGCM(key_back).decrypt(nonce, body, None) == big
print(f"hybrid: {len(big)/1e6:.2f} MB under AES-GCM in {t_aes*1000:.1f} ms; the 32-byte AES key travels inside a {len(wrapped_key)}-byte RSA envelope")

# ---------- Part 4: Diffie–Hellman ----------
print("\n== Part 4: Diffie–Hellman with small numbers ==")
g, pm = 5, 23                                  # public: generator and prime
a, b = 6, 15                                    # Alice's and Bob's private numbers
A, B = pow(g, a, pm), pow(g, b, pm)             # what they send in the open
print(f"public g={g}, p={pm}; Alice sends A = {g}^{a} mod {pm} = {A}; Bob sends B = {g}^{b} mod {pm} = {B}")
print(f"Alice computes B^a = {pow(B, a, pm)}; Bob computes A^b = {pow(A, b, pm)}  -> same shared secret, never transmitted")
