#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

e = 3
d = -1

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while d == -1:
    # p = getPrime(100)
    # q = getPrime(100)
    p = 752708788837165590355094155871
    q = 986369682585281993933185289261
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

n = p * q

flag = b"crypto{N33d_b1g_pR1m35}"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag
