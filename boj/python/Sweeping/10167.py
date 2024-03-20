import sys
INF = -(10 ** 15)
input = sys.stdin.readline

class Node:
    def __init__(self, lmax=INF, rmax=INF, smax=INF, prefix=0):
        self.lmax = lmax
        self.rmax = rmax
        self.smax = smax
        self.prefix = prefix

    def __str__(self):
        return "prefix {}, lmax {}, rmax {}, smax {}".format(self.prefix, self.lmax, self.rmax, self.smax)

    def set(self, value):
        self.lmax = self.rmax = self.smax = self.prefix = value

def merge(left: Node, right: Node):
    lmax = max(left.lmax, left.prefix + right.lmax)
    rmax = max(right.rmax, right.prefix + left.rmax)
    smax = max(left.smax, right.smax, left.rmax + right.lmax)
    prefix = left.prefix + right.prefix
    return Node(lmax, rmax, smax, prefix)


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [Node() for _ in range(4 * n)]
        self.indexes = [0] * n
        self.order(1, 0, n - 1)

    def order(self, node, start, end):
        if start == end:
            self.indexes[start] = node
            return

        mid = (start + end) >> 1
        self.order(node << 1, start, mid)
        self.order(node << 1 | 1, mid + 1, end)

    def update(self, index, value):
        index = self.indexes[index]
        self.tree[index].set(self.tree[index].prefix + value)
        while index > 1:
            index >>= 1
            self.tree[index] = merge(self.tree[index << 1], self.tree[index << 1 | 1])

def solve():
    n = int(input())
    tree = SegmentTree(n)
    board = [[] for _ in range(n)]
    coordinates = [list(map(int, input().split())) for _ in range(n)]

    z = list(zip(*coordinates))
    xdicts = {xx: x for x, xx in enumerate(sorted(set(z[0])))}
    ydicts = {yy: x for x, yy in enumerate(sorted(set(z[1])))}

    for x, y, weight in coordinates:
        board[ydicts[y]].append((xdicts[x], weight))

    result = 0
    for s in range(n):
        tree = SegmentTree(n)
        for y in range(s, n):
            for index, weight in board[y]:
                tree.update(index, weight)
            result = max(result, tree.tree[1].smax)

    print(result)

solve()