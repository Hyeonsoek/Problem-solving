import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = brray[start]
        return tree[node]
    
    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    
    tree[node] = LL + RR
    return tree[node]

def propagate(node, start, end):
    if lazy[node]:
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        
        tree[node] += (end - start + 1) * lazy[node]
        lazy[node] = 0
        
def update(node, start, end, left, right, k):
    propagate(node, start, end)
    
    if right < start or end < left:
        return
    
    if left <= start and end <= right:
        lazy[node] = k
        propagate(node, start, end)
        return
    
    mid = (start + end) >> 1
    update(node * 2, start, mid, left, right, k)
    update(node * 2 + 1, mid + 1, end, left, right, k)
    
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    
def query(node, start, end, left, right):
    propagate(node, start, end)
    
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = query(node * 2, start, mid, left, right)
    RR = query(node * 2 + 1, mid + 1, end, left, right)
    
    return LL + RR

n = int(input())
array = [ 0, *map(int, input().split()) ]
# b[x] = a[x] - a[x-1]
brray = [ 0, *(array[x+1] - array[x] for x in range(n)) ]

tree = [0] * (4 * n)
lazy = [0] * (4 * n)

init(1, 1, n)

m = int(input())

for _ in range(m):
    q, *a = map(int, input().split())
    
    if q & 1:
        l, r = a
        # [l, r] +1
        # => b[l] + b[l+1] + ... + b[r]
        # => a[l] + 1 - a[l-1] + (a[l+1] + 1) - a[l] + ... + a[r] + 1 - a[r-1]
        # => a[r] - a[l-1] + (l - r + 1)
        update(1, 1, n, l, r, 1)
        update(1, 1, n, r + 1, r + 1, -(r - l + 1))
    else:
        i, = a
        print(query(1, 1, n, 1, i))