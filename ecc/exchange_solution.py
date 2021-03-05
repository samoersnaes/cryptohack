from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from ecc import * # E, pt_add, and scalar_mult


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


"""
Optional read:

You can also remove '% p' when calculating Qysq and still get the same result.
When calculating Qy, we end up taking the result mod p anyway, so it appears
not to matter for this example. I simply don't know whether all intermediate
values (in this case Qysq) are required to be in E(Fp). I prefer to be
cautious and therefore *do* take all values mod p.

Qysq is a quadratic residue of p, and p is congruent to 3 mod 4, so we can
use Lagrange's solution to quickly find the positive and negative square roots
of Qysq. It turns out that our final answer is the same no matter whether we
assign the positive or negative square root to Qy.

Lagrange's formula:
https://en.wikipedia.org/wiki/Quadratic_residue#Prime_or_prime_power_modulus

Refer to 'Quadratic Residues' and 'Legendre Symbol' in the General challenges
for more information.
"""

Qx = 4726
nB = 6534
a, b, p = E['a'], E['b'], E['p']

Qysq = (Qx**3 + (a * Qx) + b) % p
assert pow(Qysq, (p - 1) // 2, p) == 1 # Qysq is a quadratic residue of p
Qy = pow(Qysq, (p + 1) // 4, p) # positive or negative versions both work

QA = (Qx, Qy)
S = scalar_mult(nB, QA, E)

shared_secret = S[0] # we only want the x-coordinate of the shared secret
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))
