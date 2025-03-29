import sys
from collections import deque
input = sys.stdin.readline
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

def solve():
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    def is_inner(yy, xx):
        return 0 <= yy < N and 0 <= xx < N
    
    def is_openable(yy, xx, y, x):
        return L <= abs(board[y][x] - board[yy][xx]) <= R

    def bfs(i, j, res):
        visited[i][j] = res

        queue = deque()
        queue.append((i, j))

        cost = 0
        union = []

        while queue:
            y, x = queue.popleft()
            cost += board[y][x]
            union.append((y, x))

            for k in range(4):
                yy = DRY[k] + y
                xx = DRX[k] + x
                if is_inner(yy, xx) and is_openable(yy, xx, y, x) and visited[yy][xx] < res:
                    queue.append((yy, xx))
                    visited[yy][xx] = res

        n = len(union)
        if n > 1:
            value = cost // n
            for y, x in union:
                board[y][x] = value
                Vqueue.append((y, x))

    res = 0
    visited = [[-1] * N for _ in range(N)]
    Vqueue = deque([(i, j) for i in range(N) for j in range(N)])
    while Vqueue:
        for _ in range(len(Vqueue)):
            yy, xx = Vqueue.popleft()
            if visited[yy][xx] < res:
                bfs(yy, xx, res)
        res += 1

    print(res - 1)

solve()