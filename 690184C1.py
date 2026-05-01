for _ in range(int(input())):
    n, k = map(int, input().split())
    for i in range(128):
        x = 1 << i
        if x > n:
            print("NO")
            break
        if (n - x) % k == 0:
            print("YES")
            break
