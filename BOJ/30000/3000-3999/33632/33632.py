def solve():
    w1, h1 = map(int, input().split())
    px, py = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    
    if py < y1:
        return 0.0
    
    w2 = w1 * (py - y1) / py
    x3 = px * y1 / py
    x4 = w1 + ((px - w1) * y1 / py)
    
    if x2 <= x3 or x4 <= x1:
        return 0.0
    
    if x1 <= x3 < x4 <= x2:
        return 1.0
    
    if x3 <= x1 < x2 <= x4:
        return min(1.0, (x2 - x1) / w2)
    
    if x1 <= x3 <= x2 <= x4:
        return min(1.0, (x2 - x3) / w2)
    
    if x3 <= x1 <= x4 <= x2:
        return min(1.0, (x4 - x1) / w2)

print(f'{solve():0.6f}')