import sys
from collections import *
input = sys.stdin.readline
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

N, M, K = map(int, input().split())
board = [[*map(int, input().strip())] for _ in range(N)]
visited = [[[[0] * M for _ in range(N)] for _ in range(K + 1)] for _ in range(2)]

def isinner(xx, yy):
    return 0 <= xx < M and 0 <= yy < N

visited[1][K][0][0] = 1
queue = deque([(1, K, 0, 0)])
while queue:
    dist, k, xx, yy = queue.popleft()
    
    if (xx, yy) == (M - 1, N - 1):
        print(dist)
        exit(0)
    
    isday = dist & 1
    isnextday = (dist + 1) & 1
    for i in range(4):
        nx = xx + DRX[i]
        ny = yy + DRY[i]
        if isinner(nx, ny):
            if board[ny][nx] and k > 0:
                if isday:
                    if not visited[isnextday][k-1][ny][nx]:
                        visited[isnextday][k-1][ny][nx] = 1
                        queue.append((dist + 1, k - 1, nx, ny))
                else:
                    if not visited[isnextday][k][yy][xx]:
                        visited[isnextday][k][yy][xx] = 1
                        queue.append((dist + 1, k, xx, yy))
            if not board[ny][nx] and not visited[isnextday][k][ny][nx]:
                visited[isnextday][k][ny][nx] = 1
                queue.append((dist + 1, k, nx, ny))

print(-1)

# 3 3 2
# 011
# 111
# 110