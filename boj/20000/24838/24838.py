import sys
from collections import defaultdict
MOD = 10 ** 9 + 7
input = sys.stdin.readline
inputmap = lambda : map(int, input().split())

def solve():
    n, m = inputmap()
    arr = sorted([*inputmap()])
    
    prefix = [0 for _ in range(n + 2)]
    for _ in range(m):
        start, end = inputmap()
        prefix[start] += 1
        prefix[end + 1] -= 1
    
    for x in range(2, n + 2):
        prefix[x] += prefix[x - 1]
        
    counter = defaultdict(int)
    for x in range(1, n + 1):
        counter[prefix[x]] += 1
    
    case = 1
    summax = 0
    for count, value in sorted(counter.items(), reverse=True):
        for i in range(value):
            summax += count * arr.pop()
            case = case * (i + 1) % MOD
    
    print(summax, case)

for _ in range(int(input())):
    solve()