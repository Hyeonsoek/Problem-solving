n = int(input())
k = int(input())

low, high = 1, min(10 ** 9, n ** 2)

while low <= high:
    mid = (low + high) // 2
    
    idx = 0
    for i in range(1, n+1):
        value = min(n, mid // i)
        idx += value
    
    if idx >= k:
        high = mid - 1
    else:
        low = mid + 1
        
print(low)