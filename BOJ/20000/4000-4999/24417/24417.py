MOD=10**9+7

def m(a, b):
    c=[[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j])%MOD
    return c

def f(a, n):
    c=[[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            c = m(c, a)
        a = m(a, a)
        n >>= 1
    return c

n = int(input())
c = f([[1, 1], [1, 0]], n)
print(c[1][0], n - 2)