import sys
from bisect import *
from collections import defaultdict
input = sys.stdin.readline

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

n, m = map(int, input().split())

linear = defaultdict(list)
for _ in range(n):
    fx, fy = map(int, input().split())
    
    if fy == 0:
        isMinus = '-1' if fx < 0 else '1'
        key = isMinus + 'x'
        linear[key].append(fx * int(isMinus))
    elif fx == 0:
        isMinus = '-1' if fy < 0 else '1'
        key = isMinus + 'y'
        linear[key].append(fy * int(isMinus))
    else:
        key = (quadrant(fx, fy), fy / fx)
        linear[key].append(fx * (-1 if fx < 0 else 1))
        
for key in linear:
    linear[key].sort()

result = 0
for _ in range(m):
    ex, ey = map(int, input().split())
    if ey == 0:
        isMinus = '-1' if ex < 0 else '1'
        key = isMinus + 'x'
        target = bisect_right(linear[key], ex * int(isMinus))
    elif ex == 0:
        isMinus = '-1' if ey < 0 else '1'
        key = isMinus + 'y'
        target = bisect_right(linear[key], ey * int(isMinus))
    else:
        key = (quadrant(ex, ey), ey / ex)
        target = bisect_right(linear[key], ex * (-1 if ex < 0 else 1))
        
    result = max(result, target)
    
print(result)