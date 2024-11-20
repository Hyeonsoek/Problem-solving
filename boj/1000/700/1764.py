from sys import stdin
input = stdin.readline

def solve():
    n, m = map(int, input().split())
    h = set(input().strip() for _ in range(n))
    s = set(input().strip() for _ in range(m))
    hs = sorted(list(h & s))
    print(len(hs))
    for x in hs:
        print(x)

solve()