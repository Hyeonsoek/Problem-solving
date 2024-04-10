def LCM(a, b):
    return a * b // GCD(a, b)

def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

def solve():
    n = int(input())
    graph = [[] for _ in range(n)]
    result = [1] * n
    
    def dfs(node, value):
        visited = [0] * n
        visited[node] = 1
        
        def _dfs(node):
            result[node] *= value
            for x in graph[node]:
                if not visited[x]:
                    visited[x] = 1
                    _dfs(x)
                    
        _dfs(node)
        
    for _ in range(n - 1):
        a, b, p, q = map(int, input().split())
        
        wa = result[a] * q
        wb = result[b] * p
        
        lcm = LCM(wa, wb)
        mutiplyA = (lcm // wa)
        mutiplyB = (lcm // wb)
        
        dfs(a, mutiplyA)
        dfs(b, mutiplyB)
        
        graph[a].append(b)
        graph[b].append(a)

    print(*result)
    
solve()