import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n:int) -> None:
        self.n = n
        self.array = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
        self.tree = [[0] * (n+1) for _ in range(n+1)]
        
        for y in range(1, self.n + 1):
            for x in range(1, self.n + 1):
                self.update(y, x, self.array[y][x])

    def update(self, y, x, value):
        while y <= self.n:
            px = x
            while px <= self.n:
                self.tree[y][px] += value
                px += px & -px
            y += y & -y
            
    def sum(self, y, x):
        result = 0
        while y > 0:
            px = x
            while px > 0:
                result += self.tree[y][px]
                px -= px & -px
            y -= y & -y
        return result
        
n, m = map(int, input().split())
fenwicktree = FenwickTree(n)

for _ in range(m):
    query = list(map(int, input().split()))
    
    if query[0]:
        w, y1, x1, y2, x2 = query
        result = fenwicktree.sum(y2, x2)
        result -= fenwicktree.sum(y2, x1 - 1)
        result -= fenwicktree.sum(y1 - 1, x2)
        result += fenwicktree.sum(y1 - 1, x1 - 1)
        print(result)
    else:
        w, y, x, c = query
        fenwicktree.update(y, x, c - fenwicktree.array[y][x])
        fenwicktree.array[y][x] = c