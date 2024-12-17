from sys import stdin

input = stdin.readline
dirr = [[-1, 0], [1, 0], [0, 1], [0, -1]]
opposite = {1: 2, 2: 1, 3: 4, 4: 3}

r, c, m = map(int, input().split())
shark = {}

for _ in range(m):
    rr, cc, s, d, z = map(int, input().split())
    s %= ((r-1)*2) if d <= 2 else ((c-1)*2)
    shark[(rr, cc)] = [s, d, z]

def move_shark():
    global shark
    new_shark = {}

    for key in shark:
        s, d, z = shark[key]
        y, x = key

        yy = y + dirr[d-1][0] * s
        xx = x + dirr[d-1][1] * s
        while yy > r or yy < 1:
            if yy > r:
                yy -= abs(yy-r)*2
            else:
                yy += abs(1-yy)*2
            d = opposite[d]

        while xx > c or xx < 1:
            if xx > c:
                xx -= abs(xx-c)*2
            else:
                xx += abs(1-xx)*2
            d = opposite[d]

        if (yy, xx) in new_shark:
            if z > new_shark[(yy, xx)][2]:
                new_shark[(yy, xx)] = [s, d, z]
        else:
            new_shark[(yy, xx)] = [s, d, z]

    shark = new_shark


answer = 0
for i in range(1, c + 1):
    for j in range(1, r + 1):
        if (j, i) in shark:
            answer += shark[(j, i)][2]
            del shark[(j, i)]
            break
    move_shark()

print(answer)