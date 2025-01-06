import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = [0, *map(int, input().split())]
    
    for x in range(1, n + 1):
        arr[x] += arr[x-1]
    
    result = -100 * n
    for x in range(k, n + 1):
        result = max(result, arr[x] - arr[x-k])
    
    return result

print(solve())