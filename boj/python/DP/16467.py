import sys
MOD = 100000007
input = sys.stdin.readline

def mult(a, b, n):
    result = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                result[x][y] += a[x][z] * b[z][y]
            result[x][y] %= MOD
    
    return result

def fast(a, n, size):
    if n == 1:
        return a
    x = fast(a, n // 2, size)
    xx = mult(x, x, size)
    return mult(xx, a, size) if n % 2 else xx

def solve():
    k, n = map(int, input().split())
    mat = [[0] * (k + 1) for _ in range(k + 1)]
    mat[0][0] += 1
    mat[0][k] += 1
    for x in range(1, k + 1):
        mat[x][x - 1] = 1
    
    mat = fast(mat, n, k + 1)
    return mat[0][0]
    
t = int(input())
for _ in range(t):
    sys.stdout.write(f'{solve()}\n')