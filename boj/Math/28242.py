n = int(input())
b2ac = (5*n*n + 10*n + 1) ** .5
x1 = (-(n+1) + b2ac) / (2 * n)
x2 = (-(n+1) - b2ac) / (2 * n)

for a in range(1, n+1):
    if n % a == 0:
        c = n // a
        b = -x1 * a
        d = -x2 * c
        if b != int(b) or d != int(d):
            continue
        
        if b * d == -(n + 2):
            print(a, int(b), c, int(d))
            exit(0)

print(-1)