import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0, *map(int, input().split())]
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    tree = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        for next in graph[node]:
            if not visited[next]:
                tree[node].append(next)
                dfs(next)
    
    cache = [[-1, -1] for _ in range(n + 1)]
    def dynamic(node, add):
        if cache[node][add] != -1:
            return cache[node][add]
        
        result = 0
        if add == 1:
            result += arr[node]

        for next in tree[node]:
            if add == 1:
                left = dynamic(next, 0)
                result += left
            else:
                left = dynamic(next, 0)
                right = dynamic(next, 1)
                result += max(left, right)

        cache[node][add] = result
        return result
    
    result = []
    def backtracking(node, add):
        if add:
            result.append(node)
        
        for next in tree[node]:
            if add:
                backtracking(next, 0)
            else:
                backtracking(next, dynamic(next, 0) < dynamic(next, 1))
    
    dfs(1)
    
    left, right = dynamic(1, 0), dynamic(1, 1)
    print(max(left, right))
    backtracking(1, left < right)
    print(*sorted(result))
    
solve()