import sys
input = sys.stdin.readline
CANNOT = "blobsad"

def solve():
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]
    
    if sum(arr) % k != 0:
        return CANNOT
    
    result = 0
    prefix = 0
    start = 0
    for x in range(n):
        prefix += arr[x]
        if prefix >= k:
            prefix %= k
            pivot = 0
            center = 0
            for xx in range(start, x + 1):
                pivot += arr[xx]
                if pivot >= k / 2:
                    center = xx
                    break
        
            kk = k
            for xx in range(start, x + 1):
                result += abs(center - xx) * min(kk, arr[xx])
                kk -= min(kk, arr[xx])
                
            arr[x] = prefix
            start = x
    
    return result

print(solve())