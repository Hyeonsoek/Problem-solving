from sys import stdin
from collections import defaultdict

n = int(input())
array = []
d = defaultdict(int)
s = 0
for _ in range(n):
    value = int(stdin.readline())
    array.append(value)
    d[value] += 1
    s += value

print(round((s/n)))

array.sort()
print(array[n//2])

rd = defaultdict(list)
for k, v in d.items():
    rd[v].append(k)
for k in rd:
    rd[k] = sorted(rd[k])
t = rd[sorted(d.values())[-1]]

print(t[1]) if len(t) > 1 else print(t[0])
print(array[-1] - array[0])