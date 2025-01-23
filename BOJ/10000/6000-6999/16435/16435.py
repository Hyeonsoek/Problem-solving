import sys
input = sys.stdin.readline

def solve():
    n, l = map(int, input().split())
    h = sorted(map(int, input().split()))
    
    for i in h:
        if i <= l:
            l += 1
    print(l)

solve()