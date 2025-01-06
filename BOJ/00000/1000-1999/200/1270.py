import sys
from collections import Counter
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    n = int(input())
    for _ in range(n):
        t, *arr = map(int, input().split())
        counter = Counter(arr)
        for key, value in counter.items():
            if value / t > 0.5:
                output(f'{key}\n')
                break
        else:
            output("SYJKGW\n")
            
solve()