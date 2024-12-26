def solve():
    n, m, k = map(int, input().split())
    
    if n == m:
        print(-1)
        return
    
    arr = [0] * n
    for i in range(k - 1):
        arr[i] = i + 1
    
    for i in range(k - 1, k + n - m - 1):
        arr[i] = n - i + k - 1
    
    for i in range(k + n - m - 1, n):
        arr[i] = i- (k + n - m - 1) + k
    
    print(*arr)

solve()