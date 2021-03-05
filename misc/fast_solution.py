import time
from Crypto.Util.number import long_to_bytes
import hashlib


FLAG = b'crypto{????????????????????}'

ct = '7442b44b070ee542422792611070bbfbdb7401df3899142dbe076e6a'
cur = [i for i in range(1588017608, 1588017619)] # 1588017613


def generate_key(cur):
    key = long_to_bytes(cur)
    return hashlib.sha256(key).digest()


def decrypt(key):
    ciphertext = long_to_bytes(int(ct, 16))
    assert len(ciphertext) <= len(key), "Data package too large to encrypt"
    decrypted = b''
    for i in range(len(ciphertext)):
        decrypted += bytes([ciphertext[i] ^ key[i]])
    return decrypted


if __name__ == '__main__':
    for c in cur:
        print(decrypt(generate_key(c)))