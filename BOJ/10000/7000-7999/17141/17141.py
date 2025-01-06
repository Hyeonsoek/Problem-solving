import sys
from collections import deque
from itertools import combinations
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

def solve():
    n, m = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]
    
    virus = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus.append((i, j))
                board[i][j] = 0
    
    def bfs(positions):
        queue = deque()
        visited = [[0] * n for _ in range(n)]
        
        for i, j in positions:
            queue.append((1, i, j))
            visited[i][j] = 1
        
        while queue:
            count = len(queue)
            for _ in range(count):
                cost, xx, yy = queue.popleft()
                for d in range(4):
                    nx = DRX[d] + xx
                    ny = DRY[d] + yy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                        queue.append((cost + 1, nx, ny))
                        visited[nx][ny] = cost + 1
        
        result = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if not visited[i][j]:
                        return sys.maxsize
                    result = max(result, visited[i][j])
        
        return result - 1

    if len(virus) <= m:
        result = bfs(virus)
        print(-1 if result == sys.maxsize else result)
    else:
        result = sys.maxsize
        for comb in combinations(virus, m):
            result = min(result, bfs(comb))
        print(-1 if result == sys.maxsize else result)

solve()