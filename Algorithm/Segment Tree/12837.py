import sys
from math import ceil, log2
input = sys.stdin.readline

class SegTree:
    def __init__(self, n:int):
        self.n = n
        self.height = ceil(log2(n)) + 1
        self.tree = [ 0 ] * (1 << self.height + 1)
        
    def update(self, index, diff):
        self._update(1, 1, self.n, index, diff)
        
    def sum(self, left, right):
        return self._sum(1, 1, self.n, left, right)
        
    def _update(self, node, start, end, index, diff):
        if index < start or end < index:
            return
        self.tree[node] += diff
        if start < end:
            mid = (start + end) // 2
            self._update(node * 2, start, mid, index, diff)
            self._update(node * 2 + 1, mid + 1, end, index, diff)
        
    def _sum(self, node, start, end, left, right):
        if end < left or right < start:
            return 0
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        LL = self._sum(node * 2, start, mid, left, right)
        RR = self._sum(node * 2 + 1, mid + 1, end, left, right)
        
        return LL + RR
    
n, m = map(int, input().split())
segtree = SegTree(n)

for _ in range(m):
    q, p, x = map(int, input().split())
    
    if q & 1:
        segtree.update(p, x)
    else:
        print(segtree.sum(p, x))