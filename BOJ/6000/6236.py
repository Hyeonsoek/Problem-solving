import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def decision(k):
    start = k
    count = 1
    
    for x in range(n):
        if k < arr[x]:
            return False
        
        if arr[x] <= start:
            start -= arr[x]
        else:
            start = k - arr[x]
            count += 1
    
    return count <= m

low, high = 0, 10 ** 10
while low <= high:
    mid = (low + high) // 2
    
    if decision(mid):
        high = mid - 1
    else:
        low = mid + 1
    
print(low)