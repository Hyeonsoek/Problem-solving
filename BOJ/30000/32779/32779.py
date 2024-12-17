import sys
input = sys.stdin.readline

def solve():
    q = int(input())
    for _ in range(q):
        a, m = map(int, input().split())
        print(int(1056*a*m/600000))

solve()