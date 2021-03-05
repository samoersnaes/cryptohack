import sys
key = ''
for line in sys.stdin:
    key += line.strip().replace(':', '')
print(int(key, 16))