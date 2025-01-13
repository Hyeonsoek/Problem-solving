import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    k = int(input())
    
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + arr[i])
    
    split = []
    for i in range(k, n + 1):
        split.append(prefix[i] - prefix[i - k])
    
    cache = [[0] * (n + 1) for _ in range(4)]
        
    for i in range(1, 4):
        for j in range(k * i, n + 1):
            cache[i][j] = max(cache[i][j-1], cache[i - 1][j - k] + split[j - k])
    
    print(cache[3][n])

solve()