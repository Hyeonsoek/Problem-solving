import sys, collections
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def bfs(n, graph):
    tree = [[] for _ in range(n)]
    visited = [False] * n

    visited[0] = True
    queue = collections.deque([0])

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[node] = True
                tree[node].append(child)
                queue.append(child)

    return tree


def solve():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    tree = bfs(n, graph)
    cache = [[-1] * 2 for _ in range(n)]

    def dp(node, early):
        if cache[node][early] != -1:
            return cache[node][early]

        result = 1
        for child in tree[node]:
            result += dp(child, True)

        if early:
            other = 0
            for child in tree[node]:
                other += dp(child, False)
            result = min(other, result)

        cache[node][early] = result
        return result

    print(dp(0, True))


solve()