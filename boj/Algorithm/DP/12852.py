MAX = 10000000

n = int(input())
cache = [0, 0, *[MAX] * (n + 1)]

for x in range(2, n + 1):
    if x % 2 == 0:
        cache[x] = min(min(cache[x - 1], cache[x // 2]) + 1, cache[x])
    if x % 3 == 0:
        cache[x] = min(min(cache[x - 1], cache[x // 3]) + 1, cache[x])
        
    cache[x] = min(cache[x - 1] + 1, cache[x])

value = n
result = []
for _ in range(cache[n] + 1):
    result.append(value)
    nvalue = cache[value - 1]
    if value % 3 == 0:
        nvalue = min(nvalue, cache[value // 3])
    if value % 2 == 0:
        nvalue = min(nvalue, cache[value // 2])
    
    if (value % 3 == 0) and nvalue == cache[value // 3]:
        value //= 3
    elif (value % 2 == 0) and nvalue == cache[value // 2]:
        value //= 2
    else:
        value -= 1

print(cache[n])
print(*result)