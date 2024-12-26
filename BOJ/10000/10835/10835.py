import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    left = [0, *map(int, reversed(input().split()))]
    right = [0, *map(int, reversed(input().split()))]
    
    cache = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if left[i] > right[j]:
                cache[i][j] = max(cache[i][j - 1] + right[j], cache[i - 1][j], cache[i - 1][j - 1])
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i - 1][j - 1])
    
    print(cache[n][n])

solve()