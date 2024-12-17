import sys
input = sys.stdin.readline

class Node:
    def __init__(self, max=0, vmax=0):
        self.max = max
        self.vmax = vmax

    def set(self, value):
        self.max = self.vmax = value


def merge(left: Node, right: Node):
    mx = max(left.max, right.max, left.vmax + right.vmax)
    vmax = max(left.vmax, right.vmax)
    return Node(max=mx, vmax=vmax)


class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.tree = [Node() for _ in range(2*n)]

        for x in range(n):
            self.tree[x+n].set(arr[x])

        for x in range(n-1, 0, -1):
            self.tree[x] = merge(self.tree[x << 1], self.tree[x << 1 | 1])

    def update(self, index, value):
        self.tree[index + self.n].set(value)

        index += self.n
        while index > 1:
            index >>= 1
            self.tree[index] = merge(self.tree[index << 1], self.tree[index << 1 | 1])

    def query(self, left, right):
        LL = Node()
        RR = Node()

        left += self.n
        right += self.n

        while left < right:
            if left & 1:
                LL = merge(LL, self.tree[left])
                left += 1

            if right & 1:
                right -= 1
                RR = merge(self.tree[right], RR)

            left >>= 1
            right >>= 1

        return merge(LL, RR)

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    tree = SegmentTree(n, arr)

    qn = int(input())
    for _ in range(qn):
        q, a, b = map(int, input().split())

        if q & 1:
            tree.update(a-1, b)
        else:
            print(tree.query(a-1, b).max)

solve()