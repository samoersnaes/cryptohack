p = 29
ints = [14, 6, 11]
for x in ints:
    print(x, ':', [a for a in range(1, p) if pow(a, 2, p) == x])