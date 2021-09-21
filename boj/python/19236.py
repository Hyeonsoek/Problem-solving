import copy

answer = -1
dirr = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

ccw = {i: i+1 for i in range(7)}
ccw[7] = 0

def can_move(board, y, x, d):
    for i in range(1, 4):
        dy, dx = y + dirr[d][0] * i, x + dirr[d][1] * i
        if 0 <= dy < 4 and 0 <= dx < 4 and board[dy][dx] != [-1, -1]:
            return True
    return False

def move_fish(board, fish, shark):

    for i in range(1, 17):
        if i in fish:
            y, x = fish[i]
            num, d = board[y][x]
            while True:
                dy, dx = y + dirr[d][0], x + dirr[d][1]
                if 0 <= dy < 4 and 0 <= dx < 4 and [dy, dx] != shark:
                    break
                else:
                    d = ccw[d]

            if board[dy][dx] != [-1, -1]:
                num2, d2 = board[dy][dx]
                fish[num], fish[num2] = fish[num2], fish[num]
                board[dy][dx], board[y][x] = [num, d], [num2, d2]
            else:
                fish[num] = (dy, dx)
                board[dy][dx], board[y][x] = [num, d], board[dy][dx]

def bruteforce(board, fish, shark, y, x, size, d):
    global answer

    move_fish(board, fish, shark)

    if can_move(board, y, x, d):
        for i in range(1, 4):
            dy, dx = y + dirr[d][0] * i, x + dirr[d][1] * i
            if 0 <= dy < 4 and 0 <= dx < 4 and board[dy][dx] != [-1, -1]:
                number, dd = board[dy][dx]

                change_board = copy.deepcopy(board)
                change_board[dy][dx] = [-1, -1]

                new_fish = {key: fish[key] for key in fish}
                new_fish.pop(number)

                bruteforce(change_board, new_fish, [dy, dx], dy, dx, size + number, dd)
    else:
        if answer < size:
            answer = size


f = {}
b = [[[0, 0] for _ in range(4)] for _ in range(4)]

for yy in range(4):
    inputs = list(map(int, input().split()))
    for xx in range(0, len(inputs), 2):
        b[yy][xx//2] = [inputs[xx], inputs[xx+1]-1]
        f[inputs[xx]] = (yy, xx//2)

n, dd = b[0][0]
f.pop(n)
b[0][0] = [-1, -1]

bruteforce(b, f, [0, 0], 0, 0, n, dd)

print(answer)