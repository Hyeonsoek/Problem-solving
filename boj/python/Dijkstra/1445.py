import heapq
import sys
MAX = 10000
dirr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
input = sys.stdin.readline

class Node:
    def __init__(self, trash=MAX, near=MAX):
        self.trash = trash
        self.near = near

    def is_next(self, trash, near):
        if trash < self.trash:
            return True
        if trash == self.trash:
            return self.near > near

        return False

    def set(self, trash, near):
        self.trash = trash
        self.near = near

def solve():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    sx, sy = -1, -1
    ex, ey = -1, -1
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'g':
                for dx, dy in dirr:
                    xx = dx + x
                    yy = dy + y
                    if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == '.':
                        board[xx][yy] = 'w'
            if board[x][y] == 'F':
                ex, ey = x, y
            if board[x][y] == 'S':
                sx, sy = x, y

    queue = [(0, 0, sx, sy)]
    visited = [[Node() for _ in range(m)] for _ in range(n)]
    visited[sx][sy].set(0, 0)

    while queue:
        trash, near, x, y = heapq.heappop(queue)

        if visited[x][y].trash < trash:
            continue

        for dx, dy in dirr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '.' and visited[nx][ny].is_next(trash, near):
                    visited[nx][ny].set(trash, near)
                    heapq.heappush(queue, (trash, near, nx, ny))

                if board[nx][ny] == 'w' and visited[nx][ny].is_next(trash, near + 1):
                    visited[nx][ny].set(trash, near + 1)
                    heapq.heappush(queue, (trash, near + 1, nx, ny))

                if board[nx][ny] == 'g' and visited[nx][ny].is_next(trash + 1, near):
                    visited[nx][ny].set(trash + 1, near)
                    heapq.heappush(queue, (trash + 1, near, nx, ny))

    result = visited[ex][ey]
    for dx, dy in dirr:
        nx, ny = ex + dx, ey + dy
        node = visited[nx][ny]
        if 0 <= nx < n and 0 <= ny < m and result.is_next(node.trash, node.near):
            result = node

    return result

v = solve()
print(v.trash, v.near)