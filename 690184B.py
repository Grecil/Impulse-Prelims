n, m, s = map(int, input().split())
edges = set()
for i in range(m):
    u, v = map(int, input().split())
    edges.add((u, v))
    edges.add((v, u))
h = [(s, 0)]
vis = set(range(1, n + 1))
dist = [-1] * (n + 1)
for u, d in h:
    dist[u] = d
    to_rem = set()
    for v in vis:
        if (u, v) not in edges:
            h.append((v, d + 1))
            to_rem.add(v)
    vis.difference_update(to_rem)
dist.pop(s)
dist.pop(0)
print(*dist)
