# try 15

from sys import stdin

dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
next_d = {3: 2, 2: 4, 4: 1, 1: 3}

def lining():
    ret = []
    count, d = 1, 3
    sy, sx = n//2, n//2
    while count <= n:
        for _ in range(2):
            for _ in range(count):
                sy += dirr[d-1][0]
                sx += dirr[d-1][1]
                if not (0 <= sy < n and 0 <= sx < n):
                    continue
                if board[sy][sx] == 0:
                    continue
                ret.append(board[sy][sx])
            d = next_d[d]
        count += 1

    return ret

def remove_zero(line):
    temp = []
    for x in line:
        if x > 0:
            temp.append(x)
    return temp

def marble_bomb(line):
    ret = 0

    while True:
        if not line:
            break

        bomb_count = 0
        count = 1
        value = line[0]
        for x in range(1, len(line)):
            if value == line[x]:
                count += 1
            else:
                if count >= 4:
                    bomb_count += 1
                    for y in range(x-count, x):
                        line[y] = 0
                    ret += value * count
                value = line[x]
                count = 1

        if count >= 4:
            bomb_count += 1
            for y in range(len(line)-count, len(line)):
                line[y] = 0
            ret += value * count

        line = remove_zero(line)

        if bomb_count == 0:
            break

    return ret, line

def marble_copy(line):
    if not line:
        return []
    ret = []

    a_list = []
    b_list = [line[0]]

    value = line[0]
    count = 1
    for x in range(1, len(line)):
        if value == line[x]:
            count += 1
        else:
            a_list.append(count)
            b_list.append(line[x])
            count = 1
            value = line[x]
    a_list.append(count)

    for x in range(len(a_list)):
        ret.append(a_list[x])
        ret.append(b_list[x])

    ret = ret[:(n*n)-1]

    return ret

def line_to_board(line):
    idx = 0
    count, d = 1, 3
    sy, sx = n//2, n//2

    while 0 <= sy < n and 0 <= sx < n:
        for _ in range(2):
            for _ in range(count):
                sy += dirr[d-1][0]
                sx += dirr[d-1][1]
                if 0 <= sy < n and 0 <= sx < n:
                    if idx < len(line):
                        board[sy][sx] = line[idx]
                    else:
                        board[sy][sx] = 0
                    idx += 1
            d = next_d[d]
        count += 1

def blizzard(d, s):
    global board, n, m

    sy, sx = n//2, n//2
    for k in range(s):
        sy += dirr[d-1][0]
        sx += dirr[d-1][1]
        board[sy][sx] = 0

    line = lining()
    answer, line = marble_bomb(line)
    line = marble_copy(line)
    line_to_board(line)

    return answer


input_test = lambda: map(int, stdin.readline().split())

n, m = input_test()
board = [list(input_test()) for _ in range(n)]
simulate = [list(input_test()) for _ in range(m)]

# print(line)

result = 0
for di, si in simulate:
    result += blizzard(di, si)

print(result)