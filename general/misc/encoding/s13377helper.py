from pwn import * # pip install pwntools
import json
import codecs
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes
from helper import *

if __name__ == '__main__':
    r = remote('socket.cryptohack.org', 13377, level='debug')

    for _ in range(100):
        received = json_receive(r)
        rtype = received['type']
        encoded = received['encoded']
        decoded = ''

        print('Received type: ')
        print(received['type'])
        print('Received encoded value: ')
        print(received['encoded'])

        if rtype == 'hex':
            decoded = ascii_hex_decode(encoded)
        elif rtype == 'rot13':
            decoded = rot13_decode(encoded)
        elif rtype == 'utf-8':
            decoded = utf8_decode(encoded)
        elif rtype == 'bigint':
            decoded = bigint_decode(encoded)
        elif rtype == 'base64':
            decoded = base64_decode(encoded)

        to_send = {'decoded': decoded}
        json_send(r, to_send)

    json_receive(r)
