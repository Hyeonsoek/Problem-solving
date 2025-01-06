n = int(input())
arr = list(map(int, input().split()))
k = int(input())

low, high = 1, max(arr)
while low <= high:
    mid = (low + high) // 2
    
    value = 0
    for x in range(n):
        value += min(arr[x], mid)

    if value <= k:
        low = mid + 1
    else:
        high = mid - 1
    
print(high)