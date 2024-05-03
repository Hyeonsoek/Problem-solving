import sys
sys.setrecursionlimit(2000000)

def sovle():
    n, m = map(int, input().split())
    arr = [[0] * 2 for _ in range(3)]
    for x in range(2):
        arr[0][x], arr[1][x], arr[2][x] = map(int, input().split())
    
    def brute(k, xx, value):
        if k == n:
            return 1 if value >= m else 0
        else:
            result = 0
            for x in range(3):
                for y in range(2):
                    next_value = value + arr[x][y] // (1 if xx != x else 2)
                    result += brute(k+1, x, next_value)
            return result
        
    return brute(0, -1, 0)
    
print(sovle())