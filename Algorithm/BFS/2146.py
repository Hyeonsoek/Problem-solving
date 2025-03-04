import sys
from collections import deque
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [ list(map(int, input().split())) for _ in range(n) ]

    groups = []
    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                group = [(y, x)]
                queue = deque([(y, x)])

                board[y][x] = -1

                while queue:
                    sy, sx = queue.popleft()

                    for i in range(4):
                        yy, xx = DRY[i] + sy, DRX[i] + sx
                        if 0 <= yy < n and 0 <= xx < n and board[yy][xx] > 0:
                            board[yy][xx] = -1
                            group.append((yy, xx))
                            queue.append((yy, xx))

                groups.append(group)

    result = 300
    m = len(groups)   
    for front in range(m - 1):
        for end in range(front + 1, m):
            for fy, fx in groups[front]:
                for ey, ex in groups[end]:
                    target = abs(fy - ey) + abs(fx - ex) - 1
                    result = min(result, target)
                    if result == 1:
                        print(1)
                        return

    print(result)

solve()