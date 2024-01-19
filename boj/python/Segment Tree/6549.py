import sys
from math import ceil, log2
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def init(tree, array, node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    
    mid = (start + end) // 2
    LL = init(tree, array, node * 2, start, mid)
    RR = init(tree, array, node * 2 + 1, mid + 1, end)
    tree[node] = LL if array[LL] < array[RR] else RR
    return tree[node]

def _min(tree, array, node, start, end, left, right):
    if right < start or left > end:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = _min(tree, array, node * 2, start, mid, left, right)    
    RR = _min(tree, array, node * 2 + 1, mid + 1, end, left, right)
    
    if not LL:
        return RR
    
    if not RR:
        return LL
    
    return LL if array[LL] < array[RR] else RR

def dq(tree, array, n, left, right):
    index = _min(tree, array, 1, 1, n, left, right)
    area = array[index] * (right - left + 1)

    if left < index:
        area = max(area, dq(tree, array, n, left, index - 1))
    
    if index < right:
        area = max(area, dq(tree, array, n, index + 1, right))
        
    return area

while True:
    array = list(map(int, input().split()))
    
    if not array[0]:
        break
    
    n = array[0]
    tree = [0] * (1 << (ceil(log2(n)) + 1))
    
    init(tree, array, 1, 1, n)
    print(dq(tree, array, n, 1, n))