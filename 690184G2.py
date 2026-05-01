import random
from collections import Counter

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)
HBASE2 = random.randrange(HMOD)


class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1, base2=HBASE2):
        self.mod, self.base1, self.base2 = mod, base1, base2
        self._len = _len = len(s)
        f_hash, f_pow = [0] * (_len + 1), [1] * (_len + 1)
        s_hash, s_pow = f_hash[:], f_pow[:]
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            s_hash[i + 1] = (base2 * s_hash[i] + s[i]) % mod
            f_pow[i + 1] = base1 * f_pow[i] % mod
            s_pow[i + 1] = base2 * s_pow[i] % mod
        self.f_hash, self.f_pow = f_hash, f_pow
        self.s_hash, self.s_pow = s_hash, s_pow

    def hashed(self, start, stop):
        return (
            (self.f_hash[stop] - self.f_pow[stop - start] * self.f_hash[start])
            % self.mod,
            (self.s_hash[stop] - self.s_pow[stop - start] * self.s_hash[start])
            % self.mod,
        )

    def get_hashes(self, length):
        return (
            [
                (self.f_hash[i + length] - self.f_pow[length] * self.f_hash[i])
                % self.mod
                for i in range(self._len - length + 1)
            ],
            [
                (self.s_hash[i + length] - self.s_pow[length] * self.s_hash[i])
                % self.mod
                for i in range(self._len - length + 1)
            ],
        )


def check(x):
    h1, h2 = h.get_hashes(x)
    c = Counter((i, j) for i, j in zip(h1, h2))
    return max(c.values())


n, k = map(int, input().split())
s = input()
h = Hashing([ord(i) - ord("a") + 1 for i in s])
lo, hi = 1, n
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid) >= k:
        lo = mid + 1
    else:
        hi = mid - 1
print(hi)
