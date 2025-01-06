import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0, *map(int, input().split())]
    k = int(input())
    
    for x in range(1, n + 1):
        xa = x - 1
        ya, yb = arr[x-1], arr[x]
        if ya == (yb - ya) * xa and (yb - ya) == k:
            return 'T'
        
        xx = ((yb - ya) * xa - ya) / (yb - ya - k) if (yb - ya - k) != 0 else 0
        if xx != 0 and (x - 1 <= xx <= x):
            return 'T'
    
    return 'F'

print(solve())