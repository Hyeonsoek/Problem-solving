from collections import defaultdict

dirr = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def even_or_odd(arr):
    arr = list(map(lambda x: x%2==1, arr))
    return sum(arr) == 0 or sum(arr) == len(arr)

def move_fireball():
    global n, m, k, fireballs

    keys = fireballs.keys()

    for y, x in keys:
        if not fireballs[(y, x)]:
            continue

        m, d, s = fireballs[(y, x)][0]
        yy = (y + dirr[d-1][0] * s) % n
        xx = (x + dirr[d-1][1] * s) % n

        fireballs[(yy, xx)].append([m, d, s])

    keys = fireballs.keys()

    for y, x in keys:
        if len(fireballs[(y, x)]) > 1:
            m, s = 0, 0
            d = []
            for mm, dd, ss in fireballs[(y, x)]:
                m, s = m + mm, s + ss
                d.append(dd)
            start = 1 if even_or_odd(d) else 0
            m //= 5
            s = (s // len(fireballs[(y, x)])) % n

            for nd in range(start, 8, 2):
                yy = (y + dirr[nd-1][0] * s) % n
                xx = (x + dirr[nd-1][0] * s) % n




n, m, k = map(int, input().split())

fireballs = defaultdict(list)

for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs[(ri-1, ci-1)].append([mi, si % n, di])

move_fireball()

# for _ in range(k):
#     move_fireball()
#
# print(sum(map(sum, board)))