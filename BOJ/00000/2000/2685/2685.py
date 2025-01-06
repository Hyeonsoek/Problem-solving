def solve():
    b, x, y = map(int, input().split())
    
    def nbase(nn, bb):
        base = []
        while nn > 0:
            base.append(nn % bb)
            nn //= bb
        return base[::-1]
    
    xx = nbase(x, b)
    yy = nbase(y, b)
    
    if len(xx) != len(yy):
        for _ in range(len(xx) - len(yy)):
            yy.insert(0, 0)
        for _ in range(len(yy) - len(xx)):
            xx.insert(0, 0)
    
    zz = [0] * len(xx)
    for i in range(len(xx)):
        zz[i] = (xx[i] + yy[i]) % b
    
    bb = 1
    result = 0
    for i in reversed(range(len(xx))):
        result += zz[i] * bb
        bb *= b
    
    print(result)

for _ in range(int(input())):
    solve()