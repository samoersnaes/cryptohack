from Crypto.Util.number import isPrime

rems = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
primes = [p for p in range(2, 1000) if bool(isPrime(p)) and p > max(rems)]
xs = [x for x in range(2, 1000)]

def gen_rems(x, p):
    rems = []
    for e in range(1, p):
        rems.append(pow(x, e, p))
    return rems

found = False
for p in primes:
    print(p)
    for x in xs:
        r = gen_rems(x, p)
        try:
            # print(x, p, r[r.index(588):r.index(588)+len(rems)])
            if r[r.index(588):r.index(588)+len(rems)] == rems:
                print('x:', x, 'p:', p)
                found = True
                break
        except ValueError:
            # print('error')
            continue
    if found:
        break


# r = gen_rems(2, primes[0])
# print(r[r.index(588):r.index(588)+len(rems)])