import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(n) ]
    
    result = 0
    visited = [[False] * m for _ in range(n)]
    
    def bfs(sx, sy):
        ispeak = True
        visited[sx][sy] = True
        queue = deque([(sx, sy)])
        while queue:
            xx, yy = queue.popleft()
            
            for xd, yd in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                nx = xd + xx
                ny = yd + yy
                if 0 <= nx < n and 0 <= ny < m:
                    if board[xx][yy] < board[nx][ny]:
                        ispeak = False
                    
                    if not visited[nx][ny] and board[nx][ny] == board[xx][yy]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        return 1 if ispeak else 0
    
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and board[x][y] > 0:
                result += bfs(x, y)
    
    print(result)
    
solve()