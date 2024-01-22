import sys, math
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]
    
    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    tree[node] = LL ^ RR
    return tree[node]

def update(node, start, end, left, right, k):
    propagate(node, start, end)
    
    if end < left or right < start:
        return
    
    if left <= start and end <= right:
        lazy[node] ^= k
        propagate(node, start, end)
        return
    
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, k)
    update(node * 2 + 1, mid + 1, end, left, right, k)
    
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

def query(node, start, end, left, right):
    propagate(node, start, end)
    
    if end < left or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = query(node * 2, start, mid, left, right)
    RR = query(node * 2 + 1, mid + 1, end, left, right)
    
    return LL ^ RR

def propagate(node, start, end):
    if lazy[node]:
        # (A^k)^(B^k) = A^B^k^k = A^B^0 = A^B
        if start != end:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]
        
        if (end - start + 1) & 1:
            tree[node] ^= lazy[node]
        lazy[node] = 0

n = int(input())
array = list(map(int, input().split()))

width = 1 << (math.ceil(math.log2(n)) + 1)
tree = [ 0 ] * width
lazy = [ 0 ] * width

init(1, 0, n - 1)

q = int(input())
for _ in range(q):
    value = list(map(int, input().split()))
    
    if value[0] & 1:
        _, left, right, k = value
        update(1, 0, n-1, left, right, k)
    else:
        _, left, right = value
        print(query(1, 0, n-1, left, right))