def moves(a, b):
    return a + (b >> a) + (b - ((b >> a) << a)).bit_count()


for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = float("inf")
    for i in range(128):
        x = 1 << i
        if x > n:
            break
        if (n - x) % k == 0:
            ans = min(ans, moves(i, (n - x) // k))
    if ans != float("inf"):
        print("YES", ans)
    else:
        print("NO")
