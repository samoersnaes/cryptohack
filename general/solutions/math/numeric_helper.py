def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def ext_gcd(a, b):
    x,y,u,v = 0,1,1,0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - (u * q), y - (v * q)
        b,a,x,y,u,v = a,r,u,v,m,n
    return x, y