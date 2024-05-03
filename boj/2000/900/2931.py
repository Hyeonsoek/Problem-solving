from collections import deque

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

way = {
        '|': [0, 1],
        '-': [2, 3],
        '+': [0, 1, 2, 3],
        '1': [1, 3], '2': [0, 3],
        '3': [0, 2], '4': [1, 2],
        'M': [0, 1, 2, 3],
        'Z': [0, 1, 2, 3]
       }

def find_load():
    check = [[[] for _ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] == '.':
                continue
            elif board[y][x] in ['M', 'Z']:
                entrance = False
                for d in way[board[y][x]]:
                    yd, xd = dir_[d]
                    yy = y + yd
                    xx = x + xd
                    if 0 <= yy < r and 0 <= xx < c:
                        if board[yy][xx] != '.':
                            entrance = True
                            break
                if entrance:
                    continue

                for d in way[board[y][x]]:
                    yd, xd = dir_[d]
                    yy = y + yd
                    xx = x + xd
                    if 0 <= yy < r and 0 <= xx < c:
                        if board[yy][xx] == '.':
                            check[yy][xx].append((y, x))
            else:
                for d in way[board[y][x]]:
                    yd, xd = dir_[d]
                    yy = y + yd
                    xx = x + xd
                    if 0 <= yy < r and 0 <= xx < c:
                        if board[yy][xx] == '.':
                            check[yy][xx].append((y, x))

    for y in range(r):
        for x in range(c):
            if len(check[y][x]) >= 2:
                temp = []
                for cy, cx in check[y][x]:
                    for d in range(4):
                        yd, xd = dir_[d]
                        yy, xx = y + yd, x + xd
                        if (yy, xx) == (cy, cx):
                            temp.append(d)
                            break
                temp.sort()
                for key in way:
                    if temp == way[key]:
                        return y+1, x+1, key

    return


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

print(*find_load())