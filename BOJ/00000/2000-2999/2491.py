n = int(input())
arr = list(map(int, input().split()))

result = 1
cache = [1] * n
for x in range(1, n):
    if arr[x] >= arr[x - 1]:
        cache[x] += cache[x-1]

result = max(result, max(cache))
cache = [1] * n
for x in range(1, n):
    if arr[x] <= arr[x - 1]:
        cache[x] += cache[x-1]

print(max(result, max(cache)))