import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def solve():
    n = int(input())
    i, j = map(int, input().split())
    m = int(input())
    doors = [int(input()) for _ in range(m)]
    
    cache = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(m)]
    
    def dynamic(i, j, k):
        if k >= m:
            return 0
        
        if cache[k][i][j] != -1:
            return cache[k][i][j]
        
        cache[k][i][j] = min(abs(doors[k] - i) + dynamic(doors[k], j, k + 1), abs(doors[k] - j) + dynamic(i, doors[k], k + 1))
        return cache[k][i][j]

    print(dynamic(i, j, 0))

solve()