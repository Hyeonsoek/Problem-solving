def solve():
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    
    if (xb - xa) * (yc - yb) == (xc - xb) * (yb - ya):
        return -1
    
    dist = lambda xa, ya, xb, yb : ((xa - xb) ** 2 + (ya - yb) ** 2) ** .5

    ab = dist(xa, ya, xb, yb)
    bc = dist(xb, yb, xc, yc)
    ca = dist(xc, yc, xa, ya)
    
    d = [(ab + bc) * 2, (bc + ca) * 2, (ca + ab) * 2]

    return max(d) - min(d)

print(solve())