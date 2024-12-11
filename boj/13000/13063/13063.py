import sys

def solve(n, m, k):
    if (n, m, k) == (0, 0, 0):
        return
    
    h = n // 2 + 1
    
    if k >= h:
        print(-1)
        return

    if h - m <= n - (m + k):
        print(max(0, h - m))
    else:
        print(-1)

for input in sys.stdin:
    solve(*map(int, input.split()))