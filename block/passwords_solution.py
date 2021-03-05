"""
Offline attack. Simple bruteforce solution.

First, run this on the command line in the same directory
as the solution file:

$ curl https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words > words.txt

The rest is done in the script below.
"""


from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib


# slightly modified from source
# always returns a non-empty hex-string or ''
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        decrypted = b''

    return decrypted.hex()


# from the API
ct = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'

with open('words.txt', 'r') as f:
    words = [w.strip() for w in f.readlines()]

passwords = [hashlib.md5(w.encode()).digest().hex() for w in words]
for pw in passwords:
    res = long_to_bytes(int(decrypt(ct, pw), 16))
    if res.startswith(b'crypto'):
        print(res.decode())
        break