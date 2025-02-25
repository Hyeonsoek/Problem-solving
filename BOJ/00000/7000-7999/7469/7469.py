import sys
from bisect import bisect_right
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
    
    def query(left, right, k, node=1, start=0, end=n-1):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return bisect_right(tree[node], k)

        mid = (start + end) // 2
        LL = query(left, right, k, node << 1, start, mid)
        RR = query(left, right, k, node << 1 | 1, mid + 1, end)
        return LL + RR
    
    build()
    arr.sort()
    
    for _ in range(m):
        i, j, k = map(lambda x: int(x) - 1, input().split())
        low = -10 ** 9
        high = 10 ** 9
        while low <= high:
            mid = (low + high) >> 1
            q = query(i, j, mid)
            
            if k < q:
                high = mid - 1
            else:
                low = mid + 1
        
        print(low)

solve()