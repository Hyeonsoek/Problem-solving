n = int(input())
array = [*map(int, input().split())]
cache1 = [0] + [1] * n + [0]
cache2 = [0] + [1] * n + [0]

for x in range(1, n):
    lis = 0
    rlis = 0
    for y in range(x):
        if array[x] > array[y] and lis < cache1[y + 1]:
            lis = cache1[y + 1]
        if array[n - x - 1] > array[n - y - 1] and rlis < cache2[n - y]:
            rlis = cache2[n - y]
    
    cache1[x + 1] = lis + 1
    cache2[n - x] = rlis + 1
    
result = 1
for x in range(n + 1):
    value = 0
    for y in range(x + 1, n):
        if array[x] > array[y]:
            value = max(value, cache2[y + 1])
    if value > 0:
        result = max(result, cache1[x + 1] + value)
print(result)