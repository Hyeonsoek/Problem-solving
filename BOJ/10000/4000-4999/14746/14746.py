import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    C1, C2 = map(int, input().split())
    
    P = sorted(map(int, input().split()))
    Q = sorted(map(int, input().split()))
    
    minDist = sys.maxsize
    count = 0
    i, j = 0, 0
    while i < n and j < m:
        dist = abs(P[i] - Q[j])
        
        if minDist > dist:
            minDist = dist
            count = 0
        if minDist == dist:
            count += 1
        
        if P[i] > Q[j]:
            j += 1
        else:
            i += 1

    print(minDist + abs(C1 - C2), count)

solve()