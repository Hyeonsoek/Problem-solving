def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    cache = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                cache[i] = max(cache[i], cache[j] + 1)
    
    print(n - max(cache))

solve()