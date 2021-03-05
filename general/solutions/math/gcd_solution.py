def gcd(a, b): # might be useful to keep as a function for later
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(66528, 52920))