blue = [['0'] * 6 for _ in range(4)]
green = [['0'] * 6 for _ in range(4)]

def put_green(y, t):
    global green

    line_str = ''.join(green[y])
    find_idx = line_str.find('1')
    if t == 1:
        if find_idx == -1:
            green[y][5] = '1'
        else:
            green[y][find_idx - 1] = '1'
    elif t == 2:
        line_str1 = ''.join(green[y + 1])
        find_idx1 = line_str1.find('1')

        if find_idx1 == -1 and find_idx == -1:
            green[y + 1][5] = '1'
            green[y][5] = '1'
        elif find_idx1 == -1 and find_idx != -1:
            green[y + 1][find_idx - 1] = '1'
            green[y][find_idx - 1] = '1'
        elif find_idx1 != -1 and find_idx == -1:
            green[y + 1][find_idx1 - 1] = '1'
            green[y][find_idx1 - 1] = '1'
        else:
            if find_idx1 > find_idx:
                green[y + 1][find_idx - 1] = '1'
                green[y][find_idx - 1] = '1'
            else:
                green[y + 1][find_idx1 - 1] = '1'
                green[y][find_idx1 - 1] = '1'
    else:
        if find_idx == -1:
            green[y][4] = '1'
            green[y][5] = '1'
        else:
            green[y][find_idx - 1] = '1'
            green[y][find_idx - 2] = '1'

def put_blue(x, t):
    global blue

    line_str = ''.join(blue[x])
    find_idx = line_str.find('1')
    if t == 1:
        if find_idx == -1:
            blue[x][5] = '1'
        else:
            blue[x][find_idx - 1] = '1'
    elif t == 2:
        if find_idx == -1:
            blue[x][4] = '1'
            blue[x][5] = '1'
        else:
            blue[x][find_idx - 1] = '1'
            blue[x][find_idx - 2] = '1'
    else:
        line_str1 = ''.join(blue[x + 1])
        find_idx1 = line_str1.find('1')

        if find_idx1 == -1 and find_idx == -1:
            blue[x + 1][5] = '1'
            blue[x][5] = '1'
        elif find_idx1 == -1 and find_idx != -1:
            blue[x + 1][find_idx - 1] = '1'
            blue[x][find_idx - 1] = '1'
        elif find_idx1 != -1 and find_idx == -1:
            blue[x + 1][find_idx1 - 1] = '1'
            blue[x][find_idx1 - 1] = '1'
        else:
            if find_idx1 > find_idx:
                blue[x + 1][find_idx - 1] = '1'
                blue[x][find_idx - 1] = '1'
            else:
                blue[x + 1][find_idx1 - 1] = '1'
                blue[x][find_idx1 - 1] = '1'

def clear_line(bg):
    global blue, green

    clears = []
    board = blue if bg else green

    for y in range(6):
        line = 0
        for x in range(4):
            line += 1 if board[x][y] == '1' else 0

        if line == 4:
            clears.append(y)

    if clears:
        for c in clears:
            for x in range(4):
                board[x] = board[x][:c] + board[x][c+1:]
                board[x].insert(0, '0')
        return len(clears)
    return 0

def is_special(board):
    for y in range(2):
        for x in range(4):
            if board[x][y] == '1':
                return True, y
    return False, -1

def line_shift(bg):
    global blue, green

    board = blue if bg else green

    _is_special, count = is_special(board)

    if _is_special:
        count = 2 - count
        for c in range(count):
            for x in range(4):
                board[x] = board[x][:-1]
                board[x].insert(0, '0')


def monominodomino(t, x, y):
    global blue, green
    clear = 0

    # blue part
    put_blue(x, t)
    clear += clear_line(True)
    line_shift(True)

    # green in
    put_green(y, t)
    clear += clear_line(False)
    line_shift(False)

    return clear


score = 0

n = int(input())
for _ in range(n):
    tt, xx, yy = map(int, input().split())
    score += monominodomino(tt, xx, yy)

    # print("----blue----")
    # for x in blue:
    #     print(*x)
    #
    # print("----green---")
    # for x in green:
    #     print(*x)
    #
    # print()

block = 0
for x in range(4):
    block += sum(map(int, blue[x]))
    block += sum(map(int, green[x]))

print(score)
print(block)