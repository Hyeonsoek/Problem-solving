def solve(n, k):
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    cache = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)] # left, right, no
    
    if k > 0:
        cache[0][1][0] = arr[0][1]
        cache[0][1][1] = arr[0][0]
    cache[0][0][2] = sum(arr[0])
    
    for x in range(1, n):
        left, right = arr[x]
        for c in range(k + 1):
            if c > 0:
                cache[x][c][0] = max(cache[x-1][c-1][2], cache[x-1][c-1][0]) + right
                cache[x][c][1] = max(cache[x-1][c-1][2], cache[x-1][c-1][1]) + left
                
            if x + 1 > c:
                cache[x][c][2] = max(cache[x-1][c]) + left + right
            
    return max(cache[n-1][k])

n, k = map(int, input().split())
print(solve(n, k))

input()