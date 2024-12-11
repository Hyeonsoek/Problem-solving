def solve():
    n = int(input())
    m = int(input())
    arr = sorted([0] + [int(input()) for _ in range(m)] + [n + 1])
    
    cache = [0] * 41
    cache[0] = cache[1] = 1
    cache[2] = 2
    
    for i in range(3, 41):
        cache[i] = cache[i-2] + cache[i-1]
    
    result = 1
    for i in range(1, m + 2):
        result *= cache[arr[i] - arr[i-1] - 1]
    
    print(result)

solve()