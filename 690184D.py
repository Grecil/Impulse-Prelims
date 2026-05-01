for _ in range(int(input())):
    n = int(input())
    arr = [*map(int, input().split())]
    st = sorted(arr)
    pos = {arr[i]: i for i in range(n)}
    swaps = 0
    for i in range(n):
        if st[i] != arr[i]:
            ind = pos[st[i]]
            arr[i], arr[ind] = arr[ind], arr[i]
            pos[arr[i]] = i
            pos[arr[ind]] = ind
            swaps += 1
    print(swaps)
