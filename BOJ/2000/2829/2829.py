import sys
input = sys.stdin.readline

def isinner(xx, yy, n):
    return 0 <= xx < n and 0 <= yy < n

def solve():
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n)]
    
    right = [[0] * (n + 1) for _ in range(n + 1)]
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            right[x][y] += right[x - 1][y - 1] + arr[x - 1][y - 1]
    
    left = [[0] * (n + 1) for _ in range(n + 1)]
    for x in range(1, n + 1):
        for y in range(n):
            left[x][y] += left[x - 1][y + 1] + arr[x - 1][y]
    
    result = -1000000
    for k in range(2, n + 1):
        for lx in range(n - k + 1):
            for ly in range(n - k + 1):
                rx, ry = lx + k, ly + k
                r = right[rx][ry] - right[lx][ly]
                l = left[rx][ly] - left[lx][ry]
                result = max(result, r - l)
                
    print(result)
    
solve()