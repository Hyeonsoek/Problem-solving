import sys, math
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    lines = defaultdict(int)

    for _ in range(n):
        x, y = map(int, input().split())
        lines[math.atan2(y, x)] += 1

    print(max(lines.values()))

solve()