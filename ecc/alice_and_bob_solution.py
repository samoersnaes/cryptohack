from Crypto.Util.number import inverse, long_to_bytes
from Crypto.Hash import SHA1


# assumed prerequisite
def pt_add(p, q, E):
    zero = (0, 0)
    if p == zero:
        return q
    elif q == zero:
        return p
    else:
        x1, y1 = p
        x2, y2 = q
        if x1 == x2 and y1 == -y2:
            return zero

        Ea, Ep = E['a'], E['p']
        if p != q:
            lmd = (y2 - y1) * inverse(x2 - x1, Ep)
        else:
            lmd = (3 * (x1**2) + Ea) * inverse(2 * y1, Ep)
        x3 = ((lmd**2) - x1 - x2) % Ep
        y3 = (lmd * (x1 - x3) - y1) % Ep
        return x3, y3


# assumed prerequisite
def scalar_mult(n, p, E):
    q, r = p, (0, 0)
    while n > 0:
        if n % 2 == 1:
            r = pt_add(r, q, E)
        q = pt_add(q, q, E)
        n //= 2
    return r


if __name__ == '__main__':
    E = {'a': 497, 'b': 1768, 'p': 9739, 'G': (1804, 5368)}

    # previous challenge assertions omitted for brevity

    QA = (815, 3190)
    nB = 1829
    S = scalar_mult(nB, QA, E)
    Hx = SHA1.new(str(S[0]).encode()).hexdigest() # inside new: b'7929'
    print('alice and bob: ' + 'crypto{' + Hx + '}')
