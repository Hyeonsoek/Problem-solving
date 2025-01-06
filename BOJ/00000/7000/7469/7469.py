import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    tree = [[] for _ in range(4 * n)]
    
    def merge(node):
        left = tree[node << 1]
        right = tree[node << 1 | 1]
        p, q = 0, 0
        
        while p < len(left) and q < len(right):
            if left[p] < right[q]:
                tree[node].append(left[p])
                p += 1
            else:
                tree[node].append(right[q])
                q += 1
        
        if q == len(right):
            for x in range(p, len(left)):
                tree[node].append(left[x])
        else:
            for x in range(q, len(right)):
                tree[node].append(right[x])
    
    def build(node=1, start=0, end=n-1):
        if start == end:
            tree[node].append(arr[start])
            return
        
        mid = (start + end) >> 1
        build(node << 1, start, mid)
        build(node << 1 | 1, mid + 1, end)
        merge(node)
    
    def query(left, right, node=1, start=0, end=n-1):
        if right < start or end < left:
            return []
        
        if left <= start and end <= right:
            return tree[node]
    
        mid = (start + end) >> 1