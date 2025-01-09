n = int(input())
arr = list(map(int, input().split()))

result = []
value = 0
valueMin = 10 ** 9
for x in range(n):
    valueMin = min(valueMin, arr[x])
    value = max(value, arr[x] - valueMin)
    result.append(value)

print(*result)