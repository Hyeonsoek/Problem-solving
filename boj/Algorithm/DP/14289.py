import sys
input = sys.stdin.readline

class Matrix:
    MOD = 1000000007

    def __init__(self, n, matrix=None):
        self.n = n
        if matrix is None:
            self.matrix = [[0] * n for _ in range(n)]
        else:
            self.matrix = matrix

    def __mul__(self, other):
        result = Matrix(self.n)
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    result.matrix[x][y] += (self.matrix[x][z] * other.matrix[z][y]) % Matrix.MOD
                result.matrix[x][y] %= Matrix.MOD

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
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a-1][b-1] = 1
        arr[b-1][a-1] = 1

    matrix = Matrix(n, arr)
    result = fast(matrix, int(input()))
    print(result.matrix[0][0])


solve()