import sys
MAX = 400001
input = sys.stdin.readline

def solve():
    w, n = map(int, input().split())
    A = [*map(int, input().split())]
    
    ai = [-1] * MAX
    aj = [-1] * MAX
    for i in range(n - 1):
        for j in range(i + 1, n):
            p = A[i] + A[j]
            if ai[p] == -1:
                ai[p] = i
                aj[p] = j
    
    for k in range(n - 1):
        for l in range(k + 1, n):
            r = w - A[k] - A[l]
            if 0 <= r < MAX and ai[r] >= 0:
                i = ai[r]
                j = aj[r]
                if i != k and i != l and j != k and j != l:
                    return "YES"
    
    return "NO"

print(solve())