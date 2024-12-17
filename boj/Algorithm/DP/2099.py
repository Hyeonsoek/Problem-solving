import sys
input = sys.stdin.readline

class Matrix:
    def __init__(self, n, arr=None):
        self.n = n
        if arr:
            self.arr = arr
        else:
            self.arr = [[False] * n for _ in range(n)]

    def __mul__(self, other):
        result = Matrix(self.n)
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    result.arr[x][y] |= (self.arr[x][z] & other.arr[z][y])
                    
        return result
    
def fast(a, n):
    result = Matrix(a.n)
    for x in range(a.n):
        result.arr[x][x] = True
    
    pows = [a]
    for x in range(20):
        pows.append(pows[-1] * pows[-1])
    
    for x in range(21):
        if n & (1 << x):
            result = result * pows[x]
    
    return result
    
def solve():
    n, k, m = map(int, input().split())
    board = [[False] * n for _ in range(n)]
    
    for x in range(n):
        for y in map(int, input().split()):
            board[x][y - 1] = True
    
    matrix = Matrix(n, board)
    matrix = fast(matrix, k)
    
    for _ in range(m):
        a, b = map(int, input().split())
        print("death" if matrix.arr[a-1][b-1] else "life")
        
solve()