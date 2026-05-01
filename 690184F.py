class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size : _size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        start += self._size
        stop += self._size

        res_left = self._default
        res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


mod = int(1e9 + 7)


def merge(x1, x2):
    a = (x1[0] * x2[0] + x1[1] * x2[1]) % mod
    b = (x1[0] * x2[1] + x1[1] * x2[0]) % mod
    c = (x1[2] * (x2[0] + x2[1]) + x2[2]) % mod
    return (a, b, c)


n, q = map(int, input().split())
arr = []
for i in range(n):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))
st = SegmentTree(arr, (1, 0, 0), merge)
for i in range(q):
    qi, p, a, b, c = map(int, input().split())
    if qi == 0:
        st[p - 1] = (a, b, c)
    else:
        l, r, x, y = p, a, b, c
        a, b, c = st.query(l - 1, r)
        print((a * x + b * y + c) % mod)
