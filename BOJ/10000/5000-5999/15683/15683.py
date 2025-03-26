from collections import defaultdict

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def findcctv():
    cctv = []
    for y in range(n):
        for x in range(m):
            if 1 <= board[y][x] <= 5:
                cctv.append((y, x))
    return cctv

def straight(y, x, i):
    global visiable

    in_range = [range(y - 1, -1, -1), range(x + 1, m),
                range(y + 1, n), range(x - 1, -1, -1)]

    if i in [0, 2]:
        for yy in in_range[i]:
            if board[yy][x] == 6:
                break
            if 1 <= board[yy][x] <= 5:
                continue
            visiable[(yy, x)] += 1
    else:
        for xx in in_range[i]:
            if board[y][xx] == 6:
                break
            if 1 <= board[y][xx] <= 5:
                continue
            visiable[(y, xx)] += 1

def delete_loc(y, x, i):
    global visiable

    in_range = [range(y - 1, -1, -1), range(x + 1, m),
                range(y + 1, n), range(x - 1, -1, -1)]

    if i in [0, 2]:
        for yy in in_range[i]:
            if board[yy][x] == 6:
                break
            if visiable[(yy, x)] > 0:
                visiable[(yy, x)] -= 1
    else:
        for xx in in_range[i]:
            if board[y][xx] == 6:
                break
            if visiable[(y, xx)] > 0:
                visiable[(y, xx)] -= 1

def brutefoce(idx):
    global answer, visiable

    if idx == len(cctv):
        count = 0
        for y in range(n):
            for x in range(m):
                if board[y][x] > 0 or visiable[(y, x)] > 0:
                    continue
                if board[y][x] == 0:
                    count += 1
        if count < answer:
            answer = count
    else:
        y, x = cctv[idx]

        array = None
        if board[y][x] == 1:
            array = [[i] for i in range(4)]
        elif board[y][x] == 2:
            array = [[0, 2], [1, 3]]
        elif board[y][x] == 3:
            array = [[0, 1], [1, 2], [2, 3], [3, 0]]
        elif board[y][x] == 4:
            array = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
        else:
            array = [[0, 1, 2, 3]]

        for cnt in array:
            [straight(y, x, i) for i in cnt]
            brutefoce(idx+1)
            [delete_loc(y, x, i) for i in cnt]

visiable = defaultdict(int)

answer = m*n
cctv = findcctv()
brutefoce(0)
print(answer)