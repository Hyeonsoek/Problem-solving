import sys, collections
sys.setrecursionlimit(200000)
MOD = 1000000007
input = sys.stdin.readline


def solve():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    tree = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    visited[1] = True
    queue = collections.deque([1])

    while queue:
        node = queue.popleft()

        for child, cost in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                tree[node].append((child, cost))

    cache = [[-1, -1] for _ in range(n+1)]
    print(sum(dp(1, tree, cache)) % MOD)


def dp(node, tree, cache):
    if cache[node][0] != -1 and cache[node][1] != -1:
        return cache[node]

    result = [0, 0]
    for child, cost in tree[node]:
        child_result = dp(child, tree, cache)
        child_result[1] = sum(child_result)
        child_result[0] = (child_result[0] + 1) * cost

        result[1] = (result[1] + result[0] * child_result[0] + child_result[1]) % MOD
        result[0] = (result[0] + child_result[0]) % MOD

    cache[node][0] = result[0]
    cache[node][1] = result[1]
    return cache[node]


solve()