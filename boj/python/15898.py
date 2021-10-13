from itertools import permutations, combinations, product

def rotate_block(idx, count):
    if count == 0:
        return number[idx], color[idx]

    value = [[0] * 4 for _ in range(4)]
    r_color = [['W'] * 4 for _ in range(4)]

    for y in range(4):
        for x in range(4):
            if count == 1:
                value[x][3-y] = number[idx][y][x]
                r_color[x][3-y] = color[idx][y][x]
            elif count == 2:
                value[3-y][3-x] = number[idx][y][x]
                r_color[3-y][3-x] = color[idx][y][x]
            else:
                value[3-x][y] = number[idx][y][x]
                r_color[3-x][y] = color[idx][y][x]

    return value, r_color

def quality(count_color):
    return 7 * count_color['R'] +\
            5 * count_color['B'] +\
            3 * count_color['G'] +\
            2 * count_color['Y']

def alchemy(order, rotate, start):

    count_color = {'W': 0, 'R': 0, 'B': 0, 'G': 0, 'Y': 0}
    board = [[0] * 5 for _ in range(5)]
    board_color = [['W'] * 5 for _ in range(5)]

    for idx, count, loc in zip(order, rotate, start):
        value, c_color = rotate_block(idx, count)

        sy, sx = loc

        for y in range(4):
            for x in range(4):
                board[y + sy][x + sx] += value[y][x]
                if board[y + sy][x + sx] < 0:
                    board[y + sy][x + sx] = 0
                elif board[y + sy][x + sx] > 9:
                    board[y + sy][x + sx] = 9

                if c_color[y][x] != 'W':
                    board_color[y + sy][x + sx] = c_color[y][x]

    for y in range(5):
        for x in range(5):
            count_color[board_color[y][x]] += board[y][x]

    return quality(count_color)


n = int(input())
color = []
number = []

for _ in range(4):
    b = [list(map(int, input().split())) for _ in range(4)]
    c = [list(input().split()) for _ in range(4)]

    number.append(b)
    color.append(c)

answer = 0
starts = [[0, 0], [0, 1], [1, 0], [1, 1]]

comb_idx = list(permutations(range(4), 3))
rot_cnt = list(product(range(n), repeat=3))
starts_loc = list(product(starts, repeat=3))

for c in comb_idx:
    for r in rot_cnt:
        for s in starts_loc:
            answer = max(answer, alchemy(c, r, s))

print(answer)