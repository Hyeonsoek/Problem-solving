import sys
input = sys.stdin.readline

n = int(input())
arr = [float(input()) for _ in range(n)]

cache = arr[:]
for x in range(1, n):
    cache[x] = max(cache[x-1] * arr[x], cache[x])

print(f'{max(cache):.3f}')