from collections import deque
dirr = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

count = 0
for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            visited[x][y] = True
            queue = deque([(x, y)])

            is_peaks = True

            while queue:
                sx, sy = queue.popleft()

                for dx, dy in dirr:
                    xx = sx + dx
                    yy = sy + dy
                    if 0 <= xx < n and 0 <= yy < m:
                        if not visited[xx][yy] and board[xx][yy] == board[x][y]:
                            visited[xx][yy] = True
                            queue.append((xx, yy))

                        is_peaks &= board[xx][yy] <= board[x][y]

            count += 1 if is_peaks else 0

print(count)