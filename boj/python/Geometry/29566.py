def solve():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    r1, r2, r3 = map(int, input().split())

    dx12 = x2 - x1
    dy12 = y2 - y1
    dx23 = x3 - x2
    dy23 = y3 - y2
    
    dxx12 = x2*x2 - x1*x1
    dxx23 = x3*x3 - x2*x2
    dyy12 = y2*y2 - y1*y1
    dyy23 = y3*y3 - y2*y2
    
    rr12 = r2*r2 - r1*r1
    rr23 = r3*r3 - r2*r2
    
    circle1 = (-rr23 + dxx23 + dyy23)
    circle2 = (-rr12 + dxx12 + dyy12)
    
    x_upper = dy12 * circle1 - dy23 * circle2
    x_under = 2 * (dy12*dx23 - dy23*dx12)
    
    y_upper = dx12 * circle1 - dx23 * circle2
    y_under = 2 * (dx12*dy23 - dx23*dy12)
    
    x = x_upper / x_under
    y = y_upper / y_under
    
    result = abs((x1 - x) * (x1 - x) + (y1 - y) * (y1 - y) - r1 * r1)

    if result < 1e-6:
        return str(x) + " " + str(y)
    return "Impossible"

print(solve())

#(A'-A)x + (B'-B)y + C'-C=0
#(A''-A')x + (B''-B')y + C''-C'=0
#(A''-A)x + (B''-B)y + C''-B=0