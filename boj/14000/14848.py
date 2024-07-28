from math import lcm
from itertools import *

n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ban = [0] * k
compressed = set()
for x in range(k):
    if not ban[x]:
        compressed.add(arr[x])
        for y in range(x + 1, k):
            if arr[y] % arr[x] == 0:
                ban[y] = 1

result = 0
for x in range(1, len(compressed) + 1):
    for comb in combinations(compressed, x):
        l = lcm(*comb)
        result += (1 if x & 1 else -1) * (n // l)

print(n - result)