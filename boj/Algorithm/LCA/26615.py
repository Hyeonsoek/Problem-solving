import sys
sys.setrecursionlimit(100000)
MAX_DEPTH = 17
dirr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
input = sys.stdin.readline

def make_board(n, m):
    board = [[0] * (2 * m - 1) for _ in range(2 * n - 1)]
    
    for x in range(n-1):
        for y, wall in enumerate(map(int, input().split())):
            board[2*x + 1][2*y] = wall
    
    for x in range(n):
        for y, wall in enumerate(map(int, input().split())):
            board[2*x][2*y + 1] = wall
    
    return board

def make_tree(board, n, m):
    graph = [[[] for _ in range(m) ] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for xdir, ydir in dirr:
                xx, yy = 2 * x + xdir, 2 * y + ydir
                if 0 <= xx < 2 * n - 1 and 0 <= yy < 2 * m - 1 and board[xx][yy] == 0:
                    graph[x][y].append((x + xdir, y + ydir))

    depths = [0] * (n * m)
    parents = [[-1] * MAX_DEPTH for _ in range(n * m)]
    
    def dfs(x, y):
        vertex = x * m + y
        for nx, ny in graph[x][y]:
            next = nx * m + ny
            if not depths[next]:
                parents[next][0] = vertex
                depths[next] = depths[vertex] + 1
                dfs(nx, ny)
        
    dfs(0, 0)
    
    for depth in range(1, MAX_DEPTH):
        for node in range(n * m):
            prev = parents[node][depth - 1]
            parents[node][depth] = parents[prev][depth - 1]
    
    return depths, parents

def lca(parents, depths, u, v):
    result = 0
    
    if depths[u] < depths[v]:
        u, v = v, u
    
    for x in range(MAX_DEPTH - 1, -1, -1):
        if depths[u] - depths[v] >= 1 << x:
            u = parents[u][x]
            result += 1 << x
    
    if u != v:
        for depth in range(MAX_DEPTH - 1, -1, -1):
            if parents[u][depth] != -1 and parents[u][depth] != parents[v][depth]:
                u = parents[u][depth]
                v = parents[v][depth]
                result += 1 << (depth + 1)
        
        result += 2
    
    return result

def solve():
    n, m, t = map(int, input().split())
    board = make_board(n, m)
    depths, parents = make_tree(board, n, m)
    prefix = [0] * (t + 1)
    
    k = int(input())
    for _ in range(k):
        s, e, a, b, c, d, v = map(int, input().split())
        uu, vv = a * m + b, c * m + d
        count = lca(parents, depths, uu, vv)
        prefix[s-1] += (count + 1) * v
        prefix[e] -= (count + 1) * v
    
    for x in range(1, t + 1):
        prefix[x] += prefix[x-1]
        
    print(*prefix[:t], sep='\n')
        
solve()