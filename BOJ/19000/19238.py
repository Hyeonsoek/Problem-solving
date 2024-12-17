import sys
from collections import deque

input = sys.stdin.readline
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(sy, sx):
    global board, n, m

    q = deque()
    check = [[-1] * n for _ in range(n)]

    q.append([0, sy, sx])  # cost, coordinate
    check[sy][sx] = 0

    while q:
        cost, y, x = q.popleft()

        for ydir, xdir in dirr:
            yy = y + ydir
            xx = x + xdir
            if (0 <= yy < n) and (0 <= xx < n) \
                    and board[yy][xx] == 0 and check[yy][xx] == -1:
                check[yy][xx] = cost+1
                q.append([cost+1, yy, xx])

    return check

def start_tax():
    global n, m, fuel, taxi, passenger

    while fuel > 0 and len(passenger['start']) > 0:
        dist = bfs(*taxi)

        psg = []
        for i in range(len(passenger['start'])):
            y, x = passenger['start'][i]
            if dist[y][x] >= 0:
                psg.append([dist[y][x], y, x, i])

        if psg:
            psg.sort()

            cost, y, x, idx = psg[0]

            fuel -= cost
            taxi = (y, x)

            if fuel <= 0:
                return -1

            target = passenger['end'][idx]

            del passenger['end'][idx] # remove << 틀린 원흉
            del passenger['start'][idx]
        else:
            return -1

        dist = bfs(y, x)

        ty, tx = target
        if dist[ty][tx] == -1:
            return -1

        fuel -= dist[ty][tx]

        if fuel < 0:
            return -1

        taxi = target
        fuel += (dist[ty][tx] * 2)

    return fuel


n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
taxi = tuple(map(int, input().split()))
taxi = (taxi[0]-1, taxi[1]-1)

passenger = {'start': [], 'end': []}
for _ in range(m):
    sy, sx, ey, ex = map(int, input().split())
    start, end = (sy-1, sx-1), (ey-1, ex-1)
    passenger['start'].append(start)
    passenger['end'].append(end)

print(start_tax())