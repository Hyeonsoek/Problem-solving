import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    
    result = 0
    current = 0
    l, r = 0, 0
    while l <= r < n:
        if current <= m:
            result = max(result, current)
            current += arr[r]
            r += 1
        else:
            current -= arr[l]
            l += 1

    if current <= m:
        result = max(result, current)
    print(result)

solve()