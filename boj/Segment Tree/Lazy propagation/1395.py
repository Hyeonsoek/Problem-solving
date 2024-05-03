import sys, math
input = sys.stdin.readline

def update(node, start, end, left, right):
    propagate(node, start, end)
    
    if right < start or end < left:
        return
    
    if left <= start and end <= right:
        lazy[node] ^= 1
        propagate(node, start, end)
        return
    
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right)
    update(node * 2 + 1, mid + 1, end, left, right)
    
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

def propagate(node, start, end):
    if lazy[node]:
        if start != end:
            lazy[node * 2] ^= 1
            lazy[node * 2 + 1] ^= 1

            mid = (start + end) // 2
            count = 0
            if lazy[node * 2]:
                count += mid - start + 1 - tree[node * 2]
            else:
                count += tree[node * 2]
            
            if lazy[node * 2 + 1]:
                count += end - mid - tree[node * 2 + 1]
            else:
                count += tree[node * 2 + 1]
                
            tree[node] = count
        else:
            tree[node] ^= 1
        
        lazy[node] = 0

n, m = map(int, input().split())

width = 1 << (math.ceil(math.log2(n)) + 1) + 1

tree = [ 0 ] * width
lazy = [ 0 ] * width

for _ in range(m):
    o, s, t = map(int, input().split())
    
    if o:
        print(query(1, 1, n, s, t))
    else:
        update(1, 1, n, s, t)