def solve():
    n, k = map(int, input().split())
    
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        count = (n - mid + 1) * (mid + 1)
        
        if count < k:
            low = mid + 1
        elif count == k:
            return "YES"
        else:
            high = mid - 1
    
    return "NO"

print(solve())