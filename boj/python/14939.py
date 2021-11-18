import copy
from itertools import product

MAX = 987654321

def push_button(y, x, board):

    for yd, xd in [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]]:
        yy = yd + y
        xx = xd + x
        if 0 <= yy < 10 and 0 <= xx < 10:
            board[yy][xx] ^= 1

    return board

def simulate(is_push, board):
    count = 0

    for i in range(10):
        if is_push[i]:
            count += 1
            board = push_button(0, i, board)

    for i in range(1, 10):
        for j in range(10):
            if board[i-1][j]:
                count += 1
                board = push_button(i, j, board)

    if not sum(map(sum, board)):
        return count
    else:
        return MAX


MIN = MAX
BOARD = [list(map(lambda x: 0 if x == '#' else 1, list(input()))) for _ in range(10)]
quest = list(product([0, 1], repeat=10))

for q in quest:
    MIN = min(MIN, simulate(q, copy.deepcopy(BOARD)))

print(MIN)