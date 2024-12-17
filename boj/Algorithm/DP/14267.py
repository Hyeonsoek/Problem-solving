import sys
sys.setrecursionlimit(130000)
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    parents = list(map(int, input().split()))
    for x in range(1, n):
        tree[parents[x]-1].append(x)

    cache = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        cache[a-1] += b

    def dfs(node, value):
        cache[node] += value
        for next in tree[node]:
            dfs(next, cache[node])

    dfs(0, 0)
    print(*cache)


solve()