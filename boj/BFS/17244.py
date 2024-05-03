import sys
import collections
import heapq
dirr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
input = sys.stdin.readline

def bfs(board, coords, n, m):
    count = len(coords)
    graph = collections.defaultdict(list)
    for x, (sx, sy) in enumerate(coords):
        visited = [[100001] * n for _ in range(m)]
        visited[sx][sy] = 0

        queue = collections.deque([(sx, sy)])
        while queue:
            cx, cy = queue.popleft()

            for dx, dy in dirr:
                xx = dx + cx
                yy = dy + cy
                if 0 <= xx < m and 0 <= yy < n \
                        and visited[xx][yy] > visited[cx][cy] + 1 \
                        and board[xx][yy] != '#':
                    visited[xx][yy] = visited[cx][cy] + 1
                    queue.append((xx, yy))

        for y, (tx, ty) in enumerate(coords):
            graph[x].append((y, visited[tx][ty]))

    return graph

def solve():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(m)]

    start, end = -1, -1
    coords = []
    for x in range(m):
        for y in range(n):
            if board[x][y] not in '.#':
                coords.append((x, y))
                if board[x][y] == 'S':
                    start = len(coords)-1
                if board[x][y] == 'E':
                    end = len(coords)-1

    result = 100001
    graph = bfs(board, coords, n, m)
    queue = [(0, 1 << start, start)]
    while queue:
        cost, bits, index = heapq.heappop(queue)

        if index == end and bits == (1 << len(coords))-1:
            result = min(result, cost)
            continue

        for next, next_cost in graph[index]:
            if not (bits & (1 << next)):
                heapq.heappush(queue, (cost + next_cost, bits | (1 << next), next))

    print(result)

solve()