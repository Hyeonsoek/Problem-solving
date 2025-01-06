from math import gcd

n = int(input())
nn = int(n ** .5) + 1

divisor = set()
for x in range(1, nn):
    if n % x == 0:
        divisor.add(x)
        divisor.add(n // x)

count = 0
for x in divisor:
    for xx in range(1, int((x + 1) / 2) + 1):
        if gcd(x + 1 - xx, xx) == 1:
            count += 1

print(count)