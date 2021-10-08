from sys import stdin

input = lambda: map(int, stdin.readline().split())

def rotate(count, sticker):
    if count == 0:
        return sticker, r, c

    stk = None
    if count == 2:
        stk = [[0] * c for _ in range(r)]
    else:
        stk = [[0] * r for _ in range(c)]

    for y in range(r):
        for x in range(c):
            if count == 1:
                stk[x][r-y-1] = sticker[y][x]
            elif count == 2:
                stk[r-y-1][c-x-1] = sticker[y][x]
            else:
                stk[c-x-1][y] = sticker[y][x]

    rr, cc = (r, c) if count in [0, 2] else (c, r)

    return stk, rr, cc

def can_stick(sticker, by, bx, rr, cc):
    for y in range(rr):
        for x in range(cc):
            yy = by + y
            xx = bx + x
            if not (0 <= yy < n and 0 <= xx < m):
                return False
            if notebook[yy][xx] and sticker[y][x]:
                return False
    return True

def stick(sticker):
    for cnt in range(4):
        stk, rr, cc = rotate(cnt, sticker)
        for by in range(n):
            for bx in range(m):
                if can_stick(stk, by, bx, rr, cc):
                    for y in range(rr):
                        for x in range(cc):
                            if stk[y][x]:
                                notebook[by + y][bx + x] = stk[y][x]
                    return


n, m, k = input()
notebook = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = input()
    ski = [list(input()) for _ in range(r)]

    stick(ski)

print(sum(map(sum, notebook)))