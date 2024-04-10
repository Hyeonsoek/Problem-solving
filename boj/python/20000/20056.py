import math
import copy
from collections import defaultdict

dirr = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def even_or_odd(arr):
    arr = list(map(lambda x: x % 2 == 1, arr))
    return sum(arr) == 0 or sum(arr) == len(arr)

def move_fireball():
    global n, m, k, fireballs

    items = copy.deepcopy(list(fireballs.items()))

    for key, fbs in items:
        y, x = key
        for fb in fbs[:]:
            m, s, d = fb
            yy = (y + dirr[d][0] * s) % n
            xx = (x + dirr[d][1] * s) % n

            fireballs[(yy, xx)].append([m, s, d])

        for fb in fbs[:]:
            fireballs[key].remove(fb)

        if not fireballs[key]:
            fireballs.pop(key)

    items = list(fireballs.items())

    for key, fb in items:
        y, x = key
        if len(fb) > 1:
            m, s, d = 0, 0, []
            for mm, ss, dd in fb:
                m, s = m + mm, s + ss
                d.append(dd)

            fireballs.pop((y, x))

            m = math.floor(m/5)
            s = math.floor(s/len(fb))
            start = 0 if even_or_odd(d) else 1

            if m == 0:
                continue

            for nd in range(start, 8, 2):
                fireballs[key].append([m, s, nd])


n, m, k = map(int, input().split())

fireballs = defaultdict(list)

for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs[(ri-1, ci-1)].append([mi, si, di])

for _ in range(k):
    move_fireball()

answer = 0
for value in fireballs.values():
    answer += sum(map(lambda x: x[0], value))

print(answer)