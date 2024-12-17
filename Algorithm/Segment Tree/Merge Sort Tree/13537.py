import sys
from bisect import bisect_right
input = sys.stdin.readline

class MergeSortTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.tree = [[] for _ in range(4*n)]

        self.build(1, 0, n - 1)

    def merge(self, node):
        left = self.tree[node << 1]
        right = self.tree[node << 1 | 1]
        p, q = 0, 0

        while p < len(left) and q < len(right):
            if left[p] < right[q]:
                self.tree[node].append(left[p])
                p += 1
            else:
                self.tree[node].append(right[q])
                q += 1

        if q == len(right):
            for x in range(p, len(left)):
                self.tree[node].append(left[x])
        else:
            for x in range(q, len(right)):
                self.tree[node].append(right[x])

    def build(self, node, start, end):
        if start == end:
            self.tree[node].append(self.arr[start])
            return

        mid = (start + end) // 2
        self.build(node << 1, start, mid)
        self.build(node << 1 | 1, mid + 1, end)

        self.merge(node)

    def query(self, node, start, end, left, right, k):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return len(self.tree[node]) - bisect_right(self.tree[node], k)

        mid = (start + end) // 2
        LL = self.query(node << 1, start, mid, left, right, k)
        RR = self.query(node << 1 | 1, mid + 1, end, left, right, k)
        return LL + RR

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    tree = MergeSortTree(n, arr)

    qn = int(input())
    for _ in range(qn):
        left, right, k = map(int, input().split())
        print(tree.query(1, 0, n - 1, left - 1, right - 1, k))

solve()