from math import *

inputs = lambda : map(int, input().split())

n = int(input()) + 1
pos = sorted([ tuple(inputs()) for _ in range(n) ])
s, e = inputs()

start = 1
while pos[start][0] <= s:
    start += 1

bx, by = pos[start-1]
ex, ey = pos[start]

sylower = ex - bx
syupper = (ey - by) * (s - bx) + by * sylower

end = 1
while end < n - 1 and pos[end][0] <= e:
    end += 1

bx, by = pos[end-1]
ex, ey = pos[end]

eylower = ex - bx
eyupper = (ey - by) * (e - bx) + by * eylower

lower = eylower * sylower * (e - s)
upper = eyupper * sylower - eylower * syupper

_gcd = gcd(lower, upper)

lower, upper = lower // _gcd, abs(upper // _gcd)

print(upper if lower == 1 else f'{upper}/{lower}')