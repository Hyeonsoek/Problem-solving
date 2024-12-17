import sys, collections
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
populations = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[] for _ in range(n+1)]
tree[0].append(1)
visited = [False] * (n+1)

visited[1] = True
queue = collections.deque([1])

while queue:
    x = queue.popleft()
    for child in graph[x]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)
            tree[x].append(child)

cache = [[-1] * 2 for _ in range(n+1)]


def dp(node, best):
    if cache[node][best] != -1:
        return cache[node][best]

    result = 0
    for child in tree[node]:
        result += dp(child, False)

    if not best:
        other = populations[node]
        for child in tree[node]:
            other += dp(child, True)
        result = max(result, other)

    cache[node][best] = result
    return result


print(dp(0, False))