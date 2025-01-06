import sys
input = sys.stdin.readline

def solve():
    k = int(input())
    c = int(input())
    for _ in range(c):
        m, n = map(int, input().split())
        r = k - max(m, n)
        d = abs(m - n)
        
        if not d:
            print(1)
        else:
            if m > n:
                print(int(d - r <= 2))
            else:
                print(int(d - r <= 1))

solve()