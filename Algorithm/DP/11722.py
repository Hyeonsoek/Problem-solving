n = int(input())
array = list(map(int, input().split()))
cache = [1] * n

for x in range(1, n):
    value = 0
    for y in range(x):
        if array[x] < array[y] and value < cache[y]:
            value = cache[y]
    cache[x] = value + 1

print(max(cache))