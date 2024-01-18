import sys
from math import ceil, log2
input = sys.stdin.readline

n = int(input())
array = [0] + [ int(input()) for _ in range(n) ]
tree = [0] * (1 << (ceil(log2(n)) + 1))

def init(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]
    
    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    tree[node] = LL + RR
    
    return tree[node]

def update(node, start, end, index, value):
    if index < start or end < index:
        return
    
    tree[node] += value
    
    if start < end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, value)
        update(node * 2 + 1, mid + 1, end, index, value)

def sum(node, start, end, left, right):
    if end < left or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = sum(node * 2, start, mid, left, right)
    RR = sum(node * 2 + 1, mid + 1, end, left, right)
    
    return LL + RR

pos = { y : x for x, y in enumerate(array) }

init(1, 1, n)

for x in range(1, n + 1):
    if x & 1:
        x = x // 2 + 1
        print(sum(1, 1, n, 1, pos[x] - 1))
        update(1, 1, n, pos[x], -1)
    else:
        x = n - (x // 2) + 1
        print(sum(1, 1, n, pos[x] + 1, n))
        update(1, 1, n, pos[x], -1)