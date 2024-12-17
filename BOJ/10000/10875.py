from sys import stdin

def ccw(a, b, c):
    ay, ax, _ = a
    by, bx, _ = b
    cy, cx, _ = c

    op = (bx - ax) * (cy - ay)
    op -= (by - ay) * (cx - ax)

    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1


def is_intersect(x, y):
    a, b = x
    c, d = y
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    aa = (a[0], a[1])
    bb = (b[0], b[1])
    cc = (c[0], c[1])
    dd = (d[0], d[1])
    if ab == 0 and cd == 0:
        if aa > bb:
            aa, bb = bb, aa
        if cc > dd:
            cc, dd = dd, cc
        return cc <= bb and aa <= dd

    return ab <= 0 and cd <= 0


MAX = 987654321
dir_dict = {'R': {3: 0, 0: 2, 2: 1, 1: 3}, 'L': {3: 1, 1: 2, 2: 0, 0: 3}}
dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

L = int(input())
N = int(input())
lines = [(0, 0, 3)]
squares = []

time = 0
dead = False

for i in range(N):
    s, direction = stdin.readline().split()
    ly, lx, dnd = lines[-1]
    dy, dx = dir_[dnd]
    ny, nx = ly + dy * int(s), lx + dx * int(s)

    lines.append((ny, nx, dir_dict[direction][dnd]))
    squares.append(int(s))

yy, xx, dnd = lines[-1]
dy, dx = dir_[dnd]

if dy == 0:
    lines.append((yy, dx * (L + 1), dnd))
    squares.append(abs(dx * (L + 1) - xx))
else:
    lines.append((dy * (L + 1), xx, dnd))
    squares.append(abs(dy * (L + 1) - yy))

for i in range(N + 1):
    ny, nx, dnd = lines[i]

    if dead:
        continue

    min_value = MAX
    xx = lines[i:i + 2]
    for j in range(i + 1):
        if j in [i, i + 1] or j + 1 in [i, i + 1]:
            continue

        yy = lines[j:j + 2]
        if len(yy) == 2 and is_intersect(xx, yy):
            txx = xx[0][0] if xx[0][0] == xx[1][0] else xx[0][1]
            tyy = yy[0][0] if yy[0][0] == yy[1][0] else yy[0][1]

            if xx[0][0] == xx[1][0]:
                tyy, txx = txx, tyy

            ty, tx, _ = xx[0]
            min_value = min(min_value, abs(tyy - ty) + abs(txx - tx))

    if min_value != MAX:
        dead = True
        time += min_value

    if not dead:
        if abs(lines[i+1][0]) > L or abs(lines[i+1][1]) > L:
            if abs(lines[i+1][0]) > L:
                time += squares[i] - abs(lines[i+1][0]) + L + 1
            else:
                time += squares[i] - abs(lines[i+1][1]) + L + 1
            dead = True
        else:
            time += squares[i]

print(time)