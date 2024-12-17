MOD = 1000000007


class Matrix:
    def __init__(self, n, matrix=None):
        self.n = n
        self.matrix = matrix
        if matrix is None:
            self.matrix = [[0] * n for _ in range(n)]

    def __mul__(self, other):
        result = Matrix(self.n)
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    result.matrix[x][y] += (self.matrix[x][z] * other.matrix[z][y]) % MOD
                result.matrix[x][y] %= MOD
        return result


def fast(a, n):
    result = Matrix(a.n)
    for x in range(a.n):
        result.matrix[x][x] = 1

    while n > 0:
        if n & 1:
            result *= a
        a *= a
        n //= 2

    return result


def solve():
    k, n = map(int, input().split())
    arr = [[1] * x + [0] * (k + 2 - x) for x in range(1, k + 3)]
    matrix = fast(Matrix(k + 2, arr), n)
    print(matrix.matrix[k+1][0])


solve()