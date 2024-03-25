from math import log2, ceil
MOD = 1000000007

class Matrix:
    def __init__(self, m, arr=None):
        self.m = m
        if arr:
            self.arr = arr
        else:
            self.arr = [[0] * m for _ in range(m)]
    
    def __mul__(self, other):
        result = Matrix(self.m)
        for x in range(self.m):
            for y in range(self.m):
                for z in range(self.m):
                    value = (self.arr[x][z] * other.arr[z][y]) % MOD
                    result.arr[x][y] = (result.arr[x][y] + value) % MOD
        
        return result
    
def fast(a, n):
    result = Matrix(a.m)
    for x in range(a.m):
        result.arr[x][x] = 1
    
    pows = [a]
    counts = ceil(log2(n)) + 1
    for x in range(counts):
        pows.append(pows[-1] * pows[-1])
    
    for x in range(counts):
        if n & (1 << x):
            result *= pows[x]
    
    return result

def solve():
    n, m = map(int, input().split())
    arr = [[0] * m for _ in range(m)]
    arr[0][0] = 1
    arr[0][m-1] = 1
    for x in range(1, m):
        arr[x][x-1] = 1
    
    matrix = fast(Matrix(m, arr), n)
    print(matrix.arr[0][0])

solve()