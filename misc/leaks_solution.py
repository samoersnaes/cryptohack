import json
import codecs
import base64
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from collections import defaultdict
import random


def json_recv(r):
    line = r.recvline()
    return json.loads(line.decode())

def json_send(r):
    to_send = {'msg': 'request'}
    request = json.dumps(to_send).encode()
    r.sendline(request)

def hex_decode(encoded):
    return bytes.fromhex(encoded).decode()
    # return ''.join([chr(int(encoded[n:n+2], 16)) for n in range(0, len(encoded), 2)])

def utf8_decode(encoded):
    return ''.join([chr(c) for c in encoded])

def bigint_decode(encoded):
    return long_to_bytes(int(encoded, 16)).decode()

if __name__ == '__main__':
    messages = []
    with open('leaks.txt', 'r') as f:
        for line in f:
            messages.append(long_to_bytes(int(line)))

    possible = defaultdict(set)
    for m in messages:
        for i, b in enumerate(m):
            possible[i].add(b)

    allowed = {c for c in range(32, 127)}
    sifted = defaultdict(set)
    for i in range(20):
        sifted[i] = allowed - possible[i]
    print(sifted)

    text = []
    for i in range(20):
        text.append(chr(random.choice(list(sifted[i]))))
    print(''.join(text))

if False:
    DEBUG = False
    if DEBUG:
        r = remote('socket.cryptohack.org', 13370, level='debug')
    else:
        r = remote('socket.cryptohack.org', 13370)

    r.recvline()

    texts = []

    i = 0
    for _ in range(200):
        json_send(r)
        received = json_recv(r)
        if 'ciphertext' in received:
            ct = received['ciphertext']
            texts.append(ct)
            print(ct)
        else:
            i += 1

    print(i)

    with open('leaks.txt', 'a') as f:
        for t in texts:
            f.write(str(bytes_to_long(base64.b64decode(t))))
            f.write('\n')