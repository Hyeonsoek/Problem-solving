import sys
input = lambda: sys.stdin.readline().split()

def solve():
    n, m, k = map(int, input())
    arr = set(map(int, input()))
    log = sorted([tuple(map(int, input())) for _ in range(m)])
    
    for x in range(1, n + 1):
        target = set([x])
        for y in range(m):
            tt, aa, bb = log[y]
            if aa in target:
                target.add(bb)
        
        if target == arr:
            return x

    return -1

print(solve())