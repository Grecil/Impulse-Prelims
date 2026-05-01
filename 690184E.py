from collections import defaultdict

n, q = map(int, input().split())
arr = [*map(int, input().split())]
st = []
ng = defaultdict(lambda: float("inf"))
for i in range(n - 1, -1, -1):
    while st and st[-1][0] <= arr[i]:
        st.pop()
    if st:
        ng[i] = st[-1][1]
    st.append((arr[i], i))
off = 0
ans = defaultdict(lambda: float("inf"))
for _ in range(q):
    qi, x = map(int, input().split())
    if qi == 1:
        off -= 1
        while st and st[-1][0] <= x:
            v, i = st.pop()
        if st:
            ng[off] = st[-1][1]
        st.append((x, off))
    elif qi == 2:
        x += off - 1
        cur = 0
        curp = x
        while ans[curp] > cur:
            ans[curp] = cur
            curp = ng[curp]
            cur += 1
            if curp == float("inf"):
                break
    elif qi == 3:
        x += off - 1
        print(ans[x] if ans[x] != float("inf") else -1)
