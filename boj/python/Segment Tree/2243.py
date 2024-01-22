import sys
from math import ceil, log2
MAX = 1000000
HEIGHT = ceil(log2(MAX)) + 1
input = sys.stdin.readline

def update(node, start, end, index, value):
    if index < start or end < index:
        return
    
    tree[node] += value
    
    if start < end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, value)
        update(node * 2 + 1, mid + 1, end, index, value)

def query(node, start, end, count):
    if start == end:
        return start
    
    mid = (start + end) // 2
    LL = tree[node * 2]
    
    if count <= LL:
        return query(node * 2, start, mid, count)
    
    return query(node * 2 + 1, mid + 1, end, count - LL)

tree = [ 0 ] * (1 << HEIGHT + 1)

q = int(input())
for _ in range(q):
    value = list(map(int, input().split()))
    
    if value[0] & 1:
        _, index = value
        result = query(1, 1, MAX, index)
        print(result)
        update(1, 1, MAX, result, -1)
    else:
        _, index, count = value
        update(1, 1, MAX, index, count)