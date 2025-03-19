import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    print('OUT' if sum(map(int, input().split())) - n < m else 'DIMI')

solve()