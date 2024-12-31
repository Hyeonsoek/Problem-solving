from math import *
n = int(input())
arr = [*map(int, input().split())]
t, p = map(int, input().split())

result = 0
for x in arr:
    result += ceil(x / t)

print(result)
print(n // p, n % p)