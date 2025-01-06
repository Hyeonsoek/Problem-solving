import math

num = int(input())
cache = [ x for x in range(num + 1) ]

for i in range(1, num + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        cache[i] = min(cache[i], cache[i - j * j] + 1)

print(cache[num])