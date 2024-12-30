from collections import defaultdict
n, m = map(int, input().split())

data = defaultdict(int)
for i in range(n):
    k = int(input())
    for j in map(int, input().split()):
        data[j] += 1

count = 0
for value in data.values():
    if value >= m:
        count += 1

print(count)