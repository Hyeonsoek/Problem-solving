import sys
from math import ceil, log2
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]
    
    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    tree[node] = LL + RR
    return tree[node]

def update(node, start, end, left, right, d):
    propagate(node, start, end)
    
    if right < start or end < left:
        return

    if left <= start and end <= right:
        lazy[node] += d
        propagate(node, start, end)
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, d)
    update(node * 2 + 1, mid + 1, end, left, right, d)
    
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
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        tree[node] += lazy[node] * (end - start + 1)
        lazy[node] = 0

n, m, k = map(int, input().split())
array = [ 0 ] + [int(input()) for _ in range(n)]

height = 1 << (ceil(log2(n)) + 1) + 1
tree = [ 0 ] * height
lazy = [ 0 ] * height

init(1, 1, n)

for _ in range(m + k):
    value = list(map(int, input().split()))
    
    if value[0] & 1:
        _, left, right, d = value
        update(1, 1, n, left, right, d)
    else:
        _, left, right = value
        print(query(1, 1, n, left, right))