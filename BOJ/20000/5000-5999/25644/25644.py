n = int(input())
arr = list(map(int, input().split()))

result = 0
minValue = arr[0]
for x in range(1, n):
    if minValue > arr[x]:
        minValue = arr[x]
    
    result = max(result, arr[x] - minValue)

print(result)