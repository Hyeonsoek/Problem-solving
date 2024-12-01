import sys
input = sys.stdin.readline

def solve():
    N, R = map(int, input().split())
    
    result = []
    for i in range(N):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        xp = (x1 + x2 + x3 + x4) / 4
        yp = (y1 + y2 + y3 + y4) / 4
        
        dist = ((xp - x1) ** 2 + (yp - y1) ** 2) ** .5
        distO = (xp ** 2 + yp ** 2) ** .5
        
        if distO - dist <= R:
            result.append(i)
    
    print(len(result))

solve()