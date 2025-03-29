import sys
from collections import deque, defaultdict
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [[*map(int, input().strip())] for _ in range(n)]
    
    count = defaultdict(int)
    visited = [[0] * m for _ in range(n)]
    
    def isinner(nx, ny):
        return 0 <= nx < n and 0 <= ny < m
    
    def bfs(i, j, v):
        count = 0
        queue = deque([(i, j)])
        visited[i][j] = v
        
        while queue:
            xx, yy = queue.popleft()
            count += 1
            
            for i in range(4):
                nx = xx + DRX[i]
                ny = yy + DRY[i]
                if isinner(nx, ny) and not board[nx][ny] and visited[nx][ny] != v:
                    visited[nx][ny] = v
                    queue.append((nx, ny))

        return count, v + 1
    
    v = 1
    block = []
    for i in range(n):
        for j in range(m):
            if not board[i][j] == 0 and not visited[i][j]:
                count[v], v = bfs(i, j, v)
            
            if board[i][j]:
                block.append((i, j))
    
    res = [[0] * m for _ in range(n)]
    for xx, yy in block:
        s = set()
        for i in range(4):
            nx = DRX[i] + xx
            ny = DRY[i] + yy
            if isinner(nx, ny) and visited[nx][ny] not in s:
                s.add(visited[nx][ny])
                res[xx][yy] += count[visited[nx][ny]]
        res[xx][yy] += 1
        res[xx][yy] %= 10
    
    for i in range(n):
        print(*res[i], sep='')

solve()