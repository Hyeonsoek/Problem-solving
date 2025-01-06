from collections import Counter
from itertools import product

def solve():
    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        p, c = map(int, input().split())
        tree[p].append(c)
    apple = list(map(int, input().split()))
    
    # def dfs(node, perm, visited):
    #     visited |= 1 << node
    #     result = apple[node]
    #     for x in tree[node]:
    #         if perm & (1 << x):
    #             count, visited = dfs(x, perm, visited)
    #             result += count
                
    #     return result, visited
    
    # result = 0
    # for x in range(1, 2 ** n):
    #     xx = Counter(str(bin(x)))
    #     if xx['1'] <= m:
    #         count, visited = dfs(0, x, 0)
    #         if visited == x:
    #             result = max(result, count)
    
    # print(result)
    
    def dfs(node, perm, visited):
        visited[node] = 1
        result = apple[node]
        for x in tree[node]:
            if perm[x]:
                result += dfs(x, perm, visited)
        return result
    
    result = 0
    for perm in product([0, 1], repeat=n):
        counter = Counter(perm)
        if counter[1] <= m:
            visited = [0] * n
            count = dfs(0, perm, visited)
            
            if tuple(visited) == perm:
                result = max(result, count)
    
    print(result)

solve()