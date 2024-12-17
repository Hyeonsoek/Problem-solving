from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    sx, sy, ex, ey = map(int, input().split())
    
    n = int(input())
    count = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        
        rsquare = r ** 2
        distance_s = (sx - x) ** 2 + (sy - y) ** 2
        distance_e = (ex - x) ** 2 + (ey - y) ** 2
        
        if distance_e < rsquare and distance_s < rsquare:
            continue
        
        if distance_e > rsquare and distance_s > rsquare:
            continue
        
        count += 1
    
    print(count)