from collections import deque

def solve():
    n = int(input())
    m = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    x = int(input())

    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while queue:
        xx, yy = queue.popleft()
    
        if xx == n - 1 and yy == m - 1:
            return "ALIVE"
        
        for dx in range(-x, x + 1):
            for dy in range(-x + abs(dx), x - abs(dx) + 1):
                nx = dx + xx
                ny = dy + yy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == board[0][0]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    
    return "DEAD"

print(solve())