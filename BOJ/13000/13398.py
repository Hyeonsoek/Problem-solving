MAX = 10 ** 10

n = int(input())
arr = list(map(int, input().split()))
    
cache = [[-MAX] * 2 for _ in range(n + 1)]
for x in range(1, n + 1):
    cache[x][0] = max(cache[x-1][0] + arr[x-1], arr[x-1])
    cache[x][1] = max(cache[x-1][1] + arr[x-1], cache[x-1][0])

result = -(10 ** 10)
for x in range(1, n + 1):
    result = max(result, max(cache[x]))

print(result)