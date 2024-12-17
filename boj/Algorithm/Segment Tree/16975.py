import sys
from math import ceil, log2
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))
tree = [0] * (1 << ceil(log2(n) + 1))

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return
    
    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)

def query(node, start, end, index):
    if index < start or end < index:
        return 0
    
    if start == end:
        return tree[node]
    
    mid = (start + end) // 2
    LL = query(node * 2, start, mid, index)
    RR = query(node * 2 + 1, mid + 1, end, index)
    return LL + RR + tree[node]
    
def update(node, start, end, left, right, value):
    if right < start or end < left:
        return
    
    if left <= start and end <= right:
        tree[node] += value
        return
    
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, value)
    update(node * 2 + 1, mid + 1, end, left, right, value)

init(1, 1, n)

m = int(input())
for _ in range(m):
    qq = list(map(int, input().split()))

    if qq[0] & 1:
        _, i, j, k = qq
        update(1, 1, n, i, j, k)
        # print(tree)
    else:
        _, x = qq
        print(query(1, 1, n, x))