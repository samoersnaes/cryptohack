import json
import codecs
import base64
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes


def json_receive(rmt):
    line = rmt.recvline()
    return json.loads(line.decode())

def json_send(rmt, hsh):
    request = json.dumps(hsh).encode()
    rmt.sendline(request)

def ascii_hex_decode(encoded):
    return ''.join([chr(int(encoded[n:n+2], 16)) for n in range(0, len(encoded), 2)])

def rot13_decode(encoded):
    return codecs.decode(encoded, 'rot_13')

def utf8_decode(encoded):
    return ''.join([chr(c) for c in encoded])

def bigint_decode(encoded):
    return long_to_bytes(int(encoded, 16)).decode()

def base64_decode(encoded):
    return base64.standard_b64decode(encoded).decode()