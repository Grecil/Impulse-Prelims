from functools import cache
from collections import Counter
from math import gcd


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + i) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + i) % n, (y * y + i) % n
                    y = (y * y + i) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@cache
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)


n, k = map(int, input().split())
pf = prime_factors(n)
facs = []
for i in pf:
    facs.extend([i] * pf[i])
if len(facs) < k:
    print(-1)
else:
    for i in range(k, len(facs)):
        facs[k - 1] *= facs[i]
    print(*facs[:k])
