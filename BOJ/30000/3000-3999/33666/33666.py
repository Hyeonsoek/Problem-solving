import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    p = [*map(int, input().split())]
    
    avglist = [x for x in p if x > 1]
    if not avglist:
        print(n, *([0] * (m - 1)))
        return
    
    avgn = len(avglist)
    avgsum = sum(avglist)
    avg = avgsum // avgn
    
    avgmax = max([x for x in p if x <= avg])
    
    if avgmax > m:
        print(-1)
        return

    counter = [0] * m
    for x in p:
        if x <= avg:
            counter[x - 1] += 1
    
    for i in reversed(range(m - 1)):
        counter[i] += counter[i + 1]
    
    for x in p:
        if x > avg:
            counter[0] += 1
    
    print(*counter)

solve()