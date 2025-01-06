from collections import deque
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

def solve():
    x, y, n = map(int, input().split())
    x += 500
    y += 500
    visited = [[False] * 1001 for _ in range(1001)]
    
    for _ in range(n):
        Ai, Bi = map(int, input().split())
        visited[Ai + 500][Bi + 500] = True
    
    visited[500][500] = True
    queue = deque([(0, 500, 500)])
    while queue:
        dist, xx, yy = queue.popleft()
        
        if (xx == x) and (yy == y):
            return dist
        
        for d in range(4):
            nx = DRX[d] + xx
            ny = DRY[d] + yy
            if 0 <= nx < 1001 and 0 <= ny < 1001 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((dist + 1, nx, ny))
    
    return 0

print(solve())