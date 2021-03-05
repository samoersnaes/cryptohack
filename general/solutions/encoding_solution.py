import json
import codecs
import base64
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes


def json_recv(r):
    line = r.recvline()
    return json.loads(line.decode())

def json_send(r, hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def hex_decode(encoded):
    return bytes.fromhex(encoded).decode()
    # return ''.join([chr(int(encoded[n:n+2], 16)) for n in range(0, len(encoded), 2)])

def rot13_decode(encoded):
    return codecs.decode(encoded, 'rot_13')

def utf8_decode(encoded):
    return ''.join([chr(c) for c in encoded])

def bigint_decode(encoded):
    return long_to_bytes(int(encoded, 16)).decode()

def b64_decode(encoded):
    return base64.b64decode(encoded.encode()).decode()


if __name__ == '__main__':
    DEBUG = True
    if DEBUG:
        r = remote('socket.cryptohack.org', 13377, level='debug')
    else:
        r = remote('socket.cryptohack.org', 13377)

    for _ in range(100):
        received = json_recv(r)
        rtype = received['type']
        encoded = received['encoded']
        decoded = ''

        if DEBUG:
            print('Received type: ')
            print(received['type'])
            print('Received encoded value: ')
            print(received['encoded'])

        if rtype == 'hex':
            decoded = hex_decode(encoded)
        elif rtype == 'rot13':
            decoded = rot13_decode(encoded)
        elif rtype == 'utf-8':
            decoded = utf8_decode(encoded)
        elif rtype == 'bigint':
            decoded = bigint_decode(encoded)
        elif rtype == 'base64':
            decoded = b64_decode(encoded)

        to_send = {'decoded': decoded}
        json_send(r, to_send)

    print(json_recv(r))
