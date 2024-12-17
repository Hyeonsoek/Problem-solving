import sys, collections
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]

    queue = collections.deque([(0, 0)])
    visited = [[False] * n for _ in range(m)]

    visited[0][0] = True

    while queue:
        nx, ny = queue.popleft()

        if nx == m-1 and ny == n-1:
            return "Yes"

        for xd, yd in [(1, 0), (0, 1)]:
            xx = xd + nx
            yy = yd + ny
            if 0 <= xx < m and 0 <= yy < n:
                if board[xx][yy] == 1 and not visited[xx][yy]:
                    queue.append((xx, yy))
                    visited[xx][yy] = True

    return "No"


print(solve())