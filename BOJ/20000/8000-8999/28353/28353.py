def solve():
    n, k = map(int, input().split())
    arr = sorted([*map(int, input().split())])
    
    result = 0
    start, end = 0, n - 1
    while start < end:
        t = arr[start] + arr[end]
        if t <= k:
            result += 1
            start += 1
            end -= 1
        elif t > k:
            end -= 1
    
    print(result)
    
solve()