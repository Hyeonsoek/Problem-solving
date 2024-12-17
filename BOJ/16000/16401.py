import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    low, high = 1, max(arr)
    while low <= high:
        mid = (low + high) // 2
        
        count = 0
        for x in range(n):
            count += arr[x] // mid
            
        if count < m:
            high = mid - 1
        else:
            low = mid + 1
    
    print(low - 1)
    
solve()