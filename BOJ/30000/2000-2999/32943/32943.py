import sys
input = sys.stdin.readline

def solve():
    x, c, k = map(int, input().split())
    log = [[*map(int, input().split())] for _ in range(k)]
    log.sort()
    
    data = {}
    datarev = {}
    for i in range(k):
        t, s, n = log[i]
        if s not in data:
            if n in datarev:
                del data[datarev[n]]
            data[s] = n
            datarev[n] = s
    
    for i, s in sorted(datarev.items()):
        print(i, s)

solve()