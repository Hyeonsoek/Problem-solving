import sys
MAX = -sys.maxsize
input = sys.stdin.readline

class Node:
    def __init__(self, lmax=MAX, rmax=MAX, smax=MAX, prefix=0):
        self.lmax = lmax
        self.rmax = rmax
        self.smax = smax
        self.prefix = prefix
    
    def set(self, value):
        self.lmax = self.rmax = value
        self.smax = self.prefix = value

def merge(left: Node, right: Node):
    lmax = max(left.lmax, left.prefix + right.lmax)
    rmax = max(right.rmax, right.prefix + left.rmax)
    smax = max(left.smax, right.smax, left.rmax + right.lmax)
    prefix = left.prefix + right.prefix
    return Node(lmax, rmax, smax, prefix)

def query(tree, n, left, right):
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
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [Node() for _ in range(4 * n)]
    
    for x in range(n):
        tree[x + n].set(arr[x])

    for x in range(n - 1, 0, -1):
        tree[x] = merge(tree[x << 1], tree[x << 1 | 1])
    
    m = int(input())
    for _ in range(m):
        x1, y1, x2, y2 = map(lambda v: int(v) - 1, input().split())
        
        if y1 < x2:
            left = query(tree, n, x1, y1+1)
            mid = query(tree, n, y1+1, x2)
            right = query(tree, n, x2, y2+1)
            print(left.rmax + mid.prefix + right.lmax)
        else:
            left = query(tree, n, x1, x2)
            mid = query(tree, n, x2, y1+1)
            right = query(tree, n, y1+1, y2+1)
            
            result = max([
                left.rmax + mid.prefix + right.lmax,
                left.rmax + mid.lmax,
                mid.rmax + right.lmax,
                mid.smax
            ])
            print(result)
    
solve()