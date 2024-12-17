import sys, collections
input = sys.stdin.readline
dirr = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    count = 0
    result = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and board[x][y] == 1:
                area = 1
                count += 1
                queue = collections.deque([(x, y)])
                visited[x][y] = True

                while queue:
                    sx, sy = queue.popleft()

                    for dx, dy in dirr:
                        xx = dx + sx
                        yy = dy + sy
                        if (0 <= xx < n and 0 <= yy < m and
                                board[xx][yy] == 1 and not visited[xx][yy]):
                            visited[xx][yy] = True
                            area += 1
                            queue.append((xx, yy))

                result = max(result, area)

    print(count, result, sep='\n')

solve()