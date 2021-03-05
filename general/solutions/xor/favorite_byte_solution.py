xored = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for mask in range(1, 256):
    candidate = ''.join([chr(byte ^ mask) for byte in xored])
    if candidate.startswith('crypto'):
        print(candidate)
        break