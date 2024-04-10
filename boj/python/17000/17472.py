from sys import stdin
from collections import deque

MAX = 987654321
dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find_area(n, m, board):
    value = 0
    blocks = []
    check = [[0] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if board[y][x] and not check[y][x]:
                value += 1

                q = deque()
                block = []

                check[y][x] = value
                q.append((y, x))

                while q:
                    sy, sx = q.popleft()

                    block.append((sy, sx))

                    for yd, xd in dir_:
                        yy = yd + sy
                        xx = xd + sx
                        if 0 <= yy < n and 0 <= xx < m and not check[yy][xx] and board[yy][xx]:
                            check[yy][xx] = value
                            q.append((yy, xx))

                blocks.append(block)

    return value, blocks, check


def distance(n, m, value, blocks, check):
    result = []

    for a in range(value):
        for b in range(value):
            if a != b:
                min_cost = MAX
                for sy, sx in blocks[a]:
                    q = deque()

                    for nd in range(4):
                        q.append((nd, 0, sy, sx))

                    while q:
                        d, cost, y, x = q.popleft()

                        yy, xx = y + dir_[d][0], x + dir_[d][1]

                        if 0 <= yy < n and 0 <= xx < m:
                            if check[yy][xx] == 0:
                                q.append((d, cost+1, yy, xx))
                            elif check[yy][xx] == b+1:
                                if 2 <= cost < min_cost:
                                    min_cost = cost
                                break

                if min_cost != MAX:
                    if (b+1, a+1, min_cost) not in result:
                        result.append((a+1, b+1, min_cost))

    return result, value

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return False

    parent[u] = v
    return True


N, M = map(int, input().split())
BOARD = [list(map(int, stdin.readline().split())) for _ in range(N)]

graph, cluster = distance(N, M, *find_area(N, M, BOARD))
parent = [x for x in range(cluster+1)]
graph.sort(key=lambda x: x[2])

count = 0
answer = 0
for a, b, cost in graph:
    if merge(a, b):
        answer += cost
        count += 1

if count == cluster-1:
    print(answer if answer else -1)
else:
    print(-1)