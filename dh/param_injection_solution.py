from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


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


shared_secret = 230582828342844349126836085799395916934368298821927592299861447875268374993197271876605822847027220595912680068018378960767013987091636991225146122690126396973844135974756155461919600575462554400071996687928910843092016816532953768913563483141318549970171156163555355500977323322677195288736986981749978064588447676421068484817807512088547183721503112265512723789303889726635718323876979730522043254784692023195795176868561335048297163330924594590451217779417934
iv = '82f374462d5fe65f98ef0fb83d7795aa'
ciphertext = '3780667470f3e35484abca2f4ac8029cc934dadca943ac812bf2afc0555e7769'

print(decrypt_flag(shared_secret, iv, ciphertext))

