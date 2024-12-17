import sys
from math import *
input = sys.stdin.readline

def FFT(f, w, n):
    if n == 1:
        return
    
    even = []
    odd = []
    for i in range(n):
        (odd if i & 1 else even).append(f[i])
    
    FFT(even, w * w, n // 2)
    FFT(odd, w * w, n // 2)
    
    wp = complex(1, 0)
    for i in range(n // 2):
        f[i] = even[i] + wp * odd[i]
        f[i + n // 2] = even[i] - wp * odd[i]
        wp *= w

def multiply(a : list, b : list):
    n = 1
    while n < len(a) + 1 or n < len(b) + 1:
        n *= 2
    n *= 2
    while len(a) < n:
        a.append(complex(0, 0))
    while len(b) < n:
        b.append(complex(0, 0))
    c = [complex(0, 0) for _ in range(n)]
    w = complex(cos(2 * pi / n), sin(2 * pi / n))
    
    FFT(a, w, n)
    FFT(b, w, n)
    
    for i in range(n):
        c[i] = a[i] * b[i]
    
    FFT(c, complex(1,0) / w, n)
    for i in range(n):
        c[i] /= complex(n, 0)
        c[i] = complex(round(c[i].real), round(c[i].imag))
    
    return c

def solve():
    n = int(input())
    X = [*map(int, input().split())]
    Y = [*map(int, input().split())][::-1]
    
    X.extend(X)
    Y.extend([0] * n)
    
    Z = multiply(X, Y)
    
    result = 0
    for i in range(n-1, 2*n-2):
        result = max(result, int(Z[i].real))
    
    print(result)
    
solve()