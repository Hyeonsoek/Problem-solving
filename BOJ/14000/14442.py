import sys
from collections import deque
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(N)]

    distance = [[11] * M for _ in range(N)]
    distance[0][0] = 0
    
    queue = deque([(0, 0, 1)])
    while queue:
        x, y, count = queue.popleft()
        
        if x == N - 1 and y == M - 1 and distance[x][y] <= K:
            return count
        
        for dx, dy in dirr:
            xx = dx + x
            yy = dy + y
            if 0 <= xx < N and 0 <= yy < M:
                nextdist = distance[x][y] + board[xx][yy]
                if distance[xx][yy] > nextdist:
                    distance[xx][yy] = nextdist
                    queue.append((xx, yy, count + 1))
    
    return -1

print(solve())