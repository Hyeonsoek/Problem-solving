import sys
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

def propagate(node, start, end):
    if lazy[node]:
        if start != end:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]
        
        if (end - start + 1) & 1:
            tree[node] ^= lazy[node]
        lazy[node] = 0
        
def update(node, start, end, left, right, k):
    propagate(node, start, end)
    
    if right < start or end < left:
        return
    
    if left <= start and end <= right:
        lazy[node] ^= k
        propagate(node, start, end)
        return
    
    mid = (start + end) >> 1
    update(node * 2, start, mid, left, right, k)
    update(node * 2 + 1, mid + 1, end, left, right, k)
    
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]
    
def query(node, start, end, index):
    propagate(node, start, end)
    
    if index < start or end < index:
        return 0
    
    if start == end:
        return tree[node]
    
    mid = (start + end) // 2
    if index <= mid:
        return query(node * 2, start, mid, index)
    else:
        return query(node * 2 + 1, mid + 1, end, index)
    

n = int(input())
array = list(map(int, input().split()))

tree = [0] * (4 * n)
lazy = [0] * (4 * n)

init(1, 0, n-1)

m = int(input())
for _ in range(m):
    q, *a = map(int, input().split())
    
    if q & 1:
        left, right, c = a
        update(1, 0, n-1, left, right, c)
    else:
        index, = a
        print(query(1, 0, n-1, index))