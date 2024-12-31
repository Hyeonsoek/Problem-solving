import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    
    if N == 2 and K == 1:
        print(1, 2)
        return
    
    if N >= 2:
        print(-1)
        return
    
    print(*[1] * K)

solve()