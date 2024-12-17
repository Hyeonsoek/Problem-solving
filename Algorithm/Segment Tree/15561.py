import sys
INF = -sys.maxsize
input = sys.stdin.readline

class Node:
    def __init__(self, lmax=INF, rmax=INF, smax=INF, prefix=0):
        self.lmax = lmax
        self.rmax = rmax
        self.smax = smax
        self.prefix = prefix

    def set(self, value):
        self.lmax = self.rmax = self.smax = self.prefix = value

def merge(left: Node, right: Node):
    lmax = max(left.lmax, left.prefix + right.lmax)
    rmax = max(right.rmax, right.prefix + left.rmax)
    smax = max(left.smax, right.smax, left.rmax + right.lmax)
    prefix = left.prefix + right.prefix
    return Node(lmax, rmax, smax, prefix)

def init(tree, arr, n):
    for x in range(n):
        tree[x+n].set(arr[x])

    for x in range(n-1, 0, -1):
        tree[x] = merge(tree[x << 1], tree[x << 1 | 1])

def update(tree, index, value, n):
    tree[index + n].set(value)

    index += n
    while index > 1:
        index >>= 1
        tree[index] = merge(tree[index << 1], tree[index << 1 | 1])

def query(tree, left, right, n):
    LL = Node()
    RR = Node()
    left += n
    right += n

    while left < right:
        if left & 1:
            LL = merge(LL, tree[left])
            left += 1

        if right & 1:
            right -= 1
            RR = merge(tree[right], RR)

        left >>= 1
        right >>= 1

    return merge(LL, RR)

def solve():
    n, q, u, v = map(int, input().split())
    arr = list(map(lambda xx: u * int(xx) + v, input().split()))
    tree = [Node() for _ in range(4*n)]

    init(tree, arr, n)

    for x in range(q):
        qq, a, b = map(int, input().split())

        if qq & 1:
            update(tree, a-1, b * u + v, n)
        else:
            print(query(tree, a-1, b, n).smax - v)

solve()