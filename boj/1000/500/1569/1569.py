def solve():
    n = int(input())
    point = [[*map(int, input().split())] for _ in range(n)]

    minx, maxx = 1000, -1000
    miny, maxy = 1000, -1000
    for x in range(n):
        px, py = point[x]
        minx = min(px, minx)
        maxx = max(px, maxx)
        miny = min(py, miny)
        maxy = max(py, maxy)
        
    def isinoutline(minx, maxx, miny, maxy):
        for x in range(n):
            px, py = point[x]
            if not ((px in [minx, maxx] and miny <= py <= maxy) or
                    (py in [miny, maxy] and minx <= px <= maxx)):
                return False
        return True
    
    xlength = maxx - minx
    ylength = maxy - miny
    
    if xlength == ylength:
        return xlength if isinoutline(minx, maxx, miny, maxy) else -1
                
    if xlength < ylength:
        gap = ylength - xlength
        result = isinoutline(minx - gap, maxx, miny, maxy) | isinoutline(minx, maxx + gap, miny, maxy)
        return ylength if result else -1
    
    gap = xlength - ylength
    result = isinoutline(minx, maxx, miny - gap, maxy) | isinoutline(minx, maxx, miny, maxy + gap)
    return xlength if result else -1

print(solve())