import sys
sys.setrecursionlimit(2000000)

def solve():
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    
    cache = [[-1] * (m + 2) for _ in range(n + 1)]
    
    def dynamic(i, v):
        if i == n:
            return 0
        
        if cache[i][v] != -1:
            return cache[i][v]
        
        res = dynamic(i + 1, arr[i] + 1) + (m - v + 1) ** 2
        if v + arr[i] <= m:
            res = min(res, dynamic(i + 1, v + arr[i] + 1))
        
        cache[i][v] = res
        return res
    
    print(dynamic(0, 0))

solve()