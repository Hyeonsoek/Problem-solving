def solve():
    h_lo, h_hi = map(int, input().split())
    s_lo, s_hi = map(int, input().split())
    v_lo, v_hi = map(int, input().split())
    r, g, b = map(int, input().split())
    
    M = max(r, g, b)
    m = min(r, g, b)
    
    V = M
    S = 255 * (V - m) / V
    
    if V == r:
        H = 60 * (g - b) / (V - m)
    elif V == g:
        H = 60 * (b - r) / (V - m) + 120
    else:
        H = 60 * (r - g) / (V - m) + 240
        
    if H < 0:
        H += 360
    
    if h_lo <= H <= h_hi and s_lo <= S <= s_hi and v_lo <= V <= v_hi:
        return "Lumi will like it."
    
    return "Lumi will not like it."

print(solve())