from Crypto.Util.number import inverse


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


# expect to create a module of helper functions in this file
if __name__ == '__main__':
    E = {'a': 497, 'b': 1768, 'p': 9739}

    x = (5274, 2841)
    y = (8669, 740)
    assert pt_add(x, y, E) == (1024, 4440)
    assert pt_add(x, x, E) == (7284, 2107)

    p = (493, 5564)
    q = (1539, 4742)
    r = (4403, 5202)
    s = pt_add(p, p, E)
    t = pt_add(s, q, E)
    add_flag = pt_add(t, r, E)
    assert add_flag == (4215, 2162)
    print(f'crypto{add_flag}')