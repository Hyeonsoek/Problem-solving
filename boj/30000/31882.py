import re

n = int(input())
arr = input()

cache = [0] * (n + 1)
for x in range(1, n + 1):
    cache[x] = cache[x-1] + x * (x + 1) // 2

result = 0
values = re.findall(r'[2]+', arr)
for x in values:
    result += cache[len(x)]

print(result)