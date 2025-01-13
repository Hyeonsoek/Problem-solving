from collections import *
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]
HDRX = [-2, -1, 1, 2, -2, -1, 1, 2]
HDRY = [-1, -2, -2, -1, 1, 2, 2, 1]

def solve():
    K = int(input())
    W, H = map(int, input().split())
    
    visited = [[[0] * W for _ in range(H)] for _ in range(K + 1)]
    board = [[*map(int, input().split())] for _ in range(H)]
    
    def isinner(xx, yy, k):
        return 0 <= xx < W and 0 <= yy < H and\
            not visited[k][yy][xx] and not board[yy][xx]
    
    visited[K][0][0] = 1
    queue = deque([(0, K, 0, 0)])
    while queue:
        dist, k, xx, yy = queue.popleft()
        
        if (xx, yy) == (W - 1, H - 1):
            return dist
        
        for d in range(4):
            nx = xx + DRX[d]
            ny = yy + DRY[d]
            if isinner(nx, ny, k):
                visited[k][ny][nx] = 1
                queue.append((dist + 1, k, nx, ny))

        if k:
            for d in range(8):
                nx = xx + HDRX[d]
                ny = yy + HDRY[d]
                if isinner(nx, ny, k - 1):
                    visited[k-1][ny][nx] = 1
                    queue.append((dist + 1, k - 1, nx, ny))
    
    return -1

print(solve())