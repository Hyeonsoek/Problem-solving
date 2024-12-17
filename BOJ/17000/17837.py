import collections
from sys import stdin

input = stdin.readline
dirr = [[0, 1], [0, -1], [-1, 0], [1, 0]]
opposite = {0: 1, 1: 0, 2: 3, 3: 2}

def simulate():
    global board, horse, board_horse, n, k

    for i in range(k):
        r, c, d = horse[i]
        ydir, xdir = dirr[d]
        rr, cc = r + ydir, c + xdir

        state = board_horse[(r, c)].copy()
        state = state[state.index(i):]

        if 0 <= rr < n and 0 <= cc < n:
            if board[rr][cc] == 0:
                for x in state:
                    board_horse[(rr, cc)].append(x)
                    board_horse[(r, c)].remove(x)
                    horse[x] = [rr, cc, horse[x][2]]
            elif board[rr][cc] == 1:
                for x in state[::-1]:
                    board_horse[(rr, cc)].append(x)
                    board_horse[(r, c)].remove(x)
                    horse[x] = [rr, cc, horse[x][2]]
            else:
                d = opposite[d]
                ydir, xdir = dirr[d]
                rr, cc = r + ydir, c + xdir

                if 0 <= rr < n and 0 <= cc < n:
                    if board[rr][cc] == 0:
                        for x in state:
                            board_horse[(rr, cc)].append(x)
                            board_horse[(r, c)].remove(x)
                            horse[x] = [rr, cc, horse[x][2]]
                        horse[i] = [rr, cc, d]
                    elif board[rr][cc] == 1:
                        for x in state[::-1]:
                            board_horse[(rr, cc)].append(x)
                            board_horse[(r, c)].remove(x)
                            horse[x] = [rr, cc, horse[x][2]]
                        horse[i] = [rr, cc, d]
                    else:
                        horse[i] = [r, c, d]
                else:
                    horse[i] = [r, c, d]
        else:
            d = opposite[d]
            ydir, xdir = dirr[d]
            rr, cc = r + ydir, c + xdir

            if 0 <= rr < n and 0 <= cc < n:
                if board[rr][cc] == 0:
                    for x in state:
                        board_horse[(rr, cc)].append(x)
                        board_horse[(r, c)].remove(x)
                        horse[x] = [rr, cc, horse[x][2]]
                    horse[i] = [rr, cc, d]
                elif board[rr][cc] == 1:
                    for x in state[::-1]:
                        board_horse[(rr, cc)].append(x)
                        board_horse[(r, c)].remove(x)
                        horse[x] = [rr, cc, horse[x][2]]
                    horse[i] = [rr, cc, d]
                else:
                    horse[i] = [r, c, d]
            else:
                horse[i] = [r, c, d]

        for y, x, _ in horse:
            key = y, x
            if len(board_horse[key]) >= 4:
                return True
    return False

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_horse = collections.defaultdict(list)
horse = []

for i in range(k):
    r, c, d = map(int, input().split())
    horse.append([r-1, c-1, d-1])
    board_horse[(r-1, c-1)].append(i)

answer = 1
while answer <= 1000:
    if simulate():
        print(answer)
        exit()
    answer += 1

print(-1)